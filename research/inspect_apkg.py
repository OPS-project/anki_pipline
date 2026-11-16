from pathlib import Path
import zipfile,sqlite3,json,re,hashlib,io,statistics,sys
import zstandard
from mutagen import File
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent
def clean(s):return BeautifulSoup(s,'html.parser').get_text(' ',strip=True)
def varint(data,i):
 out=0;shift=0
 while True:
  b=data[i];i+=1;out|=(b&127)<<shift
  if b<128:return out,i
  shift+=7
def pb(data):
 i=0;out=[]
 while i<len(data):
  key,i=varint(data,i);field=key>>3;wire=key&7
  if wire==0:v,i=varint(data,i)
  elif wire==2:n,i=varint(data,i);v=data[i:i+n];i+=n
  elif wire==1:v=data[i:i+8];i+=8
  elif wire==5:v=data[i:i+4];i+=4
  else:raise ValueError('unsupported wire '+str(wire))
  out.append((field,v))
 return out
def inspect(path):
 z=zipfile.ZipFile(path);dest=ROOT/'inspection'/path.stem;dest.mkdir(exist_ok=True)
 dbname=next((s for s in ['collection.anki21b','collection.anki21','collection.anki2'] if s in z.namelist()),None)
 db=z.read(dbname)
 if dbname.endswith('b'):db=zstandard.ZstdDecompressor().decompress(db,max_output_size=500*1024*1024)
 dbpath=dest/'collection.sqlite';dbpath.write_bytes(db)
 conn=sqlite3.connect(dbpath)
 conn.create_collation('unicase',lambda a,b:(a.casefold()>b.casefold())-(a.casefold()<b.casefold()))
 modelraw,deckraw=conn.execute('select models,decks from col').fetchone()
 if modelraw:
  models=json.loads(modelraw);decks=json.loads(deckraw)
 else:
  models={}
  for mid,name in conn.execute('select id,name from notetypes'):
   fs=[{'name':r[0]} for r in conn.execute('select name from fields where ntid=? order by ord',(mid,))]
   ts=[{'name':r[0],'config_strings':[(k,v.decode('utf8',errors='replace')) for k,v in pb(r[1]) if isinstance(v,bytes)]} for r in conn.execute('select name,config from templates where ntid=? order by ord',(mid,))]
   models[str(mid)]={'name':name,'flds':fs,'tmpls':ts}
  decks={str(i):{'name':n.replace('\x1f','::')}for i,n in conn.execute('select id,name from decks')}
 media=z.read('media')
 try:media=json.loads(media)
 except Exception:
  entries=pb(zstandard.ZstdDecompressor().decompress(media,max_output_size=50*1024*1024));media={}
  for index,(_,v) in enumerate(entries):
   vals=dict(pb(v));media[str(vals.get(255,index))]=vals[1].decode('utf8')
 lookup={v:k for k,v in media.items()}
 rows=conn.execute('select id,mid,tags,flds from notes').fetchall()
 notes=[];cov={};missing=[]
 for nid,mid,tags,flds in rows:
  model=models.get(str(mid),{});names=[f['name'] for f in model.get('flds',[])]
  fs=dict(zip(names,flds.split('\x1f')));refs={}
  for name,value in fs.items():
   sound=re.findall(r'\[sound:([^\]]+)\]|(?:src|href)=[\"\']([^\"\']+\.(?:mp3|opus|ogg|wav))',value)
   found=[a or b for a,b in sound]
   if found:
    refs[name]=found;cov[name]=cov.get(name,0)+1
    missing.extend((nid,name,f) for f in found if f not in lookup or lookup[f] not in z.NameToInfo)
  notes.append({'id':nid,'model':model.get('name'), 'tags':tags,'fields':fs,'audio_refs':refs})
 (dest/'notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2),encoding='utf8')
 (dest/'models.json').write_text(json.dumps(models,ensure_ascii=False,indent=2),encoding='utf8')
 (dest/'media.json').write_text(json.dumps(media,ensure_ascii=False),encoding='utf8')
 # Select three evenly spaced content notes, then inspect their actual packaged audio.
 samples=[]
 for n in [notes[i] for i in sorted(set([0,len(notes)//2,len(notes)-1]))]:
  aud=[]
  for field,refs in n['audio_refs'].items():
   for ref in refs[:1]:
    if ref in lookup:
     raw=z.read(lookup[ref])
     if dbname.endswith('b'):
      try:raw=zstandard.ZstdDecompressor().decompress(raw,max_output_size=20*1024*1024)
      except Exception:pass
     target=dest/f'sample_{n["id"]}_{len(aud)}{Path(ref).suffix}';target.write_bytes(raw)
     try:
      m=File(io.BytesIO(raw));duration=round(m.info.length,3) if m else None
     except Exception:duration=None
     aud.append({'field':field,'reference':ref,'bytes':len(raw),'duration_s':duration})
  samples.append({'id':n['id'],'fields':{k:clean(v) for k,v in n['fields'].items()},'audio':aud})
 info={'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'size':path.stat().st_size,'db':dbname,'notes':len(notes),'cards':conn.execute('select count(*) from cards').fetchone()[0], 'models':[{ 'name':m.get('name'),'fields':[f['name'] for f in m.get('flds',[])],'cards':[t['name'] for t in m.get('tmpls',[])]}for m in models.values()], 'decks':[d['name'] for d in decks.values()], 'media':len(media),'audio_field_coverage':cov,'missing_refs':missing[:20],'missing_ref_count':len(missing),'samples':samples}
 (dest/'audit.json').write_text(json.dumps(info,ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps({k:v for k,v in info.items() if k not in ['samples','decks']},ensure_ascii=False))
 print('SAMPLES',json.dumps([{'id':s['id'],'fields':{k:v for k,v in s['fields'].items() if not k.startswith(('ex1t_','ex2t_','ex3t_','ex4t_','ex5t_','tr_'))},'audio':s['audio']}for s in samples],ensure_ascii=False)[:4500])
if __name__=='__main__':
 for name in sys.argv[1:]:
  try:inspect(ROOT/'downloads'/name)
  except Exception as e:print(name,type(e).__name__,str(e))
