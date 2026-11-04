# Method resources

This catalogue describes available method families, their use conditions and prerequisites. It does not supply tools, guarantee results or make any method compulsory. Source identifiers point to background research, not an instruction to fetch every paper. Verify an implementation and its current requirements before relying on it. Named task templates often reorganize overlapping goal, context, constraints and format fields.

| Family | Relevant conditions | Operation and prerequisites | Limit |
|---|---|---|---|
| Direct task instructions | Clear request and sufficient current information | Complete the requested action from its actual requirements | An extra template may add no useful information |
| Audience and output specification | A recipient or program needs a particular form | Express the result at the required depth, in the required artifact or format | Role labels create no expertise; concise prose does not replace required files |
| Few-shot or contrastive examples | A format or interpretation distinction is unclear | Use relevant examples, optionally including a distinguishing near-miss | Incidental example details can bias the result |
| Decomposition, least-to-most, plan-and-solve | Dependencies make direct completion difficult | Break the work into useful dependent operations with inspectable intermediate results | Completed steps do not establish a complete final deliverable |
| Reasoning-model prompting | The model supports internal reasoning | Supply clear goals and constraints; request verifiable results and useful explanations | Verbose hidden-reasoning requests are unnecessary; model-specific compatibility varies |
| Tool-grounded action, ReAct family | Environment observations determine later action | Invoke an available authorized tool and inspect its actual result | Describing a tool call is not execution |
| Program-aided reasoning, PAL family | Computation, parsing or repeated deterministic transformation | Execute an appropriate program against declared inputs in an authorized environment | A program may implement the wrong semantics despite running successfully |
| Retrieval and just-in-time context | A fact or source is missing from available context | Search available authorized sources and retain provenance | Retrieved material can be stale, incomplete or untrusted |
| Structured outputs | A consumer requires a precise record | Use supported schema enforcement and semantic validation | A JSON instruction alone does not enforce a schema; valid shape is not truth |
| Verification questions, CoVe family | A factual or semantic claim has a decisive check | Obtain relevant source evidence, executable checks or independent review | Repetition and self-judgment are not independent corroboration |
| Feedback/refinement, Self-Refine or Reflexion family | Observed feedback can change an unsuccessful attempt | Diagnose the failure, revise and check the result | Feedback can amplify errors and adds cost; a localized structural mismatch is not a causal diagnosis or a completed repair |
| Multiple candidates, self-consistency | Additional attempts can distinguish plausible alternatives | Sample within an available budget and validate outputs | Agreement can reflect correlated errors |
| Search, Tree-of-Thought-style branching | Discrete alternatives and backtracking are useful | Explore bounded branches with observable acceptance criteria | Requires extra execution or inference and a suitable search problem |
| Source-bound summaries and handoffs | Long history, restart or context pressure | Retain decisive state, exceptions and recoverable source pointers | Compression can lose information; stale pointers may prevent recovery |
| Learned compression, LLMLingua-2 family | Repeated large inputs justify a compression component | Use an available implemented compressor with resource accounting | Requires a model/tool; shorter text need not preserve every requirement |
| Prompt/program optimization, GEPA family | Repeated tasks offer trustworthy feedback | Search versioned prompt candidates using separate development and evaluation data | Requires an implemented optimizer and budget; overfitting remains possible |
| Evolving context/playbooks, ACE family | Repeated work offers reusable guidance | Maintain applicable additions and reconcile stale or conflicting entries | Accumulated text and errors can increase cost or harm later use |
| Native multimodal/artifact methods | Meaning depends on tables, images, layout or rendered behavior | Use an available document, spreadsheet, vision or browser capability | Plain text may omit essential relationships or recipient-visible defects |

Research identifiers: Prompt Report (arXiv:2406.06608); ReAct (2210.03629); PAL (2211.10435); Self-Refine (2303.17651); self-consistency (2203.11171); Tree of Thoughts (2305.10601); LLMLingua-2 (2403.12968); GEPA (2507.19457); ACE (2510.04618). These identifiers describe method families, not implementations bundled with REL. They do not establish effectiveness on the current task or make REL a replication of those systems.
