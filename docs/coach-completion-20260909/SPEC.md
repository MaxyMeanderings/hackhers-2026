# Coach completion follow-up

## Authority and preserved history

New bounded task authorized by the user to finish the coach and open a PR after verification. The previous spec-fa7abd1282236c13 failed task, repair ledger, and batch receipts remain historical and unchanged. This task repairs inherited implementation and verifies it; it does not relabel earlier work as proof-passed. Upstream product authority is docs/AGENT-SPEC.md.

## Files to Change

| File | Action |
| --- | --- |
| `coach/PROMPT.md` | Update completion deliverable or reproducible evaluation configuration |
| `coach/CLAUDE-CODE-ADAPTER.md` | Update completion deliverable or reproducible evaluation configuration |
| `coach/README.md` | Update completion deliverable or reproducible evaluation configuration |
| `README.md` | Update completion deliverable or reproducible evaluation configuration |
| `coach/templates/count-ledger.md` | Update completion deliverable or reproducible evaluation configuration |
| `coach/templates/experiment-card.md` | Update completion deliverable or reproducible evaluation configuration |
| `coach/templates/idea-brief.md` | Update completion deliverable or reproducible evaluation configuration |
| `coach/templates/mvp-brief.md` | Update completion deliverable or reproducible evaluation configuration |
| `coach/eval/evaluation-cases.md` | Update completion deliverable or reproducible evaluation configuration |
| `coach/eval/RESULTS.md` | Update completion deliverable or reproducible evaluation configuration |
| `coach/eval/run.py` | Update completion deliverable or reproducible evaluation configuration |
| `coach/examples/study-session.md` | Create labeled synthetic coaching example |
| `.nightshift.toml` | Update completion deliverable or reproducible evaluation configuration |

## Acceptance Criteria

1. GIVEN a student pastes `coach/PROMPT.md` into a fresh Claude chat conversation and states a hackathon idea WHEN the coach responds THEN it opens by asking about the idea and what prompted it before offering any advice, per `docs/AGENT-SPEC.md:21`.
2. GIVEN any point in the conversation WHEN the coach asks a batch of questions THEN the batch contains between 1 and 5 questions, per `docs/AGENT-SPEC.md:10,23`.
3. GIVEN the student has not yet answered a question WHEN the coach continues the conversation THEN it does not fill the gap with an invented fact, per `docs/AGENT-SPEC.md:22`.
4. GIVEN the student names an unfamiliar business term (e.g. "TAM", "switching cost") WHEN the coach uses it THEN the coach briefly explains it, per `docs/AGENT-SPEC.md:24`.
5. GIVEN the student answers a question WHEN the coach's next turn begins THEN it distinguishes what the answer establishes from what remains uncertain, per `docs/AGENT-SPEC.md:25`.
6. GIVEN the six inquiry steps (person/problem, reachable count, alternatives, switching reasons, experiment design, human decision) WHEN the coach runs a full session THEN it follows the sequence and content requirements at `docs/AGENT-SPEC.md:32-74`, including asking whether each account of the problem is the student's own experience, a direct observation, a secondhand report, or a hypothesis (`docs/AGENT-SPEC.md:35-36`).
7. GIVEN the coach cites an externally verifiable claim WHEN it is written into any deliverable THEN it is placed beside a retrievable source URL, and if research tooling fails or is unavailable the coach discloses the limitation and labels the result unverified instead of fabricating it, per `docs/AGENT-SPEC.md:76-82`.
8. GIVEN a student uses the optional Claude Code path via `coach/CLAUDE-CODE-ADAPTER.md` instead of Claude chat WHEN the same idea and answers are supplied THEN the coaching behavior (question batching, contract, inquiry sequence, research rules) is unchanged from the Claude chat path, per `docs/AGENT-SPEC.md:7`.
9. GIVEN a completed coaching session WHEN the student asks for the deliverables THEN the coach can populate all four `coach/templates/*.md` templates (idea brief, count ledger, experiment card, MVP brief) as described in `docs/AGENT-SPEC.md:84-89`.
10. GIVEN a student proposes more than three MVP features WHEN the coach responds THEN it negotiates the list down to at most three, each tied to an observed problem or an explicitly labeled assumption, per `docs/AGENT-SPEC.md:67-68,102`.
11. GIVEN each of the 10 rows in `coach/eval/evaluation-cases.md` (whose `Case`/`Expected behavior` text is retained verbatim from `docs/AGENT-SPEC.md:95-104`, plus a concrete synthetic runnable student prompt per row) WHEN each of the ten is actually run live against `coach/PROMPT.md` in the selected live-evaluation runtime (Claude Code, authenticated) THEN the observed transcript matches the row's expected behavior, and the outcome (pass/fail, notes, and the inspected citation per `docs/AGENT-SPEC.md:106`) is recorded in `coach/eval/RESULTS.md` for all ten cases — this criterion is unmet until all ten live outcomes and their citation inspection are recorded; partial, incomplete, or asserted-but-not-executed evidence never satisfies it.
12. GIVEN a new student with no prior context WHEN they open `coach/README.md` THEN they can determine, without leaving that file, how to start a Claude chat session, how to optionally start a Claude Code session instead, and where the templates and evaluation fixtures live, per `docs/AGENT-SPEC.md:7,9`.

## Behavioral proof mapping

B1: bounded evidence-retention proof supporting AC3/5/6/7: distinguish simulated observations from verified real users and reject fabricated counts or demand in the final structured summary. B2: bounded experiment-retention proof supporting AC9/10: retain the student-selected single feature, reachable participant count, measurable precommitted threshold, assumption label and not-yet-run status across turns. These two machine-checked scenarios do not alone establish every original AC; opening, question-count limits, jargon explanation, the full six-step sequence, spontaneous feature negotiation, four deliverables and citation accuracy additionally require independent semantic review of the ten-case suite and full conversation. D1: AC8 and AC12 documentation inspection: identical canonical prompt reference and discoverable usage; live Claude chat parity remains explicitly unverified unless actually executed. D2: AC11 execution evidence inspection: ten original cases plus full coaching session must be actually executed, independently semantically reviewed, and reported with citation inspection. B1/B2 are prototype model behavior; D1/D2 are documentation/evidence inspection, not ordinary deterministic code logic. Prototype assertions are narrow reproducible facts; independent semantic transcript review remains mandatory and may fail delivery even when assertions pass.

## Verification and limits

Use repaired runtime profile claude-subscription-multiturn-text-v1 with actual prior assistant turns replayed, no tools, no persistent session. It proves tool-free Claude CLI behavior, not browsing or UI parity. Independently authored heldout cases remain outside checkout and are not shared with implementation author. Source seals and ledger-backed development/final gates are required. Two proof repairs allow three total attempts, capped at 64 calls per gate. The full original ten-case and six-stage synthetic coaching conversation evidence supplements the bounded proof scenarios. No fabricated RED, no missing-ledger bypass, no old-budget reset. No production deployment.
