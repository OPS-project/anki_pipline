from codex_vong1_audit import *

def save(slug,data):
 p=OUT/slug;p.mkdir(exist_ok=True);(p/'analysis.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')

def oald():
 ns=json.loads((ROOT/'research/inspection/oald/notes.json').read_text(encoding='utf8'))
 media=set(json.loads((ROOT/'research/inspection/oald/media.json').read_text(encoding='utf8')).values())
 c1=[n for n in ns if n['fields']['def_cefr']=='C1'];pairs=[]
 for n in c1:
  f=n['fields']
  for i in range(1,4):
   s=text(f[f'exm_structured_content{i}']);audio=refs(f[f'exm_phonetics_br_audio{i}'])+refs(f[f'exm_phonetics_am_audio{i}'])
   valid=[a for a in audio if a in media]
   pairs.append({'id':n['id'],'headword':f['headword'],'i':i,'sentence':s,'words':len(words(s)),'audio':valid,'has_audio':bool(valid),'terminal':bool(re.search(r'[.!?][\"”’\)]*$',s)),'capital':bool(re.match(r'^[\"“‘(]*[A-Z]',s))})
 all_audio=[p for p in pairs if p['has_audio'] and p['sentence']]
 structural=[p for p in all_audio if p['words']>=6 and p['terminal'] and p['capital']]
 result={'method':'def_cefr C1; at least one example slot with packaged audio. Structural candidate: >=6 English tokens, capital start, terminal .!? allowing closing quotes. Does NOT certify syntax, audio alignment or C1 difficulty.','c1_senses':len(c1),'c2_senses':sum(n['fields']['def_cefr']=='C2'for n in ns),'c1_with_audio':len({p['id']for p in all_audio}),'c1_audio_pairs':len(all_audio),'structural_senses':len({p['id']for p in structural}),'structural_pairs':len(structural),'structural_median_words':statistics.median(p['words']for p in structural),'all_audio_median_words':statistics.median(p['words']for p in all_audio),'all_audio_ge20':sum(p['words']>=20 for p in all_audio),'all_audio_pairs':all_audio,'structural_candidates':structural}
 save('oald-c1-filter',result)
 print('OALD',{k:v for k,v in result.items()if not isinstance(v,list)})

def newhsk():
 d=load(ROOT/'chung/raw/newhsk3-sentence-hsk1-4/deck.apkg','newhsk3-1-4')
 ns=[n for n in d['notes']if 'Listening'in d['models'][str(n['mid'])]['name']]
 levels={}
 for level in range(1,5):
  a=[n for n in ns if d['models'][str(n['mid'])]['name'].endswith(str(level))]
  levels[str(level)]={'notes':len(a),'targets':len({n['fields']['Focus Word Simplified']for n in a}),'length':lengths(a,'Mandarin Sentence Simplified','ja'),'audio_ref_notes':sum(bool(refs(n['fields']['Han']))for n in a)}
 unique={n['fields']['Mandarin Sentence Simplified']for n in ns}
 sm=save_samples(d,[ns[0],ns[len(ns)//2],ns[-1]],['Han'],['Focus Word Simplified','Focus Word Pinyin','Mandarin Sentence Simplified','Mandarin Sentence Pinyin','English Sentence'])
 save('newhsk3-1-4',{'listening_notes':len(ns),'distinct_sentence_texts':len(unique),'levels':levels,'samples':sm,'front_audio_models':[m['name']for m in d['models'].values()if any('{{Han}}'in t.get('qfmt','')for t in m['tmpls'])],'back_audio_models':[m['name']for m in d['models'].values()if any('{{Han}}'in t.get('afmt','')for t in m['tmpls'])]})
 print('NewHSK',levels,'distinct',len(unique))

def glassy():
 d=load(ROOT/'chung/raw/en-glassygaia-teded-p1/deck.apkg','glassygaia-p1')
 (d['out']/'notes.json').write_text(json.dumps(d['notes'],ensure_ascii=False),encoding='utf8')
 print('Glassy',d['info']['notes'],d['info']['audio_fields'],[(m['name'],[f['name']for f in m['flds']])for m in d['models'].values()])
 for n in d['notes'][:1]:print(str(n)[:3000])

if __name__=='__main__':
 oald();newhsk();glassy()
