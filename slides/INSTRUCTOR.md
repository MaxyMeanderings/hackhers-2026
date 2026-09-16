# Facilitator guide — build your own coach

The core workshop teaches students to build and test a conversational coach from
a supplied build brief and their approved specification. The completed repository
coach illustrates the target behavior. Student deliverables are the spec, coach
prompt, four output templates, test cases, and actual test evidence.

## Schedule

The 90-minute workshop uses slides 1–30. Slides 31–40 are optional follow-on
material about using a finished coach to investigate a hackathon idea.

| Section | Slides | Time | Activity |
|---|---|---|---|
| Start | 1–4 | 6 minutes | Copilot mindset and student build deliverables |
| Reference coach | 5–7 | 6 minutes | Show the target behavior and outputs |
| Build your coach | 8–23 | 60 minutes | Brief, spec, approval, implementation, testing, and repair |
| Engineering | 24–28 | 10 minutes | Principles and workflow options |
| Show your work | 29–30 | 8 minutes | Demonstrate the student-built coach and share artifacts |

Checkpoint time is included in Build your coach. Reserve its remaining 23 minutes
for short explanations and demonstrations. Move optional material into a later
session instead of reducing student implementation time.

## Student checkpoints

| Checkpoint | Slide | Time | Completion evidence |
|---|---|---|---|
| Prepare your build folder | 11 | 5 minutes | Own folder, BUILD-BRIEF.md, working access, scope summary |
| Review your spec | 14 | 8 minutes | Saved SPEC.md, observable acceptance cases, explicit team approval |
| Implement your coach | 17 | 12 minutes | Own prompt, four templates, test cases, requirement trace |
| Test your coach | 23 | 12 minutes | Actual input and response, reasoned verdict, repair/retest where needed |

Ask pairs to signal ready or needs help at each stop. Installation alone is not
working model access. Files on disk are not proof of correct behavior. A test of
the supplied reference coach does not demonstrate the student’s implementation.
Confirm the actual prompt path loaded for the final checkpoint.

## Preparation and facilitation

Students start in a fresh folder with walkthrough/BUILD-BRIEF.md saved as
BUILD-BRIEF.md. Use walkthrough/CLAUDE-CODE-STEPS.md for the build prompts.
Each pair reviews and approves its own SPEC.md before implementation. Let Claude
propose file paths; students should inspect the files actually created.

Show one reference requirement, its prompt instruction, and a test briefly, then
return to the student projects. Slide 6 contains recorded synthetic excerpts from
the retained conversation. Label reference demonstrations and recorded responses;
they are examples, not passing evidence for student builds.

The implementation is a conversational coach prompt and supporting files. An app,
a database, and a separate hackathon product are not required workshop deliverables.
Explain the engineering slides as design lenses whose applicability depends on
what is being built. On slide 28, present BMAD and gstack as workflow options.

Slide 3 adapts Chorouk Malmoum’s post from the supplied screenshot. The thumbnail
opens the original image. Present its comparison as a practice students can learn,
not a research finding or a claim that autonomous execution is inherently wrong.

## Access and fallbacks

Use the organizer’s API access setup. Never project keys. If a pair is blocked,
pair them on a working laptop. They may draft the spec manually while resolving
access, but label unexecuted checks Not run and incomplete builds incomplete.
Do not replace a student implementation with the reference coach and call it done.

Preserve exact inputs and full responses. A failed case is useful evidence: repair
the student prompt, repeat that case, and check one previously passing case. If
all tested cases pass immediately, try a harder case or another requirement.
Do not invent a failure, repair, or successful evaluation.

## Completion

At slide 29, each pair demonstrates its own coach and explains a requirement,
where it is implemented, the observed test result, and remaining limitations.
At slide 30, share the build kit and published presentation URL. Optional slides
31–40 show how the finished coach could later inform a separate project.
