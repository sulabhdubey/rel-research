"""Targeted engineering checks, not independent empirical tasks."""
from copy import deepcopy
from fractions import Fraction as F
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import walkthrough as w


def reference(rows, c):
    # Separately implemented ordinary calculation, not SQL or wrapper helpers.
    chosen = {}
    for r in sorted(rows, key=lambda x: (x['sample_id'], -x['revision'])):
        if r['available'] <= c['as_of'] and r['sample_id'] not in chosen:
            chosen[r['sample_id']] = r
    total = F(0); peak = None; minutes = 0; count = 0
    for r in chosen.values():
        if not (c['start'] <= r['t'] < c['end']) or r['duration'] <= 0 or r['value'] is None:
            continue
        if r['quality'] not in ([1, 2] if c['quality_rule'] == 'graded' else [1]):
            continue
        v = F(str(r['value'])) * F(str(c['calibration_gain'])) + F(str(c['calibration_offset']))
        energy = v if c['unit'] == 'Wh' else v * F(str(r['duration'])) / 60
        power = energy * 60 / F(str(r['duration']))
        total += energy; peak = power if peak is None else max(peak, power)
        minutes += r['duration']; count += 1
    return {'energy_kwh': float(total/1000), 'peak_kw': None if peak is None else float(peak/1000),
            'valid_minutes': minutes, 'valid_count': count}


class WalkthroughChecks(unittest.TestCase):
    def setUp(self):
        self.rows, self.c = w.fixture()
        self.clock = {**self.c, 'interval_anchor':'start','interval_totals_measured':True,'power_nonnegative':True}

    def check_reference(self, rows, c):
        result = w.decide(rows,c)['result']; expected=reference(rows,c)
        for k in expected:
            if expected[k] is None:self.assertIsNone(result[k])
            else:self.assertAlmostEqual(result[k],expected[k])

    def test_reuse_invokes_historical_sql(self):
        result=w.decide(self.rows,self.c)
        self.assertEqual(result['action'],'reuse_saved_method');self.assertEqual(result['sql_executions'],1)
        self.assertEqual(result['result']['energy_kwh'],0.03);self.check_reference(self.rows,self.c)

    def test_calibration_changes_operation_and_answer(self):
        c={**self.c,'calibration_gain':1.25,'calibration_offset':7}
        r=w.decide(self.rows,c);self.assertEqual(r['action'],'adapt_with_retained_method')
        self.assertEqual(r['result']['energy_kwh'],0.0515);self.check_reference(self.rows,c)

    def test_latest_revision_precedes_quality(self):
        rows=self.rows+[dict(self.rows[0],revision=1,quality=0),dict(self.rows[1],revision=1,available=100,value=999)]
        self.check_reference(rows,self.c);self.assertEqual(w.decide(rows,self.c)['result']['energy_kwh'],0.02)

    def test_watts_graded_and_calibration(self):
        rows=[dict(r,quality=2,value=r['value']*6) for r in self.rows]
        self.check_reference(rows,{**self.c,'unit':'W','quality_rule':'graded','calibration_offset':3})

    def test_empty_eligible_set(self):
        rows=[dict(r,quality=0) for r in self.rows];self.check_reference(rows,self.c)
        self.assertIsNone(w.decide(rows,self.c)['result']['peak_kw'])

    def test_irrelevant_context_does_not_change_answer(self):
        self.assertEqual(w.decide(self.rows,self.c)['result'],w.decide(self.rows,{**self.c,'display_color':'blue'})['result'])

    def test_restore_original_contract_reuses_v1(self):
        w.decide(self.rows,{**self.c,'calibration_gain':2})
        self.assertEqual(w.decide(self.rows,self.c)['action'],'reuse_saved_method')

    def test_changed_facts_recompute_instead_of_reusing_answer(self):
        before=w.decide(self.rows,self.c)
        after=w.decide([dict(self.rows[0],value=15),self.rows[1]],self.c)
        self.assertEqual(before['method_id'],after['method_id'])
        self.assertEqual(after['result']['energy_kwh'],0.035)

    def test_refusal_does_not_destroy_valid_method(self):
        w.decide(self.rows,{**self.clock,'start':5,'end':15},'exact_clock_window')
        self.assertEqual(w.decide(self.rows,self.c)['result']['energy_kwh'],0.03)

    def test_empty_clock_interval_is_exact(self):
        r=w.decide(self.rows,{**self.clock,'start':5,'end':5},'exact_clock_window')
        self.assertEqual(r['energy_wh'],'0')

    def test_empty_clock_needs_no_interval_anchor(self):
        r=w.decide(self.rows,{**self.c,'start':5,'end':5},'exact_clock_window')
        self.assertEqual(r['energy_wh'],'0')

    def test_overlapping_support_outside_query_rejected(self):
        rows=[self.rows[0],dict(self.rows[1],t=5,value=0)]
        r=w.decide(rows,{**self.clock,'start':0,'end':5},'exact_clock_window')
        self.assertEqual(r['action'],'refuse_exact_answer')
        self.assertNotIn('admissible_energy_wh',r)
        self.assertIn('Overlapping',r['reason'])

    def test_negative_support_outside_query_rejected(self):
        rows=[self.rows[0],dict(self.rows[1],value=-1)]
        r=w.decide(rows,{**self.clock,'start':0,'end':5},'exact_clock_window')
        self.assertEqual(r['action'],'refuse_exact_answer')
        self.assertNotIn('admissible_energy_wh',r)
        self.assertIn('Negative',r['reason'])

    def test_unknown_and_missing_context_reject(self):
        for changed in ({**self.c,'unit':'kWh'}, {k:v for k,v in self.c.items() if k!='calibration_gain'},
                        {**self.c,'end':float('nan')}, {**self.c,'schema_version':True}):
            with self.subTest(changed=changed),self.assertRaises(ValueError):w.decide(self.rows,changed)

    def test_clock_unknown_anchor_has_no_numeric_claim(self):
        r=w.decide(self.rows,self.c,'exact_clock_window');self.assertEqual(r['action'],'refuse_exact_answer')
        self.assertNotIn('admissible_energy_wh',r)

    def test_partial_clock_refuses_with_qualified_bound(self):
        with patch.object(w,'Engine',side_effect=AssertionError('No SQL required for refusal')):
            r=w.decide(self.rows,{**self.clock,'start':5,'end':15},'exact_clock_window')
        self.assertEqual(r['admissible_energy_wh'],['0','30']);self.assertEqual(r['sql_executions'],0)

    def test_full_bin_union_is_not_falsely_refused(self):
        r=w.decide(self.rows,self.clock,'exact_clock_window')
        self.assertEqual(r['action'],'answer_from_interval_totals');self.assertEqual(r['energy_wh'],'30')

    def test_zero_partial_bin_is_exact(self):
        rows=[dict(r,value=0) for r in self.rows]
        r=w.decide(rows,{**self.clock,'start':5,'end':15},'exact_clock_window')
        self.assertEqual(r['energy_wh'],'0')

    def test_gap_overlap_and_negative_are_not_bounded(self):
        variants=([dict(self.rows[0],duration=5),self.rows[1]],
                  [dict(self.rows[0],duration=15),self.rows[1]],
                  [dict(self.rows[0],value=-1),self.rows[1]])
        for rows in variants:
            with self.subTest(rows=rows):
                r=w.decide(rows,self.clock,'exact_clock_window')
                self.assertEqual(r['action'],'refuse_exact_answer');self.assertNotIn('admissible_energy_wh',r)

    def test_duplicate_revision_rejected(self):
        with self.assertRaises(ValueError):w.decide(self.rows+[self.rows[0]],self.c)

    def test_tampered_saved_bundle_rejected_before_sql(self):
        with tempfile.TemporaryDirectory() as td:
            target=Path(td);target.joinpath('PROVENANCE.json').write_bytes((w.HERE/'PROVENANCE.json').read_bytes())
            target.joinpath('methods.json').write_text('{}')
            with patch.object(w,'HERE',target),self.assertRaisesRegex(ValueError,'identity changed'):w.decide(self.rows,self.c)

    def test_fresh_process_reloads_methods(self):
        p=subprocess.run([sys.executable,'-B',str(w.HERE/'demo.py')],cwd=w.HERE,capture_output=True,text=True,check=True,timeout=15)
        r=json.loads(p.stdout)
        self.assertEqual([x['decision']['action'] for x in r['cases']],['reuse_saved_method','adapt_with_retained_method','refuse_exact_answer'])
        self.assertEqual([x['decision']['model_calls'] for x in r['cases']],[0,0,0])


if __name__=='__main__':unittest.main()
