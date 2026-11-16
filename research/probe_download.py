from pathlib import Path
import requests,json
ROOT=Path(__file__).resolve().parent
for sid in ['524918335','258311532']:
 d=json.loads((ROOT/'inspection'/f'anki_{sid}.json').read_text(encoding='utf8'))['available']['deck']
 try:
  r=requests.get(f'https://ankiweb.net/svc/shared/download-deck/{sid}',params={'t':d['downloadKey']},stream=True,timeout=12)
  print(sid,r.status_code,r.headers.get('Content-Length'),r.url.split('?')[0],r.headers.get('Content-Type'),flush=True)
  r.close()
 except Exception as e:print(sid,type(e).__name__,flush=True)
