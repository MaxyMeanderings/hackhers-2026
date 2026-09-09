# Independent source and acceptance review

Date: 2026-09-09

Decision: **APPROVE the source and documentation checkpoint for final proof execution**. The selected terminal runtime has the reviewed ten-case and full-conversation evidence. Live Claude chat parity remains unverified. Final proof is pending; this document is not a release-proof PASS or authorization to represent all surfaces as tested.

Reviewed authorities: `docs/AGENT-SPEC.md` and this task's `SPEC.md`. Reviewed implementation and documentation: both READMEs, `coach/PROMPT.md`, `coach/CLAUDE-CODE-ADAPTER.md`, all four templates, `coach/eval/run.py`, evaluation cases/results, and the populated example. Behavioral conclusions use the independently reviewed actual responses, not prompt instructions alone.

Source identity at review:

- `coach/PROMPT.md`: `c74966e3cb5c86801fe5d30aa410f6f14edb8a1ce755001a3b94d2fb4b2386e1`.
- `coach/eval/run.py`: `55a41ca4e7951502fd301b3563d699e6376b91f0848075e6983f46ddc21d2d27`.
- `coach/examples/study-session.md`: `63ec36e949e2a1684f20dc30d55bd686c54fb3b1c4a2fe683834b96fa73fc0be`.

| AC | Assessment | Evidence and limit |
| --- | --- | --- |
| 1 | Supported in the selected terminal samples; chat not executed | Cases 01–03 and 07 discover idea/origin and do not jump to feature advice. The no-user case offers a tentative discovery step, as required by the product's own evaluation row. This is not verification of the literal fresh-chat surface. |
| 2 | Supported in reviewed samples | Ten-case, five-turn, and public-development reviews inspect focused requests beyond numbering. A single behavior question across several people counts as one focused question; distinct requested fields count separately. The original stricter participant-multiplication finding and its reasoned withdrawal remain in `PUBLIC-DEVELOPMENT-FORMAT-REVIEW.md`. Some replies exceed the prompt's preferred three pieces but remain within the product's five-question ceiling. |
| 3 | Supported with wording limits | Unknown contact counts, uncertain causal links, outlier behavior, source limits, and Not run survive the reviewed cases and final summaries. Known precision caveats include “working for polling” and “as usual” inside a proposed action; they are not presented as clean wording or hidden from the results. No new material fabricated ledger/result/decision failure is established. |
| 4 | Supported in sampled terms | Case 02 explains TAM; case 08 explains MVP in beginner language. This does not demonstrate every possible unfamiliar term. |
| 5 | Supported | Ordinary replies separate established evidence and unknowns. Exact requested structured summaries use their requested fields instead of adding recap prose. The full conversation preserves account type separately from synthetic mode. |
| 6 | Supported by complete five-turn session | `CONVERSATION-REVIEW-OPUS-REPAIR2.md` maps observed person/problem, six counts, sourced alternative/current behavior, switching/disconfirmation, one measurable experiment, and explicit human decision. Supplied observation provenance and six real Unknowns remain intact. |
| 7 | Supported for tool-free fallback and supplied research | Cases 04–06 disclose unavailable browsing and do not invent product facts. The conversation preserves facilitator and Google vendor attribution beside the supplied URL/date. Independent vendor-page inspection supports the limited collection/chart/export claims. Live coach browsing is not established. |
| 8 | Static common-prompt criterion satisfied; live parity unverified | README and adapter reference the same canonical prompt. Results expressly distinguish print-mode evaluation from Claude chat and interactive paste. The task's D1 mapping permits documentation inspection while retaining that limit; a shared file does not prove equivalent behavior. |
| 9 | Supported | The final actual conversation response populates Idea Brief, Count Ledger, Experiment Card, and MVP Brief. The example contains that complete response unchanged. Both timing/reminder criteria, Not run, Team A, approval date, and Proceed are retained. |
| 10 | Supported | Case 08 negotiates two features, each exercised and observed in one paper-grid experiment with explicit assumptions. Full conversation likewise retains two selected features, each tied to the test. Public final summary retains the student's single selected reminders feature. |
| 11 | Satisfied for selected live-evaluation runtime | All ten original case rows remain verbatim. All ten actual c749 prompt responses have independent semantic judgments recorded in `coach/eval/RESULTS.md`; full conversation and citation inspection are linked. Historical failed suites remain separate. Supplemental runs used an isolated copy with the exact subsequently applied prompt; later helper metadata/auth/default changes are disclosed. |
| 12 | Satisfied by documentation inspection | `coach/README.md` contains direct chat startup, optional terminal startup, prompt/template/evaluation links, account expectations, and model configuration. A student need not leave that file to understand either startup path. |

## Source and documentation checks

Local Markdown targets in both READMEs, adapter, results, and worked example resolve. The example includes the complete actual turn-5 output exactly. The ten original Case/Expected behavior rows match the product specification. The evaluator compiles, defaults to Opus with environment/argument overrides, records the requested selector separately from reported model identifiers, removes API/provider overrides, and gates on logged-in first-party Claude subscription authentication. Its exclusive evidence writes and actual session resume remain visible in source. This review did not launch the evaluator or claim a fresh model call using the helper's latest metadata changes.

The adapter distinguishes its tool-free system-prompt command from interactive paste. It makes no unsupported promise of model/account parity or browsing. The count template distinguishes reported problems from contact provenance. All four templates retain the product's required fields and human approval boundary.

`coach/eval/RESULTS.md` accurately scopes the ten-case and full-session passes, source inspection, public development receipt, model identifiers, and preserved historical failures. It retains imprecise wording and finite-sample limitations. `FINAL-PROOF.md` currently states pending execution and explicitly says that the supplemental/public evidence does not replace final proof. No private case body was inspected during this review.

Final proof must bind the actual final source and preserve cumulative accounting. Any later implementation change requires its applicable verification and source binding. Updating the excluded task proof record after execution must report the actual outcome; this review must not be cited as having already observed it.

## Final helper model-selector refinement

The earlier helper hash above is preserved as the preceding reviewed state. Current `coach/eval/run.py` SHA-256: `00287dd8cd8c6fe2b6136dfbf451d702d1b847e7b3d3394ddca1ec34e6737e19`. The empty `COACH_EVAL_MODEL` value now falls back to `opus`; explicitly blank or whitespace-only `--model` values are rejected before authentication or any subprocess. Independent checks exercised both rejected argument values with a subprocess guard and evaluated the empty-environment fallback. No model or authentication calls occurred. The prompt remains unchanged. This narrow refinement is approved; the prior source/documentation disposition remains in effect for this updated helper.
