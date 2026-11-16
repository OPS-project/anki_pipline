"""Local speech diagnostic; source text is not passed to recognizer."""
from codex_vong3_audit import *
import difflib,time
OUT=ROOT/'chung/kiem_chung_Codex_vong3'
TOOLS=ROOT/'research/tools/whisper-cpp-v1.9.2'
EXE=TOOLS/'bin/Release/whisper-cli.exe';MODEL=TOOLS/'ggml-small-q5_1.bin'
def norm(s):return ''.join(c for c in unicodedata.normalize('NFKC',s).lower()if c.isalnum())
for slug,folder,lang in SPECS:
 result=[]
 for s in json.loads((OUT/slug/'samples.json').read_text(encoding='utf8')):
  if not s['decode_ok']:continue
  wav=ROOT/s['wav'];prefix=wav.parent/(wav.stem+'_asr')
  start=time.monotonic()
  r=subprocess.run([str(EXE),'-m',str(MODEL),'-f',str(wav),'-l',lang,'-t','6','-bo','1','-bs','1','-nf','-nt','-otxt','-of',str(prefix)],capture_output=True)
  p=prefix.with_suffix('.txt');hyp=p.read_text(encoding='utf8').strip()if p.exists()else''
  row={'index':s['index'],'id':s['id'],'reference':s['sentence'],'translation':s['translation'],'asr':hyp,'similarity':round(difflib.SequenceMatcher(None,norm(s['sentence']),norm(hyp),autojunk=False).ratio(),3),'exit_code':r.returncode,'elapsed_seconds':round(time.monotonic()-start,2)}
  result.append(row)
  (OUT/slug/'asr_diagnostic.json').write_text(json.dumps({'model':'Whisper small-q5_1; whisper.cpp v1.9.2; greedy; language fixed; no reference prompt','method':'16 evenly spaced notes, diagnostic only. Not human listening or full-corpus alignment certification.','results':result},ensure_ascii=False,indent=2),encoding='utf8')
  print(slug,row['index'],row['similarity'],flush=True)
