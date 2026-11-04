# Frozen localization reference

This runnable example bundles our retained robust filter, both acquired arithmetic programs, their two equal means, and separate scoring. The included fixture is constructed for engineering checks; it is not a physical benchmark or evidence of improvement.

Verified environment: Windows, Python3.13.7, NumPy2.4.6. Other hosts/versions have not been qualified. Using an existing Python environment with NumPy, run from this folder:

```text
python -B example.py
python -B test_reference.py
```

The commands use no network, model provider, credentials, raw dataset or GPU. `requirements.txt` records the tested dependency; no dependency is installed automatically. Prediction returns robust, J1, J2, J1-mean and J2-mean poses plus three continuation states and measured work. The shared robust path is executed once; a deployed mean still needs both full filters. The frozen programs are research methods, not a newly trained model.

Input contract: `planar-range-bearing-v1`; seconds, metres and radians; unicycle forward/angular velocity with initial control available at time zero; causal observed landmark IDs, range and bearing; independently available fixed2D map; supplied starting pose. Metadata declarations are not provenance proof. An actual source adapter must verify frames, calibration, timing, identities, map availability and reference roles. No adapter or fresh dataset is bundled.

Prediction rejects evaluation truth as an input. `evaluate()` accepts reference separately and rejects missing time support. Span coverage alone does not qualify interpolation gaps or reference accuracy. The0.5m threshold is descriptive.

Continuation requires the same complete bound input record and trusted, unaltered checkpoints for all three filters at the same saved time. Saved snapshots are copied before resume. Input/method binding detects changed records/methods but does not authenticate state contents. This is a reference replay component, not a live streaming, safety-qualified or general agent-host service. Historical implementation and source hashes are in the parent build/map records; test failures remain in the parent evidence.
