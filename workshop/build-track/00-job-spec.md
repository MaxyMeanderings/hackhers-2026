# Stage 0 — define the job before writing a prompt

This is the first step of the build track: before any prompt text exists, write
down what the assistant is for. Skipping this step is the most common reason a
first prompt disappoints — the "prompt" wasn't wrong, the job was never defined.

Five questions, answered in a few lines each:

1. **Job.** What decision does the student walk away able to make? (Not "chat
   about my idea" — "decide whether to build it, narrow it, or drop it.")
2. **Input.** What does the assistant start with? (An idea and what prompted
   it — not a finished pitch.)
3. **Tools.** What can it actually use? Web research, pasted text, nothing?
   Say so explicitly — an assistant that silently has no tools will still
   *sound* like it researched something unless the prompt forbids that.
4. **Boundaries.** What must it never do? (Invent a competitor, a quote, a
   count, or a citation. Contact anyone. Publish anything.)
5. **Output.** What artifact proves the session was useful, independent of
   how the conversation felt?

## Worked example: this repo's actual job spec

The shipped coach answered these same five questions in
[`docs/AGENT-SPEC.md`](../../docs/AGENT-SPEC.md) before `coach/PROMPT.md` was
written:

| Question | Answer in this repo |
| --- | --- |
| Job | "Help students turn a hackathon idea into a defensible, small experiment." (`docs/AGENT-SPEC.md:15`) |
| Input | A person and a recent problem — "Tell me about the last time," not a hypothetical (`docs/AGENT-SPEC.md:26-28`) |
| Tools | Public links and pasted research; no required API keys (`docs/AGENT-SPEC.md:8`) |
| Boundaries | "Never fabricate browsing, source content, quotations, interviews, counts, prices, or market estimates." (`docs/AGENT-SPEC.md:79`) |
| Output | Idea brief, count ledger, experiment card, MVP brief — four named files, not "a good conversation" (`docs/AGENT-SPEC.md:87-90`) |

Notice the boundaries line is the one a first draft prompt almost always
leaves out. Stage 1 writes a prompt that skips it on purpose, so the failure
is visible before the fix is.

Next: [`01-prompt-v1.md`](01-prompt-v1.md).
