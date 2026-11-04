# Run121 independent manuscript review

Reviewed 5 November 2026 IST. Final verdict: **PASSED for Markdown source and claim scope after one correction**. This review checks current canonical v0.6 Markdown and its source claims. It does not approve PDFs/bundles, independently retrieve author web sources, rerun original learners/physical recordings, or change publication authority.

## Required correction R1

In PAPER.md section 3, the paragraph beginning `The code studies used recorded...` now follows a paragraph introducing Runs106,111,118 and119 but still says `Within each study` the maximum allowances were60 actions and900 seconds. Bind that statement explicitly to S1–S6. Their models and limits do not apply to every newly added study.

Recommended wording: `The two S1/S2 code studies used recorded gpt-6-luna/medium workers. The four S3–S6 studies used gpt-6.1-sol/medium. In S1–S6, compared workers received...` Add Run118's actual gpt-5.6-terra/medium,12-call/two-evaluation/300-second limits in its section or appendix. Run118's source report establishes those different conditions. This is a comparison-scope clarification, not a change to historical results.

**Resolution:** the author applied that clarification. Rereview of current section3 explicitly finds S1/S2, S3–S6 and `Within S1-S6`; section10 now gives the actual Run118 model and limits. Current PAPER SHA-256 is `eae8d96449cc452af1b53b86faf4d1257e7d99b05b4ea89ca453514d1c9e27d0`. Historical sections4–7 remain unchanged. The correction landed between the initial content read and the first hash collection; the JSON file bindings therefore identify the corrected rereview bytes, not an independently hashed initial defective version. No manuscript text was modified by this reviewer.

## Checks that passed

- Sections4–7 containing S1–S6 are byte-equivalent after newline normalization to the preserved v0.5 manuscript:7,524 characters each. The update has not silently changed historical result paragraphs or tables.
- Run106's12.47% joint-guidance gain versus ordinary learners,5.77% gain versus stronger later robust control, and16 versus11 above-band counts match the inspected report. The manuscript correctly states that both learner arms used REL and gives the failed-transfer context for the development-selected comparator.
- Run111's28.73% input-request saving,2.54% additional arm wall and100.30% learned-checker overhead match the report. The decision target,384 distinct queries,382 verified results and prior corpus exposure are retained. It does not relabel input-query work as measured physical sensing or REL efficacy.
- Run118's2/2 versus1/2 pinned complete endpoint, identity/provenance tie and3.63% deployment-token increase match the source report. The ambiguous audit counting unit is not called a wrong identity merge; scope remains one development-exposed task.
- Run119's three-row MSE/count/episode/max-error table matches the saved summary. Independent arithmetic on that summary gives10.38909005065507% lower MSE and9.510869565217394% fewer above-band outputs versus robust; mean MSE is1.8392874531041326% above acquired. Both numerical qualification and fresh confirmation flags remain false. The six exposed recordings and47,970 correlated endpoints are correctly distinguished.
- The Cartesian squared-error identity is correct for position vectors and needs no independence assumption. It is not extended to heading covariance, a physical error bound or tail guarantee. Execution-cost estimates are labelled estimates rather than new timed deployments.
- The nine components are not presented as nine independent replications. Four typed families remain distinct; numerical/path certificates are not used as physical-pose certificates. The Run120 package remains a trusted fixed-record example with constructed tests.
- Source non-admission agrees with SOURCE_REVIEW.md: author descriptions supply useful range/3D/quasi-omnidirectional/LiDAR facts, but exact configuration/timing/reference/calibration roles remain unresolved after access failures. Manuscript wording does not assert absent data, dataset ineffectiveness, guaranteed reference independence or proven leakage.
- METHODS_RESEARCH.md correctly remains prospective: no unchanged compatibility claim, no fabricated bearings, no missing lateral motion silently discarded, no threshold/model comparison admitted. Its range-only Jacobian and Joseph update are internally consistent under the stated planar/height assumptions; no claim of empirically validated AAU geometry follows.
- The obsolete uncapped-history next-step sentence is removed. The paper, reader brief and sharing drafts select evidence review and conditional reopening, not another broad dataset or local-threshold search.
- No private project names, account identifiers, credentials, private transcript quotations or local absolute machine paths appeared in the five reviewed manuscript-facing Markdown files. Source reports remain separately scoped private derived evidence.

## Delivery dependencies outside this review

At review time the manuscript-facing text describes a v0.6 package whose PDFs, new component verifier, manifest and source baseline links were not yet rebuilt. Parent execution must verify those actual artifacts before saying the package is delivered. Verify the new component arithmetic from trajectory summaries rather than merely comparing repeated summary values, and distinguish same-evidence reconstruction from new physical replication. Preserve old v0.5 PDF/ZIP identities and avoid presenting them as current.

The manuscript says source baseline and current skill identity are recorded separately. The new package must actually contain that current identity record; the historical f598... digest in the appendix applies to the old edition. Its relationship to the core-only Run118 treatment must remain exact.

## Scope and disposition

Read canonical PAPER.md, EVIDENCE_APPENDIX.md, READER_BRIEF.md, README.md and SHARING_DRAFTS.md; Run121 SOURCE_REVIEW.md and METHODS_RESEARCH.md; current component map; relevant original Run106/111/118/119 reports and Run119 summary. Used the preserved v0.5 manuscript for text comparison. Source-team external assertions are attributed to their recorded review, not independently re-browsed here. No new empirical execution or independently measured run costs were produced.

The generic REL core should stay unchanged. The needed correction concerns presentation of mixed-study scope. Existing REL source/claim and evidence-boundary rules already cover it.

## Methods appendix update rereview

The methods appendix was subsequently amended from SHA-256 `11b0093e4a4fb1e1c2c13f4a1b7cc99867352d2eba058abbd82992f4fb865888` to `f970b4280cf48241b8b63d428f9372cd3c560f270d2ded3ccabe58ce121d67bf`. The added paragraph distinguishes AAU's pairwise affine raw-range model `gamma*h + beta` from the unit-scale additive-bias special case. Its residual `r - gamma*h - beta` and state Jacobian `gamma*H` are algebraically consistent when calibration parameters are held at their declared values. The text explicitly retains calibration uncertainty/dependence, terrain/height and orientation limitations, and quasi-omnidirectional motion rather than claiming the simple planar model reproduces the author estimator. This aligns with the source review's affine-calibration, three-dimensional-geometry and motion findings. The author-section details remain attributed to the methods/source reviewers; this rereview did not fetch the paper independently.

**Disposition: passed, no new manuscript correction required.** PAPER.md and its claim review are unchanged. The appendix remains a prospective specification, numerical source admission remains closed, and the earlier methods hash remains preserved in the JSON history. PDF renderer differences reported by the parent belong in its visual receipt; they do not change this Markdown/source review into independent rendered-PDF validation.
