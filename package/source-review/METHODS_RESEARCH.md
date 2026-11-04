# Run121 methods research and range-only transfer contract

Reviewed 5 November 2026 IST. This is a prospective methods appendix, not an executed AAU experiment. No new recording, upstream executable, training job or experimental model call was used. The current installed Recursive Evidence Loop, Run119 report, Run120 frozen numerical loop, graph interpreter and both acquired graphs were read. The source qualification and empirical admission decision belong to the parent study.

## Decision supported by the research

Range-only adaptation is scientifically meaningful, but it changes the observation model and the acquired programme's feature semantics. The strong ordinary comparison must include a robust innovation-weighted range filter with the same motion, geometry, timestamps, initialization and development access. Simply removing bearing from the arrays and reusing the old method identifier would be an invalid transfer. A scalar update also cannot manufacture information that the sensors never measured.

Current literature supplies relevant mechanisms and cautions. None establishes transfer of our retained programs or resolves AAU's source contract.

| Primary source and version | Read scope and decision-relevant finding | Consequence for Run121 |
|---|---|---|
| [KD-EKF](https://arxiv.org/html/2603.18027v1), arXiv:2603.18027v1, 6 March 2026 | Read system design sections 3.1–3.4, Algorithm 1 and evaluation setup 4.1, plus abstract/version metadata. A frozen LLaMA teacher supervises a smaller student; disagreement with UWB-derived positions scales covariance through a median/MAD window. The EKF fuses trilaterated positions with pedestrian dead reckoning, rather than directly updating scalar ranges. Evaluation uses server hardware, manually measured reference points/distances and a shared post-processing step. Fixed-covariance comparisons do not settle our strong-robust-control question. The source does not fully establish trajectory-separated train/test assignment in the inspected description. | A predictor-derived reliability cue is a candidate, not a source of geometric truth. Preserve distillation, preprocessing and inference costs; require an explicit causal post-processing rule and recording-separated roles. No claim that a billion-parameter student is an appropriate lightweight baseline for this task. |
| [Adaptive Robot Localization with Ultra-wideband Novelty Detection](https://arxiv.org/html/2505.05903v1), arXiv:2505.05903v1, 9 May 2025 | Read methodology sections 3.1–3.4 and experimental setup/comparison sections 4.1–4.3. An autoencoder trained on nominal ranges maps reconstruction errors to covariance and bias. Crucially, section 3.4 fits the bias map using Vicon-derived ranges: unsupervised novelty training does not make the complete estimator reference-free. Nine changed scenes remain one laboratory context. The principal comparator is a static-covariance EKF. Some displayed equations have apparent typographical inconsistencies, so the numerical implementation must be independently derived. | If transferring the idea, separate nominal training, reference-dependent calibration and scoring roles. Compare against robust ordinary filtering, not just a fixed weak covariance. Novelty can reflect changed location or geometry as well as corrupted measurements; correct classification does not alone establish better state estimates. |
| [A Tightly Coupled Fusion Method of UWB and IMU for Indoor Positioning](https://www.mdpi.com/2079-9292/15/21/5076), Electronics 15(21):5076, published 2 November 2026, DOI 10.3390/electronics15215076 | Direct page opens failed. The search service returned a substantial indexed publisher extract: preprocessing, coordinate model, scalar-range geometry, Huber weighting, time matching, comparisons and ablations. It combines calibration, innovation-dependent weights, covariance adaptation and outlier rejection. The extract discusses vertical range correction and rejecting temporally unmatched fusion blocks. Full article/figures/code were not independently recovered or reproduced. | Supports robust weighting and calibrated geometry as ordinary control requirements. It does not justify copying reported thresholds into AAU or declaring this paper's estimator independently reproduced. Its comparisons do not qualify our unseen-data claim. |

Literature refresh was targeted to range-only robust versus acquired updates, including the recent November paper. Searches also returned unrelated or secondary results; these were not relied on. Access date is not a paper's publication date. Published result snippets were exposed, but no AAU outcomes or raw arrays were read here.

## Derived range-only observation model

This derivation is independent algebra for the proposed interface; it is not taken from an AAU file whose geometry has yet to qualify.

Let the planar body pose be `s = (px, py, theta)`. Let tag `j` have fixed body-frame lever arm `(lx_j, ly_j, lz_j)` and the body's reference height be `z0`. Let anchor `i` have surveyed world coordinates `(ax_i, ay_i, az_i)`. Assume negligible roll/pitch; if that is not justified, the three-state model is not adequate without an explicit additional orientation/uncertainty treatment.

```
tx = px + cos(theta)*lx - sin(theta)*ly
ty = py + sin(theta)*lx + cos(theta)*ly
tz = z0 + lz
dx = tx - ax;  dy = ty - ay;  dz = tz - az
h(s,i,j) = sqrt(dx*dx + dy*dy + dz*dz)

H = [dx/h,
     dy/h,
     (dx*(-sin(theta)*lx-cos(theta)*ly)
      +dy*(cos(theta)*lx-sin(theta)*ly))/h]
```

`H` is the 1-by-3 Jacobian evaluated at the predicted state. The coincident-anchor/tag case `h=0` has no ordinary Euclidean-distance derivative; it needs a declared rejection or distinct treatment, not a hidden epsilon that claims physical validity. A center-mounted tag has no direct heading derivative. An offset tag can constrain heading jointly with geometry, but one instantaneous scalar range does not determine the entire pose. Multiple tags/anchors do not automatically yield independent errors or full observability in every layout.

Keep measured slant distance in this model rather than projecting it to a 2D distance unless height and the induced noise distribution are explicitly handled. For covariance `P`, measured range `r`, calibrated range bias `b` and variance `R>0`:

```
e = r - b - h(s)
S = H P H^T + R
z = e^2 / S
K = P H^T / S
s_new = s + K e
P_new = (I-KH) P (I-KH)^T + K R K^T
```

Wrap heading after correction. The Joseph covariance expression is a numerical stability choice, not a guarantee that the stochastic model is calibrated. Sensor lever arms, map frame and clock alignment must be established from source records. Estimating them from confirmation pose truth would invalidate the intended independent test.

The subsequently inspected [AAU author paper, section IV-C](https://arxiv.org/html/2607.15807v2), models raw range as `gamma_ij*h(s,i,j) + beta_ij`, with pairwise scale and offset calibration. For that model the residual is `e = r - gamma*h - beta` and the core-state Jacobian is `gamma*H`; the equations above are the unit-scale special case. Calibration uncertainty and core/calibration dependence must be represented consistently rather than counted as independent measurement noise without justification. Section IV-B also uses a terrain surface model; fixed height and yaw-only orientation are conditional simplifications, not an exact reproduction of its estimator. Section V-A establishes quasi-omnidirectional motion, so a prospective AAU adapter must retain lateral motion where provided. This limited follow-up read covered sections IV-B/IV-C and V-A setup; no source arrays were accessed.

If the robot supplies lateral body velocity, its motion must use an SE(2) twist with both forward and lateral components. The current frozen unicycle propagation cannot silently discard lateral velocity. Controls must be measured odometry, not differentiated scoring poses. Asynchronous ranges must be processed at their measured times; pairing future ranges into an apparent simultaneous multitag observation changes available information. Correlated same-epoch observations require a justified joint covariance or an explicit approximation, not an unsupported independence assertion.

## Ordinary controls and fair adaptation

A strong bounded ordinary family consists of a calibrated scalar range EKF, robust innovation weighting, and an adaptive-covariance variant if its calibration is supportable. A concrete Huber-inspired one-step option is `u=e/sqrt(S)`, `w=min(1,c/abs(u))` with `w=1` at zero residual, followed by `R_effective=R/w` and a recomputed gain. This is a specified influence-limiting approximation, not a claim to reproduce a named iterative M-estimator. A hard-rejection variant may be retained if development justifies it. No numerical threshold, noise constant, window size or winner is selected in this appendix.

All controls need the same measured observations, source geometry, initialization, state dimension, motion model, calibration examples and permitted feedback. Calibrate on assigned recordings, choose on development recordings and evaluate once on reserved recordings; do not random-split dependent endpoints. Include a fixed tuned covariance as a diagnostic, but it cannot stand in for the strong robust ordinary control. A learned rule using extra history/metadata requires the equally informed ordinary alternative to receive those inputs too.

The candidate comparison should initially hold observations fixed and measure recording-level mean squared position error, large-error frequency/duration, per-recording regressions, divergence, missing-output coverage and total execution/acquisition costs. Operational large-error tolerance must come from a declared consumer requirement or remain a descriptive error-distribution statistic. The old 0.5 m band cannot silently become an industrial safety threshold.

Position averaging is an ordinary additional readout with actual shared execution costs. Its errors are correlated because the estimators consume the same sensors; no independent-variance or calibrated confidence claim follows. Heading averaging needs explicit behavior for antipodal directions. There is no reason to add another learned selector before a source-qualified comparison exposes a residual decision gap.

## What the retained programs actually contain

The inspected source is `outputs/brain-ai-run120-component-source-qualification-2026-11-04/reference/rel_localization/`. J1 and J2 are bounded acquired scalar computation graphs, not neural networks trained on AAU.

| Retained object | Exact behavior relevant to adaptation | Required handling |
|---|---|---|
| Frozen observation loop | Two-dimensional `(range,bearing)` innovation, origin-mounted planar landmark model, 2-by-3 Jacobian; fixed range/bearing noise formula; joint NIS; unicycle motion. | Replace under a new source-specific range-only contract. Keep original immutable. The old range-dependent noise constants are not an AAU calibration. |
| J1 | Range scale `4*clip(zr,1,25)`; independent bearing scale `clip(zb,1,100)`; constant process scales, zero biases, no rejection/state. | Its range branch can form an explicitly named scalar projection candidate. Remove unreachable bearing branch/output under a new contract. This is adapted reuse, not execution of the unchanged two-channel program. |
| J2 | Range scale `6*clip(zr/16,1,8)`; separate bearing branch. A retained `m0` tracks clipped joint NIS using `clip(dt/3,0,1)`. Process scales use the previous `m0` clipped to `[1,3]`. | Scalar innovation energy has a different calibration from the old two-channel NIS; substituting it changes the retained state's meaning. Specify whether to retire that state, recalibrate its rule on training data, or acquire a new rule. Do not fill missing bearing inputs with zeros. |
| Graph interpreter | Requires `range-bearing-v1`, validates all seven output fields and includes bearing inputs. | A new range-only version must reject unsupported input/output fields and old checkpoints. Merely accepting the old version while ignoring outputs would hide semantic drift. |

The mechanistic question is therefore whether a method learned for one sensor model can be usefully adapted once the exact information contract changes. The correct rejection of incompatible state is part of this test, not a missing-value nuisance to conceal.

## Admission and REL consequence

The next empirical decision requires the source team's documented geometry, timing, calibration/reference provenance, available archive/schema, licence and recording roles. This methods appendix does not override an unresolved prerequisite. If those cannot be resolved, retain it as a future adaptation specification and consolidate the paper as authorized; do not substitute synthetic physical evidence.

No new generic REL instruction is recommended from this review. Existing source/claim, operational-adapter and fair-information rules already require the changes described above. The applied lesson is concrete: a saved method's executable feature definitions, not its prose lesson name, determine whether reuse is valid.

Costs: this subtask used coordinator/subagent reading, primary web retrieval and local source inspection; no empirical filter execution, training, GPU run or paid provider API was invoked. Full model-token and wall-energy accounting is unavailable. Literature/source-derived evidence is not a new AAU performance result.
