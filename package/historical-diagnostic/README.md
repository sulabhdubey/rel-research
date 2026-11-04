# Nested annotation-scope diagnostic

This is a small, data-and-code evidence export from a **researcher-targeted post-outcome check**. All original E2/E3 study attempts had passed their prespecified sampled cases before source review identified the defect. These checks are not a fresh independent holdout and do not show that a learner or REL independently learned the repair.

- The same eight accepted/rejected cases were applied to all twelve frozen U methods. Eleven passed all eight. Method U03 (exported as original_pipeline.py) falsely accepted two cases and passed six.
- Child property names or array indices were merged into the parent instance's evaluated-location set, allowing a later invalid sibling to be skipped. Reversed-order rejection and valid-value controls are included.
- The separate two-line repair removes only the child-instance annotation merge at the two unevaluated-value boundaries. It passes 8/8 diagnostics, 76/76 original E2 checks, and 89/89 original E3 checks. The original method and original study scores remain unchanged.
- Independent expected answers were verified with jsonschema 4.26.0, remote retrieval forbidden. Candidate execution used the existing offline, read-only, non-root, resource-limited guest. Fifteen completed guest checks are described in results.json; this is not fifteen independent trials.

## Contents

- cases.json: eight investigator-authored static inputs and expected Boolean answers.
- original_pipeline.py and repaired_pipeline.py: exact failing frozen method and separate repaired bytes.
- repair.diff: minimal human-readable difference.
- results.json: anonymized method IDs, original diagnostic observations, code hashes and scoped repair results.
- MANIFEST.sha256: exported-file identity, not a claim of correctness.

Review these files without executing them. A replay must use an appropriately isolated offline runner; this export does not provide or qualify a sandbox. The full E2/E3 fixture corpus and harness are deliberately not duplicated here, so those two recheck totals cannot be independently reproduced from this small export alone. Original case-source provenance remains in the study evidence.

The eight new cases are investigator-authored; the two Python files are study-generated validator artifacts, not copied source from the upstream test-suite repository. The mathematical/JSON Schema semantics are shared subject matter. This note makes no separate licensing or production-readiness claim for a validator implementation.
