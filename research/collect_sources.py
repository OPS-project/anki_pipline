from pathlib import Path
import concurrent.futures, json, requests, re
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parent
URLS={
 'hskstory1':'https://hskstory.com/anki/hsk-1',
 'hskstory7':'https://hskstory.com/anki/hsk-7-9',
 'hskstory_about':'https://hskstory.com/about',
 'newhsk_readme':'https://raw.githubusercontent.com/NewHSK3/new-hsk-3-anki-deck/main/README.md',
 'newhsk_releases':'https://api.github.com/repos/NewHSK3/new-hsk-3-anki-deck/releases',
 'kaishi_releases':'https://api.github.com/repos/donkuri/kaishi/releases/latest',
 'kaishi_tree':'https://api.github.com/repos/donkuri/kaishi/git/trees/main?recursive=1',
 'oald_releases':'https://api.github.com/repos/5mdld/anki-english-oald-decks/releases/latest',
 'n1_tree':'https://api.github.com/repos/mxggle/anki-jlpt-n1-grammar-example-sentences/git/trees/main?recursive=1',
 'anki_english':'https://ankiweb.net/shared/info/1640832357',
 'anki_c1mirror':'https://anki-decks.com/anki-decks/english/english-c1-american-accent/',
 'anki_collocations':'https://ankivn.com/decks/advanced-english-collocations-1000-daily-practice-cards/',
 'ankidrone':'https://tatsumoto-ren.github.io/blog/ankidrone-essentials.html',
 'lexicore':'https://raw.githubusercontent.com/X-Trivle/LexiCore/main/README.md',
}

def get(item):
 name,url=item
 try:
  r=requests.get(url,timeout=50);r.raise_for_status()
  ext='.json' if 'api.github' in url else '.html' if '<html' in r.text[:500].lower() else '.txt'
  (ROOT/'inspection'/f'{name}{ext}').write_text(r.text,encoding='utf-8')
  if ext=='.json':
   data=r.json()
   if isinstance(data,list): data=[{'tag':d.get('tag_name'),'date':d.get('published_at'),'assets':[(a['name'],a['size'],a['browser_download_url']) for a in d.get('assets',[])]} for d in data]
   elif 'assets' in data:data={'tag':data.get('tag_name'),'date':data.get('published_at'),'assets':[(a['name'],a['size'],a['browser_download_url']) for a in data['assets']]}
   elif 'tree' in data:data=[d['path'] for d in data['tree']][:80]
   return name,data
  if ext=='.html':
   soup=BeautifulSoup(r.text,'html.parser')
   links=[(a.get_text(' ',strip=True)[:70],a.get('href')) for a in soup.select('a[href]') if any(s in a.get('href','') for s in ['apkg','download','ankiweb.net','gumroad','payhip','yandex'])]
   scripts=[s.get('src') for s in soup.select('script[src]')]
   return name,{'links':links,'scripts':scripts,'text':soup.get_text(' ',strip=True)[:500]}
  return name,r.text[:7500]
 except Exception as e:return name,str(e)

if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
  for name,result in ex.map(get,URLS.items()):print(json.dumps({name:result},ensure_ascii=False))
