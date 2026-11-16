from pathlib import Path
import requests,re,json,concurrent.futures,datetime
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent
def fetch(name,url):
 try:
  r=requests.get(url,timeout=35);r.raise_for_status();(ROOT/'inspection'/name).write_text(r.text,encoding='utf8')
  soup=BeautifulSoup(r.content,'html.parser')
  return {'name':name,'text':soup.get_text(' ',strip=True)[:12000], 'media':re.findall(r'https[^\s<>"\\]+?(?:mp3|apkg|ogg|wav)[^\s<>"\\]*',r.text)[:30]}
 except Exception as e:return {'name':name,'error':str(e)}
if __name__=='__main__':
 for item in [('refold_buy.html','https://refold.la/decks/buy/english-phrasal-verbs-deck'),('n1_readme.txt','https://raw.githubusercontent.com/mxggle/anki-jlpt-n1-grammar-example-sentences/main/README.md'),('it_audit.txt','https://raw.githubusercontent.com/KakkoiDev/nihongo-it-anki/master/docs/tts-audio-debugging.md')]:
  print(json.dumps(fetch(*item),ensure_ascii=False))
