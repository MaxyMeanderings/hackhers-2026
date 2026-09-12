# Stage 5 (instructor) — build the same toy coach three ways

This is the instructor comparison in the 60–72 min slot of
[`../WORKSHOP-DRAFT.md`](../WORKSHOP-DRAFT.md), not a student exercise. Same
toy build, same target, three different amounts of process around it:
**unstructured Claude**, **NightShift**, and **BMAD**. The point is to make
the value of spec → verify → build → review → drift visible by first showing
what happens without it.

None of these three runs have been executed by this session — this is a
command-by-command runbook to rehearse before you show it live, not a
recording of an actual pass. Toy-scale on purpose: this targets a prompt
around Stage 4's 15-line `prompt-v2.txt` size, not the full 238-line
`coach/PROMPT.md`.

## The shared build target

Give every path the same one-line brief, so the comparison is apples to
apples:

> Build a hackathon idea coach: a system prompt that refuses top-down market
> claims ("everyone needs this") in favor of a reachable-audience count,
> requires a source URL for any competitor claim, and negotiates the student
> down to at most 3 MVP features tied to one measurable experiment.

That's a compressed version of `docs/AGENT-SPEC.md`'s actual Purpose and
Research rules (`docs/AGENT-SPEC.md:15-17`, `:75-79`) — small enough to build
three times in a class period, specific enough that "did it actually do the
job" has a real answer.

## Path 1 — unstructured Claude (the contrast case)

One prompt, no process:

```
Build me a hackathon idea coach: <paste the brief above>.
```

Take whatever comes back. Do not ask for tests, sources, or a review. This
is deliberately the "before" case — the class should watch for what's
*missing*, not what's wrong: no record of why any design choice was made, no
check that the prompt's claims about its own behavior are true, no test that
would catch a regression on the next edit, no way to tell later whether a
change drifted from the original intent. Every one of those gaps is a named
stage in Path 2.

## Path 2 — NightShift

The actual pipeline this repo's own coach was built with (see the
`batch(state)`/`lock(...)`/`checkpoint` commits in `git log --oneline` on
`main` — that history is this exact pipeline's real output, not a
demonstration). Five stages, each gating the next:

```sh
/nightshift-product <REF>       # spec — the "build prompt, like a PRD"
/nightshift-adversarial <key>   # works cited — verifies every technical claim
/nightshift-implement <key>     # TDD — RED phase, then the GREEN fix
/nightshift-review <key>        # code/drift review, part 1 — six lenses
/nightshift-drift <key>         # code/drift review, part 2 — spec vs. git diff
```

What each stage actually is, from its own command definition:

- **`/nightshift-product <REF>`** — "Spec Production Harness — fetches a
  ticket from any source (gh/jira/monday/notion/bd)... asks three grounding
  questions, runs nightshift-code-fact-extractor on identifiers, then
  delegates to /nightshift-spec with Sources + Model Router enforcement"
  (`~/.claude/commands/nightshift-product.md:3`). `<REF>` needs a real ticket
  source or an existing bead — for a from-scratch classroom toy with no
  ticket tracker, create one bead first (`docs/HANDOFF-COACH.md`'s
  `beads-mirror.sh` and the `bd:bd-...` form in your global
  `~/.claude/CLAUDE.md`'s drew-* pipeline section describe the mechanism —
  this is user-level config, not part of this repo); this is the one
  prerequisite step this runbook doesn't fully resolve for you.
- **`/nightshift-adversarial <key>`** — "loads an approved spec, extracts
  every technical claim, runs nightshift-code-fact-extractor on each one,
  and surfaces conflicts to the engineer for CONFIRM/OVERRIDE/BLOCK
  decisions. BLOCKED if unresolved claims remain"
  (`~/.claude/commands/nightshift-adversarial.md:3`). This is literally the
  "works cited" step.
- **`/nightshift-implement <key>`** — "TDD-aware... Seals the spec
  (spec-lock), runs the RED phase under an agent firewall, locks the failing
  tests under the nightshift-bot identity (red-lock)... then writes the
  GREEN fix" (`~/.claude/commands/nightshift-implement.md:3`).
- **`/nightshift-review <key>`** — "Post-implementation code review across
  six lenses: DRY, SOLID, ACID, CoC, Big O, and LLM trust boundaries"
  (`~/.claude/commands/nightshift-review.md:3`).
- **`/nightshift-drift <key>`** — "Reads SPEC.md, extracts the Files to
  Change table + acceptance criteria + claims, cross-references against the
  actual git diff... Output saved to docs/<task-key>/DRIFT.md"
  (`~/.claude/commands/nightshift-drift.md:3`).

Or run all five (plus preflight/deploy, which you can stop before) as one
orchestrated pass: `/nightshift-eng <REF-or-task-key>`
(`~/.claude/commands/nightshift-eng.md:3`). Your global `~/.claude/CLAUDE.md`
drew-* section is explicit that this pipeline is beads-backed and never
invokes a gstack skill — don't cross the streams live.

## Path 3 — BMAD

Available in this environment (`~/.claude/skills/bmad-*`, confirmed
2026-09-12). No 1:1 stage-for-stage match to NightShift's names — map by
what each skill's own description says it does, and verify live before
presenting it as equivalent:

```
bmad-prd              # spec — "Create, update, or validate a PRD"
bmad-build             # implementation — "Turns implementation work into
                        #   working code, reviewed and verified"
bmad-code-review       # code review — "several independent reviewers in
                        #   parallel, then triage and present the findings"
bmad-retrospective     # drift-equivalent — "Review a completed epic against
                        #   the evidence it left behind — spec, stories,
                        #   diffs, commits, sprint status"
```

Two honest gaps, not papered over:

- **No exact "works cited" stage.** The closest analogs are `bmad-review`
  ("adversarial critique, edge cases, verification gaps, structure, prose")
  and `bmad-deep-recon` ("market, domain, technical, competitive..."
  research), but neither is described as verifying a spec's own technical
  claims against the codebase before implementation the way
  `nightshift-adversarial` is. Pick one and see what it actually surfaces
  when you run it, rather than asserting it's the same check.
- **No stated TDD discipline.** `bmad-build`'s description says "reviewed
  and verified," not RED-phase-then-GREEN-fix. Don't claim TDD parity with
  NightShift on this path unless you watch it actually write a failing test
  first.

`bmad` (no argument) will answer "what do I start with" for whichever of
these you haven't used before, if you want a live fallback instead of
committing to this exact sequence.

## What to actually show the class

Run Path 1 live — it's fast and the gap is the lesson. For Paths 2 and 3,
you likely don't have time to run every stage live; walk the actual artifact
trail from a *prior* run instead: NightShift's is this repo's own
`docs/coach-completion-20260909/` and `.nightshift/coach-completion-20260909.md`
(real SPEC.md, real adversarial citations log, real review history,
including the documented 8/10 → 10/10 repair — see
[`04-scaling-up.md`](04-scaling-up.md)). Rehearse whichever BMAD stage you
pick beforehand so you have a real artifact to show there too, not a cold
first run in front of the class.
