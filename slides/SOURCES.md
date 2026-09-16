# Source map

The build walkthrough is authored teaching material. It illustrates how to reproduce
the workflow; it does not pretend to be a transcript of the historical build.

- Slides 4–6, 23–29: ../coach/README.md, ../coach/PROMPT.md,
  ../coach/templates/, and ../coach/examples/study-session.md.
- Slide 5: exact excerpts from the input and output fields of
  ../docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/turn-01.json.
  The full response contains additional context; the slide labels the excerpts.
- Slides 6, 25, 27, 31: recorded synthetic example summaries from
  ../coach/examples/study-session.md. No actual interviews or experiment results claimed.
- Slides 7–18: walkthrough/BUILD-BRIEF.md and walkthrough/CLAUDE-CODE-STEPS.md,
  grounded in ../docs/AGENT-SPEC.md, ../coach/PROMPT.md and ../coach/eval/evaluation-cases.md.
- Slides 23–34: walkthrough/USE-THE-COACH.md and walkthrough/HACKATHON-PLAYBOOK.md.
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

Slides 19–22 use the following primary sources. Scheduling, validation, booking,
and operation-count examples are authored teaching illustrations, not claims
about implemented coach behavior.

- DRY: [The Pragmatic Programmer, tip 15](https://pragprog.com/tips/).
- Convention over configuration: [Rails introduction](https://guides.rubyonrails.org/getting_started.html).
- SOLID: [Robert C. Martin, SOLID relevance](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html).
- ACID: [IBM transaction properties](https://www.ibm.com/docs/en/iis/11.7.0?topic=transactions-transaction-properties).
- Big O: [Carnegie Mellon machine learning primer](https://www.cs.cmu.edu/~mgormley/courses/ml-primer/bigO.html).

Slide 33 summarizes the official BMAD and gstack repositories linked above.
Omitting their setup is a workshop scope decision. The slide does not assert that
either tool lacks engineering principles, review, testing, or evidence features.
Sources accessed September 16, 2026.
