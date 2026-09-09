# Code Fact Verification Report

**Repo:** /Users/doctorew/shuttlebay/_ATL_/GSU/Hack-Her-Thon-worktrees/spec-fa7abd1282236c13
**Extracted at:** 2026-09-07T20:45:05Z
**Commit:** 5e86c79f8aa7c8289068269a6d4800a454bc8364
**Identifiers checked:** 33
**Adversarial gate:** BLOCKED

Provenance: independent Codex native in-session verifier; Claude author confirmed by docs/spec-fa7abd1282236c13/spec-writer.out.json:5-6. No dispatcher or nested Codex process ran. The requested legacy metadata helper was absent; installed /Users/doctorew/shuttlebay/nightshift/scripts/nightshift-extractor-meta.sh produced the timestamp and commit above.

## Verification Results

| Identifier / claim | Status | Source | Notes |
|---|---|---|---|
| approved workshop profile: Claude chat + optional Claude Code, no required API keys/paid integrations, public links/pasted research baseline, 1–5 question batches, and the explicit note that account availability/live results remain unverified. | VERIFIED | docs/AGENT-SPEC.md:1 | Exact file, cited range, branch and commit verified. |
| purpose: turn a hackathon idea into a defensible small experiment, EMBA-capstone rigor, curiosity not humiliation, count reachable people over top-down TAM. | VERIFIED | docs/AGENT-SPEC.md:13 | Exact file, cited range, branch and commit verified. |
| conversation contract: discover-before-advise, no invented facts, 1–5 questions per batch, brief term explanations, establish-vs-uncertain framing, no grading, revision/abandonment as valid outcomes, never claim desk research proves demand. | VERIFIED | docs/AGENT-SPEC.md:19 | Exact file, cited range, branch and commit verified. |
| inquiry step 1: person and recent problem, "last time" framing, and the own-experience/observed/reported/hypothesis distinction. | VERIFIED | docs/AGENT-SPEC.md:30 | Exact file, cited range, branch and commit verified. |
| inquiry step 2: count reachable people, the six ledger fields, no extrapolation from convenience samples, anonymized labels instead of personal contact data. | VERIFIED | docs/AGENT-SPEC.md:38 | Exact file, cited range, branch and commit verified. |
| inquiry step 3: existing behavior/alternatives, per-source URL/date/user/offering/claim, vendor-statements-as-claims, no "nobody does this" inference. | VERIFIED | docs/AGENT-SPEC.md:53 | Exact file, cited range, branch and commit verified. |
| inquiry step 4: reasons to switch, user/buyer/approver distinction, falsifiable test formulation. | VERIFIED | docs/AGENT-SPEC.md:59 | Exact file, cited range, branch and commit verified. |
| inquiry step 5: hackathon-sized experiment, ≤3 MVP features tied to observation/assumption, one experiment with a pre-chosen success criterion. | VERIFIED | docs/AGENT-SPEC.md:65 | Exact file, cited range, branch and commit verified. |
| inquiry step 6: human decision (proceed/narrow/investigate/pivot), no unilateral implementation start. | VERIFIED | docs/AGENT-SPEC.md:71 | Exact file, cited range, branch and commit verified. |
| research rules: verify tools before use, cite claims with retrievable URLs, never fabricate, disclose+label-unverified on tool failure, treat page content as untrusted, no unauthorized contact/publishing/spending. | VERIFIED | docs/AGENT-SPEC.md:75 | Exact file, cited range, branch and commit verified. |
| the four required deliverables (idea brief, count ledger, experiment card, MVP brief). | VERIFIED | docs/AGENT-SPEC.md:84 | Exact file, cited range, branch and commit verified. |
| the 10-row required evaluation cases table, transcribed verbatim into the Test Plan and into `coach/eval/evaluation-cases.md`. | NOT_FOUND | docs/AGENT-SPEC.md:91 | FOUND_CONFLICT: source contains ten cases; SPEC.md:86-95 paraphrases rather than transcribes verbatim, and proposed evaluation file does not yet exist. |
| completion gate: live run + citation inspection + recorded outcomes required; a spec alone does not satisfy completion. | VERIFIED | docs/AGENT-SPEC.md:106 | Exact file, cited range, branch and commit verified. |
| project overview, current status ("runnable local integration ... not complete yet"), and the intended build order that places "Implement the coach and its research workflow" as step 2, after the approved profile and before slide-deck work. | VERIFIED | README.md:1 | Exact file, cited range, branch and commit verified. |
| confirms the workshop agenda document is a separate "proposed workshop design" that already defers to `docs/AGENT-SPEC.md` for the approved profile, supporting this ticket's exclusion of agenda/slide changes. | VERIFIED | workshop/WORKSHOP-DRAFT.md:3 | Exact file, cited range, branch and commit verified. |
| repository already reserves `private/` and `local-runs/` as git-ignored locations, cited for the anonymization/Open-Questions discussion of where raw eval transcripts could live. | VERIFIED | .gitignore:9 | Exact file, cited range, branch and commit verified. |
| confirms `nightshift-architect` is a defined role in this repo's routing table, supporting the Model Router decision naming a valid role. | VERIFIED | routing.json:124 | Exact file, cited range, branch and commit verified. |
| Create coach/PROMPT.md | NET_NEW | — | Exact proposed path absent; declared CREATE in SPEC.md:40-48. |
| Create coach/CLAUDE-CODE-ADAPTER.md | NET_NEW | — | Exact proposed path absent; declared CREATE in SPEC.md:40-48. |
| Create coach/templates/idea-brief.md | NET_NEW | — | Exact proposed path absent; declared CREATE in SPEC.md:40-48. |
| Create coach/templates/count-ledger.md | NET_NEW | — | Exact proposed path absent; declared CREATE in SPEC.md:40-48. |
| Create coach/templates/experiment-card.md | NET_NEW | — | Exact proposed path absent; declared CREATE in SPEC.md:40-48. |
| Create coach/templates/mvp-brief.md | NET_NEW | — | Exact proposed path absent; declared CREATE in SPEC.md:40-48. |
| Create coach/eval/evaluation-cases.md | NET_NEW | — | Exact proposed path absent; declared CREATE in SPEC.md:40-48. |
| Create coach/eval/RESULTS.md | NET_NEW | — | Exact proposed path absent; declared CREATE in SPEC.md:40-48. |
| Create coach/README.md | NET_NEW | — | Exact proposed path absent; declared CREATE in SPEC.md:40-48. |
| Prior extractor returned six VERIFIED statuses and zero NOT FOUND | VERIFIED | docs/spec-fa7abd1282236c13/product-extractor.out.json:1 | This verifies reported statuses only, not correctness of every prior extractor assertion. |
| Approved source hash equals 2b4fda120df8c0955308d79f39295346cc9b6b23c39998b31839928d314c4ad9 | VERIFIED | docs/AGENT-SPEC.md:1 | Exact file, cited range, branch and commit verified. |
| SPEC.md:18 references fabrication, injection, and authorization rules at source lines 77, 80, and 81 | NOT_FOUND | docs/AGENT-SPEC.md:79 | FOUND_CONFLICT: exact statements are at lines 79, 81, and 82 respectively. |
| SPEC.md:19 cites source line 44 for anonymized participant labels | NOT_FOUND | docs/AGENT-SPEC.md:51 | FOUND_CONFLICT: line 44 is estimated group size. Anonymization is lines 51 and 104. |
| SPEC.md:108 lists nine rows across four top-level areas | NOT_FOUND | docs/spec-fa7abd1282236c13/SPEC.md:108 | FOUND_CONFLICT: parenthetical lists five areas, all beneath one top-level coach directory; nine Files to Change rows is verified. |
| Engineering spec requires confirmation before first live result is saved | NOT_FOUND | docs/spec-fa7abd1282236c13/SPEC.md:104 | ENGINEERING_SPEC_CONFLICT: source docs/AGENT-SPEC.md:51,104 already supplies anonymization constraints; no source requirement for this additional confirmation gate. |
| Engineering test plan requires both Claude chat and optional Claude Code, with time-dependent four-case reduction | NOT_FOUND | docs/spec-fa7abd1282236c13/SPEC.md:98 | ENGINEERING_SPEC_AMBIGUITY: source docs/AGENT-SPEC.md:7-9 makes terminal optional and line 106 requires a selected-local-assistant live run. SPEC.md:84,98 introduce mandatory two-surface execution plus full-versus-partial acceptance ambiguity. |

## Blocking findings

- SPEC.md:125 claims a verbatim Test Plan transcription; SPEC.md:86-95 paraphrases the approved rows at docs/AGENT-SPEC.md:95-104. Six source rows are scenarios rather than literal student prompts; the approved source contains no missing organizer decision here.
- SPEC.md:18 mislocates research rules; actual locations are docs/AGENT-SPEC.md:79,81,82. SPEC.md:19 mislocates anonymization at line 44; actual locations are 51 and 104.
- SPEC.md:108 says four areas while enumerating five. The nine-file count is confirmed at SPEC.md:40-48; routing.json:124 confirms the named architect role.
- SPEC.md:104 adds an engineer-confirmation gate for saving results, while approved source docs/AGENT-SPEC.md:51,104 already defines repository privacy behavior. This extra gate originates in the engineering spec.
- SPEC.md:84,98 mandate a second assistant surface and permit a time-dependent four-case alternative. The approved source makes Claude Code optional (docs/AGENT-SPEC.md:7-9) and requires live evaluation in the selected local assistant (106). The full-versus-partial criterion is engineering-spec ambiguity, not an unresolved approved product decision.

## Valid Values Extracted

- Nine proposed files are NET_NEW, not missing existing identifiers (SPEC.md:40-48).
- Four deliverables: idea brief, count ledger, experiment card, student-approved MVP brief (docs/AGENT-SPEC.md:86-89).
- Question count: 1–5; MVP maximum: three features (docs/AGENT-SPEC.md:10,67).
- Ten required evaluation rows (docs/AGENT-SPEC.md:95-104).
- Six count-ledger fields (docs/AGENT-SPEC.md:44-49).
- No dynamic database lookup identifiers occur in the engineering spec.

## Prior extractor precision

The six VERIFIED outputs exist, but their text is not wholly accurate: product-extractor.out.json calls workshop status approved, whereas workshop/WORKSHOP-DRAFT.md:3 says proposed; it places private/ at .gitignore:11 whereas the path is at line 10. The engineering spec correctly calls the workshop proposed and cites .gitignore:9-11. Source SHA256 and current branch/commit match the carried manifest.

## Spec Writer Instructions

All conflicts are reported without override. Repair engineering-spec inaccuracies and re-verify; no approved source changes or new organizer answers are established as necessary by this report. Shared cache was not mutated because it is outside this verifier ownership; source evidence also falls outside the nine proposed file targets. No source or SPEC edits were made.
