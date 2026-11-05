# Brain-inspired questions, measurable engineering

**Research direction:** combine cheap prediction, temporary working state, stored observations and slower revision—then measure when each is useful.

The neuroscience discussion encouraged a system with multiple timescales. It did not establish that an artificial component reproduces a biological mechanism. The engineering question became whether a small amount of useful state can reduce repeated work while preserving correct decisions after conditions change.

## The proposed design and its test

The initial synthesis combined a cheap predictor, a calibrated gate to expensive reasoning, short-lived working state, source-bound observations and slower updates when evidence persists. Each component introduces a cost and a failure mode.

For example, let a gate cost `G`, an expensive computation cost `E`, and escalation occur with fraction `p`. If the cheap computation is already paid in both alternatives, the gated route saves computation only when `G + pE < E`. That arithmetic is useful, but incomplete: the gate may miss rare consequential cases. Cost and error must be evaluated together.

A memory store similarly pays back only when later avoided work exceeds acquisition, storage, retrieval, checking and maintenance. A short sequence can reveal the overhead without showing its eventual amortization; a promised future payoff is not a measured payoff.

## What survived the experiments

Some observation histories and reusable states helped within their tested contracts. Other added mechanisms lost to ordinary persistence, direct current-state access, efficient recomputation or conventional filtering. The retained [component map](../package/component-evidence/COMPONENT_MAP.md) separates SQL, numerical, temporal-graph and localization families rather than presenting them as one integrated brain-like architecture.

In localization, a learner-acquired update had a better average error than a stronger ordinary robust comparator on the reported recordings, but more large errors. Combining both histories by ordinary averaging changed that trade-off again. This is useful evidence about estimator behavior—not dominance on every consumer's objective. [Reported comparison](../package/component-evidence/REPORT119.md).

## What “efficient” must mean

Token counts, database work, elapsed time and joules describe different quantities. GPU temperature is not an energy measurement. Local work excludes remote inference unless that cost is separately recorded. The programme has not demonstrated whole-system energy savings or human-brain energy parity.

The next architectural claim needs a consumer contract: what must be correct, what can remain unresolved, what large errors cost, and what resources are included. Biology supplies questions; the system's measured behavior must supply the answer.

[Executable components](06-executable-learning.md) · [Measurement lessons](08-failures-and-measurement.md) · [Back to the atlas](README.md)
