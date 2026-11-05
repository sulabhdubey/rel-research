# Ordinary temporal fact acquisition

A small, standard-library Python example of buying only the observations needed
to justify a temporal reachability answer. It retains ordinary lazy acquisition,
an eager reference policy, source-bound fact memory, and restartable checkpoints.
It has no probability estimator or learned policy.

All contacts and labels in the demo and tests are hand-authored. They are
**engineered verification cases**, not fresh empirical data, natural observations,
an evaluated agent acquiring a method, or evidence of a learning improvement.
There are no source contact datasets or external services in this example.

## Run

Use Python 3.10 or newer. From this directory:

```sh
python -B demo.py
python -B -m unittest -v test_controller
```

No installation or third-party package is required. The demo starts one child
Python process to restore a JSON checkpoint, then prints its decisions and actual
acquisitions. It shows budget abstention, repeated reuse, changed conditions, paid
absence, incomplete envelopes, and stale-version rejection. It makes no network
requests and writes no files. The test command includes a separate process restart
and exhaustive small cases checked by an independently implemented state-space
search; tests establish their covered behavior, not universal correctness.

## Use the module

```python
from temporal_controller import Event, FactMemory, Query, decide

events = (Event(0, 20, 0, 1), Event(1, 40, 1, 2))
memory = FactMemory(events, source_id="example-source", version="v1")
observations = {0: 1, 1: 1}  # Engineered answers, standing in for a trusted source.
result = decide(
    events, Query(0, 2, 0, 40), observations.__getitem__, memory,
    source_id="example-source", version="v1", complete=True, budget=2,
)
assert result.answer is True
assert result.witness == (0, 1)

checkpoint = memory.to_json()
restored = FactMemory.from_json(checkpoint, events, "example-source", "v1")
```

`Event(id, t, u, v)` is an undirected possible contact, with a unique nonnegative
integer identity. Events must be sorted by `(t, id)`. Vertices and times are
integers. `Query(source, target, start, deadline, mode)` permits waiting:

- `duration20` uses each contact over `[t-20, t]`. A traveller must reach its
  departure vertex by `t-20` and arrives at the other vertex at `t`. Overlapping
  intervals cannot form a chain. A contact ending at the deadline is allowed.
- `instant` uses each contact at `t`. A chain of valid contacts in the same slot
  is allowed. This is a declared computational semantics, not a physical claim.

The source equals target query has an empty positive witness and costs no facts.
The query window must still be valid. The fixed duration is part of this example's
contract; applications needing other durations must change and revalidate it.

## What an answer means

Let the lower graph contain acquired-true events, and the upper graph contain
all events except acquired-false ones. The callback must return the integer `0`
or `1` for an event's stable validity under the declared source/version. Both
values count as acquisitions. Boolean values and floating-point lookalikes are
rejected. With a complete envelope, the true graph lies between these bounds.

| Answer | Required evidence |
| --- | --- |
| `True` | A time-valid witness using only acquired-true events. |
| `False` | No time-valid path even in the upper graph, and `complete=True`. |
| `None` | The available evidence does not justify either verdict. |

The returned reason distinguishes a positive witness, a complete upper refutation,
an incomplete envelope, and an exhausted acquisition budget. An incomplete
envelope can still support a positive witness. It never supports a negative
answer. Setting `complete=True` is a caller assertion: the code cannot discover
events omitted from the envelope or establish sensor coverage.

`policy="lazy"` finds a feasible path with the fewest unknown events and acquires
its first unknown event. It recomputes bounds after every observation.
`policy="eager"` acquires all relevant unknown events up to the budget, after
honoring initially decisive bounds. Both share public time/component pruning.
Neither policy is claimed optimal for expected acquisitions. The demonstration
does not establish a performance advantage on real workloads.

## Reuse and failure boundaries

Memory binds observations to an explicit source identity, source version, and
SHA256 hash of the ordered envelope. Two sources with identical envelopes still
have distinct fact scopes. This explicit source binding hardens an earlier
content/version-only interface; it does not invalidate earlier source-isolated
experiments. Hashes bind contents; they do not authenticate a source, prove its
answers, protect a checkpoint from deliberate rewriting, or establish completeness.

Changed query starts, deadlines, targets, or temporal semantics reuse still-valid
facts and recompute the decision. A changed source, version, or envelope rejects
the entire old state. This example does **not** implement selective invalidation
of individual records across versions. Such reuse requires an additional source
contract identifying unchanged facts. The caller must update `version` whenever
validity can change, even if the public event list is identical.

Checkpoints use a strict JSON schema. Missing/extra fields, duplicate JSON keys,
duplicate or unknown fact IDs, stale bindings, malformed facts, and nonstandard
numeric constants are rejected. No pickle or dynamic code execution is used.
Use small checkpoints from an authorized source: this is not a hardened parser
for unlimited hostile input, a signed provenance system, or a crash-atomic file
store. The caller owns durable storage and source authentication.

Input validation runs before calling the observation source. A callback exception
or invalid observation stops the call; already accepted facts remain in memory
for retry. The controller never retries automatically. Its normal return records
successful acquisitions in `requests`; it does not provide a failure receipt when
the callback raises. Applications charging for failed attempts must account for
those attempts in their callback or source adapter. Memory is intended for one
controller at a time; concurrent mutation requires caller synchronization.

## Costs and limits

`budget` is a nonnegative integer limiting callback acquisitions for this call.
It does not limit CPU, memory, source latency, or money. Cached facts are free in
that count, but checking and persistence still have a real cost. `path_checks`
and `edge_scans` are diagnostic operation counts, not end-to-end timing. This
implementation prioritizes clarity over large-graph efficiency and materializes
the event envelope and immutable witness tuples.

The tests cover temporal boundaries, changed requirements, scope rejection,
strict restore, failure recovery, fact conflicts, paid negatives, incomplete
envelopes, bounded abstention, and 64 truth masks under both semantics and
policies with three acquisition limits. Repetitions and generated masks are
dependent engineering checks. They are not independent empirical trials or
evidence of autonomous learning, a new algorithm, or general superiority.
