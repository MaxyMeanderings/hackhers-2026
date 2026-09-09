# Independent complete-experiment repair draft review

Date: 2026-09-09

Initial draft: `/private/tmp/coach-complete-experiment-repair.md`, SHA-256 `dfdf086ef5b80ea9f0058614d1689dd98769214bc232d4520acc6291f69efcd6`.

Decision: **REQUEST ONE NARROW STATIC CLARIFICATION** before approval.

The additions distinguish feature availability from observed effectiveness, require a response to a failed proposed experiment, and treat an absent eligible event as inconclusive. These are generic product requirements directly supported by the public findings in `PUBLIC-DEVELOPMENT-BOUNDARIES-REVIEW.md`. They do not depend on private evidence and do not change existing counts, source rules, question limits or output templates.

The structured-output sentence assumes every schema has a free-text threshold string. Some requested schemas can instead use numeric thresholds or exact literals. Instructing the model to insert prose there could collide with the existing exact-key/type/literal requirement. Limit this instruction to an available free-text threshold or plan field, expressly preserving requested keys/types/literals and distinguishing new experiment proposals from exact summaries of already selected plans. The current public new-experiment request already provides a free-text threshold field, so the clarification still addresses its missing response without an oracle-specific exception.

No source was edited and no model call was made by this reviewer. Static approval, once this conflict is resolved, will not prove execution success; all applicable actual gates remain required with prior failures and cumulative accounting preserved.

## Revised draft approval

Current draft SHA-256: `682f62a154591cd6bb5331d00222a7b16ededa656e7d132ae643996f86bc6927`.

Decision: **APPROVE for the authorized repair and evaluation**. The revised sentence limits failure-response insertion to an available free-text threshold or plan field, preserves requested keys/types/literals, and explicitly distinguishes new experiment proposals from exact summaries of selected plans. The identified static conflict is resolved. The diff contains only the reviewed effectiveness, complete-experiment and inconclusive-observation additions. No new conflict with the original product criteria was found. The original draft review and public failures remain preserved; no runtime behavior is claimed from static inspection.
