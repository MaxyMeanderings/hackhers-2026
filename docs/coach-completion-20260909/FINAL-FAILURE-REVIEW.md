# Independent review of final authorized development failure

Date: 2026-09-09

Decision: **FAIL — stop this bounded repair attempt and preserve an honest
incomplete checkpoint. Do not run final heldouts or merge the coach as complete.**

## Evidence and exact failure

The reviewer read both final first-turn artifacts against the locked public
assertions in `behavior-scenarios.json`, the completion specification, and the
current prompt. Source prompt SHA-256 is
`c30e25155e5030e7ac03021a9d7780de29966a6468ad45b151137d573e9bfdaa`;
the runtime prototype-map digest is
`62cdaa8048965bae4976a21c57177478121497056469ecbeb3a731e5297d4e33`.
Both artifacts belong to seal
`7ec07ec42222d523d0149d663095767c4acf0a7679d31a5199693086778f45a8`.

| Artifact | Scenario | Independent finding |
| --- | --- | --- |
| `development-e8cd4af33a90404d8fb9d6dc3945f34d.json` | `public-evidence` | The entire completion is wrapped in a Markdown JSON fence despite the request for raw JSON. The question-mark assertion passes; all three JSON-field assertions fail because the full response cannot be parsed as JSON. Both prohibited-text assertions pass. The inner content uses scalar `Unknown`, false demand, and unverified source status, so the earlier scalar-versus-ledger ambiguity is not this failure. |
| `development-f58ddeb11c684709bfe12527b8a19d38.json` | `public-experiment` | The entire completion is similarly fenced. The question-mark assertion passes and all nine JSON-field assertions fail at document parsing. A proposed two-feature, five-person experiment is visible inside the fence, but that is not a valid raw JSON completion and does not satisfy the locked format contract. |

Independent strict parsing with Python's `json.loads` rejected both unchanged
completion strings with `Expecting value at position 0`. This is not an
underspecified field-type dispute: the user inputs explicitly request raw JSON,
and the current prompt explicitly forbids Markdown fences. Removing the fences
after execution would alter the observed answer and weaken the oracle rather
than demonstrate that the coach followed the request.

Each response has three focused questions; the five-question product ceiling is
not the observed final failure. Neither response claims a successful experiment
or proven demand. These positive observations do not override the required exact
format. Both conversations stop after their failed first turn; their final
retention turns were not executed under this source revision.

## Accounting and disposition

The reviewer invoked only the read-only runtime status operation. It reports:

- Latest development gate: `fail`, reason `behavior_failed`.
- Failed scenarios: `public-evidence` and `public-experiment`.
- Prototype repairs: 2, matching the specification's two-repair limit.
- Development launches: 11; final launches: 0.
- Infrastructure failures: 1.

The status operation's outer `outcome=pass` means status retrieval succeeded;
the nested latest proof outcome remains fail. It is not a development pass.
The latest receipt still suggests `repair_prototype`, but that generic next-action
label does not grant another repair beyond the exhausted specification budget.
Remaining call capacity does not enlarge the repair allowance.

Preserve the exact completions, failed receipts, prior reviews, and budget history.
Do not change the oracle, strip the fences, resample the unchanged failed prompt,
create a new budget to bypass exhaustion, or launch unused final heldouts.
Any publication must clearly identify an incomplete failed checkpoint; this
review does not approve a completion claim or a merge of the failed coach.

No prompt, oracle, fixture, runtime, or historical evidence was edited. No new
model call occurred. Private heldout bodies remain uninspected and unused by
this review. Any future work requires a separately authorized next scope with
the existing failure and accounting history retained.
