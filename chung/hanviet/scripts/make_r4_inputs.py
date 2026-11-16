# Điều phối: tập R4 = mọi mục loai=cung_dung chưa thuộc tập review nào và không bị R1 sửa -> 06_review/inputs_r4/set_cd_NN.tsv
import sys, json, csv, glob, os, math
sys.stdout.reconfigure(encoding="utf-8")
man = json.load(open("06_review/inputs/manifest.json", encoding="utf-8"))
reviewed = set()
for v in man["sets"].values():
    reviewed |= set(v if isinstance(v, list) else v.get("note_keys", []))
r1 = {r["note_key"] for r in csv.DictReader(open("06_review/fixes_r1_doc_am.tsv", encoding="utf-8"), delimiter="\t")}
ctx = {}
for f in glob.glob("04_draft/input/*.tsv"):
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"): ctx[r["note_key"]] = r
cols = ["note_key","level","hanzi","word_pinyin","meaning_en","sentence","sentence_en","hanviet","nghia_vi","loai","tu_viet","khac_biet","pt_kieu","pt_noi_dung","status","review_reason","char_note","drafted_by"]
rows = []
for l in open("07_final/merged_v2.jsonl", encoding="utf-8"):
    d = json.loads(l); k = d["note_key"]
    if d.get("loai") != "cung_dung" or k in reviewed or k in r1: continue
    c = ctx[k]; pt = d.get("phan_tich") or {}
    notes = "; ".join(f'{x["char"]}: {x["note"]}' for x in d.get("hanviet_chars", []) if x.get("note"))
    rows.append({"note_key": k, "level": d["level"], "hanzi": d["hanzi"], "word_pinyin": d["word_pinyin"], "meaning_en": c["meaning_en"],
                 "sentence": c["sentence"], "sentence_en": c["sentence_en"], "hanviet": d.get("hanviet",""), "nghia_vi": d.get("nghia_vi",""),
                 "loai": d.get("loai",""), "tu_viet": d.get("tu_viet",""), "khac_biet": d.get("khac_biet",""), "pt_kieu": pt.get("kieu",""),
                 "pt_noi_dung": pt.get("noi_dung",""), "status": d.get("status",""), "review_reason": d.get("review_reason",""),
                 "char_note": notes, "drafted_by": d.get("drafted_by","")})
os.makedirs("06_review/inputs_r4", exist_ok=True)
n = math.ceil(len(rows) / 490); size = math.ceil(len(rows) / n)
for i in range(n):
    with open(f"06_review/inputs_r4/set_cd_{i+1:02d}.tsv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, cols, delimiter="\t", lineterminator="\n"); w.writeheader()
        for r in rows[i*size:(i+1)*size]: w.writerow({k: (v or "").replace("\t"," ").replace("\n"," ") for k, v in r.items()})
print(len(rows), "rows ->", n, "files of", size)
