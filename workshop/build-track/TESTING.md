# Shakedown cruise — testing the real coach before the event

Two checks, not one. The scripted run catches prompt/behavior regressions
fast; the manual run catches everything the script can't see, because it
doesn't play a student — it just calls the model and records the transcript.

## Preflight (read-only, run this first)

```sh
unset ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL
unset CLAUDE_CODE_USE_BEDROCK CLAUDE_CODE_USE_VERTEX CLAUDE_CODE_USE_FOUNDRY
claude auth status --json
claude --version
```

Confirmed working on this machine on 2026-09-11: `claude auth status --json`
reports `"loggedIn": true`, `"authMethod": "claude.ai"`,
`"apiProvider": "firstParty"`, `"subscriptionType": "max"`; `claude --version`
is `2.1.268`. If any field differs, fix sign-in before running either check
below — `coach/eval/run.py` will refuse to run without it
(`coach/eval/run.py:60-64`).

## 1. Scripted regression (`coach/eval/run.py cases`)

Confirms the frozen `coach/PROMPT.md` still produces the recorded prompt SHA
and still passes the ten synthetic cases, exactly how the shipped coach was
originally verified (`coach/eval/RESULTS.md:3-9`).

```sh
python3 coach/eval/run.py cases --output docs/coach-completion-20260909/live/shakedown-$(date +%Y%m%d)
```

Read this before running it:

- **Cost and time.** Ten fresh Opus sessions, one `claude -p` call each, up
  to 8 turns and a 300-second timeout per case (`coach/eval/run.py:78,97`).
  Budget real wall-clock time and real subscription usage — run this early,
  not right before the event when you want quota headroom for live student
  demos.
- **It never self-grades.** Every record ships with
  `"judgment": "PENDING_INDEPENDENT_REVIEW"` (`coach/eval/run.py:94`) — a
  nonzero exit code and populated `output` mean the call transported
  successfully, not that the response passed. Read each case's `output`
  against `coach/eval/evaluation-cases.md`'s "Expected behavior" column
  yourself, the same way independent reviews like
  `docs/coach-completion-20260909/CASES-REVIEW-OPUS-COMPLETE-EXPERIMENT.md`
  did.
- **Append-only.** It refuses to overwrite an existing output file
  (`coach/eval/run.py:71-72`) — pass a fresh `--output` directory per run,
  as above.
- Add `--ids 04 08` to rerun only specific cases (useful after touching the
  prompt, without re-spending quota on the other eight).

## 2. Manual live walkthrough

Catches interaction-level issues the harness's isolated per-case calls can't
— pacing across a real multi-turn conversation, whether question batches
feel like 1–5 focused questions in practice (`docs/AGENT-SPEC.md:10`), and
whether the terminal path actually matches the chat path a student would use.

```sh
claude --model opus --safe-mode --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
  --tools "" --system-prompt-file coach/PROMPT.md
```

(Adapted from `coach/CLAUDE-CODE-ADAPTER.md:24`, with `${COACH_EVAL_MODEL:-opus}` resolved to `opus`.) Then:

1. Open with an idea and what prompted it, in your own words — not a case
   from the eval list, so you're testing the live path, not re-confirming
   the scripted one.
2. Work all the way through to a proceed/narrow/investigate/pivot decision
   and all four deliverables (idea brief, count ledger, experiment card, MVP
   brief) — the shipped coach's own conversation proof stopped short of this
   once before (`docs/HANDOFF-COACH.md:33`, "student approval and all four
   final deliverables were NOT executed"), so it's worth confirming this
   still completes.
3. Note anything that reads as bundled/duplicated questions or unsupported
   named-product claims — both are flagged as open wording caveats in the
   last review, not fully closed (`coach/eval/RESULTS.md:77-80`).

If you also want the Claude-chat surface tested (not just Claude Code),
repeat step 1–3 at claude.ai with the same pasted `coach/PROMPT.md` — the
project has never claimed chat/terminal parity is verified
(`coach/README.md:31`, `coach/eval/RESULTS.md:83`), so this is real
remaining risk if the event uses chat.

## Before the event

- Run the scripted regression once, days ahead, with quota to spare for a
  rerun if it fails.
- Run one manual walkthrough on the actual device/account type students
  will use (chat vs. terminal, per `coach/CLAUDE-CODE-ADAPTER.md`).
- Keep a saved transcript from a successful walkthrough as the "clearly
  labeled recorded demo" `WORKSHOP-DRAFT.md:72` already calls for in case of
  a connectivity failure during the workshop itself.
