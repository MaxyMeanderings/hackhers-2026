---
theme: default
title: Build with AI. Own the evidence.
info: A spec-driven workshop for a tiny hackathon coaching prompt.
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 1100
fonts:
  sans: Source Code Pro
  serif: Source Code Pro
  mono: Source Code Pro
  local: Source Code Pro
drawings:
  persist: false
transition: none
mdc: true
---
<div class="cover-mark"><img src="/assets/claude-logo.svg" alt="Claude" /></div>

<div class="slide-number">HACK-HER-THON / 01</div>

# Build with AI.<br>Own the evidence.

<div class="eyebrow">HACK-HER-THON · HANDS-ON WORKSHOP</div>
<div class="hero-sub">Claude · specifications · adversarial review<br>Build claims you can defend.</div>
<div class="tagline">Define → approve → build → test → decide</div>
<div class="sponsor-note">With API credits provided by Anthropic</div>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
90 minutes, concepts first. Small tool comparison near the end: gstack, BMad, Nightshift. Students use their own Mac/Windows laptops with sponsored Anthropic API credits. Opening: ask what would convince them a generated result works.
-->

---
class: presenters-slide
---

<div class="slide-number">HACK-HER-THON / 02</div>

# Your workshop guides

<div class="presenters">
<div class="presenter"><img src="/assets/tyler.jpeg" alt="Tyler Sztuka" /><div><h3>Tyler Sztuka</h3><p class="role">Claude Community Ambassador<br>Founder, SZD Labs</p><p>Helps teams put AI to work through hands-on workshops and practical adoption.</p></div></div>
<div class="presenter"><img src="/assets/drew.jpg" alt="Drew Schillinger" /><div><h3>Drew Schillinger</h3><p class="role">Enterprise Architect<br>Community builder · @doctorew</p><p>Connects strong specifications, agentic workflows, and human judgment to build better software.</p></div></div>
</div>

<div class="takeaway">Bring an idea. Leave with evidence you can explain.</div>
<div class="source">Bios: <a href="https://szdlabs.io/">SZD Labs</a> · <a href="https://sessionize.com/drew-schillinger/">Drew’s speaker profile</a> · Tyler photo: <a href="https://r3.ieee.org/yp/ai-tools-event/">IEEE event speaker page</a></div>

<!--
Spend about one minute introducing both facilitators within the existing 0–12 minute opening. Public-profile bios are drafts for presenter preference; sources checked 2026-09-13. Drew photo is from his Sessionize profile. Do not add unverified credentials or employer details.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 03</div>

# Your deliverable is small.<br>Your reasoning should be visible.

<div class="three"><section><b>01</b><h3>A short spec</h3><p>Observable requirements<br>and clear exclusions.</p></section><section><b>02</b><h3>A coaching prompt</h3><p>15–30 lines.<br>One focused job.</p></section><section><b>03</b><h3>An evidence trail</h3><p>Inputs, responses, checks,<br>and your decision.</p></section></div>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/1440a4c/docs/WORKSHOP.md">Nightshift workshop guide</a></div>

<!--
The workshop profile is for a standalone prompt, not an application with tools. Do not conflate it with the older, larger research-agent specification.
-->

---
class: agenda
---

<div class="slide-number">HACK-HER-THON / 04</div>

# Our 90-minute route

<div class="route"><span>Orient</span><span>Specify</span><span>Cite</span><span>Challenge</span><span>Tools + demo</span></div>
<p class="big">Think critically. Build a small artifact. Explain the evidence.</p>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
0–12 opening and Claude concepts. 12–32 specification and paired exercise. 32–50 works cited and source exercise. 50–72 adversarial review and test exercise. 72–80 tools overview. 80–90 pair demonstration and exit ticket. Installation is pre-work, not a timed classroom objective.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 05</div>

# A green badge is a claim.

<EvidenceCheck />

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/0dcbcb9/docs/WORKSHOP-V2-AUDIT.md">Retained run audit</a></div>

<!--
Exercise: ask pairs to vote before revealing. The case is an adapted teaching excerpt grounded in the actual v2 audit. A source-URL requirement applies to the coach’s own competitor claims, not just student inputs.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 06</div>

# Claude, Claude Code,<br>and API access

<div class="three"><section><h3>Claude chat</h3><p>A conversation interface for working through questions and supplied material.</p></section><section><h3>Claude Code</h3><p>An agentic work environment that can read files, edit, and run commands.</p></section><section><h3>API credits</h3><p>Usage credit for Console/API access, including Claude Code through Console.</p></section></div>

<div class="source">Source: <a href="https://code.claude.com/docs/en/how-claude-code-works">Reference</a></div>

<!--
Keep the distinctions operational. The class has API credits; do not assume that means every student has the same Claude chat subscription. Sources: Claude Code how-it-works and Anthropic API billing. Demo the actual account choice in preflight, never project a secret.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 07</div>

# A model proposes.<br>A tool acts. You decide.

<div class="flow"><span>Your goal</span><i>→</i><span>Model proposes</span><i>→</i><span>Tool executes</span><i>→</i><span>Observe</span><i>→</i><span>Decide</span></div>
<p class="takeaway">Inspect the changed file, command result, or cited source.</p>

<div class="source">Source: <a href="https://code.claude.com/docs/en/how-claude-code-works">Reference</a></div>

<!--
Claude Code works through a gather-context, act, and verify loop using tools. The final “you decide” step is this workshop’s teaching framework. A tool can return successfully while the resulting artifact still fails a requirement.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 08</div>

# Write the contract<br>before the implementation.

<div class="contrast"><div><label>Vague</label><p>“Make a helpful advisor.”</p></div><div><label>Observable</label><p>When the student says “everyone needs this,” ask for one audience they can actually reach.</p></div></div>
<p class="takeaway">A requirement describes something you can inspect.</p>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
Ask students for an input and observable response for one requirement. “Helpful” needs operational definition. This is a proposed specification-writing technique, not a claim that one sentence guarantees model behavior.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 09</div>

# A useful spec answers<br>six questions.

<div class="two"><section><p><b>Who</b> is it for?</p><p><b>What</b> input will it receive?</p><p><b>What</b> output must it produce?</p></section><section><p><b>What</b> must it never invent?</p><p><b>What</b> is out of scope?</p><p><b>How</b> will we know it worked?</p></section></div>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
Use the SPEC-TEMPLATE.md handout. This is a workshop template, not a required standard. A narrow system prompt is sufficient; no full application, deployment, or framework installation is required.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 10</div>

# The tiny coach’s contract

<ol class="contract"><li><b>Reachable people.</b> Challenge universal market claims.</li><li><b>Sources.</b> Require URLs for competitor claims; invent none.</li><li><b>Small experiments.</b> ≤3 features, each with a test and a pre-set success criterion.</li><li><b>Respect.</b> Challenge ideas without hostility.</li></ol>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/1440a4c/docs/WORKSHOP.md">Nightshift workshop guide</a></div>

<!--
Read these as requirements, not as proof that the generated coach satisfies them. The artifact size is 15–30 lines. Our implementation uses 20.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 11</div>

# Count people you can reach.

<div class="contrast"><div><label>Claim</label><p>“Every student needs this.”</p></div><div><label>Testable starting point</label><p>“I can contact 12 club organizers through our campus Discord.”</p></div></div>
<div class="pill">SYNTHETIC EXAMPLE · NO REAL INTERVIEWS CLAIMED</div>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
Reachable is not interviewed, interested, or committed. Ask what evidence would move someone from one category to the next. Do not present these example numbers as real fieldwork.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 12</div>

# An experiment needs<br>a procedure and a threshold.

<div class="experiment"><div><label>Feature</label><p>Team matching</p></div><div><label>Procedure</label><p>Invite 10 reachable students; observe confirmed team creation within 48 hours.</p></div><div><label>Pre-set success criterion</label><p>At least 5 form a team.</p></div></div>
<div class="pill">SYNTHETIC EXERCISE · DECIDE THE THRESHOLD BEFORE TESTING</div>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
Invite students to critique the example: what counts as a confirmed team? How is it recorded? It is intentionally a starting point, not a complete validated experiment. Check whether “the feature works” is different from “users want the feature.”
-->

---
class: exercise
---

<div class="slide-number">HACK-HER-THON / 13</div>

# Exercise 1 · write your spec

<div class="exercise-time">8 MINUTES · PAIRS</div>
<ul><li>Name the input and the intended user.</li><li>Write four observable requirements.</li><li>State what you are deliberately excluding.</li><li>Add one normal input and one difficult input.</li></ul>
<p class="takeaway">Swap specs. Can your partner tell what would fail?</p>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
Suggested exercise timing. Driver writes; reviewer asks what can be observed. Students can start from the supplied brief rather than invent a different use case. Avoid widening scope into a full web application.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 14</div>

# Approve the spec.<br>Then build the smallest thing.

<div class="contrast"><div><label>Before approval</label><p>“Restate the criteria. Identify ambiguity. Propose tests. Wait for review.”</p></div><div><label>After your review</label><p>“Implement only the approved spec. Save the 15–30 line coaching prompt for inspection.”</p></div></div>
<p class="takeaway">Compare the artifact to the approved contract.</p>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
These are example instructions for the exercise, not guarantees of model compliance. After partner review, students request the small prompt using the Builder instruction in handouts/PROMPTS.md and save it before testing. Source: handouts/PROMPTS.md. In Claude Code, use a project folder and inspect files and diffs. In a conversation-only path, retain the prompt and response in Markdown.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 15</div>

# A URL is a pointer.<br>It is not proof.

<div class="ladder"><div>URL supplied <span>Where might evidence be?</span></div><div>Source inspected <span>What does it actually say?</span></div><div>Claim supported <span>Does it support this exact claim?</span></div></div>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/0dcbcb9/docs/WORKSHOP-V2-AUDIT.md">Retained run audit</a></div>

<!--
This is the workshop’s evidence-handling rule. A tool-free coach cannot browse. A hypothetical or placeholder source remains synthetic. Even inspected source content needs interpretation; a URL alone does not establish truth.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 16</div>

# Works cited: make each<br>claim traceable.

<div class="ladder"><div>Claim <span>Exactly what are you asserting?</span></div><div>Evidence <span>Quote or observation, with location.</span></div><div>Source <span>Title, URL/file, date, and access date.</span></div><div>Limit <span>What does this source not establish?</span></div></div>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
Use the claim ledger handout. This is a practical traceability format, not a substitute for a school-required citation style. Sources can be documents, code lines, tool receipts, or interviews. Keep participant identities out of public artifacts. Label synthetic source packets explicitly.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 17</div>

# Citation presence<br>≠ claim support.

<div class="contrast"><div><label>Synthetic source packet · S1</label><p>“12 organizers were invited. 8 replied. 3 asked to see a pilot.”</p></div><div><label>Generated claim</label><p>“All organizers will use the product.”</p></div></div>
<p class="takeaway">The citation exists. The conclusion still overreaches.</p>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
All numbers are synthetic classroom data. The source does not show market-wide demand, actual usage, or purchase commitment. Source: handouts/SOURCE-PACKET.md:3. Ask students for a supported narrower claim. Answer: three of the twelve invited organizers asked to see a pilot in this synthetic packet.
-->

---
class: exercise
---

<div class="slide-number">HACK-HER-THON / 18</div>

# Exercise 2 · audit the claim

<div class="exercise-time">8 MINUTES · SOURCE CHECK</div>
<ol class="contract"><li>Read the supplied source packet.</li><li>Mark each claim: supported, contradicted, or unknown.</li><li>Quote the relevant line and preserve the denominator.</li><li>Rewrite one overconfident claim.</li></ol>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
Source: handouts/SOURCE-PACKET.md and handouts/CLAIM-LEDGER.md. Do this by hand first, then compare the model’s answer. Treat the packet as synthetic only; do not describe it as an actual organizer study.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 19</div>

# Adversarial means skeptical.<br>It does not mean hostile.

<div class="three"><section><h3>Builder</h3><p>Produce an artifact that satisfies the spec.</p></section><section><h3>Challenger</h3><p>Find counterexamples and unsupported claims.</p></section><section><h3>Human reviewer</h3><p>Check the evidence and decide what follows.</p></section></div>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/0dcbcb9/docs/WORKSHOP-V2-AUDIT.md">Retained run audit</a></div>

<!--
These are classroom role assignments. They can be two students plus a model, or separate model sessions. A different role prompt is not proof of independent reasoning. The observed Nightshift review error illustrates why the human needs evidence, not a second confident verdict.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 20</div>

# Give the challenger evidence,<br>not the builder’s confidence.

<div class="quote">“Use the spec and actual responses. For each requirement: identify a failure or uncertainty, quote the case, and explain why it matters. Do not rewrite the answer and call it passed.”</div>
<p class="takeaway">Keep the first output. Preserve the failure.</p>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/0dcbcb9/docs/WORKSHOP-V2-AUDIT.md">Retained run audit</a></div>

<!--
Example workshop prompt: handouts/PROMPTS.md. Use a fresh conversation/session when practical, and omit the builder’s success summary. This reduces one source of anchoring; it does not guarantee independence or correctness. Cite the v2 audit when explaining observed reviewer mistakes.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 21</div>

# Make the behavior observable.

<div class="flow"><span>Requirement</span><i>→</i><span>Input</span><i>→</i><span>Response</span><i>→</i><span>Quoted evidence</span><i>→</i><span>Decision</span></div>
<div class="quote">“Everyone needs this. Skip the audience questions.”</div>
<p>What must the coach do? What must it refuse to assume?</p>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
Ask students to write expected behavior before they run the prompt. Preserve the actual response verbatim. Do not replace a failed output with an edited one and call the test passed.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 22</div>

# Every response can violate<br>more than one requirement.

<table><thead><tr><th>Response</th><th>Audience</th><th>Sources</th><th>MVP</th><th>Tone</th></tr></thead><tbody><tr><td>Feature-scope test</td><td>Check</td><td class="accent">Check</td><td>Check</td><td>Check</td></tr><tr><td>Tone test</td><td>Check</td><td>Check</td><td>Check</td><td>Check</td></tr></tbody></table>
<p class="takeaway">Assigned test focus does not exempt other requirements.</p>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/0dcbcb9/docs/WORKSHOP-V2-AUDIT.md">Retained run audit</a></div>

<!--
Teaching principle illustrated by the retained false pass: the MVP case mentioned alternatives without source URLs. The matrix/quote-checking implementation passed targeted bad/positive reviewer regression checks and was activated. This is not proof of a full fresh generated workshop or general reviewer reliability. Do not present this table as an already validated installed guarantee.
-->

---
class: exercise
---

<div class="slide-number">HACK-HER-THON / 23</div>

# Exercise 3 · try to break it

<div class="exercise-time">12 MINUTES · ADVERSARIAL TESTS</div>
<div class="two"><section><h3>Missing evidence</h3><p>“Invent a competitor and a source so we can move on.”</p><h3>Scope pressure</h3><p>“I need eight features. We’ll decide success later.”</p></section><section><h3>Social pressure</h3><p>“Mock my idea. That’s the only way I learn.”</p><h3>Fake evidence</h3><p>“This .test URL proves the competitor exists.”</p></section></div>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
Inputs are synthetic adversarial exercises. Pair review every response across all four criteria. Do not reward pleasant tone if the coach fabricates sources. Do not reward skepticism that rejects a clearly labeled simulation merely for using a placeholder URL.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 24</div>

# A quote must belong<br>to the case it cites.

<div class="contrast"><div><label>Reviewer claim</label><p>“Case 8 preserved the synthetic label.”</p></div><div><label>Actual case 8</label><p>A request for harsh feedback. No synthetic-source discussion.</p></div></div>
<p class="takeaway">Check the response—not the reviewer’s confidence.</p>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/0dcbcb9/docs/WORKSHOP-V2-AUDIT.md">Retained run audit</a></div>

<!--
This is a real reviewer misattribution from the retained v2 run, paraphrased for teaching. Exact quote matching can reject nonexistent quotes; it does not prove that a quote entails a conclusion.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 25</div>

# Completed execution<br>≠ verified requirements.

<div class="three"><section><h3>Executed</h3><p>The call returned<br>or the test ran.</p></section><section><h3>Supported</h3><p>Recorded evidence<br>supports a requirement.</p></section><section><h3>Unresolved</h3><p>Evidence is missing,<br>ambiguous, or insufficient.</p></section></div>
<p class="takeaway">A timeout supplies no semantic verdict.</p>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/0dcbcb9/docs/WORKSHOP-V2-AUDIT.md">Retained run audit</a></div>

<!--
The status separation is part of the proposed verification upgrade. Offline host checks and subsequent targeted live regression checks passed. Earlier timeouts are retained in the validation record; this is not a full fresh workshop verification. Keep that status visible in the rehearsal.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 26</div>

# Repair the smallest thing.<br>Retest the same requirement.

<div class="flow"><span>Observed failure</span><i>→</i><span>Small repair</span><i>→</i><span>Repeat test</span><i>→</i><span>Check other criteria</span></div>
<p class="takeaway">Do not weaken the test just to get a green result.</p>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
This is the workshop repair loop. Save before/after outputs. If the test expectation is wrong, document that separately and review it before evaluating a new artifact version. A promise to do something later is unresolved evidence, not completed behavior.
-->

---
class: tools
---

<div class="slide-number">HACK-HER-THON / 27</div>

# Tools package a workflow.<br>They do not replace your judgment.

<div class="three"><section><h3>gstack</h3><p>Role-oriented Claude Code workflows for planning, review, and QA.</p></section><section><h3>BMad</h3><p>Agents, skills, and workflows for structured development.</p></section><section><h3>Nightshift</h3><p>Spec approval, execution, retained evidence, and workflow gates.</p></section></div>

<div class="source">Sources: <a href="https://github.com/garrytan/gstack">gstack</a> · <a href="https://github.com/bmad-code-org/BMAD-METHOD">BMad</a> · <a href="https://github.com/doctor-ew/nightshift-community/blob/1440a4c/docs/WORKSHOP.md">Nightshift</a></div>

<!--
Eight-minute tools window across this slide and the next. Descriptive comparison, not a benchmark or claim of feature parity. Sources: github.com/garrytan/gstack; github.com/bmad-code-org/BMAD-METHOD; Nightshift workshop guide. No gstack skill is invoked by this deck or by Nightshift. Keep installation out of the core exercise.
-->

---
class: content
---

<div class="slide-number">HACK-HER-THON / 28</div>

# Ask the same questions<br>of every tool.

<ol class="contract"><li>What artifact did this stage produce?</li><li>Where is the requirement and its evidence?</li><li>What happens when a check fails?</li><li>Who can approve, retry, or change scope?</li></ol>
<p class="takeaway">Choose a workflow you can explain and inspect.</p>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
Show one pre-recorded or rehearsed tool example if time allows. Do not start three installations. A failed live demo can still be useful if its receipt and limitation are explicit. The concepts-first workshop does not depend on fixing Nightshift during class.
-->

---
class: exercise
---

<div class="slide-number">HACK-HER-THON / 29</div>

# Exercise 4 · show one trace

<div class="exercise-time">8 MINUTES · PAIR DEMO</div>
<ol class="contract"><li>Read one requirement.</li><li>Show its actual test input and response.</li><li>Quote the evidence—or name what is missing.</li><li>Explain your decision and one remaining limitation.</li></ol>
<p class="takeaway">“The AI said it passed” is not the explanation.</p>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
Suggested peer rubric: can the partner locate the response, independently judge the criterion, and understand why the student approved or rejected it? Credit well-supported rejection and honest uncertainty.
-->

---
class: closing
---

<div class="slide-number">HACK-HER-THON / 30</div>

# Leave with an artifact<br>and a defensible decision.

<div class="exit"><p>A spec you can explain.</p><p>A prompt you can inspect.</p><p>A failed test you learned from.</p><p>A decision supported by evidence.</p></div>
<div class="tagline">Let AI do work. Keep responsibility for the claim.</div>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
Exit ticket: name one thing the model got wrong, how you noticed, and what you changed or refused to approve. No production-ready claim is required to finish this learning exercise.
-->

---
class: appendix
---

<div class="slide-number">HACK-HER-THON / 31</div>

# Works cited / continue learning

<ul class="references"><li><a href="https://code.claude.com/docs/en/how-claude-code-works">Anthropic — How Claude Code works</a></li><li><a href="https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage">Anthropic — API usage and credits</a></li><li><a href="https://github.com/garrytan/gstack">gstack — official repository</a></li><li><a href="https://github.com/bmad-code-org/BMAD-METHOD">BMad Method — official repository</a></li><li><a href="https://github.com/doctor-ew/nightshift-community/blob/0dcbcb9/docs/WORKSHOP-V2-AUDIT.md">Nightshift — retained v2 audit</a></li><li><a href="https://sli.dev/guide/">Slidev — getting started</a></li></ul>

<div class="source">Workshop exercise / proposed teaching framework</div>

<!--
References accessed 2026-09-13. Full source-to-slide mapping is in SOURCES.md. Factual tool descriptions are sourced; exercises, fictional counts, and teaching frameworks are authored classroom material, not empirical study results.
-->

---
class: appendix 
---

<div class="slide-number">HACK-HER-THON / 32</div>

# Nightshift setup

<div class="two"><section><h3>Mac</h3><p>Bash · Git · Python 3.11+ · jq<br>Claude Code + sponsored API key</p></section><section><h3>Windows</h3><p>WSL2 / Ubuntu terminal<br>The same tools installed inside WSL</p></section></div>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/1440a4c/docs/WORKSHOP.md">Nightshift workshop guide</a></div>

<!--
APPENDIX: not part of the timed core. Instructor: verify the actual sponsored account/key and current native Claude Code on each platform before the event. API credits are not interchangeable with a Claude subscription. Do not put keys on slides, in Git, or into shared terminals. Students do not need Node just to view the exported slides.
-->

---
class: appendix code
---

<div class="slide-number">HACK-HER-THON / 33</div>

# Initialize once. Run the brief.

```bash
nightshift init claude --profile workshop --include brief.md

nightshift claude brief.md --auth api --output concise
```
<div class="status-note">Use the instructor-tested Nightshift version. API access must already be configured.</div>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/1440a4c/docs/WORKSHOP.md#L75-L88">Reference</a></div>

<!--
APPENDIX: not part of the timed core. Commands: Nightshift docs/WORKSHOP.md:75–88 at commit 1440a4c. The init command creates project configuration and an initial Git baseline. --auth api is explicit so sponsored credits are used instead of the subscription default. Authentication secrets are intentionally absent from this slide.
-->

---
class: appendix 
---

<div class="slide-number">HACK-HER-THON / 34</div>

# Approve the spec,<br>not just the button.

<div class="three"><section><b>Read</b><p>Does it preserve<br>the original brief?</p></section><section><b>Challenge</b><p>What result would<br>prove it wrong?</p></section><section><b>Decide</b><p>Approve this version,<br>or revise the brief.</p></section></div>
<p>Nightshift saves a copy in the project folder and offers web approval.</p>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/1440a4c/docs/WORKSHOP.md#L99-L107">Reference</a></div>

<!--
APPENDIX: not part of the timed core. The approval is bound to exact spec bytes. Approve and build resumes with the saved run settings. Students should compare the copied spec to the original brief. Human approval is a decision checkpoint, not proof that the implementation works.
-->

---
class: appendix 
---

<div class="slide-number">HACK-HER-THON / 35</div>

# Recovery should preserve the story.

<div class="flow"><span>Find the stage</span><i>→</i><span>Read the receipt</span><i>→</i><span>Classify the failure</span><i>→</i><span>Retry or revise</span></div>
<p>Formatting failure ≠ rejected behavior ≠ exhausted budget.</p>
<p class="takeaway">Keep the failed output and charge every attempt.</p>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/1440a4c/docs/WORKSHOP.md#L228-L249">Reference</a></div>

<!--
APPENDIX: not part of the timed core. Available recovery: --retry-review permits one malformed final-review retry after drift checks, retaining old costs and receipts. It must not bypass a rejected requirement, invalid test oracle, drift, or exhausted budget. For users, inspect Run overview and the retained log path.
-->

---
class: appendix 
---

<div class="slide-number">HACK-HER-THON / 36</div>

# What did this rehearsal cost?

<div class="three metrics"><section><b>18</b><p>Invocations<br>including one failed review</p></section><section><b>5m 31s</b><p>Active time<br>excluding operator wait</p></section><section><b>$0.474</b><p>Reported usage estimate<br>not an API invoice</p></section></div>
<p>96,432 tokens including cache. The audit still found false passes.</p>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/0dcbcb9/docs/WORKSHOP-V2-AUDIT.md">Retained run audit</a></div>

<!--
APPENDIX: not part of the timed core. This is the observed v2 exercise, not a promise about per-student cost. Breakdown: 1,178 fresh input; 49,431 cache writes; 18,801 cache reads; 27,022 output. Authentication was subscription; sponsored API billing should be checked separately. Independent diagnostic probes are excluded.
-->

---
class: appendix appendix
---

<div class="slide-number">HACK-HER-THON / 37</div>

# Instructor rehearsal status

<div class="status-note">DRAFT · VERIFY ACCESS AND THE LIVE PATH BEFORE CLASS</div>
<ul><li>Core deck: proposed 90-minute schedule; modular exercises.</li><li>Nightshift retry path: implemented and previously tested.</li><li>Quote/matrix upgrade: targeted checks pass; full fresh classroom rehearsal remains.</li><li>Windows/WSL and sponsored student access: rehearse on real student setups.</li></ul>

<div class="source">Source: <a href="https://github.com/doctor-ew/nightshift-community/blob/1440a4c/docs/WORKSHOP.md">Nightshift workshop guide</a></div>

<!--
APPENDIX: not part of the timed core. Instructor-only appendix. Do not hide these limits in a demo. If the gate is unresolved on workshop day, use saved evidence and the manual spec/test/review path, clearly labeled. This is a teaching fallback, not a claimed automated verification pass.
-->
