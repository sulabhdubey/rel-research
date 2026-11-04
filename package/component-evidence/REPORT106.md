# Run106 — acquired observation updates on recorded robot trajectories

Eight native learner sessions constructed, tested, saved and adapted executable update methods. On two later recorded sessions, the adapted joint-guidance group had **12.47% lower mean squared position error than ordinary engineering learners**. Against the best-performing conventional filter in the later results (`robust`), the gain was **5.77%**, with **16 versus 11 errors above 0.5 m per 23,990-decision replay on average**. That is an accuracy/risk trade-off, not dominance.

The pinned adoption conditions **passed**. The development-selected conventional control (`reject`) failed transfer badly, producing a much larger **99.79%** primary relative improvement. We preserve that result but do not use its unusually weak later behavior as the only headline. The strongest later conventional comparison is descriptive and was not used to select or retune a candidate. Advance the mechanism for further research; no operational deployment is authorized or demonstrated.

## What was built and tested

This run directly addresses Run105's missing-operation limitation. Learners construct arithmetic graphs for measurement covariance, motion uncertainty, bounded bias and rejection; they cannot merely select a filter name. The common EKF and its physical state are supplied engineering, not learner inventions. An acquired residual update is a narrower capability than learning an entire filter or brain-inspired architecture.

UTIAS MR.CLAM provides physical recordings of commands, camera-derived range/bearing and motion-capture reference. These are offline known-map replays, not live navigation. Five robots share each recording environment; timestamps are correlated. [non-public source: Research and source scope](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/RESEARCH.md), [non-public source: source-access amendment](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/SOURCE_ACCESS_AMENDMENT.md), [non-public source: plan](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/PLAN.md), [non-public source: frozen study](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/STUDY_DESIGN.md), [non-public source: manifest](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/MANIFEST.json).

Qualification used Dataset 1's first 600 seconds. Acquisition used Dataset 2's first 600 seconds and mean position MSE. Fresh adaptation sessions used Dataset 3's first 600 seconds and a changed consumer objective: MSE plus 0.1 times the fraction of errors above 0.5 m. Two native sequences per O and J, same model (`gpt-6.1-sol`, medium), full REL, inputs, feedback and allowances. Later Dataset 4 and occluded Dataset 9 each used first 1,200 seconds across all five robots: **23,990 unique time/robot decisions per policy**. The 0.5 m band is a declared descriptive threshold, not a safety criterion. Current pose reference is available only for common initialization and subsequent scoring.

## Results

The ordinary control was selected on adaptation data: **reject**. All eight conventional methods are reported, including stronger later outcomes if any; no final-data policy selection is used for the primary result. O is ordinary engineering; J emphasizes acquisition of method and required context. `acquire` means the frozen earlier method; `adapt` means the method after changed-consumer feedback. `no_candidate_state` resets only learner-authored scalars; ordinary host EMA helpers and physical state remain.

| Policy | Position RMSE (m) | Errors >0.5m | Timed replay seconds |
|---|---:|---:|---:|
| fixed | 0.1030 | 25 / 23,990 | 10.06 |
| low_R | 0.1119 | 39 / 23,990 | 9.99 |
| high_R | 0.1028 | 28 / 23,990 | 9.79 |
| robust | 0.0995 | 11 / 23,990 | 9.74 |
| reject | 2.1326 | 2,586 / 23,990 | 9.72 |
| adaptive | 0.1078 | 25 / 23,990 | 9.84 |
| adaptive_robust | 0.1059 | 12 / 23,990 | 9.90 |
| range_noise | 0.1010 | 28 / 23,990 | 9.82 |
| rep1-J-acquire | 0.1008 | 35 / 23,990 | 10.73 |
| rep1-J-acquire-no_candidate_state | 0.1024 | 36 / 23,990 | 10.75 |
| rep1-J-adapt | 0.0959 | 18 / 23,990 | 10.42 |
| rep1-J-adapt-no_candidate_state | 0.0959 | 18 / 23,990 | 10.44 |
| rep1-O-acquire | 0.0989 | 15 / 23,990 | 10.50 |
| rep1-O-adapt | 0.0999 | 19 / 23,990 | 10.59 |
| rep1-O-adapt-no_candidate_state | 0.0999 | 19 / 23,990 | 10.84 |
| rep2-J-acquire | 0.1028 | 39 / 23,990 | 11.02 |
| rep2-J-acquire-no_candidate_state | 0.1031 | 39 / 23,990 | 11.10 |
| rep2-J-adapt | 0.0973 | 14 / 23,990 | 10.96 |
| rep2-J-adapt-no_candidate_state | 0.0985 | 22 / 23,990 | 11.12 |
| rep2-O-acquire | 0.1053 | 54 / 23,990 | 10.80 |
| rep2-O-adapt | 0.1065 | 68 / 23,990 | 10.69 |
| rep2-O-adapt-no_candidate_state | 0.1065 | 68 / 23,990 | 10.75 |

The primary group MSE averages both adapted replicas: O=0.010660; J=0.009331. The preselected hard-rejection filter has divergent error on two Dataset 9 trajectories, with runs of 617 and 143 rejected measurements. This is consistent with a loss of recovery; it is a diagnostic association, not a separate causal test. [non-public source: Rejection diagnostic](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/REJECTION_DIAGNOSTIC.json). Bounded soft reweighting remains a stronger comparator. Both joint replicas improve over their own acquisition method on later MSE; both ordinary replicas worsen slightly after adaptation. Those paired observations are useful feasibility evidence, not a sufficiently replicated instruction-effect estimate. Per-recording group values and all adoption predicates are in [non-public source: DECISION.json](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/DECISION.json). There are two later recording units; we do not claim a population significance result from thousands of correlated timestamps. [non-public source: All per-robot results](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/RESULTS.json).

## What was actually learned and reused

- rep1 O: 6 → 6 arithmetic nodes; 0 → 0 retained scalars; numeric method changed: True.
- rep1 J: 15 → 5 arithmetic nodes; 1 → 0 retained scalars; numeric method changed: True.
- rep2 O: 4 → 4 arithmetic nodes; 0 → 0 retained scalars; numeric method changed: True.
- rep2 J: 14 → 14 arithmetic nodes; 1 → 1 retained scalars; numeric method changed: True.

This is actual executable construction and later invocation. All eight submissions matched their best-seen development objective. Several saved lessons still use proposal-style wording; exact method artifacts and measured feedback, rather than those sentences alone, define the usable handoff. Reset and semantic conditions were supplied in the task, so this is not evidence of discovering hidden context requirements. Conventional innovation reweighting and noise adaptation have prior art; compositions in this small language are not automatically new algorithms. Instruction effects are exploratory: both arms use REL, so this does not estimate REL versus no REL.

- rep1 O: adapted MSE 0.009984; resetting candidate state each observation 0.009984.
- rep1 J: adapted MSE 0.009202; resetting candidate state each observation 0.009202.
- rep2 O: adapted MSE 0.011336; resetting candidate state each observation 0.011336.
- rep2 J: adapted MSE 0.009459; resetting candidate state each observation 0.009695.

For the second joint learner, preserving its scalar working state reduced MSE by **2.42%** against resetting that scalar after every observation, with **14 versus 22** large errors. The first joint learner instead removed its earlier scalar during adaptation and achieved the lowest MSE. Memory is useful conditionally, not automatically.

The equal-helper check reuses the identical saved method without another model call and reproduces its output. This identifies a deployable artifact, not an ongoing workflow advantage over possessing that artifact. A separate child process restored complete physical/filter and method state exactly on a 60-second later prefix; changed-method binding was rejected. [non-public source: Restart receipt](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/restart/CHECK.json). This is one host/path, not broad recovery or portability qualification.

## Defects found and fixed

1. Two source copies disagree on landmark IDs 11 and 17. Qualification reference residuals consistently support the swapped mapping. The correction is common to all arms; raw source bytes remain unchanged. Another public mirror already contains it, so this is not a new public discovery. [non-public source: Source diagnostic](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/MAP_QUALIFICATION.json).
2. An unknown barcode initially stopped the parser. It is now quarantined and counted instead of guessed as a known landmark. Other-robot observations remain excluded.
3. The initial robust baseline used separate normalized coordinates rather than joint innovation covariance. The original qualification is preserved and the corrected controls rerun before the study freeze. Do not mistake this repair for learner improvement.
4. The first zero-inference native preflight hit the nested Windows sandbox's state-database permission restriction. A scoped preflight outside that nested boundary verified subscription login and disabled ambient tools. No inference occurred on the failed attempt; no uncertain model attempt was retried.
5. After Dataset4 completed, Dataset9's initial odometry order violated the loader's assumption: four robots each have one backwards step of approximately 0.1 seconds. The original loader stopped before Dataset9 scoring. A separately pinned stable source-time ordering repair preserves every row and file-order ties. Three additional tests verify unchanged earlier inputs, preserved rows and the intended rejection in the old loader. Dataset4 results and all learner methods remain untouched. The comparison resumed on Dataset9; this corrected same-data result is not an additional independent confirmation. [non-public source: Repair and costs](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/EVALUATOR_REPAIR.json).

## Verification and costs

527,780 derived policy/robot/time rows were recalculated from saved errors. Eleven core tests cover geometry, angle boundaries, covariance propagation, bounded expressions, causal inputs, constant-control equivalence, checkpoint restoration and invalid-method rejection; three more cover source ordering. Actual child-process recovery and direct helper reuse passed. [non-public source: Audit](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/AUDIT.json) is same-coordinator, same-data verification, not independent validation or a protected evaluator guarantee.

All eight native attempts and failed proposals are retained. Native token count: **1,311,364**, including cached input: O=650,181, J=661,183. Recorded stage durations sum to **1274.23s**; stages can overlap, so this is not elapsed turn time. Candidate evaluation is already inside native-attempt time and is not added twice. The aborted Dataset4 stage contributes its measured policy time; its loader/serialization/failure overhead is missing. Resumed Dataset9 CPU=59.73s; sampled resumed-process peak RSS=46.1MiB. [non-public source: Full accounting](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/acquired-observation-update/COSTS.json). Research/coordinator tokens and complete electricity costs remain unknown. No GPU or separately billed API was used.

## Delivery and REL decision

Raw third-party recordings, host configuration, private transport logs and account metadata remain local. The minimized private package includes frozen methods, derived outcomes, tests, provenance identities and a same-data verifier. Raw data must be separately acquired for numerical replay; this package does not claim source-origin authentication or redistribution rights.

The review applied existing REL source/control guidance; it found and corrected defects while preserving matched conditions. This observation does not isolate the skill's causal contribution. Update its evidence and the existing architecture programme; keep generic instructions stable unless a distinct missing invariant is demonstrated. The brain–AI result concerns learned operation/state behavior. Comparative REL effectiveness is a separate question.
