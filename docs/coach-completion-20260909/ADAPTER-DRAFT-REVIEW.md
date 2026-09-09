# Independent adapter draft review

Date: 2026-09-09

Draft: `/private/tmp/coach-adapter-draft.md`

SHA-256: `f29cf8326512cee21636e153d6fc9e172c8cd7cd45227975fde8c4c74a82dae2`

Decision: **One documentation correction requested** before copying the draft
into `coach/CLAUDE-CODE-ADAPTER.md`.

The statement that the evaluator uses fresh print-mode sessions needs to
distinguish its modes. `coach/eval/run.py` runs independent cases with
`--no-session-persistence`; conversation mode creates a `--session-id` and uses
`--resume` for subsequent turns. Recommended wording: independent cases use
fresh sessions, while the full conversation resumes an actual Claude session.
Both use print-mode calls and the canonical system-prompt file.

The draft's target-relative links to `PROMPT.md`, `eval/RESULTS.md`, `eval/run.py`,
and `templates/` resolve. The evaluator removes the listed authentication and
alternate-provider environment overrides, supports `--model` and
`COACH_EVAL_MODEL`, and requires a logged-in `claude.ai` authentication method.
The draft additionally asks the student to check `apiProvider=firstParty`; the
harness does not explicitly test that field, so the documented manual check
must not be described as an identical implemented condition.

Local CLI help supports safe mode, explicit MCP configuration, empty built-in
tools, model choice, and session resumption. The file-based system-prompt flag
and its interactive/non-interactive applicability are documented in the
[official CLI reference](https://code.claude.com/docs/en/cli-reference), inspected
on 2026-09-09. The linked
[official quickstart](https://code.claude.com/docs/en/quickstart) also resolves.

The reviewer performed a non-billing, sanitized authentication-status lookup
after removing the documented overrides. In this sandbox it returned exit 1,
`loggedIn=false`, `authMethod=none`, and `apiProvider=firstParty`. This confirms
the response fields but does not establish successful authentication or the
host's sign-in state. No credentials or account identifiers were printed, and
no model request or interactive session was launched.

The draft accurately distinguishes common instructions from proved surface
parity. No sealed source was edited during this review.
