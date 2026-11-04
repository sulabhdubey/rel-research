# Observation reuse and rediscovery work — 24 October 2026

Two generated reporting-service sequences completed **26 fresh task sessions**:
two acquisitions and six later tasks per policy. Every session started with empty
output/helper locations. Prior query measurements were absent from shared code
and current documentation. All policies had the same current service access.

**Finding:** retained observations reduced later query work, but the REL variants
did not improve final decisions over ordinary factual handoff in these sequences.
REL with facts used 76.8% less
later query work than REL without history. Ordinary handoff used
77.6% less. Adding REL to the
factual handoff used 55.4%
more total tokens and 7.1%
more uncached input plus output, with equal final correctness.

| Policy | Later tasks passed | Probes | Query VM-work upper bounds | Total tokens | Uncached input + output |
|---|---:|---:|---:|---:|---:|
| Ordinary + factual handoff | 6/6 | 32 | 1,101,500 | 713,384 | 191,528 |
| REL + factual handoff | 6/6 | 40 | 1,136,900 | 1,108,706 | 205,154 |
| REL + agent-created lessons | 6/6 | 48 | 1,185,700 | 1,588,998 | 263,174 |
| REL without episode history | 6/6 | 102 | 4,909,400 | 767,000 | 163,224 |

The lesson-writing policy used
122.7% more total tokens than
ordinary handoff, including its feedback turns. It provided no aggregate query-work
advantage over either factual-handoff policy. REL's work comparison with ordinary
handoff differed by cohort: slightly lower work in C1, higher in C2. These are
descriptive contrasts from two streams, not stable population estimates.

Query work includes diagnostic probes and final report execution. Values are
conservative SQLite VM-instruction upper bounds, not money or energy. These
queries took fractions of a second of CPU time per task on this machine; a large
work ratio does not establish a large wall-time saving. Token totals include
cached input; uncached input plus output is shown separately.

The two common acquisitions used 485,720 tokens and
1,789,100 query-work units. They are counted once in actual study
usage of 4,663,808 tokens and 10,122,600
query-work units. Policy rows include their own feedback and lesson-maintenance
turns. Parent-model effort, full engineering costs, money and energy remain unknown.

To avoid treating history as free, the following scenario charges the **entire**
two-task acquisition and its feedback to each retained-history policy, while N
pays only for its six fresh later tasks. Earlier reports produced during acquisition
receive no credit in this conservative accounting. These are alternative deployment
scenarios, not additional observed runs or sums to add to actual study usage.

| Policy, with history acquisition charged | Query work | Total tokens | Uncached input + output |
|---|---:|---:|---:|
| Ordinary + factual handoff | 2,890,600 | 1,199,104 | 248,832 |
| REL + factual handoff | 2,926,000 | 1,594,426 | 262,458 |
| REL + agent-created lessons | 2,974,800 | 2,074,718 | 320,478 |
| REL without episode history | 4,909,400 | 767,000 | 163,224 |

On that basis, REL with facts still used
40.4% less query work,
but 107.9% more total
tokens than N. Lower database work therefore does not establish lower total cost.

The source revision changed for two of four stores before E3. The lesson-bearing
workers read earlier lessons, measured changed conditions, selected updated
routes and wrote revisions. E4 tested later use in fresh sessions. Correct final
choices and matching report results corroborate action; a read or saved lesson
alone was not accepted as proof. Ordinary factual handoff was a strong control.
Both E4 lesson-bearing workers read the E3 lesson, reused four exact older
measurements for unchanged stores, measured four newly aggregated requests and
selected all eight routes correctly. All 24 later first-saved plans also passed;
no final-accuracy or later repair advantage was observed.

| Nonmodel policy | Later tasks passed | Later query work | Acquisition query work |
|---|---:|---:|---:|
| auto | 0/6 | 2,227,100 | 700,400 |
| measure_all | 6/6 | 6,922,600 | 2,139,100 |
| revision_cache | 6/6 | 1,404,400 | 2,139,100 |

The cache is a conventional researcher-implemented exact-key baseline, not an
agent, REL, or a novel algorithm. It keys source revision and filter parameters;
its reuse across the tested aggregation changes succeeds here but is not a general
optimizer guarantee. Its construction effort was not measured. No agent-policy
superiority over that practical alternative is inferred from a successful loop.

Two unrelated host issues were preserved: a no-inference filesystem-permission
failure and a no-inference Windows path-spelling mismatch. The latter was corrected
prospectively by verifying the same filesystem object; positive and rejection
checks passed. Original releases, logs and failed starts remain. One acquisition
also corrected a suboptimal first saved plan before final submission. Its learner's
explanation is retained as an attributed account, not independently proven cause.
The post-run aggregation audit also found an exhausted iterator that zeroed token
subfields while leaving total tokens correct. The faulty summary was retained,
the aggregation was repaired and all fields were independently reconciled with
the original session receipts before this report was generated. No model attempt
was changed or repeated for that correction.

At E2 the O/R/L factual packets matched; later histories follow each policy's own
observations. O/R separates REL from ordinary work with initial equal facts; R/N
tests retained observations under REL; L/R includes lesson-authoring and feedback
costs. Facts preserve service requests/results and final feedback, not every actor
interpretation, so L/R is not a pure formatting comparison. Acquisitions used REL;
ordinary continuation is not an end-to-end no-REL acquisition baseline.

This is two seeded sequences from one constructed generator, with one worker per
policy/stage, rather than independent production-project evidence. Models ran
through the existing contained host. The researcher knows the evaluator. Query
counts, intermediate decisions, costs, failures and limits remain explicit; no
population significance, general RSI or novel optimizer claim follows.

All 20 core files remain unchanged. Existing instructions already require scoped
reuse, current evidence and actual output checks. Evidence and examples are updated;
no new mandatory instruction or behavior-change claim was justified.

[Structured results](EVIDENCE_2026-10-24_OBSERVATION_COST.json) · [Evidence index](EVIDENCE.md).
Design references: [AgentCL](https://arxiv.org/abs/2606.02461),
[MemoryArena](https://arxiv.org/abs/2602.16313),
[SQLite planning](https://www.sqlite.org/optoverview.html), and
[VM callback semantics](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_progress_handler).
