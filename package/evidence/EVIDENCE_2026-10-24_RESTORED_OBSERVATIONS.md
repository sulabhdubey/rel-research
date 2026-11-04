# Observation retention: restoring verification values

24 October 2026. The restored-results candidate **did not meet the pinned cost-adoption criteria**. All results below are descriptive for six fresh constructed cases.

## What caused the earlier increase

The prior compact-REL run used 51 model requests versus 42 with raw history. Of its 149,547 extra tokens, 116,106 were repeated initial context, 32,760 later input growth and 681 output. Cached input accounted for 145,792 of the increase. Some workers reopened raw history to recover numerical results for valid grouped-result checks; one reread the attached skill. Other extra requests occurred without an archive read. This identifies multiple observed contributors, not a single proven behavioral cause. The private local trace diagnosis is retained; raw transcripts are not included in this package.

## What changed and what stayed comparable

The candidate appends exact historical numerical results to the existing observation table. It preserves the previous columns, source revisions, requests, measured costs, ordering, errors and raw fallback. No new route recommendations, current answers, summary model calls, or instructions discouraging verification were added. The current 20-file REL core remained frozen.

Six ordinary acquisitions supplied the same complete archives to four later sessions each: R raw-history REL; C prior compact-view REL; V restored-results REL; H ordinary work with the same restored view. Conditions include stable sources, changed source revisions and reassigned job labels. Every session used gpt-6.1-sol/medium with the same tools, 60-action and 900-second maximum allowances. These are equal allowances, not equal executed effort.

## Measured later-task outcomes

| Arm | Tasks passed | Final jobs | First saved jobs | Requests | Total tokens | Uncached input + output | Raw reads | Query VM work |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| REL raw | 6/6 | 48/48 | 48/48 | 39 | 871,285 | 153,461 | 12 | 1,302,200 |
| REL prior compact | 6/6 | 48/48 | 48/48 | 47 | 1,021,888 | 128,192 | 4 | 1,302,200 |
| REL restored results | 6/6 | 48/48 | 48/48 | 41 | 805,136 | 146,704 | 2 | 713,400 |
| Ordinary restored results | 6/6 | 48/48 | 48/48 | 35 | 564,115 | 128,275 | 0 | 1,290,600 |

## Acquisition-inclusive comparisons

Common acquisition: 634,348 tokens, 141,420 uncached input plus output, and 4,256,100 query VM steps. Charge it in full to each deployment alternative, but count it only once in actual study use.

| Contrast | Total tokens | Uncached input + output | Query VM work |
|---|---:|---:|---:|
| V/C | -13.09% | +6.87% | -10.59% |
| V/R | -4.39% | -2.29% | -10.59% |
| H/V | -16.74% | -6.40% | +11.61% |

For restored REL versus the previous compact view, requests changed from 47 to 41, archive reads from 4 to 2, and live probes from 56 to 40. Total-token reductions occurred in four of six cases. Both remapped-label cases used more tokens than raw REL. The restored view fixes a verified information omission but does not satisfy every pinned cost criterion.
A larger table can eliminate a follow-up read, but the total must include changed request counts and verification behavior. Reduced raw reads alone do not establish lower complete cost. Cached input is included in total tokens and shown separately in the structured results; these counts are not monetary prices. Cache allocation was observed, not experimentally controlled; differences in uncached usage should not be attributed solely to the display mechanism.

## All paired later-token results

| Case | R | C | V | H |
|---|---:|---:|---:|---:|
| F1 | 152,247 | 153,089 | 106,557 | 93,111 |
| F2 | 165,526 | 221,978 | 112,820 | 81,129 |
| F3 | 124,436 | 132,582 | 131,417 | 94,728 |
| F4 | 209,289 | 199,848 | 129,891 | 94,430 |
| F5 | 107,713 | 162,092 | 162,635 | 82,782 |
| F6 | 112,074 | 152,299 | 161,816 | 117,935 |

## Decision and REL update

- at_least_four_paired_token_reductions: **pass**.
- charged_total_tokens_at_least_10_percent_lower_than_C: **pass**.
- charged_total_tokens_not_above_R: **pass**.
- no_extra_failed_decisions: **pass**.
- query_work_within_10_percent: **pass**.
- uncached_not_increased: **fail**.

The report, worked example and version-bound evidence are updated locally. No new mandatory core rule is justified solely by this comparison. Keep the restored display as an evaluated task-local candidate with its actual wins and losses, rather than silently replacing the ordinary factual handoff default.

## Accounting, verification and limits

Actual recorded use across all 30 sessions: 3,896,772 total tokens = 3,863,202 input + 33,570 output. Of input, 3,198,720 tokens were cached. Uncached input plus output: 698,052. Reasoning-output counters are a subset of output and are not added twice.
Measured retention preparation: 0.265625 CPU seconds, 1.110502 wall seconds, 570,096 stored bytes across all arms. Actual summed dispatch time: 3237.44 seconds; parallel sums are not elapsed study time. Backend query CPU: 0.625000 seconds; query wall: 0.876021 seconds.
Separate measured data construction and qualification: 18.741738 wall seconds, 16.640625 CPU seconds and 13,565,300 qualification query VM steps, with zero model calls. These are study infrastructure costs, not included in either arm's worker totals.
All task starts, native request usage, acquisition, feedback, query probes and final executions are included. Feedback used no additional model turns. Parent-model usage, complete engineering/research costs, dollars and whole-laptop/remote-model energy remain unknown. The total is complete for the declared worker boundary, not every resource used by the investigation.
Source-qualified SQL routes were cross-checked against separately implemented full-row arithmetic. Original and restored view fields were checked against the actual archive and rendered text. Typed skill attachments and fresh-session identities were verified. The contained cooperative host hides backend data from workers, but is not a hostile sealed evaluator. Six cases are six paired units; 240 final decisions are not 240 independent experiments. No broad portability, statistical equivalence, long-term autonomous improvement or novel architecture is established.

## Research rationale

The [context-compression study](https://arxiv.org/html/2608.16370v1) motivates measuring retrieval work and retained-state interventions separately from completion. [Raw-RAG](https://arxiv.org/html/2610.30755v1) motivates retaining source evidence and a strong raw-history comparison. [MemoryTax](https://arxiv.org/html/2610.29823v1) motivates acquisition-inclusive accounting, with its limited evaluation scope preserved. These papers motivate our design; their reported effects are not evidence for REL.

## Reproduction and next decision

Local artifacts: PLAN.md, RESEARCH.md, DESIGN_BINDINGS.json, ANALYSIS_BINDINGS.json, QUALIFICATION.json, PROJECTOR_QUALIFICATION.json, ACCOUNTING_QUALIFICATION.json, INPUT_INTEGRITY_AUDIT.json, ANALYSIS.json and TRAJECTORY.json. The bound source scripts and original native receipts remain local. Reproduction requires the matching installed Codex/Docker host and subscription access; the generic skill alone is not this research runner.

Do not repeat view-format comparisons merely to obtain a preferred result. Use these costs and traces to decide whether a future task has a concrete information-reacquisition or request-scheduling gap. Any subsequent candidate must change that specific mechanism and use fresh evidence.
