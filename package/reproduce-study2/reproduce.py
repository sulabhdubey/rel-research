"""Standard-library offline reconstruction of the exported study table."""
from pathlib import Path
import csv,hashlib,json
ROOT=Path(__file__).resolve().parent
for line in (ROOT/'MANIFEST.sha256').read_text('ascii').splitlines():
 digest,name=line.split('  ',1)
 assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,('changed file',name)
rows=list(csv.DictReader((ROOT/'attempts.csv').open(newline='',encoding='utf8')))
assert len(rows)==24 and len({r['cell'] for r in rows})==24
old=json.loads((ROOT/'historical_acquisition.json').read_bytes());result={}
for arm in 'ABC':
 rs=[r for r in rows if r['arm']==arm];assert len(rs)==8
 assert {(r['origin'],r['profile'],r['repetition']) for r in rs}=={(o,p,t) for o in ('O1','O2') for p in 'RU' for t in ('1','2')}
 total=sum(int(r['total_tokens']) for r in rs)
 uv=sum(int(r['input_tokens'])-int(r['cached_input_tokens'])+int(r['output_tokens']) for r in rs)
 assert all(int(r['total_tokens'])==int(r['input_tokens'])+int(r['output_tokens']) for r in rs)
 result[arm]={'attempts':8,'e2_correct':sum(int(r['e2_pass']) for r in rs),'e3_correct':sum(int(r['e3_pass']) for r in rs),'both_correct':sum(int(r['e2_pass']) and int(r['e3_pass']) for r in rs),'new_tokens':total,'inclusive_tokens':total+(old['total_tokens'] if arm!='A' else 0),'new_uncached_plus_output':uv,'inclusive_uncached_plus_output':uv+(old['uncached_plus_output'] if arm!='A' else 0)}
assert result==json.loads((ROOT/'expected_summary.json').read_bytes()),'exported aggregate mismatch'
print(json.dumps({'verified_table':result,'actual_new_worker_tokens':sum(r['new_tokens'] for r in result.values()),'scope':'Recomputes exported records; does not authenticate raw events or rerun models.'},indent=2))
