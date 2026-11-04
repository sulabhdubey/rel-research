"""Check explicitly required finite routes in JSON cases; no inference of adequacy.

CLI: python coverage_audit.py cases.json required.json
required.json is a nonempty list of nonempty top-level selector objects, e.g.
[{"op":"read"},{"op":"write"}]. Cases may contain additional fields.
Missing keys differ from explicit null. Expected values are JSON scalars only.
Exit 0: every declared route appears; 1: missing route; 2: malformed input.
This does not execute cases, discover undeclared routes, or prove correctness.
"""
import argparse,json,math,sys

def scalar(x):
 return x is None or type(x) in (str,bool,int) or (type(x) is float and math.isfinite(x))

def _read(path):
 def pairs(rows):
  d={}
  for k,v in rows:
   if k in d:raise ValueError('duplicate JSON object key')
   d[k]=v
  return d
 with open(path,encoding='utf-8-sig') as f:
  return json.load(f,object_pairs_hook=pairs,parse_constant=lambda x:(_ for _ in ()).throw(ValueError('nonfinite JSON constant')))

def audit(cases,required):
 if type(cases) is not list or any(type(c) is not dict for c in cases):raise ValueError('cases must be a list of objects')
 if type(required) is not list or not required:raise ValueError('required must be a nonempty list')
 seen=set();routes=[]
 for req in required:
  if type(req) is not dict or not req or any(type(k) is not str or not scalar(v) for k,v in req.items()):raise ValueError('route must be a nonempty object of scalar selectors')
  key=tuple(sorted((k,type(v).__name__,repr(v)) for k,v in req.items()))
  if key in seen:raise ValueError('duplicate required route')
  seen.add(key)
  count=sum(all(k in c and type(c[k]) is type(v) and c[k]==v for k,v in req.items()) for c in cases)
  routes.append({'selector':req,'matching_cases':count,'covered':count>0})
 return {'all_declared_routes_present':all(r['covered'] for r in routes),'case_count':len(cases),'routes':routes,'scope':'presence only; not execution, assertions, independence, semantic correctness or exhaustive coverage'}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('cases');p.add_argument('required');a=p.parse_args()
 try:r=audit(_read(a.cases),_read(a.required))
 except (OSError,ValueError,TypeError) as e:print(json.dumps({'error':str(e)}));return 2
 print(json.dumps(r,sort_keys=True));return 0 if r['all_declared_routes_present'] else 1
if __name__=='__main__':raise SystemExit(main())
