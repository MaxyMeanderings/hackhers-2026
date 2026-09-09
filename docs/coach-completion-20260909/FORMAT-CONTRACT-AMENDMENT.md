# Format contract amendment — 2026-09-09

## Authorization and purpose

After reviewing the distinction between presentation and evidence correctness,
the user authorized the proposed change: “please make it so. Need this working
so I can set up the curriculka”. This follows the explicit recommendation to
accept raw JSON or one complete fenced JSON block while retaining strict content
validation and performing fresh Claude-only evaluations.

The workshop specification requires conversational coaching and four readable
deliverables. It does not require every coaching response to be a raw JSON
transport document. Structured public and private proof responses remain useful
for checking retained facts, but a single presentation fence is not a change to
those facts.

## Revised acceptance

The revised proof may accept either an entire raw JSON response or exactly one
complete JSON code block, with only whitespace outside it. The parser may remove
that outer wrapper. It must not search arbitrary prose for a convenient object,
repair malformed JSON, merge multiple blocks, infer missing fields, or discard
contradictory text. Duplicate keys, invalid JSON, and trailing data remain invalid.

All data assertions remain unchanged, including exact final keys, field types,
counts, unknown values, selected features, pre-test thresholds, and result status.
Original response text remains available for prohibited-content checks and
independent semantic review. Conversation history retains actual original model
responses. The runtime's existing strict mode remains the default; this is an
explicit project opt-in.

## History and accounting

The previously sealed raw-JSON runs remain FAIL under their original contract.
The offline extraction diagnostic does not relabel them, execute their skipped
turns, or establish a final proof PASS. Fresh admission, execution, and review
are required under the revised contract.

At authorization, the canonical counters were 11 development launches, zero
final launches, two repairs, and one infrastructure failure. Those counts and
the original failure lineage must remain intact. The contract amendment does
not authorize resetting a ledger or disguising previous failures as fresh work.
The unchanged prompt was first evaluated again with Sonnet and then Opus. Both
suites retained substantive unsupported-premise failures, independent of JSON
presentation. The user's continuation authorization is therefore implemented
as three additional prompt repair attempts, increasing the cumulative limit
from two to five while retaining the two already consumed. This follows the
project's existing three-attempt implementation repair allowance.

The runtime must record an explicit policy amendment with authorization,
independent review, and old/new policy identity before using the increased cap.
This is not a ledger reset. Existing development/final call caps and consumed
launches remain unchanged. Each subsequent canonical prompt repair is charged
against the cumulative allowance. The current failed prompt must be resealed
unchanged for the runtime/contract migration before applying a repaired prompt.

Draft-only supplemental evaluations may run in an isolated temporary workspace
with a byte-identical copy of the portable evaluator and public fixture inputs.
Their exact prompts and responses must be retained; they are development
evidence, not canonical admission or a substitute for charging repairs.

## Product acceptance

All ten original cases and the full six-stage conversation still require
independent semantic review. Fabricated contact counts, unsupported causal
claims, missing source provenance, excessive questions, or incomplete
deliverables remain product failures regardless of JSON parseability.

Coach executions use Claude with subscription authentication and configurable
Claude model selection. The worked example must identify synthetic evidence,
retain real-fieldwork unknowns, and link the actual reviewed conversation.
Live Claude chat parity is not inferred from terminal execution.
