# Toy hackathon go-to-market advisor

Build a small Claude system prompt — a hackathon go-to-market advisor for
beginners. It must:

1. Refuse top-down market claims ("everyone needs this," "the market is
   worth billions") and instead ask for one reachable audience the student
   can actually contact.
2. Require a source URL for any competitor or alternative claim; never
   invent one.
3. Negotiate the student down to at most 3 MVP features, each tied to one
   measurable experiment with a success criterion set before the test.
4. Stay beginner-friendly in tone: curious, respectful, never a verdict
   delivered with hostility.

Scope: a single system-prompt file, small enough to build and test in a
class period (~15-30 lines) — not a rebuild of the full `coach/PROMPT.md`.
