# R6: áp quyết định âm của Opus (06_review/r6/quyet_dinh_am.json) -> 06_review/fixes_r6_doc_am.tsv
# Người áp: Sonnet; nội dung quyết định: Opus (reviewer ghi opus:r6_quyet_dinh_am).
# Đọc/ghi TSV cùng cơ chế với merge/validate (tách theo \n và \t, không bọc/bỏ ngoặc kép).
import sys, re, glob, json
sys.stdout.reconfigure(encoding="utf-8")
H = ["note_key","hanviet","nghia_vi","loai","tu_viet","khac_biet","pt_kieu","pt_noi_dung","status","review_reason","char_note"]


def rows(f):
    lines = open(f, encoding="utf-8-sig").read().split("\n")
    hd = lines[0].rstrip("\r").split("\t")
    for l in lines[1:]:
        l = l.rstrip("\r")
        if l:
            yield dict(zip(hd, l.split("\t")))


hvpre = {}
for l in open("02_chars/item_hv.jsonl", encoding="utf-8"):
    d = json.loads(l); hvpre[d["note_key"]] = d["hv_pre"]
latest = {}
for f in sorted(glob.glob("04_draft/out/*.tsv")):
    for r in rows(f):
        if r["hanviet"] == "=": r["hanviet"] = hvpre[r["note_key"]]
        latest[r["note_key"]] = r
for f in sorted(glob.glob("06_review/fixes_*.tsv")):
    if "fixes_r6" in f: continue
    for r in rows(f): latest[r["note_key"]] = r
Q = json.load(open("06_review/r6/quyet_dinh_am.json", encoding="utf-8"))
MAP = {"hanviet_moi":"hanviet","char_note":"char_note","pt_noi_dung_moi":"pt_noi_dung","khac_biet_moi":"khac_biet",
       "tu_viet_moi":"tu_viet","loai_moi":"loai","status":"status","review_reason":"review_reason"}
per = {}
order = []
for c in Q["chars"]:
    for t in c.get("theo_tu", []):
        if t["note_key"] not in per: order.append(t["note_key"])
        per.setdefault(t["note_key"], []).append((c["char"], t))
n_doi = n_note = n_nr = 0
TAB = chr(9); NL = chr(10)
def clean(c): return re.sub(r"[\t\r\n]+", " ", c)
with open("06_review/fixes_r6_doc_am.tsv", "w", encoding="utf-8", newline="") as f:
    def wr(cells): f.write(TAB.join(clean(c) for c in cells) + NL)
    wr(H + ["reviewer"])
    for k in order:
        r = {h: (latest[k].get(h) or "") for h in H}
        old_hv = r["hanviet"]
        hvs = {t["hanviet_moi"] for _, t in per[k] if t.get("hanviet_moi")}
        assert len(hvs) <= 1, (k, hvs)
        for field, col in MAP.items():
            vals = [t[field] for _, t in per[k] if t.get(field) not in (None, "")]
            if not vals: continue
            if field in ("char_note", "review_reason"):
                seen = []
                for v in vals:
                    if v not in seen: seen.append(v)
                r[col] = "; ".join(seen)
            elif field == "status":
                r[col] = "needs_review" if "needs_review" in vals else vals[0]
            else:
                r[col] = vals[0]
        if any(t.get("status") == "needs_review" for _, t in per[k]): n_nr += 1
        elif any(t.get("chi_sua_char_note") for _, t in per[k]) and r["hanviet"] == old_hv: n_note += 1
        else: n_doi += 1
        wr([r[h] for h in H] + ["opus:r6_quyet_dinh_am"])
print("dòng", len(order), "doi", n_doi, "chi_sua_ghi_chu", n_note, "needs_review", n_nr)
