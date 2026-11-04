# Run86: compiled methods across a longer changing lifecycle

28 October 2026. Development architecture study; four chains, two public-data families, 16 decisions per chain. Pinned plan [historical source: PLAN.md], machine-readable reconstruction [historical source: RESULTS.json], independent review [historical source: REVIEW.md].

## Result

All 64 numerical reports were correct. Each of the four learners acquired a calibrated, parameterized SQL method on its first episode. All 60 later reports used that stored executable method directly, without another model call. State continuity and verified method identity were independently checked across all 60 transfers.

| Policy | Correct reports | New model calls | Direct later executions | New tokens | Cached input | Uncached input + output |
|---|---:|---:|---:|---:|---:|---:|
| Ordinary competent reuse | 32/32 | 2 | 30 | 103,483 | 75,520 | 27,963 |
| REL joint method/state guidance | 32/32 | 2 | 30 | 129,958 | 95,232 | 34,726 |

Both policies made 14 acquisition tool calls, including two witness reads. No rejected tools, wrong submitted reports or failed later dispatches were observed. REL used 25.58% more new tokens, with equal correctness and direct-reuse counts. The fixed difference was 26,475 tokens. Because both policies then used zero additional model tokens, this horizon contains no REL-versus-ordinary token break-even.

Acquisition nevertheless amortized: new tokens per correct report fell from 51,741.5 to 3,233.84 for ordinary reuse and from 64,979 to 4,061.19 for REL. This is the measured model-token curve, not an electricity or whole-system cost claim. The actual shared Run85 origin methods cost 190,539 historical tokens; allocating that same origin cost once to each policy yields 9,188.19 and 10,015.53 tokens per report respectively. Those allocations are not additional model calls or independent spending.

## What was built and learned

The host now admits declarative parameter bindings, verifies an acquired method through its actual invocation, persists versioned methods and dispatches a verified applicable method directly. General model reasoning is a fallback. This extends A2 in the existing six-proposal programme and removes Run85's unnecessary model call on every episode.

The A1 witness held observations and objective fixed while changing calibration gain. The old selected context projection stayed identical although the independently required output changed. All four agents read this witness and added gain/offset to selected fields and executable parameter bindings. They compiled general methods from the available documentation before any wrong output occurred. This demonstrates a checked missing distinction and proactive repair, not reactive discovery from a production failure or proof that the witness caused the repair. Both ordinary and REL learners had the same witness and complete contract.

Later changes included gains/offsets, units, quality rules, reporting bounds, threshold inclusivity and restored regimes. All methods handled them without edits. Therefore no in-study retirement/reinstatement or later procedure evolution occurred; those registry paths have only regression-test evidence here. Output checking still used a trusted Python oracle after every dispatch. A production system with no such oracle would require different validation evidence.

## Research and design

The cycle inspected [counterexample-guided abstraction refinement](https://web.stanford.edu/class/cs357/cegar.pdf), the [DreamCoder method-learning abstract](https://arxiv.org/abs/2006.08381) and [MemoryArena's interdependent-task abstract](https://arxiv.org/abs/2602.16313). The implemented design borrows the general ideas of a missing-distinction witness, executable reuse and sequential evaluation. This is not a reproduction of those systems or a full-paper review in this cycle.

Two UCI public datasets supplied numerical observations: [Appliances energy prediction](https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction) and [Beijing PM2.5](https://archive.ics.uci.edu/dataset/381/beijing+pm2+5+data). Their source hashes and archive/member identities are in SOURCES.json. Reporting revisions and calibration contracts were controlled constructions, not claims about actual instrument calibration. Adjacent source windows overlap by 729 records in 29 of 30 transitions. These are longer development workflows, not independent fresh holdouts or 64 independent problems.

## Defects, corrections and measurement boundary

Independent review found registry history aliasing, incorrect replacement priority and failure to roll back in-memory state after a rejected save. They were corrected after the trial, preserving runtime_v1 and RELEASE.trial.json. Six focused tests pass, including the changed paths. The original successful methods did not exercise those defects, so historical outcomes were not silently rewritten. A test-import collision caught during construction was also corrected; test names and module identity were verified.

The trial's per-cell wall timers excluded admission checks. Their sums were 58.04 seconds for ordinary reuse and 55.43 seconds for REL, which are partial overlapping worker times, not campaign elapsed time or a valid inclusive speed comparison. Threaded process CPU counters cannot be attributed per cell and are not summed as costs. The corrected runner starts timing at admission and labels process CPU unattributable. No new native run was spent to conceal the original omission. Research/coordinator/reviewer tokens, full hardware costs and energy remain unmeasured.

The release hash bound every trial receipt. The separate reconstruction validates outputs with a differently implemented numerical oracle and checks every saved-state link. This is same-data verification, not independent task replication. The independent reviewer checked all 64 outputs, 60 links, 60 direct method identities and four acquisition paths.

## Programme decision and REL update

Keep the direct compiled execution path for this architecture; retain ordinary parameterized reuse as the strong control. A1 is partially exercised, A2 now has a longer working lifecycle, and A6 has persistence/repair checks but no improved-learning-procedure result. A4 and A5 have no new implementation evidence.

Advance A3 only through measured repeated work. Review found all 32 task files share the same latest-revision winner map, while their final eligible sets have 31 distinct values. This suggests caching the exact selection interface, not the whole report or eligibility result. The next cycle must count cache-key construction, invalidation, materialization, SQL, checking and misses, and compare ordinary memoization/incremental processing. It must challenge row identity, order, revision and availability changes. All six proposals remain in the existing programme.

REL already calls for tracing acquired methods into use, inclusive costs, fair controls and repairing evaluator defects. These findings justify a working example, evidence and task-runtime repairs; they do not justify another mandatory core instruction. The core and conditional research reference remain unchanged. The private repository is synchronized before the next material study.
