# Learning a method is different from remembering advice

**Concrete output:** reusable programs, checked solver state, temporal-graph methods and a small localization reference implementation. These are working components, with different contracts.

Written advice can be misinterpreted. An executable method makes an operation inspectable—but still needs applicable inputs, verification and a rule for adapting or rejecting reuse.

## Six mechanisms, one unresolved integration question

| Mechanism | What it contributes | What must still be checked |
|---|---|---|
| A1: Counterexample-refined working state | Keep decision-relevant context or numerical progress | Whether retained state remains useful after change |
| A2: Validity-conditioned method compilation | Store and invoke an actual program | Correct acquisition, applicability and later reuse |
| A3: Conditional decomposition with reusable interfaces | Compose methods with explicit input/output contracts | Compatible semantics and recovery |
| A4: Complementary information acquisition | Request inputs that can change a decision | Benefit known before paying for the answer |
| A5: Output-directed approximation and refinement | Refine only as much as the consumer requires | Valid bounds and unresolved boundary cases |
| A6: Reversible consolidation and procedure evolution | Improve the process that creates later methods | Advantage over a frozen process with equal information |

Source, measurement and version binding cut across all six. They are conditions for interpreting results, not an additional proof of intelligence.

## Selected executed results

**Saved methods:** Run86 used saved executable methods for 60 later reports without new model calls during those reports. Ordinary engineering achieved this too. The useful result is reuse; the comparison does not establish a REL-specific advantage. [Report](../package/component-evidence/REPORT86.md).

**Decision-relevant inputs:** Run111's ordinary witness/progress policy used **28.73% fewer requests** with **2.54% more wall time** than the development-selected alternate/width control; both verified 382 of 384 decisions. Another ordinary policy bought fewer inputs, so this is a particular trade-off, not the minimum possible request count. The equivalent saved learned graph took more time than the direct formula. Two decisions remained unresolved. [Report](../package/component-evidence/REPORT111.md).

**Procedure changes:** Run92 tested procedure evolution. It added **20.12% recorded tokens** without a demonstrated later advantage. The failed candidate remains evidence; it was not promoted just because it revised itself. [Report](../package/component-evidence/REPORT92.md).

## Try reuse under changed requirements

The [Run125 walkthrough](../examples/reuse-adapt-refuse/README.md) makes three operations visible: reuse an acquired method, execute a retained calibration-aware method when the requirement changes, and decline an exact answer when the observations do not determine it. The rows and routing are constructed for this example; it does not learn a new method during execution. The ordinary reference uses the same facts. Readers can challenge the applicability checks with a minimal counterexample.

## Try the small public reference

The [localization reference](../package/reference/README.md) supports prediction, separate evaluation and checked save/restart on constructed fixed records. The package records 17 passing engineering tests after preserved failed attempts. It needs no model API or GPU. It is not a live robot deployment or an independent sensor benchmark.

The [component map](../package/component-evidence/COMPONENT_MAP.md) shows what actually connects. A convex-output certificate, a graph reachability proof and a robot pose estimate have different truth conditions. Shared vocabulary does not make them interchangeable.

**Open integration question:** can learning a method and its required context together improve later choices among reuse, observation, refinement and rebuilding beyond strong ordinary implementations?

[Reproduction coverage](REPRODUCTION_AND_SCOPE.md) · [Back to the atlas](README.md)
