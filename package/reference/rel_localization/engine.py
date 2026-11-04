"""Bounded scalar numeric program; no eval, imports, I/O, host tools or Python execution."""
import json
import math
INPUTS=set('er eb zr zb nis range dt v w pr pb rr rb ema_r ema_b mean_r mean_b'.split())
BOUNDS={'r_scale':(.01,100.),'b_scale':(.01,100.),'qv':(.01,100.),'qw':(.01,100.),'range_bias':(-1.,1.),'bearing_bias':(-.2,.2),'reject':(0.,1.)}
OPS={'add':2,'sub':2,'mul':2,'div':2,'min':2,'max':2,'abs':1,'sqrt':1,'exp':1,'gt':2,'lt':2,'if':3,'clip':3}
def number(x):return type(x) in (float,int) and math.isfinite(x) and abs(x)<=1e6
def validate(p):
    if type(p)!=dict or set(p)!={'version','lesson','init','nodes','outputs','state'}:raise ValueError('program fields')
    if p['version']!='range-bearing-v1' or not isinstance(p['lesson'],str) or len(p['lesson'])>1800:raise ValueError('contract/lesson')
    if type(p['init'])!=dict or len(p['init'])>8 or any(k not in {f'm{i}' for i in range(8)} or not number(v) for k,v in p['init'].items()):raise ValueError('state init')
    known=INPUTS|set(p['init']);nodes=p['nodes']
    if type(nodes)!=list or len(nodes)>64:raise ValueError('node count')
    def ref(v):return number(v) or isinstance(v,str) and v in known
    for n in nodes:
        if type(n)!=dict or set(n)!={'name','op','args'}:raise ValueError('node fields')
        name=n['name'];op=n['op'];a=n['args']
        if not isinstance(name,str) or not name.startswith('n') or len(name)>24 or name in known or op not in OPS or type(a)!=list or len(a)!=OPS[op] or not all(ref(v) for v in a):raise ValueError('node reference/op')
        known.add(name)
    if type(p['outputs'])!=dict or set(p['outputs'])!=set(BOUNDS) or not all(ref(v) for v in p['outputs'].values()):raise ValueError('outputs')
    if type(p['state'])!=dict or set(p['state'])!=set(p['init']) or not all(ref(v) for v in p['state'].values()):raise ValueError('state update')
    if len(json.dumps(p))>18000:raise ValueError('program size')
    return p
class Engine:
    def __init__(self,p):self.p=validate(p);self.calls=0
    def __call__(self,c,state):
        env=dict(c);env.update(state if state else self.p['init']);self.calls+=1
        def value(v):return float(env[v]) if isinstance(v,str) else float(v)
        for n in self.p['nodes']:
            a=[value(x) for x in n['args']];op=n['op']
            if op=='add':y=a[0]+a[1]
            elif op=='sub':y=a[0]-a[1]
            elif op=='mul':y=a[0]*a[1]
            elif op=='div':y=a[0]/(a[1] if abs(a[1])>=1e-9 else math.copysign(1e-9,a[1]))
            elif op=='min':y=min(a)
            elif op=='max':y=max(a)
            elif op=='abs':y=abs(a[0])
            elif op=='sqrt':y=math.sqrt(max(0.,a[0]))
            elif op=='exp':y=math.exp(max(-30.,min(30.,a[0])))
            elif op=='gt':y=float(a[0]>a[1])
            elif op=='lt':y=float(a[0]<a[1])
            elif op=='if':y=a[1] if a[0]>.5 else a[2]
            elif op=='clip':y=max(a[1],min(a[2],a[0]))
            if not math.isfinite(y) or abs(y)>1e9:raise ValueError('numeric bound')
            env[n['name']]=y
        out={k:value(v) for k,v in self.p['outputs'].items()};st={k:value(v) for k,v in self.p['state'].items()}
        if any(not math.isfinite(v) or not BOUNDS[k][0]<=v<=BOUNDS[k][1] for k,v in out.items()):raise ValueError('output physical bounds')
        if any(not math.isfinite(v) or abs(v)>1e4 for v in st.values()):raise ValueError('retained-state bound')
        return out,st
def fixed(scale=4.):return {'version':'range-bearing-v1','lesson':'Ordinary tuned constant noise; reset state for a new recording.','init':{},'nodes':[],'outputs':{'r_scale':scale,'b_scale':scale,'qv':1.,'qw':1.,'range_bias':0.,'bearing_bias':0.,'reject':0.},'state':{}}
