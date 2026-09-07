# Nightshift terminal failure receipt

Status: failed. Ticket: spec:docs/AGENT-SPEC.md. Local bead: hht-90k.
Branch: nightshift/spec-fa7abd1282236c13.
Worktree: /Users/doctorew/shuttlebay/_ATL_/GSU/Hack-Her-Thon-worktrees/spec-fa7abd1282236c13.
Publication: withheld; no push, PR, merge, or deployment performed by this run.

## Failed gate and evidence

Mandatory live Claude evaluation failed after the initial run and three smallest-scope behavioral repairs. Final verdict: 8 PASS, 2 FAIL, all ten responses tied to the same prompt hash. Source construction passed independently but cannot override actual behavior.

- Case 04: unsupported cited claims (Doodle mobile apps; Forms free pricing). See LIVE-REVIEW.md citation inspection and live-case-04.json.
- Case 08: three-feature subset proposed without an actual linked experiment. See live-case-08.json and source requirement docs/AGENT-SPEC.md:102.
- Full coaching conversation stopped after two actual final-hash turns; four deliverables and human approval remain unverified. Claude chat live parity remains unverified.

## Commands and output

Executed `python3 docs/spec-fa7abd1282236c13/live-eval.py` for complete suites; the harness records command inputs, actual output, runtime, timestamps and hashes. Each of the ten final commands exited 0; semantic review still failed. Runtime is Claude Code subscription; key/provider override variables removed in the harness. Case 04 enables WebFetch/WebSearch; other cases disable tools. CLI transport parsing was repaired with an explicit positional `--` separator without changing fixtures.

Executed `python3 docs/spec-fa7abd1282236c13/coaching-turn.py` twice on the final prompt, with explicitly synthetic inputs. Actual responses are conversation-turn-01.json and conversation-turn-02.json.

Independent native Codex review: LIVE-CASES.json, LIVE-REVIEW.md, REVIEW-native.md. No second Codex process was launched.

## Repair history

1. Adaptive opening and synthetic provenance repair by Claude; accompanying source documentation corrections by orchestrator. Evidence retained in attempt1/ and attempt2/.
2. Immediate source-required coaching priorities and unknown real-count handling, in PROMPT.md. Subsequent output retained in attempt3/.
3. Front-loaded existing requirements for numerical reach, discovery, counting, feature scope and anonymization. Final hash below. Fixtures and acceptance criteria were not relaxed. No fourth repair attempted.

## Next operator action

Begin a separately authorized follow-up focused on claim-to-citation checking and concrete experiment linkage for feature scoping. Preserve the locked fixtures, rerun affected cases after repair, then all ten cases and the complete four-deliverable conversation on one prompt version. Require independent evidence approval before source commit/push/PR. No later independent tickets were supplied in this batch.

## Retained changes

Seven coach prompt/adapter/template/README files plus evaluation results are unverified source retained locally. Engineering spec and RED fixtures were sealed in local bot commits. Reports, transcripts, harnesses and tracker remain in this isolated worktree. Caller checkout preserved.

Prompt SHA256: 8ae1c4bd8f24fd8ecdf1ead6f1a808c163143490e76af711162f80baf3a83083

```text
 A .nightshift/spec-fa7abd1282236c13.md
 A coach/CLAUDE-CODE-ADAPTER.md
 A coach/PROMPT.md
 A coach/README.md
 A coach/templates/count-ledger.md
 A coach/templates/experiment-card.md
 A coach/templates/idea-brief.md
 A coach/templates/mvp-brief.md
?? .nightshift/.active-scope-spec-fa7abd1282236c13
?? .nightshift/.checkout-lease/
?? .nightshift/.claim-cache.jsonl
?? .nightshift/agents/
?? .nightshift/spec-fa7abd1282236c13-citations-trim.jsonl
?? .nightshift/spec-fa7abd1282236c13-citations.attempt1.jsonl
?? .nightshift/spec-fa7abd1282236c13-citations.jsonl
?? .nightshift/spec-fa7abd1282236c13.locks
?? coach/eval/RESULTS.md
?? docs/spec-fa7abd1282236c13/.bd-id
?? docs/spec-fa7abd1282236c13/ADVERSARIAL.attempt1.md
?? docs/spec-fa7abd1282236c13/ADVERSARIAL.md
?? docs/spec-fa7abd1282236c13/LIVE-CASES-attempt3.json
?? docs/spec-fa7abd1282236c13/LIVE-CASES.json
?? docs/spec-fa7abd1282236c13/LIVE-REVIEW-attempt1.md
?? docs/spec-fa7abd1282236c13/LIVE-REVIEW-attempt3.md
?? docs/spec-fa7abd1282236c13/LIVE-REVIEW.md
?? docs/spec-fa7abd1282236c13/RED.log
?? docs/spec-fa7abd1282236c13/REVIEW-native-attempt1.md
?? docs/spec-fa7abd1282236c13/REVIEW-native.md
?? docs/spec-fa7abd1282236c13/SPEC-DIGEST.md
?? docs/spec-fa7abd1282236c13/adversarial-native.attempt1.out.json
?? docs/spec-fa7abd1282236c13/adversarial-native.out.json
?? docs/spec-fa7abd1282236c13/attempt1/
?? docs/spec-fa7abd1282236c13/attempt2/
?? docs/spec-fa7abd1282236c13/attempt3/
?? docs/spec-fa7abd1282236c13/citation-inspection.md
?? docs/spec-fa7abd1282236c13/cli-help.txt
?? docs/spec-fa7abd1282236c13/coaching-turn.py
?? docs/spec-fa7abd1282236c13/conversation-state.json
?? docs/spec-fa7abd1282236c13/conversation-turn-01.json
?? docs/spec-fa7abd1282236c13/conversation-turn-02.json
?? docs/spec-fa7abd1282236c13/eval-inputs.json
?? docs/spec-fa7abd1282236c13/implementation-repair.in.md
?? docs/spec-fa7abd1282236c13/implementation-repair.out.json
?? docs/spec-fa7abd1282236c13/implementation.in.md
?? docs/spec-fa7abd1282236c13/implementation.out.json
?? docs/spec-fa7abd1282236c13/live-case-01.json
?? docs/spec-fa7abd1282236c13/live-case-02.json
?? docs/spec-fa7abd1282236c13/live-case-03.json
?? docs/spec-fa7abd1282236c13/live-case-04.json
?? docs/spec-fa7abd1282236c13/live-case-05.json
?? docs/spec-fa7abd1282236c13/live-case-06.json
?? docs/spec-fa7abd1282236c13/live-case-07.json
?? docs/spec-fa7abd1282236c13/live-case-08.json
?? docs/spec-fa7abd1282236c13/live-case-09.json
?? docs/spec-fa7abd1282236c13/live-case-10.json
?? docs/spec-fa7abd1282236c13/live-eval.py
?? docs/spec-fa7abd1282236c13/product-extractor.in.md
?? docs/spec-fa7abd1282236c13/product-extractor.out.json
?? docs/spec-fa7abd1282236c13/runtime-access.json
?? docs/spec-fa7abd1282236c13/source.json
?? docs/spec-fa7abd1282236c13/spec-author-provider.txt
?? docs/spec-fa7abd1282236c13/spec-repair.in.md
?? docs/spec-fa7abd1282236c13/spec-repair.out.json
?? docs/spec-fa7abd1282236c13/spec-writer.in.md
?? docs/spec-fa7abd1282236c13/spec-writer.out.json
?? docs/spec-fa7abd1282236c13/verify-evidence.py
```
