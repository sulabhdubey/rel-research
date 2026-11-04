# Study 1: offline table reproduction

Run `python reproduce.py` using Python 3. No external package, model, network,
credential, Docker engine or GPU is required. The script verifies the bundled
file hashes, all 26 role identities, phase accounting, scored-count consistency
and the reported table. The manifest binds every package file except itself;
it detects changes relative to the supplied manifest, not a malicious rewrite
of both data and manifest or authenticity of the underlying observations.

`attempts.csv` contains the two actual origin acquisitions and all 24 later
attempts. It exports only study role identifiers, outcomes and recorded integer
token counts. It omits private filesystem paths, account/thread identifiers,
prompts and raw trajectories. `source_provenance.json` binds the source record
bytes by digest; it does not bundle or authenticate those source records.

For each phase, total tokens = input + output. Cached input is included in input;
reasoning output is included in output. Total usage = task usage + feedback
usage. The feedback counts are recorded explicitly, including zeros; they are
not inferred from a missing field. All failed work within these attempts remains
in its recorded counts. Correctness here is the saved scored-packet verdict,
not full specification correctness or independently re-executed output.

The ordinary no-history arm A passed 7/8 later tasks; ordinary same-history B
and REL same-history C each passed 8/8. Acquisition cost is charged once to each
retained policy B/C, not once per task. These are separate counterfactual policy
totals: do not add both acquisition allocations into actual campaign spending.
A receives no acquisition charge. All actual 26 attempts sum to 3,861,892 tokens,
including 357,417 origin acquisition tokens and 145,482 feedback tokens.

Expected inclusive totals are A 1,270,553, B 1,475,038 and C 1,473,718. The script
reconstructs these and their cached/uncached components directly from rows and
checks the independently exported original accounting summary. Repeated source
checks are not independent agent trials. The paper explains source membership,
the single observed failure, direct replay and study limitations.

This package reproduces saved-record arithmetic. It does not rerun agents,
validate raw model events, rescore code, establish causal lesson use, or prove
broader RSI effectiveness. Parent/reviewer work, currency and physical energy
are unmeasured; token counts are not complete economic or energy costs.
