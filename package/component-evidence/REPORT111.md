# Run111: choosing missing inputs for a checked decision

1 November 2026. Completed, with independent numerical and result reconstruction.

Run111 combines an earlier agent-built numerical certificate, retained solver state and selective input acquisition. In the fresh comparison, a decision-aware acquisition policy used **28.73% fewer input requests with 2.54% more recorded arm wall time** than the development-selected ordinary control. That timer includes selection, broker access, computation and checks. Both verified **382 of 384 distinct query decisions**, with the same two cases unresolved. The saved learner-built checker executed correctly but doubled arm wall time relative to the equivalent direct formula. The result supports selective acquisition; it does not establish that the learned artifact or the complete architecture is better than ordinary engineering.

The deliverable is an implemented comparison, preserved per-request evidence, independent reconstruction and a source-backed replay example. The target is the exact sign of a fixed optimization model's output, not agreement with the dataset's class labels. Input purchases are controlled access to recorded binary values; their counts are measured, but physical sensing latency and electricity are not.

## 1. Why this follows the wider programme

Run109–110 found that a carefully implemented probability model could still guide queries poorly when its underlying predictions were weak. Continuing the same density-model search would not address that result. Run102 already supplied an actual learner-built primal–dual checker, and Run103 supplied continued numerical state. Run111 connects these earlier methods to a different question: **is the unresolved decision caused by missing information, unfinished computation, or both?**

This integrates A2 acquired methods, A3 reusable computation, A4 information acquisition and A5 output-directed completion in the existing A1–A7 plan. A1 retains the current input mask and numerical state. A6's improvement procedure stays fixed. A7 checks which claims follow from source semantics, executed actions and the consumer's endpoint. The six brain–AI threads remain relevant: organisation, training versus exposure, resources, measurement, representation/use and capability forecasting. Neither a biological analogy nor an earlier mathematical breakthrough supplies the empirical outcome automatically; here the mathematical construction is implemented and compared directly.

## 2. Source and genuinely missing information

The official [LIBSVM w8a collection](https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html#w8a) contains 49,749 rows and 300 features. [Platt's source description, section 3.2](https://www.microsoft.com/en-us/research/uploads/prod/1998/04/sequential-minimal-optimization.pdf), establishes binary webpage features. The source validator also checks every stored value. This supports the allowed `{0,1}` domain; hidden empirical minima or the realized query values are not used to choose bounds.

An independent source audit reconstructed the recorded Run102/103 assignments and inspected later implementation references. It found 34,704 unique input vectors, of which 32,096 had appeared in the recorded earlier experimental tasks. The remaining 2,608 supported 384 fresh unique query identities. Training uses previously exposed inputs; 64 development queries are also previously exposed and disjoint from all selected training inputs. Fresh query identities have no overlap with those roles.

The raw file had been parsed previously. Thus, “fresh” means unused in the recorded task assignments, not a new corpus or cryptographically protected raw-data custody. Source metadata and hashing were inspected before release; the fresh query arrays were withheld from the scorer until qualification and review. See [non-public source: source research](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/certified-information/RESEARCH.md), `SOURCE_ROLES.json` and `AUDIT_SOURCE.json` for coverage and limits.

For each query, the policy initially knows no active input bits. The broker returns only the requested bit; zero is a paid answer. The policy cannot inspect nonzero indices, labels, the full row norm or other hidden summaries. All methods can omit coordinates absent from the training matrix because their optimum weight is exactly zero under this objective. The same active-input support is available to every control.

## 3. What is verified

For the weighted hinge objective

`F(w) = 0.5 wᵀDw + Σᵢ Cᵢ max(0, 1 − Hᵢw)`, with positive diagonal `D`,

the required output is the strict sign of `qᵀw*` at the unique optimum. There is no free intercept and no artificial tolerance band around zero. Outputs are positive, negative, structurally exact zero, or unresolved.

A feasible dual point provides a lower objective bound. If the checked primal–dual gap is `g`, strong convexity gives a weighted distance bound on `w − w*`. For acquired bits and any permitted completion of the remaining bits:

- `L₀ = Σknown qⱼwⱼ + Σunknown min(0, wⱼ)`;
- `U₀ = Σknown qⱼwⱼ + Σunknown max(0, wⱼ)`;
- `M = Σknown qⱼ²/Dⱼ + Σunknown 1/Dⱼ`;
- numerical error is bounded by `sqrt(2 g M)`, with the retained implementation's numerical allowance and a separate sum-arithmetic allowance.

The final enclosure combines the input range and numerical radius. A decision is emitted only when the enclosure has one strict sign, or the output is structurally zero. A solver's “solved” status alone is insufficient. Inactive-coordinate projection is applied consistently before recalculating the checked gap.

The actual saved Run102 w8a graph, with 25 algebra nodes and SHA256 `437a99f65146c105689a67180550775f79f137b7e801800da33c2e1514b028fb`, supplies the learned arm's numerical radius. Its cap-vector centre is not mistaken for the requested query centre. The solver keeps an immutable problem and fixed dummy query interface; changing the acquired-input mask does not weaken its state-identity checks.

The mathematical enclosure is backed by independent finite checks. The implementation uses float64 allowances, not formal directed rounding or a machine-checked numerical proof.

## 4. Controls and frozen decisions

Four allocation schedules are crossed with two input-selection rules:

| Schedule | Operation |
|---|---|
| Tight first | Finish the numerical solve, then purchase inputs. |
| Observe first | Use the initial checkpoint while acquiring inputs, then refine when needed. |
| Alternate | Continue the solve by 200 iterations after every eight acquisition rounds. |
| Witness | Refine when the input-only interval already determines the answer but numerical uncertainty still prevents certification; otherwise acquire an input. |

The width rule purchases the remaining feature with largest absolute current coefficient. The progress rule considers both possible answers and ranks expected immediate certification, then progress toward excluding zero, then interval-width reduction. Training-only feature frequencies supply its probabilities. It is a conventional adaptation of [stochastic Boolean function evaluation](https://arxiv.org/pdf/1303.0726); the published independence and discrete-threshold guarantees are not asserted for this correlated floating-point problem.

These eight ordinary arms use the direct numerical formula. A ninth arm runs the saved learner graph with witness/progress. A tenth purchases every active input and performs a tight solve. All share the same inputs, objective, batching opportunity, iteration limits and checking mathematics. The new missing-input wrapper and controller are coordinator-built; this run does not count them as a newly autonomous acquisition.

The primary allocation comparison is **ordinary witness/progress versus the best development-selected non-witness schedule**. Selection maximizes verified completion, then minimizes recorded wall time plus the declared 1 ms per-request proxy. It selected **alternate/width**. The learned/direct twin and width/progress differences are separate comparisons. Every fresh arm remains visible; no fresh runner-up replaces the frozen control.

## 5. Qualification and fresh design

All six development conditions passed on two QPs and 64 queries:

| Qualification requirement | Observed |
|---|---:|
| Reference resolves at least 60 cases, at least 24 nonzero | 64 resolved, all nonzero |
| At least 16 unresolved after eight progress-rule purchases | 64 |
| At least eight such cases have legal opposite-sign completion witnesses | 64 |
| Query rules change first completion or paid work for at least eight cases | 62 |
| A numerical continuation certifies a case without another input | 10 such rescues across the development executions |
| No observed soundness or contract error | 0 |

The fresh comparison contains 12 QPs with 32 unique queries each and four requirement phases: ordinary penalties, changed diagonal regularization, changed example penalties, and a permuted feature interface. Each phase has three training replicas. Training sets may overlap. The permutation phase is a changed interface condition, not a paired isolated causal permutation experiment.

Ten arms run twice per QP, with reversed arm order on the second timing repetition: 240 executions and 7,680 output opportunities, but only **384 distinct query cases in 12 correlated clusters from one source**. The repetitions are not additional independent evidence. Descriptive uncertainty uses 2,000 paired cluster resamples with seed 111.

The measured development duration projected beyond the original 600-second single-process limit. Before fresh access, a reviewed execution amendment split the unchanged 240 executions into two sequential six-model batches. Exact membership, order, merge completeness and stale-admission rejection were tested. Both batches completed within the original per-process limit. The original plan, scorer, development choice and result bytes remained frozen.

## 6. Fresh results

Totals below include both timing repetitions. Every arm verified 764 of 768 opportunities, representing the same 382 of 384 distinct queries. There were no observed false or unknown-reference acceptances; the same two query decisions remained unresolved for all methods.

| Method | Input requests | Recorded computation wall time | Solver iterations |
|---|---:|---:|---:|
| Tight / width | 62,978 | 22.001 s | 23,450 |
| Tight / progress | 44,306 | 41.999 s | 23,450 |
| Observe / width | 70,798 | 27.159 s | 8,750 |
| Observe / progress | 53,242 | 53.307 s | 8,750 |
| **Alternate / width — frozen control** | **62,974** | **29.913 s** | **21,750** |
| Alternate / progress | 44,316 | 33.622 s | 21,750 |
| Witness / width | 62,996 | 23.304 s | 15,350 |
| **Witness / progress — allocation candidate** | **44,880** | **30.672 s** | **13,050** |
| Saved learner graph / witness / progress | 44,880 | 61.437 s | 13,050 |
| All active inputs / tight solve | 167,744 | 4.475 s | 23,450 |

The allocation candidate saved 18,094 requests, or **28.73%**, with **2.54%** extra measured wall time and no newly unresolved output. It meets the pinned condition of at least 5% fewer requests with at most 20% extra computation. Its paired-cluster request difference was −753.92 requests per 32-query batch/repetition, with a descriptive 95% resampling interval of [−859.43, −653.08]. The corresponding time difference was +0.0316 s, interval [−0.5522, +0.4459]; the data do not establish a computation-speed gain.

**The controls locate the contribution.** Ordinary alternate/progress also uses substantially fewer requests than alternate/width, and uses 564 fewer requests than witness/progress. Witness/progress was about 8.77% faster than alternate/progress in these recorded totals. The study therefore does not isolate a unique superiority of the witness schedule. Decision-aware input ranking accounts for much of the useful effect, while the schedule changes the computation/request trade-off.

**Actual learned-method reuse works, but its overhead matters.** The saved graph reaches the same final purchased sets, per-row decisions, request counts and certificate steps as the direct witness/progress twin, with the same solver/check sequence. Acquisition order is identical in 22 of 24 model/repetition pairs; one row swaps two request positions in both repetitions after small floating-point differences. Its 61.437 s versus 30.672 s is **100.30% more arm wall time**. That arm does not satisfy the primary raw cost condition against the frozen control. The successful allocation comparison must not be relabeled a benefit caused by learning or by REL.

The checker timing bucket increases from 5.527 s to 25.658 s, accounting for 65.43% of the extra recorded wall time. Selection timing also rises, so the entire difference cannot be assigned causally to graph arithmetic. In the direct candidate, selection alone occupies 21.956 s, or 71.58% of recorded wall time. Any next optimization must include that work instead of targeting only interpretation overhead. See `POST_RUN_DIAGNOSTIC.json`.

**The complete-input baseline is fastest when retrieval is cheap.** It takes only 4.475 s of computation, while buying 167,744 inputs. The prospective additive-latency sensitivities at 0, 0.1, 1 and 10 ms/request remain in `FRESH_OUTCOME.json`. At the declared 1 ms proxy, witness/progress totals 75.552 proxy-seconds versus 92.887 for the frozen control, 106.317 for the saved graph twin and 172.219 for all inputs. These are sensitivity calculations, not measured end-to-end latency. They assume additive equal-cost queries and do not establish a physical sensing or network saving.

## 7. Costs, corrections and reproducibility

The three numerical jobs used **441.016 seconds of in-process wall time**: 52.035 for development and 230.734 plus 158.247 for the fresh batches. These include their own loading, arm execution, offline references, witness checks and result writing. The corresponding three enclosing command timers total **475.511 seconds**. These are alternative timing boundaries, not quantities to add together. The cost ledger combines 32 distinct, nonnested recorded operations into a **715.501-second pre-delivery work subtotal**, including recorded source preparation, tests, audits and workspace replay. This is summed work time, not end-to-end elapsed time or complete research cost. Later package verification and delivery have separate receipts.

The exact reused method's earlier acquisition/adaptation has recorded client receipts totaling **160,052 tokens**, including cached input, and 174.569 seconds of historical session wall time. That is a historical method cost, not a new charge for each Run111 arm. No new evaluated learner session, direct paid provider request or GPU run was launched. Full coordinator/reviewer token usage, uninstrumented work, electricity and complete host idle/sensing costs remain unknown; the recorded subtotal is not an all-in research cost.

The evidence retains implementation and review failures. A source codec typo was fixed before modeling. A first development audit needed a bounded floating-point summation correction. The fresh audit exposed a different replay problem: the reviewer allocated state like the Fortran-contiguous source arrays, whereas the producer used C-contiguous working state. Near-equal progress scores changed a discrete tie choice. The repair preserves the original auditor and available failure evidence, reconstructs the producer's exact state representation for policy replay, and separately checks the mathematical enclosure. Initial failed full-audit durations are unknown; two saved fresh diagnostic filenames refer to one operation, and overwritten intermediate diagnostics are disclosed rather than counted as separately sealed receipts. The repair changes neither purchased inputs nor scored results and does not relax the requirement that requests replay exactly. The completed fresh audit checked all 240 attempts, 37,082 numerical checkpoints and 659,114 input purchases; the public-outcome audit reconstructed the selection, result and all 20 cluster intervals.

The package provides a standard-library result verifier, exact public attempt files and a development replay using a locally supplied source file of the pinned hash. Raw source vectors, purchased bit values, fitted solver vectors and local-path manifests remain excluded; their omissions and identities are explicit. This is same-evidence reconstruction plus a declared numerical replay, not independent new-data replication. Publication remains private.

## 8. Programme and REL decision

Retain the demonstrated component: a system can distinguish unfinished computation from missing inputs and stop acquiring information once its output is checked. Keep the strong ordinary progress controls and the fast complete-input baseline. Do not claim that every input-selection rule needs a learned backend.

The next mechanism should address repeated work across **different update events**, before adding more acquisition heuristics. A purchased bit changes a small part of the input state; a solver continuation changes the numerical candidate and may invalidate different cached quantities. Qualify whether a learner can acquire an incremental checking-and-selection method that tracks these dependencies correctly, then compare it with a strong conventional incremental implementation, the direct formula and the frozen graph on fresh changed requirements. This joins A1's retained state, A2's method acquisition and A3's computation to the now-tested A4/A5 decision contract. Include selection cost, preserve the exact checking contract and reject stale compiled state. The independent graph/witness-query source remains a materially different alternative if ordinary incremental processing already removes the gap.

REL's evidence, replay example and existing programme are updated from this result. The generic core remains stable: existing instructions already require the independent controls, full execution boundary, preserved failures, source-role checks and whole-programme review used here. The numerical representation lesson is retained in the study and next design; broader instruction changes need evidence that they transfer beyond this example.
