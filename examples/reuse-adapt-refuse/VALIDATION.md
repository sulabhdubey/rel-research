# What is checked in this walkthrough?

Checked 5 November 2026. Example version 1.0, a separate supplement to the unchanged report (study edition v0.7) and public package v0.7.1.

| Check | Scope and result |
|---|---|
| `python -B demo.py` | Three constructed decisions: reuse gives 30 Wh; calibration-aware execution gives 51.5 Wh; exact partial-window energy is refused with a conditional 0-30 Wh range using the original uncalibrated totals |
| `python -B -m unittest test_walkthrough test_runtime_portability -v` | 23 tests pass: 22 walkthrough checks plus one optional-API compatibility regression |
| `python -B independent_checks.py` | Nine separately authored arithmetic/boundary checks pass; imports the implementation but not its test/reference helpers |
| Historical payloads | `methods.json` is unchanged from the reviewed Run125 bundle; SQL hashes are recorded in `PROVENANCE.json` |
| Public runtime change | One constructor guard tolerates absence of Python's optional extension-loading API; existing-API errors are not caught; the SQL function allowlist remains unchanged |
| File identity | `SHA256SUMS` identifies this example's files, excluding the checksum file itself |

These are engineering checks on constructed cases, not independent empirical trials, external-user validation or proof that REL beats ordinary engineering. The ordinary non-SQL reference receives the same facts and requirements. Timings printed by the commands cover their own local execution, not the full research or model-acquisition cost.

## Why the correction matters

The first version passed 19 tests but checked overlap only among bins intersecting the requested window. Suppose bin A is [0,10) with 10 Wh and bin B is [5,15) with 0 Wh; the query is [0,5). B does not intersect the query, yet under nonnegative power it constrains the second half of A. Discarding B did not justify the simple disjoint-bin bound. The corrected implementation checks the full eligible-bin contract before giving a nonempty clock-window answer. It rejects that overlapping input under this contract rather than pretending to solve the more general overlap problem.

Regression checks also cover negative totals outside the query and exact empty queries without anchors. Original failed attempts remain preserved privately. The released tests expose the corrected behavior and its relevant rejection.

The public-release review found a second, narrower issue: the original runtime assumed an optional Python API always existed. A regression using a real in-memory SQLite connection with that API hidden failed before the guard and passed afterwards. This simulates one build difference; it is not a native macOS or Linux qualification.

## Execution and safety scope

Tested with Python 3.13.7 on Windows. Python 3.11+ and SQLite 3.25+ are declared requirements; other combinations have not been independently qualified here. [Python documents the optional extension-loading API](https://docs.python.org/3.13/library/sqlite3.html#sqlite3.Connection.enable_load_extension).

The demo uses bundled method code and constructed rows in an in-memory database. It makes no network requests or model calls and writes only to stdout. Tests use a temporary identity-check copy and a fresh Python process. The historical `Store` helper remains in the copied runtime but is not used. This is an inspectable local example, not a service for untrusted code or an OS sandbox. Review the code before adapting it.

Private paths, correspondence and operational receipts are excluded from this reader export. Source identities and selected contracts are inspectable; original acquisition events are not independently reproduced. Checksums detect changes against the supplied manifest, not malicious rewriting of both files and manifest.

[Back to the walkthrough](README.md)
