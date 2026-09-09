# Evaluation runtime pin

The first sealed runtime used Claude Code 2.1.263. During continuation, the global
installation reported 2.1.266. The canonical probe rejected that mismatch before
launching a model. The retained receipt is `proof-runtime-version-failure.json`;
it consumed one infrastructure observation and recorded the pending prototype
repair, without changing the development model-launch count.

A task-local copy of 2.1.263 was extracted from the existing npm cache. The global
installation was not downgraded. Package source:
[Anthropic Darwin ARM64 package](https://registry.npmjs.org/@anthropic-ai/claude-code-darwin-arm64/-/claude-code-darwin-arm64-2.1.263.tgz).

- Package SHA-1: `834973ee5bfd712bbda8519b2826838b51cffcf8`.
- Executable SHA-256: `ef5d2909c8af49f31ab6d5487e90316777bc2fac170adfe8160716caa8aaf4f9`.
- Executable: `/private/tmp/coach-cli-2.1.263/package/claude`.
- Version response: `2.1.263 (Claude Code)`.
- Authentication preflight: `loggedIn: true`, `authMethod: claude.ai`,
  `apiProvider: firstParty`, with API credentials and alternate-provider overrides
  removed. No account identifiers or authentication material are stored here.

Evaluation processes put the task-local executable first in PATH and set
`DISABLE_AUTOUPDATER=1` and `DISABLE_UPDATES=1`. These settings prevent this
process from updating its evaluated CLI; they do not change global settings.
See [official update controls](https://code.claude.com/docs/en/installation).

Model selection remains configurable. The scenarios select the `sonnet` alias;
actual reported model identifiers remain in execution evidence. A CLI pin does
not make a hosted model alias immutable. Machine-local paths are provenance,
not portable installation instructions; another machine must verify its own
executable and follow the preserved proof-state rules before evaluation.
