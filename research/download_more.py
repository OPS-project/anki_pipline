from download_samples import get,ROOT
from bs4 import BeautifulSoup
import requests,json,concurrent.futures
tasks={
 'ankidrone.apkg':requests.get('https://cloud-api.yandex.net/v1/disk/public/resources/download',params={'public_key':'https://disk.yandex.com/d/adEb8n9uhOacHw','path':'/Ankidrone Essentials V9.apkg'},timeout=30).json()['href'],
 'it_vocab.apkg':'https://github.com/KakkoiDev/nihongo-it-anki/releases/download/it-vocab/v5.2/it-vocab-complete.apkg',
 'n1_grammar.apkg':'https://github.com/mxggle/anki-jlpt-n1-grammar-example-sentences/releases/download/v2.0.0/JLPT_N1_N1__-v2.0.0.apkg',
}
for sid,name in [('1736976202','ultimate1'),('801432412','ultimate2'),('804826171','closeup_c2'),('524918335','english_c1_us'),('258311532','newhsk_sentence')]:
 d=json.loads((ROOT/'inspection'/f'anki_{sid}.json').read_text(encoding='utf8'))['available']['deck']
 tasks[name+'.apkg']=f'https://ankiweb.net/svc/shared/download-deck/{sid}?t='+d['downloadKey']
for level in range(2,7):
 r=requests.get(f'https://hskstory.com/anki/hsk-{level}',timeout=30);soup=BeautifulSoup(r.content,'html.parser')
 (ROOT/'inspection'/f'hskstory{level}.html').write_text(r.text,encoding='utf8')
 tasks[f'hskstory{level}.apkg']=next(a['href'] for a in soup.select('a[href]') if a['href'].endswith('.apkg'))
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
  for result in ex.map(get,tasks.items()):print(result,flush=True)
