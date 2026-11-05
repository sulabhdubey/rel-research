# Public traces: establish what the artifact actually says

**Deliverable:** a public annotation and verification package for selected agent-activity artifacts. The contribution is making specific classifications, availability gaps and extraction steps inspectable.

The earlier investigation began with a stronger ambition: find a previously unidentified artifact or incident. That was not established. What survived was a narrower, useful artifact: a source-bound record that other readers can inspect and challenge.

## What the selected material establishes

The investigation selected **116 captures**, acquired **71**, and recorded **45 as unavailable**. The sample was purposive. It cannot estimate incident prevalence across all agent activity.

A recorded request, an HTTP response and a confirmed security incident are different events. In this package, an event is a recorded request entry within a capture, with response status when available. A 2xx response alone does not establish a successful compromise, the identity of an actor, or its intent. Programs were inspected statically; suspicious payloads were not executed.

The distinction also matters for timestamps. An older record in a catalogue is evidence of that record's date, not automatic proof that a later incident existed in that year.

## Why it is useful

Re-extraction can expose inconsistent classifications or missing inputs. A capture inventory makes unavailable evidence visible. A precise event definition prevents an apparently simple headline count from silently changing meaning.

These practices transferred to later research: retain the original evidence, name the unit being counted, and bind a claim to the operation that actually produced it. A verifier that reconstructs a table from supplied files tests that reconstruction. It does not independently authenticate the original event.

## Read the separate public package

[Public Agent Trace Notes](https://github.com/sulabhdubey/public-agent-trace-notes) contains the incident-specific paper and evidence. Its v2.1.1 publication record fixes the event definition without changing the numerical study. This atlas links that archive rather than duplicating its payload-bearing material.

The surrounding public projects include [Transluce's agent-activity research](https://transluce.org/agent-activity) and [Swarm Traces](https://swarmtraces.org/). They are sources and context, not endorsements of this annotation work.

**Not supplied by this page:** the full source corpus, all 116 capture bodies, independent incident confirmation, a new forensic method or a claim that a previously unknown incident was discovered.

[Back to the atlas](README.md) · [Evidence boundaries](REPRODUCTION_AND_SCOPE.md)
