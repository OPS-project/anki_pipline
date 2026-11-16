# Điều phối: lọc có mục tiêu cho lượt rà cuối R5 (chạy trên bản merge sau R4).
# L1: loai ∈ {ghep_nghia,yeu_to,khong_giup} mà âm HV cả từ (≥2 chữ) xuất hiện trong nghia_vi  -> có thể cung_dung bị đánh thấp
# L2: thành ngữ 4 chữ loai=ghep_nghia ở các lô có tỷ lệ cung_dung 4 chữ thấp (<15%)           -> thành ngữ quen bị đánh thấp
# L3: pt_noi_dung có mẫu "<chữ của từ> <âm>" mà âm khác âm HV đã chọn của chữ đó               -> phân tích ghi nghĩa Việt như âm
# L4: danh sách điều phối: chữ 幻/推/腻/量 (sau R1), từ khóa "vốn", "phục tòng", "nghĩa gốc", "bắt nguồn", 打量
# L5: các note_key nêu trong r3_phan_tich_toan_cuc.md (thành ngữ nhóm B/C, cặp mâu thuẫn, từ nguyên)
# L6: tu_viet khác âm HV cả từ (cung_dung/khac_dung), không có ghi chú "từ Việt đọc"
import sys, json, csv, glob, os, re, collections, argparse
sys.stdout.reconfigure(encoding="utf-8"); sys.path.insert(0, "scripts")
from hv_common import reading_key
ap = argparse.ArgumentParser(); ap.add_argument("--merged", required=True); ap.add_argument("--outdir", required=True); a = ap.parse_args()
items = [json.loads(l) for l in open(a.merged, encoding="utf-8")]
ctx = {}
for f in glob.glob("04_draft/input/*.tsv"):
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"): ctx[r["note_key"]] = r
def low(s): return re.sub(r"\s+", " ", s.lower()).strip()
CJK = re.compile(r"[\u3400-\u9fff]")
# tỷ lệ cung_dung 4 chữ theo lô
four = collections.defaultdict(lambda: [0, 0])
# "lô thấp" tính theo bản soạn gốc (merged_v1), không theo bản đã sửa
for l in open("07_final/merged_v1.jsonl", encoding="utf-8"):
    d0 = json.loads(l)
    if len(CJK.findall(d0["hanzi"])) == 4:
        b = d0.get("drafted_by", ""); four[b][1] += 1; four[b][0] += d0.get("loai") == "cung_dung"
lowbatches = {b for b, (c, n) in four.items() if n >= 5 and c / n < 0.15}
# mục đã có reviewer xem (log R2/R4) thì không đưa vào L2
reviewed = set()
for f in glob.glob("06_review/log_r[24]_*.tsv"):
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"): reviewed.add(r["note_key"])
r3keys = set(re.findall(r"zh:hskstory-hsk[0-9]+:\d+", open("06_review/r3_phan_tich_toan_cuc.md", encoding="utf-8").read()))
sel = collections.defaultdict(set)
for d in items:
    k = d["note_key"]; hv = low(d.get("hanviet", "")); nv = low(d.get("nghia_vi", "")); loai = d.get("loai")
    pt = (d.get("phan_tich") or {}).get("noi_dung", "")
    nch = len(CJK.findall(d["hanzi"]))
    if loai in ("ghep_nghia", "yeu_to", "khong_giup") and nch >= 2 and "?" not in hv and hv and hv in nv: sel[k].add("L1")
    if nch == 4 and loai == "ghep_nghia" and d.get("drafted_by") in lowbatches and k not in reviewed: sel[k].add("L2")
    chosen = {c["char"]: c.get("hv", "") for c in d.get("hanviet_chars", [])}
    for m in re.finditer(r"([\u3400-\u9fff])\s+([^\s\(\)\+\→,;:'\"“”]+)", pt):
        ch, w = m.group(1), m.group(2)
        if ch in chosen and chosen[ch] and re.match(r"^[a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]+$", w.lower()):
            if reading_key(w) != reading_key(chosen[ch]): pass  # L3 bỏ (kiểu trình bày); xem CHECKPOINT
            break
    txt = " ".join([pt, d.get("khac_biet", ""), d.get("nghia_vi", "")])
    if any(c in d["hanzi"] for c in "幻推腻") or d["hanzi"] == "打量" or re.search(r"vốn |phục tòng|nghĩa gốc|bắt nguồn|có gốc", txt): sel[k].add("L4")
    if k in r3keys: sel[k].add("L5")
    # L6: tu_viet khác âm HV cả từ (cung_dung/khac_dung), trừ khi char_note đã ghi "từ Việt đọc"
    tv = low(d.get("tu_viet", ""))
    notes_all = " ".join(c.get("note", "") for c in d.get("hanviet_chars", []))
    if loai in ("cung_dung", "khac_dung") and tv and hv and tv != hv and "từ Việt đọc" not in notes_all and "Việt hóa" not in notes_all: sel[k].add("L6")
cols = ["note_key","flags","level","hanzi","word_pinyin","meaning_en","sentence","sentence_en","hanviet","nghia_vi","loai","tu_viet","khac_biet","pt_kieu","pt_noi_dung","status","review_reason","char_note","drafted_by"]
os.makedirs(a.outdir, exist_ok=True)
rows = []
for d in items:
    k = d["note_key"]
    if k not in sel: continue
    c = ctx[k]; pt = d.get("phan_tich") or {}
    notes = "; ".join(f'{x["char"]}: {x["note"]}' for x in d.get("hanviet_chars", []) if x.get("note"))
    rows.append({"note_key": k, "flags": ",".join(sorted(sel[k])), "level": d["level"], "hanzi": d["hanzi"], "word_pinyin": d["word_pinyin"],
                 "meaning_en": c["meaning_en"], "sentence": c["sentence"], "sentence_en": c["sentence_en"], "hanviet": d.get("hanviet", ""),
                 "nghia_vi": d.get("nghia_vi", ""), "loai": d.get("loai", ""), "tu_viet": d.get("tu_viet", ""), "khac_biet": d.get("khac_biet", ""),
                 "pt_kieu": pt.get("kieu", ""), "pt_noi_dung": pt.get("noi_dung", ""), "status": d.get("status", ""),
                 "review_reason": d.get("review_reason", ""), "char_note": notes, "drafted_by": d.get("drafted_by", "")})
size = 450; n = (len(rows) + size - 1) // size
for i in range(n):
    with open(f"{a.outdir}/set_r5_{i+1:02d}.tsv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, cols, delimiter="\t", lineterminator="\n"); w.writeheader()
        for r in rows[i*size:(i+1)*size]: w.writerow({kk: (v or "").replace("\t", " ").replace("\n", " ") for kk, v in r.items()})
cnt = collections.Counter(f for s in sel.values() for f in s)
print("selected", len(rows), "files", n, dict(cnt), "lowbatches", sorted(lowbatches))
