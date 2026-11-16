"""Round 3: read source APKGs only; output inspection evidence, no deck build."""
import codex_vong1_audit as base
from codex_vong1_audit import *
import subprocess,wave
import imageio_ffmpeg

base.OUT=ROOT/'chung/kiem_chung_Codex_vong3';base.OUT.mkdir(exist_ok=True)
FFMPEG=imageio_ffmpeg.get_ffmpeg_exe()
SPECS=[('friends','en-sitcom-friends-s01e02','en'),('gg-p2','en-glassygaia-teded-p2','en'),('gg-p3','en-glassygaia-teded-p3','en'),('zh-7000','zh-vi-7000-shadowing','zh')]

def describe():
 for slug,folder,lang in SPECS:
  d=base.load(ROOT/'chung/raw'/folder/'deck.apkg',slug)
  (d['out']/'notes.json').write_text(json.dumps(d['notes'],ensure_ascii=False),encoding='utf8')
  print(slug,d['info']['notes'],d['info']['audio_fields'],d['info']['missing_reference_count'],flush=True)
  print('MODELS',[(m['name'],[f['name']for f in m['flds']])for m in d['models'].values()],flush=True)
  print('SAMPLE',str(d['notes'][0])[:2200],flush=True)

def stats(v):
 v=sorted(v)
 return {'n':len(v),'median':statistics.median(v),'p10':v[int(.1*(len(v)-1))],'p25':v[len(v)//4],'p75':v[3*len(v)//4],'p90':v[int(.9*(len(v)-1))],'min':v[0],'max':v[-1]}if v else{}

def audit():
 mapping={'friends':('Target: line','Sound',None),'gg-p2':('English','Audio','Vietnamese'),'gg-p3':('English','Audio','Vietnamese'),'zh-7000':('Hanzi','Audio Chinese','Part of Speech')}
 for slug,folder,lang in SPECS:
  d=base.load(ROOT/'chung/raw'/folder/'deck.apkg',slug);ns=d['notes'];sf,af,tf=mapping[slug]
  (d['out']/'notes.json').write_text(json.dumps(ns,ensure_ascii=False),encoding='utf8')
  lengths=[len(base.words(n['fields'][sf]))if lang=='en'else len(re.sub(r'\s','',base.text(n['fields'][sf])))for n in ns]
  durations={};missing=[];audio_notes=0;rawtags={};withaudio=[]
  for n in ns:
   rr=base.refs(n['fields'].get(af,''));valid=[r for r in rr if r in d['lookup']and d['lookup'][r]in d['zip'].NameToInfo]
   audio_notes+=bool(valid)
   if valid:withaudio.append(n)
   else:missing.append({'id':n['id'],'sentence':base.text(n['fields'][sf]),'audio_field':n['fields'].get(af,'')})
   for r in valid:
    if r in durations:continue
    raw=base.decompress(d['zip'].read(d['lookup'][r]))
    try:
     m=File(io.BytesIO(raw));durations[r]=m.info.length if m else None
     if len(rawtags)<3:rawtags[r]={'duration':durations[r],'tags':str(m.tags)[:1400]if m and m.tags else None,'sample_rate':getattr(m.info,'sample_rate',None)if m else None}
    except Exception:durations[r]=None
  report={'notes':len(ns),'sentence_field':sf,'audio_field':af,'translation_field':tf,'length':stats(lengths),'ge12':sum(v>=12 for v in lengths),'ge20':sum(v>=20 for v in lengths),'audio_present_notes':audio_notes,'audio_missing_notes':missing,'unique_referenced_files':len(durations),'audio_seconds_unique':stats([v for v in durations.values()if v]),'unparsed_durations':sum(v is None for v in durations.values()),'nonempty_raw_fields':{k:sum(bool(n['fields'].get(k,'').strip())for n in ns)for k in ns[0]['fields']},'source_audio_prefixes':dict(Counter(r.split('-')[0]for r in durations))if lang=='zh'else{},'media_metadata_samples':rawtags}
  if tf:
   report['translation_empty_notes']=[n['id']for n in ns if not base.text(n['fields'][tf])]
   report['translation_lengths']=[{'id':n['id'],'source_n':lengths[i],'vi_n':len(base.text(n['fields'][tf]).split()),'source':base.text(n['fields'][sf]),'translation':base.text(n['fields'][tf])}for i,n in enumerate(ns)if base.text(n['fields'][tf])and (len(base.text(n['fields'][tf]).split())<=5 or (lang=='en'and len(base.text(n['fields'][tf]).split())/max(1,lengths[i])<.6))]
  if slug=='friends':
   report['context_before_nonempty']=sum(bool(base.text(n['fields']['Target: line before']))for n in ns)
   report['context_after_nonempty']=sum(bool(base.text(n['fields']['Target: line after']))for n in ns)
  (d['out']/'analysis.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
  (d['out']/'durations.json').write_text(json.dumps(durations,ensure_ascii=False),encoding='utf8')
  # Sixteen evenly spaced notes, not chosen for good-looking translations/audio.
  indices=sorted({round(i*(len(ns)-1)/15)for i in range(16)})
  samples=[]
  for i in indices:
   n=ns[i];rr=base.refs(n['fields'][af]);valid=[r for r in rr if r in d['lookup']]
   if not valid:continue
   r=valid[0];p=d['out']/f'sample_{i:05d}{Path(r).suffix}';p.write_bytes(base.decompress(d['zip'].read(d['lookup'][r])))
   wav=p.with_suffix('.wav');res=subprocess.run([FFMPEG,'-v','error','-y','-i',str(p),'-ar','16000','-ac','1','-c:a','pcm_s16le',str(wav)],capture_output=True)
   secs=None
   if res.returncode==0:
    with wave.open(str(wav))as w:secs=w.getnframes()/w.getframerate()
   samples.append({'index':i,'id':n['id'],'lang':lang,'sentence':base.text(n['fields'][sf]),'translation':base.text(n['fields'][tf])if tf else None,'fields':n['fields'],'ref':r,'wav':str(wav.relative_to(ROOT)),'decode_ok':res.returncode==0,'decoded_seconds':secs})
  (d['out']/'samples.json').write_text(json.dumps(samples,ensure_ascii=False,indent=2),encoding='utf8')
  print(slug,{k:v for k,v in report.items()if k in ['notes','length','audio_present_notes','audio_missing_notes','unique_referenced_files','audio_seconds_unique','unparsed_durations','context_before_nonempty','context_after_nonempty']},'SAMPLES',len(samples),flush=True)

if __name__=='__main__':audit()
