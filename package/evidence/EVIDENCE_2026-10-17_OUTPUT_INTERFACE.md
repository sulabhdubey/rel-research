# Explicit task outputs and tool visibility — 17 October 2026

Explicit output contracts changed artifact choices but did not establish an efficiency improvement. None of the 16 eligible T/I submissions created an optional companion, versus four of eight original-contract submissions; all 12 genuinely required companions passed. Under full REL, the file-only interface used 1.9% more total tokens than the original contract, and tool projection used a further 8.7% more than the identical file-only task. Under ordinary work, projection used 21.8% fewer total tokens than file-only access, but 3.8% more uncached input plus output; both variants cost more than ordinary work with the original contract. Neither interface passed the predeclared admission criteria.

The optional host-integration reference is clarified to distinguish required deliverables from permitted and host-reserved paths in the existing task contract, and to keep any tool projection consistent with that source. It does not require a new manifest or repeated metadata. This is a factual interface clarification, not a demonstrated performance gain from its wording. The main skill and generic host executables remain unchanged; automatic projection and extra output-contract files are not adopted as default optimizations.

## Prospective design and controls

The prior deliverable-scope paragraph did not qualify for promotion. This study
tested the task/tool interface without adding another skill paragraph. Six fresh
task instances were crossed with three interfaces and two work styles, giving
36 native model sessions. No outcomes were discarded or retried.

L supplies the existing task contract. T adds a compact explicit output-contract
file distinguishing required outputs, optional permitted artifacts and reserved
files. I supplies the byte-identical T task and also shows that contract in the
tool definition and list result. Thus I/T tests visibility with equal available
facts; T/L tests explicit task clarification. R loads the frozen full REL skill;
O uses ordinary work without REL. Every session has current rules, public
examples, the same tool permissions and evaluator, and no retained history.

All sessions used gpt-6-luna, medium effort, native Codex subscription transport,
60-action/900-second limits and at most two simultaneous workers. Learner code
ran only in the existing offline bounded Docker guest. The fixed order rotates
all six policies across task positions. A required-artifact check was the same
for all policies; tool output presentation did not alter permission enforcement
or suppress optional actions.

The event-time tasks have 256-operation integration workloads; dependency tasks
use seven packages, up to three versions and twelve queries per workload.
Each task contains twelve newly seeded integration workloads and eight known
semantic boundaries. Two tasks require a five-public-result digest manifest;
four leave that companion optional. These are six generated comparison units
in two previously studied families, not 756 independent trials, independently
sourced production tasks or a broad benchmark score.

## Results and complete recorded worker cost

| Policy | Correct tasks | Total tokens | Uncached input + output | Requests | Actions | Tokens / correct task |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| REL / existing contract | 6/6 | 1,357,309 | 172,413 | 63 | 82 | 226,218 |
| REL / explicit file | 6/6 | 1,383,337 | 214,825 | 65 | 97 | 230,556 |
| REL / file + tool projection | 6/6 | 1,503,684 | 201,156 | 70 | 100 | 250,614 |
| Ordinary / existing contract | 6/6 | 736,192 | 150,720 | 46 | 66 | 122,699 |
| Ordinary / explicit file | 6/6 | 1,198,895 | 164,911 | 61 | 91 | 199,816 |
| Ordinary / file + tool projection | 6/6 | 937,764 | 171,172 | 52 | 78 | 156,294 |


| Task | Companion required | RL | RT | RI | OL | OT | OI |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| resolve-H | No | 261,347 | 159,134 | 269,004 | 81,707 | 260,121 | 130,302 |
| resolve-I | Yes | 285,520 | 167,738 | 467,104 | 142,019 | 285,077 | 170,926 |
| resolve-J | No | 174,991 | 342,791 | 133,134 | 110,774 | 139,076 | 148,043 |
| stream-H | No | 213,578 | 265,400 | 210,741 | 94,260 | 117,958 | 116,045 |
| stream-I | Yes | 204,603 | 256,459 | 198,878 | 204,405 | 265,842 | 206,649 |
| stream-J | No | 217,270 | 191,815 | 224,823 | 103,027 | 130,821 | 165,799 |


Total tokens include cached input. Uncached input plus output is reported
separately; neither measure is billed currency, FLOPs or energy. Reasoning
tokens are retained in the receipts and are not added again to output totals.

| Comparison | Total token change | Uncached change | Tasks saving | Worst task change | Numeric screen |
| --- | ---: | ---: | ---: | ---: | --- |
| RI vs RT | +8.7% | -6.4% | 3/6 | +178.5% | Fail |
| OI vs OT | -21.8% | +3.8% | 4/6 | +26.7% | Fail |
| RT vs RL | +1.9% | +24.6% | 3/6 | +95.9% | Fail |
| OT vs OL | +62.9% | +9.4% | 0/6 | +218.4% | Fail |
| RI vs RL | +10.8% | +16.7% | 3/6 | +63.6% | Fail |
| OI vs OL | +27.4% | +13.6% | 0/6 | +60.9% | Fail |


The predeclared admission required at least 10% aggregate token savings,
savings on at least four of six tasks, no task above 25% token regression,
no increase in aggregate uncached input plus output, no quality regression and
no critical authority/evidence regression. A background-independent interface
recommendation requires both R and O to satisfy these criteria. Tool-projection
qualification: **False**. Explicit-task-file qualification:
**False**. I/L is the descriptive combined contrast, not a
replacement primary comparison. All contrasts are shown; no multiplicity-adjusted
significance or population-general effect is asserted.

## Observed mechanism and errors

| Policy | Optional companions / 4 | Required artifacts passed / 2 | Repeated Python calls | Rejected or nonzero-exit calls |
| --- | ---: | ---: | ---: | ---: |
| RL | 3 | 2 | 0 | 5 |
| RT | 0 | 2 | 0 | 8 |
| RI | 0 | 2 | 0 | 9 |
| OL | 1 | 2 | 0 | 2 |
| OT | 0 | 2 | 0 | 4 |
| OI | 0 | 2 | 0 | 4 |


Original-contract REL produced three optional companions in four eligible tasks; original-contract ordinary work produced one. Two companions were exact copies of all five public results and two were small task/method summaries; their recorded contents were checked. All four explicit-contract policies produced none. Required artifacts passed in every policy. No identical Python-call repetitions were observed in any policy, including the original contracts, so their absence cannot be credited to the intervention. Projection did not generally replace file reads: RI read the contract file seven times over six tasks, while OI read it four times. There were 32 rejected or nonzero-exit calls across policies, including input-shape assumptions, test errors, implementation repairs, an ephemeral scratch-file assumption and an optional bytecode-write failure. A separate zero-exit check in stream-J/RL printed a semantic mismatch, which the worker repaired; it is preserved but is not counted as a process exception. Initial input totals were identical for L/T in each background; I added 885 initial input tokens per six-task group. Later requests and context growth differed: RL/RT/RI made 63/65/70 model requests and OL/OT/OI made 46/61/52. These are descriptive observations, not a causal token decomposition. Removing optional artifacts alone did not remove the other sources of effort.

Optional artifacts are not automatically erroneous or wasteful. The last column
counts rejected tool calls and nonzero process exits, not every semantic failure
printed by an otherwise successful process. Repeated calls
are classified from actual code, source/write state and returned outputs;
the review does not infer private reasoning or intent. A useful repair after
passing public examples remains useful. Fewer artifact writes do not alone
prove a token saving or improved completion.

## Verification and measurement limits

Four test methods first failed because the projection was absent, then passed
against the actual broker, including required versus optional companions,
source-bound projection, unknown/mismatched fields, authority mismatch, reserved
phase restrictions and an unchanged input schema. All six reference methods
passed their full bounded-guest qualification; the prior grader/evaluator bytes
were unchanged. T/I task files were identical, and L/T shared task facts,
evaluation and permissions matched. Actual native tool definitions, list
replies and public source hashes were reconciled after dispatch.

36/36 task endpoints passed all declared checks;
756/756 check verdicts passed. The
denominator comprises 720 method checks, 12 required-artifact checks and 24
optional-artifact absence-permitted verdicts; these are not independent samples.
All recorded model requests, intermediate failures, tool results, receipt-only
feedback and verification are included. Campaign usage was
**7,117,181 tokens**, including
**6,041,984 cached input tokens**;
uncached input plus output was **1,075,197**.
There were 357 model requests and 514 tool actions.

Elapsed campaign time was 2581.73 seconds; summed
attempt time was 4852.83 seconds and is a different
measure. Reference qualification took 101.65
seconds. Nested guest time must not be added to enclosing attempt time.
Parent research/build/review tokens, currency, human effort and complete
physical/remote energy are unavailable, not zero. This is complete recorded
worker cost, not a complete cost-effectiveness or wall-energy measurement.
No paid API or GPU model experiment was used.

No critical authority, custody or final-evidence regression was observed in the exposed task declarations, unchanged public inputs, tool definitions/results, preserved execution receipts, frozen submissions, completion messages and verified worker terminals. All 36 final messages and relevant successful/error checks were inspected. This is a scoped review of this host and these routes, not an independent security audit or a guarantee about unexercised tools. Two parent audit probes initially used an incorrect declaration path, and the first final-message selector expected the wrong phase name; the actual producer schema was inspected, selectors were corrected and the earlier records were preserved. These postprocessing corrections changed no task, model attempt or outcome.

## Research and next decision

Current primary [tool-design guidance](https://www.anthropic.com/engineering/writing-tools-for-agents)
motivated testing precise task interfaces and inspecting actual trajectories;
it did not establish the result in advance. The [MCP tool specification](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
distinguishes interface schemas and structured tool results. Our manifest is a
task deliverable contract, not an MCP outputSchema or proof of downstream
correctness. [Agent Skills packaging](https://agentskills.io/specification)
does not itself provide host enforcement. These sources were inspected before
building the study on 17 October 2026.

Close this output-interface optimization branch at its current scope. The last prompt-level candidate and these task/tool variants do not justify further default-rule growth or another near-identical wording search. Reuse precise existing task contracts when a concrete ambiguity needs correction. A later efficiency experiment should start from a distinct, observed remaining workflow cost and test a specific mechanism against the strong ordinary-work baseline, with new task instances and inclusive accounting. Do not tune this manifest on the now-exposed six tasks or treat reduced optional output as proof of lower whole-task cost.

The main skill remains byte-identical to the evaluated predecessor. This study
does not establish reliable semantic memory, sustained learning, autonomous
capability acquisition, broad harness portability, universal RSI effectiveness
or superiority over equally informed ordinary work.
