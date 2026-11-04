# Retained experience after ordinary repair

21 October 2026. Private exploratory study.

**The residual failure qualified, all six matched workers completed, and REL
with history had the highest transfer score in both origin blocks. These are
small exploratory advantages, with cost and regression tradeoffs—not a
completed migration or broad RSI proof.**

On 704 positions excluding exact supplied history inputs, artifact-only,
ordinary-history and REL-history scored **550 / 550 / 553** for origin one and
**533 / 520 / 535** for origin two. Thus adding history alone tied once and lost
thirteen positions once. Adding REL to the same history gained three and
fifteen positions. REL plus history exceeded artifact-only work by three and
two positions, but that combined contrast cannot isolate history from REL.

REL introduced five and zero regressions against its two inherited artifacts;
ordinary history introduced eleven and twenty; artifact-only work introduced
zero and fifteen. Some relative gains came from preserving existing behavior
rather than repairing more failures. The evidence supports reporting these
observed differences, not assigning certainty to a mechanism or population
effect from two origin blocks.

On the 81 inputs absent from the old profile, all origin-one arms scored 74;
origin two scored 57 / 65 / 65. The eight-position origin-two difference consists
of an existing composed-document behavior lost by artifact-only repair and
preserved by both history arms. Neither history arm repaired a new-input failure
in that origin. This is useful regression evidence, not a discovery of eight
new capabilities.

REL used **41.7% and 23.2% more recorded tokens** than artifact-only work, and
**20.0% and 16.7% more uncached input plus output**. Against equally informed
ordinary history it used fewer total tokens in both origins, but uncached cost
and elapsed time moved in opposite directions across origins. There is no
uniform efficiency win. No condition repaired the complete contract.


## Matched worker results

| Origin | Condition | Correct / 716 | Transfer / 704 | New inputs / 81 | Fixed | Regressions |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | Artifact only | 553 | 550 | 74 | 20 | 0 |
| 1 | Ordinary + history | 561 | 550 | 74 | 39 | 11 |
| 1 | REL + history | 563 | 553 | 74 | 35 | 5 |
| 2 | Artifact only | 535 | 533 | 57 | 20 | 15 |
| 2 | Ordinary + history | 529 | 520 | 65 | 19 | 20 |
| 2 | REL + history | 542 | 535 | 65 | 12 | 0 |

“Fixed” means a starting failure now passes; “regressions” means a starting pass now fails. Complete migration success was **0/6**. Higher scores are partial repairs, not complete task success. The excluded A1 attempt is not in this table.

## Question and qualified task

Does prior episode evidence help repair a real implementation after earlier
ordinary debugging left errors? Does REL add value beyond equally informed
ordinary work?

The preceding Requests study closed its measured gap with ordinary repair. This
study therefore returned to preserved unfinished Mistune migrations rather than
reducing ordinary resources or inventing a new failure. The two historical
ordinary-debugging artifacts were reproduced at 479/652 and 477/652 against
their original CommonMark 0.30 contract. Those historical subjects also loaded
REL; they are not historical no-skill controls.

The current contract targets CommonMark 0.31.2 exact example-style HTML while
preserving the supplied Mistune implementation and dependency boundary. This is
an explicit migration contract, not a claim that every mismatch is a current
upstream defect. Research used the [official specification](https://spec.commonmark.org/0.31.2/),
[version changes](https://spec.commonmark.org/0.31.2/changes.html),
[Mistune 2 documentation](https://mistune.lepture.com/en/v2/guide.html) and
[After the Fix](https://arxiv.org/html/2609.34603v2). The paper informed separation
of inherited code, episode evidence and later execution; this is not a
reproduction of its experiments.

The profile contains 652 official positions and 64 prospectively composed
documents: ordered pairs of eight closed blocks separated by an HTML comment.
Their expected outputs were fixed before candidate execution. An older
markdown-it-py 3.0.0 reference failed three changed normative positions; the
checksum-verified 4.2.0 reference passed all 716 with the declared blockquote
format adapter. No expected output was altered to make a candidate pass.
Replacing the library with that reference is excluded by the repair contract,
but is a simpler alternative a deployment should evaluate when replacement is
allowed.

The unchanged inherited implementations score 533/716 and 530/716 under the
current contract. The new comparison has two origin blocks, each with:

- **A, artifact only:** current requirements and inherited code; no REL or
  episode record.
- **H, ordinary plus history:** the same inputs plus the historical record.
- **R, REL plus history:** the same factual inputs as H, with the frozen REL skill.

All arms inherit earlier code improvements. A is therefore not a pure no-state
or from-scratch control. H−A estimates incremental episode evidence; R−H
estimates added REL under equal factual history. R−A combines both changes.

The 6,398-byte history contains actual earlier final notes and the first residual
failure from each earlier specification section, capped at twelve in source
order. It was selected and verified by the coordinator before current scoring.
This is a pooled, fallible record of two named earlier attempts, not autonomous
memory creation or an optimal retrieval policy. It excludes later sections once
the cap is reached. The task prompt does not explicitly map its inherited source
to one of those two historical attempt names; both H and R receive the same
pooled leads and must check their actual code. Current requirements and source
govern applicability. Conclusions apply to this record policy, not every form
of source-specific memory.

Twelve exact history inputs overlap the scored target. The pinned primary score
excludes these, leaving **704 positions**. A second stratum has **81 exact inputs
absent from the old profile**: seventeen official inputs and 64 compositions.
The remaining 635 inputs overlap the earlier profile. Novel input text does not
establish a novel mechanism or training independence.

## Execution, fairness and corrections

Fresh native sessions used gpt-6-luna/medium, identical tools and permissions,
60 tool actions and 900 seconds including startup, with separately bounded
final grading. Normative prose and three public diagnostics were identical.
No extra answer, lesson or reflection artifact was required. Conditions ran
serially, with order balanced across origins. Candidate Python ran only in the
qualified offline, nonroot Docker guest with a read-only root, scoped mounts,
resource limits and dropped privileges. No paid provider API or GPU was used.

Before inference, a skill packaging error was corrected: the native adapter
needed its registered JSON manifest, not the installed checksum file. The
corrected snapshot retained identical core bytes and all twenty registered
files. No guard was disabled.

The first A1 attempt then exposed a real study-host defect: copying a frozen
source propagated read-only attributes into the advertised editable workspace.
Its patch failed and its unchanged 533/716 score is **not an ordinary-repair
failure**. Its complete receipt and 251,054 tokens remain in campaign costs.
It is excluded from effect comparisons.

A prospective amendment created A1c and corrected only the remaining mutable
working copies. Actual broker patches and protected-input rejection checks
passed for all six corrected workspaces; source hashes were unchanged.
The corrected order was A1c, H1, R1, R2, H2, A2. No failed-model reroll or
cross-worker result sharing occurred.

Final scoring checks exact declared output, regressions against each inherited
origin and complete repair. Grouped grading reduces container overhead; groups
and individual positions are not independent trials. Missing execution or
unavailable grades remain distinct from wrong candidate outputs. Scored frozen
bytes and result identities are checked again during closure.

## Interpretation limits

There are two origin blocks, one source family and one model configuration.
The numerous query positions are dependent. Public specification examples and
related earlier evidence were exposed; this is an exploratory comparison, not
a protected or training-clean benchmark. The experiment does not establish
universal RSI, autonomous lesson acquisition, sustained compounding improvement
or broad harness portability. Higher aggregate accuracy cannot erase regressions,
and success on supplied history examples must not be called transfer.

All recorded model attempts, cached input, uncached input plus output, actions
and dispatch durations are reported. Cache and reasoning counts are included
subsets. The prior two origins cost 4,674,250 recorded tokens, including 204,490
uncached input plus output; these are shared sunk acquisition costs, not free
history and not six newly incurred costs. Complete coordinator tokens,
engineering time, currency and physical/remote energy remain unknown. Summed
dispatch intervals are not full campaign elapsed time. Tokens per complete
repair is undefined if no complete repair occurs.


## Cost and action accounting

| Attempt | Requests | Actions | Total tokens | Cached input (included) | Uncached input + output | Dispatch seconds |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A1 (excluded) | 10 | 18 | 251,054 | 203,904 | 47,150 | 142.504 |
| A1c | 33 | 51 | 1,041,539 | 928,000 | 113,539 | 299.916 |
| H1 | 45 | 59 | 2,205,250 | 2,120,960 | 84,290 | 322.311 |
| R1 | 44 | 55 | 1,475,642 | 1,339,392 | 136,250 | 363.834 |
| A2 | 44 | 51 | 1,552,901 | 1,475,456 | 77,445 | 418.483 |
| H2 | 49 | 60 | 1,928,409 | 1,811,456 | 116,953 | 421.571 |
| R2 | 50 | 60 | 1,912,832 | 1,822,464 | 90,368 | 390.797 |

The six eligible workers used **10,116,573 recorded tokens**, 618,845 uncached input plus output, 336 actions and 2216.911 summed dispatch seconds. Including the excluded infrastructure attempt, the seven-worker totals are **10,367,627 tokens**, 665,995 uncached input plus output, 354 actions and 2359.416 summed seconds. All worker usage identities reconciled. No feedback-model request was made.

Separately recorded source/reference acquisition took 1.829 summed seconds; qualification replays took 213.811 summed seconds. The post-comparison diagnostic took 31.931 seconds. Qualification jobs partly overlapped; worker comparisons did not. These timings do not cover all preparation, source reading or engineering. The A1 permissions fault, pre-inference manifest correction and failed/corrected tool calls remain preserved.

Observed tool-result failure counts (not all possible semantic errors): A1=1, A1c=2, H1=0, R1=2, A2=5, H2=6, R2=5. Successful exits can still print failed assertions or caught exceptions; exit status alone is not correctness. The evaluator checked the actual returned HTML. Token totals, cache and elapsed dispatch must be considered separately rather than converted to an unmeasured monetary or energy claim.

## Verified mechanism and task-local correction

H1 invoked the history file in actual Python tests and repaired the single-equals setext heading in the supplied record. Its regex edit changed a repeated single-character capture to a capture of the full sequence; the consumer still used `m.group(2) == '='`. Thus a multi-equals underline became a level-two heading. The same boundary error remained in R1. This is supported by saved source and exact pre/post outputs, not an interpretation of hidden model reasoning.

[Python's capture semantics](https://docs.python.org/3/library/re.html#re.Match.group) and the [current heading contract](https://spec.commonmark.org/0.31.2/#setext-headings) support a specific prediction. After the six workers, a separately pinned diagnostic changed only that consumer in a copy of H1 to `m.group(2).startswith('=')`. It scored **565/716**, repairing **4** H1 failures with **0** new regressions. Predicted examples 80 and 81 recovered and the supplied example 83 stayed correct. This verifies the narrow producer/consumer repair. It is coordinator-directed, uses exposed evidence, leaves other failures, and is excluded from worker comparisons.

R2's final internal check also contained two incorrect expected outputs despite the canonical history containing correct full outputs. Its entity fixture omitted the paragraph wrapper and rejected a correct result; its empty-fence fixture accepted an extra newline that the contract rejects. The independent final evaluator scored both correctly. This is a verified fixture-construction error, not a reason to change the gold labels. Reusing source-checked fixtures can avoid manual transcription errors, but that proposed practice was not a matched intervention here. The worker's nonzero last check remains recorded.

## REL decision and next discriminating question

**Keep the core skill unchanged; update its evidence and observed examples.**
The comparison has a limited positive result worth preserving alongside its
costs and remaining errors. It does not justify adding a new mandatory prompt
or claiming that retained history always helps.

The coordinator applied REL to recover failed earlier work, research the current
contract, qualify a real residual gap, separate information conditions, preserve
failed attempts, diagnose actual errors and verify a bounded correction. Its
own editable-copy preflight omission was an execution error: the existing host
integration reference already explicitly requires the actual authorized write
probe. The working-copy correction applied that rule without changing original
sources or protected inputs.

Worker failures also fall under existing checks: follow a changed representation
through its consumer; check an existing valid case as well as the target
failure; verify feedback criteria against the current contract. R1 still missed
the capture-consumer mismatch, and R2 manually reconstructed two fixtures
incorrectly. More wording is not established as the remedy. The package adds
the verified producer/consumer example, full bounded comparison and explicit
limits. Its twenty core instruction/reference/asset files remain byte-identical
to the evaluated version.

The task-local diagnostic is retained as a reproducible patch and graded
artifact; it is not merged into original worker outputs or promoted as a fully
working parser. The private package contains sanitized evidence, not private
chat transcripts or the complete research infrastructure.

**Next decision:** whether a concrete execution aid can prevent these observed
mistakes on a different qualified repair. A candidate should reuse
source-checked expected outputs and exercise a changed producer together with
its dependent consumer, then be compared with equally informed ordinary tests.
Review the earlier requirement-linked and executable-aid studies first so this
does not repeat an already-closed format comparison. Require an actual residual
failure and a changed mechanism before another model campaign. This is a
proposal, not an implemented or proven improvement, and no further campaign
was started during this study.
