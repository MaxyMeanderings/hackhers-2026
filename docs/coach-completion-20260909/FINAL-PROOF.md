# Final release proof

Status: **FAIL — release is not verified.**

The canonical private final run and the subsequent read-only final gate both returned `behavior_failed`. Four final model calls executed: three turns passed and the last turn failed its local oracle. The sanitized receipt is [proof-final-format.json](proof-final-format.json). The failed case identifier is public commitment metadata; private inputs and completions are not published.

The ten original cases, full five-turn conversation, and public development gate passed, as recorded in `coach/eval/RESULTS.md`. Those results do not waive the failed private final gate. No final PASS or verified merge is authorized by this checkpoint.

All thirteen frozen source hashes in [static-source-identity.json](static-source-identity.json) still match after execution. The canonical prompt remains `c74966e3cb5c86801fe5d30aa410f6f14edb8a1ce755001a3b94d2fb4b2386e1`; the evaluator remains `00287dd8cd8c6fe2b6136dfbf451d702d1b847e7b3d3394ddca1ec34e6737e19`. Execution used the pinned Claude CLI and subscription authentication.

Retained totals are sixteen development launches, four final launches, three repairs used against the amended cumulative limit of five, and one infrastructure failure. Historical failures and policy amendments remain recorded. No private-failure-driven adaptation or retry has occurred. The runtime requires independently reviewed heldout replacement before further eligible final proof; changing a commitment alone does not establish success.

Final execution intentionally retains completion hashes and outcomes rather than private response bodies. The exact failed assertion cannot be reconstructed from the sanitized receipt; no semantic diagnosis is claimed.
