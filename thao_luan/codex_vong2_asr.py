"""Local ASR diagnostic only; reference text is never supplied to recognizer."""
from codex_vong2_audit import *
import difflib,time
OUT=ROOT/'chung/kiem_chung_Codex_vong2'
TOOLS=ROOT/'research/tools/whisper-cpp-v1.9.2'
EXE=TOOLS/'bin/Release/whisper-cli.exe';MODEL=TOOLS/'ggml-small-q5_1.bin'
def norm(s):return ''.join(c for c in unicodedata.normalize('NFKC',s).lower()if c.isalnum())
def sim(a,b):return difflib.SequenceMatcher(None,norm(a),norm(b),autojunk=False).ratio()
for slug in ['sekai-news','love-is-blind','djg','ted-amy']:
 samples=json.loads((OUT/slug/'samples.json').read_text(encoding='utf8'))
 result=[];sf='Sentence'if slug in ['sekai-news','ted-amy']else'Expression'if slug=='love-is-blind'else'Japanese'
 for s in samples:
  if not s['decode_ok']:continue
  wav=ROOT/s['wav'];prefix=wav.parent/(wav.stem+'_asr')
  cmd=[str(EXE),'-m',str(MODEL),'-f',str(wav),'-l','en'if slug=='ted-amy'else'ja','-t','6','-bo','1','-bs','1','-nf','-nt','-otxt','-of',str(prefix)]
  start=time.monotonic();r=subprocess.run(cmd,capture_output=True)
  fp=prefix.with_suffix('.txt');transcript=fp.read_text(encoding='utf8').strip()if fp.exists()else''
  expected=plain(s['fields'][sf],slug=='love-is-blind')
  row={'index':s['index'],'id':s['id'],'reference':expected,'asr':transcript,'similarity':round(sim(expected,transcript),3),'previous_similarity':round(sim(plain(s['previous']),transcript),3),'next_similarity':round(sim(plain(s['next']),transcript),3),'exit_code':r.returncode,'elapsed_seconds':round(time.monotonic()-start,2)}
  result.append(row)
  (OUT/slug/'asr_diagnostic.json').write_text(json.dumps({'model':'Whisper small-q5_1; whisper.cpp v1.9.2; greedy; language fixed; no reference prompt','method':'16 evenly spaced note indices; ASR output is fallible and not human listening or full alignment certification.','results':result},ensure_ascii=False,indent=2),encoding='utf8')
  print(slug,s['index'],row['similarity'],row['elapsed_seconds'],flush=True)
