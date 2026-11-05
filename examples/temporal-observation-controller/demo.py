"""Run the entirely hand-authored examples: python -B demo.py."""
from dataclasses import asdict
import json
from pathlib import Path
import subprocess
import sys

from temporal_controller import Event, FactMemory, Query, decide


EVENTS = (Event(0, 20, 0, 1), Event(1, 20, 1, 2), Event(2, 40, 1, 3))
SOURCE = "engineered-example"
VERSION = "v1"
TRUTH = {0: 1, 1: 1, 2: 1}


def solve(memory, query, **kwargs):
    return decide(EVENTS, query, TRUTH.__getitem__, memory,
                  source_id=SOURCE, version=VERSION, complete=True, **kwargs)


def main():
    if sys.argv[1:] == ["--resume-child"]:
        memory = FactMemory.from_json(sys.stdin.read(), EVENTS, SOURCE, VERSION)
        decision = solve(memory, Query(0, 2, 0, 20, "instant"))
        print(json.dumps({"decision": asdict(decision), "checkpoint": memory.to_json()}))
        return
    if sys.argv[1:]:
        raise SystemExit("Usage: python -B demo.py")
    memory = FactMemory(EVENTS, SOURCE, VERSION)
    initial = solve(memory, Query(0, 2, 0, 20, "instant"), budget=1)
    child = subprocess.run(
        [sys.executable, "-B", str(Path(__file__).resolve()), "--resume-child"],
        input=memory.to_json(), text=True, capture_output=True, check=True, timeout=15,
    )
    resumed = json.loads(child.stdout)
    memory = FactMemory.from_json(resumed["checkpoint"], EVENTS, SOURCE, VERSION)
    examples = [
        {"case": "one acquisition leaves an unknown answer", **asdict(initial)},
        {"case": "new process restores facts and buys only the missing fact", **resumed["decision"]},
        {"case": "exact repeat reuses acquired facts", **asdict(solve(memory, Query(0, 2, 0, 20, "instant")))},
        {"case": "duration semantics forbid the same-slot chain", **asdict(solve(memory, Query(0, 2, 0, 20)))},
        {"case": "changed target and deadline recompute bounds", **asdict(solve(memory, Query(0, 3, 0, 40)))},
    ]
    absent = (Event(0, 20, 0, 1),)
    for complete in (True, False):
        cache = FactMemory(absent, "engineered-absence", VERSION)
        decision = decide(absent, Query(0, 1, 0, 20), lambda _: 0, cache,
                          source_id="engineered-absence", version=VERSION, complete=complete)
        examples.append({"case": "paid absence", "complete": complete, **asdict(decision)})
    try:
        FactMemory.from_json(memory.to_json(), EVENTS, SOURCE, "v2")
    except ValueError as error:
        examples.append({"case": "changed source version rejects stale facts", "rejection": str(error)})
    print(json.dumps({
        "evidence": "Engineered verification only; no acquired dataset or learning result.",
        "examples": examples,
    }, indent=2))


if __name__ == "__main__":
    main()
