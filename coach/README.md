# Hackathon Idea Coach

Turn an idea into a specific problem to investigate, a count of reachable people, and a small experiment. You make the final decision. No API key or paid integration is required. Use your own eligible Claude account; account features can vary.

## Start with Claude chat

1. Open [PROMPT.md](PROMPT.md) and copy the entire document.
2. Start a fresh conversation at [claude.ai](https://claude.ai) using your own account.
3. Paste the prompt, then describe your idea and what prompted it.
4. Answer the coach's focused questions with what you know. Unknown is a useful answer.

If browsing is unavailable, paste relevant source excerpts with their URLs and access dates. The coach should disclose the limitation and distinguish source claims from assumptions.

## Optional terminal path

With an existing Claude Code installation and eligible subscription sign-in, open a terminal at this repository root, start `claude`, paste all of `coach/PROMPT.md` as your first message, and describe your idea. Use `claude auth status` to check sign-in. No project configuration edits are needed. [Official startup documentation](https://code.claude.com/docs/en/quickstart).

The [adapter](CLAUDE-CODE-ADAPTER.md) also provides a dedicated tool-free command. Both paths reference the same prompt; this does not establish live behavioral parity. See [evaluation results](eval/RESULTS.md) for tested runtime and remaining limitations.

## Your four outputs

Ask the coach for the outputs when ready; it can produce them directly in chat. Blank versions are available to save yourself:

- [Idea brief](templates/idea-brief.md): person, recent problem, evidence and alternatives.
- [Count ledger](templates/count-ledger.md): estimates, contacts, recent problems, workarounds and commitments.
- [Experiment card](templates/experiment-card.md): observations and a decision rule chosen before testing.
- [MVP brief](templates/mvp-brief.md): at most three features, acceptance criteria and your explicit decision.

Use anonymous participant labels and inspect evidence before sharing. The coach does not implement or publish on your behalf.

## Check the coach

[Evaluation cases](eval/evaluation-cases.md) contain ten synthetic challenges and a full conversation procedure. [Results](eval/RESULTS.md) distinguish actual outcomes from unverified behavior.

Behavior source: [approved specification](../docs/AGENT-SPEC.md), especially lines 7–11, 75–89 and 106.
