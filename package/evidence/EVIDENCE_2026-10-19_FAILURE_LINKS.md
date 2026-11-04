# Linking past failures to current repair requirements

19 October 2026. Exploratory instruction comparison; private evidence summary.

## Finding

Ordinary repair completed 0/2 tasks; the linking cue completed 0/2. The primary endpoint does not show a reliability advantage. Every attempt, including the unsuccessful feasibility work, is retained.
The question was whether an explicit linking cue helps beyond strong ordinary
repair with the same information. It was not REL versus no REL: both arms loaded
the same skill, and both received the same six failures and current requirements.
These were coordinator-observed baseline failures, not autonomous learner memory.

## Research, source choice and amendments

The [PyPA changelog](https://packaging.pypa.io/en/stable/changelog/) and
[specifier API](https://packaging.pypa.io/en/stable/specifiers.html) motivated
version-migration tasks. The public [After the Fix paper](https://arxiv.org/html/2609.34603v1)
informed the distinction between retained correction, appropriate reuse and added
benefit over a fresh worker. This study is not a reproduction or a novelty claim.

The initial packaging profiles closed at ordinary-repair ceilings: 292/292 and
246/246 selected upstream vectors. An intervening ordinary attempt remained at
175/246. It encountered an undisclosed patch-size bound and later made edits
without checking their behavior. The common interface was clarified, and the
corrected ordinary worker passed 246/246. This does not isolate the clarification's
causal effect. No linking arm ran on those saturated profiles.

One prospective source pivot used the real Mistune 2.0.5 library and all 652
[CommonMark 0.30 examples](https://spec.commonmark.org/0.30/), grouped into 82
requests. Original Mistune passed 445/652 exact query positions and 16/82 complete
requests. These are compatibility differences against a pinned migration contract,
not newly discovered upstream bugs. The task covers interacting block, list,
delimiter, reference, escape and renderer behavior; it is not a new toy parser.

An independently implemented markdown-it-py reference passed all 652 after a
general blockquote newline adapter aligned it with the declared example-output
convention. Its two earlier formatting disagreements/correction attempts remain
recorded. Expected outputs were not changed. A separately pinned HTML token
profile distinguishes some representation differences; it is not full DOM or
CommonMark semantic equivalence.

The Markdown ordinary screen used all 60 actions without final submission. Its
original status remains failed. A prospective admission amendment allowed a
separate frozen-code replay to establish actual remaining errors, before any
comparison worker started. That replay passed 357/652 exact query positions;
21 requests raised candidate exceptions. Inspection confirmed an unrecognized
setext heading and a newly broken uppercase hexadecimal character reference.
The latter was correct in the starting library. The diagnostic did not become
an in-budget result or a completed screen. This outcome-informed amendment limits
confirmatory interpretation and is preserved with the original design.

## Fair contrast

Each comparison used a fresh native context with gpt-6-luna/medium, current REL,
the same initial source, factual history, tools and permissions, and 60 actions /
900 seconds including model-host startup. Grading had a separate bounded allowance.
Two repetitions per arm ran in fixed order O,L then L,O, at most two simultaneously.
No scored output or repaired source was handed from one worker to another.
The existing offline Docker guest used a read-only root, nonroot user, disabled
network, dropped capabilities, one CPU, 512 MB memory and a PID bound. The
Windows controller reconciled owned descendant cleanup. These are scoped host
controls, not a claim of complete adversarial isolation. No GPU or direct paid
provider API was used.

- O requested ordinary debugging, testing, positive/negative/regression checks and
  completion of every required repair.
- L additionally framed work as connecting relevant past failures to current
  requirements, rejecting obsolete assumptions and using those links for repairs
  and executable checks. It required no mapping essay or reflection call.

Both received the versioned normative prose with paired example blocks omitted.
The public evaluation data was visible to the coordinator; pretrained familiarity
is unknown. This is not a sealed, training-unseen benchmark. The comparison is an
incremental instruction effect; tool actions alone cannot reveal private reasoning
or prove the worker mentally made the requested link.

## Original comparison results

| Attempt | Exact query positions | Complete requests | Listed failures repaired | Baseline-pass positions lost | Tool actions | Recorded tokens |
| --- | --- | --- | --- | --- | --- | --- |
| M-L-R1 | 472/652 | 16/82 | 6/6 | 8 | 60 | 1,657,914 |
| M-L-R2 | 480/652 | 20/82 | 6/6 | 3 | 60 | 2,835,157 |
| M-O-R1 | 479/652 | 21/82 | 6/6 | 11 | 60 | 2,704,901 |
| M-O-R2 | 477/652 | 19/82 | 6/6 | 3 | 54 | 1,969,349 |

Repetition 1: the linked cue changed exact correct query positions by -7 versus ordinary repair. Repetition 2: the linked cue changed exact correct query positions by +3 versus ordinary repair. These are descriptive differences on one shared source profile.
They do not establish a population effect, sustained learning or cost-effectiveness.
The separate HTML token-profile scores were 485 and 483 for ordinary repair, and
478 and 484 for linking. The primary exact-output verdicts were not replaced.

All four comparison workers repaired the six supplied failures and improved
exact scores from the original 445/652. The broader repairs still introduced
regressions. Ordinary repair averaged 478/652 correct positions; the cue averaged
476/652. Those are averages of two attempts on the same cases, not independent
task samples. Remaining failures therefore cannot be explained merely by refusing
to use the supplied history.

The public tool-action audit confirms that every comparison worker read current
requirements and history, edited saved parser code and executed behavior checks.
Ordinary workers made 17 and 14 Python calls; linked workers made 8 and 17. Some
calls inspected sources or printed outputs rather than asserting correctness.
Three workers executed a behavior check after their final edit; the first linked
worker made further edits after its last Python check. This is an observed
verification gap, not proof that it caused the score difference. The later linked
worker verified known examples, NUL handling and per-query state isolation, yet
still missed other cases. A successful selected check is not complete coverage.

Examples in the first pair illustrate distinct boundary failures: an ordinary
repair merged paragraph text across a blank line into a setext heading; a linked
repair double-escaped an entity in a link title. Both were correct in the original
library. These source-corroborated regressions support checking changed behavior
and preserved boundaries, without establishing that another generic reminder
would make workers perform those checks correctly.

Incomplete attempts remain failures for complete task success. Their official
query results stay ungraded, rather than becoming zero or borrowing a later replay.
Grouped candidate exceptions fail the request and its returned-output contract;
they do not prove each constituent input would independently raise. Query positions,
requests and entire repair attempts are dependent units, not interchangeable samples.
No query-level significance test or universal RSI effect is claimed.

Separate diagnostic replays:

- M-O-feas: 357/652 exact query positions and 16/82 requests in a separate replay; the original attempt remains unsubmitted.

## Cost and scope

Across all eight model attempts, recorded usage is at least 16,337,384
tokens, including 15,519,360 cached input tokens.
Uncached input plus output is at least 818,024.
The study recorded 431 tool actions and 4179.38
summed dispatch seconds. Cached input is already part of input; reasoning output
is already part of output. Do not add those subsets again or equate token counts
with money. Interrupted usage is a validated observed bound, not a final receipt.

| Arm, comparison only | Complete repairs | Recorded tokens | Uncached input + output | Actions | Summed dispatch seconds |
| --- | --- | --- | --- | --- | --- |
| Ordinary | 0/2 | 4,674,250 | 204,490 | 114 | 1281.37 |
| Linking cue | 0/2 | 4,493,071 | 201,999 | 120 | 1071.41 |

The cue used 3.9% fewer aggregate recorded tokens and 1.2% less uncached input plus
output across these two comparison attempts. The direction reversed by repetition:
the first linked attempt was cheaper and the second was more expensive. More
actions and mixed correctness prevent interpreting this as a demonstrated general
efficiency gain. No post-feedback reflection calls were added to either arm.

Qualification used 10 recorded attempts and
2052.28 summed seconds; separate diagnostic
replays used 110.84 seconds. These are outside model
dispatch. Nested guest times are not added to enclosing dispatch, and parallel
durations are not elapsed study time. Recorded acquisition used 17
requests and 11.25 summed seconds, with the failed
acquisition duration unknown. Parent/coordinator tokens, complete engineering time, billed
currency cost and local/remote energy are unknown. No fully inclusive economic
or energy-efficiency claim follows. Tokens per complete repair are undefined
where the denominator is zero; incomplete usage prevents an exact all-cost ratio.

Package delivery verification additionally recorded 145.14 seconds across the
initial temporary-directory-denied run and corrected offline run. The corrected
run reconciled 108 test identities: 107 passed and one live Docker opt-in test
was skipped. These software checks do not establish a model-performance gain.

## What changes in REL

No new mandatory linking procedure is promoted. The common patch contract was
corrected locally; existing host guidance already requires exposing actual
operation-specific limits. Existing REL guidance also requires actual method use,
changed-behavior checks, preserving failures and reserving completion budget.
Duplicating those instructions would not establish that they are followed.
The frozen and installed main skill remains unchanged; this release updates the
evidence and reconciles earlier verified supporting-file corrections.

The next justified mechanism question is whether a concrete, bounded executable
check chosen from a requirement prevents an observed regression while leaving
enough budget to finish. It would need a newly pinned intervention and fresh
source task, not extra repetitions selected to improve this result. The present
study does not establish sustained learning, autonomous acquisition, broad host
portability, a better architecture, or a new algorithm.

## Reproduction boundary

The companion [de-identified ledger](EVIDENCE_2026-10-19_FAILURE_LINKS.json) records
original results, diagnostics, costs and source/skill digests. Raw native traces,
account/session identities, local paths, downloaded source/test datasets and the
full research harness remain outside this repository. This is reviewable evidence,
not a stand-alone reproducible model benchmark. Package checks and generic examples
remain runnable through the [non-public source: delivery guide](https://github.com/sulabhdubey/recursive-evidence-loop/blob/507357e1d7a55335f9205134ad1c32ac4657b0bc/docs/DELIVERY.md).

Source documentation: [Mistune 2 guide](https://mistune.lepture.com/en/v2/guide.html),
[markdown-it-py usage](https://markdown-it-py.readthedocs.io/en/latest/using.html),
[version specifiers](https://packaging.python.org/en/latest/specifications/version-specifiers/).
CommonMark material is attributed to John MacFarlane under CC BY-SA 4.0; the full
downloaded specification is not redistributed in this evidence package.
