# Điều phối: bỏ khẳng định từ nguyên không nguồn trong 11 dòng goi_nho của fixes_r1 -> fixes_r1b_wording.tsv
import sys, csv, re
sys.stdout.reconfigure(encoding="utf-8")
rows = list(csv.DictReader(open("06_review/fixes_r1_doc_am.tsv", encoding="utf-8"), delimiter="\t"))
H = list(rows[0].keys())
pat = re.compile(r"'([^']+)' trong tiếng Việt có gốc từ chữ này")
out = []
for r in rows:
    if pat.search(r["pt_noi_dung"]):
        r = dict(r)
        r["pt_noi_dung"] = pat.sub(r"gợi nhớ: âm gần với từ Việt '\1' (liên tưởng, không khẳng định từ nguyên)", r["pt_noi_dung"])
        r["pt_kieu"] = "goi_nho"
        r["reviewer"] = "opus:dieu_phoi_r1b"
        out.append(r)
with open("06_review/fixes_r1b_wording.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(H)
    for r in out: w.writerow([r[h] for h in H])
print(len(out)); [print(r["note_key"], r["pt_noi_dung"]) for r in out[:3]]
