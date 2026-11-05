# What can an agent carry forward?

**Observations, executable methods, working state — and evidence of when reuse stops helping.**

This is the public reader package for *Retained Experience, Executable Methods, and the Limits of Transfer: Evidence from Recursive Evidence Loop*, by **Sulabh Dubey**. Study edition v0.7; public package v0.7.1, 5 November 2026. Technical report, not peer reviewed.

## Read the research

| Start here | Contents |
|---|---|
| [One-page brief](package/READER_BRIEF.pdf) · [text](package/READER_BRIEF.md) | The question, principal findings and limits |
| [Full paper](package/PAPER.pdf) · [text](package/PAPER.md) | Six agent-study summaries and a wider component synthesis |
| [Evidence appendix](package/EVIDENCE_APPENDIX.pdf) · [text](package/EVIDENCE_APPENDIX.md) | Controls, accounting, failures and evidence boundaries |
| [Download the complete evidence package](https://github.com/sulabhdubey/rel-research/releases/tag/v0.7.1) | Versioned ZIP, standalone PDFs and SHA-256 checksums |
| [Reproduction guide](package/README.md) | Offline saved-result checks and a constructed example |

## Explore the wider research

The [research atlas](atlas/README.md) connects eight topics: public agent traces, intelligence and consciousness, brain-inspired memory, mathematics, REL, executable learning, reverse engineering and unfamiliar combinations, and failures that changed the programme. Each page distinguishes results from synthesis and open questions.

[Study register](atlas/STUDY_REGISTER.md) · [What readers can reproduce](atlas/REPRODUCTION_AND_SCOPE.md)

This 5 November supplement leaves the versioned v0.7.1 paper, selected evidence and release assets unchanged. It is a curated route through the programme, not a claim that every numbered run is an independent discovery.

## What we found

- Retained observations reduced repeated database work by about **77%**. Ordinary factual handoff achieved the same benefit.
- **60 later reports** reused saved executable methods without a new model call, in both REL and ordinary arms.
- Retained scalar state improved one acquired robot-update method's MSE by **2.42%** versus resetting that scalar; another learner removed its scalar.
- A procedure revision produced matching later methods and outputs with **20.12% more recorded tokens**, including revision cost.

These are different scoped studies, not a pooled treatment effect. Useful component reuse does not establish that adding REL consistently beats equally informed ordinary work.

## What you can check

The package includes selected saved summaries, two arithmetic/identity verifiers, the current REL instruction snapshot, and a runnable constructed localization example with 17 engineering tests. The standard-library verifiers need no network, credentials or model access. The example requires an existing NumPy installation.

The package does **not** include original model transcripts, complete historical hosts/prompts, raw sensor recordings or private project evidence. Reconstructing the supplied numbers is different from independently replicating the original studies. [Exact boundaries and commands](package/README.md).

## Run a checked example

[Temporal observation controller](examples/temporal-observation-controller/README.md) · [Validation and commands](examples/temporal-observation-controller/VALIDATION.md)

This standard-library Python example asks only for observations needed to justify a graph decision, retains still-valid facts across queries, and restores them in a fresh process. It returns **unknown** when the budget or evidence is insufficient. The example includes 20 unit tests and a separate time-expanded graph checker. All cases are constructed; this is reusable ordinary software, not a demonstrated learned-policy improvement. No model, account, data download or third-party dependency is needed.

## Discuss and cite

We welcome specific criticism of the controls, applicability contracts, retained-state failures and the next experiment that would change a conclusion. [X discussion](https://x.com/SulabhDubey/status/2118090896885551559). Use GitHub Issues for reproducibility questions; do not post credentials or private logs.

Suggested citation: Sulabh Dubey (2026). *Retained Experience, Executable Methods, and the Limits of Transfer: Evidence from Recursive Evidence Loop*. Technical report v0.7; public package v0.7.1. This repository.

[Release changes](package/PUBLICATION_NOTE.md) · [Rights and dependencies](package/RIGHTS_AND_DEPENDENCIES.md)

Only the reviewed reader export is public. Historical private-source links are identified as unavailable provenance, not public download endpoints. No broad open-source license is selected by this publication.
