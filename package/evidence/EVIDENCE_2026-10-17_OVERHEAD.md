# Token overhead: two rejected candidates — 17 October 2026

The baseline package is commit `368b6d99b78a4dc6b506927a47847ffb7ec7870f`.
Its main skill SHA-256 is
`17e4c092a9323099194d05664b0ffff3afd8ff3f2758daa24a5f07344ea0991e`.
The main skill and runtime software remain unchanged by this update. Only the
optional evolution reference and delivery evidence are clarified. No reduction
in worker cost has been established for that clarification.

## Reconciled prior excess

The previous ten-task REL trajectories used 3,498,468 reported tokens versus
2,728,437 for matched ordinary work, both fully correct on the declared checks:
28.2% more. REL made 124 model requests versus 114, despite fewer tool actions
(249 versus 259), and read fewer overlapping same-snapshot bytes. The exact
770,031-token difference decomposes into 278,788 from larger first inputs at
REL request counts, 99,395 from request-count differences at ordinary first
inputs, 392,400 later context growth, and -552 output. This is an accounting
identity with a chosen order, not identification of four causal effects.

## Fresh prospective comparisons

All trials used matched GPT-6-luna/medium, current task information, tools and
limits: 60 actions and 900 seconds. Generated code ran in the offline Docker
guest. Event reconciliation covered watermarks, duplicates, revisions and
finality; dependency planning required exact reachability and global optimum
under conflicts and changing policies. Twelve complete integration workloads
and eight boundaries were graded per task. No separate paid API or GPU run.

| First comparison | Correct tasks / cases | Total worker tokens | Uncached input + output |
| --- | --- | ---: | ---: |
| Full REL | 8/8; 160/160 | 1,854,216 | 233,608 |
| Compact main file | 8/8; 160/160 | 1,964,002 | 279,010 |
| Ordinary work | 8/8; 160/160 | 1,459,748 | 293,412 |

Four two-episode sequences. Each policy could retain its own complete code and
raw feedback. Both policy versions were initially supplied; later activation
was not discovery of an unseen rule. The compact entrypoint cut initial input
by 922 tokens but used 5.9% more total tokens and more model requests. Savings
occurred in only one of four sequences. Candidate rejected.

| Second comparison | Correct tasks / cases | Total worker tokens | Uncached input + output |
| --- | --- | ---: | ---: |
| Full REL | 4/4; 80/80 | 1,056,015 | 161,423 |
| Full REL plus concise-evidence paragraph | 4/4; 80/80 | 996,952 | 141,656 |
| Ordinary work | 4/4; 80/80 | 720,555 | 97,067 |

Four fresh cold-start tasks; no history. The paragraph reduced total tokens
5.6%, below the pinned 10% minimum. It saved tokens on three tasks but used
97.7% more on the fourth. Uncached input plus output fell 12.2%; summed dispatch
time rose 3.4%. Ordinary work remained cheaper in every task. Candidate rejected.
All arms parsed full examples; candidate and full-REL serialized tool-result
bytes were nearly equal. A consistent causal mechanism was not established.

## Scope and disposition

All 36 attempts and errors were retained: 36 correct tasks, 720/720 cases,
8,051,488 reported worker tokens. Cases within tasks are correlated. Four
sequences or four cold-start tasks cannot establish universal effectiveness or
precise population effects. Cache hits are included; parent research/build/
review, currency, human time and physical/remote energy remain unmetered.
The parent authored the tasks and oracle; this is not an independently sealed
external benchmark or production deployment test.

Every submitted artifact and guest receipt reconciled. Self-authored erroneous
test expectations and one all-idle-source implementation error were repaired
within the original attempts. No critical authority/evidence violation was
observed in the bounded review. Preparation permission and analyzer-typo
failures are preserved; no model trial was erased or rerun to improve scores.
The common event contract was clarified before the second loop for all arms;
cross-loop absolute costs are not a causal treatment comparison.

Neither behavioral candidate was installed. The optional
[non-public source: skill-evolution reference](https://github.com/sulabhdubey/recursive-evidence-loop/blob/507357e1d7a55335f9205134ad1c32ac4657b0bc/references/skill-evolution.md) now distinguishes
trace-based cost diagnosis from assumptions about prompt length or read count.
This is a measurement clarification, not a demonstrated improvement from its
wording. Broader learning, semantic reliability and portability remain open.

Research rationale came from [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents),
[tool design](https://www.anthropic.com/engineering/writing-tools-for-agents),
[skill consumption](https://www.microsoft.com/en-us/research/publication/from-raw-experience-to-skill-consumption-a-systematic-study-of-model-generated-agent-skills/),
[Beam](https://beam.apache.org/documentation/basics/) and
[pip](https://pip.pypa.io/en/stable/topics/dependency-resolution/).
These sources motivate hypotheses, not the reported results. The complete
local study traces remain separate from this portable generic package.
