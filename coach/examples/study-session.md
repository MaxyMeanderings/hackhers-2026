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
| 1 | Idea and directly observed scheduling difficulty; causation still unknown | [Opening](../../docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/turn-01.json) |
| 2 | Club roster, reachable people, contacts, reports, workarounds, commitments | [Count distinctions](../../docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/turn-02.json) |
| 3 | Existing methods, switching hypothesis, counterevidence, supplied vendor summary | [Alternatives and experiment](../../docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/turn-03.json) |
| 4 | Two-feature experiment and measurable pre-test criterion | [Human decision requested](../../docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/turn-04.json) |
| 5 | Anonymous team approval, date, Proceed decision, four outputs requested | [Final response](../../docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/turn-05.json) |

The coaching session had no browsing tools. Its vendor information came from a
facilitator-supplied summary; the coach preserved that attribution. Independent
source inspection and behavioral judgments are linked in the
[evaluation results](../eval/RESULTS.md).

## Four populated deliverables

The following is the recorded final response, reproduced without correcting or
inventing model output.

All four deliverables below. **Synthetic workshop roleplay — not field evidence.** Save these yourself; I have not written any files, contacted anyone, or built anything.

---

## Idea Brief

**Evidence mode:** Synthetic workshop roleplay — not field evidence

**Target person:** Club organizer coordinating study-session times for a 24-member campus club; members are the responders. Which of the two is the primary target was not explicitly chosen — Unknown.

**Recent problem and evidence type:** Direct observation (student as club member, watching the organizer, not the organizer): the organizer was "chasing availability answers in the group chat"; nobody settled on a time; two planned study sessions did not happen. The causal link between non-settlement and the sessions not happening is the student's account, not separately verified.

**Current behavior or workaround:** Group chat plus manual comparison of availability. All 6 contacted use this. No other tools currently used. Nobody in the scenario reported trying another tool — a statement about reports, not proof none was ever tried.

**Reachable group:** 8 of a 24-member roster reachable before judging.

**Evidence gathered so far:** Six scenario counts (see Count Ledger). 3 of 6 contacted described a recent scheduling problem; 3 reported no recent problem, which is not a problem report in either direction. Why those 3 had no problem: Unknown.

**Alternatives researched (source URL | access date | target user | offering | narrow supported claim):**
https://workspace.google.com/intl/en/products/forms/ | 2026-09-09 | Unknown | survey response collection, response charts, export of raw data to Google Sheets | Google says Forms collects survey responses, shows response charts, and exports raw data to Sheets. Facilitator-supplied summary of vendor claims; page not opened by coach. Availability of these capabilities does not establish fit for this club's scheduling problem. Page silence about scheduling establishes nothing.

**Switching hypothesis:** Student's labeled hypothesis, not a finding — a link inside the existing chat could reduce the organizer's chasing without asking members to install anything. Weakening observation named in advance: if a simple shared link does not help the two participants coordinate without chasing, or if everyone prefers the existing chat, investigate rather than build a new app.

**Unknowns and open questions:** Whether the 2 committed members are among the 3 problem-reporters; what the 3 no-problem members actually do when a time is being set; which specific upcoming session the test covers; who posts the link; whether members saw the original chat messages; all real-fieldwork counts.

---

## Count Ledger

**Evidence mode:** Synthetic workshop roleplay — not field evidence

**Scenario counts (synthetic):**
- Estimated group size and basis: 24 — club roster
- Realistically reachable before judging: 8
- Actually contacted: 6
- Described a recent instance of the problem: 3
- Using an existing workaround: 6 (group chat + manual availability comparison)
- Agreed to a concrete next step: 2

**Real-fieldwork counts:**
- Estimated group size and basis: Unknown
- Realistically reachable before judging: Unknown
- Actually contacted: Unknown
- Described a recent instance of the problem: Unknown
- Using an existing workaround: Unknown
- Agreed to a concrete next step: Unknown

**Participant labels (anonymous only):** Not supplied — counts were given in aggregate only.

**Participant details, only if supplied:** Not supplied. No participant rows have been created from aggregate totals. Whether the 2 who agreed overlap with the 3 problem-reporters is Unknown.

---

## Experiment Card

**Evidence mode:** Synthetic workshop roleplay — not field evidence

**Participants:** The 2 committed members.

**What they do:** Each submits availability through a link posted in the existing group chat; the organizer then compiles the responses manually and posts one mutually available time in the chat.

**What is observed:** Elapsed time, follow-up reminder count, and whether the organizer posts one mutually available time.

**Success criterion set before the test:** Both participants submit within five minutes with zero follow-up reminders, and the organizer identifies and posts a mutually available time within ten minutes total.

**What changes if the result disappoints:** If either part fails, investigate where coordination broke down and narrow the workflow before adding features — do not build additional features or a standalone app. If no session-planning occasion arises during the test window, the result is inconclusive rather than a pass or a failure.

**Result:** Not run.

---

## MVP Brief

**Evidence mode:** Synthetic workshop roleplay — not field evidence

**Feature 1 — availability-submission link posted in the existing chat**
- Description: A single link in the group chat through which each participant submits their availability.
- Tied to observed problem or labeled assumption: Observed (direct observation) — the organizer was "chasing availability answers in the group chat"; all 6 contacted "use the group chat and manually compare availability." Assumption (labeled, untested): collecting availability through one link reduces the chasing.
- Role in the experiment: Both committed participants submit through it.
- Testable acceptance criteria: Both submit within five minutes with zero follow-up reminders.

**Feature 2 — organizer's manual compile-and-post step**
- Description: The organizer reads the submitted availability and posts one mutually available time in the chat.
- Tied to observed problem or labeled assumption: Observed (direct observation) — "nobody settled on a time." Assumption (labeled, untested): a manual compile step by a person is sufficient at this size, so no automated matching is needed yet.
- Role in the experiment: Produces the posted time that ends the coordination attempt.
- Testable acceptance criteria: The organizer identifies and posts a mutually available time within ten minutes total elapsed.

**Deferred features and reasons:** Automated time matching, automated reminders or notifications, calendar integration, member profiles or accounts, and any standalone app — none is exercised by this single test, and no supplied observation supports them yet. Six hours, one beginner coder, and one business student is the stated capacity.

**Student approval to proceed:** Approved
**Approved by:** Team A
**Date:** 2026-09-09
**Decision:** Proceed

---

This records Team A's roleplay decision only. Nothing has been built, sent, or scheduled.
