# Current-source streaming repair qualification

20 October 2026. Exploratory source qualification and ordinary repair.

**A real, previously reported Requests framing defect was reproduced in current
acquired source. Two independent ordinary workers repaired all 220 failing
positions while preserving all 434 starting passes. Neither received REL or
episode history. No retained-experience comparison qualified.**

## From project screening to a real failure

Four additional local project leads were inspected beyond the preceding
[three-project screen](EVIDENCE_2026-10-20_PROJECT_QUALIFICATION.md). Active work,
passing reported repairs and a broader training gap did not supply a suitable
completed-repair failure. An older lookup timeout could not be replicated: the
current query instead failed to open its database. That access failure neither
resolves nor confirms the older latency problem. Other projects were unchanged.

The public-source branch acquired Requests 2.34.2 with its published wheel
checksum and current main at `611c6162cbc4ac2020a2f91c7cfa4f3abf9bbb60`.
The actual `Response.iter_lines` body was exercised at a controlled
`iter_content` seam. Both release and main reproduced chunk-dependent framing
errors. Issue [#3980](https://github.com/psf/requests/issues/3980) is closed;
that historical status does not establish current release behavior.

The initial partial port of the old fix omitted prerequisite behavior and was
not a faithful prior-art baseline. Its results remain preserved. The exact
merged implementation from [#3984](https://github.com/psf/requests/pull/3984),
commit `084625cb3cd6bed4feeb0e65c880dc02c2fb3aa1`, was then acquired and graded.
It repaired many cases but failed when requested Unicode decoding still yielded
bytes. The current acquired decoder explicitly permits this fallback.

## Design and results

The plan and corrected framing contract preceded worker dispatch. Cases covered
split CRLF, actual bytes/text, universal newlines, empty chunks and fields,
custom/overlapping delimiters, unfinished records, forwarding and early yield.
An independent reference was checked against complete-content built-ins and
poisoned read-ahead fixtures. See the [Requests API](https://docs.python-requests.org/en/stable/api/)
and [Python string semantics](https://docs.python.org/3/library/stdtypes.html#str.splitlines).

Both fresh native workers used gpt-6-luna/medium, identical source, requirements,
tools and limits: 60 actions and 900 seconds including startup. No extra lesson,
reflection or answer artifact was required. The coordinator used REL; workers
had no enabled skill or episode history. Candidate Python ran in the existing
offline, nonroot, resource-bounded Docker guest. No paid provider API was used.

| Artifact | Correct / positions | Starting failures repaired | Starting passes lost |
| --- | ---: | ---: | ---: |
| Acquired released method | 434 / 654 | 0 | 0 |
| Partial historical port, incomplete baseline | 385 / 654 | 27 | 76 |
| Exact historical merged method | 556 / 654 | 196 | 74 |
| Independent reference | 654 / 654 | 220 | 0 |
| Ordinary O1 | 654 / 654 | 220 | 0 |
| Ordinary O2 | 654 / 654 | 220 | 0 |

These are dependent positions in one method family, not 654 independent tasks.
Twenty-eight groups reduce container overhead and are not the scientific unit.
Public source and related diagnostics were exposed; no training-clean or
protected holdout is claimed. The exact historical method's 98 remaining
positions raised `TypeError`; its aggregate improvement hid 74 regressions.

The admission rule required repeatable residual errors after ordinary repair.
Both ordinary workers passed, so six conditional comparison attempts were not
dispatched. No artificial resource reduction or new trap was used to obtain a
desired failure. This leaves REL's added value unresolved.

## Recorded costs and corrections

| Worker | Requests | Actions | Total tokens | Cached input, included | Uncached input + output | Dispatch seconds |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| O1 | 12 | 16 | 198,926 | 151,168 | 47,758 | 181.055 |
| O2 | 6 | 10 | 83,848 | 62,464 | 21,384 | 143.317 |

Total recorded worker use was 282,774 tokens, 26 actions and 324.372 summed
dispatch seconds, with no feedback-model request. Per completed repair this
averaged 141,387 recorded tokens, or 34,571 uncached input plus output. These are
descriptive worker costs, not full-project efficiency. Cache and reasoning are
subsets, not additional tokens.

All tool receipts were reconciled. O1 had two nonzero Python exits: a corrected
import path and a faulty test expecting a result before the complete delimiter
arrived. The worker corrected the fixture and checked actual early emission.
O2 had no nonzero Python exits; neither worker had a broker rejection.

Separately recorded costs include 6.091 source-acquisition seconds, 71.380
summed baseline-grading seconds and 84.993 native-preflight seconds. Initial
Docker information querying stalled while the engine was unavailable; its
duration is unknown and the failed attempt remains recorded. Starting the
existing engine resolved it. O1 briefly overlapped historical-baseline grading,
so dispatch times are not contention-controlled efficiency estimates. The two
workers did not overlap.

Complete coordinator tokens, engineering time, money and physical/remote
energy remain unknown. Dispatch includes its own setup, tools and grading;
do not double-count those subtotals or call summed durations campaign elapsed.

## Consequence for REL

The core instructions, references and executable helpers are unchanged.
Existing checks already cover current contracts, source dependencies, correct
feedback and faithful baselines. An [non-public source: observed example](https://github.com/sulabhdubey/recursive-evidence-loop/blob/507357e1d7a55335f9205134ad1c32ac4657b0bc/docs/EXAMPLES.md#observed-check-a-saved-fix-against-current-runtime-values)
now connects those checks to actual conditional reuse:
requested conversion does not prove resulting representation, and a literal-LF
JSONL lesson does not replace a universal-newline contract.

The evaluated O1 repair was exported locally with its Apache-2.0 licence and a
diff against the acquired full module. Exact evaluated bytes were matched and
full-module syntax checked. No installed library was changed, and no upstream
submission or complete HTTP/transport integration test occurred. This package
contains sanitized evidence, not the full private study infrastructure.

Two successful ordinary repairs establish this bounded engineering result.
They do not demonstrate a new algorithm, REL superiority, broad portability
or sustained self-improvement. Reopen the learning question for a naturally
recurring error after ordinary repair, rather than rerolling this solved profile.

See the [structured summary](EVIDENCE_2026-10-20_REQUESTS_QUALIFICATION.json).
