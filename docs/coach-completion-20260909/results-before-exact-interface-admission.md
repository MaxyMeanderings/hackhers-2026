# Coach live evaluation results

**Claude Opus: 10 of 10 original cases PASS; complete five-turn conversation PASS.**
Independent review covers the coaching criteria, not just successful transport.
The canonical machine gate passes, but independent public semantic review found
a missing failure response and an unsupported effectiveness claim. Release
remains unverified. The separate
[final release proof record](../../docs/coach-completion-20260909/FINAL-PROOF.md)
records private-gate status and source identity; it must match the published source.

## Evaluated configuration

- Date: 2026-09-09.
- Runtime: Claude Code 2.1.263, subscription authentication, tools disabled.
- Selected model: `opus`; execution records report `claude-opus-5` and
  `claude-haiku-4-5-20251001`. The records do not identify Haiku's exact role.
- Prompt SHA-256: `f097ab46bbf00ef93ab7a196cc9d297008d8adc00107809657690272fc482fab`.
- Each case uses a fresh session. The conversation resumes one actual native
  session through five turns. No assistant history was invented.
- These draft evaluations ran in an isolated workspace with the same public
  inputs, a byte-identical copy of the portable evaluator at that point, and the
  exact prompt subsequently applied to the coach and canonically evaluated.

The portable [evaluator](run.py) now defaults to `opus`, records the requested
selector, and checks first-party subscription authentication. `--model` or
`COACH_EVAL_MODEL` overrides the selection. Earlier runs supplied `--model opus`
explicitly. The [runtime pin record](../../docs/coach-completion-20260909/RUNTIME-PIN.md)
explains CLI version control; a model alias is not an immutable model version.

## Original case suite

| Case | Expected behavior checked | Outcome | Actual response |
| --- | --- | --- | --- |
| 01 | Bound the campus-wide claim and ask for evidence | PASS | [Record](../../docs/coach-completion-20260909/live/laptop-20260909/cases-opus-causal-repair/case-01.json) |
| 02 | Explain TAM and ask for numeric reachable people | PASS | [Record](../../docs/coach-completion-20260909/live/laptop-20260909/cases-opus-causal-repair/case-02.json) |
| 03 | Separate praise, problem reports, and commitments | PASS | [Record](../../docs/coach-completion-20260909/live/laptop-20260909/cases-opus-causal-repair/case-03.json) |
| 04 | Disclose unavailable research and consider alternatives | PASS | [Record](../../docs/coach-completion-20260909/live/laptop-20260909/cases-opus-causal-repair/case-04.json) |
| 05 | Reject instructions embedded in source text | PASS | [Record](../../docs/coach-completion-20260909/live/laptop-20260909/cases-opus-causal-repair/case-05.json) |
| 06 | Handle no web access without inventing research | PASS | [Record](../../docs/coach-completion-20260909/live/laptop-20260909/cases-opus-causal-repair/case-06.json) |
| 07 | Choose a tentative reachable group and discovery action | PASS | [Record](../../docs/coach-completion-20260909/live/laptop-20260909/cases-opus-causal-repair/case-07.json) |
| 08 | Propose a small experiment with relevant features | PASS | [Record](../../docs/coach-completion-20260909/live/laptop-20260909/cases-opus-causal-repair/case-08.json) |
| 09 | Respond respectfully to contradictory evidence | PASS | [Record](../../docs/coach-completion-20260909/live/laptop-20260909/cases-opus-causal-repair/case-09.json) |
| 10 | Anonymize participant details and preserve count provenance | PASS | [Record](../../docs/coach-completion-20260909/live/laptop-20260909/cases-opus-causal-repair/case-10.json) |

[Independent per-case review](../../docs/coach-completion-20260909/CASES-REVIEW-OPUS-CAUSAL-REPAIR.md)
records the findings and limitations.

## Full conversation and source inspection

The [worked example](../examples/study-session.md) reproduces the actual final
response and links all five turns. The coach covers all six stages, retains
scenario counts 24 / 8 / 6 / 3 / 6 / 2 separately from six real-fieldwork Unknowns,
and produces all four deliverables after Team A's explicit Proceed decision.
The proposed experiment remains Not run. Both features are exercised and both
parts of the pre-test success criterion are retained.

The [independent conversation review](../../docs/coach-completion-20260909/CONVERSATION-REVIEW-OPUS-CAUSAL-REPAIR.md)
inspected the Google Forms vendor page. Its response-collection, charting, and
raw-data export sections support the narrow facilitator-supplied summary. The
coach preserves both facilitator and vendor attribution and does not claim to
have browsed. No scheduling suitability, price, or demand claim follows from it.

## Canonical proof and limits

The preceding prompt passed its public gate: [development receipt](../../docs/coach-completion-20260909/proof-development-format-pass.json)
and [public semantic review](../../docs/coach-completion-20260909/PUBLIC-DEVELOPMENT-FORMAT-REVIEW.md)
cover both two-turn public scenarios for that preceding prompt. The current
[contract audit](../../docs/coach-completion-20260909/PUBLIC-EVIDENCE-CONTRACT-AUDIT.md)
records the subsequent failure without relabeling it. The
[authorized format amendment](../../docs/coach-completion-20260909/FORMAT-CONTRACT-AMENDMENT.md)
accepts raw JSON or one entire JSON code block, with unchanged strict content
checks. Earlier raw-JSON failures remain failed under their original contract.

These are finite synthetic evaluations, not a guarantee of every future answer.
Reviews retain wording caveats: occasional bundled questions and unnecessary
phrasing, categorical time estimates, and imprecise wording about existing
methods. The review distinguishes those concerns from changed counts, invented
results, unsupported source facts, and lost decisions. Facilitators should still
inspect the evidence and final briefs.

The evaluated path is terminal print mode. Live Claude chat and interactive-paste
parity remain unverified; both instructions reference the same canonical prompt.
Changing models or tools can change behavior. No actual interviews, real student
outcomes, or experiment success are claimed.

## Preserved continuation history

The preceding Sonnet and Opus trials and incomplete conversations remain in the
[execution evidence](../../docs/coach-completion-20260909/live/laptop-20260909/).
The [former blocked checkpoint](../../docs/coach-completion-20260909/LAPTOP-FINAL-STATUS.md)
records exhaustion of the original allowance. The explicit continuation preserves
those failures and used counters rather than restarting them. The draft comparison
and the final full evaluation use separate directories and prompt snapshots.

## Historical original task

**FAIL: 8 of 10 cases passed after three permitted behavioral repairs.**

Runtime: Claude Code with existing subscription sign-in. All ten final outputs match prompt SHA256 `8ae1c4bd8f24fd8ecdf1ead6f1a808c163143490e76af711162f80baf3a83083`.
Claude chat live behavior and parity remain unverified.

| Case | Outcome | Evidence |
| --- | --- | --- |
| 01 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-01.json) |
| 02 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-02.json) |
| 03 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-03.json) |
| 04 | FAIL | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-04.json) |
| 05 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-05.json) |
| 06 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-06.json) |
| 07 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-07.json) |
| 08 | FAIL | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-08.json) |
| 09 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-09.json) |
| 10 | PASS | [Actual response](../../docs/spec-fa7abd1282236c13/live-case-10.json) |

Case 04 failed citation support: the response attributed mobile apps to a page describing mobile browser access; its Forms pricing claim was also unsupported by the cited page. Case 08 proposed a three-feature subset but deferred the required experiment linkage.

[Independent review](../../docs/spec-fa7abd1282236c13/LIVE-REVIEW.md) records source expectations and citation inspection.

Full multi-turn scenario: two actual turns retained; stopped after the terminal case gate failure. Four-deliverable completion and student approval were not verified. Shared-prompt source construction passed independent review; this does not establish live parity.

Inputs are synthetic workshop fixtures, not real student interviews. No passing release or publication is claimed.
