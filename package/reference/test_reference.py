"""Source-free engineering checks; Python standard library plus NumPy only.

Run from this folder: python -B test_reference.py --report ../TESTS.json
The report appends attempts so an initial failure is not erased by a repair.
Synthetic observations here are explicitly fixtures, not authenticated sensor data.
"""
import argparse
import copy
import hashlib
import inspect
import json
import math
from pathlib import Path
import sys
import time
import unittest
from unittest import mock
from datetime import datetime, timezone

import numpy as np

from example import fixture
from rel_localization import runner


class ReferenceTests(unittest.TestCase):
    def setUp(self):
        self.packet, self.reference = fixture()

    def assert_poses_equal(self, left, right):
        self.assertEqual(set(left), set(right))
        for name in left:
            np.testing.assert_array_equal(left[name], right[name], err_msg=name)

    def test_five_outputs_share_endpoint_and_observation_support(self):
        result = runner.predict(self.packet)
        self.assertEqual(set(result['poses']), {'robust', 'J1', 'J2', 'J1-mean', 'J2-mean'})
        expected_times = np.arange(.5, self.packet['duration'], .5)
        expected_count = sum(row[0] <= expected_times[-1] for row in self.packet['observations'])
        for name, rows in result['poses'].items():
            with self.subTest(policy=name):
                a = np.asarray(rows)
                self.assertEqual(a.shape, (len(expected_times), 4))
                self.assertTrue(np.isfinite(a).all())
                np.testing.assert_array_equal(a[:, 0], expected_times)
        for name, counts in result['counts'].items():
            with self.subTest(component=name):
                self.assertEqual(counts['observations_consumed'], expected_count)
                self.assertEqual(counts['engine_calls_this_invocation'], 0 if name == 'robust' else expected_count)

    def test_prediction_has_no_reference_input_and_scoring_does_not_mutate_it(self):
        self.assertNotIn('reference', inspect.signature(runner.predict).parameters)
        forbidden = copy.deepcopy(self.packet)
        forbidden['reference'] = self.reference
        with self.assertRaises(ValueError):
            runner.predict(forbidden)
        packet_before = copy.deepcopy(self.packet)
        result = runner.predict(self.packet)
        before = copy.deepcopy(result['poses'])
        score = runner.evaluate(result['poses'], self.reference)
        shifted = copy.deepcopy(self.reference)
        for row in shifted:
            row[1] += 20.
        shifted_score = runner.evaluate(result['poses'], shifted)
        self.assertNotEqual(score['robust']['mse_m2'], shifted_score['robust']['mse_m2'])
        self.assertEqual(self.packet, packet_before)
        self.assert_poses_equal(before, result['poses'])
        self.assert_poses_equal(before, runner.predict(self.packet)['poses'])

    def test_future_observation_and_motion_changes_do_not_change_past_poses(self):
        cut = 4.
        changed = copy.deepcopy(self.packet)
        for row in changed['observations']:
            if row[0] > cut:
                row[2] += 2.
                row[3] = float((row[3] + .2 + np.pi) % (2*np.pi) - np.pi)
        for row in changed['odometry']:
            if row[0] > cut:
                row[1] += .4
                row[2] -= .1
        a, b = runner.predict(self.packet), runner.predict(changed)
        for name in a['poses']:
            with self.subTest(policy=name):
                x, y = np.asarray(a['poses'][name]), np.asarray(b['poses'][name])
                np.testing.assert_array_equal(x[x[:, 0] <= cut], y[y[:, 0] <= cut])
        self.assertFalse(np.array_equal(a['poses']['robust'], b['poses']['robust']))

    def test_serialized_restart_matches_uninterrupted_for_multiple_boundaries(self):
        complete = runner.predict(self.packet)
        for cut in (.5, 4., 7.5):
            with self.subTest(cut=cut):
                partial = runner.predict(self.packet, stop_at=cut)
                checkpoints = json.loads(json.dumps(partial['checkpoints'], allow_nan=False))
                resumed = runner.predict(self.packet, checkpoints=checkpoints)
                self.assert_poses_equal(complete['poses'], resumed['poses'])
                for name in complete['counts']:
                    self.assertEqual(complete['counts'][name]['observations_consumed'], resumed['counts'][name]['observations_consumed'])
                    self.assertEqual(complete['counts'][name]['rejected'], resumed['counts'][name]['rejected'])
                    self.assertEqual(complete['checkpoints'][name], resumed['checkpoints'][name])

    def test_restart_preserves_supplied_checkpoint_and_is_repeatable(self):
        partial = runner.predict(self.packet, stop_at=4.)
        checkpoints = json.loads(json.dumps(partial['checkpoints'], allow_nan=False))
        original = copy.deepcopy(checkpoints)
        first = runner.predict(self.packet, checkpoints=checkpoints)
        self.assertEqual(checkpoints, original, 'resuming must not mutate the supplied saved checkpoint')
        second = runner.predict(self.packet, checkpoints=checkpoints)
        self.assert_poses_equal(first['poses'], second['poses'])

    def test_checkpoint_input_and_method_mismatch_rejected(self):
        checkpoints = runner.predict(self.packet, stop_at=4.)['checkpoints']
        changed = copy.deepcopy(self.packet)
        changed['observations'][-1][2] += .01
        with self.assertRaisesRegex(ValueError, 'mismatch'):
            runner.predict(changed, checkpoints=copy.deepcopy(checkpoints))
        swapped = copy.deepcopy(checkpoints)
        swapped['J1'], swapped['J2'] = swapped['J2'], swapped['J1']
        with self.assertRaisesRegex(ValueError, 'mismatch'):
            runner.predict(self.packet, checkpoints=swapped)
        with self.assertRaises(ValueError):
            runner.predict(self.packet, checkpoints={'robust': checkpoints['robust']})

    def test_checkpoint_retrograde_stop_and_misaligned_bank_rejected(self):
        checkpoints = runner.predict(self.packet, stop_at=4.)['checkpoints']
        for stop in (.5, 3.5, 4.):
            with self.subTest(stop=stop):
                with self.assertRaises(ValueError):
                    runner.predict(self.packet, checkpoints=copy.deepcopy(checkpoints), stop_at=stop)
        earlier = runner.predict(self.packet, stop_at=3.)['checkpoints']
        mixed = copy.deepcopy(checkpoints)
        mixed['J1'] = earlier['J1']
        with self.assertRaises(ValueError):
            runner.predict(self.packet, checkpoints=mixed)

    def test_checkpoint_malformed_rows_and_state_rejected(self):
        checkpoints = runner.predict(self.packet, stop_at=4.)['checkpoints']
        cases = []
        for label, field, value in (
            ('state shape', 'x', [0., 0.]),
            ('nonfinite covariance', 'p', [[math.nan, 0., 0.], [0., 1., 0.], [0., 0., 1.]]),
            ('row shape', 'rows', [[.5, 0., 0., 0.]]),
            ('row time mismatch', 't', 3.5),
        ):
            changed = copy.deepcopy(checkpoints)
            changed['robust'][field] = value
            cases.append((label, changed))
        for label, changed in cases:
            with self.subTest(case=label):
                with self.assertRaises(ValueError):
                    runner.predict(self.packet, checkpoints=changed)

    def test_declared_semantic_mismatch_rejected_without_provenance_claim(self):
        for key, value in (
            ('distance_unit', 'centimetre'), ('angle_unit', 'degree'),
            ('clock', 'wall_clock'), ('motion', 'spatial_holonomic'),
            ('odometry_origin', 'reference_derivative'),
            ('measurement_origin', 'reference_generated_bearing'),
            ('identity_availability', 'offline_truth_association'),
            ('map_availability', 'built_from_confirmation_truth'),
            ('initialization', 'future_reference'),
        ):
            with self.subTest(field=key):
                changed = copy.deepcopy(self.packet)
                changed['semantics'][key] = value
                with self.assertRaises(ValueError):
                    runner.predict(changed)
        # Passing a fixture with allowed declarations proves schema behavior only.
        # It cannot establish that any numeric values came from physical sensors.
        self.assertIn('do not authenticate provenance', runner.predict(self.packet)['scope'])

    def test_invalid_shape_nonfinite_units_and_identity_rejected(self):
        cases = []
        def case(label, mutate):
            changed = copy.deepcopy(self.packet)
            mutate(changed)
            cases.append((label, changed))
        case('initial shape', lambda p: p.update(initial=[0., 0.]))
        case('initial nonfinite', lambda p: p.update(initial=[0., math.nan, 0.]))
        case('initial heading', lambda p: p.update(initial=[0., 0., 180.]))
        case('odometry shape', lambda p: p.update(odometry=[[0., 1.]]))
        case('observation shape', lambda p: p.update(observations=[[.5, 6, 1.]]))
        case('nonfinite measurement', lambda p: p['observations'][0].__setitem__(2, math.inf))
        case('bearing units', lambda p: p['observations'][0].__setitem__(3, 90.))
        case('nonpositive range', lambda p: p['observations'][0].__setitem__(2, 0.))
        case('fractional ID', lambda p: p['observations'][0].__setitem__(1, 6.5))
        case('unknown ID', lambda p: p['observations'][0].__setitem__(1, 999))
        case('map coordinates', lambda p: p.update(landmarks={'6': [1., 2., 3.]}))
        case('map canonical ID', lambda p: p.update(landmarks={'06': [1., 2.]}))
        case('empty map', lambda p: p.update(landmarks={}))
        for label, changed in cases:
            with self.subTest(case=label):
                with self.assertRaises(ValueError):
                    runner.predict(changed)

    def test_time_order_support_and_stop_endpoint_rejected(self):
        cases = []
        def case(label, mutate):
            changed = copy.deepcopy(self.packet)
            mutate(changed)
            cases.append((label, changed))
        case('initial control late', lambda p: p['odometry'][0].__setitem__(0, .1))
        case('negative observation', lambda p: p['observations'][0].__setitem__(0, -.1))
        case('observation past duration', lambda p: p['observations'][-1].__setitem__(0, 9.))
        case('unordered observations', lambda p: p['observations'].__setitem__(slice(0, 2), list(reversed(p['observations'][:2]))))
        case('unordered motion', lambda p: p['odometry'].__setitem__(slice(1, 3), list(reversed(p['odometry'][1:3]))))
        case('no endpoint duration', lambda p: p.update(duration=.5))
        for label, changed in cases:
            with self.subTest(case=label):
                with self.assertRaises(ValueError):
                    runner.predict(changed)
        for stop in (0., .75, self.packet['duration'], math.inf):
            with self.subTest(stop=stop):
                with self.assertRaises(ValueError):
                    runner.predict(self.packet, stop_at=stop)

    def test_empty_measurements_and_tied_events_are_causal_valid_cases(self):
        empty = copy.deepcopy(self.packet)
        empty['observations'] = []
        result = runner.predict(empty)
        for name in result['counts']:
            self.assertEqual(result['counts'][name]['observations_consumed'], 0)
            np.testing.assert_array_equal(result['poses']['robust'], result['poses'][name])
        tied = copy.deepcopy(self.packet)
        tied['observations'].insert(1, list(tied['observations'][0]))
        result = runner.predict(tied)
        self.assertEqual({c['observations_consumed'] for c in result['counts'].values()}, {16})

    def test_equal_mean_squared_error_identity(self):
        output = runner.predict(self.packet)['poses']
        r = np.asarray(output['robust'])[:, 1:3]
        truth = np.column_stack([np.interp(np.asarray(output['robust'])[:, 0], np.asarray(self.reference)[:, 0], np.asarray(self.reference)[:, k]) for k in (1, 2)])
        for name in ('J1', 'J2'):
            with self.subTest(replica=name):
                j = np.asarray(output[name])[:, 1:3]
                m = np.asarray(output[name+'-mean'])[:, 1:3]
                np.testing.assert_allclose(m, (r+j)/2, rtol=0, atol=0)
                left = np.sum((m-truth)**2, axis=1)
                right = (np.sum((r-truth)**2, axis=1)+np.sum((j-truth)**2, axis=1))/2-np.sum((r-j)**2, axis=1)/4
                np.testing.assert_allclose(left, right, rtol=1e-12, atol=1e-14)

    def test_circular_heading_wrap_and_antipodal_fallback(self):
        # Isolate readout algebra with valid synthetic component output rows.
        def fake_run(record, config, engine=None, **kwargs):
            if engine is None:
                headings = [math.pi-.1, .2]
            else:
                headings = [-math.pi+.1, .2-math.pi]
            return {'checkpoint': {'rows': [[.5, 0., 0., headings[0], 1., 1., 0., 0.], [1., 0., 0., headings[1], 1., 1., 0., 0.]]}, 'measurements': 0, 'rejected': 0}
        with mock.patch.object(runner.frozen_filter, 'run', side_effect=fake_run):
            output = runner.predict(self.packet)['poses']
        for name in ('J1-mean', 'J2-mean'):
            self.assertAlmostEqual(abs(output[name][0][3]), math.pi)
            self.assertEqual(output[name][1][3], .2)

    def test_scoring_known_errors_episodes_quantile_and_wrapped_heading(self):
        distances = np.array([0., .6, .8, 0., .7, 0.])
        times = np.arange(1, 7)*.5
        poses = {'known': [[float(t), float(d), 0., -math.pi+.01] for t, d in zip(times, distances)]}
        reference = [[0., 0., 0., math.pi-.01], [3.5, 0., 0., math.pi-.01]]
        result = runner.evaluate(poses, reference)['known']
        self.assertEqual(result['samples'], 6)
        self.assertAlmostEqual(result['mse_m2'], 1.49/6)
        self.assertAlmostEqual(result['rmse_m'], math.sqrt(1.49/6))
        self.assertEqual(result['above_0_5m'], 3)
        self.assertEqual(result['episodes'], 2)
        self.assertAlmostEqual(result['p95_m'], .775)
        self.assertEqual(result['max_m'], .8)
        self.assertAlmostEqual(result['heading_rmse_rad'], .02)

    def test_reference_interpolation_crosses_angle_boundary_circularly(self):
        poses = {'known': [[.5, 1., 2., math.pi]]}
        ref = [[0., 0., 1., math.pi-.1], [1., 2., 3., -math.pi+.1]]
        result = runner.evaluate(poses, ref)['known']
        self.assertEqual(result['mse_m2'], 0.)
        self.assertAlmostEqual(result['heading_rmse_rad'], 0.)

    def test_missing_reference_support_and_invalid_scoring_input_rejected(self):
        poses = {'known': [[.5, 0., 0., 0.], [1., 0., 0., 0.]]}
        references = ([], [[0., 0., 0., 0.]], [[0., 0., 0.], [2., 0., 0.]],
                      [[0., 0., 0., 0.], [0., 0., 0., 0.]],
                      [[.6, 0., 0., 0.], [2., 0., 0., 0.]],
                      [[0., 0., 0., 0.], [.9, 0., 0., 0.]],
                      [[0., 0., 0., 0.], [2., math.nan, 0., 0.]])
        for index, ref in enumerate(references):
            with self.subTest(reference_case=index):
                with self.assertRaises(ValueError):
                    runner.evaluate(poses, ref)
        for raw in ([], [[.5, 0., 0.]], [[.5, 0., 0., 0.], [.5, 0., 0., 0.]], [[.5, math.inf, 0., 0.]]):
            with self.subTest(poses=raw):
                with self.assertRaises(ValueError):
                    runner.evaluate({'bad': raw}, [[0., 0., 0., 0.], [2., 0., 0., 0.]])


class RecordingResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records = []
        self.started = {}

    def startTest(self, test):
        self.started[test.id()] = time.perf_counter()
        super().startTest(test)

    def stopTest(self, test):
        status = 'passed'
        details = []
        for outcome, entries in (('failed', self.failures), ('error', self.errors)):
            for item, detail in entries:
                if item.id() == test.id() or getattr(item, 'test_case', None) is test:
                    status = outcome
                    details.append(detail)
        self.records.append({'test': test.id(), 'status': status, 'wall_seconds': time.perf_counter()-self.started[test.id()], 'details': details})
        super().stopTest(test)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    parser.add_argument('--test', action='append', help='Run a named ReferenceTests method; repeat to select several')
    args = parser.parse_args()
    started_utc = datetime.now(timezone.utc).isoformat()
    start = time.perf_counter()
    cpu_start = time.process_time()
    root = Path(__file__).resolve().parent
    def identities():
        return {str(path.relative_to(root)).replace('\\', '/'): hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(root.rglob('*')) if path.is_file() and path.suffix in {'.py', '.json'} and '__pycache__' not in path.parts}
    before = identities()
    suite = unittest.TestSuite(ReferenceTests(name) for name in args.test) if args.test else unittest.defaultTestLoader.loadTestsFromTestCase(ReferenceTests)
    result = unittest.TextTestRunner(verbosity=2, resultclass=RecordingResult).run(suite)
    after = identities()
    passed = result.wasSuccessful() and before == after
    attempt = {'started_utc': started_utc, 'passed': passed, 'tests_run': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors), 'wall_seconds': time.perf_counter()-start, 'cpu_seconds': time.process_time()-cpu_start, 'timed_scope': 'Test suite and source-identity capture after module imports; excludes interpreter/import startup.', 'tests': result.records, 'sha256_before': before, 'sha256': after, 'sources_unchanged': before == after, 'scope': 'Synthetic source-free engineering only; no raw recordings, external model calls, upstream execution, empirical superiority or physical-provenance proof.'}
    if args.report:
        if args.report.exists():
            report = json.loads(args.report.read_text(encoding='utf8'))
        else:
            report = {'schema': 'run120-source-free-tests-v1', 'attempts': []}
        report['attempts'].append(attempt)
        report['latest_passed'] = attempt['passed']
        report['attempt_count'] = len(report['attempts'])
        args.report.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n', encoding='utf8')
    return 0 if passed else 1


if __name__ == '__main__':
    sys.exit(main())
