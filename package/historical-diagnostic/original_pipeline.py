from fractions import Fraction

def _eq(a,b):
    if isinstance(a,bool) or isinstance(b,bool):
        return isinstance(a,bool) and isinstance(b,bool) and a==b
    if isinstance(a,(int,float)) and isinstance(b,(int,float)): return a==b
    if isinstance(a,dict) and isinstance(b,dict):
        return a.keys()==b.keys() and all(_eq(a[k],b[k]) for k in a)
    if isinstance(a,list) and isinstance(b,list):
        return len(a)==len(b) and all(_eq(x,y) for x,y in zip(a,b))
    return type(a) is type(b) and a==b

def _num(x): return isinstance(x,(int,float)) and not isinstance(x,bool)
def _integer(x): return _num(x) and (isinstance(x,int) or x.is_integer())
def _type(x,t):
    return {'null':x is None,'boolean':isinstance(x,bool),'object':isinstance(x,dict),
            'array':isinstance(x,list),'number':_num(x),'integer':_integer(x),
            'string':isinstance(x,str)}.get(t,False)
def _div(x,d):
    try: return (Fraction(str(x))/Fraction(str(d))).denominator==1
    except Exception: return False
def _empty(): return {'p':set(),'i':set()}
def _merge(dst,src):
    dst['p'].update(src['p']); dst['i'].update(src['i'])

def _eval(s,x,d):
    # Result annotations belong to a schema only when that schema succeeds.
    out=_empty()
    if isinstance(s,bool): return s,out
    if not isinstance(s,dict): return True,out
    def sub(sc,val): return _eval(sc,val,d)
    if 'type' in s:
        ts=s['type'] if isinstance(s['type'],list) else [s['type']]
        if not any(_type(x,t) for t in ts): return False,out
    if 'enum' in s and not any(_eq(x,v) for v in s['enum']): return False,out
    if 'const' in s and not _eq(x,s['const']): return False,out
    if _num(x):
        for k,ok in (('minimum',lambda a,b:a>=b),('maximum',lambda a,b:a<=b),
                     ('exclusiveMinimum',lambda a,b:a>b),('exclusiveMaximum',lambda a,b:a<b)):
            if k in s and not ok(x,s[k]): return False,out
        if 'multipleOf' in s and not _div(x,s['multipleOf']): return False,out
    if isinstance(x,str):
        if 'minLength' in s and len(x)<s['minLength']: return False,out
        if 'maxLength' in s and len(x)>s['maxLength']: return False,out
    if isinstance(x,list):
        if len(x)<s.get('minItems',0) or len(x)>s.get('maxItems',float('inf')): return False,out
        if s.get('uniqueItems') and any(_eq(x[i],x[j]) for i in range(len(x)) for j in range(i)): return False,out
        local=_empty()
        if d=='draft7':
            if 'items' in s:
                it=s['items']
                if isinstance(it,list):
                    for i,sc in enumerate(it[:len(x)]):
                        ok,a=sub(sc,x[i])
                        if not ok:return False,out
                        local['i'].add(i)
                    ai=s.get('additionalItems',True)
                    for i in range(len(it),len(x)):
                        ok,a=sub(ai,x[i])
                        if not ok:return False,out
                        local['i'].add(i)
                else:
                    for i,v in enumerate(x):
                        ok,a=sub(it,v)
                        if not ok:return False,out
                        local['i'].add(i)
            if 'contains' in s:
                matches=[i for i,v in enumerate(x) if sub(s['contains'],v)[0]]
                if not matches:return False,out
                local['i'].update(matches)
        else:
            pref=s.get('prefixItems',[])
            if not isinstance(pref,list): pref=[]
            for i,sc in enumerate(pref[:len(x)]):
                ok,a=sub(sc,x[i])
                if not ok:return False,out
                local['i'].add(i)
            if 'items' in s:
                for i in range(len(pref),len(x)):
                    ok,a=sub(s['items'],x[i])
                    if not ok:return False,out
                    local['i'].add(i)
            if 'contains' in s:
                matches=[i for i,v in enumerate(x) if sub(s['contains'],v)[0]]
                if len(matches)<s.get('minContains',1) or len(matches)>s.get('maxContains',float('inf')): return False,out
                local['i'].update(matches)
        _merge(out,local)
    if isinstance(x,dict):
        if len(x)<s.get('minProperties',0) or len(x)>s.get('maxProperties',float('inf')): return False,out
        if any(k not in x for k in s.get('required',[])): return False,out
        local=_empty(); props=s.get('properties',{})
        if isinstance(props,dict):
            for k,sc in props.items():
                if k in x:
                    ok,a=sub(sc,x[k])
                    if not ok:return False,out
                    local['p'].add(k)
            if 'additionalProperties' in s:
                for k,v in x.items():
                    if k not in props:
                        ok,a=sub(s['additionalProperties'],v)
                        if not ok:return False,out
                        local['p'].add(k)
        if d=='draft7':
            for trigger,dep in s.get('dependencies',{}).items():
                if trigger in x:
                    if isinstance(dep,list):
                        if any(k not in x for k in dep):return False,out
                    else:
                        ok,a=sub(dep,x)
                        if not ok:return False,out
                        _merge(local,a)
        else:
            for trigger,names in s.get('dependentRequired',{}).items():
                if trigger in x and any(k not in x for k in names):return False,out
            for trigger,sc in s.get('dependentSchemas',{}).items():
                if trigger in x:
                    ok,a=sub(sc,x)
                    if not ok:return False,out
                    _merge(local,a)
        _merge(out,local)
    # Applicators export annotations only from successful evaluations.
    if 'allOf' in s:
        for sc in s['allOf']:
            ok,a=sub(sc,x)
            if not ok:return False,out
            _merge(out,a)
    for key,mode in (('anyOf','any'),('oneOf','one')):
        if key in s:
            results=[sub(sc,x) for sc in s[key]]
            good=[a for ok,a in results if ok]
            if not good or (mode=='one' and len(good)!=1):return False,out
            for a in good:_merge(out,a)
    if 'not' in s and sub(s['not'],x)[0]:return False,out
    if 'if' in s:
        cond,ca=sub(s['if'],x)
        if cond:_merge(out,ca)
        branch='then' if cond else 'else'
        if branch in s:
            ok,a=sub(s[branch],x)
            if not ok:return False,out
            _merge(out,a)
    # Deferred annotations see all applicable successful adjacent applicators.
    if d=='draft2020-12' and isinstance(x,dict) and 'unevaluatedProperties' in s:
        for k,v in x.items():
            if k not in out['p']:
                ok,a=sub(s['unevaluatedProperties'],v)
                if not ok:return False,out
                out['p'].add(k); _merge(out,a)
    if d=='draft2020-12' and isinstance(x,list) and 'unevaluatedItems' in s:
        for i,v in enumerate(x):
            if i not in out['i']:
                ok,a=sub(s['unevaluatedItems'],v)
                if not ok:return False,out
                out['i'].add(i); _merge(out,a)
    return True,out

def solve(case):
    """Validate the declared draft7 / draft2020-12 profile U; return a strict bool."""
    return bool(_eval(case['schema'],case['instance'],case['dialect'])[0])
