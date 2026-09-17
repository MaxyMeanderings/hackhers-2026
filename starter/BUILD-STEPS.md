# Build walkthrough in Claude Code

Build your own coach in this starter folder. Read BUILD-BRIEF.md first.
Your deliverables are SPEC.md, a coach prompt, four output templates, test cases,
and saved inputs, responses, and review decisions.

## 1. Orient
Start `claude` in your project folder. Source: https://code.claude.com/docs/en/quickstart .
Prompt: Read BUILD-BRIEF.md. Summarize what we must build and identify questions
to resolve. Do not implement yet.

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

## 5. Run cases
Use a fresh conversation and load the coach prompt created in your own project.
Confirm the actual file path. Run an acceptance case from your SPEC.md and save
the exact input and full response. Compare the behavior with your expectation;
do not manually improve a response before reviewing it. Use fresh conversations
for independent cases.

## 6. Challenge in a separate session
Review SPEC.md, the coach prompt, and the saved test responses. For each applicable
requirement, quote the exact response text. Mark pass, fail, or unresolved.
Explain unsupported claims. Do not assume the builder's summary is correct.
Separate sessions organize context; inspect the review rather than treating it as proof.

## 7. Repair
Fix only the reported requirement violation. Repeat the failing case and one that
previously passed. Preserve earlier responses so the team can explain the change.

These are authored teaching prompts, not a transcript of a previous run.
File references in these instructions resolve from your starter folder.
The spec and implementation files are deliverables you create, not supplied answers.
