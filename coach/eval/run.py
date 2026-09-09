#!/usr/bin/env python3
"""Run synthetic coach cases or a real conversation turn; never self-grade.

CLI contract: https://code.claude.com/docs/en/cli-reference
Each output directory is append-only. Conversation uses Claude's actual session
resume, not invented assistant history. No API billing fallback is allowed.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import uuid

ROOT = Path(__file__).resolve().parents[2]
PROMPT = ROOT / "coach/PROMPT.md"
DEFAULT_CASES = ROOT / "docs/spec-fa7abd1282236c13/eval-inputs.json"


def encode(value):
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def environment():
    result = os.environ.copy()
    for name in (
        "OPENAI_API_KEY", "CODEX_API_KEY", "ANTHROPIC_API_KEY",
        "ANTHROPIC_AUTH_TOKEN", "OPENAI_BASE_URL", "ANTHROPIC_BASE_URL",
        "CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX",
        "CLAUDE_CODE_USE_FOUNDRY",
    ):
        result.pop(name, None)
    return result


def write_new(path, value):
    with path.open("x") as stream:
        stream.write(encode(value))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("cases", "turn"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--ids", nargs="+")
    parser.add_argument("--model", default=os.environ.get("COACH_EVAL_MODEL") or "opus",
                        help="Claude model (default: COACH_EVAL_MODEL or opus)")
    parser.add_argument("--message-file", type=Path)
    parser.add_argument("--web-case", action="store_true",
                        help="Allow only WebFetch/WebSearch for case 04")
    args = parser.parse_args()
    if not args.model.strip():
        parser.error("Choose a nonempty Claude model")
    env = environment()
    auth = subprocess.run(["claude", "auth", "status", "--json"], env=env,
                          text=True, capture_output=True, timeout=30)
    identity = json.loads(auth.stdout)
    if auth.returncode or not identity.get("loggedIn") or identity.get("authMethod") != "claude.ai" or identity.get("apiProvider") != "firstParty":
        parser.error("Claude subscription sign-in required; API fallback disabled")
    version = subprocess.check_output(["claude", "--version"], env=env, text=True).strip()
    prompt_hash = hashlib.sha256(PROMPT.read_bytes()).hexdigest()
    args.output.mkdir(parents=True, exist_ok=True)

    def call(label, message, *, web=False, session=None, resume=False):
        destination = args.output / (label + ".json")
        if destination.exists():
            raise RuntimeError("Evidence already exists: " + str(destination))
        if hashlib.sha256(PROMPT.read_bytes()).hexdigest() != prompt_hash:
            raise RuntimeError("Prompt changed during evaluation")
        command = ["claude", "-p", "--output-format", "json", "--safe-mode",
                   "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
                   "--tools", "WebFetch,WebSearch" if web else "",
                   "--permission-mode", "dontAsk", "--max-turns", "8",
                   "--system-prompt-file", str(PROMPT)]
        if args.model:
            command += ["--model", args.model]
        if web:
            command += ["--allowedTools", "WebFetch,WebSearch"]
        if session:
            command += ["--resume" if resume else "--session-id", session]
        else:
            command += ["--no-session-persistence"]
        command += ["--", message]
        record = dict(id=label, started_at=datetime.now(timezone.utc).isoformat(),
                      runtime="Claude Code", cli_version=version, auth="subscription",
                      selected_model=args.model,
                      prompt_sha256=prompt_hash, input=message,
                      tools="WebFetch,WebSearch" if web else "none",
                      judgment="PENDING_INDEPENDENT_REVIEW")
        try:
            proc = subprocess.run(command, cwd=ROOT, env=env, text=True,
                                  capture_output=True, timeout=300)
            raw = json.loads(proc.stdout) if proc.stdout.strip() else {}
            record.update(exit_code=proc.returncode, is_error=raw.get("is_error"),
                          subtype=raw.get("subtype"), output=raw.get("result", ""),
                          models=list(raw.get("modelUsage", {})),
                          permission_denials=raw.get("permission_denials", []),
                          errors=raw.get("errors", []), stderr=proc.stderr[:1500])
        except (subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
            record.update(transport_error=type(exc).__name__, exit_code=1, output="")
        record["prompt_unchanged"] = hashlib.sha256(PROMPT.read_bytes()).hexdigest() == prompt_hash
        write_new(destination, record)
        good = record.get("exit_code") == 0 and not record.get("is_error") and bool(record.get("output")) and record["prompt_unchanged"]
        print(label, "response recorded" if good else "transport failed", flush=True)
        return record, good

    if args.mode == "cases":
        cases = json.loads(args.cases.read_text())
        if args.ids:
            cases = [case for case in cases if case["id"] in args.ids]
            if {case["id"] for case in cases} != set(args.ids):
                parser.error("Unknown case id")
        if not cases or len({case['id'] for case in cases}) != len(cases):
            parser.error("Cases must be nonempty and unique")
        with ThreadPoolExecutor(max_workers=3) as pool:
            results = list(pool.map(lambda case: call("case-" + case["id"], case["prompt"],
                                web=args.web_case and case["id"] == "04"), cases))
        return 0 if all(good for _, good in results) else 1

    if not args.message_file:
        parser.error("turn requires --message-file")
    message = args.message_file.read_text()
    if not message.strip():
        parser.error("Empty turn")
    history = sorted(args.output.glob("turn-*.json"))
    for previous in history:
        record = json.loads(previous.read_text())
        if record.get("prompt_sha256") != prompt_hash or not record.get("prompt_unchanged") or record.get("exit_code") or record.get("is_error") or not record.get("output"):
            parser.error("Prior turn is stale or failed; preserve it and use a fresh conversation directory")
    session_file = args.output / "session.json"
    if session_file.exists():
        session = json.loads(session_file.read_text())["id"]
    else:
        session = str(uuid.uuid4())
        write_new(session_file, {"id": session, "prompt_sha256": prompt_hash})
    record, good = call("turn-%02d" % (len(history) + 1), message,
                        session=session, resume=bool(history))
    if good:
        print(record["output"])
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
