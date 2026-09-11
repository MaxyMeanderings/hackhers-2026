# Stage 3 — stop eyeballing runs, test a fixed case list

One manual run only tells you about one input. Stage 2 ended by noticing a
*second*, untested failure mode (the coach still leaning toward giving a
verdict). The fix for "I might be missing failure modes" is a fixed list of
cases you rerun after every prompt change — exactly what
[`coach/eval/evaluation-cases.md`](../../coach/eval/evaluation-cases.md)
is: ten synthetic student lines, each targeting one named failure
(`coach/eval/evaluation-cases.md:3-49`).

## Why you can't just point the real harness at prompt-v2.txt

[`coach/eval/run.py`](../../coach/eval/run.py) hardcodes its target prompt —
`PROMPT = ROOT / "coach/PROMPT.md"` (`coach/eval/run.py:20`) — and refuses to
run if that file changes mid-evaluation (`coach/eval/run.py:72-74`, "Prompt
changed during evaluation"). That's deliberate: it stops an evaluation from
silently grading a different prompt than the one in the recorded SHA. It also
means the harness is not a generic tool you point at any file — for a toy
prompt, you build the same shape by hand, one case at a time.

## The one-case-at-a-time pattern, extracted from the real harness

This is the actual `claude` invocation `run.py` builds per case
(`coach/eval/run.py:75-81`), with the prompt path swapped to the toy prompt:

```sh
claude -p --output-format json --safe-mode \
  --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
  --tools "" --permission-mode dontAsk --max-turns 8 \
  --system-prompt-file workshop/build-track/prompt-v2.txt \
  --model opus --no-session-persistence -- \
  "There are no competitors. My idea is a form for a student club to collect study-session availability."
```

Run it once per case in
[`coach/eval/evaluation-cases.md`](../../coach/eval/evaluation-cases.md),
swapping the last argument for each case's "Runnable synthetic student
prompt," and read each JSON `result` field against that case's "Expected
behavior" column. That is literally independent review, not a pass/fail the
model reports on itself — `run.py` never grades output; every record ships
with `"judgment": "PENDING_INDEPENDENT_REVIEW"` (`coach/eval/run.py:90`) for
a human to close.

## What the real harness adds beyond this

`coach/eval/run.py` is this same loop, made repeatable: it strips
API-key/Bedrock/Vertex/Foundry environment overrides and checks first-party
subscription auth before it will run (`coach/eval/run.py:29-37`,
`coach/eval/run.py:60-64`), refuses to overwrite existing evidence
(`coach/eval/run.py:70-71`), and records the prompt's SHA-256 with every
result so "which prompt version passed" is never ambiguous
(`coach/eval/run.py:66`, `coach/eval/RESULTS.md:9`). None of that is
optional ceremony — this project's own history has a private-heldout-test
exposure it's still recovering from (`docs/HANDOFF-COACH.md:44`, a process
listing printed private review input into a parent context), which is the
kind of leak these checks are built to make harder to repeat.

Next: [`04-scaling-up.md`](04-scaling-up.md).
