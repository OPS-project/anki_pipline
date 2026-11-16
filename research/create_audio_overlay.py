from pathlib import Path
import json,csv,re
ROOT=Path(__file__).resolve().parent
notes=json.loads((ROOT/'inspection/hskstory1/notes.json').read_text(encoding='utf8'))
path=ROOT.parent/'HSKStory_HSK1_SentenceAudio.tsv'
rows=[]
for n in notes:
 src=re.search(r'<audio[^>]+src="([^"]+)"',n['fields']['StoryTitle'])
 assert src,n['id']
 rows.append([n['fields']['Hanzi'],f'[sound:{src[1]}]'])
assert len(rows)==300 and len({r[0]for r in rows})==300
with path.open('w',encoding='utf8',newline='')as f:
 f.write('#separator:tab\n#html:true\n#columns:Hanzi\tSentenceAudio\n')
 csv.writer(f,delimiter='\t').writerows(rows)
print(path.name,len(rows),'mappings; no new audio or example text')
