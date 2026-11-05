# Reuse, adapt, or refuse?

A saved method is useful only when it still answers the current question. This demonstration makes three choices visible using one small energy-reporting example.

```sh
python -B demo.py
python -B -m unittest test_walkthrough test_runtime_portability -v
python -B independent_checks.py
```

Run these commands from this directory with Python 3.11 or later. They use the standard library, an in-memory SQLite database and bundled files. There are no downloads, credentials, model calls or external services. The demo writes JSON to stdout and does not write files. Tests create a temporary copy for an identity check and start one fresh Python process; temporary files are removed afterwards.

## One set of observations, three requests

The **constructed** observations are 10 Wh and 20 Wh, with labels at minutes 0 and 10 and declared durations of ten minutes. Both are available, eligible and unrevised. The reporting window is initially `[0,20)`. These are three separate requests: the partial-window request uses the original 10 Wh and 20 Wh totals with identity calibration, not the preceding calibrated values.

| Request and condition | Action actually taken | Checked result |
|---|---|---|
| Sum whole eligible rows selected by their timestamp; identity calibration | Execute the original saved Wh/binary SQL method against the current rows | **30 Wh** (`0.03 kWh`), two eligible rows |
| Same whole-row report; now correct each reading as `1.25 * value + 7 Wh` | Select and execute the later saved calibration-aware SQL method | **51.5 Wh** (`0.0515 kWh`), not the previous 30 Wh |
| Exact physical energy from minute 5 to minute 15 using the original totals and identity calibration; known disjoint bins and nonnegative power, but no within-bin shape | Refuse the exact answer and state the conditional admissible range | **0-30 Wh**; no exact answer or invented prorating truth |

The third range assumes the query is completely covered by the known bins and there is no peak-power or shape restriction. Two different consumption patterns fit the same recorded totals: all energy outside the requested half-bins, or all energy inside. Recomputing the same totals cannot distinguish them. Finer observations or an explicitly permitted approximation model could change the task.

Refusal is selective. With the same known support, the complete `[0,20)` interval has exact energy 30 Wh. Missing anchors, unobserved time, overlapping support, or contradictory negative totals are identified separately. These are declared demonstration assumptions; they are not facts established about the original dataset used in historical studies.

## What is retained, and what was learned?

`methods.json` holds two actual previously model-authored SQL methods. The first comes from Run85; the calibration-aware method was acquired in Run86. Run86 received earlier methods through its archive/seed context, not through a pre-populated before-registry. Their identities and a minimized lineage summary are recorded in [PROVENANCE.json](PROVENANCE.json). Original acquisition records remain privately retained; these hashes do not authenticate those events. The [public Run86 report](../../package/component-evidence/REPORT86.md) gives the wider study context.

This demo **does not learn a method again**. Its routing, binding bridge and applicability checks were authored for this walkthrough. Selecting a previously acquired method is an adaptation of execution, not a new learning result. The stored object is method code, not a cached numeric answer: changed observations are read again and can change the answer. A fresh process reloads the same bundle from disk.

Historical studies also found useful reuse with ordinary engineering. The tests include an ordinary non-SQL calculation using the same facts and requirements; they establish agreement on covered cases, not a REL advantage. All rows shipped here are constructed, with no original dataset records or private conversations.

## Inspect the decisions

- `walkthrough.py`: explicit conditions and routing; distinguishes row-label selection from a physical clock interval.
- `methods.json`: historical method payloads, unchanged.
- `runtime.py`: restricted in-memory SQL executor with a declared optional-API compatibility patch; not an OS sandbox or a promise of arbitrary-code safety. Its unused historical `Store` helper is not invoked by this walkthrough.
- `test_walkthrough.py`: relevant correctness, changed-behavior, rejection and restart checks.
- `demo.py`: one command showing the three outcomes and narrow execution timing.

The method digest detects an unexpected change against the bundled manifest. It does not establish semantic truth, authenticate an author, or protect against someone able to rewrite both files. Current requirements and measurement meaning still need checking.

## What would be useful feedback?

Run the commands, then challenge one decision or bring a minimal counterexample:

1. What is retained here: a method, a numeric answer, or both? Does changing a reading update the result?
2. Which operation changes when calibration changes, and why should the result become 51.5 Wh?
3. What observation or explicit assumption would make the partial-window answer exact? Can you find a case where the code gives an unjustified answer or refuses a justified one?

[Open a GitHub issue](https://github.com/sulabhdubey/rel-research/issues/new) with the command, Python/SQLite versions, minimal **constructed** inputs, expected result and actual result. Describe the assumption that makes the expectation valid. Please exclude credentials, private logs and real personal or customer records. A reproducible counterexample is more useful here than an unqualified score.

See [validation, the preserved correction and compatibility scope](VALIDATION.md). The example needs Python 3.11+ with SQLite window-function support (SQLite 3.25+). The declared minimum is an API requirement, not a tested cross-platform matrix. It was tested on Windows/Python 3.13.7; a real SQLite connection with the optional extension API hidden exercises that specific compatibility branch. No new third-party dependency is installed.

This supplement is separate from the unchanged report (study edition v0.7) and public package v0.7.1. The repository's [existing rights and sharing scope](../../package/RIGHTS_AND_DEPENDENCIES.md) applies; no broader license is added.

The practical lesson: **retain the computation, check its current assumptions, and make the resulting operation visible.** This is a runnable illustration of checked components, not a new empirical comparison, architecture result or general RSI effectiveness claim.
