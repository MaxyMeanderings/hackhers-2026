# Stage 1 — the smallest prompt that could plausibly work

A first draft, deliberately thin. It covers job and input from Stage 0; it
leaves out tools, boundaries, and output on purpose.

```
You are a coach for hackathon ideas. Ask the student about their idea, ask
about competitors, and tell them whether it's a good idea.
```

That's it — three sentences. It is a complete, syntactically fine prompt, and
it is missing everything that made the shipped coach pass its cases.

## Run it

```sh
claude --model opus --system-prompt-file workshop/build-track/prompt-v1.txt
```

(Save the block above as `workshop/build-track/prompt-v1.txt` first, or paste
it as your first chat message instead of using `--system-prompt-file`.)

Then say:

> There are no competitors. My idea is a form for a student club to collect
> study-session availability.

## What to watch for

This is the real Case 04 prompt from
[`coach/eval/evaluation-cases.md:43`](../../coach/eval/evaluation-cases.md).
With the thin prompt, watch for the assistant naming specific competing
products or pricing with no source attached — because nothing in the prompt
told it that a claim without a URL isn't allowed. This is not hypothetical:
the shipped coach's *own* earlier draft failed this exact way. The recorded
outcome:

> "Case 04 failed citation support: the response attributed mobile apps to a
> page describing mobile browser access; its Forms pricing claim was also
> unsupported by the cited page."
> — [`coach/eval/RESULTS.md:117`](../../coach/eval/RESULTS.md)

That's the teaching moment for this stage: the failure is fluent and
confident, not sloppy-sounding. Reading the response is not enough to catch
it — you have to check the claim against the source, which is why Stage 2
puts the rule in the prompt instead of trusting a second read-through.

Next: [`02-add-guardrail.md`](02-add-guardrail.md).
