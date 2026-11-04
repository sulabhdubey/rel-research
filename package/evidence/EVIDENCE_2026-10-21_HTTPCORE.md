# HTTPcore: ordinary-repair qualification before retained-experience testing

21 October 2026. **Result: the ordinary repair passed all fourteen frozen
scenarios. No residual failure qualified for the planned history comparison.**

## What was tested

This study retained the real HTTPcore implementation at commit
`10a658221deb38a4c5b16db55ab554b0bf731707`: 31 Python files and 7,139 lines.
The target was interrupted async response cleanup, orphaned connection capacity,
and ownership of connections assigned to pending requests. These are existing
upstream leads, not newly discovered incidents: [discussion 1053](https://github.com/encode/httpcore/discussions/1053),
[issue 1110](https://github.com/encode/httpcore/issues/1110) and
[cleanup proposal 1116](https://github.com/encode/httpcore/pull/1116).

Controlled in-memory transports and scheduling exercised the actual package in
offline Docker. The scope was asyncio/AnyIO and direct HTTP/1.1 pooling. The
production report in issue 1110 concerns synchronous concurrency; this study
exercised analogous async ownership bookkeeping, not that production workload.

A setup defect was corrected before model execution: direct low-level Requests
omitted the mandatory Host header. Six initial probes therefore stopped before
the intended behavior. Original results and source were preserved; these failures
were excluded as evidence of library defects.

## Ordinary work and outcomes

One fresh-context `gpt-6.1-sol/medium` worker received current REL, the complete
task contract, original library, upstream documentation/tests, dependencies, and
a readable test driver. It received no previous repair episode or upstream patch.
Its allowance was 60 actions and 900 seconds; it used 37 actions. The grader
imported the protected test driver against a frozen candidate package, so replacing
the learner's pipeline could not substitute for repairing the real library.

| Frozen profile | Before repair | After repair |
| --- | ---: | ---: |
| Lifecycle scenarios passing | 0 / 12 | 12 / 12 |
| Normal reuse/discard controls passing | 2 / 2 | 2 / 2 |
| Unresolved scenarios | 0 | 0 |
| Regressions among original passes | — | 0 |

The worker changed two library files, retaining unfinished cleanup ownership,
deferring completion flags, protecting reserved connections, reclaiming abandoned
capacity and serializing transport closure. It also created reusable local checks.
Its own additional concurrent-close probe exposed an intermediate race, which it
corrected before submission. That probe had a zero process exit but contained an
AssertionError outcome; process exit alone was not treated as success.

Additional evidence includes 82 worker-generated parameter combinations through
the supplied driver and 11 worker-authored lifecycle checks. These are related
checks, not independent tasks or withheld evaluations. Thirty-two selected upstream
async test bodies were also executed on the final candidate after its last change.
That small runner strips decorators and supplies a limited assertion adapter; it
is not the full upstream pytest suite. Sync generation, HTTP/2, proxies, Trio and
real network operation remain outside qualification. The patch is a local research
artifact, not an upstream-ready or installed production release.

## Cost and interpretation

| Recorded quantity | Value |
| --- | ---: |
| Model repair attempts | 1 |
| Total input plus output tokens | 986,883 |
| Cached input tokens, included above | 898,688 |
| Uncached input plus output tokens | 88,195 |
| Output tokens, included above | 14,122 |
| Tool actions / worker guest invocations | 37 / 10 |
| Outer attempt time, including startup and grading | 469.20 seconds |
| Sum of separately recorded non-overlapping acquisition/execution phases | 505.59 seconds |

No extra reflection model call was made. Usage identity and source bindings were
verified. The phase sum excludes unmeasured coordinator work and is not total
end-to-end project time. Parent research/build/analysis tokens, historical harness
acquisition, complete human effort, energy and subscription cost allocation remain
unknown. Cached tokens are included in the main total rather than silently removed.

## Decision for REL

The six conditional history-comparison attempts were not prepared or dispatched.
The frozen ordinary endpoint has no remaining error for that comparison to repair.
Changing tests after seeing this success would require a separately declared study;
repetition or a weaker baseline would not establish a learning benefit.

This is useful ordinary engineering and observed within-attempt self-correction.
Because the worker already used REL and no comparator ran, it does not establish
that REL caused those actions, improves later decisions, or lowers cost. One real
package and fourteen related scenarios do not establish broad reliability.

All twenty core REL files remain unchanged. Existing instructions already cover
fixture-versus-product errors, actual changed behavior, source binding, ordinary
baseline qualification and preservation of negative results. Evidence records are
updated; another mandatory rule is not supported by this result.

At workstream level, repeated qualification ceilings now justify reassessing task
selection before spending on another repair family. A next correctness study needs
an existing ordinary-work incident with a reproducible unresolved decision and a
specific past observation that could change it. An alternative cost study would
need a separate prospective design including initial learning and later reuse costs.
Neither is a result of this completed qualification.

[Structured summary and recorded costs](EVIDENCE_2026-10-21_HTTPCORE.json).

Raw traces, the study harness and the local repair remain outside this package.
