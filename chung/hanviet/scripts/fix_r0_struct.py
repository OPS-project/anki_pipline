# Điều phối: sửa lỗi cấu trúc sau validator v1 -> 06_review/fixes_r0_struct.tsv (không sửa file soạn)
import sys, json, csv, glob, os
sys.stdout.reconfigure(encoding="utf-8")
H = ["note_key","hanviet","nghia_vi","loai","tu_viet","khac_biet","pt_kieu","pt_noi_dung","status","review_reason","char_note"]
issues = [json.loads(l) for l in open("05_validate/issues_v1.jsonl", encoding="utf-8")]
need = {}
for d in issues:
    if d["level"] == "error": need.setdefault(d["note_key"], set()).add(d["code"])
rows = {}
for f in glob.glob("04_draft/out/*.tsv"):
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
        if r["note_key"] in need: rows[r["note_key"]] = r
out = []
for k, codes in need.items():
    r = dict(rows[k])
    if "E_TU_VIET_LOAI" in codes and r["tu_viet"]:
        tv = r["tu_viet"]; r["tu_viet"] = ""
        if not r["pt_noi_dung"]:
            r["pt_kieu"] = "goi_nho"; r["pt_noi_dung"] = f"như trong: {tv}"
        elif tv not in r["pt_noi_dung"]:
            r["pt_noi_dung"] = r["pt_noi_dung"] + f"; như trong: {tv}"
    if "E_HV_COUNT" in codes or "E_HV_NOT_IN_CANDS" in codes:
        # 方便面: âm có nguồn PHƯƠNG TIỆN MIẾN; 'mì' là từ Việt gốc từ 麵
        r["hanviet"] = "PHƯƠNG TIỆN MIẾN"
        r["loai"] = "ghep_nghia"; r["tu_viet"] = ""
        r["pt_kieu"] = "goi_nho"; r["pt_noi_dung"] = "方便 phương tiện (tiện lợi) + 面 miến (mì; 'mì' tiếng Việt bắt nguồn từ chữ này) → mì tiện lợi"
        r["char_note"] = "面=miến (âm Hán Việt có nguồn); 'mì' không phải âm Hán Việt trong nguồn"
    out.append(r)
with open("06_review/fixes_r0_struct.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(H + ["reviewer"])
    for r in out: w.writerow([r[h] for h in H] + ["opus:dieu_phoi_r0"])
print(len(out), "fixes")
for r in out: print(r["note_key"], r["hanviet"], r["loai"], r["pt_noi_dung"][:70])
