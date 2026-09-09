# Study-session scheduling: worked example

**Synthetic workshop roleplay — not field evidence.** These numbers belong to
an invented club exercise. No interviews or experiment were conducted.

This example is the actual final response from a five-turn Claude Opus session
using the [coaching prompt](../PROMPT.md). The earlier turns establish the
observation, separate counts, alternatives, switching hypothesis, and experiment.
The student then chooses Proceed and requests all four deliverables.

Use the conversation in a curriculum to pause at three decisions: what the
observation establishes, what the six counts mean, and what result would cause
the team to change direction. A completed brief is a plan to learn, not proof
that demand exists.

## Recorded conversation

| Turn | Student contribution and coaching stage | Actual input and response |
| --- | --- | --- |
| 1 | Idea and directly observed scheduling difficulty; causation still unknown | [Opening](../../docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-causal-repair/turn-01.json) |
| 2 | Club roster, reachable people, contacts, reports, workarounds, commitments | [Count distinctions](../../docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-causal-repair/turn-02.json) |
| 3 | Existing methods, switching hypothesis, counterevidence, supplied vendor summary | [Alternatives and experiment](../../docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-causal-repair/turn-03.json) |
| 4 | Two-feature experiment and measurable pre-test criterion | [Human decision requested](../../docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-causal-repair/turn-04.json) |
| 5 | Anonymous team approval, date, Proceed decision, four outputs requested | [Final response](../../docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-causal-repair/turn-05.json) |

The coaching session had no browsing tools. Its vendor information came from a
facilitator-supplied summary; the coach preserved that attribution. Independent
source inspection and behavioral judgments are linked in the
[evaluation results](../eval/RESULTS.md).

## Four populated deliverables

The following is the recorded final response, reproduced without correcting or
inventing model output.

**Synthetic workshop roleplay — not field evidence**

---

## Idea Brief

**Evidence mode:** Synthetic workshop roleplay (not field evidence)

**Target person:** Campus club study-session organizer, and club members needing a session time

**Recent problem and evidence type:** Student's direct observation, yesterday: organizer was "chasing availability answers in the group chat"; "nobody settled on a time" and two planned sessions "did not happen." Student was a club member watching, not the organizer. Whether members would have attended had a time been set: Unknown.

**Current behavior or workaround:** All 6 contacted members "currently use the group chat and manually compare availability." No other tool use was reported (a statement about reports, not proof of absence).

**Reachable group:** 8 of 24 roster members reachable before judging

**Evidence gathered so far:** One direct observation of a chat exchange; 6 contacts with 3 recent problem descriptions, 3 no-problem reports, 6 workaround users, 2 concrete next-step commitments. All synthetic scenario values.

**Alternatives researched (source URL | access date | target user | offering | narrow supported claim):**
- https://workspace.google.com/intl/en/products/forms/ | 2026-09-09 | Unknown | Survey response collection, response charts, export to Google Sheets | Google says Forms collects survey responses, shows response charts, and exports raw data to Google Sheets. Facilitator-supplied summary of vendor claims; page not opened by coach. Does not establish that it solves club study-session scheduling.
- Continuing the current manual chat process (in-club alternative, no source needed)

**Switching hypothesis:** Student's hypothesis, not a finding — "a link in the existing chat could save the organizer from chasing answers without asking members to install anything."

**Unknowns and open questions:** Why the 3 no-problem members report no problem, and what they do when a time is needed; whether chasing and the missed sessions are causally linked; who posts the availability link; when the next real session need occurs; whether the 2 committed participants represent the other 6; all real-fieldwork counts.

---

## Count Ledger

**Evidence mode:** Synthetic workshop roleplay (not field evidence)

**Scenario counts (supplied):**
- Estimated group size and basis: 24 (club roster)
- Realistically reachable before judging: 8
- Actually contacted: 6
- Described a recent instance of the problem: 3
- Using an existing workaround: 6 (group chat + manual availability comparison)
- Agreed to a concrete next step: 2

**Real-fieldwork counts (separate):**
- Estimated group size and basis: Unknown
- Realistically reachable before judging: Unknown
- Actually contacted: Unknown
- Described a recent instance of the problem: Unknown
- Using an existing workaround: Unknown
- Agreed to a concrete next step: Unknown

**Participant labels (anonymous only):** Individual labels not supplied. The 2 committed participants are referred to here as Participant A and Participant B (coach-assigned labels for readability).

**Participant details, only if supplied:** Not supplied. No per-participant rows are available; the counts above are aggregates and no rows are derived from them.

*Note: the 3 no-problem reports are not problem reports, and none of these counts extrapolate to the wider campus.*

---

## Experiment Card

**Evidence mode:** Synthetic workshop roleplay (not field evidence)

**Participants:** The 2 committed club members (Participant A, Participant B), plus the club organizer performing the compile-and-post step

**What they do:** Each committed participant submits availability through a link posted in the existing group chat. The organizer then manually compiles the responses and posts one mutually available time. Who posts the link itself: Unknown.

**What is observed:** Elapsed time, follow-up reminder count, and whether the organizer posts one mutually available time

**Success criterion set before the test:** Both committed participants submit within five minutes with zero follow-up reminders, and the organizer identifies and posts a mutually available time within ten minutes total

**What changes if the result disappoints:** If either part fails, investigate where coordination broke down and narrow the workflow before adding features

**Result:** Not run

---

## MVP Brief

**Evidence mode:** Synthetic workshop roleplay (not field evidence)

**Feature 1 — Availability-submission link posted in the existing chat**
- Description: A single link, shared in the group chat the club already uses, through which a member submits their availability
- Tied to observed problem or labeled assumption: Evidence — all 6 contacted members "currently use the group chat and manually compare availability"; observed, "nobody settled on a time." **Assumption:** submitting to a link instead of replying in chat reduces the organizer's need to chase answers. Difficulty was observed; its cause is not established.
- Role in the experiment: Both committed participants submit through it; submissions and reminder count are the measured signals
- Testable acceptance criteria: Both participants submit within five minutes, with zero follow-up reminders

**Feature 2 — Organizer's manual compile-and-post step**
- Description: The organizer reads the submitted availability, identifies an overlapping time, and posts it in the chat. Manual, no automation.
- Tied to observed problem or labeled assumption: Evidence — direct observation of the organizer "chasing availability answers in the group chat." **Assumption:** once availability is collected in one place, a human can settle a time quickly without further chasing.
- Role in the experiment: Produces the observable end state — a posted mutually available time
- Testable acceptance criteria: Organizer identifies and posts one mutually available time within ten minutes total elapsed

**Deferred features and reasons:** Automated overlap detection, member profiles or accounts, notifications/reminders, calendar integration, and anything requiring an install — none is exercised by this single test, and the switching hypothesis explicitly avoids asking members to install anything. Six hours, one beginner coder, and one business student also argue for the manual path first.

**Student approval to proceed:** Approved

**Approved by (anonymous student or team label):** Team A

**Date (supplied date or Unknown):** 2026-09-09

**Decision (proceed / narrow / investigate further / pivot, or pending):** Proceed

---

This records Team A's roleplay decision only. Nothing has been built, sent, or contacted, and no files were written — copy these four sections wherever you keep your workshop notes.
