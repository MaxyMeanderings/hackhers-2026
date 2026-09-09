# Public feature literal and exact-interface audit

Date: 2026-09-09

Decision: the retained response fails the sealed exact interface, but its sole value difference is feature-label capitalization. That difference does not establish a material product failure such as changing the selected feature, inventing evidence, or losing the experiment decision. The request underspecifies the required case-sensitive feature label.

## Evidence and observed difference

Reviewed `development-76664c9aebae48248a7248d7a693331a.json`, all public prototype assertions in `behavior-scenarios.json`, and the public product requirements. The inspected scenario file SHA-256 is `662cd7642d92300ad7b7679e4d5e3abae53904d65eda72f90b633237701476a2`.

The actual object has the exact required keys. All values and JSON types except the feature-label text match the oracle. The selected array contains `Reminders`; the oracle requires `reminders`. Both name the single feature selected by the student. The request identifies that feature in prose and asks for `features (array)`; it does not specify a case-sensitive string literal for the array element. By contrast, it explicitly supplies the fixed strings for action, metric, result, feature basis and real interviews.

The runtime correctly returned FAIL under its typed, case-sensitive equality. Preserve that failure, its seal and all consumed counters. This audit does not authorize regrading, case-folding the oracle, accepting arbitrary aliases or editing retained evidence.

## Review of the full public exact interface

| Requirement | Assessment |
| --- | --- |
| Final evidence object keys | Explicitly requested, with no additional keys |
| Final evidence counts | Supplied quantities and zero commitments are unambiguous; the request calls their types numbers |
| Real-interview sentinel | Both current evidence requests explicitly require the exact `Unknown` string, including the no-real-interviews condition |
| Demand booleans | Boolean type is explicit; unsupported demand or expressly unproven demand supports false |
| Source-status value | The request supplies the verified/unverified vocabulary; the unsupported claim and unavailable research support unverified |
| Intermediate experiment result | Literal `not run` is supplied in the request |
| Final experiment keys and fixed action/metric/result/basis/sentinel strings | Explicitly requested; the retained actual response matches them |
| Final experiment selected feature | Correct feature identity is supplied, but the exact case-sensitive array element is not specified |
| Final experiment participant and threshold counts | Both quantities are supplied; the request calls their types numbers |
| Aggregate final-case assertions | Agree with their corresponding final-turn objects |
| Array presence and size limits | Explicit in the current intermediate requests; semantic quality still requires independent review |

Two additional serialization constraints should be clarified before another challenge if the current oracles are retained unchanged:

1. Count equality distinguishes integers from floating-point representations, while the requests say number. Explicitly request integer JSON literals for cardinality fields if forms such as `5.0` must fail despite denoting the same quantity.
2. The question check searches raw completion text for a literal question-mark character. A valid JSON escaped representation could contain a question mark after parsing without the raw glyph. Explicitly request literal question-mark punctuation if this serialization distinction is intentional.

The public evidence prohibition also rejects every secure-URL marker, although the request says not to research rather than expressly banning all URL text. Requesting a source URL is permitted fallback behavior under the product specification. Likewise, raw name-fragment/initial prohibitions can match ordinary wording or an unrelated anonymous label. These are stricter output-text contracts than simply omitting the supplied person's identity. If these existing prohibitions remain unchanged, make their exact excluded text and no-URL requirement explicit in the public request. This avoids treating an unstated byte-level restriction as a demonstrated coaching error. No prohibition was changed during this audit.

## Prospective clarification

The smallest repair for the observed mismatch is to request `features` as exactly the one-element array `["reminders"]`, including lowercase spelling. Retain the exact oracle. Clarify the remaining integer, punctuation and excluded-text requirements together rather than discovering them through additional model calls. Preserve prior failures and obtain independent review and the supported new lock/challenge/seal before execution under the clarified contract.

These clarifications describe the intended interface; they do not supply new market evidence, alter selected facts or waive independent product-semantic review. No private fixtures, private expectations, provider calls, source edits or oracle changes were used in this audit.
