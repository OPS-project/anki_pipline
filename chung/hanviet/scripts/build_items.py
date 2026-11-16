"""Trích 00_base/items.jsonl + chars.txt từ apkg đã build, đối chiếu với research/inspection.
Chạy: python -I build_items.py ROOT WORKDIR   (ROOT = thư mục 'Anki Search')"""
import sys, os, re, json, zipfile, sqlite3, html, collections, hashlib
sys.stdout.reconfigure(encoding="utf-8")
ROOT, WORK = sys.argv[1], sys.argv[2]
APKG = f"{ROOT}/chung/build/zh/Tieng_Trung_HSK_nghe_cau.apkg"
MAN = f"{ROOT}/chung/build/zh/manifest_hskstory.json"
OUT = f"{ROOT}/chung/hanviet/00_base"
os.makedirs(WORK, exist_ok=True)
with zipfile.ZipFile(APKG) as z:
    z.extract("collection.anki2", WORK)
db = sqlite3.connect(f"{WORK}/collection.anki2")
FN = "NoteKey Sentence Reading Pinyin Audio Image Translation TranslationStatus SourceSubtitle SourceSubtitleLabel ContextBefore ContextAfter Speaker TargetWords LinkKey Notes SourceType SourceTitle SourceID SourceURL Episode Start End VoiceType QAStatus TargetAudio".split()
notes = {}
for nid, guid, flds in db.execute("select id,guid,flds from notes"):
    f = dict(zip(FN, flds.split("\x1f")))
    notes[f["NoteKey"]] = (nid, guid, f)
def txt(s):
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()
def span(s, cls):
    # TargetWords có span lồng nhau: lấy từ <span class="cls"> tới <span class="tw-..."> kế tiếp (hoặc hết chuỗi)
    parts = re.split(r'(?=<span class="tw-(?:hanzi|pinyin|meaning)">)', s)
    return [p for p in parts if p.startswith('<span class="%s">' % cls)]
man = json.load(open(MAN, encoding="utf-8"))
LV = {"1":"HSK1","2":"HSK2","3":"HSK3","4":"HSK4","5":"HSK5","6":"HSK6","7":"HSK7-9"}
src = {}
for i in range(1, 8):
    for n in json.load(open(f"{ROOT}/research/inspection/hskstory{i}/notes.json", encoding="utf-8")):
        src[(i, n["id"])] = n["fields"]
rows, issues = [], collections.defaultdict(list)
for it in man["items"]:
    k = it["NoteKey"]
    if k not in notes: issues["note_missing_in_apkg"].append(k); continue
    nid, guid, f = notes[k]
    ids = it["source_note_ids"]
    if len(ids) != 1: issues["multi_source_ids"].append(k)
    tw = f["TargetWords"]
    hz = txt(" ".join(span(tw, "tw-hanzi")))
    py = txt(" ".join(span(tw, "tw-pinyin")))
    mean = txt(" ".join(span(tw, "tw-meaning")))
    ep = f["Episode"].strip()
    m = re.search(r"(\d)", ep)
    level = (f["Episode"] if f["Episode"] in LV.values() else None)
    if level is None:
        level = {"1":"HSK1"}.get(ep)  # fallback below
    rows.append(dict(note_key=k, anki_guid=guid, anki_note_id=nid, source_note_id=ids[0], level=ep,
        hanzi=hz, word_pinyin=py, meaning_en=mean, sentence=txt(f["Sentence"]),
        target_in_sentence="".join(re.findall(r'<span class="target[^"]*">(.*?)</span>', f["Sentence"], flags=re.S)).replace("<","") ,
        sentence_pinyin=txt(f["Pinyin"]), sentence_en=txt(f["SourceSubtitle"]), deck=it["deck"]))
for r in rows:
    r["target_in_sentence"] = txt(r["target_in_sentence"])
with open(f"{OUT}/items.jsonl", "w", encoding="utf-8", newline="\n") as fo:
    for r in rows: fo.write(json.dumps(r, ensure_ascii=False) + "\n")
print("rows", len(rows), "levels", collections.Counter(r["level"] for r in rows))
# cross-check
lvnum = {v:int(k) for k,v in LV.items()}
mis = collections.defaultdict(list); nosrc = []
for r in rows:
    key = (lvnum.get(r["level"]), r["source_note_id"])
    s = src.get(key)
    if not s: nosrc.append(r["note_key"]); continue
    if txt(s["Hanzi"]) != r["hanzi"]: mis["hanzi"].append((r["note_key"], txt(s["Hanzi"]), r["hanzi"]))
    if txt(s["Meaning"]) != r["meaning_en"]: mis["meaning"].append((r["note_key"], txt(s["Meaning"]), r["meaning_en"]))
    if txt(s["ExampleHanzi"]) != r["sentence"]: mis["example"].append((r["note_key"], txt(s["ExampleHanzi"]), r["sentence"]))
    if txt(s.get("TonePinyin","")) != r["word_pinyin"]: mis["pinyin"].append((r["note_key"], txt(s.get("TonePinyin","")), r["word_pinyin"]))
    if txt(s.get("ExamplePinyin","")) != r["sentence_pinyin"]: mis["ex_pinyin"].append((r["note_key"], txt(s.get("ExamplePinyin","")), r["sentence_pinyin"]))
    if txt(s.get("ExampleEnglish","")) != r["sentence_en"]: mis["ex_en"].append((r["note_key"], txt(s.get("ExampleEnglish","")), r["sentence_en"]))
print("no source match", len(nosrc), nosrc[:5])
for k, v in mis.items(): print("MISMATCH", k, len(v), v[:3])
# checks
print("unique note_key", len({r['note_key'] for r in rows}), "unique guid", len({r['anki_guid'] for r in rows}), "unique nid", len({r['anki_note_id'] for r in rows}))
print("notes in apkg", len(notes), "issues", {k: len(v) for k, v in issues.items()})
byh = collections.defaultdict(list)
for r in rows: byh[r["hanzi"]].append(r)
dup = {h: v for h, v in byh.items() if len(v) > 1}
print("hanzi in >1 item:", len(dup), "items", sum(len(v) for v in dup.values()))
with open(f"{WORK}/dup_hanzi.tsv", "w", encoding="utf-8") as fo:
    for h, v in sorted(dup.items()):
        fo.write(h + "\t" + " | ".join(f"{r['level']}:{r['word_pinyin']}:{r['meaning_en']}" for r in v) + "\n")
diff = [r for r in rows if r["target_in_sentence"] != r["hanzi"]]
empt = [r for r in rows if not r["target_in_sentence"]]
print("target!=hanzi", len(diff), "empty target", len(empt))
with open(f"{WORK}/target_diff.tsv", "w", encoding="utf-8") as fo:
    for r in diff: fo.write(f"{r['note_key']}\t{r['level']}\t{r['hanzi']}\t{r['target_in_sentence']}\t{r['sentence']}\n")
# chars
def cjk(c):
    o = ord(c); return 0x3400 <= o <= 0x9FFF or 0xF900 <= o <= 0xFAFF or o >= 0x20000
order = list(LV.values()); cnt = collections.Counter(); first = {}
for r in rows:
    for c in set(r["hanzi"]):
        if cjk(c):
            cnt[c] += 1
            if c not in first or order.index(r["level"]) < order.index(first[c]): first[c] = r["level"]
with open(f"{OUT}/chars.txt", "w", encoding="utf-8", newline="\n") as fo:
    for c in sorted(cnt, key=lambda c: (order.index(first[c]), -cnt[c], c)):
        fo.write(f"{c}\t{first[c]}\t{cnt[c]}\n")
print("chars", len(cnt), collections.Counter(first.values()))
noncjk = collections.Counter(c for r in rows for c in r["hanzi"] if not cjk(c))
print("non-CJK chars in hanzi", dict(noncjk))
