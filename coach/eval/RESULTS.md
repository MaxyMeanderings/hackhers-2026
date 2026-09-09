# Coach live evaluation results

**Latest completion follow-up: BLOCKED.** Both permitted proof repairs are
consumed; the final prompt failed both public scenarios by fencing required raw
JSON. No final heldout proof ran. The last supplemental ten-case suite passed
seven cases on the preceding prompt; its full conversation also failed semantic
review. See [current status and actual evidence](../../docs/coach-completion-20260909/LAPTOP-FINAL-STATUS.md).

## Historical original task

**FAIL: 8 of 10 cases passed after three permitted behavioral repairs.**

Runtime: Claude Code with existing subscription sign-in. All ten final outputs match prompt SHA256 `8ae1c4bd8f24fd8ecdf1ead6f1a808c163143490e76af711162f80baf3a83083`.
Claude chat live behavior and parity remain unverified.

| Case | Outcome | Evidence |
| --- | --- | --- |
| 01 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-01.json) |
| 02 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-02.json) |
| 03 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-03.json) |
| 04 | FAIL | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-04.json) |
| 05 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-05.json) |
| 06 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-06.json) |
| 07 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-07.json) |
| 08 | FAIL | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-08.json) |
| 09 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-09.json) |
| 10 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-10.json) |

Case 04 failed citation support: the response attributed mobile apps to a page describing mobile browser access; its Forms pricing claim was also unsupported by the cited page. Case 08 proposed a three-feature subset but deferred the required experiment linkage.

[Independent review](../../docs/spec-fa7abd1282236c13/LIVE-REVIEW.md) records source expectations and citation inspection.

Full multi-turn scenario: two actual turns retained; stopped after the terminal case gate failure. Four-deliverable completion and student approval were not verified. Shared-prompt source construction passed independent review; this does not establish live parity.

Inputs are synthetic workshop fixtures, not real student interviews. No passing release or publication is claimed.
