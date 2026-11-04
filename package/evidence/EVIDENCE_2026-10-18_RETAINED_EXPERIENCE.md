# Retained executable experience — 18 October 2026

The comparison completed 26 native attempts: two independent acquisition attempts
and 24 later sessions, arranged as eight matched A/B/C blocks. A used ordinary
work without history, B ordinary work with complete origin history, and C the
frozen REL skill with byte-identical history to B. No outcome was discarded or
retried. All used gpt-6-luna, medium effort, equal current rules, tools and budgets,
and the existing offline Docker guest.

| Approach | Correct later tasks | Later-task tokens | Tokens including acquisition | Inclusive tokens / correct task | Inclusive uncached input + output |
|---|---:|---:|---:|---:|---:|
| A: ordinary, no history | 7/8 | 1,270,553 | 1,270,553 | 181,508 | 168,473 |
| B: ordinary, same history | 8/8 | 1,117,621 | 1,475,038 | 184,380 | 304,094 |
| C: REL, same history | 8/8 | 1,116,301 | 1,473,718 | 184,215 | 243,894 |

C and B were effectively tied on total tokens: C used 0.1% fewer inclusive tokens,
with lower later-task totals in four of eight blocks. C used 19.8% fewer inclusive
uncached-input-plus-output tokens; that later-task measure was lower in six of
eight blocks. Cache behavior matters, and neither token measure is a dollar,
compute or energy measurement. These small clustered descriptive comparisons do
not establish statistical superiority or general effectiveness.

History-bearing methods used about 12% fewer later-task tokens than A, but their
acquisition-inclusive totals were about 16% higher. On tokens per fully correct
later task, C was 1.5% higher than A; on uncached input plus output per correct
task, C was 26.7% higher. This preserves both the observed correctness difference
and the costs instead of treating either as the complete result.

## Task, information and cost boundaries

Workers built recursive standard-library JSON Schema validators on the official
[JSON-Schema-Test-Suite](https://github.com/json-schema-org/JSON-Schema-Test-Suite),
commit `55719286c33ae0d1823bfb65fea10338a19bc37c`. The profile covers declared
composition, equality, type, numeric, array and object rules; it excludes remote
references, regular expressions, optional formats and other undeclared features.
It is not a complete production validator.

The origin packet has 294 scored vectors, same-dialect transfer 282 and the
newer-dialect packet 58. All 681 public and private retained source answers agreed
with an independently implemented installed validator. Whole schema groups were
separated, and repeated schema-instance decisions were excluded across roles.
Metadata-only differences did not qualify as fresh inputs. These are nested
checks in one public source family, not thousands of independent model trials or
proof of absence from pretraining.

Both origin agents used REL and authored their own code and lessons. They passed
their origin tasks; their lessons described evidence scope rather than a new
technical correction. Histories included code, prose, public inputs and actual
feedback without quality filtering. They were frozen at the origin. Both dialects
were fully described from the start and already implemented by both origins.
Consequently this is retained-method transfer, not learning unknown dialect rules,
an isolated prose-memory effect, a randomized acquisition comparison or sustained
procedure evolution.

Actual worker usage was 3,861,892 tokens, including 3,204,864 cached input tokens;
uncached input plus output was 657,028. Origin acquisition cost 357,417 tokens,
including 145,482 feedback tokens. Each origin is charged once in the actual
campaign and once to each separately reported counterfactual history policy.
Counterfactual arm totals must not be summed into actual campaign cost. All 26
usage records reconciled independently, with no unknown worker usage. Research
orchestration, review labour, currency and physical energy remain incomplete.
The campaign spanned 1,840.54 seconds including intervening analysis; summed worker
dispatch time was 3,096.03 seconds. Two workers could overlap.

## Failure, actual reuse and follow-up loops

One A validator omitted the string-type handler and failed 12 private checks,
despite passing 19 supplied examples and 11 self-authored probes. Its independent
repeat passed. A separately preserved investigator repair added only that handler
and passed all 634 scored vectors across the three packets. The original failed
attempt remains failed; this is not retroactive learner improvement.

Source and action review confirmed exact code reuse in one B submission and
adaptation followed by execution in other submissions. Consultation alone is not
counted as method execution, and code-plus-prose history does not isolate the
effect of written lessons.

Four post-comparison direct replays of the unchanged origin executables passed
all 680 transfer checks in 21.66 summed seconds, with zero new model calls. No REL
or prose lessons were supplied to those replays. Acquisition and checking still
cost resources. This establishes sufficiency of saved code on the exposed tasks,
not a prospectively randomized fourth arm or a general applicability mechanism.

A distinct, historical event-processing diagnostic passed 20 algorithm checks
under each of two task contracts. The compatible contract completed successfully;
the changed-output contract correctly failed because the old companion artifact
did not satisfy the new requirement. Correct computation alone did not establish
complete task success. These exposed historical tasks establish operation and a
useful rejection, not fresh confirmation or broad portability.

## Skill decision and evidence scope

The optional study-design reference now names direct use of an existing executable
as a conditional simple comparator. It requires authorization, proportionate
effort, complete current-contract checking and acquisition-inclusive cost; it
does not impose another benchmark on ordinary work. Existing guidance already
covered simple baselines and applicability. This is a scoped clarification of a
missed comparison, not evidence that the previous skill lacked those principles
or that the new wording improves performance. The core entry point and generic
host software are unchanged.

The evaluated core entry-point SHA-256 was
`17e4c092a9323099194d05664b0ffff3afd8ff3f2758daa24a5f07344ea0991e`.
The prior package commit was `7ce1dfea69d74c95e44c9772b1fc700e8054692f`.
The run-local skill snapshot remained frozen throughout. Raw private traces,
source fixtures and account records are not packaged here. These findings do not
establish universal RSI, a novel algorithm, an improved brain-inspired
architecture, long-term learning, or superiority to complete public frameworks.
