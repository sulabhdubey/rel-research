# Source and claim review

Use this when a conclusion depends on reading papers, documents, datasets, code, citations, or versioned evidence. It is an optional review mode, not a requirement for an ordinary task.

Source validity, coverage of current requirements, and observed execution are separate claims. A source-correct example can omit required behavior; passing it does not demonstrate a complete task. Checking changed parts alone can also miss required behavior in parts that were never updated.

- Inventory every content-bearing representation and local reference mechanism before claiming complete coverage. An automated match is a navigation aid. Challenge missing matches against raw source and leave unsupported formats unknown.
- Label each candidate passage's role: source's own result, assumption, cited input, conjecture, example, corollary, or revision note. The first theorem or occurrence need not be the main result. Match the claimed scope, assumptions, proof dependencies, source version, and audience to the actual evidence.
- Track dependency direction. A changed premise can invalidate downstream claims; an alternative independent support path may preserve them. A citation edge alone is not a proof dependency or evidence of support. Preserve withdrawn, repaired, and superseded versions rather than silently replacing history.
- Before counting corroboration as independent, trace its underlying evidence. Mirrors, summaries, translations and analyses derived from one source do not create independent observations. A separately implemented check of the same inputs can verify interpretation or calculation; it is not fresh-data replication. Keep unknown lineage unknown.
- For originality or practical benefit, compare the exact mechanism and resource model with relevant primary prior work and strong simple baselines. Distinguish a known method, a new combination, a mathematical claim, a verified proof, a finite implementation, and measured benefit. An incomplete search cannot establish global novelty; an asymptotic bound does not establish useful finite-size time or energy.
