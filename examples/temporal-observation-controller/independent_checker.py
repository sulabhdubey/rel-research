"""Independent time-expanded graph audit of the public temporal controller."""
from __future__ import annotations

import argparse
from collections import deque
from datetime import datetime, timezone
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import random
import subprocess
import sys
import time


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expanded_reachable(events, query, allowed):
    """Build explicit node/time vertices, wait arcs and traversal arcs; BFS.

    No production reachability, witness, pruning, or acquisition helpers used.
    """
    duration = 20 if query.mode == "duration20" else 0
    usable = [e for e in events if e.id in allowed
              and query.start <= e.t - duration <= e.t <= query.deadline]
    nodes = {query.source, query.target}
    moments = {query.start, query.deadline}
    for event in usable:
        nodes.update((event.u, event.v))
        moments.update((event.t - duration, event.t))
    moments = sorted(moments)
    adjacency = {(node, moment): [] for node in nodes for moment in moments}
    for node in nodes:
        for before, after in zip(moments, moments[1:]):
            adjacency[node, before].append((node, after))
    for event in usable:
        adjacency[event.u, event.t - duration].append((event.v, event.t))
        adjacency[event.v, event.t - duration].append((event.u, event.t))
    origin = (query.source, query.start)
    seen, queue = {origin}, deque([origin])
    while queue:
        state = queue.popleft()
        if state[0] == query.target:
            return True
        for successor in adjacency[state]:
            if successor not in seen:
                seen.add(successor)
                queue.append(successor)
    return False


def independent_witness(events, query, facts, witness):
    if witness is None:
        return False
    records = {event.id: event for event in events}
    node, at = query.source, query.start
    for event_id in witness:
        if type(event_id) is not int or facts.get(event_id) != 1:
            return False
        event = records[event_id]
        departure = event.t - (20 if query.mode == "duration20" else 0)
        if at > departure or event.t > query.deadline:
            return False
        if node == event.u:
            node = event.v
        elif node == event.v:
            node = event.u
        else:
            return False
        at = event.t
    return node == query.target


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--module-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started, wall, cpu = utc(), time.perf_counter(), time.process_time()
    module_dir = args.module_dir.resolve()
    bindings = {name: sha(module_dir / name) for name in
                ("temporal_controller.py", "test_controller.py", "demo.py", "README.md")}
    spec = importlib.util.spec_from_file_location("audited_temporal_controller", module_dir / "temporal_controller.py")
    tc = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = tc
    spec.loader.exec_module(tc)
    results, failures = [], []
    decisions = checkpoints = 0

    def check(label, fn):
        before = time.perf_counter()
        try:
            detail = fn()
            results.append({"check": label, "status": "pass", "detail": detail,
                            "wall_seconds": time.perf_counter() - before})
        except Exception as error:
            failures.append({"check": label, "type": type(error).__name__, "message": str(error)})
            results.append({"check": label, "status": "fail", "wall_seconds": time.perf_counter() - before})

    def require_rejection(fn):
        try:
            fn()
        except (ValueError, TypeError):
            return
        raise AssertionError("invalid input accepted")

    def one(events, query, truth, prior, complete, budget, policy):
        nonlocal decisions, checkpoints
        memory = tc.FactMemory(events, "audit-source", "v1")
        for event_id in prior:
            memory.put(event_id, truth[event_id])
        before = dict(memory.facts)
        observed = []

        def fetch(event_id):
            assert event_id not in before and event_id not in [r[0] for r in observed]
            observed.append((event_id, truth[event_id]))
            return truth[event_id]

        decision = tc.decide(events, query, fetch, memory, source_id="audit-source",
                             version="v1", complete=complete, budget=budget, policy=policy)
        ids = {event.id for event in events}
        lower = expanded_reachable(events, query, {i for i in ids if memory.facts.get(i) == 1})
        upper = expanded_reachable(events, query, {i for i in ids if memory.facts.get(i) != 0})
        actual = expanded_reachable(events, query, {i for i in ids if truth[i] == 1})
        expected = True if lower else False if complete and not upper else None
        context = {"events": [vars(e) for e in events], "query": vars(query), "truth": truth,
                   "prior": list(prior), "complete": complete, "budget": budget, "policy": policy}
        assert decision.answer is expected, ("wrong or unsupported evidence decision", context, vars(decision))
        if decision.answer is not None:
            assert decision.answer is actual, ("wrong truth answer", context)
        if decision.answer is True:
            assert independent_witness(events, query, memory.facts, decision.witness), context
        else:
            assert decision.witness is None
        assert decision.requests == tuple(observed), context
        assert budget is None or len(observed) <= budget, context
        assert dict(memory.facts) == {**before, **dict(observed)}, context
        decisions += 1
        if decisions % 31 == 0:
            restored = tc.FactMemory.from_json(memory.to_json(), events, "audit-source", "v1")
            repeat = tc.decide(events, query, lambda _: (_ for _ in ()).throw(AssertionError("zero-budget fetch")),
                               restored, source_id="audit-source", version="v1", complete=complete, budget=0)
            assert repeat.answer is expected and not repeat.requests
            checkpoints += 1

    def exhaustive():
        # Different ID orders, negative times/vertices, overlapping and exact-boundary arcs.
        graphs = [
            (tc.Event(91, 0, -2, 5), tc.Event(2, 0, 5, 9), tc.Event(33, 20, -2, 8), tc.Event(74, 40, 8, 9)),
            (tc.Event(31, 20, 0, 1), tc.Event(7, 30, 1, 2), tc.Event(28, 40, 1, 2), tc.Event(12, 60, 2, 3)),
            (tc.Event(17, -1, 0, 1), tc.Event(20, 19, 1, 2), tc.Event(1, 20, 0, 2), tc.Event(55, 40, 2, 3)),
        ]
        qparts = [(-2, 9, -20, 40), (0, 3, 0, 60), (0, 3, -21, 40)]
        start_count = decisions
        for events, parts in zip(graphs, qparts):
            events = tuple(sorted(events, key=lambda event: (event.t, event.id)))
            for mask in itertools.product((0, 1), repeat=4):
                truth = dict(zip([e.id for e in events], mask))
                for mode, complete, policy, budget, prior_index, window_shift in itertools.product(
                        ("instant", "duration20"), (False, True), ("lazy", "eager"),
                        (0, 1, None), (0, 1, 2), (0, 1)):
                    priors = ((), (events[0].id, events[2].id), tuple(truth))
                    source, target, begin, end = parts
                    query = tc.Query(source, target, begin + window_shift, end - window_shift, mode)
                    one(events, query, truth, priors[prior_index], complete, budget, policy)
        return {"decisions": decisions - start_count, "graphs": 3, "truth_masks_per_graph": 16}

    def diverse():
        rng = random.Random(1230511)
        start_count = decisions
        for case in range(80):
            records = []
            for index in range(rng.randrange(0, 9)):
                u, v = rng.sample((-4, 0, 3, 8, 13), 2)
                records.append(tc.Event(11 + 9 * index, rng.choice((-20, -1, 0, 1, 19, 20, 21, 39, 40, 41, 60)), u, v))
            events = tuple(sorted(records, key=lambda e: (e.t, e.id)))
            truth = {e.id: rng.randrange(2) for e in events}
            prior = tuple(i for i in truth if rng.randrange(3) == 0)
            for variant in range(3):
                source, target = rng.choices((-4, 0, 3, 8, 13, 99), k=2)
                begin = rng.choice((-40, -1, 0, 1, 20))
                end = rng.choice(tuple(t for t in (-1, 0, 19, 20, 21, 40, 41, 60) if t >= begin))
                for mode, complete, policy, budget in itertools.product(
                        ("instant", "duration20"), (False, True), ("lazy", "eager"), (0, 2, None)):
                    one(events, tc.Query(source, target, begin, end, mode), truth, prior, complete, budget, policy)
        return {"decisions": decisions - start_count, "seed": 1230511, "graphs": 80}

    def boundaries():
        events = (tc.Event(10, 20, 0, 1), tc.Event(20, 40, 1, 2))
        truth = {10: 1, 20: 1}
        expected = [(0, 40, True), (1, 40, False), (0, 39, False), (-1, 40, True)]
        for begin, end, answer in expected:
            query = tc.Query(0, 2, begin, end)
            assert expanded_reachable(events, query, set(truth)) is answer
            one(events, query, truth, (), True, None, "lazy")
        empty = ()
        for mode in ("instant", "duration20"):
            one(empty, tc.Query(99, 99, -7, -7, mode), {}, (), False, 0, "lazy")
            one(empty, tc.Query(99, 0, -7, -7, mode), {}, (), False, 0, "lazy")
        return {"explicit_cases": 8}

    def validation_and_scope():
        events = (tc.Event(10, 20, 0, 1),)
        memory = tc.FactMemory(events, "source-A", "v1")
        memory.put(10, 1)
        touched = []
        base = dict(source_id="source-A", version="v1", complete=True)
        query = tc.Query(0, 1, 0, 20)
        fetch = lambda i: touched.append(i) or 1
        for patch in ({"source_id": "source-B"}, {"version": "v2"}, {"complete": 1},
                      {"budget": True}, {"budget": 1.0}, {"budget": -1},
                      {"budget": float("nan")}, {"budget": float("inf")}, {"policy": "unknown"}):
            require_rejection(lambda patch=patch: tc.decide(events, query, fetch, memory, **{**base, **patch}))
        for bad_query in (tc.Query(0, 0, 2, 1), tc.Query(True, 1, 0, 20),
                          tc.Query(0, 1, 0.0, 20), tc.Query(0, 1, 0, 20, "unknown")):
            require_rejection(lambda q=bad_query: tc.decide(events, q, fetch, memory, **base))
        altered = (tc.Event(10, 21, 0, 1),)
        require_rejection(lambda: tc.decide(altered, query, fetch, memory, **base))
        for value in (False, True, 0.0, 1.0, 2, None):
            require_rejection(lambda value=value: memory.put(10, value))
        require_rejection(lambda: memory.put(10, 0))
        require_rejection(lambda: memory.put(True, 1))
        require_rejection(lambda: memory.put(999, 1))
        try:
            memory.facts[10] = 0
            raise AssertionError("public facts mapping mutable")
        except TypeError:
            pass
        assert not touched and dict(memory.facts) == {10: 1}
        for source, version, envelope in (("source-B", "v1", events), ("source-A", "v2", events),
                                          ("source-A", "v1", altered)):
            require_rejection(lambda source=source, version=version, envelope=envelope:
                              tc.FactMemory.from_json(memory.to_json(), envelope, source, version))
        return {"invalid_input_side_effects": len(touched), "scope_dimensions_rejected": 3}

    def strict_json():
        events = (tc.Event(10, 20, 0, 1),)
        memory = tc.FactMemory(events, "source-A", "v1")
        memory.put(10, 1)
        original = json.loads(memory.to_json())
        packets = []
        for row in ([[10, 1], [10, 1]], [[10, 1], [10, 0]], [[True, 1]], [[10, True]],
                    [[10.0, 1]], [[10, 1.0]], [[999, 1]], [[10, None]], {"10": 1}):
            packets.append(json.dumps({**original, "facts": row}))
        packets.extend(["[]", "null", json.dumps({**original, "extra": 0}),
                        json.dumps({k: v for k, v in original.items() if k != "schema"}),
                        memory.to_json()[:-1] + ',"version":"v1"}',
                        memory.to_json().replace('[[10,1]]', '[[10,NaN]]'),
                        memory.to_json().replace('[[10,1]]', '[[10,Infinity]]')])
        for packet in packets:
            require_rejection(lambda packet=packet: tc.FactMemory.from_json(packet, events, "source-A", "v1"))
        return {"rejected_packets": len(packets)}

    def callback_failure():
        events = (tc.Event(10, 20, 0, 1), tc.Event(20, 40, 1, 2))
        query = tc.Query(0, 2, 0, 40)
        cases = []
        for policy, fail_value in itertools.product(("lazy", "eager"), ("raise", True, 1.0, 2)):
            memory = tc.FactMemory(events, "failure-source", "v1")
            attempts = []
            def fetch(event_id):
                attempts.append(event_id)
                if len(attempts) == 1:
                    return 1
                if fail_value == "raise":
                    raise RuntimeError("engineered source failure")
                return fail_value
            try:
                tc.decide(events, query, fetch, memory, source_id="failure-source", version="v1",
                          complete=True, budget=2, policy=policy)
                raise AssertionError("failed or invalid observation accepted")
            except (RuntimeError, ValueError):
                pass
            assert attempts == [10, 20] and dict(memory.facts) == {10: 1}
            restored = tc.FactMemory.from_json(memory.to_json(), events, "failure-source", "v1")
            resumed = []
            answer = tc.decide(events, query, lambda i: resumed.append(i) or 1, restored,
                               source_id="failure-source", version="v1", complete=True, budget=1, policy=policy)
            assert answer.answer is True and resumed == [20]
            cases.append({"policy": policy, "failure": str(fail_value), "accepted_before_failure": 1,
                          "attempts_before_failure": 2, "retry_acquisitions": 1})
        return cases

    def child_restart():
        events = (tc.Event(10, 20, 0, 1), tc.Event(20, 40, 1, 2))
        memory = tc.FactMemory(events, "child-audit", "v1")
        memory.put(10, 1)
        script = '''import json, sys
sys.path.insert(0, sys.argv[1])
from temporal_controller import Event, Query, FactMemory, decide
events=(Event(10,20,0,1),Event(20,40,1,2))
memory=FactMemory.from_json(sys.stdin.read(),events,"child-audit","v1")
requested=[]
r=decide(events,Query(0,2,0,40),lambda i: requested.append(i) or 1,memory,source_id="child-audit",version="v1",complete=True,budget=1)
print(json.dumps({"answer":r.answer,"requested":requested,"facts":dict(memory.facts)}))
'''
        run = subprocess.run([sys.executable, "-B", "-c", script, str(module_dir)],
                             input=memory.to_json(), text=True, capture_output=True, timeout=20, check=True)
        result = json.loads(run.stdout)
        assert result == {"answer": True, "requested": [20], "facts": {"10": 1, "20": 1}}
        return result

    def builder_commands():
        command_results = []
        for suffix in (["-m", "unittest", "-v", "test_controller"], ["demo.py"]):
            before, command_start = time.perf_counter(), utc()
            run = subprocess.run([sys.executable, "-B", *suffix], cwd=module_dir,
                                 text=True, capture_output=True, timeout=30)
            record = {"argv": ["python", "-B", *suffix], "started_utc": command_start,
                      "finished_utc": utc(), "wall_seconds": time.perf_counter() - before,
                      "returncode": run.returncode, "stdout": run.stdout, "stderr": run.stderr}
            command_results.append(record)
            assert run.returncode == 0, record
            if suffix == ["demo.py"]:
                packet = json.loads(run.stdout)
                assert len(packet["examples"]) == 8
        return command_results

    check("explicit time/deadline and empty-envelope boundaries", boundaries)
    check("independent exhaustive time-expanded truth and evidence", exhaustive)
    check("deterministic diverse graphs, prior observations and changed queries", diverse)
    check("validation before fetch, live and restored source scopes", validation_and_scope)
    check("strict JSON duplicate keys, IDs, type and shape rejection", strict_json)
    check("fetch exception and invalid-value recovery under both policies", callback_failure)
    check("independent child process checkpoint restart", child_restart)
    check("existing builder suite and eight-case demo", builder_commands)
    after = {name: sha(module_dir / name) for name in bindings}
    if bindings != after:
        failures.append({"check": "source stability", "message": "audited files changed during audit"})
    output = {"schema": "run123-independent-controller-audit-v1", "started_utc": started,
              "finished_utc": utc(), "status": "pass" if not failures else "fail",
              "module_bindings_before": bindings, "module_bindings_after": after,
              "checker_sha256": sha(Path(__file__)), "independent_decision_cases": decisions,
              "additional_checkpoint_zero_budget_replays": checkpoints, "checks": results,
              "failures": failures, "wall_seconds": time.perf_counter() - wall,
              "auditor_process_cpu_seconds": time.process_time() - cpu,
              "limits": ["Engineered finite checks, not empirical or learned-model evidence.",
                         "Uses explicit time-expanded graph reachability without production helper imports.",
                         "No network, paid call, real source data, concurrency or security guarantee tested.",
                         "Total wall contains the nested builder-command walls; do not add them again.",
                         "Auditor process CPU excludes child-process CPU."]}
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": output["status"], "decision_cases": decisions,
                      "checkpoint_replays": checkpoints, "failures": failures,
                      "wall_seconds": output["wall_seconds"]}, indent=2))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
