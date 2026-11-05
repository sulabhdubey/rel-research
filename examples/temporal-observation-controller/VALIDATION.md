# Validation and evidence scope

This source-free ordinary controller is the reusable software deliverable from Run123, 5 November 2026. It is a supplement; the v0.7.1 paper and package have not changed.

From this directory, with Python 3.10 or newer:

```sh
python -B demo.py
python -B -m unittest -v test_controller
python -B independent_checker.py --module-dir . --output controller-audit.json
```

The unit suite passed 20 tests, including 768 finite cases and a real child-process checkpoint restore. The separate checker uses explicit time-expanded graph reachability. Its checked version passed 12,680 constructed decisions and 409 checkpoint replays, along with strict-state, source-scope and callback-failure checks. These are dependent engineering cases, not independent empirical trials or evidence of a learning advantage. Running the checker writes the requested local JSON receipt and launches bounded child Python processes; it makes no network calls.

An initial independent-auditor fixture had unsorted same-time events. The controller correctly rejected it. Sorting that fixture fixed the audit without changing the controller; the original failed attempt remains in the private research record. This public checker is the corrected version.

The controller assumes truthful observations and accurate source version/completeness declarations. It does not authenticate sources, provide a security sandbox, or manage concurrent mutation. See the [full interface and limits](README.md). All examples are engineered; no raw participant data, credentials, local paths or original provider transcripts are included.

The separate source-qualification experiment is not distributed in this example. The code implements complete scope rejection, not selective cross-version metadata migration. No third-party dependencies, model access or data download are needed. Recorded local execution used Python 3.13.7. Python 3.10 is the syntax minimum; a multi-version compatibility matrix was not run.

Controller SHA-256: `b0f8f244303afb084aefdfc709eaf3135c8ef56fb5ad729b8b509341c0d9dd10`.
