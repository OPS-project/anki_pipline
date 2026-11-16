"""Tạo bộ dữ liệu bàn giao cuối (hanviet_10898.jsonl/.tsv, needs_review.tsv, stats.json/.md).

Chạy (từ thư mục hanviet):
  python -I scripts/finalize.py [--outdir 07_final] [--tmp <thư mục tạm>]
Xem scripts/README_finalize.md.
"""
import sys, os, re, json, glob, csv, argparse, subprocess, collections, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
from hv_common import reading_key
from validate_drafts import read_tsv, load_jsonl, OUT_COLS, FIX_COLS, CJK, LOAI, STATUS, BOSUNG_DEFAULT, load_cands_bosung, apply_cands_bosung

ROOT = os.path.dirname(HERE)
LABEL = "bản nháp AI"
EXPECT = 10898
KEY_ONLY = re.compile(r"^[a-zâăêôơưđ]+\d(\s*,\s*[a-zâăêôơưđ]+\d)+$", re.I)


def P(*a):
    return os.path.join(ROOT, *a)


def run(args):
    r = subprocess.run([sys.executable, "-I"] + args, cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        sys.exit(f"LỖI khi chạy {args[0]}: {r.stdout}\n{r.stderr}")
    return r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ""


def tsv_rows(path):
    header, rows, derr = read_tsv(path)
    if derr:
        sys.exit(f"{path}: không giải mã UTF-8")
    if header is None:
        return []
    return [dict(zip(header, r)) for _, r in rows if len(r) == len(header)]


def is_junk(seg):
    return "hvpinyin nhiều âm" in seg or "lọc theo Thiều Chửu còn" in seg or bool(KEY_ONLY.match(seg.strip()))


def split_outside(s):
    """Tách theo '; ' hoặc ' | ' nhưng không tách bên trong cặp ngoặc ( ) [ ]."""
    parts, cur, depth, i = [], "", 0, 0
    while i < len(s):
        ch = s[i]
        if ch in "([（": depth += 1
        elif ch in ")]）": depth = max(0, depth - 1)
        if depth == 0 and (s.startswith("; ", i) or s.startswith(" | ", i)):
            parts.append(cur); cur = ""; i += 2 if s.startswith("; ", i) else 3; continue
        cur += ch; i += 1
    parts.append(cur)
    return parts


def clean_note(s, counter):
    segs = [x.strip() for x in split_outside(s) if x.strip()]
    out = []; seen_body = set()
    for x in segs:
        # điều phối: so trùng theo NỘI DUNG sau khi bỏ tiền tố "chữ: " (merge nhiều vòng nhân bản "X: note" cho từng chữ)
        body = re.sub(r"^[㐀-鿿]{1,4}\s*:\s*", "", x).strip()
        if is_junk(x):
            counter["junk"] += 1
        elif x in out or body in seen_body:
            counter["dup"] += 1
        else:
            out.append(x); seen_body.add(body)
    return "; ".join(out)


def round_of_fix(fn):
    m = re.match(r"fixes_(r\d+[a-z]?)[_.]", fn)
    return m.group(1) if m else fn


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default=P("07_final"))
    ap.add_argument("--tmp")
    ap.add_argument("--cands-bosung", default=BOSUNG_DEFAULT, help="file ứng viên bổ sung có nguồn (tùy chọn; chỉ dùng nếu tồn tại)")
    a = ap.parse_args()
    tmp = a.tmp or tempfile.mkdtemp(prefix="finalize_")
    os.makedirs(tmp, exist_ok=True)
    os.makedirs(a.outdir, exist_ok=True)

    items_p, hv_p = P("00_base", "items.jsonl"), P("02_chars", "item_hv.jsonl")
    base = ["scripts/merge_drafts.py", "--items", items_p, "--item-hv", hv_p, "--outs", P("04_draft", "out"),
            "--fixes", P("06_review"), "--drafted-by-map", P("05_validate", "drafted_by_map.json"),
            "--expect", str(EXPECT)]
    if os.path.exists(a.cands_bosung):
        base += ["--cands-bosung", a.cands_bosung]
    m1, tf, m2 = (os.path.join(tmp, n) for n in ("merged1.jsonl", "tone_flags_final.jsonl", "merged2.jsonl"))
    print("[1] merge:", run(base + ["--out", m1]))
    run(["scripts/tone_flags.py", "--item-hv", m1, "--rules", P("03_tone", "tone_rule_table.csv"), "--out", tf])
    print("[1] merge+tone:", run(base + ["--tone-flags", tf, "--out", m2]))

    items = load_jsonl(items_p)
    item_hv = {x["note_key"]: x for x in load_jsonl(hv_p)}
    apply_cands_bosung(item_hv, load_cands_bosung(a.cands_bosung))
    recs = load_jsonl(m2)

    # char_note: dòng mới nhất (out, rồi fixes theo tên file)
    latest = {}
    for p in sorted(glob.glob(P("04_draft", "out", "*.tsv"))):
        for r in tsv_rows(p):
            latest[r["note_key"]] = r.get("char_note", "")
    fix_changed = collections.defaultdict(set)
    fix_by_reviewer = collections.defaultdict(set)
    for p in sorted(glob.glob(P("06_review", "fixes_*.tsv"))):
        fn = os.path.basename(p)
        for r in tsv_rows(p):
            latest[r["note_key"]] = r.get("char_note", "")
            fix_changed[round_of_fix(fn)].add(r["note_key"])
            fix_by_reviewer[r.get("reviewer", "?")].add(r["note_key"])

    # reviewed_in
    reviewed = collections.defaultdict(list)
    for p in sorted(glob.glob(P("06_review", "log_r*_*.tsv"))):
        m = re.match(r"log_(r\d+)_(.+)\.tsv$", os.path.basename(p))
        if not m:
            continue
        tag = f"{m.group(1)}:{m.group(2)}"
        for r in tsv_rows(p):
            k = r.get("note_key")
            if k and tag not in reviewed[k]:
                reviewed[k].append(tag)
    r1p = P("06_review", "fixes_r1_doc_am.tsv")
    if os.path.exists(r1p):
        for r in tsv_rows(r1p):
            if "r1" not in reviewed[r["note_key"]]:
                reviewed[r["note_key"]].insert(0, "r1")

    # tone_flags: merge bỏ cờ khi mục có fix bất kỳ; tone_flags.py đã chạy trên bản merge nên cờ luôn khớp âm hiện tại
    tfl = {x["note_key"]: x.get("tone_flags") for x in load_jsonl(tf)}
    cnt = collections.Counter()
    recovered = 0
    for rec in recs:
        k = rec["note_key"]
        raw = latest.get(k, "")
        cn = clean_note(raw, cnt) if raw.strip() else ""
        if cn:
            rec["char_note"] = cn
            cnt["items_with_char_note"] += 1
            if not any(c.get("note") for c in rec.get("hanviet_chars", [])):
                recovered += 1
        if tfl.get(k):
            rec["tone_flags"] = tfl[k]
        else:
            rec.pop("tone_flags", None)
        rec["label"] = LABEL
        rec["reviewed_in"] = reviewed.get(k, [])

    # R6: chữ được Opus quyết needs_review -> certainty "uncertain" (không đổi gì khác)
    qd = P("06_review", "r6", "quyet_dinh_am.json")
    if os.path.exists(qd):
        unc = set()
        for ch in json.load(open(qd, encoding="utf-8")).get("chars", []):
            for t in ch.get("theo_tu", []):
                if t.get("status") == "needs_review":
                    unc.add((t["note_key"], ch["char"]))
        n_unc = 0
        for rec in recs:
            for c in rec.get("hanviet_chars", []):
                if (rec["note_key"], c.get("char")) in unc and c.get("certainty") != "uncertain":
                    c["certainty"] = "uncertain"; n_unc += 1
        print("certainty=uncertain (R6):", n_unc, "chữ /", len(unc), "cặp")
    # tone_flags chỉ cho chữ certainty sure/chosen (TIEU_CHUAN mục 3); áp sau bước uncertain
    n_tf = 0
    for rec in recs:
        tfs = rec.get("tone_flags")
        if not tfs: continue
        ok = {c.get("char") for c in rec.get("hanviet_chars", []) if c.get("certainty") in ("sure", "chosen")}
        keep = [t for t in tfs if t.get("char") in ok]
        if len(keep) != len(tfs):
            n_tf += 1
            if keep: rec["tone_flags"] = keep
            else: rec.pop("tone_flags", None)
    print("mục bỏ cờ thanh của chữ không chắc:", n_tf)

    # kiểm cuối
    errs = []
    if len(recs) != EXPECT:
        errs.append(f"số dòng {len(recs)} != {EXPECT}")
    if [r["note_key"] for r in recs] != [it["note_key"] for it in items]:
        errs.append("thứ tự/tập note_key khác items.jsonl")
    if len({r["note_key"] for r in recs}) != len(recs):
        errs.append("note_key trùng")
    for r in recs:
        k = r["note_key"]
        n_cjk = len(CJK.findall(r["hanzi"]))
        toks = r["hanviet"].split()
        if len(toks) != n_cjk:
            errs.append(f"{k}: số âm {len(toks)} != số chữ {n_cjk}")
        iv = item_hv.get(k)
        chars = r.get("hanviet_chars", [])
        if len(chars) != n_cjk:
            errs.append(f"{k}: hanviet_chars {len(chars)} != {n_cjk}")
        for i, c in enumerate(chars):
            hv = c.get("hv")
            if not hv or hv == "?":
                continue
            cands = iv["chars"][i].get("cands", []) if iv and i < len(iv["chars"]) else []
            if reading_key(hv) not in {reading_key(cd.get("reading", "")) for cd in cands}:
                errs.append(f"{k}: âm {hv!r} (chữ {c.get('char')}) ngoài cands")
        if r.get("loai") is not None and r["loai"] not in LOAI:
            errs.append(f"{k}: loai {r.get('loai')!r}")
        if r.get("status") not in STATUS:
            errs.append(f"{k}: status {r.get('status')!r}")
    if errs:
        print(f"KIỂM CUỐI THẤT BẠI: {len(errs)} lỗi", file=sys.stderr)
        for e in errs[:50]:
            print("  " + e, file=sys.stderr)
        sys.exit(1)

    # xuất
    out = lambda n: os.path.join(a.outdir, n)
    with open(out("hanviet_10898.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    def tone_str(r):
        return " ".join(f"{t['char']}:{t['actual_in_word']}→{t['predicted']}"
                        for t in r.get("tone_flags", []) if t.get("flag") == "ngoai_le")

    cols = ["note_key", "level", "anki_guid", "hanzi", "word_pinyin", "hanviet", "nghia_vi", "loai", "tu_viet",
            "khac_biet", "pt_kieu", "pt_noi_dung", "char_note", "tone_ngoai_le", "status", "review_reason",
            "drafted_by", "reviewed_in", "label"]

    def flat(r):
        pt = r.get("phan_tich", {})
        d = dict(r)
        d.update(pt_kieu=pt.get("kieu", ""), pt_noi_dung=pt.get("noi_dung", ""), tone_ngoai_le=tone_str(r),
                 reviewed_in=",".join(r.get("reviewed_in", [])))
        return [str(d.get(c, "")).replace("\t", " ").replace("\n", " ").replace("\r", " ") for c in cols]

    def writer(f):
        return csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, quotechar=None)

    with open(out("hanviet_10898.tsv"), "w", encoding="utf-8-sig", newline="") as f:
        w = writer(f)
        w.writerow(cols)
        for r in recs:
            w.writerow(flat(r))
    nr = [r for r in recs if r["status"] == "needs_review"]
    with open(out("needs_review.tsv"), "w", encoding="utf-8-sig", newline="") as f:
        w = writer(f)
        w.writerow(["note_key", "level", "hanzi", "hanviet", "nghia_vi", "review_reason"])
        for r in nr:
            w.writerow([str(x).replace("\t", " ").replace("\n", " ") for x in
                        (r["note_key"], r.get("level", ""), r["hanzi"], r["hanviet"], r.get("nghia_vi", ""),
                         r.get("review_reason", ""))])

    # stats
    C = collections.Counter
    by_round = C()
    cover_any = 0
    for r in recs:
        rs = r["reviewed_in"]
        if rs:
            cover_any += 1
        for rd in {x.split(":")[0] for x in rs}:
            by_round[rd] += 1
    st = {
        "tong": len(recs),
        "theo_loai": dict(C(r.get("loai", "(không)") for r in recs)),
        "theo_status": dict(C(r["status"] for r in recs)),
        "theo_level": dict(C(r.get("level", "?") for r in recs)),
        "co_phan_tich": sum(1 for r in recs if r.get("phan_tich")),
        "co_tone_flag_ngoai_le": sum(1 for r in recs if tone_str(r)),
        "co_char_note": cnt["items_with_char_note"],
        "char_note_khoi_phuc": recovered,
        "doan_rac_da_don": cnt["junk"],
        "doan_trung_da_bo": cnt["dup"],
        "do_phu_review": {"it_nhat_mot_vong": cover_any, "khong_vong_nao": len(recs) - cover_any,
                          "theo_vong": dict(sorted(by_round.items()))},
        "drafted_by": dict(C(r.get("drafted_by", "(không)") for r in recs).most_common()),
        "so_muc_sua_theo_vong": {k: len(v) for k, v in sorted(fix_changed.items())},
        "so_muc_sua_theo_reviewer": {k: len(v) for k, v in sorted(fix_by_reviewer.items())},
        "luu_y": "Được kiểm (reviewed_in) khác với đã xác minh. Mọi mục là bản nháp AI.",
    }
    with open(out("stats.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(st, f, ensure_ascii=False, indent=1)
    L = ["# Thống kê bộ dữ liệu Hán Việt HSK", "", f"Tổng: {st['tong']} mục (nhãn: {LABEL}).", ""]

    def tbl(title, d):
        L.extend([f"## {title}", "", "| Mục | Số |", "|---|---|"] + [f"| {k} | {v} |" for k, v in d.items()] + [""])
    tbl("Theo loại", st["theo_loai"])
    tbl("Theo status", st["theo_status"])
    tbl("Theo level", st["theo_level"])
    tbl("Một số chỉ số", {"có phân tích": st["co_phan_tich"], "có cờ thanh ngoại lệ": st["co_tone_flag_ngoai_le"],
                          "có char_note": st["co_char_note"], "char_note khôi phục (merge làm mất)": recovered,
                          "đoạn rác đã dọn": cnt["junk"], "đoạn trùng đã bỏ": cnt["dup"]})
    tbl("Độ phủ review (mục được kiểm, không phải đã xác minh)",
        {"ít nhất một vòng": cover_any, "không vòng nào": len(recs) - cover_any,
         **{f"vòng {k}": v for k, v in sorted(by_round.items())}})
    tbl("Số mục được sửa theo vòng (fixes_*.tsv)", st["so_muc_sua_theo_vong"])
    tbl("Số mục được sửa theo reviewer", st["so_muc_sua_theo_reviewer"])
    tbl("Phân bố drafted_by", st["drafted_by"])
    with open(out("stats.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L))
    print(json.dumps({k: st[k] for k in ("tong", "theo_loai", "theo_status", "co_phan_tich", "co_tone_flag_ngoai_le",
                                         "co_char_note", "char_note_khoi_phuc", "doan_rac_da_don", "doan_trung_da_bo",
                                         "do_phu_review", "so_muc_sua_theo_vong")}, ensure_ascii=False, indent=1))
    print(f"OK -> {a.outdir}; needs_review={len(nr)}")


if __name__ == "__main__":
    main()
