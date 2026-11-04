# Deliverable-scope investigation — 17 October 2026

The previously rejected context-guidance candidate's 97.7% token spike was
associated with optional output preparation. A fresh four-policy comparison
completed 24 native model attempts. The added paragraph changed aggregate
reported tokens by **+2.9%** relative to current full REL and used fewer
tokens on **2/6** matched tasks.

The new default paragraph is not admitted. Only the optional cost-diagnosis reference is clarified: distinguish requirements from permission, inspect actual replies, and preserve useful post-check repairs. This factual measurement clarification is not a demonstrated performance gain from its wording.

## What the old outlier actually showed

The candidate used 316,107 tokens versus 159,887 for full REL: 156,220 extra.
Its first four requests cost 70,358 versus 76,610. Five subsequent requests
producing an optional companion cost 130,260; remaining repair, checks and
completion cost 115,489 versus 83,277. Thus -6,252 + 130,260 + 32,212 = 156,220.
Repeated full-output and encoded-output computations, plus a print probe, were
visible in this optional phase. All 52 audited replies across the old three
arms exactly matched the client-to-server wire payloads. Relevant output was
successful and untruncated; a lost-output transport defect was not established.

The required deliverable was an executable method. The companion path was
permitted, not required. A later correction to ignore installed names outside
the package catalog was useful, even after public examples passed. Removing all
post-pass work would remove that repair. Observed phase accounting does not
establish that deleting the phase would save exactly 130,260 tokens, nor why
the model chose it or whether the earlier candidate wording caused it.

## Prospective comparison

| Policy | Correct tasks | Reported tokens | Uncached input + output | Requests | Actions | Tokens / correct task |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Full REL + deliverable distinction | 6/6 | 1,633,676 | 204,300 | 75 | 97 | 272,279 |
| Current full REL | 6/6 | 1,587,692 | 216,044 | 70 | 98 | 264,615 |
| Ordinary work | 6/6 | 1,278,304 | 162,016 | 67 | 93 | 213,051 |
| Deliverable distinction alone | 6/6 | 1,113,221 | 161,925 | 65 | 98 | 185,537 |


F is the currently installed full skill; D adds one paragraph distinguishing
required deliverables from permitted optional artifacts; P is that paragraph
alone through the same native skill loader; O has no skill. P is a conventional
minimal-instruction comparator, not full REL. All sessions used gpt-6-luna at
medium effort, the same current rules, task examples, tools, 60-action and
900-second limits, and offline code execution. No arm received past-task history.
Noncandidate configurations and tool-result receipts were reconciled.

Six generated tasks span event-time reconciliation and dependency optimization.
Full stream workloads have 256 operations; dependency workloads have seven
packages, up to three releases each and twelve queries. Per task, twelve fresh
integration workloads and eight reused semantic boundaries check the method.
Two tasks also require a compact digest manifest of five public results; four
leave the companion optional. All arms face the same 21 checks per task.
There are six matched task units, not 504 independent replications. The tasks
and reference were investigator-authored, not independently sourced production
cases, an external benchmark score, or evidence of sustained learning.

| Task | Required companion | F tokens | D tokens | D change | P tokens | O tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| resolve-E | No | 228,697 | 415,915 | +81.9% | 124,450 | 334,745 |
| resolve-F | Yes | 187,487 | 220,511 | +17.6% | 198,282 | 379,955 |
| resolve-G | No | 273,640 | 315,437 | +15.3% | 231,440 | 122,540 |
| stream-E | No | 250,648 | 179,150 | -28.5% | 194,178 | 154,966 |
| stream-F | Yes | 440,220 | 210,543 | -52.2% | 207,997 | 134,049 |
| stream-G | No | 207,000 | 292,120 | +41.1% | 156,874 | 152,049 |


D's uncached-input-plus-output total changed by -5.4%, despite its
higher aggregate reported tokens. Its worst matched token regression was
+81.9%. P used 12.9% fewer total
tokens than O in aggregate, but saved on only 2/6 tasks and had a
+88.9% worst regression. P/O uncached input plus output changed by only
-0.06%. These mixed outcomes do not establish a robust generic
replacement, monetary saving, or benefit unique to recursive learning.

## Mechanism and decision

| Policy | Optional companion write actions | Required companion write actions |
| --- | ---: | ---: |
| D | 3 | 2 |
| F | 4 | 2 |
| O | 3 | 2 |
| P | 1 | 2 |


Write counts are observable artifact activity, not a token decomposition or
automatic proof that every write was wasteful. The qualitative review separately
inspected repeated Python computations, returned outputs, repair and required
validation. It found: F and D each produced an optional companion on three of four eligible tasks. D had six repeated public-output computations versus one for F; all returned identical, successful, untruncated outputs. P had one optional-artifact task and one repeated computation, while O had three and two respectively. F initially wrote an undefined placeholder on one optional task, then repaired it. Required companions passed in every arm. Repaired example-schema assumptions and boundary-test errors contributed other costs; they are not all attributable to the deliverable rule.

The pinned cost threshold required at least 10% aggregate D/F savings, savings
on four of six tasks, no higher uncached-input-plus-output total, no quality or
required-companion regression, and lower observed optional-companion effort.
The numerical screen is **not passed**;
default promotion is **rejected**.
The descriptive six-task bootstrap savings interval is
[-46.5%,
31.3%]. It is not
population inference across models or task domains. No outcome-selected rerun,
discarded task, added replicate or changed threshold was used.

## Verification and complete cost

Before dispatch, the old method-only grader was shown to accept the new
required-companion task without its companion. The extended grader rejects
missing, malformed, stale, duplicate-key and wrong-digest companions and accepts
correct ones and optional absence. Actual guest missing/correct checks and all
six full reference packets passed the intended positive/negative criteria.
This is qualification for a new obligation, not invalidation of historical
method-only results. Unchanged containment and mutation checks retain their
exact-source evidence; generated code ran only in the bounded offline guest.

The campaign recorded **5,612,893 tokens**, including
**4,868,608 cached input tokens**;
uncached input plus output was **744,285**.
All 24 attempts, failed intermediate calls and final checks are
included: 24 correct task endpoints and
504/504 declared checks passed.
Summed attempt time was 3439.37 seconds and is not
elapsed campaign time; nested execution time is not added again. Parent
research/build/review, currency, human work and complete physical/remote energy
remain unknown. Token counts including cache are not money or energy savings.
No paid API or GPU experiment was used.

## Research and limits

The initial audit used the exact old task contract, full calls, wire responses,
source snapshots and cumulative usage. Current primary
[tool-design guidance](https://www.anthropic.com/engineering/writing-tools-for-agents)
supports examining actual calls and results on realistic workflows;
the [Agent Skills specification](https://agentskills.io/specification) describes
instruction/resource packaging. Neither establishes this candidate's efficacy.

Baseline package commit: `a9b454d0c1f80823a81eec237c3df355e315e6a9`. Shared instruction updates remain distinct
from the frozen study snapshots. Reliable memory interpretation, consistent
autonomous acquisition, sustained causal improvement and broad portability
remain open; this focused study does not complete the original RSI roadmap.
The next useful question must address a verified remaining mechanism and have
its own bounded information value. Another prompt variant solely to obtain a
passing cost result is not justified by this study.
