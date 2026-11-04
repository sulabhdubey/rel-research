# Run121 — AAU source qualification

Reviewed 5 November 2026 IST using the installed Recursive Evidence Loop and Run120's source handoff. **NOT ADMITTED for numerical comparison.** The author paper supplies useful model and provenance facts, but the exact recording contract could not be established. This is a bounded admission outcome, not a finding that the dataset is unusable.

## Established author information

The [official dataset page](https://www.aau.at/en/smart-systems-technologies/control-of-networked-systems/datasets/uwb-localization-for-an-industrial-amr/) advertises 13 trajectories, three vehicle tags, twelve anchors, wheel/body-motion inputs, ranges, LiDAR-derived poses and configuration files. Its indexed current text declares AGILOX copyright and CC BY-NC-SA 4.0, permitting attributed noncommercial research/adaptation with share-alike obligations; commercial use needs written permission. No dataset bytes were redistributed.

The directly associated [author paper, arXiv2607.15807v2](https://arxiv.org/html/2607.15807v2), has these relevant facts: the vehicle is quasi-omnidirectional; tag offsets and anchor locations are three-dimensional. A scalar range model incorporates pairwise affine biases and calibration uncertainty. Onboard LiDAR supplies pose reference; its static map supplies anchor truth. Calibration uses pose priors on an indoor trajectory, then transfers outdoors. These facts require a declared motion/observation adaptation and dependent-reference interpretation. They do not prohibit a fair comparison. Version2, revised3 August2026, reports unchanged content apart from a robot figure. Sections IV–V were inspected, including published results encountered while establishing reference and calibration roles.

## Admission matrix

| Requirement | State | What must still be established |
|---|---|---|
| Identified range sensor family | Established at author-description level | Exact recording field names, units, invalid-value conventions and measurement timestamps. |
| Tag/anchor geometry | Configurations advertised; mathematical roles described | Numeric tag offsets, coordinate origins/axes, installation uncertainty and exact file provenance. |
| Motion input | Body motion advertised; model needs lateral motion | Wheel/body velocity schema, timestamp clock, sign/frame and interpolation convention. |
| Synchronization | Unresolved | Sensor clocks, offset treatment, latency and whether times represent measurement or receipt. |
| Scoring reference | Production modality described | Exact pose schema, temporal coverage, accuracy bounds, odometry contribution and unavailable-reference handling. |
| Calibration/evaluation separation | A qualitative calibration-to-transfer procedure is described | Recording identifiers, calibration file lineage, all13 recording roles and disjoint development/confirmation assignment. |
| Initialization | Pose-prior concept described | Reproducible initial-pose source and allowance shared by every comparator. |
| Rights | Current author indexed declaration available | Recheck terms before changed use/acquisition; retain attribution and applicable adaptation obligations. |

The mathematical observation model is not a CSV specification. A stated LiDAR reference is not proof of independence from all model inputs; shared map provenance does not, by itself, prove leakage. The unresolved boundary is whether role-limited inputs and scoring can actually be implemented from identified records without inventing missing semantics. A schema-only or metadata-only validation would not establish raw quality, coverage or an empirical performance difference.

## Access and exposure

- Direct author-page retrieval timed out twice; its current indexed author text was returned by targeted searches.
- The official README URL was inaccessible to the web reader. A normal managed-shell HTTPS request failed DNS. One approved scoped network request then failed connection establishment. No approval-review rejection occurred; no README content was obtained.
- The paper's arXiv abstract/version record and HTML were accessible. Initial retrieval covered methods; a continuation exposed the setup/evaluation sections and published numeric tables. Those tables are literature exposure, not fresh evaluation data. They were not transcribed into proposed thresholds.
- Exact-title/source searches returned unrelated snippets, including other UWB datasets and published results. Those were not opened or adopted. No further dataset family was screened and no broad search followed the admission failure.
- No archive was downloaded, no raw recording decoded, no upstream code run, no model trained or compared, and no author contacted. The archive size advertised on the author page is500MB; its transport and contents were not probed.

## Decision and transferable finding

Follow the pinned fallback: consolidate the existing paper and component evidence. A new range-only prototype would otherwise require assumptions that the planned comparison cannot yet audit. In particular, dropping lateral velocity, flattening sensor geometry, inventing bearings or deriving online measurements from scoring reference would change the task while concealing the missing contract.

The useful retained lesson is to check both the observation model and the motion/reference/calibration lineage when changing sensors. REL already requires semantic adapter checks, independent evidence roles and fair controls; this review alone does not justify a new mandatory core rule or establish REL's causal performance benefit.

Reopen only when the official README/configuration inventory or an equivalent author-supplied contract resolves the listed fields and permits a prospective split. At that point compare a source-appropriate conventional robust/bias-aware range filter with the explicit learned adaptation and equally informed averaging. Preserve the published-paper exposure and do not label the old range-bearing methods unchanged. No new threshold sweep or model-worker call is admitted now.

The accompanying JSON records exact sources, access attempts and remaining fields. It is a source review, not an exhaustive host exposure audit or independent replication.
