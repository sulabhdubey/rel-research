# REL paper and evidence — public package v0.7.1

Study edition: **v0.7, 5 November 2026**. Public-package changes correct release wording and remove a private workspace field; numerical results and research methods are unchanged.

Read [the one-page brief](READER_BRIEF.pdf), [the paper](PAPER.pdf) and [the evidence appendix](EVIDENCE_APPENDIX.pdf). Markdown equivalents are included for accessible reading and citation. See [PUBLICATION_NOTE.md](PUBLICATION_NOTE.md) for export changes and omissions.

## Run the supplied checks

From this extracted package directory, using an existing Python installation:

```text
python -I -B verify_selected_results.py
python -I -B verify_component_results.py
```

The first checks byte identity and selected S1-S6 accounting, including its two historical arithmetic reconstructions. The second reconstructs Run119's table from saved trajectory-level metrics. Neither reruns the original model trials or sensor-data scoring.

With NumPy already installed, run the [constructed localization example](reference/README.md) and its 17 engineering tests:

```text
cd reference
python -B example.py
python -B test_reference.py
```

No credentials, model calls, network access, GPU or automatic dependency installation are required. Tested: Python 3.13.7, NumPy 2.4.6, Windows. Inspect scripts before running. Extraction into a fresh folder is not a security sandbox.

## Supplied and absent evidence

`rel-current/` contains the exact 21-file generic skill/support snapshot and its manifest, for reading as data. It is not installed or loaded automatically. `evidence/`, `reproduce-study1/`, `reproduce-study2/` and `historical-diagnostic/` preserve selected historical summaries and accounting. `component-evidence/` provides later reports, a component map and saved Run119 metrics. `source-review/` records an unresolved source admission rather than an admitted experiment. `review/` describes prior review scope.

Full historical prompts/hosts, native transcripts, raw datasets and private observational receipts are absent. Pinned private-source links in historical reports identify unavailable provenance; they are not public downloads and are not required by the commands above. Historical next-action sections are not the current research plan. Public artifacts support selected-result reconstruction and a constructed example, not independent scientific replication or a general REL advantage.

See [rights and dependencies](RIGHTS_AND_DEPENDENCIES.md), [version identity](VERSIONS.json) and [publication note](PUBLICATION_NOTE.md). The broader research repository stays private.

[Detailed reconstruction coverage](REPRODUCTION_COVERAGE.md) lists what is and is not available for each evidence family.
