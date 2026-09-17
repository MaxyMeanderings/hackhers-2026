# Facilitator guide — build your own coach

The core workshop teaches students to build and test a conversational coach from
a supplied build brief and their approved specification. The completed repository
coach illustrates the target behavior. Student deliverables are the spec, coach
prompt, four output templates, test cases, and actual test evidence.

## Schedule

The 90-minute workshop uses slides 1–35 and closing slides 46–47. Slides 36–45 are optional follow-on
material about using a finished coach to investigate a hackathon idea.

| Section | Slides | Time | Activity |
|---|---|---|---|
| Start | 1–9 | 10 minutes | Workshop links, sponsored API credit sign-in, copilot mindset, and student build deliverables |
| Reference coach | 10–12 | 6 minutes | Show the target behavior and outputs |
| Build your coach | 13–28 | 60 minutes | Brief, spec, approval, implementation, testing, and repair |
| Engineering | 29–33 | 10 minutes | Principles and workflow options |
| Show your work | 34–35, 46–47 | 8 minutes | Demonstrate the student-built coach and share artifacts |

Checkpoint time is included in Build your coach. Reserve its remaining 23 minutes
for short explanations and demonstrations. Move optional material into a later
session instead of reducing student implementation time.

## Student checkpoints

| Checkpoint | Slide | Time | Completion evidence |
|---|---|---|---|
| Prepare your build folder | 16 | 5 minutes | Own folder, BUILD-BRIEF.md, working access, scope summary |
| Review your spec | 19 | 8 minutes | Saved SPEC.md, observable acceptance cases, explicit team approval |
| Implement your coach | 22 | 12 minutes | Own prompt, four templates, test cases, requirement trace |
| Test your coach | 28 | 12 minutes | Actual input and response, reasoned verdict, repair/retest where needed |

Ask pairs to signal ready or needs help at each stop. Installation alone is not
working model access. Files on disk are not proof of correct behavior. A test of
the supplied reference coach does not demonstrate the student’s implementation.
Confirm the actual prompt path loaded for the final checkpoint.

## Preparation and facilitation

Students download and extract the student starter ZIP into their own workspace.
Its contents come from ../starter/. Use ../starter/BUILD-STEPS.md for the build
prompts and ../starter/BUILD-BRIEF.md for the requirements.
Each pair reviews and approves its own SPEC.md before implementation. Let Claude
propose file paths; students should inspect the files actually created.

Show one reference requirement, its prompt instruction, and a test briefly, then
return to the student projects. Slide 11 contains recorded synthetic excerpts from
the retained conversation. Label reference demonstrations and recorded responses;
they are examples, not passing evidence for student builds.

The implementation is a conversational coach prompt and supporting files. An app,
a database, and a separate hackathon product are not required workshop deliverables.
Explain the engineering slides as design lenses whose applicability depends on
what is being built. On slide 33, present BMAD and gstack as workflow options.

Slide 8 adapts Chorouk Malmoum’s post from the supplied screenshot. The thumbnail
opens the original image. Present its comparison as a practice students can learn,
not a research finding or a claim that autonomous execution is inherently wrong.

## Access and fallbacks

Slides 4–7 walk students through claiming the sponsored API credits and choosing
the Anthropic Console login inside Claude Code. Have every pair scan the offer on
slide 4 right after the workshop links on slide 3. The QR code is this event’s
offer; the form screenshot on slide 5 is from an earlier offer until replaced.
Credits are issued within a couple of minutes of a valid claim. Students must
submit the Organization ID from the Claude Console, not a Claude.ai user ID,
which the system rejects. Each person can claim once, and the link’s expiration
date is shown on the offer page.

Use the organizer’s API access setup. Never project keys. If a pair is blocked,
pair them on a working laptop. They may draft the spec manually while resolving
access, but label unexecuted checks Not run and incomplete builds incomplete.
Do not replace a student implementation with the reference coach and call it done.

Preserve exact inputs and full responses. A failed case is useful evidence: repair
the student prompt, repeat that case, and check one previously passing case. If
all tested cases pass immediately, try a harder case or another requirement.
Do not invent a failure, repair, or successful evaluation.

## Completion

At slide 34, each pair demonstrates its own coach and explains a requirement,
where it is implemented, the observed test result, and remaining limitations.
At slides 35 and 46–47, share the build kit and published presentation URL. Optional slides
36–45 show how the finished coach could later inform a separate project.

## Completed backup

The [reference/completed-coach branch](https://github.com/doctor-ew/hackhers-2026/tree/reference/completed-coach)
is the already-baked backup. Download it before the event into a separate folder
for offline demos and recovery. Read its coach/README.md and coach/eval/RESULTS.md
for setup and tested limits. Do not merge the backup into main or copy it into a
student workspace. The reference branch does not publish the live slides.

Use the starter ZIP for students rather than the full repository archive. Main
contains brief teaching excerpts in the slides but no completed coach. The ZIP
contains only four starter files and no Git history or reference implementation.

## Connection and access slides

Slide 2 includes both speakers’ photos, introductions, and LinkedIn QR codes.
Slide 3 provides QR codes and clickable links to the live deck and repository.
The only repeats are at the end: speaker connections on slide 46 and resources
on slide 47. Skip optional practice (slides 36–45) using the Stay connected
navigation button when closing the core workshop. Allow scanning time within
the opening and closing sections.
