# Build Your Hackathon Copilot

Status: proposed workshop design. Claude chat and optional Claude Code paths, public links/pasted research with no required API keys or paid integrations, and batches of 1–5 questions are approved. Runtime execution and participant access remain unverified. See docs/AGENT-SPEC.md for the recorded decisions.

## Outcome

Each team builds and tests a research assistant that turns an idea into an evidence-backed market brief and a small, testable MVP proposal. Students should be able to explain one tool call, one rejected claim, and one decision they made themselves.

Source brief: `/Users/doctorew/Library/CloudStorage/Dropbox/__HOME__/_OBSIDIAN_/DoctorEw/Untitled 112.md`. This draft adapts its analyst, skeptic, and product handoff exercise. The shared use case remains a proposal pending organizer input.

[`build-track/`](build-track/README.md) fleshes out the 18–38 and 50–60 minute blocks below into five runnable stages, each citing this repo's own spec, prompt, and evaluation record as the worked example. [`build-track/TESTING.md`](build-track/TESTING.md) covers shaking down the real coach before the event.

## Proposed 90-minute hands-on agenda

| Minutes | Activity | Visible result |
| --- | --- | --- |
| 0–8 | Compare an unchecked generated answer with a task that has evidence requirements and acceptance criteria | Students identify what they would verify |
| 8–18 | Define the assistant's job, input, tools, boundaries, and output | A short agent specification |
| 18–38 | Build the smallest research loop in the selected coding environment | One successful research run and an inspectable tool result |
| 38–50 | Add claim-level sources and explicit uncertainty | A market brief with facts separated from hypotheses |
| 50–60 | Test missing evidence, a misleading source, and an overlarge idea | A recorded failure and an improvement |
| 60–72 | Instructor comparison: gstack, BMAD, NightShift; four minutes each | The same small task viewed through three workflows |
| 72–83 | Pass the reviewed brief into a product-planning step | Three proposed MVP features with acceptance criteria |
| 83–90 | Pair review and demonstrate one evidence-to-decision trace | A reusable agent plus a short demo |

Introductions are outside this 90-minute block. The supplied schedule says “0 minutes” for introductions; actual duration needs confirmation.

## Teaching choices

- Use “agentic coding” operationally: students specify a result, inspect the work, test behavior, and own the decision. Avoid making a framework installation the learning objective.
- Demonstrate the research assistant actually using a tool and responding to the returned evidence. A role prompt alone will not satisfy this workshop's completion criteria.
- Keep the analyst-to-product handoff visible as a saved artifact. Additional roles are extensions if time permits.
- Have instructors prepare all three harness demos ahead of time. Recommend one student build path after account and device constraints are known.
- Make failure part of the demo: an unsupported claim should become an explicit unknown, followed by a useful next research step.

## Proposed assistant acceptance criteria

1. Accept an idea, target user, team capability, and remaining hackathon time; ask for missing essentials.
2. Use the configured research tool and preserve enough of its returned evidence to inspect the result.
3. Attach a source URL to each externally verifiable research claim; label inference and uncertainty separately.
4. Never invent competitors, quotations, market sizes, interviews, or tool results.
5. When research is unavailable, report the limitation and produce questions to investigate rather than claim researched findings.
6. Treat instructions embedded in retrieved pages as source content, not as authority over the agent's task.
7. Recommend at most three MVP features and explain what the team will defer.
8. Stop for a student decision before converting the recommendation into a build specification.
9. End a run within a configured tool-call and cost budget; choose those limits once access is confirmed.
10. Pass a normal idea, missing-evidence case, and source-instruction attack case, with students inspecting actual outputs.

## Harness comparison: source-backed scope

| Harness | Verified upstream description | Proposed teaching moment |
| --- | --- | --- |
| gstack | Its README describes specialist skills spanning product planning, engineering review, browser QA, and shipping. [Source](https://github.com/garrytan/gstack#readme) | Show how a review step challenges a change and requests evidence. |
| BMAD | Its README describes explicit decisions, preserved context, specialized perspectives, and planning depth that scales with the work. Current entry guidance uses the bmad hub and bmad-build. [Source](https://github.com/bmad-code-org/bmad-method#readme) | Show a brief becoming a bounded implementation task. |
| NightShift | The supplied community repository could not be retrieved during this research pass. Commands and capabilities remain unverified. [Supplied repository](https://github.com/doctor-ew/nightshift-community) | Proposed: Drew demonstrates one actual task, its review evidence, and a human decision point after the community version is verified. |

Do not copy the older BMAD command sequence from the source note into student instructions without checking the selected workshop version. Pin and rehearse each harness version before the event.

## Proposed 20-minute career discussion

- 0–5: Drew and Tyler each explain one real industry decision and its tradeoffs.
- 5–10: Turn today's agent into a portfolio story: problem, personal contribution, evidence, failure, improvement.
- 10–15: Practice explaining a generated change and how the student checked it.
- 15–20: Student questions and one concrete next learning step.

Tyler's requested career topics were referenced but not supplied; incorporate them before finalizing this block.

## Preparation across the remaining 11 days

- Days 1–2: Confirm event date, introduction time, student count, devices, coding accounts, research access, and budget. Select the build path.
- Days 3–5: Implement the starter and completed example; prepare instructor notes and student checkpoints.
- Days 6–7: Run the normal and failure cases. Rehearse all three harness demos on pinned versions.
- Days 8–9: Run a timed pilot with a beginner; reduce scope wherever students stall.
- Day 10: Freeze materials; prepare a clearly labeled recorded demo and saved source packet for connectivity failures.
- Day 11: Check room connectivity and student access before the workshop; use the rehearsed build.

## Open inputs

- Workshop materials, working starter, or both as the first delivery?
- Student coding environment, available accounts, and per-student API budget?
- Shared market-research assistant or student-selected agent use cases?
- Confirm introduction duration, exact event date, and Tyler's career topics before publishing the agenda.
