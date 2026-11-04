# Public package validation — v0.7.1

Checked 5 November 2026. This receipt describes the reviewed reader export, not a new empirical study or security certification.

| Item | Result |
|---|---|
| ZIP inventory | 144 files; unique safe paths; no traversal, symlink or case collision |
| Package manifest | 143 entries; exact file inventory and matching SHA-256 hashes |
| Selected-results verifier | Passed: supplied-byte identity and selected saved accounting |
| Component-results verifier | Passed: Run119 table reconstructed from saved metrics |
| Constructed example | Passed using existing Python 3.13.7 / NumPy 2.4.6 |
| Reference tests | 17 passed; zero failures or errors |
| Execution changes | Extracted files unchanged; no extra generated file |
| Preserved methods | All 15 Python files unchanged from reviewed v0.7 |
| Skill snapshot | All 21 generic REL files and inner manifest unchanged |
| Privacy review | Raw text, decoded JSON strings, filenames, PDF text/metadata and actions checked; known private workspace field removed |
| Secret scan | Gitleaks 8.30.1, default rules, redacted reports, no findings in final export |
| Reader links | No broken relative Markdown links; unavailable private provenance explicitly labelled |

ZIP SHA-256:

```text
aa0dcdcc8b2d51f2392ceb020059ed43ba93820525c79abb9be6c22774e8baf3
```

Inner package manifest SHA-256:

```text
e3dcfeb674a86cd897d30ba20c9cd2cc17366482bb90f303c8e278fdce8d4ef8
```

The ZIP and standalone PDFs are supplied with `SHA256SUMS.txt` in the release. Checksums identify bytes; they do not authenticate original events or prove scientific effects. Independent model-assisted reader and privacy reviews are not external peer review. Targeted scanners may miss undiscovered sensitive content. Raw datasets, private chats and original model trajectories are excluded, so complete historical replication is unavailable.

An earlier private review missed one JSON-escaped workspace path. The public export removes it and checks decoded fields. Original failure records remain preserved privately; this receipt replaces neither their historical scope nor their failures.
