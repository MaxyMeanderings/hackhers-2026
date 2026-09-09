# Independent static prompt review

Date: 2026-09-09

Reviewed prompt: `coach/PROMPT.md`

SHA-256: `c2963707f980882c9b51ae21f52457c72b6de562471f35a40900304d1936a70c`

Authority: `docs/AGENT-SPEC.md` and `docs/coach-completion-20260909/SPEC.md`.
The four files in `coach/templates/` were also inspected to assess output coverage.
This review is static. No live transcript, private heldout fixture, or runtime
process arguments were inspected. No behavior pass or completion claim follows
from this review. Implementation files were not edited.

## Findings

### R1 — Medium: immediate advice rules conflict with opening discovery

`coach/PROMPT.md:15` requires discovering the idea and its origin before advice.
However, `coach/PROMPT.md:41` requires addressing situations in the current reply,
and `coach/PROMPT.md:48` requires proposing a group and discovery action while
`coach/PROMPT.md:51` requires proposing features and an experiment immediately.
There is no opening exception for these advice requirements.

When a first message supplies many features or cannot name a user but omits what
prompted the idea, these instructions compete. Asking about the origin and
proposing an experiment in that same reply does not establish the missing origin
before advice. This risks acceptance criterion 1 in
`docs/coach-completion-20260909/SPEC.md:27` and the discovery requirement in
`docs/AGENT-SPEC.md:21`.

Recommended resolution: explicitly give missing opening discovery precedence
over provisional advice; resume the situation-specific advice once the student
has supplied that context. Validate an opening with missing origin and a
feature-heavy proposal, and an opening with missing origin and no named user.
This is an instruction conflict, not an observed execution failure.

### R2 — Medium: embedded output structures do not cover all template fields

`coach/PROMPT.md:128` instructs the model to populate four embedded structures and
says they mirror the template files. A student pasting only this prompt does not
receive all fields present in those files:

- `coach/templates/mvp-brief.md:17` includes each feature's role in the experiment;
  `coach/templates/mvp-brief.md:34` includes deferred features and why they were
  cut. Neither has a corresponding embedded output field.
- `coach/templates/mvp-brief.md:40` records an anonymous approver, date, and a
  four-way decision. `coach/PROMPT.md:179` instead supplies an explicit yes/no
  approval field. The general instruction to retain the decision helps but does
  not resolve this structural mismatch for narrow, investigate, or pivot.
- `coach/templates/experiment-card.md:7` includes evidence mode and result.
  The embedded experiment card at `coach/PROMPT.md:164` omits both. Surrounding
  prompt instructions add labels and result for roleplay specifically, leaving
  the ordinary fieldwork output without the same explicit coverage.

This limits confidence in full template population under acceptance criterion 9
in `docs/coach-completion-20260909/SPEC.md:35`. Recommended resolution: align the
embedded field list with the actual templates, using Unknown for missing
approver/date and preserving all four decision choices. Keep unused feature
slots omitted or deferred. Confirm complete outputs in both synthetic and
ordinary fieldwork sessions. This is a static coverage finding; the model may
add these fields voluntarily, but that behavior has not been established here.

## Static coverage

The prompt explicitly addresses a single question block with at most five
focused items, evidence/unknown recaps, all six count categories, anonymous
participants, source attribution, claim-adjacent URLs, vendor claims, tool
limitations, source instruction distrust, at most three features, one experiment,
pre-test thresholds, and preservation of student-selected scope and decisions.
The six inquiry stages are present. Synthetic counts remain separate from real
fieldwork counts, and synthetic results remain labeled.

These are instruction-presence findings only. Live opening behavior, pacing,
question counts, source accuracy, evidence retention, full output completeness,
and the ten required cases still need execution and independent semantic review.
Tool-free CLI evidence cannot establish live browsing or Claude chat parity, as
recorded in `docs/coach-completion-20260909/SPEC.md:46`.

## Independent re-review of the first revision

Reviewed SHA-256:
`f8e30ff6bd06b694e8eed242d0fd350cd425e98043481681f68b9dd444975927`.
The original findings above remain historical findings against the earlier hash.

R2 is resolved at the instruction level. The revised embedded structures include
evidence mode, participant details when supplied, experiment result, per-feature
role and acceptance criteria, deferred features and reasons, anonymous approver,
date, and the four decision choices with pending support. Actual output coverage
still requires live semantic review.

R1 is partially resolved. `coach/PROMPT.md:18` now explicitly places the missing
opening question before advice and gives this order precedence. This addresses
the narrow question-before-advice wording of completion acceptance criterion 1.
However, `coach/PROMPT.md:20` expressly permits provisional advice in that same
reply before the missing answer is available. The upstream requirement to
discover what the student knows before advice in `docs/AGENT-SPEC.md:21` remains
in tension with that permission. Recommended resolution remains to defer
provisional advice until the missing opening context has been answered. This
residual issue is static; no live opening has been reviewed here.

## Independent re-review of the second revision

Reviewed SHA-256:
`68a1eb9dc122706c5b42a28d8bf549aeed89dac7035d629c2744c05f77743dc2`.
The complete revised prompt was read. Earlier findings and dispositions above
remain historical records against their respective hashes.

R1 is resolved at the instruction level. The opening now requires waiting for
the missing idea or origin answer before substantive solution or feature advice,
and expressly gives that rule precedence over immediate situation responses.
Its limited allowance for helping an uncertain student select a tentative group
and plan one evidence-gathering action supports discovery itself. This is a
reasonable reconciliation with the required no-identifiable-user behavior in
`docs/AGENT-SPEC.md:101`; it does not authorize premature feature recommendations.
Live review should check that proposed groups remain tentative and that this
allowance does not expand into product or feature advice before opening answers.

R2 remains resolved at the instruction level; the expanded template fields are
retained. No further actionable static findings were identified in this revision.
The prompt is ready to freeze for the required execution and independent
semantic review. This disposition is not a behavior pass, proof-gate result,
citation inspection result, or completion claim.

## Static review of the first behavioral repair

Reviewed SHA-256:
`ab44aa52391de41224ce0caf4bd9dcfacc63473b8ea3b7dc54bc5f6fa7286f2c`.

The revised response discipline directly addresses the observed case 04, 08,
and 10 failures: atomic requests, no prose requests, a whole-reply request count,
explicit separation of observed difficulty from inferred cause, preservation of
synthetic account type, and no inferred direct-contact count from a report.
These are appropriate instruction repairs; their effectiveness is unverified.

A remaining priority collision needs resolution before execution: the new
three-piece ceiling coexists with the immediate broad-claim instruction to ask
for bounded group, reachable number, and recent evidence. Missing opening origin
adds another request. Explicitly prioritize and defer a lower-priority request,
or permit up to five atomic requests, rather than requiring all four within
three items. The original external workshop limit is five; this conflict is
introduced by the stricter internal response rule.

## Static follow-up on the behavioral repair

Reviewed SHA-256:
`f010bad03d56d762410cbbaae09ce1a31b8cf1572a32d811b603498a4c376d17`.

The broad-claim request collision is resolved for the supplied-idea openings
under review. The prompt allocates one item to the recent problem, if any, that
prompted the idea; one to a bounded group; and one to the reachable number.
It explicitly defers evidence type and event details and prohibits a duplicate
origin request. The combined origin/problem item concerns one triggering event
rather than multiple independently answerable facts.

The added instructions also prohibit deriving student identity or circumstances
from workspace metadata and embedding unsupported causes or workarounds in
questions. No additional blocking static finding is identified for this repair.
Proceed to the authorized execution gate and supplemental evaluation; all
earlier failed outcomes remain failures and behavioral effectiveness remains
unverified until new outputs are reviewed.
