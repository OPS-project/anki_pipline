from pathlib import Path
import concurrent.futures, requests, json, sys
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent
tasks={
 'hskstory1.apkg':'https://audio.hskstory.com/downloads/anki/hskstory-hsk1-anki-v11.apkg',
 'hskstory7.apkg':'https://audio.hskstory.com/downloads/anki/hskstory-hsk7-9-anki-v8.apkg',
 'kaishi.apkg':json.loads((ROOT/'inspection/kaishi_releases.json').read_text())['assets'][0]['browser_download_url'],
 'lexideck_sample.apkg':'https://assets-2-prod.whop.com/public/uploads/2026-09-20/305d9e95-7a9d-44b1-8471-76eb2b4f8748/application.apkg',
 'hsk2025.pdf':'https://hsk.cn-bj.ufileos.com/3.0/新版HSK考试大纲1219.pdf',
}
def get(item):
 name,url=item;dest=ROOT/'downloads'/name
 if dest.exists():return name,dest.stat().st_size,'cached'
 try:
  r=requests.get(url,timeout=180,stream=True);r.raise_for_status()
  with dest.open('wb') as f:
   for chunk in r.iter_content(1024*1024):f.write(chunk)
  return name,dest.stat().st_size,r.status_code
 except Exception as e:return name,str(e)
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
  for result in ex.map(get,tasks.items()):print(result,flush=True)
