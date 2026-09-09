# Independent semantic review of retained public development outputs

Date: 2026-09-09

Decision: **Request changes; preserve the failed gate**.

Reviewed all three retained public development artifacts for seal
`7ec07ec42222d523d0149d663095767c4acf0a7679d31a5199693086778f45a8`
against `behavior-scenarios.json` and the source prompt at SHA-256
`336f5ad322a9317ec62b3aee1152477a95673c7770874bd281719695b1e9d0f5`.
The artifact `prompt_sha256` is the runtime's prototype-map digest
`d90673ef632c894be0c3cb06c4bf86c0a051baea348dc1ba8a8a303a7822294f`,
not the standalone prompt file hash. Only public inputs and completions were read.

## Evidence scenario: first turn

Artifact: `development-27567493b0b9413aa6b0f0811efc6d7f.json`.

The runtime records failure of the assertion requiring `real_interviews` to equal
the scalar string `Unknown`. The response instead returns a six-field ledger
object whose values are all `Unknown`. The other expected and prohibited
assertions are satisfied.

This is a genuine mismatch against the sealed oracle, but the input is
underspecified: it calls the field “the ledger entry for real interviews” without
giving its JSON type. The whole-ledger interpretation is plausible alongside the
prompt's instruction to keep six real-fieldwork counts. The output does not
fabricate real interviews, set missing counts to zero, or claim demand. The
second scenario turn explicitly requests scalar `Unknown`, but was not executed
after the first-turn failure and cannot retroactively disambiguate that request.

A generic repair is legitimate: individual count fields or individual ledger
entries should contain their scalar value or `Unknown`; a whole ledger is
returned only when requested. Explicit user-requested types and structures must
remain higher priority. This improves predictable summaries without changing the
sealed oracle or coaching the model with private cases. The recorded failure
must remain a failure; this ambiguity does not authorize a pass or free retry.

The response contains five focused questions in one string and keeps names and
URLs out. It distinguishes praise without commitment and unsupported demand
claims. Its third question asks whether to treat an unsourced claim as unverified;
the coach should maintain that classification directly rather than make evidence
integrity optional. The `source_status` field itself remains unverified.

## Experiment scenario: first turn

Artifact: `development-1b2465ace39c42d39ab3a0378d51875c.json`.

All machine assertions pass. The response proposes two features and a concrete
five-person test with an observable awareness measure and a matching four-of-five
threshold. It distinguishes reported missed changes from the hypothesis that
reminders/calendar functionality might help, keeps recurrence and switching
unverified, and records `not run` and no proven demand.

One substantive semantic gap remains: the question about “the other 3 reachable
members” assumes the two people reporting missed changes belong to the five
reachable members. The input gives those groups separately without establishing
their overlap. Ask whether the reporting members are among the reachable group
before subtracting them. There are four focused questions; they are in the
requested questions string but are not numbered as the prompt requires.

The evidence rationale is a paraphrase rather than the prompt's short exact quote,
and gives a combined reminder/calendar rationale rather than distinct per-feature
bases. These are instruction-compliance gaps even though the main causal
distinction is maintained. The provisional card does not state what changes if
the result disappoints; a full experiment deliverable still needs that decision
rule. The narrow machine assertions do not establish those omitted semantics.

## Experiment scenario: second turn

Artifact: `development-bd8c3eb7c93c43189c1e2388c994f857.json`.

Machine and semantic retention pass for this bounded turn. The response preserves
the selected single reminder feature, five participants, changed-event response
action, three responses within 24 hours, assumption basis, scalar real-interview
Unknown, no proven demand, and not-run result. It supplies only the requested
JSON object without additional features or prose.

This is not a pass for the whole development gate or the full product. The
evidence scenario's second turn is absent. The third original-case suite and a
complete six-stage conversation require separate semantic review. No oracle,
prompt, fixture, or runtime was edited during this review.
