# Failed-tool recovery: six completed repairs, no demonstrated advantage from the extra procedure

20 October 2026 · Exploratory, version-bound study

All six workers completed their scored repairs with zero scored regressions.
The explicit recovery cue did not improve correctness over ordinary tool
documentation. Costs were mixed. After correcting an ambiguous dotenv contract,
the ordinary worker used fewer tokens and made fewer rejected edits.
Eight conditional repetitions were cancelled under the pinned ceiling rule.

## Question and fair comparison

The preceding study exposed a specific failure: a worker understood a repair but
repeatedly sent over-escaped patch arguments. This study asks whether an explicit
recovery procedure improves the next actual saved repair beyond clear ordinary
documentation. It does not test REL against no REL.

Both conditions received the same current REL snapshot, gpt-6-luna/medium model,
starting executable, public diagnostics, ordinary tool documentation, exact failed
operation and error, protected inputs, offline execution tool, permissions and
60-action/900-second allowance. Each worker had a fresh native session. At most
two ran concurrently. The cue additionally instructed the worker to inspect the
failure and effects, read current decoded source and digest, change the failed
assumption before retrying, preserve guards and check saved behavior.

The failed edit was replayed through the actual broker before dispatch and
verified not to change source bytes. It was a deliberately supplied checkpoint,
not a spontaneously acquired learner experience. Its proposed replacement
already contained a correct edit. Both conditions also received the same defect
description. This is a recovery-and-completion comparison, not independent bug
discovery or long-term learning.

## Sources and task admission

Two public code families were pinned and retained with their notices:

- [python-dotenv source and tests](https://github.com/theskumar/python-dotenv/tree/0b2880591780a426b0551436f47a17e7a76d954f):
  55 distinct literal parser cases after one verified duplicate was removed.
  The unchanged reference passed 55/55; controlled quoting and CRLF-counting
  defects reduced the starting program to 52/55.
- [JSON Patch tests](https://github.com/json-patch/json-patch-tests/tree/2a928f9044aad35c74e2788d498bcf2c6b91adea),
  [python-json-patch](https://github.com/stefankoegl/python-json-patch/tree/c39058eabd7e50e92e6a6fd7e915c0218c7284f3)
  and [python-json-pointer](https://github.com/stefankoegl/python-json-pointer/tree/fb771073c8b1b05f0e1d82a8c0608968a65b0a90):
  108 distinct eligible cases after disabled, no-verdict and duplicate cases were
  recorded separately. The reference passed 108/108; controlled array insertion
  and pointer-decoding defects reduced the starting program to 103/108.

The JSON Patch profile exercises the six operations, root and array behavior,
escaping and rejection cases. The dotenv profile checks decoded values, original
spans, line positions, comments, Unicode and invalid-line recovery. Public
diagnostics contained five cases per task. Other cases were unavailable through
the worker's supplied inputs. This is scoped tool-host separation; the coordinator
could read the gold data, and public-source pretraining exposure is unknown.

## A real setup defect was found and corrected

Before model calls, a current-broker check found two incorrect draft API fields:
write uses `text`, and list accepts no `path`. Both were corrected equally;
the original drafts and correction receipts remain preserved.

After the first two attempts, artifact review found an unrelated input description
in the shared dotenv contract. Both original dotenv workers ultimately added a
text-patching branch that the intended parser task did not need. Their parser
scores remain valid for the scored profile, but those scores do not establish
minimal scope or successful implementation of the unrelated branch. The ambiguous
contract limits interpretation of their costs. It is not evidence that REL caused
the behavior, nor proof of its sole cause.

A separate follow-up plan was pinned before its two fresh workers. It clarified
dotenv-only inputs equally for both conditions and added twenty new complete
configuration documents, composed from upstream literal examples. Expected spans
and line offsets were derived from those literals, then checked against the
unchanged reference in the offline guest. Two new documents were public and
eighteen unshown. The 55 original cases stayed as regression checks: 75 total.
The reference passed 75/75 and the damaged program 52/75 before model dispatch.
These are fresh compositions within the same source family, not a third
independent family.

Both follow-up workers passed 75/75, including all eighteen unshown new documents.
Neither changed the wrapper or added the irrelevant text-patching feature.
The original four-attempt results remain intact. Comparing original and clarified
costs does not isolate the contract change: cases, context and independent model
realizations also differ.

## Recorded results

| Task / condition | Correct | Initially failing cases repaired | Regressions | Tool calls | New rejected edits | Total native tokens | Uncached input + output | Wall seconds |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Original dotenv / ordinary | 55/55 | 3 | 0 | 26 | 1 | 397,288 | 60,008 | 236.9 |
| Original dotenv / recovery cue | 55/55 | 3 | 0 | 22 | 1 | 329,569 | 51,297 | 177.3 |
| JSON Patch / ordinary | 108/108 | 5 | 0 | 19 | 0 | 323,154 | 39,506 | 235.4 |
| JSON Patch / recovery cue | 108/108 | 5 | 0 | 21 | 0 | 349,883 | 67,643 | 239.9 |
| Clarified dotenv / ordinary | 75/75 | 23 | 0 | 14 | 0 | 159,282 | 18,738 | 164.0 |
| Clarified dotenv / recovery cue | 75/75 | 23 | 0 | 18 | 1 | 271,411 | 23,603 | 196.8 |


Every worker fixed all of its initially failing scored cases. There were no
repeated identical rejected operations within a worker, using argument identity
with the source digest excluded. Newly rejected edits all reported that the patch
context did not match exactly once. The original dotenv pair had one each; the
clarified recovery worker had one; the other three had none. These counts exclude
the supplied seeded failure, which was present equally in each pair.

On native total tokens, the cue changed cost by -17.0%
for original dotenv, +8.3% for JSON Patch,
and +70.4% for clarified dotenv.
The clarified pair also used +26.0%
more uncached input plus output with the cue. These are three descriptive paired
observations, not statistically established effects. Cases within one program are
not independent learner replications.

## Cost coverage

All six native attempts have complete recorded usage, including failed tool
operations, worker checks and finalization: **1,830,587 total tokens**,
comprising 1,809,204 input and 21,383 output.
Of the input, 1,569,792 tokens were reported cached.
Uncached input plus output was **260,795**.
Reasoning-token metadata is a subset of output and is not added again.

The six launch-to-terminal worker intervals sum to 1250.3 seconds
(20.8 worker-minutes), including startup and host completion.
Concurrent execution means that sum is not elapsed study duration.
Six zero-model reference/damaged qualification runs took 100.7 recorded
seconds in total, separately from those worker intervals. All 120 worker tool
actions are counted, including the three rejected edits.

For these completed scored tasks, total native tokens per scored task success
equal each row's native-token value. That metric does not turn the hundreds of
case-level checks into hundreds of independent successes.

Coordinator reasoning, complete orchestration and source-acquisition costs,
human effort, money, whole-laptop energy and remote inference energy are not fully
measured. This is complete native-worker accounting, not complete project
cost-effectiveness. No direct paid provider API was invoked.

## Research basis

[RAG-Repair](https://arxiv.org/html/2510.17874v1) motivated separating an accepted
tool operation from actual task completion and expecting model-dependent effects.
[Schema First Tool APIs](https://arxiv.org/html/2603.13404v1) reports reduced
interface misuse in its constrained pilot without successful task completion;
that distinction shaped the two separate endpoints here.
[Anthropic's tool-design guidance](https://www.anthropic.com/engineering/writing-tools-for-agents)
motivated a clearly documented ordinary baseline and measurement of errors,
tokens and runtime. Task semantics were checked against
[RFC 6901](https://www.rfc-editor.org/rfc/rfc6901.html) and
[RFC 6902](https://www.rfc-editor.org/rfc/rfc6902.html).
Their findings informed the design; they are not measurements of REL.

## Skill decision and next discriminating question

Do not promote the longer recovery procedure to a mandatory rule. Ordinary
documentation was sufficient on every scored task, and the cue was more costly in
two of three pairs. Retain the existing optional guidance about current decoded
arguments, complete views, exact source identity and actual affected outputs.
The contract defect was in the study builder, not a demonstrated missing rule in
the generic skill. Existing instructions already require checking actual task
contracts and preserving qualified failures.

This cycle updates the skill package's evidence, latest-result pointers and scoped
compatibility record. **The installed core instructions and executable helpers
remain unchanged.** No gain from new instruction wording is claimed.

The useful next prerequisite is an observed residual recovery failure under an
already clear, current interface—for example a real interrupted operation with
uncertain effects, where retry and reconciliation are materially different.
Only then would a bounded matched comparison of a small executable recovery aid
versus ordinary recovery be justified. Creating more examples of an already
solved literal edit would not answer that question. No such next study was run here.

## Verification and limits

Six unique native sessions completed, all usage receipts reconciled, and worker
descendant cleanup was verified. Source/input bindings, literal case mappings,
public/unshown membership and type-sensitive scorer positive/negative controls
passed. Saved-code diffs were inspected separately from passing scores.
Original candidate bytes, rejected operations, drafts, admissions and follow-up
artifacts remain in the private evidence package.

These checks establish these repairs under this host. They do not establish a
new algorithm, universal RSI, autonomous capability acquisition, broad portability,
hostile whole-agent isolation, long-term benefit or performance superiority.
Both arms used REL; no conclusion about REL versus a skill-free agent follows.

## Evidence identities

The raw study traces and research harness remain private local artifacts. The generic package includes the sanitized [non-public source: result ledger](https://github.com/sulabhdubey/recursive-evidence-loop/blob/507357e1d7a55335f9205134ad1c32ac4657b0bc/docs/evidence/2026-10-20-tool-recovery.json), not a fully reproducible model benchmark.

- `PLAN.md`: `5b69e3ddbf8c1c8bf692636ad93e4da80045e736898634955fba09095a0360a5`.
- `CONTRACT_FOLLOWUP_PLAN.md`: `b200ef125a38ee032a002fd9173eb7e169070dc108b96b3109fb950ac560f694`.
- `ADMISSION.json`: `e5bba76a35d75d0854dd77c7f3e6c646a508b9554021ad301c25c944486bab3d`.
- `CONTRACT_FOLLOWUP_PIN.json`: `de8abdd5c0015aa5ae987f787040198f103811a86d84edb32148c871509ae1b9`.
- `ANALYSIS.current.json`: `374357d923b4d6a860f62a7b6b35341c693f4b10b4d4903ca3d626611823b35b`.
- `FINAL_VERIFICATION.json`: `0563a6f09f600626fec4a2c763f28151937f2c423c154a3b11c13e96e50dd141`.
- `ARTIFACT_AUDIT.current.json`: `20f261fc7f80f1302fcf64bb115fbd8caefd3dcdba7cd9f6995b0a83d4bd37e5`.
