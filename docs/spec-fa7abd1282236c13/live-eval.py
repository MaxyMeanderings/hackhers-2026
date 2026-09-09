"""Execute synthetic coach evaluations with subscription Claude Code; never grade itself.
CLI reference: https://code.claude.com/docs/en/cli-reference
Local flag evidence: cli-help.txt. Inputs: eval-inputs.json and coach/eval/evaluation-cases.md.
"""
import concurrent.futures, datetime, hashlib, json, os, pathlib, subprocess, sys
ROOT=pathlib.Path(__file__).resolve().parents[2]
EVIDENCE=pathlib.Path(__file__).resolve().parent
ENV=os.environ.copy()
for key in ("OPENAI_API_KEY","CODEX_API_KEY","ANTHROPIC_API_KEY","ANTHROPIC_AUTH_TOKEN","OPENAI_BASE_URL","ANTHROPIC_BASE_URL","CLAUDE_CODE_USE_BEDROCK","CLAUDE_CODE_USE_VERTEX","CLAUDE_CODE_USE_FOUNDRY"):
    ENV.pop(key,None)
def run_one(case):
    prompt=ROOT/"coach/PROMPT.md"
    assert prompt.is_file(), "canonical prompt missing"
    web=case["id"]=="04"
    cmd=["claude","-p","--output-format","json","--safe-mode","--strict-mcp-config","--mcp-config",'{"mcpServers":{}}',"--tools","WebFetch,WebSearch" if web else "","--permission-mode","dontAsk","--max-turns","8","--no-session-persistence","--system-prompt-file",str(prompt)]
    if web: cmd += ["--allowedTools","WebFetch,WebSearch"]
    cmd += ["--",case["prompt"]]
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        proc=subprocess.run(cmd,cwd=ROOT,env=ENV,text=True,capture_output=True,timeout=240)
        raw=json.loads(proc.stdout) if proc.stdout.strip() else {}
        result={"id":case["id"],"started_at":started,"runtime":"Claude Code","auth":"subscription; API credentials/provider overrides removed","prompt_sha256":hashlib.sha256(prompt.read_bytes()).hexdigest(),"input":case["prompt"],"tools":"WebFetch,WebSearch" if web else "none","exit_code":proc.returncode,"is_error":raw.get("is_error"),"subtype":raw.get("subtype"),"output":raw.get("result",""),"models":list(raw.get("modelUsage",{})),"permission_denials":raw.get("permission_denials",[]),"errors":raw.get("errors",[]),"stderr":proc.stderr[:1500],"judgment":"PENDING_INDEPENDENT_REVIEW"}
    except Exception as exc:
        result={"id":case["id"],"started_at":started,"transport_error":str(exc),"judgment":"FAIL"}
    (EVIDENCE/("live-case-"+case["id"]+".json")).write_text(json.dumps(result,indent=2)+"\n")
    print(case["id"],result.get("subtype",result.get("transport_error")),flush=True)
    return result
if __name__=="__main__":
    cases=json.loads((EVIDENCE/"eval-inputs.json").read_text())
    if len(sys.argv)>1: cases=[c for c in cases if c["id"] in sys.argv[1:]]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results=list(pool.map(run_one,cases))
    sys.exit(1 if any(r.get("exit_code",1)!=0 or r.get("is_error") or not r.get("output") for r in results) else 0)
