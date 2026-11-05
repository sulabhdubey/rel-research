"""Coordinator-authored applicability routing around two historical SQL methods.

This fixed teaching example is not an autonomous learner or arbitrary-code sandbox.
"""
from copy import deepcopy
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

from runtime import Engine

HERE = Path(__file__).resolve().parent


def finite(value):
    return type(value) in (int, float) and math.isfinite(value)


def load_methods():
    raw = (HERE / 'methods.json').read_bytes()
    provenance = json.loads((HERE / 'PROVENANCE.json').read_text(encoding='utf-8'))
    if hashlib.sha256(raw).hexdigest() != provenance['bundle_sha256']:
        raise ValueError('Saved method identity changed; review before execution.')
    return json.loads(raw)


def validate(rows, context):
    if not isinstance(context, dict):
        raise ValueError('Current context must be explicit.')
    expected = {'family': 'energy', 'schema_version': 1,
                'revision_policy': 'latest_available_then_quality'}
    if any(context.get(key) != value for key, value in expected.items()) or type(context.get('schema_version')) is not int:
        raise ValueError('Unsupported family, schema or revision semantics.')
    if context.get('unit') not in ('Wh', 'W') or context.get('quality_rule') not in ('binary', 'graded'):
        raise ValueError('Unsupported or missing units/quality rule.')
    for key in ('as_of', 'start', 'end', 'calibration_gain', 'calibration_offset'):
        if key not in context or not finite(context[key]):
            raise ValueError('Missing or nonfinite current field: ' + key)
    if context['end'] < context['start']:
        raise ValueError('Window is reversed.')
    if not isinstance(rows, list) or not rows or len(rows) > 20000:
        raise ValueError('A bounded nonempty observation list is required.')
    fields = {'sample_id', 'revision', 'available', 't', 'duration', 'value', 'quality'}
    identities = set()
    for row in rows:
        if set(row) != fields:
            raise ValueError('Observation fields differ.')
        if type(row['sample_id']) is not int or type(row['revision']) is not int:
            raise ValueError('Sample and revision identities must be integers.')
        identity = (row['sample_id'], row['revision'])
        if identity in identities:
            raise ValueError('Ambiguous duplicate sample/revision identity.')
        identities.add(identity)
        if any(not finite(row[k]) for k in ('available', 't', 'duration')):
            raise ValueError('Nonfinite observation support.')
        if row['value'] is not None and not finite(row['value']):
            raise ValueError('Nonfinite reading.')
        if type(row['quality']) is not int or row['quality'] not in (0, 1, 2):
            raise ValueError('Unsupported quality code.')


def eligible(rows, context):
    latest = {}
    for row in rows:
        if row['available'] <= context['as_of']:
            prior = latest.get(row['sample_id'])
            if prior is None or row['revision'] > prior['revision']:
                latest[row['sample_id']] = row
    return [r for r in latest.values() if r['duration'] > 0 and r['value'] is not None
            and (r['quality'] == 1 or context['quality_rule'] == 'graded' and r['quality'] == 2)]


def energy_wh(row, context):
    # Decimal strings preserve the explicitly supplied decimal input contract.
    q = lambda x: Fraction(str(x))
    value = q(context['calibration_gain']) * q(row['value']) + q(context['calibration_offset'])
    return value if context['unit'] == 'Wh' else value * q(row['duration']) / 60


def refused(reason, **extras):
    return {'action': 'refuse_exact_answer', 'reason': reason,
            'sql_executions': 0, 'model_calls': 0, **extras}


def clock_answer(rows, context):
    q = lambda x: Fraction(str(x))
    start, end = q(context['start']), q(context['end'])
    if start == end:
        return {'action': 'answer_from_interval_totals', 'energy_wh': '0',
                'reason': 'Empty interval; no measurement support is needed.', 'sql_executions': 0, 'model_calls': 0}
    if context.get('interval_anchor') != 'start' or context.get('interval_totals_measured') is not True:
        return refused('Interval support is not established; timestamp labels alone do not define an integral.')
    if context.get('power_nonnegative') is not True:
        return refused('The nonnegative-power bound is not authorized by the current source contract.')
    bins = sorted((q(r['t']), q(r['t']) + q(r['duration']), energy_wh(r, context))
                  for r in eligible(rows, context))
    # The stated model applies to the supplied observations, not merely those
    # intersecting Q. An overlapping bin outside Q may constrain an inside bin.
    if any(energy < 0 for _, _, energy in bins):
        return refused('Negative bin energy contradicts the granted nonnegative-power model.')
    if any(right[0] < left[1] for left, right in zip(bins, bins[1:])):
        return refused('Overlapping intervals are outside this disjoint-bin demonstration contract.')
    relevant = [b for b in bins if b[0] < end and b[1] > start]
    cursor, lower, upper = start, Fraction(0), Fraction(0)
    for left, right, energy in relevant:
        if energy < 0:
            return refused('Negative bin energy contradicts the granted nonnegative-power model.')
        if max(start, left) > cursor:
            return refused('The requested interval includes unobserved or ineligible time; no finite bound is established.')
        if min(end, right) <= cursor or left < cursor and cursor != start:
            return refused('Overlapping intervals are outside this disjoint-bin demonstration contract.')
        cursor = min(end, right)
        upper += energy
        if left >= start and right <= end:
            lower += energy
    if cursor < end:
        return refused('The requested interval includes unobserved or ineligible time; no finite bound is established.')
    if lower == upper:
        return {'action': 'answer_from_interval_totals', 'energy_wh': str(lower),
                'reason': 'All positive-energy contributions are fully determined by complete observed bins.',
                'sql_executions': 0, 'model_calls': 0}
    return refused('Within-bin distribution is missing; recomputation of the same totals cannot give an exact answer.',
                   admissible_energy_wh=[str(lower), str(upper)],
                   bound_scope='Known disjoint bins, complete query coverage, nonnegative power and no peak/shape constraint.')


def decide(rows, context, requirement='whole_rows'):
    """Explicit teaching policy; v1/v2 adaptation is selection, not new learning."""
    validate(rows, context)
    if requirement == 'exact_clock_window':
        return clock_answer(rows, context)
    if requirement != 'whole_rows':
        raise ValueError('Unsupported requested quantity.')
    methods = load_methods()
    compatible_v1 = (context['unit'] == 'Wh' and context['quality_rule'] == 'binary'
                     and context['calibration_gain'] == 1 and context['calibration_offset'] == 0)
    key = 'v1' if compatible_v1 else 'v2'
    method = methods[key]
    if any(context.get(k) != v for k, v in method['guard'].items()):
        raise ValueError('Historical method guard mismatch.')
    if any(k not in context for k in method['context_fields']):
        raise ValueError('Historical method context missing.')
    # v1 had no typed bindings; this three-field binding bridge is authored here.
    params = {k: context[k] for k in ('as_of', 'start', 'end')} if key == 'v1' else {
        k: context[v['field']] for k, v in method['bindings'].items()}
    engine = Engine(rows)
    try:
        executed = engine.query(method['sql'], params)
    finally:
        engine.con.close()
    return {'action': 'reuse_saved_method' if key == 'v1' else 'adapt_with_retained_method',
            'method_id': method['id'], 'result': executed['rows'][0], 'sql_executions': 1,
            'sql_wall_seconds': executed['wall_seconds'], 'sql_steps_approx': executed['sql_steps_approx'],
            'model_calls': 0, 'reason': 'Original whole-row contract holds.' if key == 'v1' else
            'Current unit/quality/calibration contract requires the already acquired parameterized method.'}


def fixture():
    rows = [{'sample_id': i, 'revision': 0, 'available': 0, 't': i*10,
             'duration': 10, 'value': value, 'quality': 1} for i, value in enumerate((10, 20))]
    context = {'family': 'energy', 'schema_version': 1, 'revision_policy': 'latest_available_then_quality',
               'unit': 'Wh', 'quality_rule': 'binary', 'as_of': 50, 'start': 0, 'end': 20,
               'calibration_gain': 1, 'calibration_offset': 0}
    return rows, context


def sequence():
    rows, c = fixture()
    return [
        {'case': 'reuse', 'decision': decide(deepcopy(rows), c)},
        {'case': 'adapt', 'decision': decide(deepcopy(rows), {**c, 'calibration_gain': 1.25, 'calibration_offset': 7})},
        {'case': 'refuse', 'decision': decide(deepcopy(rows), {**c, 'start': 5, 'end': 15,
             'interval_anchor': 'start', 'interval_totals_measured': True, 'power_nonnegative': True}, 'exact_clock_window')}
    ]
