# Native Source Review

**Verdict:** FAIL — five bounded source findings.
**Extracted at:** 2026-09-07T20:59:40Z
**Commit:** 3fd2b34cd744fb5aee7a9cc9bcc1a9930f45e4b6
**Scope:** coach/PROMPT.md, coach/CLAUDE-CODE-ADAPTER.md, coach/README.md, four coach/templates files. Final source reread after implementation.out.json appeared. Evaluation fixtures and results were not inspected. No source edits; native Codex verification, no nested process or launcher.

## Findings

| ID | Severity | Finding | Evidence |
|---|---|---|---|
| R1 | HIGH | Adapter and README assert identical live behavior follows from identical prompt content. The approved spec explicitly says static identity does not prove behavioral parity. Prompt opening also says behavior is identical either way. | coach/CLAUDE-CODE-ADAPTER.md:4-6,28-30; coach/README.md:21-23; coach/PROMPT.md:6; SPEC.md:69,100 |
| R2 | MEDIUM | Citation rule is restricted to deliverables; approved source applies to externally verifiable claims generally, including conversation. | coach/PROMPT.md:60-62 versus docs/AGENT-SPEC.md:78 |
| R3 | MEDIUM | README refers users to another file for terminal setup but contains no actual start-session/load-prompt procedure. AC12 requires determining how to start the optional session without leaving README. | coach/README.md:20-24 versus SPEC-DIGEST.md:17 |
| R4 | MEDIUM | Adapter asserts this ticket's live evaluation exercises the paste-based path, although its author expressly disclaims inspection of evaluation evidence. This source review has no evidence supporting the assertion. | coach/CLAUDE-CODE-ADAPTER.md:34-35; docs/spec-fa7abd1282236c13/implementation.out.json:9 |
| R5 | LOW | Prompt sends feature-negotiation readers to Section 6; negotiation actually appears in Section 5. | coach/PROMPT.md:138 versus 152,162 |

## Six-Lens Evidence

- **DRY:** canonical prompt is referenced by adapter, while embedded deliverable fields and standalone templates currently correspond (PROMPT.md:171-211; templates/idea-brief.md:7-49; count-ledger.md:11-42; experiment-card.md:7-30; mvp-brief.md:11-40).
- **SOLID:** prompt, loading instructions, student README, and templates are separate artifacts (respective file headings). No class/interface surface exists in these seven markdown files.
- **ACID:** no persistence transactions are implemented in these files. Unknown counts and distinct estimates/contact/problem/commitment fields are retained (PROMPT.md:101-109; templates/count-ledger.md:3-42).
- **Convention:** the incorrect section reference is R5; README self-contained setup gap is R3. CLI flag names match recorded cli-help.txt:25,126,164,223,250; no fresh API/CLI evaluation is claimed by this review.
- **Big O:** no executable iteration/data structure implementation exists in this source scope. Question batches are bounded 1–5 and MVP features at three (PROMPT.md:38-41,137,154-160).
- **LLM trust:** untrusted pasted/retrieved instructions cannot redirect task; contact/publication/account/spending actions require authorization; anonymization and human decision remain explicit (PROMPT.md:63-73,147-150). Account provenance categories are preserved (88-93; templates/idea-brief.md:13-17). Citation coverage and unsupported parity/evaluation assertions are R1/R2/R4.

All four deliverables and their required fields exist; this is static source evidence, not proof that a live assistant produces them correctly (PROMPT.md:171-211). No finding establishes a missing organizer decision.
