# Does source-checking help beyond additional effort?

21 October 2026 · bounded exploratory repair study · current results include a disclosed evaluator correction

## Finding

This study does **not establish a reliable general advantage** from adding source-directed expectation checking to current REL. The prospectively selected, approximately effort-matched checkpoints contain one tie between unchanged starters and one positive candidate result; the third pair cannot be matched. Later outcomes vary, and the positive checkpoint advantage does not establish a sustained or independently replicated effect.

The strongest engineering finding was an evaluator defect: repeated entry-module execution retained imported dependency state and imposed an undeclared partial hot-reload requirement. It greatly exaggerated one worker's failure. A separate source-free reproduction verified the cause; all selected checkpoints and final artifacts were replayed unchanged using a corrected loader. Both score versions remain. These corrected results are **post-result reanalysis**, not untouched confirmation.

## Research and task choice

The preceding URL comparison favored the added procedure at 82.8% more aggregate uncached tokens. Equal ceilings did not resolve that effort confound. The new plan therefore selected saved artifact checkpoints using costs alone before observing their quality.

Primary-source research covered [test-oracle generation](https://arxiv.org/html/2601.05542v1), [requirements-derived assertions](https://arxiv.org/html/2607.10277v1), official specifications, upstream test loaders and package releases. The papers support distinguishing intended behavior, implementation agreement and actual bug exposure; their small or constrained evaluations do not predict this study's effect. This was a targeted design review, not an exhaustive literature review.

1. **HTTP Structured Fields qualification:** [RFC 9651](https://www.rfc-editor.org/rfc/rfc9651.html), HTTPWG suite commit `781ba38464b2ec4c547e1e14d007d4f5ace7457e`, http-sfv 0.9.9 starter and http-sf 1.4.0 reference. Across 2,127 unique checks, the starter passed 2,118 and an ordinary worker passed 2,125, leaving only two primary errors. The pinned minimum residual-gap rule retired the family and skipped five further model calls. This is useful ceiling evidence, not a treatment comparison.
2. **TOML candidate:** downloaded as data, then rejected because the historical audit found prior use of the same suite. Zero model calls. Acquisition cost remains recorded. The next family was history-checked before acquisition.
3. **JMESPath migration:** real legacy 0.5.0 source repaired against the [official specification](https://jmespath.org/specification.html) and [upstream compliance suite](https://github.com/jmespath/jmespath.py), commit `2812594e69d43098ef60f81f4efc404c071b0418`. The modern 1.1.0 reference passed all 885 admitted checks; the starter passed 720. First ordinary repair left 98 primary errors across eight source files, qualifying the planned six-attempt comparison. This qualification attempt is included, so selection is conditioned on its residual errors.

This is a substantial language-maintenance task involving filters, projections, type rules, operator precedence, functions, expression references, literals and slices. It is still one task family with repeated workers, not 885 independent agent experiments. A maintained dependency upgrade is the practical no-model alternative; the study deliberately constrains workers to repair the provided source rather than copy a replacement. No new upstream defect or novel algorithm is claimed.

The bounded history inventory covered 62 root study records. JMESPath was absent there; this is local freshness, not proof of training-unseen data. Four official examples were public; 881 other cases were primary. Seventeen duplicate inputs and six benchmark-only entries were excluded under the upstream loader rules. Queries contained input only, with no expected values, error labels or family metadata. Ordered input was preserved; finite numeric equality, Boolean distinctions and declared ValueError acceptance followed the task and upstream comparator. Per-query parser-cache clearing was shared with the starter/reference to remove an old Python compatibility artifact.

## Comparison and matching

Both arms loaded the same 20-file REL snapshot (`SKILL.md` SHA-256 `f598cee5206dd415d5884f557442ec29d07dd4049bbcde23d9c9bda214f16c1b`), used gpt-6-luna/medium, fresh native contexts, the full authoritative specification, identical fixtures and tools, and ceilings of 60 tool actions and 900 seconds. Ordinary workers were expressly told to investigate missing requirements and test positive, negative, boundary and regression behavior. No report/reflection was required. Order was R1, C1, C2, R2, R3, C3. The sole assigned difference was an instruction to check a self-authored test's expected answer against the applicable source rule before calling the code wrong. This tests that addition to REL, not REL against no REL.

For each pair, choose the largest common action index from 10 through 40 at which both are at a tool-request/usage boundary and cumulative uncached input plus output upper bounds differ by at most 10% of the smaller. Selection never reads quality. Reconstruct accepted writes/patches and verify exact final artifact hashes. Keep the preceding and subsequent usage bounds. No eligible point means unmatched; never choose the best score or force wasted actions.

| Pair | Actions each | Ordinary primary correct | Added source-checking primary correct | Uncached upper bounds R / C | Total recorded tokens R / C |
|---|---:|---:|---:|---:|---:|
| 1 | 13 | 716/881 | 716/881 | 28,635 / 30,633 | 133,979 / 150,953 |
| 2 | 40 | 725/881 | 773/881 | 75,103 / 73,188 | 1,531,615 / 1,368,932 |
| 3 | Unmatched | — | — | No eligible common point | — |

Pair 1's match is too early to compare completed changes: both artifacts are the original starter. Pair 2's point is useful local evidence for a transient advantage at similar observed effort. One informative matched pair is insufficient to establish reliability. Cached tokens, tool complexity and hidden cognitive effort are not equalized by an uncached-token match; total recorded tokens are therefore shown as well.

## Final artifacts and regressions

Regressions count checks passed by the starter but failed by the saved artifact. Scores below use the corrected loader; interrupted work is explicitly retained.

| Attempt | Correct | Regressions | Actions | Uncached tokens | Total tokens | Completion |
|---|---:|---:|---:|---:|---:|---|
| R-jp-1 | 787/885 | 0 | 59 | 83,596 | 2,284,300 | Completed |
| C-jp-1 | 765/885 | 40 | 59 | 108,591 | 3,325,231 | Completed |
| R-jp-2 | 828/885 | 19 | 60 | 98,221 | 3,195,437 | Completed |
| C-jp-2 | 814/885 | 39 | 60 | 99,784 | 2,846,408 | Completed |
| R-jp-3 | 807/885 | 29 | 60 | 65,804 | 1,409,548 | Completed |
| C-jp-3 | 729/885 | 0 | 60 | 59,037 | 1,522,333 | Interrupted; recovered artifact |

No saved artifact completes the entire contract. A final score is not an effort-matched causal estimate. Original-to-corrected final scores changed for: C-jp-1: 95 to 765. Other final scores stayed unchanged. The original catastrophic 95/885 score must not be cited as an unqualified model failure.

## Prespecified sensitivity views

Fixed action counts do not match tokens. Common token budgets select the latest request boundary under the budget and may leave different unused allowance; those differences are shown rather than disguised as exact equality. These overlapping views are not additional independent trials.

| Pair | View | Actions R / C | Ordinary primary | Source-check primary | Actual uncached upper bounds R / C |
|---|---|---:|---:|---:|---:|
| 1 | Actions 20 | 20 / 20 | 717/881 | 716/881 | 35,552 / 53,868 |
| 1 | Actions 40 | 40 / 40 | 759/881 | 669/881 | 62,341 / 78,596 |
| 1 | Uncached budget 40000 | 23 / 13 | 756/881 | 716/881 | 39,171 / 30,633 |
| 1 | Uncached budget 80000 | 56 / 40 | 783/881 | 669/881 | 79,920 / 78,596 |
| 2 | Actions 20 | 20 / 20 | 716/881 | 716/881 | 48,547 / 49,303 |
| 2 | Actions 40 | 40 / 40 | 725/881 | 773/881 | 75,103 / 73,188 |
| 2 | Uncached budget 40000 | 17 / 12 | 716/881 | 716/881 | 39,361 / 36,361 |
| 2 | Uncached budget 80000 | 44 / 43 | 725/881 | 803/881 | 79,697 / 77,222 |
| 3 | Actions 20 | 20 / 20 | 716/881 | 716/881 | 40,694 / 8,357 |
| 3 | Actions 40 | 40 / 40 | 728/881 | 725/881 | 50,265 / 35,533 |
| 3 | Uncached budget 40000 | 19 / 42 | 716/881 | 725/881 | 38,804 / 38,011 |

## Verified defects, corrections and behavioral observations

**Evaluator lifecycle.** The original grader called `exec_module` again for each group while ordinary Python imports kept dependencies cached. C1's top-level lexer modification was applied repeatedly, causing duplicate named regular-expression groups. [Python's import documentation](https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly) explains the execution operation; [module caching](https://docs.python.org/3/reference/import.html#the-module-cache) explains the retained dependencies. The task did not require partial hot reload. A separate counter fixture reproduced repeated initialization under the old judge and one successful initialization with repeated function calls under the correction; mutation and invalid-shape rejection still worked. The corrected loader retains one successfully initialized module per owned guest batch. All 20 distinct starter/reference/final/selected artifact states were replayed, without changing code, cases, expected values or selected action indices. Reference remained 885/885 and starter 720/885. The previous audit established custody, not semantic correctness; the newly discovered defect qualifies it.

**Interrupted attempt.** C3 requested a 61st tool action after its 60 permitted actions. The host raised before its normal final artifact/usage receipt. No extra model attempt was made. After verifying the process tree was stopped, the collector preserved the last saved bytes and reconciled identity-bound, monotonic native usage through the last action and interrupted terminal event. Five negative/guard checks exercised the collector. Its original failure receipt remains. The recovered score describes an interrupted artifact, not normal task completion. This repairs this study's accounting; automatic finalization in the older source-bound host is not claimed fixed.

**Source use is not source understanding.** Both arms made explicit specification-access attempts. C2's action 56 expected `0 || 4` to produce 4, but its code produced the correct value 0. A source-checking instruction did not prevent the wrong expectation, and the worker did not repair this expectation in a later executed check. In another check sequence, slice outputs changed from errors to expected arrays after edits. These are concrete tool observations, not proof that source checking caused every improvement. No private reasoning trace was used for this assessment.

**Other preserved corrections.** Initial preparation contained a shell-quoting/interface-path failure before inference; its artifacts remain. The JMESPath package license member name was corrected before build completion. The analyzer's inherited starter path was corrected before checkpoint scoring. TOML historical reuse was identified and retired. None of these was silently counted as a learner reasoning failure or a fresh successful task.

## Cost

All seven actual model attempts are included, including qualification and interruption: **16,670,501 recorded total tokens**, **612,645 uncached input plus output**, 414 executed actions, and 2006.8 summed worker wall seconds. Cached input is a subset of input; reasoning output is a subset of output and is never added again.

The six JMESPath attempts used 6,889,285 ordinary versus 7,693,972 candidate total tokens (+11.7%), and 247,621 versus 267,412 uncached tokens (+8.0%). Each arm executed 179 actions. Worker elapsed totals were 727.8 versus 857.4 seconds. One candidate's recorded interrupted usage is identity-checked but lacks the normal completion receipt; no missing cost was replaced by zero.

Successful recorded data-acquisition time: 21.5 seconds, including the retired TOML source. Recorded initial qualification time: 51.2 seconds. Original checkpoint analysis: 147.6 seconds. Corrected state replay: 234.2 seconds. These are separate recorded phases, not an exhaustive elapsed-time or energy total. Parent orchestration tokens, complete engineering effort, some failed setup/diagnostic time, dollar cost and whole-system/remote energy remain unavailable. No direct paid provider API was invoked. Tokens per fully correct completed task are undefined because none met the complete contract; a per-check ratio would not be per-task efficiency proof.

## REL decision and next discriminating question

Do not promote the extra source-checking instruction to a mandatory default. Keep authoritative expectation checking available as ordinary engineering judgment. Preserve its local positive checkpoint, its incomplete application and its costs together.

Update only conditional supporting guidance: (1) actual-work matching and cost-only checkpoint selection when claiming benefit beyond effort; (2) evaluator lifecycle parity when a judge loads/restarts executable artifacts. The main six-step skill and task-facing prompt stay unchanged. These are verified evaluation-method clarifications, not demonstrated improvements in agents' later performance. The current workers used the earlier frozen version.

The completed loop corrected measurement rather than hiding failure. A new independent claim would require a fresh task family, the qualified loader, and prospective matching at meaningful post-change states. Repeating this exposed family until a win appears would not supply that evidence. Before broader claims from older studies using this loader, audit whether their submissions used initialization side effects; this run does not silently revise those historical results.

No claim of universal RSI, sustained cross-session learning, novel architecture, or general superiority follows from this study. The private package contains the generic skill and sanitized evidence; the complete study runner, native traces and source-bound artifacts remain in the local evidence package.
