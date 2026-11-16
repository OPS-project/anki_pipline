from pathlib import Path
import requests,json,concurrent.futures,os
ROOT=Path(__file__).resolve().parent
d=json.loads((ROOT/'inspection/ankidrone_yandex.json').read_text(encoding='utf8'))
f=next(i for i in d['_embedded']['items']if i['type']=='file');url=f['file'];size=f['size'];chunk=8*1024*1024
dest=ROOT/'downloads/ankidrone_ranged.apkg'
with dest.open('wb')as stream:stream.truncate(size)
def get(start):
 end=min(start+chunk,size)-1;r=requests.get(url,headers={'Range':f'bytes={start}-{end}'},timeout=90);r.raise_for_status()
 if len(r.content)!=end-start+1:raise ValueError('Unexpected range length')
 with dest.open('r+b')as stream:stream.seek(start);stream.write(r.content)
 return start,len(r.content)
with concurrent.futures.ThreadPoolExecutor(max_workers=6)as ex:
 for done in ex.map(get,range(0,size,chunk)):print(done,flush=True)
print('COMPLETE',size,flush=True)
