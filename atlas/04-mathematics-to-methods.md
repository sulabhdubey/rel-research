# From mathematical sources to executable methods

**Useful transfer:** mathematical work gives us conditional constructions, proof obligations and ways to spend computation where an output needs it.

The programme reviewed a pinned snapshot of [OpenAI's mathematics repository](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb): 719 current manuscripts organized into 372 related families across 17 disciplines. These are inventory counts. They do not mean 719 independently accepted new solutions.

The review recorded a source-linked introductory semantic reading of all 719: selected hypotheses, main attributed results, proof overviews where source-located, and relationships between revisions. It was not an independent line-by-line verification of every proof, a complete formal build, or proof that each formal statement matched every prose claim. The later science review extended the design questions; it did not erase these verification boundaries.

## Three transfers worth keeping

**Carry the conditions with the method.** A theorem or algorithm can be correct under its assumptions and useless when an interface silently drops one of them. Store the admissible inputs, precision requirements and invalidation conditions with reusable code.

**Ask how much accuracy the output needs.** A consumer may need a decision or a bound on one quantity, not a uniformly precise internal solution. The programme built conventional primal/dual output checks and connected them to solver continuation. Their validity remains tied to the stated convexity, feasible-dual and numerical conditions. [Component map](../package/component-evidence/COMPONENT_MAP.md).

**Preserve dependencies without inventing them.** A citation is not necessarily supporting evidence; a changed citation is not necessarily a changed proof. Revisions must be checked at the semantic level required by the claim. This informed the research's version and evidence handling.

## A concrete identity—and its limit

For two estimates `r` and `j` of a Cartesian target `y`:

```text
|| (r+j)/2 - y ||² = (||r-y||² + ||j-y||²)/2 - ||r-j||²/4
```

The identity explains how disagreement can affect the error of an average. It does not require independent estimators. It also does not guarantee protection from large errors, supply a fused covariance or validate a sensor source. Those questions still require evidence. [Localization comparison](../package/component-evidence/REPORT119.md).

## What is not our novelty claim

Several early proposals overlapped established routing, versioned retrieval, constrained sampling, operator portfolios and dependency tracking. They were treated as prior art or baselines. “Inspired by new mathematics” is not sufficient evidence of a new algorithm.

The productive step is a derivation, program or counterexample with an explicit comparator. That is how the mathematical literature can change an experiment rather than merely decorate its introduction.

[Executable learning](06-executable-learning.md) · [Back to the atlas](README.md)
