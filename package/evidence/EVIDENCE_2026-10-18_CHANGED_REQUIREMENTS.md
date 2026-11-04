# Adapting retained methods to changed requirements — 18 October 2026

The study completed 24 native adaptations and 24 unchanged-code later replays.
Two historical implementations, two new profiles and two repetitions form eight
matched triplets. A used ordinary work without prior-origin history, B ordinary
work with complete history, and C frozen REL with byte-identical history to B.
All arms could retain their own adaptation output for the later replay. No
attempt was replaced, and no separate model reflection phase was added.

| Approach | Correct E2 / E3 pairs | New worker tokens | Acquisition-inclusive tokens | Inclusive tokens / correct pair | Inclusive uncached input + output |
|---|---:|---:|---:|---:|---:|
| A: ordinary, no prior history | 8/8 | 1,235,968 | 1,235,968 | 154,496 | 217,088 |
| B: ordinary, same history | 8/8 | 1,885,910 | 2,243,327 | 280,416 | 378,495 |
| C: REL, same history | 8/8 | 1,704,047 | 2,061,464 | 257,683 | 342,296 |

These are outcomes on the declared scored packets, not complete specification
certification. REL used 9.6% fewer new total tokens than same-history ordinary
work, but 37.9% more than no-prior-history ordinary work. Charging historical
acquisition changes these contrasts to 8.1% fewer and 66.8% more respectively.
No-prior-history ordinary work was cheapest in aggregate at equal observed
scored correctness.

The C/B result is composition-sensitive: REL used 35.5% fewer new total tokens
for local-reference tasks but 28.3% more for evaluated-location tasks. It used
fewer tokens in five of eight matched blocks. A retrospective leave-one-block
check reverses the aggregate ranking to 9.3% more when the largest ordinary-arm
attempt's entire matched block is omitted. That attempt remains in the primary
result. This is sensitivity analysis of the same data, not an independent test
or grounds for discarding an inconvenient observation.

## New behavior and controlled evidence

The official JSON Schema Test Suite remains pinned to commit
`55719286c33ae0d1823bfb65fea10338a19bc37c`. Profile R adds bounded same-document
references and dialect-dependent sibling semantics. Profile U adds evaluated
property/item propagation, dependent schemas and unevaluated constraints, with
no references. Every worker received the complete current specification.
Both original executables lacked these implementation capabilities; replay
confirmed failures on each new packet while all selected old-rule regressions
passed. That is a code capability gap, not proof of a model knowledge gap.

Fresh scored vectors numbered 30/18 for R adaptation/later transfer and 61/74
for U. The four packets also contain 88 repeated known-regression checks and
13 supplied examples. All 284 answers agreed with an independent validator.
Whole schema lineages separate examples, adaptation and later transfer. One
reordered-applicator near-twin was corrected before learner execution, with
the unused build preserved. These checks are nested in one source family;
they are not independent model trials or proof of no pretraining exposure.

All workers used gpt-6-luna at medium effort, equal tools and 60-action/
900-second limits. The existing offline Docker execution boundary was checked.
Source, task, history, frozen output, strict-Boolean results and request-token
records were independently reconciled. The gold remained researcher-readable;
the complete evaluator was not adversarially sealed.

## Costs and interpretation

Actual new worker usage was 4,825,925 tokens, including 4,006,912 cached-input
tokens. Uncached input plus output was 819,013. Historical acquisition of
357,417 tokens, including 145,482 feedback tokens, was already incurred. Each
retained policy is separately charged that amount for lifecycle comparison;
it is not new spending and the counterfactual totals must not be added together.
Direct replays used no model calls but did consume execution resources.
Parent/reviewer work, dollars and physical energy remain unmeasured.

Adapted methods ran successfully on the sampled later source groups. Both
ordinary and REL workers repaired their own development errors. Consultation,
source overlap and successful execution do not establish that a saved lesson
caused success, and an exact helper match also occurred in a no-history worker.
The study does not demonstrate a general REL accuracy advantage, reliable cost
advantage, sustained self-improvement or a new algorithm.

## Post-outcome defect and separate repair

Source review subsequently identified a child/parent annotation-scope leak in
one REL-produced implementation. Eight targeted diagnostic cases were authored
after inspection and independently checked. Eleven of the twelve frozen U
methods passed all eight; O1-U-P1-C falsely accepted the two nested-scope
counterexamples. This refutes complete-profile correctness despite unchanged
perfect scores on the original packets. Targeted post-outcome cases do not
establish unbiased arm error rates or a causal effect of REL.

A separate two-line investigator repair passed all eight diagnostics and all
76/89 original adaptation/transfer checks. Fifteen isolated guest executions
used no model calls. Original methods, scores and costs remain preserved; the
repair is not learner acquisition or independent confirmation. The generic
skill already requires checking the actual changed behavior and relevant
failure cases, so this does not justify adding another mandatory rule.

## Shared-skill update

The optional study-design reference now distinguishes lossless input identity
from conservative task-family grouping and links to existing equivalence-key
checks. Original inputs and labels remain intact; order, literal content,
multiplicity and references can make superficially similar cases different.
Five source-free procedural checks and the observed preflight correction
support the clarification. The underlying guidance already existed, so the
original omission was substantially an execution failure.

This is a scoped routing clarification, not a new default form, normalizer,
mandatory reflection phase or demonstrated improvement from new wording.
The main skill, generic host executables and all frozen study snapshots remain
unchanged. The predecessor package commit is
`63a91bf7892f6b6fce8775d2f1a6f809ed8c4cd4`.
