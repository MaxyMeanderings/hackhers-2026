# Laptop continuation status — 2026-09-09

**BLOCKED: coach development proof failed after both permitted repairs. The
coach is unfinished and must not be merged as verified.**

## Runtime delivered

Nightshift multi-turn replay, structural assertions, public development
transcript retention, and preservation of failed prompt lineage are merged.
The retention repair passed 18 regression tests and 25 existing proof tests,
independent review, and GitHub checks.

- [Initial runtime review and integration](https://github.com/doctor-ew/nightshift-community/pull/29)
- [Promotion to main](https://github.com/doctor-ew/nightshift-community/pull/30)
- [Development evidence and failure lineage repair](https://github.com/doctor-ew/nightshift-community/pull/31)

Runtime main and the user's runtime checkout are at
`d5aaf825f428f1dbc29cbd8963d4b8a2d60107bc`. Existing untracked work was preserved.

## Coach evaluation outcome

The final prompt file SHA-256 is
`c30e25155e5030e7ac03021a9d7780de29966a6468ad45b151137d573e9bfdaa`.
Both public scenarios failed at their first turn because the model surrounded
the requested raw JSON with Markdown fences. The locked assertions require raw
JSON. Removing fences before grading would change the acceptance contract.

- [Final development receipt](proof-development-laptop-attempt3.json)
- [Evidence scenario actual response](development-e8cd4af33a90404d8fb9d6dc3945f34d.json)
- [Experiment scenario actual response](development-f58ddeb11c684709bfe12527b8a19d38.json)
- [Static repair review](FINAL-REPAIR-REVIEW.md)
- [Independent final failure review](FINAL-FAILURE-REVIEW.md)

The canonical ledger records 11 development launches, zero final launches,
two of two repairs consumed, and one of two infrastructure failures consumed.
The infrastructure failure was CLI version drift before a model launch;
[the pinned runtime record](RUNTIME-PIN.md) explains the correction. Calls use
subscription authentication. Model selection remains configurable.

The generic receipt action `repair_prototype` does not grant another repair.
No unchanged-prompt resampling, budget reset, assertion weakening, or hidden-test
adaptation is authorized by this record. Continuation requires an explicit
budget decision that preserves this failed task's lineage; it cannot silently
create a fresh task to bypass the cap.

## Supplemental evidence and unfinished deliverables

The laptop continuation recorded 30 actual original-case responses and eight
actual conversation turns across changed prompt versions: 38 supplemental
calls, separate from the canonical proof ledger. These calls do not replace
the required gates or erase inherited executions.

The latest full ten-case run passed seven cases under independent semantic
review. It used the preceding prompt, not the final failed prompt. The latest
five-turn conversation reached all four outputs and student approval, but its
semantic review found unsupported causal/history claims and lost source
attribution. It is failed evaluation evidence, not a validated worked example.

- [Latest ten-case review](CASES-REVIEW-ATTEMPT3.md)
- [Full conversation review](CONVERSATION-REVIEW-ATTEMPT2.md)
- [Supplemental execution checkpoint](live/laptop-20260909/attempt3-checkpoint.json)
- [Private proof status and provenance](PRIVATE-PROOF-FINAL-STATUS.md)

Fresh heldouts were independently authored to replace the exposed candidates.
They remain private and unused. There is no final proof PASS. A passing ten-case
suite for the final prompt, a reviewed worked example, final acceptance, and a
verified coach merge remain incomplete. Live Claude chat parity is unverified.

The earlier handoffs, failed outputs, prompt snapshots, reviews, commitments,
and budget records remain historical evidence. This file supersedes their
current-status statements without deleting that history.
