# What Can an Agent Carry Forward?

Sulabh Dubey | 5 November 2026 | Technical review brief v0.7

## The contribution

An agent can retain observations, executable methods or working state. This report examines when each changes a later decision, and separates that benefit from adding an improvement procedure. Six agent studies and a wider component programme supply worked examples, strong ordinary controls and retained failures.

## Findings worth discussing

- Observation history reduced repeat database work by about 77%; ordinary handoff achieved the same benefit.
- In a longer lifecycle, all 60 later reports ran saved methods without a new model call. Both ordinary and REL methods did this, so REL's extra acquisition tokens did not break even against ordinary reuse.
- A robot learner's retained scalar improved MSE by 2.42% versus resetting it; another successful learner removed its scalar. Useful memory is conditional.
- Ordinary averaging improved mean error and large-error counts in exposed robot recordings, but gave up some acquired-method accuracy. A procedure revision did not improve later selected methods and added 20.12% tokens.

## What the package lets a reader do

Read the full paper and evidence appendix, inspect the current REL instruction snapshot, reconstruct selected tables from saved summaries, and run a constructed localization example with 17 engineering tests. The package does not rerun the original model trials or physical recordings. Its manifest checks byte identity; reconstruction is not independent scientific replication.

## The present conclusion

Executable reuse and source-bound observations are useful within tested contracts. Added REL instructions have not shown a consistent advantage over equally informed ordinary work. The report offers inspectable components and failure mechanisms, with complete architecture superiority and general recursive improvement still open.

The paper and selected evidence package are publicly available in the rel-research repository. The full research archive remains private. We seek feedback on missing controls, applicability contracts and what fresh evidence would change these conclusions. A new range-only experiment remains conditional on resolving the AAU source configuration and evaluation roles.
