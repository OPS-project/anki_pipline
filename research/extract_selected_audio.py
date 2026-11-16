from pathlib import Path
import json,zipfile,zstandard
ROOT=Path(__file__).resolve().parent
selections={
 'ankidrone_ranged':[(1723207442445,'SentAudio'),(1723207442517,'SentAudio'),(1723207442423,'SentAudio')],
 'oald':[(1792494562790,'exm_phonetics_am_audio1'),(1792494564248,'exm_phonetics_am_audio1'),(1792494563672,'exm_phonetics_am_audio3')],
 'it_vocab':[(1788304573912,'Audio'),(1788304577620,'Audio'),(1788304577916,'Audio')],
 'n1_grammar':[(1765938747450,'AudioFile'),(1765938747608,'AudioFile'),(1765938747956,'AudioFile')],
}
for name,sels in selections.items():
 p=ROOT/'inspection'/name
 if not(p/'notes.json').exists():continue
 notes={n['id']:n for n in json.loads((p/'notes.json').read_text(encoding='utf8'))}
 media={v:k for k,v in json.loads((p/'media.json').read_text(encoding='utf8')).items()}
 z=zipfile.ZipFile(ROOT/'downloads'/f'{name}.apkg')
 for nid,field in sels:
  refs=notes[nid]['audio_refs'].get(field,[])
  assert refs,(nid,field)
  ref=refs[0];raw=z.read(media[ref])
  if raw[:4]==bytes.fromhex('28b52ffd'):raw=zstandard.ZstdDecompressor().decompress(raw,max_output_size=20*1024*1024)
  out=p/f'sample_chosen_{nid}{Path(ref).suffix}';out.write_bytes(raw)
  print(name,nid,field,ref,len(raw))
