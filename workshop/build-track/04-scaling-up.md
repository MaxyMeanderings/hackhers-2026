# Stage 4 — from a 15-line toy to a workshop-ready coach

`workshop/build-track/prompt-v2.txt` is 15 lines. The shipped coach,
[`coach/PROMPT.md`](../../coach/PROMPT.md), is 238 lines. Both are "the same
kind of thing" — a system prompt with job, tools, rules, and output — but the
gap between them is the actual content of the rest of the workshop hour, and
it's worth naming explicitly rather than hand-waving as "and then polish it."

## What v2 is still missing, concretely

Compare against [`docs/AGENT-SPEC.md`](../../docs/AGENT-SPEC.md) and it's
three things, not vague "more detail":

1. **A full inquiry sequence, not one rule.** AGENT-SPEC.md's six stages —
   person/problem, reachable-people count, alternatives, reasons to switch,
   a hackathon-sized experiment, human decision (`docs/AGENT-SPEC.md:23-62`)
   — each has its own failure modes. v2 only hardens the "alternatives"
   stage, because that's the one Stage 1's test happened to hit.
2. **Named output artifacts.** "Produce a brief" is not testable; "produce
   an idea brief with these five fields" is. The shipped coach has four
   blank templates students fill in (`coach/templates/`), referenced by name
   in the prompt itself (`docs/AGENT-SPEC.md:87-90`).
3. **A case list that covers all six stages**, not one. `coach/eval/
   evaluation-cases.md` has ten cases; Stage 3 of this build track only ran
   one of them by hand.

None of that is a rewrite — it's the same v2 structure, repeated once per
stage of the job, with one case per stage to catch it. That loop (define →
draft → break it → fix it → test the fixed list) is the whole workshop in
miniature, and it's the same loop this coach itself went through.

## What that loop actually cost, for real, on this coach

This is the presentation's other half — not "here's a clean five-step
process," but "here's what verifying it honestly required":

- The first real evaluation attempt: **8 of 10 cases passed after three
  permitted behavioral repairs** — Case 04 on unsupported citations, Case 08
  on a dropped experiment link (`coach/eval/RESULTS.md:99-117`).
- The version that shipped: **10 of 10 cases PASS, plus a full five-turn
  conversation PASS** (`coach/eval/RESULTS.md:3`), reached only after that
  documented repair.
- Recorded cost of getting there: **36 development calls, 8 final calls, 5
  repairs, 1 infrastructure failure** — every one of them preserved, not
  discarded (`.nightshift/coach-completion-20260909.md:6-7`).

That's a real talking point for the career-discussion block in
[`WORKSHOP-DRAFT.md`](../WORKSHOP-DRAFT.md): the AI wrote a prompt in
minutes; turning it into something you'd actually hand a student took a
recorded, repeated, and occasionally failed verification loop. The skill
being taught is not "write a good prompt" — it's "know your prompt failed,
specifically, before someone else finds out."

## Bridge to the real thing

For the workshop itself, don't hand students `coach/PROMPT.md` at minute 8 —
that skips the whole loop. Hand them the Stage 0 job-spec questions and
`prompt-v1.txt`'s failure, let them build their own v2 against one or two
cases they write themselves, and only show the real 238-line prompt and its
`coach/eval/RESULTS.md` at the end, as "here's the same loop, carried all
the way through." See [`README.md`](README.md) for how this maps onto the
90-minute agenda, and [`TESTING.md`](TESTING.md) for how to shake down the
real coach before the event.
