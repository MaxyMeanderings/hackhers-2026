# HackHers 2026

Build your own go-to-market coach with Claude Code, guided by Drew and Tyler Sztuka.
Start from a behavior brief, approve a testable spec, implement your coach, and
show evidence that its behavior meets your requirements.

## Students: start here

1. [Download the student starter ZIP](https://doctor-ew.github.io/hackhers-2026/hackhers-starter.zip).
2. Extract it into your own workspace and open the extracted folder in your editor.
3. Follow its README.md and BUILD-STEPS.md using the organizer’s Claude Code access setup.
4. Follow along with the [live workshop slides](https://doctor-ew.github.io/hackhers-2026/).

The ZIP contains only four starter files: a README, build brief, build instructions,
and ignore rules. You create the spec, coach prompt, four output templates, and
tests. It contains no completed coach or recorded answers.

If you prefer Git, clone this repository on main and **copy [starter/](starter/)
into a separate project folder** before starting Claude Code. The rest of main
contains presentation and facilitator material, including short teaching excerpts.
No slide authoring dependencies are required to build your coach.

## Checkpoints

| Stage | Show your partner |
|---|---|
| Setup | Your project folder, build brief, and working Claude session |
| Specify | Saved spec, observable acceptance cases, and your approval |
| Implement | Your prompt, four templates, test cases, and one requirement trace |
| Test and repair | Exact input, full answer, verdict, and any repair/retest |

## Facilitators: the already-baked backup

The [reference/completed-coach branch](https://github.com/doctor-ew/hackhers-2026/tree/reference/completed-coach)
preserves the completed implementation, templates, evaluator, recorded examples,
and development evidence. Use it for demonstrations, recovery, or comparison
after students make their own attempt.

- [Completed coach and usage guide](https://github.com/doctor-ew/hackhers-2026/tree/reference/completed-coach/coach)
- [Recorded evaluation results and limits](https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/eval/RESULTS.md)
- [Download the completed reference](https://github.com/doctor-ew/hackhers-2026/archive/refs/heads/reference/completed-coach.zip)

Keep the backup in a separate folder. Tests against it are not evidence that a
student’s implementation passes. The preserved snapshot is commit
`4e4e8ed2edcec7299fa403cccedeca65ba22487d`. Its recorded results retain their stated
runtime and evaluation limits; this separation does not rerun the model evaluation.

## Presentation maintenance

- [Facilitator guide](slides/INSTRUCTOR.md)
- [Build and publishing instructions](slides/README.md)
- [Slide sources](slides/SOURCES.md)

Changes to the slides, starter, or starter packaging script are built in pull
requests. Merging them into main automatically updates the presentation and
starter download at the existing website. The reference branch is a preserved
backup and does not publish over the student site.
