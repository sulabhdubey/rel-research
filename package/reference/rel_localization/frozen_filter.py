import time,json,hashlib
import numpy as np,math
TAU=2*math.pi
def wrap(x):return (x+math.pi)%TAU-math.pi
def motion(x,p,v,w,dt,qv=1.,qw=1.):
    if dt<=0:return x,p
    half=.5*w*dt;s=math.sin(half)/half if abs(half)>1e-8 else 1-half*half/6
    a=x[2]+half;dx=v*dt*s*math.cos(a);dy=v*dt*s*math.sin(a)
    f=np.eye(3);f[0,2]=-dy;f[1,2]=dx
    g=np.array([[math.cos(a),0],[math.sin(a),0],[0,1.]])
    q=np.diag([(.03+.15*abs(v))**2*qv,(.03+.2*abs(w))**2*qw])*dt
    pp=f@p@f.T+g@q@g.T+np.eye(3)*dt*1e-10
    return np.array([x[0]+dx,x[1]+dy,wrap(x[2]+w*dt)]),pp
def observation(x,landmark):
    dx,dy=landmark[:2]-x[:2];r2=dx*dx+dy*dy;r=math.sqrt(max(r2,1e-12))
    h=np.array([[-dx/r,-dy/r,0],[dy/max(r2,1e-12),-dx/max(r2,1e-12),-1.]])
    return np.array([r,wrap(math.atan2(dy,dx)-x[2])]),h
CONFIGS={
 'fixed':{'scale':1.,'mode':'fixed'},
 'low_R':{'scale':.25,'mode':'fixed'},
 'high_R':{'scale':4.,'mode':'fixed'},
 'robust':{'scale':1.,'mode':'robust'},
 'reject':{'scale':1.,'mode':'reject'},
 'adaptive':{'scale':1.,'mode':'adaptive'},
 'adaptive_robust':{'scale':1.,'mode':'adaptive_robust'},
 'range_noise':{'scale':1.,'mode':'range_noise'},
}
def binding(r,config,engine):
    h=hashlib.sha256()
    for key in ('initial','odometry','observations'):h.update(np.ascontiguousarray(r[key]).tobytes())
    h.update(json.dumps({str(k):v.tolist() for k,v in r['landmarks'].items()},sort_keys=True).encode())
    h.update(json.dumps(engine.p if engine else config,sort_keys=True).encode());h.update(str(r['duration']).encode())
    return h.hexdigest()
def run(r,config,engine=None,keep=False,checkpoint=None,stop_at=None):
    start=time.perf_counter();x=r['initial'].copy();p=np.diag([.01,.01,.02])**2;od=r['odometry'];obs=r['observations'];lm=r['landmarks']
    t=0.;oi=0;mi=0;v,w=od[0,1:];ema=np.ones(2);mean=np.zeros(2);lastm=0.;lastq=(1.,1.);state={};rows=[];diagnostics=[];n_rejected=0
    source_binding=binding(r,config,engine)
    if checkpoint:
        if checkpoint['binding']!=source_binding:raise ValueError('checkpoint source/method mismatch')
        x=np.array(checkpoint['x']);p=np.array(checkpoint['p']);t=checkpoint['t'];oi=checkpoint['oi'];mi=checkpoint['mi'];v=checkpoint['v'];w=checkpoint['w'];ema=np.array(checkpoint['ema']);mean=np.array(checkpoint['mean']);lastm=checkpoint['lastm'];lastq=checkpoint['lastq'];state=checkpoint['state'];rows=checkpoint['rows'];diagnostics=checkpoint['diagnostics'];n_rejected=checkpoint['n_rejected']
    samples=np.arange(0.5,r['duration'],.5)
    if checkpoint:samples=samples[samples>t]
    if stop_at is not None:samples=samples[samples<=stop_at]
    for target in samples:
        while True:
            to=od[oi+1,0] if oi+1<len(od) else math.inf
            tm=obs[mi,0] if mi<len(obs) else math.inf
            tn=min(to,tm,float(target))
            x,p=motion(x,p,float(v),float(w),tn-t,*lastq);t=tn
            if tm<=to and tm<=target:
                _,s,rr,bb=obs[mi];mi+=1;pred,h=observation(x,lm[int(s)]);e=np.array([rr-pred[0],wrap(bb-pred[1])]);base=np.array([(.15+.02*pred[0])**2,.03**2])*config.get('scale',1.)
                projected=h@p@h.T;projection=np.diag(projected);z=e*e/(base+projection);nis=float(e@np.linalg.solve(projected+np.diag(base),e));skip=False;mode=config.get('mode','fixed')
                mult=np.ones(2)
                if mode in ('adaptive','adaptive_robust'):mult=np.clip(ema,0.25,25.)
                if mode=='range_noise':mult=np.array([max(1.,(pred[0]/3.)**2),1.])
                if mode in ('robust','adaptive_robust'):mult*=max(1.,nis/9.21)
                if mode=='reject' and nis>9.21:skip=True
                if engine:
                    context={'er':float(e[0]),'eb':float(e[1]),'zr':float(z[0]),'zb':float(z[1]),'nis':nis,'range':float(pred[0]),'dt':float(t-lastm),'v':float(v),'w':float(w),'pr':float(projection[0]),'pb':float(projection[1]),'rr':float(base[0]),'rb':float(base[1]),'ema_r':float(ema[0]),'ema_b':float(ema[1]),'mean_r':float(mean[0]),'mean_b':float(mean[1])}
                    out,state=engine(context,state);mult=np.array([out.get('r_scale',1.),out.get('b_scale',1.)]);lastq=(out.get('qv',1.),out.get('qw',1.))
                    e[0]-=out.get('range_bias',0.);e[1]=wrap(e[1]-out.get('bearing_bias',0.));skip=out.get('reject',0.)>.5
                if skip:n_rejected+=1
                else:
                    rrmat=np.diag(base*mult);ss=h@p@h.T+rrmat;k=np.linalg.solve(ss,h@p).T;x=x+k@e;x[2]=wrap(x[2]);a=np.eye(3)-k@h;p=a@p@a.T+k@rrmat@k.T;p=(p+p.T)*.5
                alpha=1-math.exp(-max(t-lastm,.001)/10.);ema=(1-alpha)*ema+alpha*np.minimum(z,100.);mean=(1-alpha)*mean+alpha*np.clip(e,[-2.,-.3],[2.,.3]);lastm=t
                if keep:diagnostics.append([t,int(s),nis,float(mult[0]),float(mult[1]),skip])
            elif to<=target:
                oi+=1;v,w=od[oi,1:]
            else:break
        if not(np.isfinite(x).all() and np.isfinite(p).all()) or max(abs(x[:2]))>1e5:raise ValueError('filter divergence')
        rows.append([target,*x,float(np.trace(p)),float(p[0,0]+p[1,1]),float(diagnostics[-1][2]) if diagnostics else 0.,float(lastm)])
    metrics={'measurements':mi,'rejected':n_rejected,'wall_seconds':time.perf_counter()-start}
    metrics['checkpoint']={'binding':source_binding,'x':x.tolist(),'p':p.tolist(),'t':t,'oi':oi,'mi':mi,'v':float(v),'w':float(w),'ema':ema.tolist(),'mean':mean.tolist(),'lastm':lastm,'lastq':list(lastq),'state':state,'rows':rows,'diagnostics':diagnostics,'n_rejected':n_rejected}
    return metrics