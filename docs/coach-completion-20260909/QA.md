# Coach completion static QA

Date: 2026-09-09

Status: static checks passed. The reported evaluator-default edge case is resolved. Private final proof and publication are separate gates; consult `FINAL-PROOF.md` for their current status.

## Checks performed

| Check | Result |
| --- | --- |
| Source and templates against product/task specifications | No material scope drift; see `DRIFT.md` |
| Relative Markdown links in root README and coach documents | All 67 targets resolve |
| Worked example provenance | Body equals the actual fifth conversation output exactly, followed by one document newline |
| Worked example conversation links | All five recorded turn files exist |
| Final original case inputs | All ten match `docs/spec-fa7abd1282236c13/eval-inputs.json` |
| Final case/conversation identity | All 15 records match prompt SHA-256 `c74966e3cb5c86801fe5d30aa410f6f14edb8a1ce755001a3b94d2fb4b2386e1`, report unchanged prompt and successful nonempty completions |
| Recorded CLI/model identity | Claude Code 2.1.263; reported identifiers `claude-opus-5` and `claude-haiku-4-5-20251001`, with Haiku's role explicitly unspecified |
| Evaluator Python syntax | Valid |
| Authentication rejection | Three mocked identities rejected before version or model launch: logged out, API-key authentication, and non-first-party provider |
| Environment sanitization | All nine API-key, base-URL and alternate-provider override variables removed |
| Requested model provenance | The helper now records `selected_model`; prior final runs supplied Opus explicitly |
| Count-ledger provenance | Problem reports no longer assume membership in the counted contacts |

The authentication checks were independently executed with mocked subprocess results. No provider executable, model call, network operation, output evidence directory or consumer ledger mutation occurred during these checks. File existence and response identity checks do not by themselves certify model behavior. Semantic PASS judgments and citation inspection are attributed to `CASES-REVIEW-OPUS-REPAIR2.md`, `CONVERSATION-REVIEW-OPUS-REPAIR2.md` and `PUBLIC-DEVELOPMENT-FORMAT-REVIEW.md`.

## Resolved default-model edge case

At initial inspection, an explicitly empty `COACH_EVAL_MODEL` environment value selected an empty string and omitted the model argument, permitting an unintended CLI default. The adapter already treats an empty value as Opus. The helper now falls back to Opus for an empty environment value and rejects explicit empty or whitespace-only selectors before authentication. Independent offline checks confirmed both rejection cases and the empty-environment fallback. This correction concerns future reproducibility; all 15 final evaluation records used explicit Opus.

## Limits

This review covers the local files and offline safeguards above. It does not re-run live evaluations, open external product pages, inspect private cases or establish live Claude chat/interactive-paste parity. The independently reviewed source citation and actual experiment/approval evidence remain linked from the results and worked example. The final release must satisfy the private gate against the final published source; current status belongs in `FINAL-PROOF.md`.

## Reviewed source identity

`static-source-identity.json` records SHA-256 values for all 13 scoped product/configuration files at this review. The final private receipt must bind the final source independently.

- Evaluator: `00287dd8cd8c6fe2b6136dfbf451d702d1b847e7b3d3394ddca1ec34e6737e19`.
- Canonical prompt: `c74966e3cb5c86801fe5d30aa410f6f14edb8a1ce755001a3b94d2fb4b2386e1`.
- Worked example: `63ec36e949e2a1684f20dc30d55bd686c54fb3b1c4a2fe683834b96fa73fc0be`.
