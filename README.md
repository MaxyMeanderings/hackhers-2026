# HackHers 2026

A workshop project for building a local hackathon idea coach with Drew and Tyler Sztuka.

The coach helps students investigate a specific person's problem, count people they can actually reach, research existing alternatives, and design a small experiment before committing to an MVP.

## Start the coach

The Claude Opus terminal evaluation passed all ten original cases and a full
coaching session. See [results and tested limits](coach/eval/RESULTS.md).

1. Open [the coaching prompt](coach/PROMPT.md) and copy the entire document.
2. Paste it into a fresh Claude chat, then describe your idea and what prompted it.
3. Work through the questions. Ask for your idea brief, count ledger, experiment card, and MVP brief when ready.

Use your own eligible account. The optional [Claude Code path](coach/CLAUDE-CODE-ADAPTER.md) uses the same prompt. No API key or new application installation is required for the chat path.

- [Student walkthrough](coach/README.md)
- [Worked synthetic example](coach/examples/study-session.md)
- [Blank output templates](coach/templates/)
- [Recorded evaluation results and limitations](coach/eval/RESULTS.md)

## Workshop planning

- [Agent behavior and evaluation specification](docs/AGENT-SPEC.md)
- [Proposed workshop agenda](workshop/WORKSHOP-DRAFT.md)

The workshop agenda and slide deck are separate planning work. The coach's evaluation results distinguish the tested terminal runtime from unverified Claude chat behavior; a shared prompt alone does not prove parity.

## Organizer references

The [completion follow-up](docs/coach-completion-20260909/SPEC.md) preserves the earlier failed evaluations and records the bounded repair and delivery requirements. Student account access still needs checking before the event.
