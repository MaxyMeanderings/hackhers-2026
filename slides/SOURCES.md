# Source map

The build walkthrough is authored teaching material. It illustrates how to reproduce
the workflow; it does not pretend to be a transcript of the historical build.

- Slides 10–12 and optional slides 38–47: the completed branch’s
  [coach guide](https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/README.md),
  [prompt](https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/PROMPT.md),
  [templates](https://github.com/doctor-ew/hackhers-2026/tree/reference/completed-coach/coach/templates),
  [worked example](https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/examples/study-session.md),
  plus walkthrough/USE-THE-COACH.md and walkthrough/HACKATHON-PLAYBOOK.md.
- Slide 11: exact excerpts from the input and output fields of the
  [recorded first turn](https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/turn-01.json).
  The full response contains additional context; the slide labels the excerpts.
- Slides 12, 40, 42, and 46 summarize the recorded synthetic worked example above.
  No actual interviews or experiment results are claimed.
- Slides 13–34: ../starter/BUILD-BRIEF.md and ../starter/BUILD-STEPS.md, grounded in the
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

## API credits onboarding

Slides 4–7 are the organizer’s sponsored-access walkthrough, adapted on
September 17, 2026 from the organizer’s existing slides (API Credits.pptx). The
QR code on slide 4 is the event offer code supplied by the organizer on
September 17, 2026; it decodes to
https://platform.claude.com/offers/2239eaf0-dbc5-49ed-b6b7-1f1fe14ea78e , an
Anthropic API credits offer page, and the slide links to the same URL. Slides 5–7
show the organizer’s own screenshots of an earlier Anthropic credits application
form, the Claude Console dashboard (platform.claude.com/dashboard), and the
Claude Code `/login` prompt. Balances, names, event titles, and dates in those
screenshots belong to the organizer’s account and earlier events; they are not
claims about student accounts or this event’s deadline. Claim rules stated on
slides 4–6 (API only, not Claude.ai; Console Organization ID required and a
Claude.ai user ID rejected; one claim per person; link expiration shown on the
offer page; credits issued within minutes) were supplied by the organizer on
September 17, 2026. Login option wording follows the Claude Code prompt in the
screenshot.

## Engineering principles and workflow scope

Slides 20–23 use the following primary sources. Scheduling, validation, booking,
and operation-count examples are authored teaching illustrations, not claims
about implemented coach behavior.

- DRY: [The Pragmatic Programmer, tip 15](https://pragprog.com/tips/).
- Convention over configuration: [Rails introduction](https://guides.rubyonrails.org/getting_started.html).
- SOLID: [Robert C. Martin, SOLID relevance](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html).
- ACID: [IBM transaction properties](https://www.ibm.com/docs/en/iis/11.7.0?topic=transactions-transaction-properties).
- Big O: [Carnegie Mellon machine learning primer](https://www.cs.cmu.edu/~mgormley/courses/ml-primer/bigO.html).

Slide 35 summarizes the official BMAD, gstack, and Nightshift repositories linked above.
Omitting their setup is a workshop scope decision. The slide does not assert that
any of these tools lacks engineering principles, review, testing, or evidence features.
Sources accessed September 16, 2026.

## Copilot and autopilot

Slide 8 adapts the copilot/autopilot comparison in a LinkedIn post attributed to
Chorouk Malmoum in the screenshot supplied by the workshop organizer on
September 16, 2026. The screenshot is the source available for this attribution;
a permalink and publication date were not supplied. The original screenshot is
bundled at public/assets/copilot-autopilot-post.png and opens from slide 8. The slide paraphrases the
idea and adds workshop questions. It does not present the post as empirical
research or imply that autonomous execution is inherently undesirable.

## Checkpoints

Slides 18, 25, 28, and 34 are authored build activities: prepare a fresh project,
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

## Speaker connections and QR destinations

- Tyler’s LinkedIn destination is linked from [SZD Labs](https://szdlabs.io/):
  https://www.linkedin.com/in/tyler-sztuka-283937123/ .
- Drew’s LinkedIn destination is linked from [his speaker profile](https://sessionize.com/drew-schillinger/):
  https://www.linkedin.com/in/andrew-schillinger/ .
- Resource codes use the published deck and repository URLs shown on the slides.
- QR images are local PNG assets with black modules, white backgrounds, and
  four-module quiet zones; no third-party QR service is called at presentation time.

Nightshift’s staged workflow and evidence description was checked against its
[public README](https://github.com/doctor-ew/nightshift-community) on September 17, 2026.
