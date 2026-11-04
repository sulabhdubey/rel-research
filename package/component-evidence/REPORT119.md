# Run119 — lower average error does not establish reliable large-error protection

Public reader note: the [bundled saved-metric export](RESULTS119.json) supports the advertised table reconstruction. The pinned original sources below remain non-public.

Completed 4 November 2026. [non-public source: Pinned plan](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/tail-risk-qualification/PLAN.md) · [non-public source: Research](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/tail-risk-qualification/RESEARCH.md) · [non-public source: Source exposure](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/tail-risk-qualification/EXPOSURE_AUDIT.md) · [non-public source: Results](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/tail-risk-qualification/RESULTS.json) · [non-public source: Independent audit](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/tail-risk-qualification/INDEPENDENT_RESULT_AUDIT.md) · [non-public source: Costs](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/tail-risk-qualification/COSTS.json) · [non-public source: Next decision](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/tail-risk-qualification/NEXT_RUN.md).

**No readout qualified to preserve the full acquired average-error gain and meet the robust large-error count. Across six exposed diagnostic recordings, equal averaging had 10.39% lower recording-balanced MSE and 9.51% fewer above-0.5m outputs than robust, but MSE was 1.84% higher than the acquired pair.** This is a completed numerical qualification of previously acquired methods. No new frontier-model worker ran. The fixed observation streams, learned programs and ordinary robust filter remained unchanged.

## What was actually executed

Forty robot-recording trajectories across eight MR.CLAM recordings, 120 filter runs and 59,960 distinct half-second endpoints. Dataset2 calibrated one disagreement threshold per retained learner without pose labels; Dataset3 selected among four fixed readouts. The six later diagnostic recordings contain47,970 distinct endpoints, repeated across11 output policies rather than independent tasks. Both learned replicas remain in every group result. Original Dataset4/9 errors matched within 1e-12 for all 30 component trajectories/replicas and complete saved error series, with exact above-band counts.

Readouts compare ordinary equal averaging, smaller position covariance, last pre-inflation NIS and normalized disagreement. Both causal filter states continue updating even when unused. Position covariance is in m²; heading variance is excluded. The position-mean identity was checked at every derived endpoint. This is output combination across histories, not a same-prior causal update experiment, a new learned updater or a REL efficacy comparison.

All MR.CLAM streams had been decoded by earlier loaders before prefix selection. These new readouts are therefore **exposed-source exploratory evidence**, not independent confirmation. The separate LSY trial4 was not opened. Raw recording/pose/reference arrays stay local.

## Development decision

No family qualified on Dataset3. The frozen acquired group had MSE0.00835249m² and17 average above-band outputs; robust had0.00981175m² and22. Every added readout raised acquired-group MSE. The NIS difference was small but exceeded the predeclared rounding tolerance. No policy was selected after inspecting the later results. Missing a selection criterion is not evidence that every component is useless or that all later recordings worsened.

The criterion to preserve the acquired group's *full* MSE gain is stronger than merely remaining better than robust. It was pinned before results and is retained. The descriptive results below also answer the weaker, practically relevant trade-off question without silently changing that criterion.

## Six-recording diagnostic summary

MSE gives each recording equal weight and each learned replica equal weight. Counts sum actual half-second outputs over the same47,970 endpoints and average the two replicas; half-integers are averages, not fractional incidents. Episodes are contiguous above-band samples, not independent accidents. The0.5m band is historical and descriptive, not an operating safety specification.

| Output | Recording-balanced MSE (m²) | Above0.5m outputs | Episodes | Maximum error (m) |
|---|---:|---:|---:|---:|
| robust | 0.04211678 | 920 | 36 | 2.118 |
| acquired | 0.03705959 | 884 | 29.5 | 2.001 |
| mean | 0.03774123 | 832.5 | 27.5 | 2.059 |
| covariance | 0.04211678 | 920 | 36 | 2.118 |
| nis | 0.03690401 | 888.5 | 30 | 2.001 |
| disagreement | 0.03885181 | 895 | 38 | 2.001 |

The acquired pair itself improved balanced MSE by12.01% versus robust, with884 versus920 above-band outputs. Thus the original excess-tail trade-off is **not universal** across recordings. Equal averaging gives a reasonable descriptive middle ground:832.5 above-band outputs, compared with884 acquired and920 robust, at1.84% higher MSE than acquired. Its mechanism is ordinary averaging. It does not erase per-recording harms: its group above-band count is55 versus robust56 in Dataset8, but its mean-with-replica2 readout has66; in Dataset9 its group count12.5 exceeds robust11.

The old Dataset4/9 gap specifically remains:

| Output | MSE (m²) | Above0.5m outputs per replica |
|---|---:|---:|
| robust | 0.00990213 | 11 |
| acquired | 0.00933067 | 16 |
| mean | 0.00916185 | 12.5 |
| covariance | 0.00990213 | 11 |
| nis | 0.00931229 | 15.5 |
| disagreement | 0.00958653 | 14.5 |

Equal averaging reduces the acquired count from16 to12.5 and slightly improves MSE there, but still misses robust's11. The lower-covariance selector matches robust's reported error metrics, choosing robust on 95,466 of 95,940 replica-endpoints (99.51%); it preserves no acquired-group mean gain. Reported covariance ranking here reflects the different update/noise constructions and does not establish which output is more accurate.

## Why the switches did not solve the problem

Across both replicas there were274 acquired-above0.5m/robust-not-above0.5m endpoints. NIS flagged157 endpoints and caught7 of those274. Disagreement flagged7,647 and caught133, but6,091 flags selected robust when the acquired output was more accurate. These are endpoint counts, not independent statistical trials. Full four-way risk counts, misses, false-fallback denominators and lost squared-error benefit are retained in [non-public source: RESULTS.json](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/tail-risk-qualification/RESULTS.json).

NIS is the last measured innovation, held through gaps; before any measurement its zero sentinel is unflagged. Age is retained. A low innovation or smaller internal covariance is not a certificate of current state accuracy. Normalized disagreement omits error cross-covariance, so it is a heuristic rather than a calibrated variance. No pose truth, future observation or offline harm label enters a readout.

## Cost and verification

The capture worker took110.10s wall and108.52s CPU, with57.4MiB sampled peak RSS. Known instrumented capture/selection/diagnostic/test/audit work totals113.02s; [non-public source: COSTS.json](https://github.com/sulabhdubey/recursive-evidence-loop/blob/e775ee8b68a2db210641768024e9bdae3384dac0/examples/tail-risk-qualification/COSTS.json) enumerates scope and unknown work. Added native-worker calls/tokens are0; coordinator/research/review model costs are not zero or fully known. Historical1,311,364 Run106 worker tokens are not new expenditure. No whole-laptop or remote inference energy was measured.

On the six diagnostic recordings, component-sum accounting estimates are28.97s robust,30.62s acquired and56.42s per robust+acquired mean bank. These are **accounting estimates**, not separately timed deployments or sums to add across all11 readouts. No extra deployment benchmark was admitted because no family passed development.

Thirteen source-free tests pass, covering unchanged numerical updates, future-input/reference isolation, restart continuity, units, ties, invalid state, mean identity and risk accounting. The first test harness attempt failed because it imported the wrong module and overrestricted a NumPy platform query; both errors were repaired before release, with all receipts retained. All189 released file identities were verified before and after capture. The independent result audit checks saved causal outputs and arithmetic; it is not another data collection or independent external replication.

## Decision and programme consequence

Close this four-readout qualification without a new model comparison, threshold sweep or post hoc replica selection. Retain the frozen robust and acquired methods and ordinary averaging as a **documented optional trade-off**, not a promoted reliability solution. Neither the numerical selection nor fresh-confirmation admission passed. A failed joint qualification does not erase the measured average improvements.

Retain acquired methods/state (85/102/103/106), selective information acquisition111, ordinary incremental maintenance112 and temporal validity113/115. Run104 already integrated decisions with unresolved trade-offs. Run119 adds a different representation—two causal state histories plus ordinary output combination—and preserves a useful averaging trade-off, while finding that these fixed innovation/covariance readouts did not qualify here. Mathematics supplies an exact complementarity identity; it does not remove correlated-error or source assumptions. No new generic REL rule or complete learned-architecture advantage follows. Eleven material cycles now lack full architecture advantage; the next programme action consolidates usable components and qualifies independent evidence instead of another local gate variant.

Run120 should consolidate the retained architecture components and evidence into one current executable/reference map, then qualify an independent numerical confirmation source for the frozen robust, acquired and equal-mean outputs. No further threshold or learned-selector sweep on MR.CLAM. Pin the consumer's permitted average/tail trade-off and source exposure before opening new outcomes; only then decide whether a model comparison is needed.
