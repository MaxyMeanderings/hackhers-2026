# Proof handoff — pending, not complete

> Superseded current status: [laptop continuation](LAPTOP-FINAL-STATUS.md).
> Development has now failed with both repairs consumed; no final calls ran.
> Do not restore the historical pre-seal snapshot over the current ledger.

User changed priority to transferring the unfinished work to a laptop. No new provider calls should be launched until that continuation is intentionally resumed.

No spec-lock commit, scope activation, behavioral seal, development prototype execution or final heldout execution has occurred for this task. One canonical public challenge ran and returned repair; its attempts/counters/outcomes are retained in proof-ledger-checkpoint.json and challenge-attempt1.json. Old failed task budgets remain unchanged.

Existing heldout candidates are EXPOSED to the implementation author: process inspection printed a Claude argv containing private review input into the parent context. No final proof may use any existing heldout body or commitment. Discard their eligibility, not their historical evidence. Before any future seal, an independent agent must author fresh private cases outside all checkouts and outside Git, obtain actual independent classification review, and replace the public commitment. Preserve the original review/exposure history; do not relabel exposed cases as hidden.

The public behavior-scenarios.json is an UNAPPROVED DRAFT. Its heldout commitment still points to an older now-ineligible candidate. Its strengthened structural operators require the runtime follow-up currently being completed. Existing challenge.json describes the earlier design and cannot authorize the revised draft. PROOF-NOTES.md describes an earlier pre-seal checkpoint and is superseded by this handoff for current call counts and eligibility.

The sanitized ledger checkpoint contains public attempts, counters, outcomes and digests only; it contains no private bodies or private locators. It is a transfer record, not a gate-PASS receipt or a way to manufacture a fresh ledger. The byte-identical proof-ledger-state.json preserves the complete canonical pre-seal state, including its empty seal history. To restore on a new clone only when no task state already exists, place it under the Git common directory at nightshift/behavior-proof/coach-completion-20260909/state.json and validate it with the helper status operation; reconcile rather than overwrite an existing ledger. This follows the runtime ledger path and schema in scripts/nightshift-behavior-proof.py (Proof.__init__, Proof.initial and Proof.transaction). Preserve the recorded challenge failure. On the laptop, verify task and repository identity, runtime revision, provider subscription login, actual Claude CLI version and executable before re-challenging. Paths and CLI version in the unsealed public draft must be revised and independently reviewed for the new machine. Do not copy authentication credentials or private fixture files into Git.

Required continuation: finish runtime structural oracle repair and tests; freeze source prompt; independently replace exposed heldouts; validate and challenge revised public scenarios; annotate actual classification approvals; activate new-task scope and lock SPEC/scenarios; seal; run development proof; complete original ten-case/full-conversation semantic review and final docs; run fresh final proof; commit/push only with honest checkpoint or completed status.

Five private design-review calls completed before the handoff (excluding the initial sandbox authentication failure): repair, repair, approve, revised-design repair, final revised-design approve. Their bodies are now exposed/ineligible and are not transferred publicly. No proof prototype calls occurred.
