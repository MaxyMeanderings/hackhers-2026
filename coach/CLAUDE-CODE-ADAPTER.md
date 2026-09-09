# Optional: Claude Code

Claude chat is the default student path; a terminal is optional. Both paths use the single [coaching prompt](PROMPT.md). Sharing that prompt does not prove identical model behavior: see [actual evaluation results](eval/RESULTS.md) for what was tested.

Use your own eligible Claude Code account and existing installation. This workshop uses subscription authentication. Account features and availability can vary. [Official quickstart](https://code.claude.com/docs/en/quickstart).

In the terminal session used for the workshop, remove API and alternate-provider overrides before checking authentication:

```sh
unset ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL
unset CLAUDE_CODE_USE_BEDROCK CLAUDE_CODE_USE_VERTEX CLAUDE_CODE_USE_FOUNDRY
claude auth status --json
```

Continue when `loggedIn` is `true`, `authMethod` is `claude.ai`, and `apiProvider` is `firstParty`. Otherwise complete subscription sign-in first. These commands remove overrides from this shell session; they do not delete stored credentials. The evaluation harness also removes API credentials and refuses non-subscription authentication.

## Start a conversation

From the repository root, start `claude`, paste the entire contents of `coach/PROMPT.md` as the first message, then describe your idea and what prompted it. This does not edit project configuration.

For a dedicated conversation with no coding or connected tools, use the exact canonical prompt as a system instruction:

```sh
claude --model "${COACH_EVAL_MODEL:-opus}" --safe-mode --strict-mcp-config --mcp-config '{"mcpServers":{}}' --tools "" --system-prompt-file coach/PROMPT.md
```

The evaluated print-mode equivalent is implemented in [the portable harness](eval/run.py). Actual runtime, model identifiers, prompt hashes, and outcomes are linked from [evaluation results](eval/RESULTS.md). The evaluated setup uses Claude Opus. The CLI model choice remains configurable; the harness defaults to `opus` and accepts `--model` or `COACH_EVAL_MODEL`. The evaluated model does not certify every other model or account. [Official CLI reference](https://code.claude.com/docs/en/cli-reference).

This tool-free form uses public source material you paste into the conversation. Give the source URL and access date with the excerpt. The coach must disclose that it cannot open a page itself; a URL alone is not evidence of page contents. No API keys, paid integrations, or new project dependencies are needed.

The evaluator runs each case in a fresh Claude Code print-mode session with this system-prompt file. Its conversation mode starts a new session and resumes that actual session for later turns. These runs are distinct from interactive paste or Claude chat; those surfaces are not certified by a command-line result.

## Save your work

Ask for the four deliverables, inspect them, and save approved text using the [templates](templates/). Use anonymous participant labels. Keep real contact information out of this repository. The coach stops for your proceed/narrow/investigate/pivot decision and does not build or publish for you.
