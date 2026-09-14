# Team playbook

Idea → coach → four outputs → approved project spec → one useful slice → test.

## Hand off to Claude Code
Read docs/idea-brief.md, docs/experiment-card.md, and docs/mvp-brief.md.
Draft docs/PROJECT-SPEC.md. For each feature, include an observable acceptance test.
Preserve exclusions and Unknowns. Propose the smallest implementation plan.
Do not build until I approve.

The filenames above are the team's saved copies of the coach outputs.
Do not imply that the coach already created these files; save them first.

## Build one slice
Approve the specific scope. Ask Claude Code to implement it, show the changes,
and run the acceptance test. Inspect the working flow yourself.
Ask a separate reviewer to compare the spec, implementation and actual test outputs.
When behavior fails, make the smallest repair and repeat the check.
The club example can start as a manual experiment; an app is not automatically necessary.

## Pitch with evidence
Show the person/problem, current alternatives, working demo, experiment result,
and what the result changed. Cite the source for each important claim.
Do not present synthetic participants as customers or an unrun experiment as successful.

## Pair practice
Driver supplies the idea and saves outputs. Challenger checks assumptions, asks for an
observable test, and inspects the evidence. Swap roles after one iteration.

This is a teaching workflow derived from the coach's experiment and MVP contract:
../../coach/PROMPT.md:116 and ../../coach/examples/study-session.md:89.
