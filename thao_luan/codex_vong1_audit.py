"""Read-only APKG metrics for round 1. No authentication or deck building."""
from pathlib import Path
import sys,json,re,sqlite3,zipfile,statistics,hashlib,unicodedata,io
from collections import Counter
from bs4 import BeautifulSoup
import zstandard
from mutagen import File

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'research'))
from inspect_apkg import pb
OUT=ROOT/'chung'/'kiem_chung_Codex_vong1'
OUT.mkdir(exist_ok=True)

def text(s):
 # Inline markup can split a word letter by letter. Only block/BR boundaries
 # introduce whitespace; do not count styled letters as separate words.
 s=re.sub(r'<\s*/?\s*(?:br|p|div|li|tr|h[1-6])\b[^>]*>',' ',s,flags=re.I)
 s=BeautifulSoup(s,'html.parser').get_text()
 s=''.join(c for c in s if unicodedata.category(c)!='Cf')
 return re.sub(r'\s+',' ',s).strip()
def chars(s):return len(re.sub(r'\s+','',text(s)))
def words(s):return re.findall(r"[A-Za-z]+(?:[’'-][A-Za-z]+)*|\d+",text(s))
def refs(s):return re.findall(r'\[sound:([^\]]+)\]',s)+re.findall(r'<(?:audio|source)\b[^>]*\bsrc=[\"\']([^\"\']+)',s)
def decompress(b):
 return zstandard.ZstdDecompressor().decompress(b,max_output_size=700*1024*1024)if b[:4]==bytes.fromhex('28b52ffd')else b

def load(path,slug):
 out=OUT/slug;out.mkdir(exist_ok=True)
 z=zipfile.ZipFile(path);dbn=next(n for n in ['collection.anki21b','collection.anki21','collection.anki2']if n in z.namelist())
 dbp=out/'collection.sqlite';dbp.write_bytes(decompress(z.read(dbn)))
 c=sqlite3.connect(dbp);c.create_collation('unicase',lambda a,b:(a.casefold()>b.casefold())-(a.casefold()<b.casefold()))
 mr,dr=c.execute('select models,decks from col').fetchone()
 if mr:
  models=json.loads(mr);decks={int(k):v['name']for k,v in json.loads(dr).items()}
 else:
  models={str(i):{'name':n,'flds':[{'name':r[0]}for r in c.execute('select name from fields where ntid=? order by ord',(i,))], 'tmpls':[{'name':r[0],'config_strings':[(k,v.decode('utf8',errors='replace'))for k,v in pb(r[1])if isinstance(v,bytes)]}for r in c.execute('select name,config from templates where ntid=?order by ord',(i,))]}for i,n in c.execute('select id,name from notetypes')}
  decks={i:n.replace('\x1f','::')for i,n in c.execute('select id,name from decks')}
 raw=decompress(z.read('media'))
 try:media=json.loads(raw)
 except Exception:media={str(dict(pb(v)).get(255,i)):dict(pb(v))[1].decode('utf8')for i,(_,v)in enumerate(pb(raw))}
 lookup={v:k for k,v in media.items()}
 carddecks={}
 for nid,did in c.execute('select nid,did from cards'):carddecks.setdefault(nid,set()).add(decks.get(did,str(did)))
 notes=[{'id':nid,'mid':mid,'tags':tags,'decks':sorted(carddecks.get(nid,[])), 'fields':dict(zip([f['name']for f in models[str(mid)]['flds']],flds.split('\x1f')))}for nid,mid,tags,flds in c.execute('select id,mid,tags,flds from notes')]
 counts=Counter();missing=[]
 for n in notes:
  for k,v in n['fields'].items():
   rr=refs(v)
   if rr:counts[k]+=1
   missing.extend((n['id'],k,r)for r in rr if r not in lookup or lookup.get(r)not in z.NameToInfo)
 info={'source_path':str(path.relative_to(ROOT)),'sha256':hashlib.file_digest(path.open('rb'),'sha256').hexdigest(),'notes':len(notes),'cards':c.execute('select count(*)from cards').fetchone()[0],'models':models,'decks':decks,'media':len(media),'audio_fields':dict(counts),'missing_reference_count':len(missing),'missing_references':missing[:10]}
 (out/'package_metrics.json').write_text(json.dumps(info,ensure_ascii=False,indent=2),encoding='utf8')
 return {'path':path,'slug':slug,'out':out,'zip':z,'db':c,'models':models,'decks':decks,'notes':notes,'media':media,'lookup':lookup,'info':info}

def lengths(ns,field,lang):
 ts=[text(n['fields'].get(field,''))for n in ns if text(n['fields'].get(field,''))]
 ls=[chars(t)if lang=='ja'else len(words(t))for t in ts]
 if not ls:return {}
 return {'n':len(ls),'median':statistics.median(ls),'p25':sorted(ls)[len(ls)//4],'p75':sorted(ls)[3*len(ls)//4],'max':max(ls),'ge30':sum(x>=30 for x in ls),'ge20':sum(x>=20 for x in ls),'ge15':sum(x>=15 for x in ls)}

def save_samples(d,ns,audiofields,fields):
 samples=[]
 for n in ns:
  aud=[]
  for f in audiofields:
   for ref in refs(n['fields'].get(f,''))[:1]:
    slot=d['lookup'].get(ref)
    if slot is None or slot not in d['zip'].NameToInfo:aud.append({'field':f,'ref':ref,'missing':True});continue
    raw=decompress(d['zip'].read(slot));dest=d['out']/('sample_'+str(n['id'])+'_'+str(len(aud))+Path(ref).suffix);dest.write_bytes(raw)
    try:m=File(io.BytesIO(raw));duration=m.info.length if m else None
    except Exception:duration=None
    aud.append({'field':f,'ref':ref,'bytes':len(raw),'duration':duration,'tags':str(m.tags)[:1000]if m and m.tags else None})
  samples.append({'id':n['id'],'fields':{k:text(n['fields'].get(k,''))for k in fields},'audio':aud})
 (d['out']/'samples.json').write_text(json.dumps(samples,ensure_ascii=False,indent=2),encoding='utf8')
 return samples

if __name__=='__main__':
 for slug,path in [('c1-american',ROOT/'chung/raw/en-c1-american-accent/deck.apkg'),('newhsk3-1-4',ROOT/'chung/raw/newhsk3-sentence-hsk1-4/deck.apkg')]:
  d=load(path,slug)
  (d['out']/'notes.json').write_text(json.dumps(d['notes'],ensure_ascii=False),encoding='utf8')
  print(slug,{k:d['info'][k]for k in ['notes','cards','audio_fields','missing_reference_count']},[m['name']for m in d['models'].values()]);print('Fields',[[f['name']for f in m['flds']]for m in d['models'].values()]);print('Decks',list(d['decks'].values())[:18])
  if slug=='c1-american':
   print('Length',lengths(d['notes'],'Front','en'))
   save_samples(d,[d['notes'][i]for i in [0,len(d['notes'])//2,-1]],['Audio','Example Audio'],['Front','Back','Definition'])
