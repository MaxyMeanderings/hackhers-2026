# Independent product review of the revised JSON format contract

Date: 2026-09-09

Decision: **Approve the explicitly authorized contract revision for prospective
evaluation, subject to implementation verification and independent semantic
review.** This does not change any historical outcome or establish a new pass.

The user accepted the recommendation to allow raw JSON or one complete JSON
code fence and authorized continuation. This is an explicit amendment following
the exhausted prior scope; it is not an inferred exception to that budget.
Existing launches, repairs, infrastructure observations, failures, and lineage
must remain recorded. The amendment must state its permitted continuation
budget; this review does not invent an additional allowance or reset counters.

## Product rationale

`docs/AGENT-SPEC.md` defines a conversational workshop coach and four text
deliverables, rather than a raw-JSON API. Exact unfenced JSON was imposed by the
evaluation scenarios. The old failures were valid against that locked contract,
but are weak evidence that the underlying workshop behavior is unusable.

Both final public first-turn responses are single complete JSON fences whose
unchanged inner bodies satisfy the existing first-turn data assertions. This
was checked offline without new model calls. It does not establish their missing
later turns or resolve the earlier semantic failures. Fenced output still fails
an explicit raw-output instruction; record that presentation-compliance issue
separately instead of treating it as failed evidence retention.

## Required acceptance boundary

The prospective evaluator may accept either the original raw JSON document or
one whole JSON code block with only surrounding whitespace. An allowed fence
syntax must be defined narrowly and tested; it must not search arbitrary prose
for a plausible object. The extracted body undergoes the same strict JSON
parsing and unchanged data assertions as a raw response.

Reject surrounding commentary, multiple blocks, malformed or trailing JSON,
duplicate keys, and unsupported fence syntax. Do not fix quotes, fill missing
fields, coerce types, remove unwanted keys, rewrite literals, or reinterpret
content. Expected and prohibited content checks must remain effective, including
privacy checks. Preserve the original completion bytes and record whether the
accepted representation was raw or fenced; extraction must not overwrite the
actual transcript.

Runtime/parser tests and an independent code review must confirm this boundary.
Contract and source identity must be explicit for new evidence. Historical strict
failures remain failures under their original contract; any offline reassessment
must be labeled as a different-contract diagnostic, not a new live execution.

## Remaining evidence obligations

The unchanged source prompt currently has SHA-256
`c30e25155e5030e7ac03021a9d7780de29966a6468ad45b151137d573e9bfdaa`.
The next original-case suite and fresh conversation still require independent
inspection for focused requests, supplied versus inferred counts, causal claims,
source/supplier attribution, privacy, human decisions, experiment scope, and all
four outputs. Presentation tolerance cannot excuse a substantive failure.

This review does not approve the still-unexecuted new suite or conversation,
private gate, merge, deployment, or completion claim. No prompt, oracle, runtime,
historical evidence, or private case was edited or inspected for this product
review beyond the public materials described above.
