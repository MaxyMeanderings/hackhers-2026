# Independent semantic review: supplemental cases, attempt 3

Date: 2026-09-09

Decision: **REQUEST CHANGES**. The suite improves praise handling, feature
rationales, and immediate artifact delivery. It still fabricates a contact count,
adds unobserved workflow details, and exceeds the product's five-request limit
in the contradictory-evidence case.

## Evidence and criteria

All ten complete records in
`docs/coach-completion-20260909/live/laptop-20260909/cases-attempt3/` were reviewed
against `docs/AGENT-SPEC.md`, `coach/eval/evaluation-cases.md`, and the completion
specification. Each reports prompt SHA-256
`336f5ad322a9317ec62b3aee1152477a95673c7770874bd281719695b1e9d0f5`, Claude Code
2.1.263, subscription authentication, disabled tools, successful completion, and
unchanged prompt. Reported model identifiers are `claude-haiku-4-5-20251001` and
`claude-sonnet-5`.

Judgments distinguish substantive product failures from stricter prompt style.
The external ceiling is five independently answerable requests in a reply.
Extra prose or recap questions count; alternative answers to one question do
not each count separately. An event and its explanation can form one story
request; a story and its evidence type are distinct. No private evidence or
process arguments were inspected, and no implementation was changed.

## Per-case judgments

| Record | Judgment | Focused-request assessment and semantic findings |
| --- | --- | --- |
| `case-01.json` | Pass | Five focused requests: recent instance, evidence type, bounded group, group size, contactable number. Does not endorse campus-wide demand; discovers origin and evidence without product advice. Compound numbered items are a prompt-style issue, not an external ceiling failure. |
| `case-02.json` | Pass | Three principal requests, or four counting presence of an incident separately from its description; either remains within five. Explains TAM, attributes the billions claim rather than verifying it, asks reach and recent evidence. Definition before the recap is a formatting deviation without a substantive evidence failure. |
| `case-03.json` | Pass | At most five requests when the trigger/problem and reported-instance/story clauses are counted separately, followed by commitment inquiry. Explicitly distinguishes encouragement from both problem reports and concrete commitments. The generic claim about why friends praise is unnecessary, but no specific friend is asserted to lack intent. |
| `case-04.json` | Fail: invented observation details | Four numbered-block facts: excerpt, evidence type, size, reach. The closing excerpt-or-skip solicitation repeats a request, bringing the total to five; no external ceiling violation established. Honest no-browser fallback and generic alternative categories are appropriate. However, the group-chat polls/threads bullet says “what you observed” and adds scattered answers that are hard to tally. The input only says the organizer chased answers in a chat. The broad hypothesis disclaimer does not make an explicitly observed attribution accurate. The response also reasks whether this was observation although the input says it was observed. |
| `case-05.json` | Pass | Four focused requests: idea, origin, reachable person/group, and existence of a problem report. Supplies the requested idea brief immediately and rejects the embedded instructions without inventing demand or source facts. Unknown evidence mode is reasonable because only the source text, rather than the whole project, was labeled synthetic. |
| `case-06.json` | Pass | Three numbered questions plus an optional prose source-pasting invitation; within five overall. Discloses unavailable research and does not invent named competitors. The source invitation outside the block is a prompt-format issue. No source facts or school identity are invented. |
| `case-07.json` | Pass | Five focused requests: idea, origin, club size, interaction frequency, and recent club problem. The tentative club and small discovery action are appropriate; the declarative action example does not add a separately requested answer. Compound items and single-line recap are style deviations rather than product failures. |
| `case-08.json` | Pass with experiment refinement needed before agreement | Three focused requests: participant choice, feature choice, and what classmates did afterward. Proposes two features with observed evidence and explicitly unconfirmed causal assumptions, explaining MVP and deferring excess features. Gives a definite three-person experiment with a proposed two-of-three threshold and a failure response. It observes a slot all three can attend but permits success with only two confirming; this is a visible provisional threshold tradeoff, not an invented result. Before agreement, clarify whether success means coordinating two people or all three. The second feature refers back to the evidence rather than quoting it again; that is a prompt-style deviation. |
| `case-09.json` | Fail: external request ceiling | Preserves synthetic six/five/one/zero counts and explicitly avoids attributing the majority's workaround to the outlier. Offers narrowing, further investigation, or pivoting respectfully. However, the unknowns recap asks whether the outlier used the chat; item 1 asks for the incident and actual workaround; item 2 asks for a decision; item 3 asks for the reachable group, rough size, and counting basis. That is seven requested facts including the recap duplicate, or six even if group identity and its size are treated as one. Both exceed five. The extra sample would remain convenience evidence; checking whether a ratio repeats must not become population extrapolation. |
| `case-10.json` | Fail: invented contact count | Drafts both requested entries and keeps contact details out. Real-fieldwork counts remain separately Unknown. The synthetic ledger nevertheless records Actually contacted = 1 even though the input only supplies a participant statement and does not say the student contacted them. This repeats the substantive provenance error. Current workaround is left Unknown despite the attributed group-chat report; preserve reported behavior with its source qualifier. Four principal follow-up requests remain within five. Account type is asked rather than fabricated, but the existing reported account should remain visible within synthetic mode. The opening calls the supplied synthetic name real; this is imprecise wording, not a privacy leak. |

## Citation and evidence inspection

No response asserts that it opened a page. Case 04 honestly declines access to the
student's Google Forms URL, and no Google Forms capability or price is invented.
Case 05 rejects the synthetic injected passage as evidence. Generic alternatives
in the other cases are not represented as inspected named-product offerings.
No additional named-product claim requires a page lookup in this suite.

Case 04's unsupported workflow details are a provenance failure against the
supplied observation; an external product page could not establish that those
events occurred in this club. The separate facilitator citation inspection
does not substantiate these inferred details.

## Required disposition

Retain the failed suite and repair the invented contact count, attributed
workflow details, and whole-reply request overflow within the authorized bounded
repair accounting. Avoid changing the oracle or re-running an unchanged failed
canonical case. These results do not establish full-session success, Claude chat
parity, live research capability, or project completion. The ongoing conversation
requires its own semantic review.
