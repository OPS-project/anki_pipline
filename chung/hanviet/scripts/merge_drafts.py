"""Hợp nhất items.jsonl + item_hv.jsonl + bản soạn (TSV) + bản sửa review -> JSON cuối (TIEU_CHUAN mục 1-3).

Chạy (từ thư mục hanviet):
  python -I scripts/merge_drafts.py --items 00_base/items.jsonl --item-hv 02_chars/item_hv.jsonl
      --outs 04_draft/out [--fixes 06_review] [--tone-flags 05_validate/tone_flags.jsonl]
      [--drafted-by-map map.json] [--default-model sonnet] [--expect 10898]
      --out 07_final/hanviet_10898.jsonl
Không bao giờ ghi đè đầu vào (từ chối nếu --out trùng một file đầu vào). Thoát mã 2 nếu số dòng != --expect,
hoặc nếu có lỗi cấu trúc (header/cột sai, note_key trùng giữa các out, fix cho note_key lạ).
"""
import sys, os, re, json, glob, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
from hv_common import reading_key, display
from validate_drafts import read_tsv, load_jsonl, OUT_COLS, FIX_COLS, CJK, BOSUNG_DEFAULT, load_cands_bosung, apply_cands_bosung

FIELDS = OUT_COLS[1:]


def die(msg):
    print("LỖI: " + msg, file=sys.stderr)
    sys.exit(2)


def read_rows(path, cols, optional=()):
    header, rows, derr = read_tsv(path)
    if derr:
        die(f"{path}: không giải mã UTF-8 ({derr})")
    if header is None:
        return []
    if header[:len(cols)] != cols or any(h not in optional for h in header[len(cols):]):
        die(f"{path}: header sai: {header}")
    out = []
    for ln, row in rows:
        if len(row) != len(header):
            die(f"{path} dòng {ln}: {len(row)} cột, cần {len(header)}")
        out.append(dict(zip(header, row)))
    return out


def build_chars(it_hv, row, hanzi, forced):
    """Trả (hanviet_str, hanviet_chars, changed:bool). forced: list lý do ép needs_review."""
    hv = row["hanviet"].strip() if row else "="
    chars_in = it_hv.get("chars") if it_hv else None
    if chars_in is None:
        n = len(CJK.findall(hanzi))
        chars_in = [{"char": c, "cands": [], "chosen": None, "certainty": "none"} for c in CJK.findall(hanzi)]
        if it_hv is None:
            forced.append("thiếu item_hv")
    toks = None if hv == "=" else hv.split()
    if toks is not None and len(toks) != len(chars_in):
        forced.append(f"số âm ({len(toks)}) khác số chữ ({len(chars_in)})")
    char_note = (row or {}).get("char_note", "").strip()
    out, changed = [], False
    for i, c in enumerate(chars_in):
        ch = c.get("char")
        cands = c.get("cands", [])
        chosen, cert, note = c.get("chosen"), c.get("certainty") or "none", None
        srcs = None
        cand = None
        if chosen:
            cand = next((cd for cd in cands if reading_key(cd.get("reading", "")) == reading_key(chosen)), None)
        if toks is not None and i < len(toks):
            t = toks[i]
            if t == "?":
                if chosen:
                    changed = True
                chosen, cert, cand = None, ("uncertain" if cands else "none"), None
            elif not chosen or reading_key(t) != reading_key(chosen):
                changed = True
                cand = next((cd for cd in cands if reading_key(cd.get("reading", "")) == reading_key(t)), None)
                if cand is not None:
                    chosen, cert, note = cand["reading"], "chosen", char_note or None
                else:
                    chosen, cert, note = t, "none", None
                    forced.append(f"âm {t!r} ngoài hv_cands")
        e = {"char": ch}
        if chosen:
            e["hv"] = display(chosen)
        if cand is not None and cand.get("sources"):
            e["source"] = ",".join(cand["sources"])
        via = None
        if cand is not None:
            via = cand.get("via")
        if via is None:
            trad = c.get("trad") or []
            via = trad[0] if len(trad) == 1 else (ch if not trad else None)
        if via and chosen:
            e["via"] = via
        e["certainty"] = cert
        e["_orig_cert"] = c.get("certainty")
        e["_changed_note"] = note
        e["_reason"] = c.get("reason")
        out.append(e)
    # ghi chú
    chosen_idx = [i for i, e in enumerate(out) if e["certainty"] == "chosen"]
    for e in out:
        if e["_changed_note"]:
            e["note"] = e["_changed_note"]
        elif e["certainty"] == "chosen" and e["_reason"]:
            e["note"] = e["_reason"]
    if char_note and not any(e.get("_changed_note") for e in out):
        for i in chosen_idx:
            out[i]["note"] = char_note
    for e in out:
        for k in ("_orig_cert", "_changed_note", "_reason"):
            e.pop(k, None)
    if hv == "=":
        hv_str = (it_hv or {}).get("hv_pre") or " ".join("?" for _ in chars_in)
    else:
        hv_str = " ".join(t.upper() for t in toks)
    return hv_str, out, changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", required=True)
    ap.add_argument("--item-hv", required=True)
    ap.add_argument("--outs", required=True)
    ap.add_argument("--fixes")
    ap.add_argument("--tone-flags")
    ap.add_argument("--drafted-by-map")
    ap.add_argument("--default-model", default="sonnet")
    ap.add_argument("--expect", type=int, default=10898)
    ap.add_argument("--cands-bosung", default=BOSUNG_DEFAULT, help="file ứng viên bổ sung có nguồn (tùy chọn)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    inputs = [a.items, a.item_hv] + glob.glob(os.path.join(a.outs, "*"))
    if a.fixes:
        inputs += glob.glob(os.path.join(a.fixes, "*"))
    if a.tone_flags:
        inputs.append(a.tone_flags)
    if a.drafted_by_map:
        inputs.append(a.drafted_by_map)
    inputs.append(a.cands_bosung)
    norm = lambda p: os.path.normcase(os.path.abspath(p))
    if norm(a.out) in {norm(p) for p in inputs}:
        die("--out trùng một file đầu vào; từ chối ghi đè")

    items = load_jsonl(a.items)
    item_hv = {x["note_key"]: x for x in load_jsonl(a.item_hv)} if os.path.exists(a.item_hv) else {}
    apply_cands_bosung(item_hv, load_cands_bosung(a.cands_bosung))
    if not item_hv:
        print("[cảnh báo] không có item_hv; chars sẽ rỗng và mọi mục thành needs_review", file=sys.stderr)
    tflags = {}
    if a.tone_flags:
        for x in load_jsonl(a.tone_flags):
            if x.get("tone_flags"):
                tflags[x["note_key"]] = x["tone_flags"]
    dmap = json.load(open(a.drafted_by_map, encoding="utf-8")) if a.drafted_by_map else {}
    item_set = {x["note_key"] for x in items}

    # bản soạn
    rows, src_file, extra_drafted = {}, {}, {}
    for p in sorted(glob.glob(os.path.join(a.outs, "*.tsv"))):
        fn = os.path.basename(p)
        for r in read_rows(p, OUT_COLS, optional=("drafted_by",)):
            k = r["note_key"]
            if k in rows:
                die(f"note_key trùng giữa các out: {k} ({src_file[k]} và {fn})")
            if k not in item_set:
                die(f"note_key không có trong items.jsonl: {k} ({fn})")
            rows[k], src_file[k] = r, fn
            if r.get("drafted_by", "").strip():
                extra_drafted[k] = r["drafted_by"].strip()

    # bản sửa
    history = collections.defaultdict(list)
    reviewed_by = {}
    changed_by_fix = set()
    fix_files = sorted(glob.glob(os.path.join(a.fixes, "fixes_*.tsv"))) if a.fixes and os.path.isdir(a.fixes) else []
    for p in fix_files:
        fn = os.path.basename(p)
        seen = set()
        for r in read_rows(p, FIX_COLS):
            k = r["note_key"]
            if k not in item_set:
                die(f"fix cho note_key lạ: {k} ({fn})")
            if k in seen:
                die(f"note_key trùng trong {fn}: {k}")
            seen.add(k)
            old = rows.get(k)
            diff = {f: old[f] for f in FIELDS if old is not None and old[f] != r[f]} if old else {f: "" for f in FIELDS if r[f]}
            history[k].append({"file": fn, "reviewer": r["reviewer"], "old": diff})
            reviewed_by[k] = r["reviewer"]
            if diff:
                changed_by_fix.add(k)
            new = {f: r[f] for f in OUT_COLS}
            rows[k] = new
            src_file.setdefault(k, fn)

    result, n_missing, n_dropped_tf = [], 0, 0
    for it in items:
        k = it["note_key"]
        row = rows.get(k)
        iv = item_hv.get(k)
        forced = []
        hv_str, hv_chars, changed = build_chars(iv, row, it["hanzi"], forced)
        rec = {"note_key": k, "hanzi": it["hanzi"], "word_pinyin": it.get("word_pinyin"), "hanviet": hv_str,
               "hanviet_chars": hv_chars}
        status = "needs_review"
        reasons = []
        if row is None:
            n_missing += 1
            reasons.append("thiếu bản soạn")
        else:
            for f in ("nghia_vi", "loai", "tu_viet", "khac_biet"):
                if row[f].strip():
                    rec[f] = row[f].strip()
            if row["pt_kieu"].strip() or row["pt_noi_dung"].strip():
                rec["phan_tich"] = {x: row[y].strip() for x, y in (("kieu", "pt_kieu"), ("noi_dung", "pt_noi_dung")) if row[y].strip()}
            status = row["status"].strip() or "needs_review"
            if row["review_reason"].strip():
                reasons.append(row["review_reason"].strip())
        if iv is not None and "?" in hv_str.split() and status != "needs_review":
            forced.append("hanviet còn '?'")
        if forced:
            status = "needs_review"
            reasons.extend(forced)
        rec["status"] = status
        if status == "needs_review":
            rec["review_reason"] = "; ".join(dict.fromkeys(reasons)) or "không rõ lý do"
        if row is not None:
            sf = src_file.get(k, "")
            dm = dmap.get(sf) or dmap.get(re.sub(r"(?<=\d)[A-Za-z]+(?=\.tsv$)", "", sf)) or extra_drafted.get(k)
            if not dm and k in src_file and not src_file[k].startswith("fixes_"):
                stem = re.sub(r"(?<=\d)[a-z]+$", "", os.path.splitext(src_file[k])[0])
                dm = f"{a.default_model}:{stem}"
            if dm:
                rec["drafted_by"] = dm
        for f in ("level", "anki_guid", "anki_note_id", "source_note_id"):
            if it.get(f) not in (None, ""):
                rec[f] = it[f]
        if k in tflags:
            if changed or k in changed_by_fix:
                n_dropped_tf += 1
            else:
                rec["tone_flags"] = tflags[k]
        if k in reviewed_by:
            rec["reviewed_by"] = reviewed_by[k]
            rec["history"] = history[k]
        result.append({kk: v for kk, v in rec.items() if v not in (None, "", [], {})})

    if len(result) != a.expect:
        die(f"số dòng {len(result)} khác {a.expect}")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    tmp = a.out + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        for r in result:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, a.out)
    st = collections.Counter(r["status"] for r in result)
    print(f"đã ghi {len(result)} dòng -> {a.out}; thiếu bản soạn={n_missing}; status={dict(st)}; "
          f"fix áp={len(reviewed_by)}; tone_flags bỏ vì âm đổi={n_dropped_tf}")


if __name__ == "__main__":
    main()
