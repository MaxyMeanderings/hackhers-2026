"""Verify saved live evidence integrity after independent behavior review."""
from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parents[2]
d=Path(__file__).resolve().parent
spec=(d/"SPEC.md").read_text()
files=re.findall(r"^\| `([^`]+)` \|",spec,re.M)
assert len(files)==9 and len(set(files))==9
for f in files: assert (root/f).is_file(), f"Missing deliverable: {f}"
expected=hashlib.sha256((root/"coach/PROMPT.md").read_bytes()).hexdigest()
review=json.loads((d/"LIVE-REVIEW.json").read_text())
assert review["verdict"]=="PASS", "Independent behavioral review has unresolved failures"
assert len(review["cases"])==10 and all(c["verdict"]=="PASS" for c in review["cases"])
for i in range(1,11):
    r=json.loads((d/(f"live-case-{i:02d}.json")).read_text())
    assert r["prompt_sha256"]==expected, f"Stale prompt evidence {i}"
    assert r["exit_code"]==0 and r["is_error"] is False and r["output"].strip(), f"Missing live response {i}"
turns=sorted(d.glob("conversation-turn-*.json"))
assert len(turns)>=4, "Full multi-turn scenario missing"
for f in turns:
    r=json.loads(f.read_text()); assert r["prompt_sha256"]==expected and r["exit_code"]==0 and not r["is_error"] and r["output"]
assert review["conversation_verdict"]=="PASS", "Full conversation has not passed independent review"
assert review["citation_inspection"]=="PASS", "Research citation inspection missing"
assert (d/"citation-inspection.md").is_file()
assert hashlib.sha256((root/"docs/AGENT-SPEC.md").read_bytes()).hexdigest()==json.loads((d/"source.json").read_text())["source_revision"], "Approved input changed"
print(f"PASS: 9 scoped files, 10 live cases, {len(turns)} conversation turns, independent grading, citation inspection, unchanged source")
