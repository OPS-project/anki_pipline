"""Finalize inspection evidence, not learning cards or a deck build."""
from codex_vong2_audit import *
import wave,difflib
OUT=ROOT/'chung/kiem_chung_Codex_vong2'
review={
 'method':{'package':'Full collections and media maps independently parsed; raw APKG read only.','sample':'16 evenly spaced note indices per required/optional source; all 64 decoded to PCM 16k mono and recognized locally. One extra DJG dialogue response checked separately.','asr':'Whisper small-q5_1, whisper.cpp v1.9.2, no reference prompt; ASR similarity is a diagnostic, not an error rate or listening certification.','limits':'No human listening; no UI/mobile import test; sample not random or representative of whole corpus; only first audio per note in initial sample.','sampling_indices':{s:[r['index']for r in json.loads((OUT/s/'samples.json').read_text(encoding='utf8'))]for s in ['love-is-blind','sekai-news','djg','ted-amy']}},
 'love-is-blind':{'translation_nonempty':8064,'comments':[
  {'index':0,'finding':'NETFLIX title text is not dialogue; caption should be separated.'},
  {'index':1613,'finding':'English has broader/looser context than literal Japanese; do not use as word-for-word gloss.'},
  {'index':5913,'finding':'Repeated Japanese clause and multiple speakers in one subtitle; ASR recognizes one welcoming phrase. Review CC duplication and transcript orthography.'},
  {'index':8063,'finding':'Japanese music marker and English subtitle credit; exclude from language sentence cards.'},
  {'index':4300,'finding':'Laughter-heavy note. ASR hallucinates repeated laughter; do not turn ASR output into correction.'}]},
 'sekai-news':{'prose_in_16_samples':12,'nonprose_indices':[0,517,776,1940],'comments':[
  {'index':0,'finding':'Preface heading has 83.606 decoded seconds; a text-length filter alone is not an alignment check.'},
  {'index':1811,'finding':'ASR contains next-note opening 大手のニュースサイトや after current sentence. Boundary leakage candidate, requires listening/crop QA.'},
  {'index':129,'finding':'ASR confuses 憂慮/有利; this alone does not establish a deck transcription error.'}],
  'provenance':{'id3_year':'2022','copyright':'(P)2021 Audible, Inc.','official_book_publication':'2019-10-09','official_audible_narrator':'岩崎 愛','audible_url':'https://www.audible.co.jp/pd/B09LYH11CL','note':'Matching title/year/Audible tag supports a commercial human recording; exact speaker identity not acoustically verified. audiobook.jp has a different narrator/version.'}},
 'djg':{'dialogues':137,'multiple_sound_markers':138,'alternatives_or_middot_candidates':389,'comments':[
  {'id':1508885374218,'finding':'Nested/malformed sound tags. Japanese field lacks に in 上手になった whereas Reading includes it. Neither the embedded Azure filename nor the reconstructed Amazon filename exists in the package; needs replacement audio after text repair. Original file not changed.'},
  {'index':3167,'finding':'First clip is A question, second clip B answer. Recognizing only first clip cannot establish truncation of complete dialogue.'},
  {'index':3519,'finding':'Middot in サダム・フセイン is a proper-name separator, not a grammar alternative.'}]},
 'ted-amy':{'comments':[
  {'index':152,'finding':'job interview. is a two-word subtitle fragment; needs adjacent context.'},
  {'index':102,'finding':'Question continues from previous note; not an independent complete sentence.'},
  {'index':237,'finding':'ASR differs slightly from transcript wording; use official transcript/audio, not blind ASR replacement.'}],
  'source':'https://www.ted.com/talks/amy_cuddy_your_body_language_may_shape_who_you_are?view=transcript'}
}
# Confirm recovery candidates in DJG without changing any raw note.
z=zipfile.ZipFile(ROOT/'chung/raw/ja-djg-grammar-sentences-audio/deck.apkg')
media=json.loads(z.read('media'));names=set(media.values())
ns=json.loads((OUT/'djg/notes.json').read_text(encoding='utf8'))
bad=next(n for n in ns if n['id']==1508885374218)['fields']['AwesomeTTS']
inner=re.findall(r'\[sound:([^\[\]]+)\]',bad)
review['djg']['recoverable_inner_files']={r:r in names for r in inner}
outer=re.sub(r'\[sound:([^\[\]]+)\]','',bad)
outer_refs=base.refs(outer)
review['djg']['reconstructed_outer_files']={r:r in names for r in outer_refs}
review['djg']['dialogue_second_clip_asr']=(OUT/'djg/dialogue_3167_part1_asr.txt').read_text(encoding='utf8').strip()
for slug in ['love-is-blind','sekai-news','djg','ted-amy']:
 a=json.loads((OUT/slug/'asr_diagnostic.json').read_text(encoding='utf8'))
 review.setdefault(slug,{})['asr_processed']=len(a['results'])
(OUT/'review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf8')
print('Review saved. ASR processed:',{s:review[s]['asr_processed']for s in ['love-is-blind','sekai-news','djg','ted-amy']})
