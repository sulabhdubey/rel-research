# REL and completing requirements absent from examples

21 October 2026. **Current REL improved the target score on one profile and tied ordinary work on the other. An added requirement-derived testing procedure completed the object profile, but performed worse than current REL on the array target. One of six workers completed its entire scoped task. The candidate remains experimental.**

## Question, sources and controls

Can REL help an agent implement explicit current requirements that are absent from supplied examples? The preceding TOML study could not isolate REL because all conditions already had it. This study compares ordinary engineering without REL (O), the current installed REL (R), and that same REL plus a requirement-derived behavioral-checking instruction (C).

Two substantial service profiles extend the real fastjsonschema 2.21.2 source to scoped JSON Schema 2020-12 behavior: object dependency/unevaluated-property validation and array prefix/items/contains/unevaluated-item validation. Both must preserve and correctly implement the declared Draft 7 route. Upstream fastjsonschema documents Draft 4/6/7 support; this is a constrained extension request, not a claim that upstream promised these newer features. The scopes share 516 legacy positions and one upstream source family. They are related profiles, not two independent domains.

The exact official test-suite commit is `0b4a7fa5e79c5e1ed60d5c034b951003bbba7fd4`. All policies receive identical complete scoped contracts, normative specification text, starting source, and source-checked examples: 20 object and 23 array examples. The examples are explicitly described as incomplete. Primary scores concern modern requirement families absent from those examples; exact query overlap with examples is zero. This is not a comparison between complete information and hidden requirements.

O receives strong ordinary instructions to implement all requirements and use positive, negative, boundary and regression checks. R additionally loads the exact installed 20-file REL snapshot and points to its optional source/claim reference. C adds a procedure to derive behaviors from requirements, create executable discriminating checks, follow failures to saved changes, and check preserved behavior. No extra essay, checklist file, lesson or answer artifact is required. All workers may author their own tests. The candidate is a coordinator-proposed method derived from prior findings, not an autonomously invented improvement procedure.

Six fresh native Codex sessions used **gpt-6-luna/medium**, 60 tool actions and 900 seconds including startup. The fixed serial order was O-object, O-array, R-object, C-array, C-object, R-array. Actual skill loading/absence, protected inputs, real broker writes, offline Docker execution and process cleanup were checked. Worker code ran in the existing network-disabled, resource-limited guest. There was no GPU or paid-provider fallback. The reverse-engineering skill routed the investigation to ordinary source tools because complete source was available; no decompilation or REA setup was needed.

The two ordinary endpoints qualified remaining target errors before completing the comparison. Their observations are included once, not reused as independent feasibility and confirmation samples. No model attempt was discarded or rerolled, and no worker received another worker's results.

## Evaluator defects and the corrected scope

Qualification caught two important coordinator issues. First, jsonschema 4.17.3 disagreed with official nested boolean/number enum cases and an additional-property annotation case. A version/checksum-bound jsonschema 4.26.0 reference agreed with every selected official expectation. The old reference failures remain recorded; labels were not changed to fit it.

Second, the original keyword-based scope filter admitted seven object cases using a structural local-reference cycle, even though the task excluded recursive references. One of these caused a whole ordinary-worker batch to fail. After observing that exception, a data-only reference-graph check identified the out-of-scope group. The correction removed it, regrouped the retained queries and rescored unchanged frozen object artifacts. The array profile had no such cases. A corrected compiler rebuilt every retained query and expected boolean directly from the pinned upstream ZIP. The independent reference passed the corrected 676-object and 688-array profiles.

Original object scores were O=655/683, R=679/683 and C=683/683. Corrected scores are O=672/676, R=672/676 and C=676/676. Thus the apparent **24-position current-REL advantage on objects disappears after the scope correction**. The correction is disclosed exposed analysis, not fresh independent confirmation. Original artifacts, costs and scores are preserved. This is an execution failure in applying existing evaluator/contract checks, not evidence that a new mandatory rule would fix every scope error.

## Results on the corrected declared scope

| Worker | All positions | Target requirements absent from examples | Starter regressions | Recorded tokens | Uncached input + output | Actions | Dispatch seconds |
|---|---:|---:|---:|---:|---:|---:|---:|
| O-object | 672/676 | 136/140 | 4 | 1,252,333 | 70,125 | 46 | 317.5 |
| R-object | 672/676 | 136/140 | 4 | 901,799 | 59,175 | 37 | 250.0 |
| C-object | 676/676 | 140/140 | 0 | 2,153,274 | 126,394 | 50 | 452.4 |
| O-array | 657/688 | 128/132 | 3 | 426,632 | 43,144 | 20 | 165.7 |
| R-array | 686/688 | 132/132 | 2 | 2,160,436 | 98,228 | 54 | 294.6 |
| C-array | 684/688 | 128/132 | 3 | 1,649,265 | 96,497 | 44 | 294.8 |

Every worker passed its supplied examples. Only C-object completed the full scoped profile, with zero scored regressions. O-object and R-object rejected the same four valid conditional-annotation cases. R-array completed all 172 modern cases, including 132 target cases, but incorrectly accepted two invalid legacy conditional cases. C-array completed all 516 legacy cases but rejected four valid modern unevaluated-item cases. O-array retained additional legacy errors. A higher aggregate score therefore does not eliminate the need to report invalid acceptance, valid rejection and regression separately.

R-O: objects tied correctness with 15.6% fewer uncached input-plus-output tokens; arrays gained four target positions and 29 total positions with 127.7% more such tokens. C-R: objects gained four target positions and completed the task, using 113.6% more uncached input-plus-output tokens; arrays lost four target positions and two total positions while using 1.8% fewer such tokens. These are descriptive observations from one worker per condition/profile, not statistically established effects or a uniform cost advantage. Selecting the best condition for each profile after seeing the results would be an oracle selection, not a demonstrated routing policy.

## What actually changed inside a successful attempt

C-object initially constructed a test expecting successful conditional annotations to be discarded. Its early self-authored check batch passed, so passing its own tests did not establish correct interpretation. It then reopened normative sections, including conditional applicators, revised the test expectation, and changed the saved implementation to retain annotations from a successful `if`. Later positive/negative interaction checks and the frozen official evaluation passed. The source reads, accepted patch and subsequent executable checks are recorded at actions 37–40 and 45–50.

This is a concrete observed path from an incorrect assumption through source research to corrected tests, changed code and verified output. It demonstrates within-task adaptation, not learner-authored cross-session memory, sustained recursive improvement or model-weight change. C-array also executed the requested method and passed 30 additional generated behavior checks, yet retained four official target failures. Generating more tests and naming requirements do not guarantee that those tests distinguish the relevant semantic error.

## Cost and accounting

All six attempts are included: **8,543,739 recorded tokens**, comprising 8,441,222 input and 102,517 output. **8,050,176 cached input tokens are already included**, not added again. Uncached input plus output totals **493,563**. Reasoning-token counts are an output subset. There were 210 model requests, 251 tool actions and 15 recorded failed tool calls.

Summed inclusive worker dispatch time was 1775.085 seconds. This includes startup, model/tool work, frozen grading and shutdown; nested tool time is not added again. Recorded initial/reference qualification took 121.330 seconds and separate corrected-scope grading took 128.003 seconds. Acquisition and setup receipts preserve the available durations and failures. Coordinator-only scope rescoring overlapped R-object, so these durations do not isolate a causal latency effect under identical host load.

Complete coordinator model tokens and engineering time, initial partial acquisition duration, currency and physical local/remote energy are unknown. These are complete recorded worker costs, not complete economic cost-effectiveness. With one complete worker result, a global tokens-per-completion ratio would mix different conditions and tasks; it is not a reliable estimate of future cost per success.

Setup errors are preserved: managed DNS and Docker access failures, an incorrect guessed specification URL, a wheel-versus-sdist builder assumption, and malformed inline inspection commands. Scoped access or corrected saved scripts resolved them. None is silently counted as a learner reasoning failure. All six native processes returned normally with descendant absence verified.

## REL decision and next decision-changing work

Keep the installed main loop and its 20 core files unchanged. The candidate's object success is worth retaining as an **opt-in experimental recipe and worked example**, but its array loss and increased cost block an automatic/default promotion. Update the private package's evidence, examples and experimental-method documentation with both wins and losses. The source-selection compiler is repaired in the study tooling; it is domain-specific and is not added to the generic skill.

The next useful question is whether checking an agent-created test's expected result against an authoritative source or a discriminating counterexample improves later repair, compared with ordinary test writing at a matched budget. It needs a different qualified task and fresh evidence. Repeating these now-exposed conditional cases or combining the best outcomes would not establish transfer. A mature validator remains the practical strong alternative where replacing the dependency is allowed; the constrained in-place task does not show that a model-written validator is preferable.

## Limits and source links

One source family, two related profiles, one attempt per condition/profile, small residual target headroom, public potentially training-exposed cases, coordinator-readable gold and an exposed scope correction limit inference. Case counts are not independent sample sizes. No novelty, universal RSI, perfection, broad portability, energy saving or sustained learning claim follows. The local evidence retains exact inputs, source identities, frozen outputs, traces, costs, original errors and corrected results. The generic private repository does not bundle the complete native research host.

Primary sources: [JSON Schema 2020-12 release notes](https://json-schema.org/draft/2020-12/release-notes), [core specification](https://json-schema.org/draft/2020-12/draft-bhutton-json-schema-01), [validation specification](https://json-schema.org/draft/2020-12/draft-bhutton-json-schema-validation-01), [official source suite](https://github.com/json-schema-org/JSON-Schema-Test-Suite/tree/0b4a7fa5e79c5e1ed60d5c034b951003bbba7fd4), [fastjsonschema documentation](https://horejsek.github.io/python-fastjsonschema/), and [reference validator package](https://pypi.org/project/jsonschema/4.26.0/).
