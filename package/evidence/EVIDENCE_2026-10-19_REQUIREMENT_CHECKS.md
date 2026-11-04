# Requirement-linked checks — 19 October 2026

Ten real model attempts across two prospective loops are complete. A new-task
screen produced two fully correct ordinary repairs; its expansion was stopped.
A follow-up used two previously acquired methods with recorded residual errors,
fresh case mixtures and four matched origin/repeat blocks.

Ordinary work completed **2/4 repairs**; the added requirement-linked
cue completed **2/4**. Recorded token use differed by
**-39.70%**, and uncached input plus output by **-34.34%**.
Correctness and cost must be assessed separately; the cue remains experimental.
The cue used fewer recorded tokens in all four pairs, with substantial variation;
one pair contributes about 64.6% of the aggregate difference. Summed worker wall
time did not improve. This is a small cost signal, not established general benefit.

| Origin/repeat | Ordinary | Linked cue | Ordinary tokens | Linked tokens |
|---|---:|---:|---:|---:|
| O/1 | 32/32 | 32/32 | 591,785 | 551,590 |
| O/2 | 32/32 | 32/32 | 1,075,352 | 343,331 |
| S/1 | 28/32 | 28/32 | 718,894 | 440,937 |
| S/2 | 28/32 | 28/32 | 467,732 | 384,913 |

Both conditions used the same REL snapshot, model, complete raw feedback, task
files, tools, budget and offline evaluator. Only a generic execution cue differed.
Workers used gpt-6-luna / medium through a Windows/Codex native coordinator, with
60 tool actions and 900 seconds per attempt. Python ran in an offline Docker
guest. This tests one model/host configuration, not broad model portability.
Eight unchanged-program replays made no model calls. Cases and replays are not
independent model trials; two acquired origins share one specification family.

Both linked workers from the failing origin executed checks of their saved
repair, including numeric parsing and ordinary timestamp normalization. Those
checks still missed a valid input crossing the internal UTC-year boundary.

The remaining representation-boundary defect was repaired separately on a copy,
which passed 64 exposed cohort cases and six focused controls. Original model
scores remain unchanged. This reused a known correction and is not a new discovery
or independently acquired model capability.

All ten attempts used **4,968,428 recorded worker
tokens**, including **4,411,776 cached input**. Parent work, full host
cost, remote compute, currency and energy are not completely measured. No missing
or failed attempt was discarded, and owned-process cleanup was verified.

A separate real-use review justified a generic example in the optional
[non-public source: product-workflow reference](https://github.com/sulabhdubey/recursive-evidence-loop/blob/507357e1d7a55335f9205134ad1c32ac4657b0bc/references/product-workflows.md): mocked error
handling and detection of a real source change need distinct evidence. Main REL
instructions are unchanged. Private project details and raw traces are excluded.

These are exploratory, version-bound results, not evidence of universal or
exponential improvement. The [machine-readable summary](EVIDENCE_2026-10-19_REQUIREMENT_CHECKS.json)
records outcomes, costs and bindings. The private local harness is not included,
so this summary alone does not reproduce the full model study.
