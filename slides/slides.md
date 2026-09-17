---
theme: default
title: Build with AI. Own the evidence.
info: Build your own go-to-market coach from a brief and specification with Claude Code.
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

# Build a coach.<br>Own how it behaves.

<div class="cover-mark"><img src="/assets/claude-logo.svg" alt="Claude" /></div><div class="hero-sub">A build brief → your spec → your coach.<br>Implement it. Test it. Explain what you changed.</div><div class="tagline">Claude Code · go-to-market discovery · human judgment</div><div class="sponsor-note">API credits provided by Anthropic</div>

<div class="source">Workshop walkthrough · teaching example</div>

<!--
The workshop deliverable is each team’s own coach prompt, templates, test cases, and evidence. The supplied coach illustrates the target. Using it for a hackathon idea is optional follow-on material.
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

<div class="intro-linkedin"><a href="https://www.linkedin.com/in/tyler-sztuka-283937123/" target="_blank" rel="noopener noreferrer"><img src="/assets/qr-tyler.png" alt="QR code: Tyler on LinkedIn" /><span>Connect with Tyler<br />on LinkedIn ↗</span></a><a href="https://www.linkedin.com/in/andrew-schillinger/" target="_blank" rel="noopener noreferrer"><img src="/assets/qr-drew.png" alt="QR code: Drew on LinkedIn" /><span>Connect with Drew<br />on LinkedIn ↗</span></a></div>


<div class="source"><a href="https://szdlabs.io/">Tyler: SZD Labs</a> · <a href="https://www.linkedin.com/in/tyler-sztuka-283937123/" target="_blank" rel="noopener noreferrer">Tyler: LinkedIn</a> · <a href="https://sessionize.com/drew-schillinger/">Drew: speaker profile</a> · <a href="https://www.linkedin.com/in/andrew-schillinger/" target="_blank" rel="noopener noreferrer">Drew: LinkedIn</a></div>

<!--

-->

---
class: content access-slide
---

<div class="slide-number">Hackhers</div>

# Open the workshop.

<WorkshopLinks />

<div class="source">Scan a QR code or click its link. Keep the slides and repository handy.</div>

---
class: content
---

<div class="slide-number">Hackhers</div>

# Claim your $50 in API credits.

<div class="credits"><div><p class="amount">$50</p><p>Anthropic is covering your Claude Code API usage today.</p><ol><li>Scan the code. Sign in to the Claude Console (console.anthropic.com) or create an account.</li><li>Submit your Console <b>Organization ID</b>, not a Claude.ai user ID. A user ID is rejected.</li><li>Wait a couple of minutes, then sign in to Claude Code with that account.</li></ol></div><a class="qr" href="https://platform.claude.com/offers/2239eaf0-dbc5-49ed-b6b7-1f1fe14ea78e" target="_blank" rel="noopener noreferrer" aria-label="Open the Anthropic API credits offer in a new tab"><img src="/assets/api-credits-qr.png" alt="QR code linking to the Anthropic API credits offer" /><span>Scan, or click to open ↗</span></a></div><div class="takeaway">Do this first. One claim each. API only: Claude Code, not the Claude.ai app. The link expires; the date is on the page.</div>

<div class="source">Anthropic API credits offer · organizer’s QR code · sponsorship wording per the organizer</div>

<!--
Have every pair scan now, before the copilot slide. Credits are issued within a couple of minutes of a valid claim; there is no overnight wait. The common failure is pasting a Claude.ai user ID instead of the Console Organization ID, which the system rejects; they can resubmit with the right ID. Each person can claim once, so they should be signed in to the Console account they will use in Claude Code. Credits cover API usage only, not claude.ai subscriptions. Never project an API key.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Apply for credits. Two minutes.

<img class="shot" src="/assets/api-credits-form.png" alt="Anthropic API credits application page with the apply-for-credits form" /><p class="shot-caption">Sign in, paste your Console <b>Organization ID</b>, submit. Find it in the Console under Settings → Organization. Credits cover the Claude API only, not Claude.ai, and each person can claim once.</p>

<div class="source">Screenshot: Anthropic API credits application page, organizer’s account · fields shown are the organizer’s, not a template</div>

<!--
Walk through the form once on the projector. This screenshot is from an earlier offer page; replace it with this event’s page before presenting. Show where the Organization ID lives in the Console so nobody pastes a Claude.ai user ID, and point out the link expiration date on the page.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Your credits live in the Claude Console.

<img class="shot" src="/assets/claude-console-dashboard.png" alt="Claude Console dashboard showing organization credits, monthly spend, and available models" /><p class="shot-caption">Claude Console dashboard · <b>Organization credits</b> is the balance Claude Code draws from. It updates a couple of minutes after a valid claim. You do not need to create an API key today.</p>

<div class="source">Screenshot: Claude Console dashboard, organizer’s account, July 2026 · balances shown are the organizer’s</div>

<!--
Point at Organization credits and Spend this month. Everything else on this page is optional for the workshop. A student who still sees a zero balance after a few minutes most likely submitted a Claude.ai user ID; have them resubmit with the Console Organization ID. Meanwhile pair them with a working laptop and keep going.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Sign in to Claude Code with those credits.

<div class="two"><div class="terminal"><div class="terminal-label">Terminal · then inside Claude Code</div><pre>claude
/login</pre></div><div><p>Choose <b>2. Anthropic Console account · API usage billing</b>.</p><p>Your browser opens. Sign in with the account that holds the credits, then return to the terminal.</p></div></div><img class="shot shot-short" src="/assets/claude-code-login.png" alt="Claude Code login prompt with Anthropic Console account selected" />

<div class="source">Screenshot: Claude Code /login prompt, organizer’s terminal · <a href="https://code.claude.com/docs/en/quickstart">Claude Code quickstart</a></div>

<!--
Option 1 uses a personal claude.ai subscription and will not draw on the sponsored credits. Option 2 is the one for today. A student already signed in with a subscription can run /login again to switch. This is the access check that checkpoint 1 relies on: a real response, not a version number.
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

# Your build. Your evidence.

<div class="three"><section><h3>Specify your coach</h3><p>Turn the supplied build brief into observable requirements and acceptance cases.</p></section><section><h3>Implement your coach</h3><p>Use Claude Code to create the prompt, four output templates, and tests in your own folder.</p></section><section><h3>Demonstrate your coach</h3><p>Run your implementation, inspect its answers, repair failures, and explain the evidence.</p></section></div><div class="takeaway">Leave with a coach you built and a behavior you can defend.</div>

<div class="source">starter/BUILD-BRIEF.md · Workshop learning objectives</div>

<!--
Show the completed coach only to establish what students are building. Filled-in business discovery outputs are examples of the coach’s eventual use, not the primary student deliverable today.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Meet the reference coach.

<div class="two"><div><p>This completed example shows what your team will build.</p><p>The coach asks focused questions, separates facts from guesses, and helps you choose a small test.</p></div><div class="artifact"><label>WHAT YOU GET</label><p>Idea brief<br>Count ledger<br>Experiment card<br>MVP brief</p></div></div><div class="takeaway">Your task: reproduce these behaviors from the brief and your approved spec.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/README.md#L3">coach/README.md:3</a></div>

<!--

-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# What a conversation looks like.

<div class="conversation"><div class="student"><label>STUDENT · SYNTHETIC EXAMPLE</label><p>“I want to investigate study-session scheduling for my campus club.”</p></div><div class="coach"><label>COACH · RECORDED RESPONSE EXCERPTS</label><p>“Whether the chasing and the missed sessions are connected is Unknown — you observed both, not a link between them.”</p><p>“After the organizer chased answers in the chat yesterday, what happened next?”</p></div></div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/turn-01.json">docs/coach-completion-20260909/live/laptop-20260909/conversation-opus-complete-experiment/turn-01.json</a></div>

<!--
Read the coach aloud. Ask: what did it refuse to assume? These are exact excerpts, with intervening response text omitted. Not a fabricated live transcript.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# The outputs are usable artifacts.

<div class="four"><section><h3>Idea brief</h3><p>Club organizer; scheduling friction; current group-chat workflow.</p></section><section><h3>Count ledger</h3><p>24 roster / 8 reachable / 6 contacted / 3 problems / 6 workarounds / 2 commitments.</p></section><section><h3>Experiment card</h3><p>Two members submit availability; organizer posts a time.</p></section><section><h3>MVP brief</h3><p>Submission link + manual compile step. Team chooses Proceed.</p></section></div><div class="takeaway">Synthetic worked example. The proposed experiment has not run.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/examples/study-session.md">coach/examples/study-session.md</a></div>

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

<div class="source"><a href="https://code.claude.com/docs/en/how-claude-code-works">Claude Code: how it works</a> · <a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/README.md">coach/README.md</a></div>

<!--
Keep these in separate conversations so implementation context does not become a student answer.
-->

---
class: content interface-slide
---

<div class="slide-number">Hackhers</div>

# Claude Code in your terminal.

<div><a class="interface-image" href="./assets/claude-terminal.png" target="_blank" rel="noopener noreferrer"><img src="/assets/claude-terminal.png" alt="Claude Code running in a terminal with a custom coding buddy" /><span>Open full-size screenshot ↗</span></a></div>
<p class="interface-caption">Work in your own starter folder. Type a request, inspect the files, and review the result. The dragon is a custom plugin; it is optional.</p>

<div class="source">Organizer-supplied screenshot · interface and account shown are Drew’s</div>


---
class: content interface-slide
---

<div class="slide-number">Hackhers</div>

# Claude Code in the desktop app.

<div><a class="interface-image" href="./assets/claude-desktop.png" target="_blank" rel="noopener noreferrer"><img src="/assets/claude-desktop.png" alt="Claude desktop app showing its Code workspace" /><span>Open full-size screenshot ↗</span></a></div>
<p class="interface-caption">This screenshot shows the Code workspace in the desktop app. The same brief → spec → build → test workflow guides your work.</p>

<div class="source">Organizer-supplied screenshot · interface and account shown are Drew’s</div>


---
class: content
---

<div class="slide-number">Hackhers</div>

# Open the project. Start Claude.

<div class="terminal"><div class="terminal-label">Terminal · in your project folder</div><pre>claude</pre></div><div class="terminal"><div class="terminal-label">Type in Claude Code</div><pre>Read BUILD-BRIEF.md and explain what we will build.
Identify the deliverables and questions to resolve.
Do not implement yet.</pre></div><div class="takeaway">Check that Claude is looking at the right folder.</div>

<div class="source"><a href="https://code.claude.com/docs/en/quickstart">Claude Code quickstart</a> · starter/BUILD-STEPS.md</div>

<!--
Show the terminal alongside VS Code in a fresh build folder containing BUILD-BRIEF.md. The next checkpoint has students prepare their own folder. Use the organizer’s API access; never display the key.
-->

---
class: content checkpoint
---

<div class="slide-number">Hackhers</div>

# Checkpoint 1: your build folder is ready.

<div class="exercise-time">5 MINUTES · PAIRS · START YOUR OWN COACH</div>
<div class="two"><div><h3>Prepare your workspace</h3><p>Download and extract the <a href="./hackhers-starter.zip">student starter ZIP</a>. Open its folder in your editor and terminal.</p><div class="terminal"><div class="terminal-label">Terminal · in that folder</div><pre>claude --version
claude</pre></div></div><div><h3>Ask your builder</h3><div class="terminal"><pre>Read BUILD-BRIEF.md.
Summarize what we must build.
List questions before implementation.
Do not build yet.</pre></div><p>Check the answer against the brief.</p></div></div><div class="takeaway">Done: your own folder, the brief, working Claude access, and an accurate scope summary.</div>
<p class="checkpoint-help">Stuck on setup? Use the organizer’s access instructions or pair on a working laptop.</p>

<div class="source">starter/BUILD-BRIEF.md · starter/BUILD-STEPS.md · Authored build checkpoint</div>

<!--
Students build their own conversational coach prompt and supporting files. Extract the starter ZIP into a separate workspace. It contains only the README, build brief, build steps, and ignore rules. Keep the completed reference checkout outside this folder. Do not copy the completed repository coach as the implementation. A successful response confirms model access; a version number alone does not. Keep credentials private. A blocked pair can review the brief together, but mark model access unresolved until a real response succeeds.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Start with a behavior brief.

<div class="artifact"><label>BUILD-BRIEF.md · WALKTHROUGH INPUT</label><p>Help student teams turn an idea into a testable opportunity.</p><ul><li>Ask about a recent problem and people they can reach.</li><li>Separate supplied evidence, hypotheses, and Unknowns.</li><li>Require sources for alternative claims.</li><li>Produce four outputs and at most three MVP features.</li><li>Let the student choose Proceed, Narrow, Investigate, or Pivot.</li></ul></div>

<div class="source">starter/BUILD-BRIEF.md:1 · <a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/PROMPT.md#L116">coach/PROMPT.md:116</a></div>

<!--

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
class: content spec-prompt
---

<div class="slide-number">Hackhers</div>

# Ask for a spec before code.

<div class="terminal"><div class="terminal-label">Type in Claude Code</div><pre>Read BUILD-BRIEF.md. Draft SPEC.md; do not implement yet.
Number requirements, exclusions, and acceptance cases.
Include DRY, SOLID, ACID, Big O, and convention over
configuration as engineering requirements where applicable.
For each: state applicability, a concrete rule, and a check.
Explain any N/A; do not add a database or app to satisfy it.
Map requirements to planned files and acceptance evidence.
Ask about consequential gaps. Wait for our approval.</pre></div><p class="checkpoint-help">Copy the full prompt from <a href="./walkthrough/CLAUDE-CODE-STEPS.md" target="_blank">Build steps → Specify ↗</a>. Keep the coach prompt and four templates in scope.</p>

<div class="source">starter/BUILD-STEPS.md · <a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/docs/AGENT-SPEC.md#L23">docs/AGENT-SPEC.md:23</a></div>

<!--
In a fresh demo folder, copy starter/BUILD-BRIEF.md there first. Show a prepared spec if a live response is slow.
-->

---
class: content checkpoint
---

<div class="slide-number">Hackhers</div>

# Checkpoint 2: your spec is testable.

<div class="exercise-time">8 MINUTES · DRAFT, CHALLENGE, APPROVE</div>
<div class="terminal"><div class="terminal-label">Ask Claude Code in your build folder</div><pre>Use the full Specify prompt in BUILD-STEPS.md.
Draft SPEC.md with behavior and engineering requirements.
Include applicability and checks. Do not implement yet.</pre></div>
<div class="two"><section><h3>Driver · inspect scope</h3><p>Check that the spec covers the brief. Identify the coach prompt, four templates, and test cases to build.</p></section><section><h3>Partner · challenge a rule</h3><p>Choose one requirement. Write an input, expected behavior, and a visible failure. Check one engineering rule or justified N/A. Resolve gaps.</p></section></div><div class="takeaway">Done: a saved spec your team can explain and explicitly approve.</div>
<p class="checkpoint-help">Too vague? Replace “be helpful” with a behavior you can observe in a response.</p>

<div class="source">starter/BUILD-BRIEF.md · starter/BUILD-STEPS.md · Authored build checkpoint</div>

<!--
Pause while every pair drafts and reviews its own SPEC.md. The partner should be able to judge an example response against the chosen acceptance case. Review the rest of the brief too; a single test does not establish complete coverage. If access is blocked, draft the same requirements manually and label that fallback. Do not approve unresolved consequential requirements just to keep pace. The next checkpoint implements the approved specification.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Review and approve the contract.

<div class="artifact"><label>REVIEW THE SPEC</label><p>Who is the student helping?<br>What must the coach ask and produce?<br>What must it never invent?<br>Which input would expose a failure?</p></div><div class="terminal"><div class="terminal-label">Type in Claude Code</div><pre>Approved: implement only the requirements in SPEC.md.
First list the files you will change and the checks you will run.
Apply the approved engineering requirements; explain each N/A.
Leave unrelated files alone.</pre></div>

<div class="source">starter/BUILD-STEPS.md</div>

<!--
Have a student identify one missing acceptance case before approval. A prompt approval is a workflow instruction, not an OS security boundary.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Watch the files take shape.

<div class="two"><div class="artifact"><label>COMPLETED REFERENCE · YOUR PATHS MAY DIFFER</label><pre>docs/AGENT-SPEC.md
coach/
  PROMPT.md
  templates/
    idea-brief.md
    count-ledger.md
    experiment-card.md
    mvp-brief.md
  eval/evaluation-cases.md</pre></div><div><h3>Inspect what changed</h3><p>The prompt defines behavior.</p><p>The templates make the outputs reusable.</p><p>The cases challenge the requirements.</p></div></div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/README.md">coach/README.md</a></div>

<!--
Show the reference files briefly, then have teams implement in their own build folders. Students should inspect the actual paths their builder creates; these reference paths are not the required student file layout.
-->

---
class: content checkpoint
---

<div class="slide-number">Hackhers</div>

# Checkpoint 3: build your coach.

<div class="exercise-time">12 MINUTES · IMPLEMENT YOUR APPROVED SPEC</div>
<div class="terminal"><div class="terminal-label">After your team approves SPEC.md</div><pre>Implement the approved SPEC.md in this project.
Create the coach prompt, four output templates, and test cases.
First propose file paths and checks. Stay within the spec.</pre></div>
<div class="two"><section><h3>Driver · inspect the files</h3><p>Open the prompt, templates, and cases Claude created. Check them against your spec.</p></section><section><h3>Partner · trace a rule</h3><p>Point from one requirement to its prompt instruction and acceptance case.</p></section></div><div class="takeaway">Done: your own coach files exist, and your partner can trace a requirement through them.</div>
<p class="checkpoint-help">Missing a rule or file? Ask for a focused repair before testing the coach.</p>

<div class="source">starter/BUILD-BRIEF.md · starter/BUILD-STEPS.md · Authored build checkpoint</div>

<!--
This is the student implementation step, not a demonstration of supplied repository files. Use the actual paths proposed and created in the pair’s project; the next checkpoint must load that implementation. Coach output templates are build artifacts here, distinct from filled-in coaching outputs generated during use. File existence is only this checkpoint’s structural check, not proof of correct behavior. If a team cannot finish, identify the missing artifact and mark implementation incomplete; do not substitute the reference coach and claim it as their build.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Read the instruction that matters.

<div class="artifact"><label>coach/PROMPT.md · EXACT EXCERPT</label><blockquote>Never invent contacts, quotes, counts, research, approval, or results. Unknown is a useful value; it does not mean zero. Never strengthen the student’s account.</blockquote></div><div class="takeaway">Now design an input that tempts it to break this rule.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/PROMPT.md#L16">coach/PROMPT.md:16</a></div>

<!--
Quote typography uses a curly apostrophe for presentation; wording is otherwise the source instruction.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Test behavior, not just the file.

<div class="test-grid"><section><label>INPUT</label><p>“Everyone on campus needs it.”</p><p>“Three friends said it is cool.”</p><p>“Invent competitor links for my pitch.”</p></section><section><label>WHAT YOU LOOK FOR</label><p>Names a reachable group to investigate.</p><p>Separates praise from commitment.</p><p>Refuses fabricated research.</p></section></div><div class="takeaway">Use a fresh coaching conversation for each independent case.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/eval/evaluation-cases.md">coach/eval/evaluation-cases.md</a></div>

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

<div class="source">starter/BUILD-STEPS.md</div>

<!--
Explain adversarial review here, with a visible response. Separate sessions organize context; they do not guarantee independence or accuracy.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Repair one failure. Test again.

<div class="two"><div class="artifact"><label>FAILURE TO CATCH · TEACHING EXAMPLE</label><p>Student: “Three people liked it.”</p><p>Coach: “You have three customers.”</p></div><div><h3>Small repair</h3><p>Preserve praise as praise. Ask what action, if any, each person committed to.</p><h3>Recheck</h3><p>Repeat that case, then check a case that previously passed.</p></div></div>

<div class="source">starter/BUILD-STEPS.md · <a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/PROMPT.md#L14">coach/PROMPT.md:14</a></div>

<!--
This illustrates a failure mode; do not present it as a quoted response from the retained evaluation.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Build demo: show the whole loop.

<div class="four"><section><h3>Spec</h3><p>Point to one numbered requirement.</p></section><section><h3>Implementation</h3><p>Show the prompt rule that addresses it.</p></section><section><h3>Test</h3><p>Run one adversarial input; save the actual answer.</p></section><section><h3>Decision</h3><p>Compare, repair if needed, and explain the evidence.</p></section></div><div class="takeaway">Your partner must be able to follow the same trail.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/PROMPT.md">coach/PROMPT.md</a> · <a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/eval/evaluation-cases.md">coach/eval/evaluation-cases.md</a></div>

<!--
Demonstrate the spec-to-test loop briefly, then let students run checkpoint 4 against the coach they built. Any facilitator reference response must be labeled recorded and is not evidence that a student implementation passed.
-->

---
class: content checkpoint
---

<div class="slide-number">Hackhers</div>

# Checkpoint 4: test the coach you built.

<div class="exercise-time">12 MINUTES · RUN, INSPECT, REPAIR</div>
<div class="two"><section><h3>Driver · run your implementation</h3><p>Start a fresh conversation. Load the coach prompt from your build folder and ask Claude to act as that coach.</p><p>Run an acceptance case from your spec. Save the exact input and full answer.</p></section><section><h3>Partner · judge the result</h3><p>Compare the answer with the expected behavior. Quote evidence for pass, fail, or unresolved.</p><p>If it fails, repair your prompt and rerun. Also check a case that passed before.</p></section></div><div class="takeaway">Done: demonstrate your coach and show the spec → implementation → test evidence.</div>
<p class="checkpoint-help">Not built yet? Finish checkpoint 3. Mark unexecuted cases “Not run.”</p>

<div class="source">starter/BUILD-BRIEF.md · starter/BUILD-STEPS.md · Authored build checkpoint</div>

<!--
The test target is the team’s newly built coach, not the completed prompt on reference/completed-coach. Confirm the actual loaded path with the team. For a praise-versus-commitment acceptance case, use a clearly synthetic student input and compare the generated response with the approved expectation. A passing result supports only the behaviors exercised. If the case passes immediately, run a harder case or another requirement; never manufacture a failure or repair story. For failures preserve before/after responses and explain the actual change. This checkpoint is the workshop’s principal demonstration of what students built.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Where do these workflows fit?

<div class="three"><section><h3>BMAD</h3><p>Structured planning and delivery with product, architecture, development, and testing perspectives.</p></section><section><h3>gstack</h3><p>Specialist workflows for planning, code review, browser testing, and shipping.</p></section><section><h3>Nightshift</h3><p>A staged engineering workflow for specification, implementation, review, and verification, with recorded evidence.</p><p class="workflow-screenshots"><a href="./assets/nightshift-stages.png" target="_blank" rel="noopener noreferrer">Stages: blocked at preflight ↗</a><br><a href="./assets/nightshift-evidence-usage.png" target="_blank" rel="noopener noreferrer">Evidence &amp; partial usage ↗</a></p></section></div><div class="takeaway">Today, we practice the decisions these workflows help organize: define requirements, review changes, and test the results.</div>

<div class="source"><a href="https://github.com/bmad-code-org/BMAD-METHOD">BMAD: official repository</a> · <a href="https://github.com/garrytan/gstack">gstack: official repository</a> · <a href="https://github.com/doctor-ew/nightshift-community">Nightshift: official repository</a></div>

<!--
None of these workflows is required for this workshop. Present each as a way to organize engineering work, without ranking them. Nightshift is Drew’s workflow example; its stages cover specification, implementation, review, and verification with recorded evidence. The organizer-supplied screenshots open full size. The stage screenshot shows the run blocked at preflight; earlier green stages do not establish successful deployment. The usage screenshot explicitly shows partial usage and a provider estimate, with actual billed cost unknown. Do not present these as a completed run or verified total cost. Today students practice the underlying decisions directly in Claude Code. Adopt a workflow when its structure helps the team; installation itself is not evidence of correctness.
-->

---
class: closing
---

<div class="slide-number">Hackhers</div>

# Show the coach you built.

<div class="exit"><p>Which requirement did your team implement?</p><p>Where does your coach enforce that behavior?</p><p>What input did you run, and what happened?</p><p>What did you repair—or what remains unresolved?</p></div><div class="tagline">Your spec → your implementation → your test evidence.</div>

<div class="source">Workshop walkthrough · teaching example</div>

<!--

-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Your coach-building kit.

<div class="two"><section><h3>Build your own</h3><p><a href="./hackhers-starter.zip">Download the student starter ZIP ↗</a></p><p><a href="./walkthrough/CLAUDE-CODE-STEPS.md" target="_blank">Follow the build steps ↗</a></p><p>Save your spec, coach prompt, four templates, test cases, and actual responses.</p></section><section><h3>Compare and continue</h3><p><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/PROMPT.md" target="_blank">Already-baked reference prompt ↗</a></p><p><a href="https://github.com/doctor-ew/hackhers-2026" target="_blank">Workshop repository ↗</a></p><p><a href="./walkthrough/HACKATHON-PLAYBOOK.md" target="_blank">Optional: apply your coach to a project ↗</a></p></section></div><div class="takeaway">Save your work, stay connected, and keep building.</div>

<div class="source">starter/BUILD-BRIEF.md · starter/BUILD-STEPS.md</div>

<!--
Students should show their own build artifacts before comparing with the reference branch. The starter ZIP has no completed prompt or templates. Optional slides explain how the coach’s outputs can inform another project after this workshop. Share the published URL for classroom access.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Optional: use the coach you built.

<div class="two"><section><h3>Claude Code · API access</h3><p>Start a fresh conversation in your build folder. Load your own coach prompt and ask Claude to act as that coach.</p><p>“Do not edit files or build yet. Help me investigate my idea.”</p></section><section><h3>Claude chat · your account</h3><p>Copy your complete coach prompt into a fresh chat. The <a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/PROMPT.md" target="_blank">reference prompt</a> is available for comparison.</p><p>Use whichever chat access your account provides.</p></section></div><div class="takeaway">Keep coaching and coding conversations separate.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/README.md#L7">coach/README.md:7</a> · walkthrough/USE-THE-COACH.md:1</div>

<!--
API credits fund API usage; do not promise they include a Claude chat subscription. In Claude Code, this is a coaching instruction; do not claim it mechanically disables tools.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Give it a real starting point.

<div class="terminal"><div class="terminal-label">FIRST COACH MESSAGE · FILL IN YOUR OWN FACTS</div><pre>Act as the coach in the prompt I supplied.
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

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/examples/study-session.md#L67">coach/examples/study-session.md:67</a></div>

<!--
Ask whether the two committed people must be among the three problem reporters. Answer: overlap is Unknown. Teams keep their own denominators.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Find alternatives. Bring sources.

<div class="two"><section><h3>Ask the coach</h3><p>“What do people do today? Which alternatives should we investigate? What would make switching worth the effort?”</p></section><section><h3>Supply evidence</h3><p>URL + relevant excerpt + access date.</p><p>Explain exactly which claim the source supports.</p></section></div><div class="takeaway">A group chat, spreadsheet, or doing nothing may be the current alternative.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/PROMPT.md#L138">coach/PROMPT.md:138</a></div>

<!--
If source browsing is unavailable, students paste excerpts. A competitor feature page does not establish demand for their idea.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# Turn an idea into an experiment.

<div class="artifact"><label>SYNTHETIC EXPERIMENT CARD · RECORDED OUTPUT SUMMARY</label><p><b>People:</b> two members who committed to a test.</p><p><b>Action:</b> submit availability through a link; organizer posts one shared time.</p><p><b>Threshold:</b> both submit in five minutes, no reminders; shared time posted within ten minutes.</p><p><b>If it fails:</b> investigate and narrow before adding features.</p></div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/examples/study-session.md#L89">coach/examples/study-session.md:89</a></div>

<!--
This is a proposed test; result remains Not run. Ask which observation exercises each feature.
-->

---
class: content
---

<div class="slide-number">Hackhers</div>

# You choose the next move.

<div class="three"><section><h3>Proceed</h3><p>Enough evidence for the next bounded experiment.</p></section><section><h3>Narrow / investigate</h3><p>Focus the audience or answer the most consequential unknown.</p></section><section><h3>Pivot</h3><p>Change the problem or approach when evidence warrants it.</p></section></div><div class="takeaway">Tell the coach your decision and why. Ask it to record your reasoning.</div>

<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/PROMPT.md#L116">coach/PROMPT.md:116</a></div>

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

<div class="source">walkthrough/USE-THE-COACH.md:19 · <a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/templates/idea-brief.md">coach/templates/idea-brief.md</a></div>

<!--
Pairs save outputs into their project docs folder. Use the linked local template pack; names can follow their team convention.
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

<div class="source">walkthrough/HACKATHON-PLAYBOOK.md:14 · <a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/examples/study-session.md#L107">coach/examples/study-session.md:107</a></div>

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
class: content access-slide
---

<div class="slide-number">Hackhers</div>

# Stay connected.

<SpeakerLinks />

<div class="source">Thanks for building with us. Share what you tried, learned, and changed.</div>

---
class: content access-slide
---

<div class="slide-number">Hackhers</div>

# Keep building. Take the links.

<WorkshopLinks />

<div class="source">Slides, starter, and source. Scan or click to return anytime.</div>
