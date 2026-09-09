# Optional: Claude Code

Claude chat is the default student path; a terminal is optional. Both paths use the single [coaching prompt](PROMPT.md). Sharing that prompt does not prove identical model behavior: see [actual evaluation results](eval/RESULTS.md) for what was tested.

Use your own eligible Claude Code account and existing installation. Check subscription sign-in with `claude auth status`; no separate API key is required for the subscription path. Account features and availability can vary. [Official quickstart](https://code.claude.com/docs/en/quickstart).

## Start a conversation

From the repository root, start `claude`, paste the entire contents of `coach/PROMPT.md` as the first message, then describe your idea and what prompted it. This does not edit project configuration.

For a dedicated conversation with no coding or connected tools, use the exact canonical prompt as a system instruction:

```sh
claude --safe-mode --strict-mcp-config --mcp-config '{"mcpServers":{}}' --tools "" --system-prompt-file coach/PROMPT.md
```

Flag sources: [official CLI reference](https://code.claude.com/docs/en/cli-reference); the executed print-mode equivalent is recorded in `docs/spec-fa7abd1282236c13/live-eval.py:18-22` and [case 01](../docs/spec-fa7abd1282236c13/live-case-01.json). That run verifies the file flag works on the evaluated installation even though it is omitted from the top-level help listing.

This tool-free form uses public source material you paste into the conversation. Give the source URL and access date with the excerpt. The coach must disclose that it cannot open a page itself; a URL alone is not evidence of page contents. No API keys, paid integrations, or new project dependencies are needed.

The evaluator uses fresh Claude Code print-mode sessions with this system-prompt file. That is distinct from testing interactive paste or Claude chat; those surfaces are not certified by a command-line result.

## Save your work

Ask for the four deliverables, inspect them, and save approved text using the [templates](templates/). Use anonymous participant labels. Keep real contact information out of this repository. The coach stops for your proceed/narrow/investigate/pivot decision and does not build or publish for you.
