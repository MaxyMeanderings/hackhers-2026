# Build walkthrough in Claude Code

Use a separate demo folder. Copy BUILD-BRIEF.md into it first. Do not overwrite the completed coach.

## 1. Orient
Start `claude` in your project folder. Source: https://code.claude.com/docs/en/quickstart .
Prompt: Read the project files and explain what is here. Identify the coach prompt,
specification, templates, and tests. Do not edit anything yet.
For an empty demo folder, read BUILD-BRIEF.md instead.

## 2. Specify
Read BUILD-BRIEF.md. Draft SPEC.md with numbered, observable requirements,
exclusions, and acceptance cases. Ask about consequential gaps. Do not implement yet.
Review whether every requirement has an observable check before proceeding.

## 3. Approve
Approved: implement only the requirements in SPEC.md. First list the files you will
change and the checks you will run. Leave unrelated files alone.

## 4. Inspect the build
Open the resulting prompt, templates and cases. Point from one spec requirement
to the prompt instruction intended to satisfy it. Inspect the diff.
The completed repository example is `../../coach/PROMPT.md`, `../../coach/templates/`,
and `../../coach/eval/evaluation-cases.md`.

## 5. Run cases
Use fresh coaching conversations for independent cases. Save the exact input and full
response; do not manually improve a response before reviewing it.

## 6. Challenge in a separate session
Review SPEC.md, the coach prompt, and the saved test responses. For each applicable
requirement, quote the exact response text. Mark pass, fail, or unresolved.
Explain unsupported claims. Do not assume the builder's summary is correct.
Separate sessions organize context; inspect the review rather than treating it as proof.

## 7. Repair
Fix only the reported requirement violation. Repeat the failing case and one that
previously passed. Preserve earlier responses so the team can explain the change.

These are authored teaching prompts, not a transcript of a previous run.
File references in these instructions resolve from this walkthrough folder.
