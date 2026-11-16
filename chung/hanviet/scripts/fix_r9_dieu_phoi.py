# Điều phối: quyết định cuối sau R5 -> 06_review/fixes_r9_dieu_phoi.tsv (dòng gốc = dòng mới nhất của note_key trong out + fixes theo thứ tự merge)
import sys, csv, glob, os
sys.stdout.reconfigure(encoding="utf-8")
H = ["note_key","hanviet","nghia_vi","loai","tu_viet","khac_biet","pt_kieu","pt_noi_dung","status","review_reason","char_note"]
latest = {}; hvpre = {}
import json
for l in open("02_chars/item_hv.jsonl", encoding="utf-8"):
    d = json.loads(l); hvpre[d["note_key"]] = d["hv_pre"]
for f in sorted(glob.glob("04_draft/out/*.tsv")):
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
        if r["hanviet"] == "=": r["hanviet"] = hvpre[r["note_key"]]
        latest[r["note_key"]] = r
for f in sorted(glob.glob("06_review/fixes_*.tsv")):
    if "fixes_r9" in f: continue
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"): latest[r["note_key"]] = r
D = {
 "zh:hskstory-hsk7:1792758609232": dict(hanviet="LÕA THỂ", nghia_vi="khỏa thân, trần truồng",
     char_note="裸=lõa (âm Hán Việt thông dụng, có trong nguồn hvpinyin; từ Việt 'lõa thể'). Cùng chữ còn đọc khỏa như trong 'khỏa thân' (điều phối r9)"),
 "zh:hskstory-hsk6:1792758601920": dict(loai="ghep_nghia", tu_viet="", pt_kieu="goi_nho",
     pt_noi_dung="未成年 vị thành niên + 人 nhân (người); tiếng Việt nói 'người vị thành niên' (điều phối r9: từ Việt đảo/rút gọn, quy tắc L6)"),
}
with open("06_review/fixes_r9_dieu_phoi.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(H + ["reviewer"])
    for k, ch in D.items():
        r = {h: (latest[k].get(h) or "") for h in H}; r.update(ch); w.writerow([r[h] for h in H] + ["opus:dieu_phoi_r9"])
        print(k, r["hanviet"], r["loai"], r["tu_viet"], r["pt_noi_dung"][:60])
