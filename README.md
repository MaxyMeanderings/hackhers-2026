# GSU Hack-Her-Thon 2026

A workshop project for building a local hackathon idea coach with Drew and Tyler Sztuka.

The coach will help students investigate a specific person's problem, count people they can actually reach, research existing alternatives, and design a small experiment before committing to an MVP.

## Current status

Repository and behavior specification are in preparation. The runnable local integration, verified example, student setup instructions, and slide deck are not complete yet.

- [Agent behavior and evaluation specification](docs/AGENT-SPEC.md)
- [Proposed workshop agenda](workshop/WORKSHOP-DRAFT.md)

The workshop will demonstrate gstack, BMAD, and NightShift alongside the student project. Exact installation and demo instructions will follow validation of the selected versions.

## Intended build order

1. Follow the approved Claude chat / optional Claude Code profile in the agent spec; verify participant access without requiring API keys or paid integrations.
2. Implement the coach and its research workflow.
3. Run an example and evaluate failures and unsupported claims.
4. Write the student walkthrough from the tested setup.
5. Build the slide deck around the working example.
