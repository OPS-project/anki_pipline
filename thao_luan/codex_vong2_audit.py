"""Independent read-only package audit; no deck output or authentication."""
import codex_vong1_audit as base
from codex_vong1_audit import *
import subprocess
import imageio_ffmpeg

base.OUT=ROOT/'chung/kiem_chung_Codex_vong2';base.OUT.mkdir(exist_ok=True)
FFMPEG=imageio_ffmpeg.get_ffmpeg_exe()
SPECS=[('love-is-blind','ja-subs2srs-love-is-blind-japan','Expression','Audio_Sentence','English'),('sekai-news','ja-subs2srs-audiobook-sekai-no-news','Sentence','Audio',None),('djg','ja-djg-grammar-sentences-audio','Japanese','AwesomeTTS','English'),('ted-amy','en-zh-ted-amycuddy-video',None,None,None)]

def plain(s,remove_speaker=False):
 soup=BeautifulSoup(s,'html.parser')
 for e in soup.find_all(['rt','rp']):e.decompose()
 s=base.text(str(soup));s=re.sub(r'\[sound:[^\]]+\]','',s)
 s=re.sub(r'\[[^\]]*\]','',s) # furigana bracket annotations
 if remove_speaker:s=re.sub(r'（[^）]*）|\([^)]*\)','',s)
 return s

def stats(v):
 v=sorted(v)
 return {'n':len(v),'median':statistics.median(v),'p10':v[int(.1*(len(v)-1))],'p25':v[len(v)//4],'p75':v[3*len(v)//4],'p90':v[int(.9*(len(v)-1))],'min':v[0],'max':v[-1]}if v else{}

def main():
 for slug,folder,sf,af,tf in SPECS:
  d=base.load(ROOT/'chung/raw'/folder/'deck.apkg',slug)
  ns=d['notes'];fields=list(ns[0]['fields']);print(slug,len(ns),fields,flush=True)
  (d['out']/'notes.json').write_text(json.dumps(ns,ensure_ascii=False),encoding='utf8')
  if not sf:
   sf=next((k for k in fields if k.lower()in['sentence','expression','english','text','front','subtitle']),None)
   af=next((k for k in fields if 'video'in k.lower()or 'audio'in k.lower()),None)
   print('TED first note',str(ns[0])[:1600],flush=True)
  if not sf or not af:continue
  lengths_raw=[len(re.sub(r'\s','',plain(n['fields'].get(sf,''))))if slug!='ted-amy'else len(base.words(n['fields'].get(sf,'')))for n in ns]
  lengths_clean=[len(re.sub(r'\s','',plain(n['fields'].get(sf,''),True)))if slug!='ted-amy'else len(base.words(n['fields'].get(sf,'')))for n in ns]
  durations={};errors=[];present_notes=0;ref_notes=0
  for n in ns:
   rr=base.refs(n['fields'].get(af,''));ref_notes+=bool(rr)
   valid=[r for r in rr if r in d['lookup'] and d['lookup'][r]in d['zip'].NameToInfo]
   present_notes+=bool(valid)
   for r in valid:
    if r in durations:continue
    raw=base.decompress(d['zip'].read(d['lookup'][r]))
    try:
     m=File(io.BytesIO(raw));durations[r]=m.info.length if m else None
    except Exception:durations[r]=None
    if durations[r]is None:errors.append(r)
  nonempty={k:sum(bool(plain(n['fields'].get(k,'')))for n in ns)for k in fields}
  by={}
  for deck in sorted({v for n in ns for v in n['decks']}):
   ix=[i for i,n in enumerate(ns)if deck in n['decks']]
   comparison=lengths_clean if slug=='love-is-blind'else lengths_raw
   by[deck]={'notes':len(ix),'length':stats([comparison[i]for i in ix]),'ge30':sum(comparison[i]>=30 for i in ix)}
  metrics={'sentence_field':sf,'audio_field':af,'length_raw':stats(lengths_raw),'length_no_speaker':stats(lengths_clean),'ge30_raw':sum(v>=30 for v in lengths_raw),'ge30_clean':sum(v>=30 for v in lengths_clean),'audio_reference_notes':ref_notes,'audio_present_notes':present_notes,'distinct_audio_refs':len(durations),'durations_all_unique':stats([v for v in durations.values()if v]),'duration_parse_errors':errors,'nonempty_fields':nonempty,'by_deck':by}
  metrics['nonempty_raw_fields']={k:sum(bool(n['fields'].get(k,'').strip())for n in ns)for k in fields}
  if slug=='djg':
   metrics['alternative_marker_notes']=[n['id']for n in ns if '・'in n['fields'][sf]or '{'in n['fields'][sf]]
   metrics['dialogue_marker_notes']=[n['id']for n in ns if re.search(r'(?:A|Ａ)\s*[:：]',plain(n['fields'][sf]))]
   metrics['tts_prefix_note_counts']=dict(Counter(r.split('-')[0]for n in ns for r in base.refs(n['fields'].get(af,''))))
  if slug=='love-is-blind':
   spans=[]
   for n in ns:
    rr=base.refs(n['fields'].get(af,''))
    if not rr:continue
    mat=re.search(r'_(\d+)_(\d+\.\d+\.\d+\.\d+)-(\d+\.\d+\.\d+\.\d+)',rr[0])
    if mat:
     def sec(s):h,m,s,ms=map(int,s.split('.'));return h*3600+m*60+s+ms/1000
     spans.append((mat[1],sec(mat[2]),sec(mat[3]),n['id']))
   spans.sort();gaps=[(a[3],b[3],b[1]-a[2])for a,b in zip(spans,spans[1:])if a[0]==b[0]]
   metrics['timestamp_notes']=len(spans);metrics['adjacent_overlaps']=sum(g<0 for a,b,g in gaps);metrics['adjacent_gap_le_07']=sum(g<=.7 for a,b,g in gaps);metrics['overlap_examples']=[v for v in gaps if v[2]<0][:10]
  (d['out']/'analysis.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2),encoding='utf8')
  (d['out']/'durations.json').write_text(json.dumps(durations,ensure_ascii=False),encoding='utf8')
  # Deterministic evenly spaced evidence, independent of Claude's examples.
  ids=sorted(set(round(i*(len(ns)-1)/15)for i in range(16)))
  samples=[]
  for i in ids:
   n=ns[i];rr=base.refs(n['fields'].get(af,''));valid=[r for r in rr if r in d['lookup']]
   if not valid:continue
   ref=valid[0];p=d['out']/f'sample_{i:05d}{Path(ref).suffix}';p.write_bytes(base.decompress(d['zip'].read(d['lookup'][ref])))
   wav=p.with_suffix('.wav')
   c=subprocess.run([FFMPEG,'-v','error','-y','-i',str(p),'-ar','16000','-ac','1','-c:a','pcm_s16le',str(wav)],capture_output=True)
   samples.append({'index':i,'id':n['id'],'decks':n['decks'],'fields':n['fields'],'ref':ref,'duration':durations.get(ref),'wav':str(wav.relative_to(ROOT)),'decode_ok':c.returncode==0,'previous':ns[max(0,i-1)]['fields'].get(sf,''),'next':ns[min(len(ns)-1,i+1)]['fields'].get(sf,'')})
  (d['out']/'samples.json').write_text(json.dumps(samples,ensure_ascii=False,indent=2),encoding='utf8')
  print('DONE',slug,{k:v for k,v in metrics.items()if k in ['length_raw','length_no_speaker','ge30_raw','ge30_clean','audio_reference_notes','audio_present_notes','distinct_audio_refs','durations_all_unique','timestamp_notes','adjacent_overlaps','adjacent_gap_le_07']},flush=True)

if __name__=='__main__':main()
