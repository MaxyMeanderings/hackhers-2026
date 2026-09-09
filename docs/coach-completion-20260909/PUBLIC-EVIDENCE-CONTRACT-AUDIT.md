# Public evidence contract audit

Date: 2026-09-09

Decision: the retained machine failure is valid under the sealed oracle, but the first-turn contract has a material ambiguity between factual counting and the intended synthetic-ledger sentinel. This mismatch does not demonstrate that the coach invented real interviews or promoted synthetic evidence into real demand.

## Reviewed public evidence

- `behavior-scenarios.json`, public evidence case, first and second turns.
- `development-801914e7822e46e186052ba2bf31bd39.json`.
- `coach/PROMPT.md`, SHA-256 `f097ab46bbf00ef93ab7a196cc9d297008d8adc00107809657690272fc482fab`.
- `docs/AGENT-SPEC.md`, the task `SPEC.md`, and the count-ledger template.

No private fixture, private expected value or private completion was inspected for this audit. No provider calls or source, oracle or ledger edits were performed.

## What failed

The first-turn oracle requires `real_interviews` to equal the exact string `Unknown`. The retained completion instead supplies a string beginning with zero, explicitly attributing that zero to the student's statement that no real interviews have happened, followed by other real-fieldwork entries marked Unknown. The recorded assertion results show that this equality is the failed expected assertion; the demand and source-status assertions pass. The permitted whole JSON fence is not the failure.

The runtime correctly rejects the nonmatching string. Preserve this observation as FAIL under its original seal. The audit does not authorize changing its judgment or editing the ledger.

## Contract assessment

The first student request expressly says “No real interviews have happened” and asks for “the ledger entry for real interviews.” It does not request the exact literal `Unknown`. An attributed zero is a natural factual reading of that supplied statement, not an invented interview count. The original product specification requires unknown counts to remain unknown and prohibits invented evidence; it does not require converting an expressly supplied absence of interviews into an unknown count.

The canonical prompt and template separately establish a convention that real-fieldwork counts in synthetic practice remain Unknown unless actual fieldwork is supplied. That supports the oracle author's intended sentinel. However, the request also expressly supplies a real-interview absence, and the prompt instructs the coach to preserve supplied facts. Whether that absence is to be treated as a literal count or ignored for the sentinel convention is not made explicit in the first request. The prose-rich string also falls short of the intended single ledger value, but that formatting defect is distinct from fabricated fieldwork.

The second student turn has no such ambiguity: it explicitly requests the exact string `Unknown` for the synthetic exercise. Its exact-literal oracle is aligned with the request. The first turn should state the same convention if literal equality is the desired acceptance contract.

## Prospective resolution

Do not broaden the existing equality merely to accept this observed response, and do not relabel the failed attempt. If the product requires the synthetic sentinel regardless of the explicitly stated absence of interviews, clarify that rule in the public first-turn request prospectively, obtain independent review, and use the supported lock/challenge/reseal workflow while retaining every failure and consumed counter. This keeps the intended exact oracle and removes the ambiguity instead of teaching the coach to suppress ordinary factual zero counts generally.

If the product instead wants factual interview counts whenever explicitly supplied, that is a different acceptance decision and must be reviewed as such. This audit does not make that change. It also does not certify all other coaching semantics or question batching in the completion; its scope is the identified first-turn field contract.
