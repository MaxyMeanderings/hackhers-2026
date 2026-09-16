---
theme: default
title: Build with AI. Own the evidence.
info: Build and use a go-to-market coach with Claude Code.
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 1280
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

<div class="slide-number">Hackhers</div>

# Build a coach.<br>Use it to build better.

<div class="cover-mark"><img src="/assets/claude-logo.svg" alt="Claude" /></div><div class="hero-sub">An idea → a testable spec → working behavior.<br>A coach → evidence → your hackathon MVP.</div><div class="tagline">Claude Code · go-to-market discovery · human judgment</div><div class="sponsor-note">API credits provided by Anthropic</div>

<div class="source">Workshop walkthrough · teaching example</div>

<!--
Open with the actual coach, not tool setup. Two linked activities: build this coach and use it to scope the team project.
-->

---
class: presenters-slide
---

<div class="slide-number">Hackhers</div>

# Your workshop guides



<div class="presenters">
<div class="presenter"><img src="/assets/tyler.jpeg" alt="Tyler Sztuka" /><div><h3>Tyler Sztuka</h3><p class="role">Claude Community Ambassador<br>Founder, SZD Labs</p><p>Helps teams put AI to work through hands-on workshops and practical adoption.</p></div></div>
<div class="presenter"><img src="/assets/drew.jpg" alt="Drew Schillinger" /><div><h3>Drew Schillinger</h3><p class="role">Enterprise Architect<br>Community builder · @doctorew</p><p>Connects strong specifications, agentic workflows, and human judgment to build better software.</p></div></div>
</div>

<div class="takeaway">Bring an idea. Leave with evidence you can explain.</div>


<div class="source"><a href="https://szdlabs.io/">Tyler: SZD Labs</a> · <a href="https://sessionize.com/drew-schillinger/">Drew: speaker profile</a></div>

<!--

-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Copilot vs autopilot: own the decision.

<div class="copilot-content"><div class="two"><section><h3>Copilot · stay engaged</h3><p>Frame the problem and state your assumptions.</p><p>Ask AI for options, explanations, and challenges.</p><p>Check the evidence. Explain why you accept or change the result.</p></section><section><h3>Autopilot · the trap</h3><p>Delegate the framing before understanding the problem.</p><p>Accept a convincing answer without checking it.</p><p>Struggle to explain the choice when someone challenges it.</p></section></div><a class="post-thumbnail" href="./assets/copilot-autopilot-post.png" target="_blank" rel="noopener noreferrer" aria-label="Open Chorouk Malmoum’s original post image in a new tab"><img src="/assets/copilot-autopilot-post.png" alt="Screenshot of Chorouk Malmoum’s LinkedIn post contrasting copilot and autopilot approaches to AI." /><span>Read original post ↗<br>Opens full size in a new tab</span></a></div><div class="takeaway">Before you ship: can you explain the choice, show the evidence, and name what would change your mind?</div>

<div class="source">Inspired by Chorouk Malmoum’s LinkedIn post · supplied screenshot · workshop adaptation</div>

<!--
Spend about one minute here. The screenshot contrasts copilot and autopilot as ways of using AI. This slide paraphrases that perspective; it is not an empirical classification of people or a claim that using AI causes skill loss. Copilot here is a metaphor, not a product name. Useful automation can still run autonomously within clear boundaries; the team owns the goal, acceptance criteria, and consequential decisions. Beginners can practice this too: predict what a change should do, ask for an explanation, test it, and explain what they learned. Ask pairs: if the demo fails, can you explain what you expected and which evidence you would inspect? Then connect this habit to the spec, challenger, and repair loop.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Two jobs. One evidence trail.

<div class="three"><section><h3>Build the coach</h3><p>Use Claude Code to specify, implement, challenge, and improve it.</p></section><section><h3>Use the coach</h3><p>Find reachable people, compare alternatives, and choose an experiment.</p></section><section><h3>Build your project</h3><p>Turn the approved MVP brief into a spec your team can test.</p></section></div><div class="takeaway">You should leave knowing what to type, inspect, and save.</div>

<div class="source">Workshop walkthrough · teaching example</div>

<!--

-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Meet your go-to-market coach.

<div class="two"><div><p>Bring a hackathon idea and a recent problem.</p><p>The coach asks focused questions, separates facts from guesses, and helps you choose a small test.</p></div><div class="artifact"><label>WHAT YOU GET</label><p>Idea brief<br>Count ledger<br>Experiment card<br>MVP brief</p></div></div><div class="takeaway">It helps you decide what deserves to be built.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/README.md#L3">coach/README.md:3</a></div>

<!--

-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# What a conversation looks like.

<div class="conversation"><div class="student"><label>STUDENT · SYNTHETIC EXAMPLE</label><p>“I want to investigate study-session scheduling for my campus club.”</p></div><div class="coach"><label>COACH · RECORDED RESPONSE EXCERPTS</label><p>“Whether the chasing and the missed sessions are connected is Unknown — you observed both, not a link between them.”</p><p>“After the organizer chased answers in the chat yesterday, what happened next?”</p></div></div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/turn-01.json">docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/turn-01.json</a></div>

<!--
Read the coach aloud. Ask: what did it refuse to assume? These are exact excerpts, with intervening response text omitted. Not a fabricated live transcript.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# The outputs are usable artifacts.

<div class="four"><section><h3>Idea brief</h3><p>Club organizer; scheduling friction; current group-chat workflow.</p></section><section><h3>Count ledger</h3><p>24 roster / 8 reachable / 6 contacted / 3 problems / 6 workarounds / 2 commitments.</p></section><section><h3>Experiment card</h3><p>Two members submit availability; organizer posts a time.</p></section><section><h3>MVP brief</h3><p>Submission link + manual compile step. Team chooses Proceed.</p></section></div><div class="takeaway">Synthetic worked example. The proposed experiment has not run.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/examples/study-session.md">coach/examples/study-session.md</a></div>

<!--
Open the locally bundled worked example if the audience wants detail. The MVP here may be a manual service; do not imply that an app is required.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Build it in six visible steps.

<div class="build-strip">Brief → Spec → Approve → Implement → Challenge → Repair</div><div class="three"><section><h3>Input</h3><p>A behavior brief: who the coach helps and what it must do.</p></section><section><h3>Files</h3><p>A spec, prompt, output templates, and test scenarios.</p></section><section><h3>Evidence</h3><p>Actual responses compared with each requirement.</p></section></div>

<div class="source">Workshop walkthrough · teaching example</div>

<!--
Walk through the real repository artifacts. Prompts on the next slides are a reproducible teaching walkthrough, not a transcript of the historical build.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Claude Code is the builder.

<div class="two"><section><h3>Building session</h3><p>Reads project files, proposes changes, edits the implementation, and runs checks.</p><p>You review scope and the diff.</p></section><section><h3>Coaching session</h3><p>Uses the finished prompt to ask about your market and experiment.</p><p>You supply evidence and choose the next step.</p></section></div>

<div class="source"><a href="https://code.claude.com/docs/en/how-claude-code-works">Claude Code: how it works</a> · <a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/README.md">coach/README.md</a></div>

<!--
Keep these in separate conversations so implementation context does not become a student answer.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Open the project. Start Claude.

<div class="terminal"><div class="terminal-label">Terminal · in your project folder</div><pre>claude</pre></div><div class="terminal"><div class="terminal-label">Type in Claude Code</div><pre>Read the project files and explain what is here.
Identify the coach prompt, specification, templates, and tests.
Do not edit anything yet.</pre></div><div class="takeaway">Check that Claude is looking at the right folder.</div>

<div class="source"><a href="https://code.claude.com/docs/en/quickstart">Claude Code quickstart</a> · walkthrough/CLAUDE-CODE-STEPS.md:5</div>

<!--
Show the terminal alongside VS Code. Use provided API access in the prepared terminal; never display the key.
-->

---
class: content checkpoint
---

<div class="slide-number">Hackhers</div>

# Checkpoint 1: Claude is ready.

<div class="exercise-time">3 MINUTES · PAIRS · ONE WORKING LAPTOP</div>
<div class="two"><div><h3>Do this</h3><p>Open a terminal in your downloaded or cloned workshop repository.</p><div class="terminal"><div class="terminal-label">Run each command in the terminal</div><pre>claude --version
claude</pre></div><p>Use the organizer’s API access setup.</p></div><div><h3>Then ask Claude</h3><div class="terminal"><pre>Read coach/PROMPT.md.
Quote one rule about evidence.
Do not edit any files.</pre></div><p>Find that same sentence in the file yourself.</p></div></div><div class="takeaway">Done: show a version, a response, and the matching rule to your partner.</div>
<p class="checkpoint-help">Stuck? Ask a facilitator about installation or access; pair with a working laptop.</p>

<div class="source"><a href="https://code.claude.com/docs/en/quickstart">Claude Code quickstart / installation</a> · coach/PROMPT.md · Authored checkpoint</div>

<!--
Pause for three minutes. The facilitator checks a version number, a successful model response, and a manually matched source sentence; installation alone does not establish working access. Have students open the downloaded or cloned repository root, not an empty folder. If installation is missing, use the linked official quickstart with a facilitator. If authentication or credits fail, follow the organizer’s setup and never project keys. Pair blocked students with a working laptop so they can still inspect the file and check the answer. Ask each pair to signal ready or needs help before continuing. Fast finishers locate a second rule and explain the failure it prevents.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Start with a behavior brief.

<div class="artifact"><label>BUILD-BRIEF.md · WALKTHROUGH INPUT</label><p>Help student teams turn an idea into a testable opportunity.</p><ul><li>Ask about a recent problem and people they can reach.</li><li>Separate supplied evidence, hypotheses, and Unknowns.</li><li>Require sources for alternative claims.</li><li>Produce four outputs and at most three MVP features.</li><li>Let the student choose Proceed, Narrow, Investigate, or Pivot.</li></ul></div>

<div class="source">walkthrough/BUILD-BRIEF.md:1 · <a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/PROMPT.md#L116">coach/PROMPT.md:116</a></div>

<!--

-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Ask for a spec before code.

<div class="terminal"><div class="terminal-label">Type in Claude Code</div><pre>Read BUILD-BRIEF.md. Draft SPEC.md with numbered,
observable requirements, exclusions, and acceptance cases.
Ask about consequential gaps. Do not implement yet.</pre></div><div class="two"><p><b>Weak:</b> “Be a helpful business coach.”</p><p><b>Testable:</b> “Never turn praise into a purchase commitment.”</p></div>

<div class="source">walkthrough/CLAUDE-CODE-STEPS.md:12 · <a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/docs/AGENT-SPEC.md#L23">docs/AGENT-SPEC.md:23</a></div>

<!--
In a fresh demo folder, copy walkthrough/BUILD-BRIEF.md there first. Show a prepared spec if a live response is slow.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Review and approve the contract.

<div class="artifact"><label>REVIEW THE SPEC</label><p>Who is the student helping?<br>What must the coach ask and produce?<br>What must it never invent?<br>Which input would expose a failure?</p></div><div class="terminal"><div class="terminal-label">Type in Claude Code</div><pre>Approved: implement only the requirements in SPEC.md.
First list the files you will change and the checks you will run.
Leave unrelated files alone.</pre></div>

<div class="source">walkthrough/CLAUDE-CODE-STEPS.md:17</div>

<!--
Have a student identify one missing acceptance case before approval. A prompt approval is a workflow instruction, not an OS security boundary.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Watch the files take shape.

<div class="two"><div class="artifact"><label>ACTUAL REPOSITORY</label><pre>docs/AGENT-SPEC.md
coach/
  PROMPT.md
  templates/
    idea-brief.md
    count-ledger.md
    experiment-card.md
    mvp-brief.md
  eval/evaluation-cases.md</pre></div><div><h3>Inspect what changed</h3><p>The prompt defines behavior.</p><p>The templates make the outputs reusable.</p><p>The cases challenge the requirements.</p></div></div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/README.md">coach/README.md</a></div>

<!--
Open each real file. Do not run the implementation prompt over this completed repository; use a separate demo directory.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Read the instruction that matters.

<div class="artifact"><label>coach/PROMPT.md · EXACT EXCERPT</label><blockquote>Never invent contacts, quotes, counts, research, approval, or results. Unknown is a useful value; it does not mean zero. Never strengthen the student’s account.</blockquote></div><div class="takeaway">Now design an input that tempts it to break this rule.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/PROMPT.md#L16">coach/PROMPT.md:16</a></div>

<!--
Quote typography uses a curly apostrophe for presentation; wording is otherwise the source instruction.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Test behavior, not just the file.

<div class="test-grid"><section><label>INPUT</label><p>“Everyone on campus needs it.”</p><p>“Three friends said it is cool.”</p><p>“Invent competitor links for my pitch.”</p></section><section><label>WHAT YOU LOOK FOR</label><p>Names a reachable group to investigate.</p><p>Separates praise from commitment.</p><p>Refuses fabricated research.</p></section></div><div class="takeaway">Use a fresh coaching conversation for each independent case.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/eval/evaluation-cases.md">coach/eval/evaluation-cases.md</a></div>

<!--
These are shortened teaching challenges, not verbatim historical test inputs. Run one live and compare the full response with all applicable rules.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Give the challenger the evidence.

<div class="terminal"><div class="terminal-label">Type in Claude Code</div><pre>Review SPEC.md, the coach prompt, and the saved test responses.
For each applicable requirement, quote the exact response text.
Mark pass, fail, or unresolved. Explain unsupported claims.
Do not assume the builder’s summary is correct.</pre></div><div class="takeaway">Keep the reviewer in a separate session. Inspect its judgment too.</div>

<div class="source">walkthrough/CLAUDE-CODE-STEPS.md:31</div>

<!--
Explain adversarial review here, with a visible response. Separate sessions organize context; they do not guarantee independence or accuracy.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Repair one failure. Test again.

<div class="two"><div class="artifact"><label>FAILURE TO CATCH · TEACHING EXAMPLE</label><p>Student: “Three people liked it.”</p><p>Coach: “You have three customers.”</p></div><div><h3>Small repair</h3><p>Preserve praise as praise. Ask what action, if any, each person committed to.</p><h3>Recheck</h3><p>Repeat that case, then check a case that previously passed.</p></div></div>

<div class="source">walkthrough/CLAUDE-CODE-STEPS.md:37 · <a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/PROMPT.md#L14">coach/PROMPT.md:14</a></div>

<!--
This illustrates a failure mode; do not present it as a quoted response from the retained evaluation.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Build demo: show the whole loop.

<div class="four"><section><h3>Spec</h3><p>Point to one numbered requirement.</p></section><section><h3>Implementation</h3><p>Show the prompt rule that addresses it.</p></section><section><h3>Test</h3><p>Run one adversarial input; save the actual answer.</p></section><section><h3>Decision</h3><p>Compare, repair if needed, and explain the evidence.</p></section></div><div class="takeaway">Your partner must be able to follow the same trail.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/PROMPT.md">coach/PROMPT.md</a> · <a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/eval/evaluation-cases.md">coach/eval/evaluation-cases.md</a></div>

<!--
Allocate about 4 minutes here; reserve another 4 minutes for Checkpoint 2. Use the existing files and a prepared response if runtime is slow. Say when a response is recorded.
-->

---
class: content checkpoint
---

<div class="slide-number">Hackhers</div>

# Checkpoint 2: prove one behavior.

<div class="exercise-time">4 MINUTES · SWAP DRIVER AND CHALLENGER</div>
<div class="terminal"><div class="terminal-label">In a fresh Claude Code conversation</div><pre>Read coach/PROMPT.md and act as that coach. Do not edit files.
Synthetic practice: five friends said it sounds cool.
I want to build a study-group app. What should I do next?</pre></div>
<div class="two"><section><h3>Driver · run and save</h3><p>Save the exact input and full answer. Keep this practice scenario labeled synthetic.</p></section><section><h3>Challenger · inspect</h3><p>Did it turn praise into customers? Quote the response and compare it with the coach rule.</p></section></div><div class="takeaway">Done: show your input, response, and pass / fail / unresolved decision with a reason.</div>
<p class="checkpoint-help">No access? Inspect the <a href="./coach/examples/study-session.md" target="_blank">recorded example</a> for an unsupported inference; label it recorded.</p>

<div class="source">coach/eval/evaluation-cases.md · coach/PROMPT.md · Authored checkpoint</div>

<!--
Pause for four minutes inside the Build it time budget. Students use the completed repository coach in a fresh session, not their unfinished demo files. Review this one behavior; a pass here is not a full coach evaluation. If the answer fails, describe a minimal repair and the input you would repeat rather than overwriting the shared example during this checkpoint. For the offline fallback, inspect a quoted response in the linked recorded example, cite its evidence boundary, and use the same pass/fail/unresolved format. Do not claim that the fallback ran the live praise test. Ask two pairs to share differing judgments and the exact text supporting them. Fast finishers propose one harder input.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Behind the scenes: fewer moving parts.

<div class="two"><section><h3>DRY</h3><p><strong>Don’t Repeat Yourself.</strong></p><p>Give each rule one authoritative home so copies do not drift.</p><p>Example: reuse one availability-validation rule wherever submissions enter.</p></section><section><h3>Convention over configuration</h3><p>Use agreed defaults for names and structure; configure exceptions.</p><p>Example: follow the framework’s folder layout so it can discover files automatically.</p></section></div><div class="takeaway">Ask the builder: “What can we reuse? Which defaults already fit?”</div>

<div class="source"><a href="https://pragprog.com/tips/">The Pragmatic Programmer: DRY</a> · <a href="https://guides.rubyonrails.org/getting_started.html">Rails: conventions</a> · Authored project examples</div>

<!--
Budget about one minute per engineering slide. These are design lenses for the team’s eventual software, not claims that the prompt-only coach implements a database or object model. DRY concerns duplicated knowledge: similar-looking code need not represent the same rule. Avoid inventing an abstraction before the shared responsibility is clear. Convention over configuration means tools understand defaults; merely agreeing on names is not automatic discovery.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# SOLID: make change manageable.

<div class="artifact"><p><strong>S — Single Responsibility:</strong> one reason to change per module.</p><p><strong>O — Open/Closed:</strong> support extensions without changing stable code.</p><p><strong>L — Liskov Substitution:</strong> replacements honor the original contract.</p><p><strong>I — Interface Segregation:</strong> expose only what each client needs.</p><p><strong>D — Dependency Inversion:</strong> depend on abstractions, not concrete details.</p></div><div class="takeaway">Example: separate availability rules from storage and notifications.</div>

<div class="source"><a href="https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html">Robert C. Martin: SOLID relevance</a> · Authored project example</div>

<!--
SOLID groups five design principles. Single responsibility groups things that change for the same reason. For the scheduling example, changing how messages are sent should not change availability rules. A replacement storage adapter must preserve the caller’s expectations, including failures. A reader should not need a write interface. Keep abstractions proportionate to the project; five principles do not require five classes or a large architecture.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# ACID: protect a database transaction.

<div class="four"><section><h3>A — Atomicity</h3><p>All changes in the transaction succeed together, or none take effect.</p></section><section><h3>C — Consistency</h3><p>A successful transaction preserves defined data rules and constraints.</p></section><section><h3>I — Isolation</h3><p>Concurrent transactions interact according to the isolation level.</p></section><section><h3>D — Durability</h3><p>Committed changes survive failures under the database’s guarantees.</p></section></div><div class="takeaway">Example: reserve a seat and update capacity in one transaction.</div>

<div class="source"><a href="https://www.ibm.com/docs/en/iis/11.7.0?topic=transactions-transaction-properties">IBM: transaction properties</a> · Authored project example</div>

<!--
The booking example extends beyond the manual MVP. If the second database write fails, atomicity prevents a partial booking. Define capacity constraints and choose concurrency control appropriate to the reservation rule; a transaction alone does not prevent every race. Serializable isolation aims for results equivalent to a serial order; weaker levels permit some anomalies. Consistency means preserving defined invariants, not proving user-entered facts true. An external email is not automatically part of a database transaction. ACID describes database behavior, not a guarantee made by a prompt.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Big O: what happens as input grows?

<p><strong>Big O is notation, not an acronym.</strong> It gives an asymptotic upper bound on how time or memory grows with input size <strong>n</strong>.</p>
<div class="three"><section><h3>O(1) · constant</h3><p>Read one array item by index.</p><p>Work stays bounded as the array grows.</p></section><section><h3>O(n) · linear</h3><p>Scan every submission once.</p><p>10× the entries → about 10× the checks.</p></section><section><h3>O(n²) · quadratic</h3><p>Compare every pair of submissions.</p><p>10× the entries → about 100× the pairs.</p></section></div><div class="takeaway">Ask: “What grows with the data?” Then measure realistic inputs.</div>

<div class="source"><a href="https://www.cs.cmu.edu/~mgormley/courses/ml-primer/bigO.html">Carnegie Mellon: Big-O</a> · Authored operation-count examples</div>

<!--
Assume fixed-cost indexed reads, per-entry checks, and pair comparisons. The growth multipliers describe operation counts for these examples, not guaranteed wall-clock time. Big O ignores constant factors and lower-order terms for sufficiently large input. It is an upper bound, not automatically a tight bound or a synonym for worst case. Database indexes, network calls, and model calls require their own cost analysis. Measure before optimizing a tiny hackathon workload.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Start using the finished coach.

<div class="two"><section><h3>Claude Code · API access</h3><p>Start a separate conversation in the repository. Ask Claude to read <code>coach/PROMPT.md</code> and act as that coach.</p><p>“Do not edit files or build yet. Help me investigate my idea.”</p></section><section><h3>Claude chat · your account</h3><p>Copy the entire <a href="./coach/PROMPT.md" target="_blank">coach prompt</a> into a fresh conversation, then describe your idea.</p><p>Use whichever chat access your account provides.</p></section></div><div class="takeaway">Keep coaching and coding conversations separate.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/README.md#L7">coach/README.md:7</a> · walkthrough/USE-THE-COACH.md:1</div>

<!--
API credits fund API usage; do not promise they include a Claude chat subscription. In Claude Code, this is a coaching instruction; do not claim it mechanically disables tools.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Give it a real starting point.

<div class="terminal"><div class="terminal-label">FIRST COACH MESSAGE · FILL IN YOUR OWN FACTS</div><pre>Act as the coach in coach/PROMPT.md.
My idea is ____. The person I want to help is ____.
The last time I observed this problem was ____.
They currently handle it by ____.
Before judging, I can reach ____.
Help me decide what to investigate first.</pre></div><div class="takeaway">If you do not know, say “Unknown.”</div>

<div class="source">walkthrough/USE-THE-COACH.md:8</div>

<!--
Give pairs two minutes to write this before speaking to the coach. Avoid invented users or made-up interviews.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Count people you can actually reach.

<div class="counts"><div><b>24</b><span>Roster</span></div><div><b>8</b><span>Reachable</span></div><div><b>6</b><span>Contacted</span></div><div><b>3</b><span>Problem reports</span></div><div><b>6</b><span>Workarounds</span></div><div><b>2</b><span>Commitments</span></div></div><p>These are different counts. They are not a conversion funnel.</p><div class="takeaway">Synthetic example: real fieldwork counts remain Unknown.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/examples/study-session.md#L67">coach/examples/study-session.md:67</a></div>

<!--
Ask whether the two committed people must be among the three problem reporters. Answer: overlap is Unknown. Teams keep their own denominators.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Find alternatives. Bring sources.

<div class="two"><section><h3>Ask the coach</h3><p>“What do people do today? Which alternatives should we investigate? What would make switching worth the effort?”</p></section><section><h3>Supply evidence</h3><p>URL + relevant excerpt + access date.</p><p>Explain exactly which claim the source supports.</p></section></div><div class="takeaway">A group chat, spreadsheet, or doing nothing may be the current alternative.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/PROMPT.md#L138">coach/PROMPT.md:138</a></div>

<!--
If source browsing is unavailable, students paste excerpts. A competitor feature page does not establish demand for their idea.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Turn an idea into an experiment.

<div class="artifact"><label>SYNTHETIC EXPERIMENT CARD · RECORDED OUTPUT SUMMARY</label><p><b>People:</b> two members who committed to a test.</p><p><b>Action:</b> submit availability through a link; organizer posts one shared time.</p><p><b>Threshold:</b> both submit in five minutes, no reminders; shared time posted within ten minutes.</p><p><b>If it fails:</b> investigate and narrow before adding features.</p></div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/examples/study-session.md#L89">coach/examples/study-session.md:89</a></div>

<!--
This is a proposed test; result remains Not run. Ask which observation exercises each feature.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# You choose the next move.

<div class="three"><section><h3>Proceed</h3><p>Enough evidence for the next bounded experiment.</p></section><section><h3>Narrow / investigate</h3><p>Focus the audience or answer the most consequential unknown.</p></section><section><h3>Pivot</h3><p>Change the problem or approach when evidence warrants it.</p></section></div><div class="takeaway">Tell the coach your decision and why. Ask it to record your reasoning.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/PROMPT.md#L116">coach/PROMPT.md:116</a></div>

<!--
No automated approval. Proceed does not mean proven product-market fit or permission to build every feature.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Save four outputs for your team.

<div class="four"><section><h3>Idea brief</h3><p>Who, problem, alternatives, evidence.</p></section><section><h3>Count ledger</h3><p>What each number represents.</p></section><section><h3>Experiment card</h3><p>Action, threshold, result, next decision.</p></section><section><h3>MVP brief</h3><p>At most three features; what you defer.</p></section></div><div class="terminal"><div class="terminal-label">ASK THE COACH</div><pre>Draft all four outputs from what I supplied.
Keep Unknowns and source attribution. Do not invent missing facts.</pre></div>

<div class="source">walkthrough/USE-THE-COACH.md:19 · <a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/templates/idea-brief.md">coach/templates/idea-brief.md</a></div>

<!--
Pairs save outputs into their project docs folder. Use the linked local template pack; names can follow their team convention.
-->

---
class: content checkpoint
---

<div class="slide-number">Hackhers</div>

# Checkpoint 3: your handoff is ready.

<div class="exercise-time">4 MINUTES · PAIRS · SAVE BEFORE YOU BUILD</div>
<div class="two"><section><h3>Driver · save the work</h3><p>Save all four coach outputs in your project. Keep missing facts marked Unknown.</p><p>Record your choice: Proceed, Narrow, Investigate, or Pivot, and why.</p></section><section><h3>Partner · show the evidence</h3><p>Open the saved outputs. Point to a person, a problem, and one testable action.</p><p>Identify a success threshold, a source or Unknown, and at most three MVP features.</p></section></div><div class="takeaway">Done: your partner can find the files and explain the next experiment without asking you.</div>
<p class="checkpoint-help">Missing evidence? Save the Unknown and the next question. You can choose Investigate.</p>

<div class="source">walkthrough/USE-THE-COACH.md · coach/templates/ · Authored checkpoint</div>

<!--
Pause for four minutes within Use it. This checks a usable handoff, not proof of demand or a requirement to choose Proceed. Have the partner open the files, rather than accept a verbal “saved.” The count ledger is the fourth output even though the next build prompt reads only three documents. Students with no working model can fill the four linked templates manually from their own facts; preserve Unknowns and label synthetic practice. Fast finishers write one acceptance case for the proposed experiment. Bring an unresolved Unknown into the next spec instead of asking the model to fill it in.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Hand the MVP to Claude Code.

<div class="terminal"><div class="terminal-label">Type in Claude Code</div><pre>Read docs/idea-brief.md, docs/experiment-card.md,
and docs/mvp-brief.md. Draft docs/PROJECT-SPEC.md.
For each feature, include an observable acceptance test.
Preserve exclusions and Unknowns. Propose the smallest
implementation plan. Do not build until I approve.</pre></div><div class="takeaway">The coach informs scope. Your team approves the build contract.</div>

<div class="source">walkthrough/HACKATHON-PLAYBOOK.md:5</div>

<!--

-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Build the smallest useful slice.

<div class="two"><div class="artifact"><label>EXAMPLE PROJECT SPEC</label><p>One availability-submission flow.</p><p>A manual organizer view.</p><p>No accounts, calendar sync, or automatic reminders yet.</p></div><div><h3>In Claude Code</h3><p>Approve one slice. Inspect changed files. Run its acceptance test.</p><p>Ask for a review against the spec before expanding scope.</p></div></div>

<div class="source">walkthrough/HACKATHON-PLAYBOOK.md:14 · <a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/examples/study-session.md#L107">coach/examples/study-session.md:107</a></div>

<!--
The recorded MVP includes a manual workflow. Only turn it into software if the team explicitly chooses that implementation and can justify it.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Pitch the evidence, not the hype.

<div class="four"><section><h3>Problem</h3><p>Who experienced what, and how you know.</p></section><section><h3>Alternatives</h3><p>What people do today; cited comparison.</p></section><section><h3>Demo</h3><p>The small workflow you actually built.</p></section><section><h3>Learning</h3><p>Test result, limits, and your next decision.</p></section></div><div class="takeaway">Link each important claim to a source, response, test, or observation.</div>

<div class="source">walkthrough/HACKATHON-PLAYBOOK.md:22</div>

<!--
This is where works cited becomes useful to their pitch. Do not turn synthetic counts into customer claims.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Where do BMAD and gstack fit?

<div class="three"><section><h3>BMAD</h3><p>Structured planning and delivery with product, architecture, development, and testing perspectives.</p></section><section><h3>gstack</h3><p>Specialist workflows for planning, code review, browser testing, and shipping.</p></section><section><h3>Today’s scope</h3><p>Practice the underlying decisions directly in Claude Code before adding workflow setup.</p></section></div><div class="takeaway">These tools can guide the work. Your project still needs explicit rules, design choices, and tests.</div>

<div class="source"><a href="https://github.com/bmad-code-org/BMAD-METHOD">BMAD: official repository</a> · <a href="https://github.com/garrytan/gstack">gstack: official repository</a> · Workshop scope: teaching choice</div>

<!--
Neither is required for this workshop. This is a time-and-focus choice, not a verdict on quality or a claim that either lacks engineering practices. Both offer substantial planning and review support. What remains for any project is domain context: which rule is authoritative, which contract a replacement must preserve, which writes belong in a transaction, and what workload to measure. DRY, SOLID, ACID, Big O, and conventions help students assess the proposed answers. The same responsibility applies when using Nightshift or a plain coding session. Adopt a workflow when its structure helps the team; installation itself is not evidence of correctness.
-->

---
class: content checkpoint
---

<div class="slide-number">Hackhers</div>

# Checkpoint 4: show one working slice.

<div class="exercise-time">6 MINUTES · PAIRS · USE YOUR APPROVED SCOPE</div>
<div class="two"><section><h3>Driver · build and run</h3><p>Choose one acceptance case from your approved project spec.</p><p>Ask Claude Code to implement the smallest slice and run the check. Inspect the changes.</p></section><section><h3>Challenger · try it</h3><p>Exercise the workflow yourself. Compare the expected result with what actually happens.</p><p>Record pass, fail, or unresolved. Swap roles for the next check.</p></section></div><div class="takeaway">Done: show one workflow, its expected and actual result, and your next decision.</div>
<p class="checkpoint-help">Not ready to code? Run the approved manual experiment, or write the missing acceptance case first.</p>

<div class="source">walkthrough/HACKATHON-PLAYBOOK.md · Authored checkpoint</div>

<!--
Keep this bounded to six minutes. The team must approve the scope before implementation. A failing check is useful evidence; do not hide it to claim completion. If the plan is still unresolved, write one concrete input and expected result, label execution Not run, and choose the next action. This fallback is planning progress, not a working-slice pass. A manual MVP can be exercised manually; explain which observation tests the feature. Ask one pair to show a failure and what they would change, and another to show a passing result with its limits.
-->

---
class: closing
---

<div class="slide-number">Hackhers</div>

# Leave with a next step you can defend.

<div class="exit"><p>Who can your team reach?</p><p>What will you test before adding features?</p><p>Which spec requirement will Claude Code build first?</p><p>What evidence would change your mind?</p></div><div class="tagline">Use the coach to investigate. Use the spec to build. Use evidence to decide.</div>

<div class="source">Workshop walkthrough · teaching example</div>

<!--

-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Your hackathon kit.

<div class="two"><section><h3>Use the coach</h3><p><a href="./coach/PROMPT.md" target="_blank">Open the full coaching prompt ↗</a></p><p><a href="./coach/templates/idea-brief.md" target="_blank">Idea brief</a> · <a href="./coach/templates/count-ledger.md" target="_blank">Count ledger</a></p><p><a href="./coach/templates/experiment-card.md" target="_blank">Experiment card</a> · <a href="./coach/templates/mvp-brief.md" target="_blank">MVP brief</a></p></section><section><h3>Build with the workflow</h3><p><a href="./walkthrough/CLAUDE-CODE-STEPS.md" target="_blank">Claude Code build steps ↗</a></p><p><a href="./walkthrough/HACKATHON-PLAYBOOK.md" target="_blank">Team playbook ↗</a></p><p><a href="https://github.com/doctor-ew/hackhers-2026" target="_blank">Workshop repository ↗</a></p></section></div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/handoff/coach-completion-20260909/coach/README.md">coach/README.md</a></div>

<!--
These links are bundled with the presentation for local use. A localhost URL on the projector is not accessible from a student laptop; distribute the repository or exported files.
-->
