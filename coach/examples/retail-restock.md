# Retail restock alerts: worked example

**Synthetic workshop roleplay — not field evidence.** These numbers belong to
an invented small-boutique-association exercise. No interviews or experiment
were conducted.

This example is the actual five-turn Claude Opus response using the renamed
[go-to-market advisor prompt](../PROMPT.md) (`prompt_sha256`
`a5af84979d38e8c6d88cf08b6fee8ea0dd71c2fdc94365aee5035b942a807bbf` in each
linked record). It exists alongside
[the study-session example](study-session.md) to show the advisor is not
scoped to any one kind of idea — this run is a retail/B2B scenario, not a
campus-club scheduling one, and produces the same TAM-pushback,
sourced-alternatives, and experiment-before-build discipline.

Use it in a curriculum the same way as the study-session example: pause on
what each turn establishes versus what stays Unknown, and note the moment in
turn 3 where the advisor refuses to treat the student's own unverified
recollection of a vendor feature as a source.

## Recorded conversation

| Turn | What the student contributed | Actual response |
| --- | --- | --- |
| 1 | Idea and a directly observed stockout at one boutique | [Opening](../../docs/gtm-rebrand-20260912/conversation-retail-restock/turn-01.json) |
| 2 | Reachable-group count, contacts, workaround, one commitment | [Count distinctions](../../docs/gtm-rebrand-20260912/conversation-retail-restock/turn-02.json) |
| 3 | An unverified personal recollection offered in place of a sourced alternative | [Refuses the unsourced claim](../../docs/gtm-rebrand-20260912/conversation-retail-restock/turn-03.json) |
| 4 | A two-feature experiment proposal with a pre-set success criterion | [Pressure-tests the criterion](../../docs/gtm-rebrand-20260912/conversation-retail-restock/turn-04.json) |
| 5 | Revised plan, synthetic team's Proceed decision, all four outputs requested | [Final response, all four deliverables](../../docs/gtm-rebrand-20260912/conversation-retail-restock/turn-05.json) |

The session had no browsing tools; turn 3 is the advisor declining to treat
the student's own unsourced recollection as evidence, and asking for a real
excerpt or an Unknown instead. Turn 4 catches a mismatch between the
proposed test and the success criterion (a middle-of-the-road result — "2
items flagged" — had no planned response) before the student could proceed
on an unclear rule.

**Review status:** these responses were read by the session that ran them
(an AI agent, not a second independent human or model reviewer) and judged
against `docs/AGENT-SPEC.md`'s conversation contract as part of preparing
this worked example. Each record still ships with
`"judgment": "PENDING_INDEPENDENT_REVIEW"` per the harness's own convention
(`coach/eval/run.py:94`) — treat this as a spot-check, not the same
independent-review bar `coach/eval/RESULTS.md` documents for the original
ten cases. Independent human review before using this as certified evidence
in the presentation is still open work.
