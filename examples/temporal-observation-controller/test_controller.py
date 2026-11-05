"""Hand-authored verification; no empirical dataset or network access."""
from dataclasses import replace
import itertools
import json
from pathlib import Path
import subprocess
import sys
import unittest

from temporal_controller import Event, FactMemory, Query, Scope, decide, identity, verify_witness


def reference_reachable(events, query, values):
    """Independent state-space search: scan every eligible next event per state.

    No weighted-path search, controller pruning, or controller bound code is used.
    """
    frontier = [(query.source, query.start)]
    visited = set(frontier)
    while frontier:
        node, arrival = frontier.pop()
        if node == query.target:
            return True
        for event in events:
            departure = event.t - 20 if query.mode == "duration20" else event.t
            if not values[event.id] or departure < arrival or event.t > query.deadline:
                continue
            if node not in (event.u, event.v):
                continue
            other = event.v if node == event.u else event.u
            state = (other, event.t)
            if state not in visited:
                visited.add(state)
                frontier.append(state)
    return False


class ControllerTests(unittest.TestCase):
    def solve(self, events, query, truth, *, memory=None, policy="lazy", **kwargs):
        memory = memory if memory is not None else FactMemory(events, "fixture", "v1")
        calls = []
        def fetch(event_id):
            calls.append(event_id)
            return truth[event_id]
        result = decide(events, query, fetch, memory, source_id="fixture", version="v1",
                        complete=kwargs.pop("complete", True), policy=policy, **kwargs)
        self.assertEqual(calls, [event_id for event_id, _ in result.requests])
        self.assertEqual(len(calls), len(set(calls)))
        return result, memory

    def test_same_slot_modes_disagree(self):
        events = (Event(0, 20, 0, 1), Event(1, 20, 1, 2))
        for policy in ("lazy", "eager"):
            self.assertIs(self.solve(events, Query(0, 2, 0, 20), {0: 1, 1: 1}, policy=policy)[0].answer, False)
            self.assertIs(self.solve(events, Query(0, 2, 0, 20, "instant"), {0: 1, 1: 1}, policy=policy)[0].answer, True)

    def test_overlapping_intervals_cannot_chain(self):
        events = (Event(0, 20, 0, 1), Event(1, 30, 1, 2))
        result, _ = self.solve(events, Query(0, 2, 0, 40), {0: 1, 1: 1})
        self.assertIs(result.answer, False)
        self.assertEqual(result.requests, ())

    def test_paid_absence_and_incomplete_refutation(self):
        events = (Event(0, 20, 0, 1),)
        for policy, complete in itertools.product(("lazy", "eager"), (True, False)):
            result, _ = self.solve(events, Query(0, 1, 0, 20), {0: 0}, policy=policy, complete=complete)
            self.assertIs(result.answer, False if complete else None)
            self.assertEqual(result.requests, ((0, 0),))
            self.assertEqual(result.reason, "complete_upper_refutation" if complete else "incomplete_envelope")

    def test_incomplete_positive_is_permitted(self):
        result, _ = self.solve((Event(0, 20, 0, 1),), Query(0, 1, 0, 20), {0: 1}, complete=False)
        self.assertIs(result.answer, True)

    def test_disconnected_empty_and_identity_queries(self):
        for policy, complete in itertools.product(("lazy", "eager"), (True, False)):
            result, _ = self.solve((), Query(0, 1, 0, 20), {}, policy=policy, complete=complete)
            self.assertIs(result.answer, False if complete else None)
            same, _ = self.solve((), Query(0, 0, 0, 0), {}, policy=policy, complete=complete)
            self.assertIs(same.answer, True)
            self.assertEqual(same.witness, ())
            self.assertEqual(same.requests, ())

    def test_eager_honors_cached_bounds_before_acquisition(self):
        events = (Event(0, 20, 0, 1), Event(1, 40, 1, 2))
        memory = FactMemory(events, "fixture", "v1")
        memory.put(0, 0)
        result, _ = self.solve(events, Query(0, 2, 0, 40), {0: 0, 1: 1}, memory=memory, policy="eager")
        self.assertIs(result.answer, False)
        self.assertEqual(result.requests, ())
        result, _ = self.solve(events, Query(0, 0, 0, 40), {}, policy="eager")
        self.assertEqual(result.requests, ())

    def test_query_changes_recompute_bounds_reuse_facts(self):
        events = (Event(0, 20, 0, 1), Event(1, 40, 1, 2))
        result, memory = self.solve(events, Query(0, 2, 0, 40), {0: 1, 1: 1})
        self.assertIs(result.answer, True)
        for query, expected in ((Query(0, 2, 1, 40), False), (Query(0, 2, 0, 39), False),
                                (Query(0, 1, 0, 40), True), (Query(2, 0, 0, 40), False)):
            changed, _ = self.solve(events, query, {}, memory=memory)
            self.assertIs(changed.answer, expected)
            self.assertEqual(changed.requests, ())

    def test_budget_unknown_and_known_answer_at_zero_budget(self):
        events = (Event(0, 20, 0, 1), Event(1, 40, 1, 2))
        for policy in ("lazy", "eager"):
            result, memory = self.solve(events, Query(0, 2, 0, 40), {0: 1, 1: 1}, budget=1, policy=policy)
            self.assertIsNone(result.answer)
            self.assertEqual(len(result.requests), 1)
            self.assertEqual(result.reason, "budget_exhausted")
            done, memory = self.solve(events, Query(0, 2, 0, 40), {0: 1, 1: 1}, memory=memory, policy=policy)
            self.assertIs(done.answer, True)
            cached, _ = self.solve(events, Query(0, 2, 0, 40), {}, memory=memory, budget=0, policy=policy)
            self.assertIs(cached.answer, True)
            self.assertEqual(cached.requests, ())

    def test_lazy_uses_minimum_unknown_path(self):
        events = (Event(0, 20, 0, 1), Event(1, 20, 0, 2), Event(2, 40, 1, 3),
                  Event(3, 40, 2, 4), Event(4, 60, 4, 3))
        memory = FactMemory(events, "fixture", "v1")
        memory.put(1, 1)
        memory.put(3, 1)
        result, _ = self.solve(events, Query(0, 3, 0, 60), {4: 1}, memory=memory)
        self.assertEqual(result.requests, ((4, 1),))
        self.assertEqual(result.witness, (1, 3, 4))

    def test_false_path_replans(self):
        events = (Event(0, 20, 0, 1), Event(1, 20, 0, 2), Event(2, 40, 1, 3), Event(3, 40, 2, 3))
        result, _ = self.solve(events, Query(0, 3, 0, 40), {0: 0, 1: 1, 2: 1, 3: 1})
        self.assertIs(result.answer, True)
        self.assertEqual(result.requests, ((0, 0), (1, 1), (3, 1)))

    def test_scope_change_rejected_before_fetch(self):
        events = (Event(0, 20, 0, 1),)
        memory = FactMemory(events, "fixture", "v1")
        memory.put(0, 1)
        cases = ((events, "different-source", "v1"), (events, "fixture", "v2"),
                 ((Event(0, 40, 0, 1),), "fixture", "v1"))
        for changed, source_id, version in cases:
            with self.assertRaisesRegex(ValueError, "scope"):
                decide(changed, Query(0, 1, 0, 40), self.fail, memory,
                       source_id=source_id, version=version, complete=True)

    def test_fact_conflicts_unknown_ids_and_readonly_view(self):
        memory = FactMemory((Event(0, 20, 0, 1),), "fixture", "v1")
        memory.put(0, 1)
        memory.put(0, 1)
        for event_id, value in ((0, 0), (1, 1), (True, 1), (0, True), (0, 1.0), (0, "1")):
            with self.assertRaises(ValueError):
                memory.put(event_id, value)
        with self.assertRaises(TypeError):
            memory.facts[0] = 0

    def test_invalid_inputs_rejected_before_fetch(self):
        events = (Event(0, 20, 0, 1),)
        query = Query(0, 1, 0, 20)
        memory = FactMemory(events, "fixture", "v1")
        bad_events = ((Event(0, 20, 0, 1), Event(0, 40, 1, 2)), (Event(True, 20, 0, 1),),
                      (Event(0, 20.0, 0, 1),), (Event(-1, 20, 0, 1),), (Event(0, 20, 1, 1),),
                      (Event(0, 40, 0, 1), Event(1, 20, 1, 2)))
        for rows in bad_events:
            with self.assertRaises(ValueError):
                decide(rows, query, self.fail, memory, source_id="fixture", version="v1", complete=True)
        for bad_query in (replace(query, source=True), replace(query, start=1.0),
                          replace(query, mode="unknown"), replace(query, start=21)):
            with self.assertRaises(ValueError):
                decide(events, bad_query, self.fail, memory, source_id="fixture", version="v1", complete=True)
        for bad_budget in (-1, True, 1.0, float("nan"), float("inf"), "1"):
            with self.assertRaises(ValueError):
                decide(events, query, self.fail, memory, source_id="fixture", version="v1", complete=True, budget=bad_budget)
        for complete in (1, 0, "true", None):
            with self.assertRaises(ValueError):
                decide(events, query, self.fail, memory, source_id="fixture", version="v1", complete=complete)
        with self.assertRaises(ValueError):
            decide(events, query, self.fail, memory, source_id="fixture", version="v1", complete=True, policy="learned")

    def test_invalid_fetch_value_preserves_previous_facts(self):
        events = (Event(0, 20, 0, 1), Event(1, 40, 1, 2))
        for invalid in (True, 1.0, "1", None, -1, 2):
            memory = FactMemory(events, "fixture", "v1")
            with self.assertRaises(ValueError):
                self.solve(events, Query(0, 2, 0, 40), {0: 1, 1: invalid}, memory=memory)
            self.assertEqual(dict(memory.facts), {0: 1})

    def test_callback_failure_preserves_valid_acquisitions(self):
        events = (Event(0, 20, 0, 1), Event(1, 40, 1, 2))
        memory = FactMemory(events, "fixture", "v1")
        def fetch(event_id):
            if event_id == 1:
                raise RuntimeError("fixture source unavailable")
            return 1
        with self.assertRaises(RuntimeError):
            decide(events, Query(0, 2, 0, 40), fetch, memory, source_id="fixture", version="v1", complete=True)
        self.assertEqual(dict(memory.facts), {0: 1})
        result, _ = self.solve(events, Query(0, 2, 0, 40), {1: 1}, memory=memory)
        self.assertEqual(result.requests, ((1, 1),))

    def test_strict_checkpoint_restore(self):
        events = (Event(0, 20, 0, 1),)
        memory = FactMemory(events, "fixture", "v1")
        memory.put(0, 1)
        text = memory.to_json()
        self.assertEqual(FactMemory.from_json(text, events, "fixture", "v1").to_json(), text)
        packet = json.loads(text)
        mutations = [dict(packet, facts=[[0, 1], [0, 1]]), dict(packet, facts=[[2, 1]]),
                     dict(packet, facts=[[True, 1]]), dict(packet, facts=[[0, True]]),
                     dict(packet, facts=[[0, 1.0]]), dict(packet, facts=[[0]]),
                     dict(packet, facts={}), dict(packet, schema="unknown"),
                     dict(packet, unexpected="data"), {key: value for key, value in packet.items() if key != "facts"}]
        invalid_texts = [json.dumps(value) for value in mutations]
        invalid_texts += [text[:-1], "[]", '"text"', text.replace('"facts":', '"facts":[],"facts":', 1),
                          text.replace('[[0,1]]', '[[0,NaN]]')]
        for invalid in invalid_texts:
            with self.assertRaises(ValueError, msg=invalid):
                FactMemory.from_json(invalid, events, "fixture", "v1")
        for source_id, version in (("other", "v1"), ("fixture", "v2")):
            with self.assertRaisesRegex(ValueError, "scope"):
                FactMemory.from_json(text, events, source_id, version)
        with self.assertRaisesRegex(ValueError, "scope"):
            FactMemory.from_json(text, (Event(0, 40, 0, 1),), "fixture", "v1")

    def test_scope_labels_and_envelope_hash(self):
        for source_id, version in (("", "v1"), ("fixture", ""), (None, "v1"), ("fixture", 1)):
            with self.assertRaises(ValueError):
                FactMemory((), source_id, version)
        with self.assertRaises(ValueError):
            Scope("fixture", "v1", "not-a-hash")
        self.assertNotEqual(identity((Event(0, 20, 0, 1),)), identity((Event(0, 40, 0, 1),)))

    def test_witness_rejects_wrong_order_missing_false_and_bool_facts(self):
        events = (Event(0, 20, 0, 1), Event(1, 40, 1, 2))
        query = Query(0, 2, 0, 40)
        self.assertTrue(verify_witness(events, query, (0, 1), {0: 1, 1: 1}))
        for witness, facts in (((1, 0), {0: 1, 1: 1}), ((0, 1), {0: 1}),
                               ((0, 1), {0: 1, 1: 0}), ((0, 1), {0: True, 1: 1}),
                               ((0, 2), {0: 1, 2: 1}), ((False, 1), {0: 1, 1: 1})):
            self.assertFalse(verify_witness(events, query, witness, facts))

    def test_actual_child_process_restart(self):
        events = (Event(0, 20, 0, 1), Event(1, 40, 1, 2))
        memory = FactMemory(events, "fixture", "v1")
        memory.put(0, 1)
        script = """import json,sys
from temporal_controller import Event,Query,FactMemory,decide
events=(Event(0,20,0,1),Event(1,40,1,2))
memory=FactMemory.from_json(sys.stdin.read(),events,'fixture','v1')
calls=[]
def fetch(eid):
    calls.append(eid)
    return 1
result=decide(events,Query(0,2,0,40),fetch,memory,source_id='fixture',version='v1',complete=True)
print(json.dumps({'answer':result.answer,'calls':calls,'checkpoint':memory.to_json()}))
"""
        child = subprocess.run([sys.executable, "-B", "-c", script], input=memory.to_json(),
                               text=True, capture_output=True, check=True,
                               cwd=Path(__file__).resolve().parent, timeout=15)
        restored = json.loads(child.stdout)
        self.assertIs(restored["answer"], True)
        self.assertEqual(restored["calls"], [1])
        after = FactMemory.from_json(restored["checkpoint"], events, "fixture", "v1")
        self.assertEqual(dict(after.facts), {0: 1, 1: 1})
        self.assertEqual(dict(memory.facts), {0: 1})

    def test_exhaustive_truth_masks_bounds_and_budget(self):
        events = (Event(0, 20, 0, 1), Event(1, 20, 1, 2), Event(2, 40, 0, 2),
                  Event(3, 40, 2, 3), Event(4, 60, 1, 3), Event(5, 60, 0, 3))
        for mask, mode, policy, budget in itertools.product(
            itertools.product((0, 1), repeat=6), ("duration20", "instant"), ("lazy", "eager"), (0, 1, None)
        ):
            truth = dict(enumerate(mask))
            query = Query(0, 3, 0, 60, mode)
            expected = reference_reachable(events, query, truth)
            result, memory = self.solve(events, query, truth, policy=policy, budget=budget)
            with self.subTest(mask=mask, mode=mode, policy=policy, budget=budget):
                lower = reference_reachable(events, query, {event.id: memory.facts.get(event.id, 0) == 1 for event in events})
                upper = reference_reachable(events, query, {event.id: memory.facts.get(event.id) != 0 for event in events})
                self.assertLessEqual(lower, expected)
                self.assertLessEqual(expected, upper)
                if result.answer is True:
                    self.assertTrue(expected and lower)
                    self.assertTrue(verify_witness(events, query, result.witness, memory.facts))
                elif result.answer is False:
                    self.assertFalse(expected or upper)
                else:
                    self.assertIsNotNone(budget)
                    self.assertFalse(lower)
                    self.assertTrue(upper)
                if budget is None:
                    self.assertEqual(result.answer, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
