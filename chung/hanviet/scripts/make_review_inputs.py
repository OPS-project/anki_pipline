"""Tạo TSV đầu vào cho pha review ngữ nghĩa từ JSON hợp nhất (không review nội dung).

Chạy (từ thư mục hanviet):
  python -I scripts/make_review_inputs.py --merged <merged.jsonl> --inputs 04_draft/input --outdir <thư mục> [--seed 20261116] [--split N]
Tập (không chồng nhau, ưu tiên theo thứ tự): set_hard, set_needs, set_khac, set_sample. Ghi manifest.json vào outdir.
"""
import sys, os, re, json, glob, math, random, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")

CTX = ["level", "hanzi", "word_pinyin", "meaning_en", "sentence", "sentence_en", "hv_cands", "cv_vi", "ce_en", "tc_char"]
CUR = ["hanviet", "nghia_vi", "loai", "tu_viet", "khac_biet", "pt_kieu", "pt_noi_dung", "status", "review_reason",
       "char_note", "drafted_by"]
COLS = ["note_key"] + CTX + CUR


def clean(s):
    return re.sub(r"[\t\r\n]+", " ", str(s if s is not None else "")).strip()


def read_input(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    hdr = lines[0].rstrip("\r").split("\t")
    out = {}
    for ln in lines[1:]:
        ln = ln.rstrip("\r")
        if not ln:
            continue
        row = ln.split("\t")
        row += [""] * (len(hdr) - len(row))
        out[row[0]] = dict(zip(hdr, row))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--merged", required=True)
    ap.add_argument("--inputs", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--seed", type=int, default=20261116)
    ap.add_argument("--split", type=int, default=0, help="chia mỗi tập thành file <=N dòng")
    a = ap.parse_args()

    with open(a.merged, encoding="utf-8") as f:
        merged = [json.loads(l) for l in f if l.strip()]
    ctx, hard_keys = {}, set()
    for p in sorted(glob.glob(os.path.join(a.inputs, "*.tsv"))):
        d = read_input(p)
        ctx.update(d)
        if os.path.basename(p).startswith("hard_"):
            hard_keys.update(d)
    missing_ctx = sum(1 for m in merged if m["note_key"] not in ctx)

    taken = set()
    sets = collections.OrderedDict()
    sets["set_hard"] = [m for m in merged if m["note_key"] in hard_keys]
    taken |= {m["note_key"] for m in sets["set_hard"]}
    sets["set_needs"] = [m for m in merged if m["note_key"] not in taken and m.get("status") == "needs_review"]
    taken |= {m["note_key"] for m in sets["set_needs"]}
    sets["set_khac"] = [m for m in merged if m["note_key"] not in taken and m.get("loai") == "khac_dung"]
    taken |= {m["note_key"] for m in sets["set_khac"]}

    rest = [m for m in merged if m["note_key"] not in taken]
    cells = collections.defaultdict(list)
    for m in rest:
        cells[(m.get("level", ""), m.get("loai", ""))].append(m)
    sample, cell_rows = set(), []
    for (lv, lo), ms in sorted(cells.items()):
        ms = sorted(ms, key=lambda m: m["note_key"])
        k = min(len(ms), max(3, math.ceil(0.05 * len(ms))))
        rng = random.Random(f"{a.seed}:{lv}:{lo}")
        pick = {m["note_key"] for m in rng.sample(ms, k)}
        extra = 0
        if lo in ("phien_am", "ten_rieng"):
            pick = {m["note_key"] for m in ms}
            extra = len(pick) - k
        sample |= pick
        cell_rows.append((lv, lo, len(ms), k, len(pick), extra))
    sets["set_sample"] = [m for m in rest if m["note_key"] in sample]

    def row_of(m):
        c = ctx.get(m["note_key"], {})
        pa = m.get("phan_tich") or {}
        notes = "; ".join(f"{h['char']}: {h['note']}" for h in m.get("hanviet_chars", []) if h.get("note"))
        cur = {"hanviet": m.get("hanviet", ""), "nghia_vi": m.get("nghia_vi", ""), "loai": m.get("loai", ""),
               "tu_viet": m.get("tu_viet", ""), "khac_biet": m.get("khac_biet", ""), "pt_kieu": pa.get("kieu", ""),
               "pt_noi_dung": pa.get("noi_dung", ""), "status": m.get("status", ""),
               "review_reason": m.get("review_reason", ""), "char_note": notes, "drafted_by": m.get("drafted_by", "")}
        ctxv = [clean(c.get(k) or (m.get(k, "") if k in ("level", "hanzi", "word_pinyin") else "")) for k in CTX]
        return "\t".join([m["note_key"]] + ctxv + [clean(cur[k]) for k in CUR])

    os.makedirs(a.outdir, exist_ok=True)
    manifest = {"seed": a.seed, "columns": COLS, "split": a.split, "sets": {}, "files": {}}
    for name, ms in sets.items():
        manifest["sets"][name] = [m["note_key"] for m in ms]
        chunks = [ms[i:i + a.split] for i in range(0, len(ms), a.split)] if a.split else [ms]
        files = []
        for i, ch in enumerate(chunks, 1):
            if not ch:
                continue
            fn = f"{name}_{i:02d}.tsv" if a.split else f"{name}.tsv"
            with open(os.path.join(a.outdir, fn), "w", encoding="utf-8", newline="\n") as f:
                f.write("\t".join(COLS) + "\n")
                for m in ch:
                    f.write(row_of(m) + "\n")
            files.append(fn)
        manifest["files"][name] = files
    with open(os.path.join(a.outdir, "manifest.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)

    tot = sum(len(v) for v in sets.values())
    print(f"seed={a.seed}; tổng mục merged={len(merged)}; thiếu ngữ cảnh input={missing_ctx}")
    for n, ms in sets.items():
        print(f"  {n}: {len(ms)}")
    print(f"  tổng 4 tập: {tot} (phần còn lại không review: {len(merged) - tot})")
    print("Ô mẫu (level, loai): còn lại | lấy phân tầng | tổng vào mẫu | thêm do phien_am/ten_rieng")
    for lv, lo, n, k, p, ex in cell_rows:
        print(f"  {lv or '-'}\t{lo or '-'}\t{n}\t{k}\t{p}\t{ex}")


if __name__ == "__main__":
    main()
