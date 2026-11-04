"""Offline arithmetic/identity checks; not original model replication."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def read(stem):
    return json.loads((ROOT / 'evidence' / ('EVIDENCE_2026-10-24_' + stem + '.json')).read_text())

def usage(x):
    assert x['totalTokens'] == x['inputTokens'] + x['outputTokens']
    assert 0 <= x['cachedInputTokens'] <= x['inputTokens']
    assert x['uncachedInputPlusOutput'] == x['totalTokens'] - x['cachedInputTokens']

def main():
    hashes = 0
    listed = set()
    for line in (ROOT / 'MANIFEST.sha256').read_text().splitlines():
        sha, rel = line.split('  ', 1)
        p = (ROOT / rel).resolve()
        assert p.is_relative_to(ROOT.resolve()), rel
        assert hashlib.sha256(p.read_bytes()).hexdigest() == sha, rel
        assert rel not in listed, rel
        listed.add(rel)
        hashes += 1
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and p != ROOT/'MANIFEST.sha256' and '__pycache__' not in p.parts}
    assert actual == listed, {'missing':sorted(actual-listed),'extra':sorted(listed-actual)}
    s3, s4, s5, s6 = [read(x) for x in ('CONNECTED_SEQUENCE', 'OBSERVATION_COST', 'LIGHTWEIGHT_OBSERVATIONS', 'RESTORED_OBSERVATIONS')]
    for study in (s3, s4, s5, s6):
        for arm in study['policies'].values():
            usage(arm['tokens'])
    assert sum(a['tokens']['totalTokens'] for a in s3['policies'].values()) + s3['acquisition']['totalTokens'] == 3285056
    assert sum(a['tokens']['totalTokens'] for a in s6['policies'].values()) + s6['acquisition']['tokens']['totalTokens'] == 3896772
    assert s6['actual_study_usage']['totalTokens'] == 3896772
    assert all(a['successes'] == 6 for a in s6['policies'].values())
    assert s5['scoped_adoption_qualified'] is False
    assert s6['scoped_adoption_qualified'] is False
    assert s6['selection_checks']['uncached_not_increased'] is False
    values = {
        'S4_REL_facts_token_increase_percent': 100 * (s4['policies']['R']['tokens']['totalTokens'] / s4['policies']['O']['tokens']['totalTokens'] - 1),
        'S4_REL_facts_query_reduction_percent': 100 * (1 - s4['policies']['R']['total_vm_steps'] / s4['policies']['N']['total_vm_steps']),
        'S4_ordinary_facts_query_reduction_percent': 100 * (1 - s4['policies']['O']['total_vm_steps'] / s4['policies']['N']['total_vm_steps']),
        'S5_compact_charged_token_change_percent': 100 * (s5['acquisition_charged']['C']['tokens']['totalTokens'] / s5['acquisition_charged']['R']['tokens']['totalTokens'] - 1),
        'S6_restored_charged_token_change_percent': 100 * (s6['acquisition_charged']['V']['tokens']['totalTokens'] / s6['acquisition_charged']['C']['tokens']['totalTokens'] - 1),
        'S6_restored_charged_uncached_change_percent': 100 * (s6['acquisition_charged']['V']['tokens']['uncachedInputPlusOutput'] / s6['acquisition_charged']['C']['tokens']['uncachedInputPlusOutput'] - 1),
    }
    values['S6_ordinary_charged_token_change_percent'] = 100 * (s6['acquisition_charged']['H']['tokens']['totalTokens'] / s6['acquisition_charged']['V']['tokens']['totalTokens'] - 1)
    targets = [55.415, 76.842, 77.564, 9.488, -13.087, 6.866, -16.744]
    for val, target in zip(values.values(), targets):
        assert abs(val-target) < .02, (val,target)
    appendix = (ROOT/'EVIDENCE_APPENDIX.md').read_text(encoding='utf8')
    nonmodel = []
    for arm in s4['nonmodel_baselines']:
        assert arm['total_work'] == arm['acquisition_work'] + arm['later_work']
        row = f"| {arm['policy']} | {arm['later_successes']}/{arm['later_tasks']} | {arm['later_work']:,} | {arm['acquisition_work']:,} |"
        assert row in appendix, ('nonmodel appendix row', row)
        nonmodel.append(arm['policy'])
    skill_root = ROOT/'rel-current'
    skill_entries = (skill_root/'MANIFEST.sha256').read_text().splitlines()
    assert len(skill_entries)==21
    skill_listed = set()
    for entry in skill_entries:
        identity, relative = entry.split('  ',1)
        assert relative not in skill_listed, ('duplicate current skill file', relative)
        skill_listed.add(relative)
        file = (skill_root/relative).resolve()
        assert file.is_relative_to(skill_root.resolve()), relative
        assert hashlib.sha256(file.read_bytes()).hexdigest()==identity, relative
    skill_actual = {p.relative_to(skill_root).as_posix() for p in skill_root.rglob('*') if p.is_file() and p!=skill_root/'MANIFEST.sha256'}
    assert skill_actual==skill_listed, ('current skill inventory', sorted(skill_actual-skill_listed), sorted(skill_listed-skill_actual))
    assert hashlib.sha256((skill_root/'SKILL.md').read_bytes()).hexdigest()==json.loads((ROOT/'VERSIONS.json').read_text())['installed_skill_sha256']
    legacy = {}
    for folder in ('reproduce-study1', 'reproduce-study2'):
        p = ROOT / folder
        r = subprocess.run([sys.executable, '-B', str(p/'reproduce.py')], cwd=p, capture_output=True, text=True, timeout=30)
        assert r.returncode == 0, (folder, r.stderr, r.stdout)
        legacy[folder] = 'passed'
    print(json.dumps({'status':'pass','identity_files':hashes,'selected_arithmetic':values,'nonmodel_rows':nonmodel,'current_skill_files':len(skill_entries),'legacy_accounting':legacy,'limit':'Saved-summary arithmetic and supplied file identities only; not original event authentication or scientific replication.'}, indent=2))

if __name__ == '__main__':
    main()
