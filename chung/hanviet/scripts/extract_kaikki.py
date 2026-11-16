"""Trích 'descendants' tiếng Việt (lang_code vi) của mục chữ Hán (pos=character) trong dump kaikki.
Usage: python -I -X utf8 extract_kaikki.py <kaikki_jsonl> <out_json>
"""
import sys, json, collections
src, out = sys.argv[1], sys.argv[2]
res = collections.defaultdict(list); n = 0; chars = 0; bad = 0
def walk(ds, acc):
    for d in ds or []:
        if d.get('lang_code') == 'vi' and d.get('word'):
            acc.append((d['word'], d.get('raw_tags') or []))
        walk(d.get('descendants'), acc)
with open(src, encoding='utf8') as f:
    for l in f:
        try: e = json.loads(l)
        except Exception: bad += 1; continue
        n += 1
        w = e.get('word', '')
        if e.get('pos') != 'character' or len(w) != 1: continue
        chars += 1
        acc = []
        walk(e.get('descendants'), acc)
        for rd, tags in acc:
            if 'borrowed' in tags or not tags:
                res[w].append([rd, None])
json.dump(res, open(out, 'w', encoding='utf8'), ensure_ascii=False)
print('entries', n, 'bad', bad, 'character entries', chars, 'with vi', len(res))
