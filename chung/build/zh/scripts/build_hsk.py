# Build "Tiếng Trung HSK" listen-first deck from HSKStory HSK1–9 (read-only on sources).
# Usage: python -I build_hsk.py
import sys, os, re, json, zipfile, sqlite3, hashlib, html
sys.stdout.reconfigure(encoding="utf-8")
PROJ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../.."))
SCRATCH = os.environ.get("ANKI_WORK", PROJ + "/.work")  # thư mục tạm + thư viện (pip --target), không đưa lên git
sys.path.insert(0, SCRATCH + "/pylib")
import genanki

SRC = PROJ + "/research/downloads"
OUT = PROJ + "/chung/build/zh"
WORK = SCRATCH + "/work/build-zh"
MEDIA = WORK + "/media"
os.makedirs(OUT, exist_ok=True); os.makedirs(MEDIA, exist_ok=True)

# --- Bản 2 (16/11): khối Hán Việt vào trường Notes (không thêm trường). Tắt bằng HANVIET="" ---
HANVIET = os.environ.get("HANVIET", PROJ + "/chung/hanviet/07_final/hanviet_10898.jsonl")
OUT_NAME = os.environ.get("OUT_NAME", "Tieng_Trung_HSK_nghe_cau_v2_hanviet.apkg")
LOAI_LABEL = {"cung_dung": "cùng dùng", "khac_dung": "khác dùng", "ghep_nghia": "ghép nghĩa", "yeu_to": "yếu tố",
              "phien_am": "phiên âm", "ten_rieng": "tên riêng"}  # khong_giup, hu_tu: ẩn nhãn
HV = {}
if HANVIET:
    for _l in open(HANVIET, encoding="utf-8"):
        _d = json.loads(_l); HV[_d["note_key"]] = _d

def hv_notes(d):
    """HTML cho trường Notes. Không hiển thị tone_flags (tạm ẩn ở bản đầu)."""
    e = html.escape
    tag = LOAI_LABEL.get(d.get("loai", ""))
    line = f'<div class="hv-line"><b>{e(d.get("hanviet", ""))}</b> · {e(d.get("nghia_vi", ""))}'
    if tag: line += f' <span class="hv-tag hv-{e(d["loai"])}">{tag}</span>'
    line += "</div>"
    more = []
    pt = d.get("phan_tich") or {}
    if pt.get("noi_dung"):
        more.append(f'<div>{"Cấu tạo" if pt.get("kieu") == "cau_tao" else "Gợi nhớ"}: {e(pt["noi_dung"])}</div>')
    if d.get("tu_viet"): more.append(f'<div>Từ Việt: {e(d["tu_viet"])}</div>')
    if d.get("khac_biet"): more.append(f'<div>Khác biệt: {e(d["khac_biet"])}</div>')
    if d.get("char_note"): more.append(f'<div>Ghi chú âm: {e(d["char_note"])}</div>')
    if d.get("status") == "needs_review":
        more.append(f'<div class="hv-open">Chưa chắc: {e(d.get("review_reason", ""))}</div>')
    more.append(f'<div class="hv-label">{e(d.get("label", "bản nháp AI"))}</div>')
    return (f'<div class="hv">{line}<details class="hv-more"><summary>Hán Việt: chi tiết</summary>'
            + "".join(more) + "</details></div>")

PARENT = "Tiếng Trung HSK"
LEVELS = [(1, "HSK1", 100), (2, "HSK2", 100), (3, "HSK3", 100), (4, "HSK4", 100),
          (5, "HSK5", 100), (6, "HSK6", 100), (7, "HSK7-9", 200)]

def rv(b, i):
    r = s = 0
    while True:
        c = b[i]; i += 1; r |= (c & 0x7F) << s; s += 7
        if not c & 0x80: return r, i

def open_apkg(path, tag):
    z = zipfile.ZipFile(path); names = z.namelist()
    for c in ("collection.anki21b", "collection.anki21", "collection.anki2"):
        if c in names:
            d = z.read(c)
            if c.endswith("b"):
                from compression import zstd; d = zstd.decompress(d)
            p = f"{WORK}/{tag}.sqlite"; open(p, "wb").write(d)
            break
    raw = z.read("media")
    try:
        mm = json.loads(raw)
    except Exception:
        from compression import zstd
        raw = zstd.decompress(raw); mm = {}; i = 0; idx = 0
        while i < len(raw):
            _, i = rv(raw, i); l, i = rv(raw, i); sub = raw[i:i + l]; i += l
            j = 0; name = None
            while j < len(sub):
                kk, j = rv(sub, j)
                if kk & 7 == 2:
                    ll, j = rv(sub, j); v = sub[j:j + ll]; j += ll
                    if kk >> 3 == 1: name = v.decode()
                else: _, j = rv(sub, j)
            mm[str(idx)] = name; idx += 1
    inv = {v: k for k, v in mm.items()}
    return z, sqlite3.connect(p), inv

def field_names(db):
    try:
        out = {}
        for ntid, o, nm in db.execute("select ntid,ord,name from fields order by ntid,ord"):
            out.setdefault(ntid, []).append(nm)
        return out
    except Exception:
        m = json.loads(db.execute("select models from col").fetchone()[0])
        return {int(k): [f["name"] for f in sorted(v["flds"], key=lambda f: f["ord"])] for k, v in m.items()}

TONE = {}
for t, chars in enumerate(["āēīōūǖĀĒĪŌŪǕ", "áéíóúǘÁÉÍÓÚǗ", "ǎěǐǒǔǚǍĚǏǑǓǙ", "àèìòùǜÀÈÌÒÙǛ"], 1):
    for ch in chars: TONE[ch] = t
def tone_of(syl):
    for ch in syl:
        if ch in TONE: return TONE[ch]
    return 5
def color_pinyin(p):
    p = html.unescape(re.sub(r"<[^>]+>", "", p)).strip()
    out = []
    for tok in p.split():
        m = re.match(r"^([^A-Za-zÀ-ɏ]*)([A-Za-zÀ-ɏüÜ']+)(.*)$", tok)
        if not m: out.append(html.escape(tok)); continue
        pre, syl, post = m.groups()
        out.append(f'{html.escape(pre)}<span class="tone-{tone_of(syl)}">{html.escape(syl)}</span>{html.escape(post)}')
    return " ".join(out)

src_attr = re.compile(r'src="([^"]+)"')
def strip_tags(s): return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()

def media_name(level, nid, kind, data, ext):
    h = hashlib.sha256(data).hexdigest()[:8]
    return f"cdt_zh_hskstory-hsk{level}_{nid}_{kind}_{h}{ext}"

def stable_id(s, lo=1 << 30, hi=1 << 31):
    return lo + int(hashlib.sha1(s.encode()).hexdigest(), 16) % (hi - lo)

FIELDS = ["NoteKey", "Sentence", "Reading", "Pinyin", "Audio", "Image", "Translation", "TranslationStatus",
          "SourceSubtitle", "SourceSubtitleLabel", "ContextBefore", "ContextAfter", "Speaker", "TargetWords",
          "LinkKey", "Notes", "SourceType", "SourceTitle", "SourceID", "SourceURL", "Episode", "Start", "End",
          "VoiceType", "QAStatus", "TargetAudio"]

CSS = open(os.path.join(os.path.dirname(__file__), "cau_nghe_v1.css"), encoding="utf-8").read()
QFMT = open(os.path.join(os.path.dirname(__file__), "front.html"), encoding="utf-8").read()
AFMT = open(os.path.join(os.path.dirname(__file__), "back.html"), encoding="utf-8").read()

model = genanki.Model(
    stable_id("model:Câu nghe v1"), "Câu nghe v1",
    fields=[{"name": f} for f in FIELDS],
    templates=[{"name": "Nghe", "qfmt": QFMT, "afmt": AFMT}],
    css=CSS, sort_field_index=1)

class Note(genanki.Note):
    @property
    def guid(self): return genanki.guid_for(self.fields[0])

decks = {}
def deck(name, desc=""):
    if name not in decks:
        decks[name] = genanki.Deck(stable_id("deck:" + name), name, description=desc)
    return decks[name]

PARENT_DESC = ("<b>Học từ deck này</b> để Anki tự đi lần lượt: 00 Phát âm → HSK1 Phần 01 → Phần 02 → … "
               "Mỗi thẻ: nghe câu trước, cố hiểu và nói lại theo; lật mặt sau để xem chữ, pinyin, nghĩa và từ mục tiêu.")
deck(PARENT, PARENT_DESC)

manifest = []; media_files = []; problems = []; total = 0; summary = []
for level, lname, chunk in LEVELS:
    z, db, inv = open_apkg(f"{SRC}/hskstory{level}.apkg", f"hsk{level}")
    fl = field_names(db)
    rows = db.execute("select id, mid, flds from notes order by id").fetchall()
    deck(f"{PARENT}::{lname}", f"HSKStory {lname}: {len(rows)} từ, mỗi từ một câu ví dụ có audio.")
    nparts = (len(rows) + chunk - 1) // chunk
    for idx, (nid, mid, flds) in enumerate(rows):
        f = dict(zip(fl[mid], flds.split("\x1f")))
        sent_files = src_attr.findall(f.get("StoryTitle", ""))
        word_files = src_attr.findall(f.get("Audio", ""))
        if not sent_files or not f.get("ExampleHanzi", "").strip():
            problems.append({"level": level, "nid": nid, "hanzi": f.get("Hanzi"), "issue": "no sentence/audio"}); continue
        def grab(fname, kind):
            key = inv.get(fname)
            if key is None:
                problems.append({"level": level, "nid": nid, "hanzi": f.get("Hanzi"), "issue": f"missing media {fname}"}); return None, None
            data = z.read(key); ext = os.path.splitext(fname)[1] or ".mp3"
            out = media_name(level, nid, kind, data, ext); p = f"{MEDIA}/{out}"
            if not os.path.exists(p): open(p, "wb").write(data)
            media_files.append(p)
            return out, hashlib.sha256(data).hexdigest()
        s_out, s_hash = grab(sent_files[0], "s")
        if not s_out: continue
        w_out, w_hash = grab(word_files[0], "w") if word_files else (None, None)
        sentence = re.sub(r'class="tone tone-(\d)"', r'class="target tone-\1"', f["ExampleHanzi"]).strip()
        hanzi = f["Hanzi"].strip(); pin_word = strip_tags(f.get("TonePinyin", ""))
        target = (f'<span class="tw-hanzi">{f.get("ToneHanzi", hanzi)}</span> '
                  f'<span class="tw-pinyin">{f.get("TonePinyin", "")}</span> '
                  f'<span class="tw-meaning">{f.get("Meaning", "")}</span>')
        part = idx // chunk + 1
        lo, hi = (part - 1) * chunk + 1, min(part * chunk, len(rows))
        dname = f"{PARENT}::{lname}::Phần {part:02d} (từ {lo}–{hi})"
        key = f"zh:hskstory-hsk{level}:{nid}"
        values = {
            "NoteKey": key, "Sentence": sentence, "Pinyin": color_pinyin(f.get("ExamplePinyin", "")),
            "Audio": f"[sound:{s_out}]", "Translation": "", "TranslationStatus": "unverified:source:HSKStory(EN)",
            "SourceSubtitle": f.get("ExampleEnglish", "").strip(), "SourceSubtitleLabel": "EN · HSKStory",
            "TargetWords": target, "LinkKey": f"zh:hsk{level}:{hanzi}:{pin_word}",
            "SourceType": "HSKStory", "SourceTitle": f"HSKStory {lname}", "SourceID": f"hskstory-hsk{level}",
            "SourceURL": f"https://hskstory.com/anki/hsk-{level if level < 7 else '7-9'}", "Episode": lname,
            "VoiceType": "unknown", "QAStatus": "NeedsListeningQA",
            "TargetAudio": f"[sound:{w_out}]" if w_out else ""}
        tags = ["hskstory", lname.lower().replace("-", "_"), f"cdt::zh"]
        if HV:
            hvd = HV.get(key)
            if hvd is None:
                problems.append({"level": level, "nid": nid, "hanzi": hanzi, "issue": "thiếu dữ liệu Hán Việt"})
            else:
                values["Notes"] = hv_notes(hvd)
                tags.append("hanviet::draft")
                if hvd.get("status") == "needs_review": tags.append("hanviet::needs_review")
        note = Note(model=model, fields=[values.get(k, "") for k in FIELDS], tags=tags)
        deck(dname).add_note(note); total += 1
        manifest.append({"NoteKey": key, "source_package": {"file": f"research/downloads/hskstory{level}.apkg"},
                         "source_note_ids": [nid], "source_media": [{"file": sent_files[0], "sha256": s_hash}] +
                         ([{"file": word_files[0], "sha256": w_hash}] if w_out else []),
                         "operation": "copy", "output": {"sentence": s_out, "word": w_out},
                         "voice_type": "unknown", "deck": dname})
    summary.append((lname, len(rows), nparts))
    print(f"{lname}: {len(rows)} notes -> {nparts} phần")

pkg = genanki.Package(list(decks.values()))
pkg.media_files = sorted(set(media_files))
out_apkg = f"{OUT}/{OUT_NAME}"
pkg.write_to_file(out_apkg)
man_name = "manifest_hskstory.json" if OUT_NAME == "Tieng_Trung_HSK_nghe_cau.apkg" else f"manifest_{OUT_NAME[:-5]}.json"
json.dump({"built_by": "Claude", "spec": "chung/spec/cau_nghe_v1.md", "hanviet": HANVIET or None, "notes": total,
           "summary": summary, "problems": problems, "items": manifest},
          open(f"{OUT}/{man_name}", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("TOTAL notes", total, "media", len(set(media_files)), "problems", len(problems))
for p in problems[:20]: print("  !", p)
print("->", out_apkg, os.path.getsize(out_apkg))
