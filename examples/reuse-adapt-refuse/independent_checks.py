"""Run125 review checks: authored separately from the demonstration tests.

Only decide is imported from the implementation. Expected values use direct
arithmetic and explicit four-half-bin witnesses, not its test/reference helpers.
"""
import json
import math
from pathlib import Path
import sys
from time import perf_counter

sys.path.insert(0, str(Path.cwd()))
from walkthrough import decide


def main():
    started = perf_counter()
    rows = [
        dict(sample_id=101, revision=0, available=0, t=0, duration=10, value=10, quality=1),
        dict(sample_id=202, revision=0, available=0, t=10, duration=10, value=20, quality=1),
    ]
    context = dict(family='energy', schema_version=1,
                   revision_policy='latest_available_then_quality', unit='Wh',
                   quality_rule='binary', as_of=50, start=0, end=20,
                   calibration_gain=1, calibration_offset=0)
    checks = []

    def numeric(name, actual, expected, action):
        assert actual['action'] == action, (name, actual)
        for key, value in expected.items():
            assert math.isclose(actual['result'][key], value, rel_tol=1e-12, abs_tol=1e-12), (name, actual, expected)
        checks.append(dict(name=name, passed=True, expected=expected, observed=actual))

    numeric('original_current_rows', decide(rows, context),
            dict(energy_kwh=(10+20)/1000, peak_kw=max(10,20)*6/1000,
                 valid_minutes=20, valid_count=2), 'reuse_saved_method')
    calibrated = dict(context, calibration_gain=1.25, calibration_offset=7)
    numeric('calibration_applied_to_each_stored_value', decide(rows, calibrated),
            dict(energy_kwh=((1.25*10+7)+(1.25*20+7))/1000,
                 peak_kw=max(1.25*10+7,1.25*20+7)*6/1000,
                 valid_minutes=20, valid_count=2), 'adapt_with_retained_method')
    changed = [dict(rows[0]), dict(rows[1], value=35)]
    numeric('current_rows_change_saved_method_answer', decide(changed, context),
            dict(energy_kwh=(10+35)/1000, peak_kw=max(10,35)*6/1000,
                 valid_minutes=20, valid_count=2), 'reuse_saved_method')
    numeric('current_rows_change_calibrated_answer', decide(changed, calibrated),
            dict(energy_kwh=((1.25*10+7)+(1.25*35+7))/1000,
                 peak_kw=max(1.25*10+7,1.25*35+7)*6/1000,
                 valid_minutes=20, valid_count=2), 'adapt_with_retained_method')
    known = dict(context, interval_anchor='start', interval_totals_measured=True,
                 power_nonnegative=True)
    for name, start, end, expected in [('full_union',0,20,30),('single_complete_bin',10,20,20)]:
        actual = decide(rows, dict(known, start=start, end=end), 'exact_clock_window')
        assert actual['action'] == 'answer_from_interval_totals' and float(actual['energy_wh']) == expected, (name, actual)
        assert actual['sql_executions'] == 0
        checks.append(dict(name=name, passed=True, expected_energy_wh=expected, observed=actual))

    # Explicit piecewise-constant energy densities (Wh/min) on four five-minute
    # half-bins. Both satisfy measured totals 10 Wh and 20 Wh; their [5,15)
    # integrals differ, so the available information cannot determine one value.
    densities = [(2,0,0,4), (0,2,4,0)]
    for density in densities:
        assert (5*(density[0]+density[1]), 5*(density[2]+density[3])) == (10,20)
    witness_integrals = [5*(density[1]+density[2]) for density in densities]
    assert witness_integrals == [0,30]
    partial = decide(rows, dict(known, start=5, end=15), 'exact_clock_window')
    assert partial['action'] == 'refuse_exact_answer' and partial['sql_executions'] == 0, partial
    assert list(map(float, partial['admissible_energy_wh'])) == witness_integrals, partial
    checks.append(dict(name='partial_bins_have_distinct_feasible_integrals', passed=True,
                       witness_energy_densities_wh_per_minute=densities,
                       half_bin_width_minutes=5, witness_integrals_wh=witness_integrals,
                       observed=partial))

    unanchored = dict(known, start=5, end=15)
    del unanchored['interval_anchor']
    absent = decide(rows, unanchored, 'exact_clock_window')
    assert absent['action'] == 'refuse_exact_answer' and absent['sql_executions'] == 0, absent
    assert 'admissible_energy_wh' not in absent, absent
    checks.append(dict(name='missing_anchor_has_no_fabricated_interval_bound', passed=True, observed=absent))

    # A zero-total overlapping observation can constrain the first bin even
    # when that second observation is outside the query. The declared global
    # disjoint-bin contract must be checked before dropping nonintersections.
    overlapping = [dict(rows[0]), dict(rows[1], t=5, value=0)]
    conflict = decide(overlapping, dict(known, start=0, end=5), 'exact_clock_window')
    assert conflict['action'] == 'refuse_exact_answer' and conflict['sql_executions'] == 0, conflict
    assert 'admissible_energy_wh' not in conflict, conflict
    checks.append(dict(name='nonintersecting_bin_still_invalidates_global_disjoint_contract',
                       passed=True, observed=conflict))
    print(json.dumps(dict(kind='independent_local_boundary_checks', check_count=len(checks),
                          passed=True, checks=checks, wall_seconds=perf_counter()-started,
                          scope='Constructed cases only; no new empirical comparison or learning trial.'), indent=2))


if __name__ == '__main__':
    main()
