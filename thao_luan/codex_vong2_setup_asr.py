"""Download public, local-only speech recognizer for independent sample checks."""
from pathlib import Path
import requests,zipfile,hashlib,json
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/tools/whisper-cpp-v1.9.2';OUT.mkdir(parents=True,exist_ok=True)
SOURCES=[('whisper-bin-x64.zip','https://github.com/ggml-org/whisper.cpp/releases/download/v1.9.2/whisper-bin-x64.zip'),('ggml-small-q5_1.bin','https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small-q5_1.bin')]
def fetch(spec):
 name,url=spec;p=OUT/name
 if not p.exists():
  r=requests.get(url,timeout=180);r.raise_for_status();p.write_bytes(r.content)
 return {'file':name,'source':url,'bytes':p.stat().st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest()}
with ThreadPoolExecutor(max_workers=2)as pool:meta=list(pool.map(fetch,SOURCES))
with zipfile.ZipFile(OUT/'whisper-bin-x64.zip')as z:z.extractall(OUT/'bin')
(OUT/'sources.json').write_text(json.dumps(meta,indent=2),encoding='utf8')
print(meta,flush=True)
print([str(p.relative_to(ROOT))for p in (OUT/'bin').rglob('*.exe')],flush=True)
