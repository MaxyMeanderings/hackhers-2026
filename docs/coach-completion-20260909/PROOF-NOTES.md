# Proof provenance and scope

The completion follow-up preserves the old failed task and its budget. Its public prototype cases assert exact final-state retention across two real assistant turns each, using strict JSON equality to reject extra fabricated fields. Independent semantic review of the original ten cases and full conversation is still required for the broader product criteria.

Heldout cases were authored by a separate Codex agent, withheld from the implementation author, stored outside all project worktrees, and independently reviewed by Claude through the installed role dispatcher using subscription authentication. That pre-seal private classification review took three calls: two repair findings (insufficient experiment fields, then extra-field fabrication gap), followed by approval. These are separate pre-seal design-review calls, not hidden prototype sampling or replacements after a failed final gate. Raw private cases and reviewer content are not published.

Public challenge and subsequent development/final completions use the repaired runtime and its canonical ledger. The explicit multi-turn profile replays real earlier assistant completions as role-tagged JSON; it is not a native persistent session. The separate full coaching-session evaluation supplies native Claude Code session evidence. Hosted model aliases remain mutable; recorded CLI/version/prompt/source hashes identify the tested invocation, not an immutable hosted backend.

MEX context used: .mex/ROUTER.md, .mex/context/architecture.md, .mex/context/proof-accounting.md, .mex/context/conventions.md, and .mex/patterns/INDEX.md from the Nightshift checkout. No canonical MEX records were changed.
