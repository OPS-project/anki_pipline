from codex_vong1_audit import *

d=load(ROOT/'chung/raw/en-glassygaia-teded-p1/deck.apkg','glassygaia-p1')
ns=d['notes'];length=lengths(ns,'English','en');by={}
for deck in sorted({k for n in ns for k in n['decks']}):
 a=[n for n in ns if deck in n['decks']];by[deck]={'notes':len(a),'length':lengths(a,'English','en'),'vietnamese':sum(bool(text(n['fields']['Vietnamese']))for n in a)}
summary={'notes':len(ns),'cards':d['info']['cards'],'length':length,'with_main_audio':sum(bool(refs(n['fields']['Audio']))for n in ns),'with_image':sum(bool(n['fields']['Image'])for n in ns),'with_vi':sum(bool(text(n['fields']['Vietnamese']))for n in ns),'with_target':sum(bool(text(n['fields']['Word_1']))for n in ns),'source_context':'Subdeck and tags name video; sequential filename. No separate URL/timecode/speaker field.','by_video':by}
(d['out']/'analysis.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
chosen=[ns[0],next(n for n in ns if 'hitler'in n['tags']),next(n for n in ns if 'coffee'in n['tags'])]
sm=save_samples(d,chosen,['Audio','Word_Example_1_Audio'],['English','Word_1','Word_Example_1','Vietnamese'])
print(json.dumps(summary,ensure_ascii=False,indent=2));print('SAMPLES',json.dumps(sm,ensure_ascii=False,indent=2))

d=load(ROOT/'research/downloads/it_vocab.apkg','it-vocab')
print('IT fields',[[f['name']for f in m['flds']]for m in d['models'].values()])
for field in ['Sentence','sentence','ExampleSentence','Expression','Japanese Sentence']:
 if any(field in n['fields']for n in d['notes']):print('IT length',field,lengths(d['notes'],field,'ja'))
print('IT example',str(d['notes'][0])[:1600])
