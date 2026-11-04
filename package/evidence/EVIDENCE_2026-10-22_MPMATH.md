# Historical mpmath formatting qualification

22 October 2026. One ordinary current-REL worker, without prior episodes, passed
all 11 bounded test functions after repairing the historical formatting failure.
No residual error qualified and no retained-history comparison ran.

The task was `mpmath__mpmath-881` from the official
[VibeMemBench dataset](https://huggingface.co/datasets/Tongyi-ConvAI/VibeMemBench),
using mpmath commit `99e3b464afb883e5088d56d34909a11765da9c8e`.
Metadata selection preceded access to the target solution; neither the gold patch
nor the target repair trajectory was supplied to the worker. This was an already
known historical issue, not a newly discovered mathematical result.

The real library contained 54 Python files and 48,070 lines including docstrings.
The worker corrected general-format notation around a rounded exponent, preserving
sign, guard digits and fixed-format carry behavior. No whole-library replacement,
blanket float coercion or fixture-specific lookup was observed.

| Artifact | Passed | Failed | Unresolved |
| --- | ---: | ---: | ---: |
| Original, corrected setup | 10 | 1 | 0 |
| Known upstream repair | 11 | 0 | 0 |
| Ordinary worker repair | 11 | 0 | 0 |

The profile was seven deterministic upstream functions and four Hypothesis
properties, each bounded at 1,000 examples. The actual property sample count was
not independently instrumented. The Python 3.12 pure backend was used; the gmpy2
property and the rest of the upstream suite were outside scope. The test driver
was visible and runnable during repair, so this was not an unseen holdout.

Fresh gpt-6.1-sol/medium used 19 actions and seven Python guest calls. Recorded cost
was 351,331 tokens, including 299,392 cached input, with 51,939 uncached input plus
output. Task phase was 227.440 seconds; outer dispatch including startup and grading
was 415.924 seconds. Neither is complete research cost. Parent tokens, full setup
and engineering time, money and physical/remote energy remain unknown.

Preserved corrections include a dependency-wheel assumption, an omitted `attrs`
dependency that caused collection errors, a worker-authored rounding fixture,
and an analysis label that had incorrectly called a phase-duration sum
nonoverlapping. Collection errors remain setup failures rather than task errors;
the corrected evaluator's rejection path was exercised through the actual guest.

Six conditional history attempts were not prepared or dispatched. All 20 REL core
files remained unchanged. A history-selected public benchmark task did not provide
the required current-worker memory gap. The known upstream repair remains a
strong direct-artifact alternative for this historical issue.

[Structured evidence](EVIDENCE_2026-10-22_MPMATH.json).
