# Lesson revision, selective context and corrected outputs

20 October 2026 · Exploratory REL study · Version-bound evidence

The study completed **26 native agent attempts**, including one feedback-only
recovery and four separately planned follow-up attempts. Twenty workers evaluated
later repairs; eight additional baselines replayed inherited programs without new
model calls. The results support careful use of retained experience, but do not
establish a generally superior revision or context-reset policy.

The hypotheses were informed by [ReHarness](https://arxiv.org/html/2610.12668v1),
[Scaling Discovery Requires Forgetting](https://arxiv.org/pdf/2610.20563v1) and
[LongHarness](https://arxiv.org/html/2610.13075v1). Their reported results are not
treated as measurements of REL.

## 1. Revising a lesson is useful only if later work benefits

Two learners authored programs and lessons, adapted to a changed output
requirement, revised their lessons from actual feedback, and faced fresh later
queries. All later arms shared the same adapted program within each origin.

| Fresh later queries | Revised lessons | Frozen lessons | Equally informed ordinary handoff | No episodic text | Direct program reuse |
| --- | ---: | ---: | ---: | ---: | ---: |
| Origin 1 | 98/101 | 86/101 | 96/101 | 95/101 | 86/101 |
| Origin 2 | 98/101 | 100/101 | 98/101 | 97/101 | 98/101 |

Revision improved the first origin's fresh score versus the ordinary handoff and
tied it in the second. It beat frozen guidance in one origin and lost in the other.
The ordinary handoff received the same assigned historical information as the
revised condition, without REL. Frozen guidance kept the original lesson and
received newer factual diagnostics; its presentation differs, so the contrast is
not a pure prose-only ablation. No-episodic-text workers still retained the common
executable. None of these eight workers passed the complete 296-query profile.

The strongest concrete failure was downstream of diagnosis: a revised lesson
correctly identified a Unicode regex error, and the later worker recognized it,
but five over-escaped patch attempts were rejected. The saved program remained
wrong on that case. A better-written lesson did not become a completed repair.

**Decision:** retain revision as an available method, with source evidence and old
records preserved. These results do not justify mandatory revision after every
task or a claim that it reliably dominates an equally informed handoff.

## 2. Context omission needs an actual exposure check

The original context pairs held current requirements, code and accessible archive
bytes fixed. They varied whether 10,307 / 16,276 characters of earlier visible
framing were preloaded. In origin 1, preloading scored 286/302 versus 278/302 for
omission, with two versus fifteen newly broken cases relative to the common
starting code. In origin 2 the scores were 297/302 versus 296/302, with no new
regressions. Omission used fewer native tokens in both pairs.

Both omission workers directly reloaded the framing archive. The original
contrast therefore measures initial preload versus later loading more clearly
than sustained selective forgetting. Its scores remain preserved.

A prospective follow-up used 84 unused queries plus 195 regression queries. Both
arms received the same instruction to retrieve historical prose for a specific
current gap; one also preloaded framing. The updated skill, programs, archives,
permissions, tools and budgets were matched within each pair. This is a separate
profile and instruction regime, not a replacement result or an old-versus-new
skill comparison.

| Follow-up | Preloaded framing | Omitted framing | New regressions, preloaded / omitted | Native tokens, preloaded / omitted |
| --- | ---: | ---: | ---: | ---: |
| Origin 1 | 262/279 | 272/279 | 0 / 0 | 276,181 / 2,908,394 |
| Origin 2 | 278/279 | 278/279 | 0 / 0 | 923,443 / 1,728,901 |

Omission improved origin 1 by three fresh and seven old cases, and tied origin 2;
no follow-up worker introduced a regression relative to its common starting
program. Omission used more total tokens and more uncached input plus output in
both pairs. The result supports a possible quality/cost trade-off in one history,
not a generally better policy or proof of an internal anchoring mechanism.

Neither omission worker directly reread the framing archive in the recorded read-tool calls; both retrieved factual prior feedback. This makes the follow-up exposure contrast clearer than the original one. This audit does not establish comprehension or a complete system-call trace of Python-mediated file reads. The follow-up tests preloading under a selective policy, not the isolated causal effect of changing that policy.

**Decision:** do not add an automatic reset rule. Current requirements and verified
artifacts must survive any context policy, and actual history retrieval must be
observed. This study concerns conformance repair with an archive retained; the
forgetting paper studies a stronger state-removal intervention in optimization.

## 3. Corrections reached real outputs, with retention and cost trade-offs

All four correction workers passed **25/25 three-version queries**, covering
**75/75 actual version-specific output decisions** each. They recomputed values
and paths, including a query whose selected node changed and then reverted.

The extra source-to-output linking cue improved old-case retention in origin 1:
194/195 old cases versus 190/195 for ordinary verification, with one versus five
regressions. In origin 2 both passed all 195 old cases without regressions. Thus
the complete-profile scores were 219/220 versus 215/220 in origin 1, and 220/220
for both in origin 2. The linking cue used more total native tokens and more
uncached input plus output in both pairs.

**Decision:** continue checking actual affected outputs and unchanged behavior.
Both conditions already did this. The additional cue showed a retention benefit
in one pair, but no advantage on the primary correction endpoint, and has not
earned a mandatory reflection or dependency-report step.

## Verified engineering changes and the shared skill

Two concrete representation failures were repaired and verified:

1. The accounting reader treated legal Unicode separators inside JSON strings as
   record boundaries. An LF-framed reader recovered usage from preserved event
   bytes. Seven boundary checks and 22 existing accounting checks passed; original
   receipts were retained.
2. A post-hoc diagnostic used literal decoded source text through the same guarded
   patch broker. It repaired the Unicode case, raising that saved program from
   292/296 to 293/296 with no regression. Stale-source and protected-file edits
   remained rejected. This was an operator-derived repair with zero new model
   calls; the original model score stays 292/296.

One existing optional operational check was clarified in two evidence-driven
steps: distinguish record delimiters from legal data characters; derive literal
tool arguments from decoded content rather than quoted display text; recompute
and verify the affected saved outputs after a correction. The main SKILL.md stays
unchanged. The mechanical corrections are verified; an isolated performance gain
from the new wording has not been established. Existing mechanism-verification
guidance already covered checking actual context exposure, so no duplicate rule
was added for that finding.

## Costs and scope

The recorded native total is **at least 39,776,091 tokens**, including at
least 37,770,368 cached-input tokens. Recorded uncached input plus output
is at least 2,005,723 tokens. Acquisition, adaptation, the failed
attempt and feedback recovery are included once in that total; endpoint costs and
zero-call replays are reported separately below.

The interrupted adaptation's final feedback generation has no captured usage
total. Coordinator usage, complete validation/acquisition/archival overhead and
whole-system/remote-model energy are also unavailable. These token figures are
not measured dollar costs, and cached tokens are not counted as free. A complete
all-in cost-effectiveness claim remains unsupported.

The study used two origin histories, one [public JSONPath source family](https://github.com/jsonpath-standard/jsonpath-compliance-test-suite/tree/20ebdcce5008c8a777ee9c80ad853ecf606950b5)
under [RFC 9535](https://www.rfc-editor.org/rfc/rfc9535.html),
gpt-6-luna/medium and the existing Windows/Codex controller with offline bounded
Docker execution. One origin needed feedback-only recovery; no program or score
was resampled to make it succeed. Case counts share programs and are not
independent learner replications. The deterministic profile excludes nine
multiple-order vectors; fresh inputs are fresh within this allocation, not proven
absent from pretraining. The evaluator is coordinator-readable. No statistical
superiority, hostile whole-agent isolation, broad portability, production parser,
weight-learning, energy-saving or universal RSI claim follows.

The next justified candidate is a compact, precise recovery aid for failed tool
operations, tested against clear ordinary tool documentation on a new task. The
present evidence favors investigating that execution bottleneck over adding more
mandatory reflection prose. That is a proposal, not a completed comparison.

## Primary sources

- [Pinned JSONPath conformance suite](https://github.com/jsonpath-standard/jsonpath-compliance-test-suite/tree/20ebdcce5008c8a777ee9c80ad853ecf606950b5)
- [RFC 9535: JSONPath](https://www.rfc-editor.org/rfc/rfc9535.html)
- [RFC 9485: I-Regexp](https://www.rfc-editor.org/rfc/rfc9485.html)
- [Recurrent Harness for Agentic Continual Learning](https://arxiv.org/html/2610.12668v1)
- [Scaling Discovery Requires Forgetting](https://arxiv.org/pdf/2610.20563v1)
- [LongHarness](https://arxiv.org/html/2610.13075v1)


## Recorded results and costs

Snapshot: 2026-10-19T20:36:03.641043+00:00. 26 terminated native attempts; 0 pending.

Atomic queries are dependent checks of shared programs. These are two learner origins, not hundreds of independent learners. Regressions are previously passing queries broken relative to each common starting executable.

## Later lesson use

| Cell | Condition | Fresh queries correct | Old queries correct | All correct | New regressions | Native tokens incl. cache | Uncached input + output | Seconds |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| S1-F | frozen | 86/101 | 183/195 | 269/296 | 0 | 667,399 | 65,671 | 253.6 |
| S1-H | handoff | 96/101 | 195/195 | 291/296 | 0 | 2,364,129 | 86,625 | 431.4 |
| S1-N | none | 95/101 | 193/195 | 288/296 | 0 | 1,838,731 | 91,403 | 430.5 |
| S1-R | revised | 98/101 | 195/195 | 293/296 | 0 | 999,753 | 54,345 | 333.2 |
| S2-F | frozen | 100/101 | 195/195 | 295/296 | 0 | 1,776,800 | 92,704 | 426.8 |
| S2-H | handoff | 98/101 | 193/195 | 291/296 | 0 | 259,973 | 49,669 | 189.6 |
| S2-N | none | 97/101 | 192/195 | 289/296 | 2 | 927,021 | 87,085 | 342.6 |
| S2-R | revised | 98/101 | 194/195 | 292/296 | 0 | 443,192 | 44,344 | 212.9 |

## Original context projection

| Cell | Condition | Fresh queries correct | Old queries correct | All correct | New regressions | Native tokens incl. cache | Uncached input + output | Seconds |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| C1-FULL | accumulated | 96/107 | 190/195 | 286/302 | 2 | 3,055,462 | 118,374 | 508.8 |
| C1-RESET | reset | 96/107 | 182/195 | 278/302 | 15 | 1,555,637 | 77,109 | 333.0 |
| C2-FULL | accumulated | 102/107 | 195/195 | 297/302 | 0 | 1,851,562 | 136,106 | 444.8 |
| C2-RESET | reset | 101/107 | 195/195 | 296/302 | 0 | 548,119 | 45,847 | 255.9 |

## Actual source-corrected outputs

| Cell | Condition | Fresh queries correct | Old queries correct | All correct | New regressions | Native tokens incl. cache | Uncached input + output | Seconds |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| P1-L | linked_output | 25/25 | 194/195 | 219/220 | 1 | 2,726,606 | 127,054 | 508.0 |
| P1-O | ordinary_output | 25/25 | 190/195 | 215/220 | 5 | 1,697,176 | 69,400 | 428.2 |
| P2-L | linked_output | 25/25 | 195/195 | 220/220 | 0 | 915,942 | 51,302 | 275.4 |
| P2-O | ordinary_output | 25/25 | 195/195 | 220/220 | 0 | 348,625 | 33,489 | 196.9 |

Fresh correction success requires all three versions of a query to be correct. The 25 query units contain 75 version decisions.

- P1-L: 75/75 individual version decisions correct.
- P1-O: 75/75 individual version decisions correct.
- P2-L: 75/75 individual version decisions correct.
- P2-O: 75/75 individual version decisions correct.

## Separate follow-up: selective history retrieval

| Cell | Condition | Fresh queries correct | Old queries correct | All correct | New regressions | Native tokens incl. cache | Uncached input + output | Seconds |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Q1-FULL | selective_preloaded | 74/84 | 188/195 | 262/279 | 0 | 276,181 | 35,029 | 211.5 |
| Q1-RESET | selective_omitted | 77/84 | 195/195 | 272/279 | 0 | 2,908,394 | 93,034 | 520.8 |
| Q2-FULL | selective_preloaded | 83/84 | 195/195 | 278/279 | 0 | 923,443 | 74,291 | 317.0 |
| Q2-RESET | selective_omitted | 83/84 | 195/195 | 278/279 | 0 | 1,728,901 | 78,853 | 469.6 |

## Zero-model-call artifact reuse

| Origin artifact | Endpoint | Fresh correct | Old correct | Total correct | Replay seconds |
| --- | --- | ---: | ---: | ---: | ---: |
| A1F | CONTEXT2 | 92/107 | 183/195 | 275/302 | 36.4 |
| A1F | CONTEXT3 | 73/84 | 183/195 | 256/279 | 25.4 |
| A1F | CORRECTIONS2 | 0/25 | 183/195 | 183/220 | 28.7 |
| A1F | LATER2 | 86/101 | 183/195 | 269/296 | 39.8 |
| A2 | CONTEXT2 | 100/107 | 193/195 | 293/302 | 34.6 |
| A2 | CONTEXT3 | 82/84 | 193/195 | 275/279 | 23.7 |
| A2 | CORRECTIONS2 | 0/25 | 193/195 | 193/220 | 27.4 |
| A2 | LATER2 | 98/101 | 193/195 | 291/296 | 41.0 |

## Acquisition, adaptation and failed-attempt costs

| Cell | Outcome | Atomic score | Recorded total tokens | Cached input | Uncached input + output | Seconds |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| A1 | task scored; later feedback interrupted | 87/92 | ≥ 2,738,023 | ≥ 2,648,064 | ≥ 89,959 | 439.5 |
| A1F | completed | 87/92 | 160,434 | 129,280 | 31,154 | 123.9 |
| A2 | completed | 90/92 | 1,344,543 | 1,273,472 | 71,071 | 409.6 |
| F0-O | completed | 76/95 | 2,375,196 | 2,283,776 | 91,420 | 512.8 |
| O1 | completed | 84/103 | 3,097,647 | 2,983,424 | 114,223 | 538.4 |
| O2 | completed | 94/103 | 2,247,202 | 2,151,040 | 96,162 | 517.6 |

Recorded native total: **at least 39,776,091 tokens**, including at least 37,770,368 cached-input tokens. Recorded uncached input plus output: at least 2,005,723 tokens.

A1 has an unreported interrupted feedback tail. Coordinator usage and full hardware/remote-model energy are unknown. These are not measured dollar costs. Shared acquisition is counted once in the actual experiment total; hypothetical deployment sequences would charge their relevant acquisition and reuse costs.

- Shared acquisition for origin 1: at least 5,996,104 native tokens, before any endpoint worker.
- Shared acquisition for origin 2: 3,591,745 native tokens, before any endpoint worker.

Complete scored endpoint profiles: 2 / 20. Token-per-completely-correct-task is not meaningful for a condition with no such completion; partial-case scores do not substitute for it.

The ordinary screen and both histories remain in the inclusive cost ledger. A1F is a separately charged feedback-only recovery, not an additional successful adaptation or repair retry. Summed worker durations are not elapsed experiment duration because workers overlapped.

## Evidence identities

The original private receipts remain preserved. These hashes identify the retained study artifacts; the generic package does not install the research-specific native host or provide a new portability guarantee.

- `PLAN.md`: `d953dc105942521ea085ad075a9bf86621df33bffa587b0b36425452b3c6c1e9`.
- `CONTEXT_FOLLOWUP_PLAN.md`: `ecece87eef297a414a2e77d28a5117ff11b80a65011a2014401a829f88045c1d`.
- `ANALYSIS.current.json`: `8d0c861ced04818e54335ab6a68dca768d3c258501d8f2bd3826af5390569ac8`.
- `FINAL_VERIFICATION.json`: `1b808365aeade51d33d2d466b2c3885865dfc3fc43f4aa44c561e5adeb126172`.
