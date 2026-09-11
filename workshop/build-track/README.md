# Build track — how to build a coach like this one

This directory is two things at once: a student-facing build-along (turn a
five-line toy prompt into a workshop-ready coach in five short stages, each
one a real, reproducible failure and fix) and the presentation's spine (each
stage cites the shipped coach's actual spec, prompt, and evaluation record —
including its two documented failures — so the talk is grounded in this
repo, not a generic "how to prompt" deck).

Nothing here is the real coach. Building a second, smaller one alongside it,
on purpose, is what makes the failures visible without students needing to
break `coach/PROMPT.md` itself.

## Stages

0. [Define the job](00-job-spec.md) — five questions, before any prompt text.
1. [Smallest possible prompt](01-prompt-v1.md) — write it, run it, predict
   how it fails.
2. [Add the guardrail](02-add-guardrail.md) — turn the observed failure into
   a prompt rule.
3. [Test a case list](03-harness.md) — stop eyeballing one run; test the ten
   cases this project actually tests.
4. [Scale to the real thing](04-scaling-up.md) — name the concrete gap
   between the toy and `coach/PROMPT.md`, and what closing that gap actually
   cost on this project.

Each stage is one commit on this branch (`workshop/build-the-coach`) — check
out any stage's commit and `git diff` the one before it to show that step's
change live: `git log --oneline` on this branch lists them in order.

## Also here

- [`TESTING.md`](TESTING.md) — how to shake down the *real* coach
  (`coach/PROMPT.md`) before the event: scripted regression + manual
  walkthrough, with exact commands.

## How this maps to the 90-minute agenda

The Stage 0–2 loop is the "18–38 min: build the smallest research loop"
block in [`../WORKSHOP-DRAFT.md`](../WORKSHOP-DRAFT.md); Stage 3 is the
"50–60 min: test missing evidence, a misleading source, an overlarge idea"
block. Stage 4 is not a live student exercise — it's instructor material for
the 60–72 min harness-comparison slot and the 83–90 min close, where showing
`coach/eval/RESULTS.md`'s real pass numbers lands better after students have
just felt their own toy prompt fail the same way.
