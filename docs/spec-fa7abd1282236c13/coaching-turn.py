"""Drive one real synthetic student turn; CLI flags documented in cli-help.txt."""
import datetime, hashlib, json, pathlib, subprocess, sys, uuid
from importlib.machinery import SourceFileLoader
helper=SourceFileLoader("live_eval",str(pathlib.Path(__file__).with_name("live-eval.py"))).load_module()
state=helper.EVIDENCE/"conversation-state.json"
prior=json.loads(state.read_text()) if state.exists() else {"session_id":str(uuid.uuid4()),"turns":0}
message=sys.stdin.read()
assert message.strip()
cmd=["claude","-p","--output-format","json","--safe-mode","--strict-mcp-config","--mcp-config",'{"mcpServers":{}}',"--tools","","--permission-mode","dontAsk","--max-turns","3","--system-prompt-file",str(helper.ROOT/"coach/PROMPT.md"),"--resume" if prior["turns"] else "--session-id",prior["session_id"],message]
proc=subprocess.run(cmd,cwd=helper.ROOT,env=helper.ENV,text=True,capture_output=True,timeout=240)
raw=json.loads(proc.stdout) if proc.stdout.strip() else {}
result={"turn":prior["turns"]+1,"timestamp":datetime.datetime.now(datetime.timezone.utc).isoformat(),"runtime":"Claude Code","auth":"subscription","models":list(raw.get("modelUsage",{})),"prompt_sha256":hashlib.sha256((helper.ROOT/"coach/PROMPT.md").read_bytes()).hexdigest(),"input":message,"output":raw.get("result",""),"exit_code":proc.returncode,"is_error":raw.get("is_error"),"subtype":raw.get("subtype")}
(helper.EVIDENCE/("conversation-turn-%02d.json"%result["turn"])).write_text(json.dumps(result,indent=2)+"\n")
if proc.returncode or raw.get("is_error") or not result["output"]:
    print(json.dumps(result)); sys.exit(1)
prior["turns"]+=1
state.write_text(json.dumps(prior,indent=2)+"\n")
print(result["output"])
