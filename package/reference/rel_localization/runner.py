"""Predict from declared inputs, then score separately. Metadata is not provenance proof."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ.setdefault(key,'1')
from pathlib import Path
import json,time,copy
import numpy as np
from . import frozen_filter
from .engine import Engine
HERE=Path(__file__).resolve().parent
SEMANTICS={'motion':'planar_unicycle','distance_unit':'metre','angle_unit':'radian','clock':'source_time_seconds','odometry_origin':'independent_measurement','measurement_origin':'independent_range_bearing','identity_availability':'causal','map_availability':'before_scored_period','initialization':'provided_at_start'}
FIELDS={'schema','semantics','duration','initial','odometry','observations','landmarks'}
METHODS={f'J{k}':json.loads((HERE/f'J{k}.json').read_text(encoding='utf8')) for k in (1,2)}

def normalize(packet):
    if type(packet)!=dict or set(packet)!=FIELDS or packet['schema']!='planar-range-bearing-v1':raise ValueError('input fields/schema; reference truth is not a prediction input')
    if packet['semantics']!=SEMANTICS:raise ValueError('incompatible or unqualified declared semantics')
    duration=float(packet['duration']);initial=np.asarray(packet['initial'],dtype=float)
    od=np.asarray(packet['odometry'],dtype=float);obs=np.asarray(packet['observations'],dtype=float)
    if obs.size==0:obs=np.empty((0,4))
    if not np.isfinite(duration) or not .5<duration<=86400 or initial.shape!=(3,) or not np.isfinite(initial).all():raise ValueError('duration/initial')
    if od.ndim!=2 or od.shape[1]!=3 or not len(od) or obs.ndim!=2 or obs.shape[1]!=4:raise ValueError('odometry/observation shape')
    if max(len(od),len(obs))>2000000 or not np.isfinite(od).all() or not np.isfinite(obs).all():raise ValueError('size/nonfinite input')
    if od[0,0]!=0 or any(np.any(np.diff(a[:,0])<0) or np.any(a[:,0]<0) or np.any(a[:,0]>duration) for a in (od,obs)):raise ValueError('time order/support; initial control must be available at zero')
    if not -np.pi<=initial[2]<=np.pi or np.any(np.abs(obs[:,3])>np.pi) or np.any(obs[:,2]<=0):raise ValueError('angle/range units')
    if type(packet['landmarks'])!=dict or not packet['landmarks']:raise ValueError('landmark map')
    lm={}
    for k,v in packet['landmarks'].items():
        if not isinstance(k,str) or not k.isdigit() or str(int(k))!=k or int(k)<=0:raise ValueError('landmark identity')
        a=np.asarray(v,dtype=float)
        if a.shape!=(2,) or not np.isfinite(a).all():raise ValueError('landmark coordinates')
        lm[int(k)]=a
    if any(int(k)!=k or int(k) not in lm for k in obs[:,1]):raise ValueError('unknown or noninteger observed landmark')
    return {'duration':duration,'initial':initial.copy(),'odometry':od.copy(),'observations':obs.copy(),'landmarks':lm}

def predict(packet,checkpoints=None,stop_at=None):
    """Replay a bound input record causally; restart requires the same complete record.

    This is not a qualified live sensor service. Entire supplied records are bound
    by hash, while the arithmetic consumes only events up to each output time.
    """
    st=time.perf_counter();r=normalize(packet)
    if checkpoints is not None and set(checkpoints)!={'robust','J1','J2'}:raise ValueError('complete bank checkpoints required')
    if stop_at is not None and (not np.isfinite(stop_at) or stop_at<.5 or stop_at>=r['duration'] or stop_at*2!=int(stop_at*2)):raise ValueError('stop_at must be a half-second endpoint inside the record')
    if checkpoints is not None:
        times=[]
        for cp in checkpoints.values():
            if type(cp)!=dict or not isinstance(cp.get('t'),(int,float)) or not np.isfinite(cp['t']):raise ValueError('checkpoint time')
            for field,shape in (('x',(3,)),('p',(3,3)),('ema',(2,)),('mean',(2,)),('lastq',(2,))):
                value=np.asarray(cp.get(field),dtype=float)
                if value.shape!=shape or not np.isfinite(value).all():raise ValueError('checkpoint state shape/finite: '+field)
            rows=np.asarray(cp.get('rows'),dtype=float)
            if rows.ndim!=2 or rows.shape[1]!=8 or not len(rows) or not np.isfinite(rows).all() or np.any(np.diff(rows[:,0])<=0) or rows[-1,0]!=cp['t']:raise ValueError('checkpoint row/time consistency')
            if not .5<=cp['t']<r['duration'] or cp['t']*2!=int(cp['t']*2):raise ValueError('checkpoint endpoint')
            if stop_at is not None and stop_at<=cp['t']:raise ValueError('stop_at must advance the saved checkpoint')
            times.append(cp['t'])
        if len(set(times))!=1:raise ValueError('bank checkpoints must share a time')
    outputs={};saved={};counts={};costs={}
    for name in ('robust','J1','J2'):
        e=None if name=='robust' else Engine(METHODS[name]);config=frozen_filter.CONFIGS['robust' if name=='robust' else 'fixed'];before=time.perf_counter()
        z=frozen_filter.run(r,config,e,keep=True,checkpoint=copy.deepcopy(checkpoints[name]) if checkpoints else None,stop_at=stop_at)
        costs[name]=time.perf_counter()-before;rows=np.array(z['checkpoint']['rows'])
        if rows.ndim!=2 or rows.shape[1]!=8 or not np.isfinite(rows).all():raise ValueError('invalid prediction rows')
        outputs[name]=rows[:,:4];saved[name]=z['checkpoint'];counts[name]={'observations_consumed':z['measurements'],'rejected':z['rejected'],'engine_calls_this_invocation':e.calls if e else 0}
    for name in ('J1','J2'):
        a,b=outputs['robust'],outputs[name]
        if not np.array_equal(a[:,0],b[:,0]):raise ValueError('unaligned bank')
        mean=(a+b)/2;sy=np.sin(a[:,3])+np.sin(b[:,3]);cx=np.cos(a[:,3])+np.cos(b[:,3]);mean[:,3]=np.where(np.hypot(sy,cx)<=1e-12,a[:,3],np.arctan2(sy,cx));outputs[name+'-mean']=mean
    return {'poses':{k:v.tolist() for k,v in outputs.items()},'checkpoints':saved,'counts':counts,'filter_wall_seconds':costs,'whole_prediction_wall_seconds':time.perf_counter()-st,'scope':'Three frozen filters and two means; one shared robust path. Metadata assertions do not authenticate provenance.'}

def evaluate(poses,reference):
    """Offline time-aligned scoring; rejects absent support instead of extrapolating."""
    gt=np.asarray(reference,dtype=float)
    if gt.ndim!=2 or gt.shape[1]!=4 or len(gt)<2 or not np.isfinite(gt).all() or np.any(np.diff(gt[:,0])<=0):raise ValueError('invalid reference')
    result={}
    for name,raw in poses.items():
        a=np.asarray(raw,dtype=float)
        if a.ndim!=2 or a.shape[1]!=4 or not len(a) or not np.isfinite(a).all() or np.any(np.diff(a[:,0])<=0):raise ValueError('invalid poses')
        if a[0,0]<gt[0,0] or a[-1,0]>gt[-1,0]:raise ValueError('reference support missing')
        truth=np.column_stack([np.interp(a[:,0],gt[:,0],gt[:,k]) for k in (1,2)]+[np.interp(a[:,0],gt[:,0],np.unwrap(gt[:,3]))]);d=np.linalg.norm(a[:,1:3]-truth[:,:2],axis=1);ang=(a[:,3]-truth[:,2]+np.pi)%(2*np.pi)-np.pi;over=d>.5
        result[name]={'samples':len(a),'mse_m2':float(np.mean(d*d)),'rmse_m':float(np.sqrt(np.mean(d*d))),'above_0_5m':int(over.sum()),'episodes':int(np.sum(over & ~np.r_[False,over[:-1]])),'p95_m':float(np.quantile(d,.95)),'max_m':float(d.max()),'heading_rmse_rad':float(np.sqrt(np.mean(ang*ang)))}
    return result
