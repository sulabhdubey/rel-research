# Inspect mechanisms; search beyond familiar combinations

**Two complementary habits:** reverse engineer what an artifact actually does, and consider useful combinations outside the current research branch.

Reverse-engineering guidance helped route inspections toward source, interfaces, dependencies and runtime boundaries. This supports concrete questions: where does state persist, what invalidates a cache, which component owns a side effect, and what operation was actually executed? It is a method of investigation, not a claim of a new learning architecture.

## What Alien Space of Science contributed

The programme inspected the [pinned repository](https://github.com/alejandrohdez00/alien-space-of-science/tree/39cbccc70cf9136f3a8009cd83a69a7bcde7107d) and [v3 paper](https://arxiv.org/abs/2603.01092v3). Its useful distinction is between **whether mechanisms fit together** and **whether their combination is familiar in a research community**.

The implementation extracts mechanism-like units, groups them into idea atoms and ranks combinations using coherence and researcher-repertoire signals before generating proposals. These are proposal-ranking signals, not calibrated probabilities that a scientific claim is true or original. An unfamiliar combination can be incoherent; a familiar one can be the best solution.

Our review inspected implementation and selected arithmetic. It did not rerun the pretrained models or underlying scientific experiments. The proposal generator's output does not itself verify its sources or implement the proposed science.

## The adaptation for REL

Keep two linked records:

1. **Mechanism:** what operation could be reused or combined?
2. **Evidence envelope:** under which assumptions did it work, fail or remain untested?

Discarding the second record makes creative recombination easier to describe and harder to trust. Keeping it lets an unusual combination address an identified failure boundary.

For example, saved solver state, an output bound and a decision-relevant input request can be combined into a concrete candidate. The experiment must show correct, useful later operations—not merely a persuasive proposal.

## What happened when an extra selector was tested

Run114 compared a learned method selector against strong ordinary dispatch. The added selector did not qualify for promotion: it was slower and used more recorded tokens. This does not invalidate broad exploration. It shows that an added selection mechanism must earn its cost. [Report](../package/component-evidence/REPORT114.md).

The practical rule is to compare distinct executable constructions, including a strong simple one. Keep unusual ideas in the portfolio, but let discriminating tests decide what becomes part of the system.

[Mathematics to methods](04-mathematics-to-methods.md) · [Back to the atlas](README.md)
