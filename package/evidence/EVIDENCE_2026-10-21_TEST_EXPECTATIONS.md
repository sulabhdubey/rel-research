# Does checking test expectations against sources improve repairs?

Exploratory study, 21 October 2026. Recursive Evidence Loop (REL), exact installed entrypoint SHA-256 `f598cee5206dd415d5884f557442ec29d07dd4049bbcde23d9c9bda214f16c1b`.

## Decision

The URL comparison produced a local positive result: the added procedure reached 379/419 and 396/419, versus 328/419 and 366/419 for controls, and introduced fewer regressions. Aggregate uncached input-plus-output cost increased 82.8%. The Markdown comparison was mixed and included a destructive final patch. Keep the added procedure experimental rather than promoting it to the default skill. The URL family has only two workers per arm. The study tests an addition alongside current REL; it does not estimate REL versus no REL or learning across sessions.

## Design and execution

R uses current REL plus strong ordinary engineering: source inspection, implementation, executable positive/negative/boundary/regression checks and repair. C receives exactly the same materials and adds an instruction to check a self-authored expected output against the applicable normative rule before diagnosing code. Neither arm must produce another report, checklist or reflection artifact. All workers use gpt-6-luna/medium, fresh contexts, 60 tool actions and 900 seconds including startup. They run serially with no transfer of outcomes between workers. Actual effort may be below the shared ceiling. Ordinary workers run first to qualify residual errors; this fixed order leaves possible service/time effects.

Generated code runs only in the previously qualified offline Docker guest: non-root, read-only root, no network, bounded memory/PIDs/CPU and per-call time. Native Codex uses ordinary account quota; no direct paid provider API or local GPU inference was invoked. URL strings were never visited and generated HTML was not rendered. The coordinator can read scoring gold; this is not a sealed evaluator. Public sources may be in model training.

Two Markdown migration profiles use markdown2 2.5.4 with CommonMark 0.31.2 requirements. Delimiters has 291 positions (189 primary, 25 supplied); links has 248 (150 primary, 21 supplied). They share 90 preserved positions and are not independent domains. Markdown-it-py 4.0.0 agrees with every selected expected output using the exact upstream CommonMark test normalizer.

The fresh-family follow-up migrates a CPython 3.12.15 urllib.parse service toward WHATWG HTTP/HTTPS behavior using stdlib plus supplied IDNA 3.20. Input-based selection retains 419 unique WPT vectors, including 200 failures; eight are supplied examples and 411 are primary. Ada URL 4.0.0 agrees with every source expectation. All cases request the same ten string fields; failure returns failure:true. Origin is omitted because some successful WPT records do not define it. The starting service passes 149/419. Mature conformant libraries are the stronger practical alternatives to these constrained migrations; no new parsing algorithm is claimed.

## Final saved-code outcomes

Primary means absent from the supplied fixture file, not absent from normative examples or globally unseen. Regressions count initially correct positions that became wrong. Individual positions are nested conformance checks, not independent model trials.

| Stage | Worker | All correct | Primary correct | Supplied examples | Regressions | Actions | Tool failures | Uncached input + output |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| markdown | C-delimiters-1 | 170/291 | 90/189 | 25/25 | 16 | 60 | 11 | 91,866 |
| markdown | C-delimiters-2 | 144/291 | 86/189 | 18/25 | 18 | 29 | 1 | 37,608 |
| markdown | C-links-1 | 0/248 | 0/150 | 0/21 | 107 | 60 | 11 | 114,542 |
| markdown | C-links-2 | 156/248 | 84/150 | 21/21 | 14 | 60 | 8 | 91,038 |
| markdown | R-delimiters-1 | 142/291 | 84/189 | 18/25 | 1 | 14 | 1 | 43,706 |
| markdown | R-delimiters-2 | 151/291 | 84/189 | 25/25 | 5 | 60 | 4 | 85,137 |
| markdown | R-links-1 | 147/248 | 84/150 | 21/21 | 1 | 60 | 2 | 105,807 |
| markdown | R-links-2 | 153/248 | 83/150 | 21/21 | 11 | 57 | 3 | 94,425 |
| url | C-url-1 | 379/419 | 371/411 | 8/8 | 6 | 57 | 4 | 117,833 |
| url | C-url-2 | 396/419 | 388/411 | 8/8 | 2 | 59 | 3 | 104,059 |
| url | R-url-1 | 328/419 | 320/411 | 8/8 | 9 | 59 | 6 | 84,008 |
| url | R-url-2 | 366/419 | 358/411 | 8/8 | 25 | 26 | 1 | 37,382 |

Aggregate descriptive totals (cases and trials must not be treated as independent):

| Stage / arm | Complete tasks | Correct positions | Primary correct | Regressions | Recorded total tokens | Cached input subset | Uncached input + output | Worker seconds |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| markdown-comparison-C | 0/4 | 470/1078 | 260/678 | 155 | 8,660,686 | 8,325,632 | 335,054 | 1190.0 |
| markdown-comparison-R | 0/4 | 593/1078 | 335/678 | 18 | 7,476,723 | 7,147,648 | 329,075 | 1140.4 |
| url-comparison-C | 0/2 | 775/838 | 759/822 | 8 | 5,107,908 | 4,886,016 | 221,892 | 718.3 |
| url-comparison-R | 0/2 | 694/838 | 678/822 | 34 | 2,653,102 | 2,531,712 | 121,390 | 452.8 |

URL correctness separated by valid and invalid input, avoiding an aggregate-only view:

| Worker | Valid URLs serialized correctly | Invalid URLs rejected correctly |
|---|---:|---:|
| C-url-1 | 189/219 | 190/200 |
| C-url-2 | 197/219 | 199/200 |
| R-url-1 | 190/219 | 138/200 |
| R-url-2 | 170/219 | 196/200 |

For URL, C changes the aggregate primary total by +81 positions across two workers and uncached input-plus-output cost by +82.8%. This is a descriptive pilot difference, not statistical proof, an independent test of every case, or evidence of sustained improvement.

## What the traces establish

In C-links-1, action 58 passed all 21 supplied fixtures. Action 59 introduced an overescaped star in a regular expression; action 60 reported a compilation error with no action left to undo it. Final-code evaluation failed in every group and scores 0/248. This failure remains in the treatment results. It is one shared implementation exception, not 248 independent failure mechanisms.

A separate post-hoc diagnostic removed the single redundant escape; another exactly reversed action 59 and recovered the recorded prior file hash. Both restored 161/248, including 81/150 primary and 21/21 supplied cases. Neither diagnostic enters the comparative scores. Restored execution still left substantial semantic errors. The existing skill already requires usable checkpoints and budget for validation/recovery; the trace demonstrates failure to enforce that instruction, not proof that another reminder improves behavior.

C-delimiters-1 accessed normative material, passed 25/25 supplied fixtures, and printed a code-span result containing a hard line break where the source rules require space normalization. Printing the result did not check its expected value or repair it. Its final primary score was 90/189 with 16 regressions. The other C delimiter worker reached 86/189 with 18 regressions, while both R workers reached 84/189. A small target gain therefore coexisted with losses in already-working behavior.

Source-access attempts, successful tool execution, assertions, saved changes and final correctness are recorded separately. A failed source-reading command is not counted as a successful read. A source citation or assertion token does not establish correct applicability or complete method uptake. The analysis uses tool events and artifacts, not private reasoning. Worker-level findings are exploratory and do not isolate a universal cognitive cause. Ordinary URL worker R-url-1 also accessed the standard, changed its host handling and executed positive/negative checks (actions 56–58). Source-guided repair was therefore not exclusive to the added instruction.

C-url-1 read the percent-encoding rules (actions 39–40), changed encoding sets, encountered a quoting SyntaxError at action 42, and corrected the source at action 44. A later negative check caught acceptance of a percent-decoded forbidden host character; it repaired the host validation and passed its final visible checks. Its saved artifact reached 379/419 with six regressions, better than either ordinary URL worker on these measures. This supports an observed source-to-code/check sequence, not a claim that every gain came from correcting a self-authored expected answer. Some source searches landed on the table of contents or returned no match.

C-url-2 reached 396/419 with two regressions. Its action 56 printed false comparisons for backslashes in query and fragment components. It changed the relevant code, and action 59 printed true for those same checks and no supplied-fixture mismatches. This is a concrete correction reaching the actual output. It is not a demonstrated revision of a wrong expected answer; not every expected value has a separately verified source-to-assertion link.

Equal ceilings did not equal equal consumed compute: ordinary URL worker R-url-2 finished after 26 actions, while C-url-1 used 57. The design measures an instruction's bounded practical result, but cannot isolate semantic expectation checking from additional effort. No cost-matched forced-effort control or per-protocol mechanism effect is established.

## Corrections and limits that matter

1. The first Markdown source compiler mishandled empty expected HTML. Exact reconstruction against the independent official JSON caught and repaired it before model calls. Initial comparison formatting was then found too strict: two qualification calls were preserved and excluded, six unstarted cells were superseded, and a new comparison used the upstream normalizer with rejection controls. No official expected HTML was rewritten.

2. Historical review found 285/291 delimiter inputs and 239/248 link inputs already present with identical expected HTML in the earlier CommonMark 0.30 study. New parser bytes and workers did not make this family fresh. The Markdown results are repeated-family evidence. A reproducible inventory of 58 root study records found URL handling previously deferred, without an executed URL study in that bounded inventory. This is not exhaustive history or training-data coverage.

3. The first URL packet gave failure records an empty requested-field list. That metadata could disclose the answer. One started pilot was preserved and excluded; three unstarted cells were superseded. Every corrected query has the same ten-field list, exact projected source gold and complete reference agreement. The corrected comparison has new worker contexts but follows this exposed pilot. The substantive R/C instruction was not changed after its results.

4. Managed download/Docker access failures and a diagnostic copy inheriting read-only attributes were preserved. Authorized scoped access and copyfile-based diagnostic copies resolved those setup issues. No uncertain model attempt was rerun or omitted. No unrelated project or machine configuration was changed.

5. The comparator, task scope, metadata, source freshness and recovery path all needed actual verification. These were execution/evaluator defects; the current skill already instructs those checks. The repaired local tools and evidence are retained without claiming that writing new policy would have prevented the errors.

## Inclusive recorded cost

All 15 model attempts are included: 12 comparison attempts and 3 excluded qualification/pilot attempts. Across 649 recorded native requests: 28,170,301 total tokens, including 26,962,048 cached input, and 1,208,253 uncached input plus output. Worker elapsed time totals 4250.1 seconds. Cached input is a subset of input, and reasoning output a subset of output; neither is added twice.

Additional recorded source acquisition took 12.48 seconds across 24 unique receipts; qualification guest work took 158.69 seconds. The two diagnostic executions total 10.78 seconds. These measurements do not cover all coordinator tokens, engineering/inspection time, failed setup latency, dollar cost or local/remote energy. No claim of complete economic cost or energy efficiency is made.

Excluded attempts retain their measured outcomes and cost in the structured appendix. Token cost per correct completed task is undefined when no complete tasks succeed; replacing that denominator with passing examples would misstate success. Cumulative per-case totals are descriptive workload measures only.

## REL disposition and next decision

Keep the 20 installed core files unchanged. Update the evidence, worked examples and experimental-method status. Retain source-checking as an opt-in candidate rather than a mandatory extra pass. The verified practical changes are exact-source comparison, a constant output interface that removes answer metadata, historical corpus-identity review, and preserved final-artifact recovery diagnostics. None demonstrates autonomous weight change, universal RSI effectiveness or a better architecture.

The next useful development is a task-local executable safeguard that leaves a previously checked artifact recoverable before a risky final change, with real action-budget enforcement. Its check would use the worker's declared executable checks, not secret scoring gold; a compile-only check would miss the runtime regular-expression error observed here. Existing host recovery capabilities must be checked before building another mechanism. Any genuinely missing safeguard should be compared with ordinary checkpointing on new work; this is a proposal, not a result here. More source-check reminders or repetitions of the same public parser corpus are not justified by this study alone.

## Primary sources and reproducibility

- [CommonMark 0.31.2 specification and examples](https://spec.commonmark.org/0.31.2/).
- [Exact upstream comparison implementation](https://github.com/commonmark/commonmark-spec/blob/0.31.2/test/normalize.py).
- [Current WHATWG URL standard](https://url.spec.whatwg.org/) (retrieved identity 845bafca22fb0c5a42c4bf384a9bdea525a2f10d).
- [Pinned WPT URL records](https://github.com/web-platform-tests/wpt/blob/c48d58747e1f211527fb695fd60548a997fae617/url/resources/urltestdata.json).
- [Ada URL documentation](https://ada-url.readthedocs.io/en/latest/).
- [CPython 3.12.15 urllib.parse source](https://github.com/python/cpython/blob/v3.12.15/Lib/urllib/parse.py).

The private local evidence bundle retains plans, source bytes/digests/licenses, release bindings, all attempts, tool receipts, frozen outputs, exact-source scoring, exclusions, diagnostics and final audit. The generic repository contains a sanitized evidence summary and method disposition, not the full native research harness. Independent reproduction still requires a compatible host and model access.
