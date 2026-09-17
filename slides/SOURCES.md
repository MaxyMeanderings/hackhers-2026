# Source map

The build walkthrough is authored teaching material. It illustrates how to reproduce
the workflow; it does not pretend to be a transcript of the historical build.

- Slides 5–7 and optional slides 31–40: the completed branch’s
  [coach guide](https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/README.md),
  [prompt](https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/PROMPT.md),
  [templates](https://github.com/doctor-ew/hackhers-2026/tree/reference/completed-coach/coach/templates),
  [worked example](https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/examples/study-session.md),
  plus walkthrough/USE-THE-COACH.md and walkthrough/HACKATHON-PLAYBOOK.md.
- Slide 6: exact excerpts from the input and output fields of the
  [recorded first turn](https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/turn-01.json).
  The full response contains additional context; the slide labels the excerpts.
- Slides 7, 33, 35, and 39 summarize the recorded synthetic worked example above.
  No actual interviews or experiment results are claimed.
- Slides 8–23: ../starter/BUILD-BRIEF.md and ../starter/BUILD-STEPS.md, grounded in the
  [original behavior spec](https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/docs/AGENT-SPEC.md)
  and [evaluation cases](https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/eval/evaluation-cases.md).
  Reference artifacts illustrate the target; checkpoints require student-built artifacts.
- Claude Code: https://code.claude.com/docs/en/quickstart and
  https://code.claude.com/docs/en/how-claude-code-works .
- Tool overview: https://github.com/bmad-code-org/BMAD-METHOD ,
  https://github.com/garrytan/gstack , https://github.com/doctor-ew/nightshift-community .
  This is a brief comparison, not a feature-equivalence or benchmark claim.
- Visual sources and bios: ASSETS.md.
- Side navigation: global-top.vue; Slidev useNav API verified against installed
  node_modules/@slidev/client/composables/useNav.ts:24 and :59.
  Global layer convention: https://sli.dev/custom/directory-structure .

The original behavior spec's account setup predates the organizer's sponsored API
arrangement. Current teaching instructions use the organizer's API access; no old
subscription-only shell setup is copied into the student flow.

## Engineering principles and workflow scope

Slides 24–27 use the following primary sources. Scheduling, validation, booking,
and operation-count examples are authored teaching illustrations, not claims
about implemented coach behavior.

- DRY: [The Pragmatic Programmer, tip 15](https://pragprog.com/tips/).
- Convention over configuration: [Rails introduction](https://guides.rubyonrails.org/getting_started.html).
- SOLID: [Robert C. Martin, SOLID relevance](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html).
- ACID: [IBM transaction properties](https://www.ibm.com/docs/en/iis/11.7.0?topic=transactions-transaction-properties).
- Big O: [Carnegie Mellon machine learning primer](https://www.cs.cmu.edu/~mgormley/courses/ml-primer/bigO.html).

Slide 28 summarizes the official BMAD and gstack repositories linked above.
Omitting their setup is a workshop scope decision. The slide does not assert that
either tool lacks engineering principles, review, testing, or evidence features.
Sources accessed September 16, 2026.

## Copilot and autopilot

Slide 3 adapts the copilot/autopilot comparison in a LinkedIn post attributed to
Chorouk Malmoum in the screenshot supplied by the workshop organizer on
September 16, 2026. The screenshot is the source available for this attribution;
a permalink and publication date were not supplied. The original screenshot is
bundled at public/assets/copilot-autopilot-post.png and opens from slide 3. The slide paraphrases the
idea and adds workshop questions. It does not present the post as empirical
research or imply that autonomous execution is inherently undesirable.

## Checkpoints

Slides 11, 14, 17, and 23 are authored build activities: prepare a fresh project,
approve a testable spec, implement a coach, and test that student implementation.
Commands follow [Claude Code quickstart](https://code.claude.com/docs/en/quickstart),
accessed September 16, 2026. Build deliverables follow ../starter/BUILD-BRIEF.md.
Testing and repair follow ../starter/BUILD-STEPS.md. A reference response
or a check against the supplied completed coach is not evidence that a student’s
implementation works.

## Starter and completed reference

The completed coach and retained evidence are preserved on
[reference/completed-coach](https://github.com/doctor-ew/hackhers-2026/tree/reference/completed-coach),
at commit 4e4e8ed2edcec7299fa403cccedeca65ba22487d. Full implementations and historical
runtime records are excluded from main and from the published student bundle.
The slide excerpts remain teaching examples with explicit reference attribution.
The starter ZIP and build handouts are generated from ../starter/.
