# Retained Experience, Executable Methods, and the Limits of Transfer

## Evidence from Recursive Evidence Loop

Sulabh Dubey | Consolidated technical report v0.7 | 5 November 2026

Public technical report; not peer reviewed. Study edition v0.7, public packaging v0.7.1. Deliverable: six agent-study summaries, a cross-programme component synthesis, saved-result reconstruction scripts, the current REL instruction snapshot, and a runnable constructed localization example. Reconstructing supplied results is distinct from independently replicating the original experiments.

## Abstract

What must an adaptive agent retain so that earlier work improves a later decision? We synthesize two complementary evidence families: controlled studies of Recursive Evidence Loop (REL), an instruction package for researching and revising work with fixed model weights, and a programme of acquired executable methods and reusable working state. Retained observations reduced repeated database work, while equally informed ordinary agents remained strong controls. Acquired robot-update programs achieved lower average error but did not uniformly reduce large errors. On six previously exposed diagnostic recordings, ordinary averaging reduced recording-balanced mean squared error by 10.39% and above-0.5 m outputs by 9.51% relative to robust filtering, while giving up 1.84% in mean squared error relative to the acquired programs. A separate numerical workflow used 28.73% fewer input requests with 2.54% more wall time; its learner-built checker was slower than the equivalent direct formula. We consolidate nine components into four typed implementation families and provide a runnable localization reference. Transfer remains conditional: an independent range-only source lacks the verified configuration and reference contract needed to admit the proposed comparison. The contribution is a source-linked synthesis and checked component package, not a pooled treatment effect or a demonstrated general architecture advantage.

## 1. The claim must identify what improved

REL asks an agent to research the current gap, apply or reject earlier lessons, select useful feedback, act and check, then retain what can change a later action. It can guide changes to tools, plans, memory and instructions. The host supplies persistence, execution and authority. Reading a Markdown skill does not create those mechanisms or make the agent follow every instruction correctly.

We distinguish four claims. **Execution:** the procedure and tools ran. **Transfer:** earlier evidence affected a later action under the current contract. **Practical benefit:** the result improved relative to a capable alternative after relevant costs and harms. **Improvement of improvement:** a changed learning procedure subsequently outperformed its frozen predecessor. Execution and transfer have concrete examples here. Practical benefits occur in particular components; consistent added REL benefit and improvement of improvement remain unestablished. These are distinct questions, so a useful component is retained even when an instruction variant fails.

The research originated in investigations of evidence provenance, brain-inspired memory and adaptation, and mathematical/source review. Those strands motivated questions, not a unified experiment. Incident tracing did not establish a previously unknown incident; biological analogies did not establish biological equivalence; reviewing mathematical work did not establish a new algorithm. Their role here is methodological background. Sections 9-11 now connect the brain-AI component results to the agent studies while retaining their separate denominators, interventions and evidence limits.

## 2. Related work and the scope of this contribution

Executable skill libraries and feedback-based refinement are established ideas. Voyager retains executable skills and iteratively improves programs from environmental feedback [1]. Reflexion retains linguistic feedback across trials without updating model weights [2]. These precedents motivate testing both executable assets and prose; REL does not claim to originate either mechanism.

AI Agents That Matter argues for evaluating costs alongside accuracy and for adequate holdouts and reproducibility [3]. MemoryArena evaluates interdependent multi-session tasks in which prior experience guides subsequent action [4]. MemoryLake's matched MemoryArena comparison explicitly distinguishes a bundled backend comparison from a representation-only or cost-matched ablation, and reports workload-dependent limits [5]. These are methodological comparators, not systems reimplemented in our studies. Their reported benefits are not evidence for REL.

Our contribution is a selected-results synthesis with executable arithmetic reconstruction: it separates useful retained information from added procedure, tests when unchanged executable assets already suffice, exposes failures hidden by scored success, and traces why smaller context can produce more model requests. The components and their contracts provide reusable engineering examples. The package does not rerun the original model trials or establish a state-of-the-art result.

A recent complementary study, Compile Once, Run Cheap [7], separates offline executable-skill authoring from later execution and distinguishes inherited code from additional feedback through separate controls. We use that distinction to interpret our longer reuse sequence: amortization of an acquired asset and added benefit from REL are different comparisons. We have not reproduced that system or compared REL against its framework.

## 3. Evidence selection and common evaluation boundaries

Sections 4-7 center the two linked 18 October code studies and all four 24 October connected-observation studies. They directly address reuse, changing requirements and information reacquisition. Intermediate 19-23 October qualification and repair studies remain in the accompanying evidence index; they are not pooled into a success rate or discarded because results were negative. The selection is thematic and retrospective, not a preregistered meta-analysis. The November extension adds the component register from Run120 and directly relevant comparisons from Runs106, 111, 118 and 119; it does not pool them with S1-S6. Run121 is source qualification and synthesis, with no new model experiment or physical-data scoring. This revision also restores the longer reuse sequence (Run86), the direct procedure-evolution comparison (Run92), and the method-selection counterexample (Run114). Appendix J records the wider research lineage and the review coverage; no claim is made that every historical raw artifact was reaudited.

The two S1/S2 code studies used recorded gpt-6-luna/medium workers. The four S3-S6 studies used gpt-6.1-sol/medium. Within S1-S6, compared workers received matched current requirements, tools and maximum allowances: 60 actions and 900 seconds per task. Fresh native sessions and bounded offline execution were used. Equal limits do not imply equal executed work or equal internal reasoning. Public source material may have appeared in training. The researcher could inspect evaluation material; these are not hostile-agent sealed evaluations.

Ordinary controls could inspect, test, repair, reuse and adapt. They were not prohibited from competent engineering. Where histories were matched initially but then evolved independently, later equality of information is not claimed. Where all arms retained code, an arm without episode history is not called state-free. Candidate adoption criteria were fixed within each study before its scored comparison; subsequent diagnosis is labelled as exposed exploratory analysis.

Model-assisted tools were used for study construction, execution, analysis and drafting. Separate reviewer agents and differently implemented checks audited selected claims; these are automated cross-checks, not external human peer review.

The independent unit is the task block or sequence, not each assertion, SQL row or generated scenario. Repeated checks on one implementation do not create independent agent trials. Results below are descriptive; no population-level superiority or equivalence follows from all tasks passing.

## 4. Executable experience: reuse is not necessarily adaptation

Study S1 acquired two JSON Schema implementations and compared 24 later sessions: A ordinary work without prior history, B ordinary work with complete origin history, and C REL with that same history. The origins used REL, so acquisition quality itself was not randomized. B and C passed 8/8 later tasks; A passed 7/8. Inclusive tokens were 1,475,038 for B and 1,473,718 for C, effectively tied at this scale. A used 1,270,553 tokens. The single ordinary failure was not reproduced by its ordinary repeat.

Direct execution of the unchanged origin implementations subsequently passed both transfer packets, with 680 case evaluations and no new model call. This exposed diagnostic established that those packets did not require a new adaptation. It did not prove an automatic policy could always decide when direct use was safe. Origin code, inputs and authored notes transferred together, so a benefit cannot be assigned specifically to prose lessons.

Study S2 introduced reference and annotation obligations missing from the earlier implementations. Twenty-four adaptations and 24 unchanged later replays passed their scored vectors. REL used 8.1% fewer acquisition-inclusive tokens than equal-history ordinary work, but 66.8% more than ordinary scratch work. Omitting one matched block reversed the REL-versus-handoff aggregate. A targeted post-outcome source review then found incorrect annotation propagation in one REL-produced implementation despite perfect scored results. A separate investigator repair passed its checks; it was not relabelled as a learner success.

Together, these studies establish observed reuse, extension and finite transfer. They do not establish general semantic correctness, a reliable REL efficiency advantage, or improvement of the learning procedure itself. Detailed row-level arithmetic and the diagnostic are preserved in the companion materials.

## 5. Connected episodes: a complete learning cycle can still tie

Study S3 used one constructed archive/CSV/SQLite migration project: one acquisition followed by three episodes under four continuation policies. An agent created a scoped preservation lesson, reused helpers, rejected the advice when a replacement-feed contract required clearing old annotations, and revised the method. Its final fresh session handled mixed source versions correctly. The trace followed the lesson into actual executable behavior and output.

| Continuation policy | Later tasks | Later task and feedback tokens |
|---|---:|---:|
| Ordinary with factual handoff | 3/3 | 598,124 |
| REL with factual handoff | 3/3 | 765,102 |
| REL with agent-created lessons | 3/3 | 972,228 |
| REL without episode history | 3/3 | 701,630 |

All arms retained code. Acquisition cost 247,972 tokens and used REL; this is a continuation comparison, not a full ordinary-from-scratch comparison. Subsequent artifacts diverged by policy. The learning cycle is observed, but every control also succeeded. A host-supplied documentation-path mistake affected twelve sessions; its prospective correction does not turn those errors into evidence of poor memory reasoning.

## 6. Observation memory: less rediscovery, not necessarily lower total cost

Study S4 removed the inherited-code shortcut. Two generated reporting-service sequences used empty output/helper locations in every session. Prior measurements of query routes were unavailable in shared code and current documentation. There were two acquisitions and six later tasks per policy, totaling 26 actual sessions. All policies retained identical access to current service behavior.

| Policy | Later tasks | Later query work | Later tokens |
|---|---:|---:|---:|
| Ordinary factual handoff | 6/6 | 1,101,500 | 713,384 |
| REL factual handoff | 6/6 | 1,136,900 | 1,108,706 |
| REL authored lessons | 6/6 | 1,185,700 | 1,588,998 |
| REL without episode history | 6/6 | 4,909,400 | 767,000 |

Query work is a conservative SQLite virtual-machine instruction upper bound, including probes and final execution. REL factual handoff used 76.8% less later query work than REL without history; ordinary handoff used 77.6% less. At matched factual handoff, adding REL increased later tokens by 55.4%. Charging the full two-task acquisition still left REL facts with 40.4% less query work than the no-history policy, but 107.9% more total tokens. Database work and total inference cost are distinct resources; the queries took fractions of a CPU second on this host.

When source revisions changed, workers measured new conditions and revised advice. Later workers reused unchanged-source measurements and selected routes correctly. That supports source-sensitive reuse. It does not establish that a general instruction layer was necessary: ordinary handoff and conventional nonmodel policies remain essential comparisons, recorded in Appendix K and the supplied S4 evidence summary.

## 7. Smaller context did not reliably reduce complete inference cost

Study S5 compared raw archives and deterministic compact observations under REL and ordinary work. Six fresh acquisition histories each fed four fresh later workers, totaling 30 sessions. All archives remained accessible; the compact table omitted result values but preserved request parameters, source revisions, cost and result identity. This is a lossy field projection with fallback, not semantic lossless compression.

All final tasks passed. Compact REL increased acquisition-inclusive total tokens by 9.5%, with reductions in only two of six later pairs. A post-run accounting diagnosis found 51 requests versus 42 for raw REL. Of 149,547 extra later tokens, 116,106 came from repeated initial context, 32,760 from subsequent input growth and 681 from output. Some workers reopened the raw archive for numerical verification; other extra requests occurred without a raw read. These observations do not identify a single complete behavioral cause. Cached input accounted for 145,792 of the token increase.

Study S6 tested a narrowly changed mechanism on six new constructed cases: restore exact historical numerical results while preserving the previous table fields, source revisions, raw fallback and verification instructions. Six acquisitions and 24 later sessions used four policies. Core REL stayed frozen.

| Later policy | Tasks | Requests | Total tokens | Uncached input + output |
|---|---:|---:|---:|---:|
| REL raw history | 6/6 | 39 | 871,285 | 153,461 |
| REL prior compact view | 6/6 | 47 | 1,021,888 | 128,192 |
| REL restored results | 6/6 | 41 | 805,136 | 146,704 |
| Ordinary restored results | 6/6 | 35 | 564,115 | 128,275 |

Charging the common acquisition to each alternative, restored REL versus prior compact REL reduced total tokens by 13.09% and query work by 10.59%, but increased uncached input plus output by 6.87%. It therefore failed the pinned adoption rule. Ordinary restored results used 16.74% fewer inclusive total tokens than restored REL, while using 11.61% more inclusive query work. This is a measured trade-off, not dominance by either policy across every resource.

The results do not justify another unchanged format comparison. A larger table can avoid a follow-up request; a shorter table can add work when it omits a value needed for verification. Complete cost depends on calls, repeated context, retrieval and verification behavior, not stored bytes alone. Cache allocation was observed rather than controlled, so uncached differences cannot be attributed solely to the display.

## 8. Real-use observations and the decision about REL itself

Private real-project observation provides ecological examples but not randomized effectiveness evidence. In one project, a preview wrapper supplied response-policy headers while a packaged error handler omitted them. Saved before/after receipts showed the correction on the actual handler without changing its error status. In another, a resource probe said block but a subsequent already-queued command ran tests. A later light validation coupled admission and action; the original failure remained recorded. Broader reject-path enforcement was not established by observation alone.

These examples motivate testing the actual changed boundary and the connection between a decision and its effect. Current REL already directs packaged-path checks, point-of-effect admission and blocked-work tests. The observed gaps therefore support enforcement and example review, not an automatic new mandatory rule. The shared core remains unchanged in this consolidation. The sharing drafts omit private project identities and content; the underlying observational receipts are not included in the reconstruction package.

## 9. From lessons to executable methods and working state

The brain-AI programme began with a cheap predictor, bounded working state, source-bound observation memory and slower evidence-driven updates. The useful engineering question became concrete: can an agent acquire a computation, carry its applicability conditions and state forward, and choose whether to reuse, observe, refine or rebuild? Biological analogy motivated this question but did not supply a mechanism or validation criterion.

The programme separates six mechanisms: working state (A1), acquired methods (A2), reusable computation (A3), useful information acquisition (A4), output-directed work (A5), and revision of the improvement procedure (A6). Source, context and version binding form an overlay (A7). These are research coordinates, not seven independently validated inventions. Run120 consolidates nine retained components into four typed families:

| Family | Working implementation | What must travel with it |
|---|---|---|
| Symbolic methods | Saved SQL, guards and current-context fields reused across changed reporting contracts | Table schema, identity rules, valid transformations and regression obligations |
| Numerical decisions | Learner-built primal-dual checker, solver continuation and selective input acquisition | Positive-curvature objective, feasible dual, linear output, input bounds and numerical allowance |
| Temporal graphs | Streaming/frontier methods, path or closure checks and saved state | Edge-time semantics, complete-graph assumptions, event identity and query obligations |
| Localization | Robust filter, two acquired update programs and pairwise equal means | Kinematics, sensor geometry, observation schema, map, time, initialization and reference roles |

The longer lifecycle in Run86 makes amortization observable. Across four chains with 16 reports each, both ordinary and REL learners acquired parameterized methods; all 60 later reports ran saved code with no new model call. Both achieved 32/32 reports per policy. Acquisition cost declined per delivered report, but REL retained a 26,475-token excess because both policies subsequently used zero model tokens. Adjacent source windows overlapped and every output had a trusted oracle; this is a measured development lifecycle, not 64 independent tasks.

Names such as state, memory or certificate do not make these interfaces interchangeable. A path witness establishes a graph fact; a primal-dual bound constrains an optimization output; neither certifies a robot's physical pose. Actual composition exists inside the numerical and localization families. Cross-family adapters and one complete learned architecture remain unqualified.

## 10. Component benefits survive strong controls, but not every stronger claim

Run106 used the UTIAS MR.CLAM range-and-bearing source [8] and executed eight native learner sessions that acquired and adapted arithmetic update graphs within a supplied EKF. On two later recorded sessions, joint-guidance methods had 12.47% lower mean squared position error than ordinary engineering learners. Both learner conditions used REL; this is not a REL-versus-no-REL effect. The best-performing conventional filter on the later results was robust soft weighting. Against that descriptive comparator, the acquired pair gained 5.77% in MSE but produced 16 versus 11 outputs above 0.5 m per 23,990-decision replay on average. The study's development-selected hard-rejection baseline transferred badly; its much larger relative improvement is retained in the original report rather than used alone to characterize benefit.

A within-method ablation is more directly informative about working state. Preserving the second joint learner's scalar reduced MSE by 2.42% versus resetting that scalar after every observation, with 14 versus 22 above-0.5 m outputs per 23,990-decision replay. Physical state and ordinary host smoothing remained in both paths. The first joint learner instead removed its earlier scalar during adaptation and achieved the lowest MSE. Retention was useful conditionally; these two learners do not establish an automatic memory-selection policy.

Run111 joined a saved numerical checker, continued solver state and requests for missing binary inputs from LIBSVM w8a [9], under the adapted positive-curvature hinge-SVM formulation [10]. A decision-aware ordinary acquisition policy used 28.73% fewer requests with 2.54% more measured arm wall time than the development-selected ordinary control. Both verified 382 of 384 distinct query decisions; the same two remained unresolved. Another ordinary control, alternate/progress, bought 564 fewer inputs than witness/progress, while witness/progress was 8.77% faster in recorded totals. Thus the 28.73% saving does not uniquely credit the witness schedule. The learner-built checker executed correctly but cost 100.30% more arm wall time than its equivalent direct formula. The target was the sign of a specified optimization output, not accuracy against dataset class labels. Input purchases were controlled reads, not measured physical sensing. Freshness referred to unused recorded task assignments within an already parsed corpus.

The direct test of added REL instructions in Run118 was a small four-session identity-adaptation pilot with the same saved code and factual handoff. Run118 used gpt-5.6-terra/medium with at most 12 calls, two evaluations and 300 seconds per session. Both ordinary sessions met the pinned complete contract; one of two REL sessions did. All four met the identity/provenance checks. The differing verdict concerned an ambiguous audit counting unit, not an observed wrong-person merge. REL used 3.63% more deployment tokens, one fewer tool call and 2.33% less recorded worker time. This one development-exposed task supports neither universal benefit nor universal harm.

Run119 kept observations and acquired programs fixed and compared robust output, acquired output and four readout rules. No rule met the predeclared requirement to preserve the full acquired MSE gain while reaching robust large-error counts. The following diagnostic summary gives each of six exposed recordings equal MSE weight and averages both acquired replicas:

| Output | Balanced MSE (m^2) | Outputs above 0.5 m | Episodes | Maximum error (m) |
|---|---:|---:|---:|---:|
| Robust | 0.04211678 | 920 | 36 | 2.118 |
| Acquired pair | 0.03705959 | 884 | 29.5 | 2.001 |
| Pairwise equal mean | 0.03774123 | 832.5 | 27.5 | 2.059 |

Counts refer to the same 47,970 distinct half-second endpoints; half-integers reflect replica averaging. They are not independent incident counts. The 0.5 m band is descriptive, not an operational safety requirement. Equal averaging improves MSE and above-band counts against robust, yet loses some acquired MSE gain and has per-recording harms. The reference package retains that optional trade-off; the failed joint qualification remains failed.

The Cartesian identity `error(mean)^2 = (error(r)^2 + error(j)^2)/2 - distance(r,j)^2/4` explains how complementary errors can improve the mean. It requires no independence assumption, but supplies neither a tail bound nor a calibrated fused covariance. The two filters also incur two execution costs. Recorded component-sum estimates were 28.97 seconds for robust, 30.62 for acquired and 56.42 for a robust-plus-acquired mean; these are accounting estimates, not independently timed deployments. Covariance, last innovation and disagreement did not establish a reliable causal harm detector in this study.

The procedure itself was tested in Run92: one model authored a revision from earlier evidence, then eight fresh learners compared it with the frozen procedure. All selected the same ordinary method, with identical later operations and outputs. The evolved condition used 20.12% more recorded tokens including revision cost; it was not promoted. In Run114, compatibility/failure-aware selection also failed its promotion criterion against ordinary synthesis and a diversity control. A later row-order counterexample exposed a defect despite the scored executions passing; the separately repaired code did not rewrite the original verdict. These results make the absence of an established procedure-level gain an experimental finding, not merely an untested ambition.

## 11. Transfer requires a contract, not just a saved program

A useful design description is a retained package `(method, state, contract, evidence, update rule)`. The contract specifies the admissible inputs and the consumer's obligation; evidence distinguishes arithmetic validity, source provenance and observed performance. Reuse is a decision under that contract. A violated assumption may require obtaining a missing fact, changing an observation model, rebuilding, or declining a result. This description organizes the existing components; it is not a newly proved algorithm or a self-enforcing host.

Run120 packages robust, two frozen acquired programs and two equal means behind a prediction interface that excludes scoring truth. Seventeen engineering checks passed after checkpoint mutation, invalid-resume boundaries and malformed-state handling were repaired. Fresh-process save/restart outputs agreed. These tests use constructed inputs; source declarations and hashes do not authenticate actual sensors or arbitrary checkpoint state. The package is a trusted fixed-record reference runner, not a validated live navigation service.

Run121 examined a genuinely different candidate: the AAU industrial AMR source [6]. Author material establishes multiple range-only UWB tags, three-dimensional sensor geometry, quasi-omnidirectional motion and LiDAR-derived pose/map reference. A range-only model can be derived, but missing bearings cannot be supplied from scoring truth. Sideways motion cannot be silently discarded, and calibration/reference dependencies must be assigned before evaluation. The README/configuration was inaccessible during this bounded review; exact clocks, geometry files, reference coverage and calibration/evaluation roles therefore remain unresolved. No raw recordings were decoded, and no empirical comparison was admitted. This is an access/qualification limit, not evidence that the dataset or range-only learning is ineffective.

This case changes the research action: consolidate evidence instead of extending the local threshold search. The preceding review of OpenAI mathematics artifacts [12] contributes ideas for conditional bounds and computational constructions; the Alien Space of Science review [13] motivates comparing distinct mechanisms rather than ranking proposal language alone. Neither makes a physical observation model interchangeable with a proof checker. A future experiment can test an explicitly adapted method once its source contract closes. It cannot call that adaptation confirmation of the unchanged range-and-bearing program.

## 12. Cost, limitations and reproducibility

Tokens include cached input, uncached input and output; cached input is a subset, not an additional charge. Reasoning-output counters are not added twice. Acquisition is charged to each alternative when judging deployment scenarios, but actual common acquisition is counted once in campaign totals. Feedback, failed recorded attempts and final execution belong to the declared worker boundary. Parent-model research, full engineering/human effort, monetary charges and physical energy remain incomplete or unknown. Tokens are not joules or prices, and overlapping worker durations are not elapsed campaign time.

The studies are small and clustered, with public or constructed tasks, known evaluators, limited models and hosts, and frequent final-accuracy ceilings. Conditions differ across studies and no pooled treatment effect is estimated. Some amendments corrected host, fixture or evaluator defects; preserved records distinguish them from scientific successes. A passing package check proves neither semantic correctness nor REL causation. A digest proves byte identity, not authorship or truth.

The review bundle includes this paper, an appendix, source-bound sanitized study summaries, original arithmetic inputs for S1/S2, an offline check of selected reported quantities, and the Run120 localization reference with constructed fixtures. It also includes the exact current 21-file REL core/support snapshot for readers to inspect, plus dependency and rights notes. The new verifier reconstructs the Run119 table from supplied trajectory-level metric summaries; it does not reread physical measurements or rerun original learners. It does not contain private conversations, full original model trajectories, credentials or a complete rerunnable native benchmark. Historical frozen study instructions and the supplied current skill are different objects. Full historical prompts, hosts and trajectories are absent; the current snapshot must not be used as a claimed reproduction of earlier treatments. The source repository baseline and current skill identity are recorded separately in the appendix; neither retroactively identifies every historical treatment. This public export preserves the study edition and records its separate package identity in VERSIONS.json. Earlier private delivery commits remain provenance markers, not public evidence endpoints.

## 13. Conclusion and next research decision

REL is usable as an evidence-oriented procedural skill. Agents have acquired methods, carried observations forward, revised advice and repaired real artifacts. Those achievements are not equivalent to demonstrating that the added procedure improves later work beyond equally informed ordinary agents. Our most useful empirical distinction is between information that saves rediscovery and procedure whose additional inference must earn its place.

The immediate choice is to preserve the stable core and the measured failures, not add rules or repeat comparisons until a desired result appears. Future REL effectiveness work needs a concrete remaining failure and fresh interdependent tasks, with ordinary handoff and direct reusable-method controls. The brain-AI programme now retains executable component families and an explicit source-transfer boundary. Run121 leaves numerical admission closed and delivers the consolidation. The v0.7 review checks the selected claims, reconstruction and package. This public edition invites reader criticism of the controls, applicability contracts and next discriminating experiment. Another empirical run requires resolved source geometry, clocks, reference dependencies and prospective data roles. The evidence supports scoped engineering reuse, with general architecture and procedure advantages still open.

## References

[1] Wang et al. Voyager: An Open-Ended Embodied Agent with Large Language Models. 2023. [arXiv](https://arxiv.org/abs/2305.16291)

[2] Shinn et al. Reflexion: Language Agents with Verbal Reinforcement Learning. 2023. [arXiv](https://arxiv.org/abs/2303.11366)

[3] Kapoor et al. AI Agents That Matter. 2024. [arXiv](https://arxiv.org/abs/2407.01502)

[4] He et al. Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks (MemoryArena), v2, 17 September 2026. [arXiv](https://arxiv.org/abs/2602.16313v2)

[5] Zhan et al. MemoryLake on MemoryArena: A Matched Study of Agent Memory Backends. 2026. [arXiv](https://arxiv.org/abs/2608.13883)

[6] AAU Control of Networked Systems. UWB Localization for an Industrial AMR, author dataset and licence page, inspected 5 November 2026. [Source](https://www.aau.at/en/smart-systems-technologies/control-of-networked-systems/datasets/uwb-localization-for-an-industrial-amr/). Exact source-paper and access coverage are supplied in the Run121 source review.

[7] Bai et al. Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds, v1, 18 October 2026. [arXiv](https://arxiv.org/abs/2610.25114v1).

[8] Leung et al. UTIAS Multi-Robot Cooperative Localization and Mapping Dataset (MR.CLAM). [Author dataset and format](https://asrl.utias.utoronto.ca/datasets/mrclam/).

[9] Chang and Lin. LIBSVM Data: Classification (Binary), w8a and other named source entries. [Author catalogue](https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html).

[10] OSQP authors. Support vector machine formulation and implementation example. [Official documentation](https://osqp.org/docs/examples/svm.html). Our positive diagonal curvature and output enclosure are specified in the internal derivation; the source example is not itself that checker.

[11] Genois et al. Contacts in a workplace; data associated with Network Science 3, 326 (2015). [SocioPatterns source](https://sociopatterns.org/datasets/contacts-in-a-workplace/). Additional graph sources and roles are identified in Appendix J.

[12] OpenAI. Mathematics release history, pinned source revision 4eaee87548250b2682affda7d05d947c05554bae. [History](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/history.md). Background review, not a new proof validation in this manuscript.

[13] Artiles et al. The Alien Space of Science: Sampling Coherent but Cognitively Unavailable Research Directions, v3, 21 October 2026. [Paper](https://arxiv.org/abs/2603.01092v3) and [reviewed repository revision](https://github.com/alejandrohdez00/alien-space-of-science/tree/39cbccc70cf9136f3a8009cd83a69a7bcde7107d). Mechanism-comparison motivation; no upstream result imported as REL evidence.

Internal studies S1-S6 and component studies C1-C9, their dates, version boundaries and reproducibility files are identified in EVIDENCE_APPENDIX.md. External sources motivate interpretation; none supplies REL result data.
