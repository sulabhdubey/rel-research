"""Reconstruct selected manuscript arithmetic from saved metrics, not sensors."""
from pathlib import Path
import hashlib,json,math,statistics
ROOT=Path(__file__).resolve().parent

def reconstruct(d):
    assert d['same_observations'] is True and d['future_truth_in_readout'] is False
    for k in ('numerical_qualification_passed','fresh_confirmation_qualified','native_model_comparison_admitted'):
        assert d[k] is False,k
    assert d['selected'] is None
    rows=d['rows']; keys=[(x['dataset'],x['robot'],x['policy']) for x in rows]
    assert len(keys)==len(set(keys)),'duplicate rows'
    assert {x['dataset'] for x in rows}==set(range(4,10)),'recording coverage'
    policies=['robust','J1','J2','J1-mean','J2-mean']; by={}
    for p in policies:
        selected=[x for x in rows if x['policy']==p]
        assert len(selected)==30,'five robots in six recordings'
        mse=[]
        for dataset in range(4,10):
            rr=[x for x in selected if x['dataset']==dataset]
            assert {x['robot'] for x in rr}==set(range(1,6))
            expected=2399 if dataset in (4,9) else 1199
            assert all(x['samples']==expected for x in rr),'endpoint denominator'
            assert all(math.isfinite(x['mse']) and x['mse']>=0 and 0<=x['over_0_5m']<=x['samples'] for x in rr)
            mse.append(sum(x['mse']*x['samples'] for x in rr)/sum(x['samples'] for x in rr))
        v={'mse':statistics.mean(mse),'over_0_5m':sum(x['over_0_5m'] for x in selected),'episodes':sum(x['episodes'] for x in selected),'max_m':max(x['max_m'] for x in selected),'samples':sum(x['samples'] for x in selected)}
        assert v['samples']==47970
        saved=d['balanced_recording_summary'][p]
        assert math.isclose(v['mse'],saved['mse'],rel_tol=1e-12,abs_tol=1e-14),'saved balanced summary'
        assert v['over_0_5m']==saved['over_0_5m']
        by[p]=v
    def pair(a,b):
        return {k:(max(by[a][k],by[b][k]) if k=='max_m' else (by[a][k]+by[b][k])/2) for k in by[a]}
    table={'robust':by['robust'],'acquired':pair('J1','J2'),'mean':pair('J1-mean','J2-mean')}
    r,j,m=(table[x] for x in ('robust','acquired','mean'))
    changes={'mean_vs_robust_mse_reduction_percent':100*(1-m['mse']/r['mse']),'mean_vs_robust_above_band_reduction_percent':100*(1-m['over_0_5m']/r['over_0_5m']),'mean_vs_acquired_mse_increase_percent':100*(m['mse']/j['mse']-1)}
    return {'table':table,'changes':changes}

def main():
    result=reconstruct(json.loads((ROOT/'component-evidence/RESULTS119.json').read_text(encoding='utf8')))
    paper=(ROOT/'PAPER.md').read_text(encoding='utf8')
    for name,label in [('robust','Robust'),('acquired','Acquired pair'),('mean','Pairwise equal mean')]:
        x=result['table'][name]
        row=f"| {label} | {x['mse']:.8f} | {x['over_0_5m']:g} | {x['episodes']:g} | {x['max_m']:.3f} |"
        assert row in paper,('manuscript table',row)
    for n in result['changes'].values():assert f'{n:.2f}%' in paper
    assert json.loads((ROOT/'source-review/SOURCE_REVIEW.json').read_text())['status']=='NOT_ADMITTED'
    core=json.loads((ROOT/'VERSIONS.json').read_text())
    assert core['new_empirical_experiment'] is False and core['version']=='0.7'
    print(json.dumps({'passed':True,**result,'scope':'Reconstructs saved metric summaries and exact manuscript table. No physical-data or model-experiment replay.'},indent=2))
if __name__=='__main__':main()
