# Facilitator guide — coach build and hackathon use

The full repository coach is the main example. The deck has 37 slides and six
sections. Use the prepared files alongside live Claude Code demonstrations.

| Section | Slides | Suggested time | Show or do |
|---|---|---|---|
| Start | 1–4 | 6 minutes | Introduce facilitators and the two linked jobs |
| Meet the coach | 5–7 | 8 minutes | Read the actual conversation excerpts; open the four outputs |
| Build it | 8–23 | 38 minutes | Brief, spec, approval, files, challenge, repair; one live case |
| Use it | 24–30 | 18 minutes | Teams start the coach, supply evidence, choose a test, save outputs |
| Your hackathon | 31–35 | 15 minutes | Turn the MVP into a project spec and run pair practice |
| Take it away | 36–37 | 5 minutes | Explain a decision and distribute the kit |

These timings are facilitation guidance, not displayed on the slides. The side
rail links to section starts and distinguishes past/current/future sections.

## Copilot and autopilot

Slide 3 introduces active judgment before the build walkthrough. Ask students
to explain a decision, identify supporting evidence, and name a reason to revise
it. Treat the comparison as a practice anyone can learn. Automation remains
useful when its goals, boundaries, and acceptance criteria are understood.
The attribution is to Chorouk Malmoum’s post in the supplied screenshot; the
slide is an adaptation, not a quotation or research finding.

## Build demonstration

Open the actual coach files in VS Code beside Claude Code. Show a spec requirement,
its prompt rule, the scenario and complete response, and your review decision.
Use walkthrough/CLAUDE-CODE-STEPS.md for the exact teaching prompts.
To demonstrate generating files, start a separate demo folder with a copy of
walkthrough/BUILD-BRIEF.md. Do not overwrite the completed repository coach.
The walkthrough is a reproducible teaching sequence, not a historical build transcript.

Run one case live if access is ready. Otherwise open a recorded response and clearly
identify it as recorded. The actual example on slide 6 is excerpted from turn-01.json
in docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/.
The supplied club story and all of its counts are synthetic; no experiment was run.

## Engineering interlude

Slides 20–23 introduce DRY and convention over configuration, SOLID, ACID,
and Big O. Allow four minutes within Build it. The examples describe potential
student software; they do not claim the coach uses a database or class hierarchy.
Slide 34 explains the decision to teach the practices before adding BMAD or gstack
setup. Present both as useful workflow options, without implying missing features.

## Student activity

Students use the coach to investigate their own idea, save its four outputs, and
choose Proceed/Narrow/Investigate/Pivot. They then use a fresh coding session to
turn the approved MVP into a project spec with observable acceptance tests.
A manual experiment may be the right first implementation; do not force an app.

## Access and fallbacks

Use the organizer-provided API setup for Claude Code. A Claude chat subscription
is separate from API credits; chat is an alternative for students with eligible access.
Confirm the actual student accounts and Windows setup before relying on a live demo.
Never project API keys. The old coach evaluation harness is subscription-specific;
do not use it unchanged as the student API-credit workflow.

Keep the completed prompt, templates, and recorded example available offline.
The final slide's local links work on the presentation machine. Distribute the repo
or exported kit files to students; localhost is not a classroom-wide download URL.

## Facilitation checks

- Praise is not a commitment; Unknown is not zero.
- The six counts are distinct; they need not form a funnel.
- A source URL alone does not establish the source's contents or demand.
- Separate reviewer sessions help organize context, not guarantee correct judgment.
- Ask which specific behavior changed after review and which evidence supports it.

Instructor preparation and runtime evidence belong here and in VALIDATION.md,
not on student-facing rehearsal-status slides.
