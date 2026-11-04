# Do typed failure summaries improve later repairs?

19 October 2026 · Completed exploratory comparison · Current REL in every arm

## Result

**No better repair reliability was demonstrated.** Raw, compact and typed feedback
each produced one completely correct repair out of four attempts. Typed feedback
localized the recorded differences and was much smaller, but one typed worker
submitted no program. It therefore had fewer passed cases overall. These results
do not justify installing typed summaries as a default REL workflow.

| Feedback | Complete repairs | Passed cases, cohort A | Recorded tokens | Cached input | Uncached input + output |
|---|---:|---:|---:|---:|---:|
| COMPACT | 1/4 | 54/64 | 1,835,401 | 1,618,048 | 217,353 |
| RAW | 1/4 | 54/64 | 1,647,946 | 1,460,992 | 186,954 |
| TYPED | 1/4 | 44/64 | 1,607,273 | 1,426,944 | 180,329 |

The second cohort produced the same per-program scores. Those were twelve
unchanged-program replays, not twelve additional model attempts. Case totals are
dependent checks within four paired origin/repeat blocks, not independent trials.

## Research and comparison design

The predecessor supplied two independently authored, actually acquired programs
from six-episode sequences. Origin O retained an extra null timestamp; origin S
misclassified valid decimal JSON as invalid JSON. Their unchanged checkpoints
passed 10/16 and 8/16 fresh checks respectively. Every arm received the same
current REL snapshot, acquired program, complete raw feedback, current contract,
public examples, tools, permissions and resource limits. Only the supplied
feedback view changed. Every worker could inspect raw evidence and build its own
diagnostic. This was a feedback-presentation study under REL, not REL versus no REL.

- **Raw:** exact original feedback.
- **Compact:** failed records with full expected/observed outputs and source
  pointers, omitting repeated input bodies and general metadata.
- **Typed:** deterministic JSON Pointer mismatches preserving presence, type and
  values, with explicit omission indicators and source recovery. No generated
  diagnosis, proposed patch, code location or extra expected facts.

Twelve subscription-native gpt-6-luna/medium sessions used fresh contexts:
two origins × three arms × two repeats. Order was pinned, at most two ran
concurrently, and each had 60 actions / 900 seconds. There were no retries or
outcome-driven additions. Candidate code ran only through the existing offline
bounded Docker evaluator; no GPU, paid API fallback or additional model service
was used. Every terminal receipt has reconciled usage and owned-process cleanup.

The two fresh cohorts each contained 16 constructed cases: four mixed event logs
with hundreds of physical items, overlapping named source/time queries, and
focused null, numeric, window, offset and malformed-input cases. Two previously
qualified, differently implemented oracle chains agreed on all 32 expectations.
Positive, wrong-output and unchanged-program fixtures ran in the actual evaluator.
The coordinator could read gold; this was not a hostile sealed evaluation. Both
cohorts share a generator and a CloudEvents/RFC source family. Some focused cases
differ primarily in identifiers. Neither is an independent production dataset.

The deterministic formatter passed 252 independent reconstruction cases plus
schema, missing-diagnostic, duplicate-member, truncation and large-value checks.
These qualify its transformation behavior, not the truth of its expected outputs
or its effectiveness as a model intervention.

## Every matched result

| Origin / repeat | Raw: cases / tokens | Compact: cases / tokens | Typed: cases / tokens |
|---|---:|---:|---:|
| O / 1 | 16/16 / 568,844 | 10/16 / 369,850 | 0/16 / 308,662 |
| O / 2 | 10/16 / 310,810 | 16/16 / 491,395 | 16/16 / 429,700 |
| S / 1 | 14/16 / 383,783 | 14/16 / 339,684 | 14/16 / 384,310 |
| S / 2 | 14/16 / 384,509 | 14/16 / 634,472 | 14/16 / 484,601 |

Typed versus raw: one block improved, one worsened, two tied. Four blocks from
two acquired programs cannot establish a population effect or broad portability.
No significance or universal RSI claim is made.

## What the traces and submitted artifacts show

1. **Localization did not ensure a correct action.** O/1 compact and O/2 raw
   submitted byte-identical acquired programs. Their recorded checks printed
   that the output did not match expected feedback, while matching the old
   observed output. O/1 compact additionally tested the incorrect rule that a
   null timestamp should remain. Other repeats repaired the same defect.
2. **Artifact completion is a separate failure.** O/1 typed made two write calls
   containing only `op` and `path`; the required `text` was absent in the original
   server requests and local receipts. The loaded tool description explicitly
   required it. Both calls were correctly rejected and preserved, and no
   `pipeline.py` was submitted. All 16 checks failed for a missing artifact, not
   16 demonstrated semantic bugs. Its ten previously passing checks are counted
   as regressions in end-to-end delivery, with that cause kept explicit.
3. **Repairing reported feedback did not cover every requirement.** All six S
   workers fixed decimal classification, improving from 8 to 14 passing cases.
   They retained two timestamp errors per cohort. Internal normalized UTC values
   can fall in 1969 or 2100 even though permitted external local-calendar inputs
   are restricted to 1970–2099. The code incorrectly revalidated the internal
   representation against the external spelling restriction.

All arms repaired 18 previously failing case instances on cohort A. Raw and
compact each retained ten old failures and no new failures. Typed retained ten
old failures and lost ten previously passing checks through the single missing
submission. A format's assigned arm does not prove that it caused a tool error.
We do not discard the failed attempt or infer a hidden motive from the trace.

## Total observable cost and its limits

Recorded worker cost was **5,090,620 tokens**, including
**4,505,984 cached input tokens**; uncached input
plus output was **584,636**. Cached input
is a subset of input and must not be added again. Each arm made 53 model requests;
actions were raw 88, compact 86 and typed 86. Summed worker dispatch time was
1648.798 seconds.
This sum includes overlapping workers and is not the study's elapsed duration.

Typed recorded 2.47% fewer total tokens than raw in aggregate. The failed O/1
typed block saved 260,182 tokens; the other three paired blocks together cost
219,509 more. Typed cost more in each of those three blocks. The net reduction
therefore does not establish a useful efficiency gain. Because every arm had
one fully correct repair, recorded tokens per complete repair equal the totals
in the table. Compact used 11.38% more tokens than raw without an aggregate
correctness improvement.

| Origin | Raw bytes | Compact bytes | Typed bytes | Typed construction wall ms |
|---|---:|---:|---:|---:|
| O | 203,563 | 164,347 | 10,487 | 38.506 |
| S | 86,081 | 13,340 | 1,754 | 0.866 |

Typed views were approximately 94.85% and 97.96% smaller than raw bytes. This
was a one-time deterministic construction, not another model call. Reported
construction wall time across all six views was 47.136 ms;
CPU time was 31.25 ms in total at coarse timer resolution. Zero-valued short
CPU samples do not mean zero resource use. Formatter development, qualification,
file loading and source recovery are not represented by that construction number.
Worker source recovery and failed attempts are included in recorded worker cost.

The earlier two six-episode acquisitions already cost 5,307,037 recorded tokens
(4,705,024 cached input; 602,013 uncached input plus output). This is shared
historical expenditure, not newly incurred spending or a charge repeated per arm.
Including that historical token ledger and this comparison gives 10,397,657
recorded worker tokens, still excluding other precursor research.
The current evaluator qualification took 52.653 summed seconds, second-cohort
replays 67.377 seconds, and the separate repair verification
15.656 seconds. These are separate from the enclosing native worker
timings; nested worker tests are not added again. Parent analysis and research,
complete setup cost, currency, remote compute and physical energy remain unknown.
This is inclusive **recorded worker** accounting, not a full economic-cost claim.

## Corrections and REL decision

The analysis code was corrected before collection to retain a missing submission
as a failed trial instead of assuming every program exists. All twelve attempts,
including rejected tools and absent artifacts, remain in the comparison.

Separately, the coordinator repaired the S timestamp defect on a copy. The
corrected program passed both exposed cohorts, **32/32 checks**, and **6/6 focused
controls**. The original passed 4/6 focused controls and failed the two valid
offset cases. Invalid external 1969/2100 event and query spellings remained
rejected. This confirms a specific engineering repair; it is not an independent
learner acquisition or fresh performance result, and original scores are unchanged.

REL's optional method catalogue now clarifies that a localized structural
mismatch is neither a causal diagnosis nor a completed repair. The main
entrypoint, host runtime and mandatory workflow are unchanged. The formatter
stays a research artifact; no automatic summarizer, extra reflection round or
default typed-feedback policy was adopted. The clarification itself has no
measured model-performance effect.

The next useful question is whether a requirement-linked check of the actual
changed behavior helps workers both complete a repair and catch representation
boundary errors beyond the supplied diagnostic. More repetitions of this format
comparison alone are not presently justified. A new study would need a pinned
intervention, ordinary testing controls, fresh tasks and complete attempt costs.

## Research sources and evidence boundaries

The design used [RFC 6901](https://www.rfc-editor.org/info/rfc6901/) for structural
addressing, [Learning to Debug Programs with LLMs](https://arxiv.org/abs/2304.05128)
and [CRITIC](https://arxiv.org/abs/2305.11738) for execution/tool-feedback background,
and [DebugRepair](https://arxiv.org/html/2604.19305v1) to distinguish reduced test
context from additional intermediate execution evidence. These are primary
background sources, not replications or performance evidence for REL. The local
research record states which sections were inspected and the unavailable route.

Predecessor repository commit: `6ae378b4b3c4ef0a965b79fa3d301008c0f88a6e`.
Tested core manifest SHA-256:
`bbb8e2b06875d18352d4ed1b6e2f6a2fdbd4bcc90d1aaa4f2d1775cd50da52d2`.
Frozen design SHA-256: `2a3bcafef0501deb4b808d394d299f16eb393bd36c922f2dcc0888c4251e2bbb`.
Frozen summary implementation SHA-256:
`3fbbf74b33b7d2446021b6647a32d8e4984e7b8e3674837ab981e199187e02f1`.
The delivered catalogue clarification changes core bytes after these trials;
their scores must not be attributed to that later wording.

The accompanying [de-identified result ledger](EVIDENCE_2026-10-19_TYPED_FEEDBACK.json)
contains all arm/block outcomes and recorded costs. Raw traces, account metadata,
local paths, full study infrastructure and generated programs are not packaged.
This is not a self-contained reproduction of all native model experiments.
