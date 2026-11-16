"""Kiểm bản soạn Hán Việt (TSV 11 cột) so với đầu vào, items.jsonl và item_hv.jsonl.

Chạy (từ thư mục hanviet):
  python -I scripts/validate_drafts.py --inputs 04_draft/input --outs 04_draft/out [--fixes 06_review]
      --items 00_base/items.jsonl --item-hv 02_chars/item_hv.jsonl
      --report 05_validate/report.md --json 05_validate/issues.jsonl
Mã thoát: 1 nếu có lỗi (level=error), 0 nếu chỉ có cảnh báo hoặc sạch.
Không ghi gì ngoài --report và --json.
"""
import sys, os, re, json, glob, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
from hv_common import reading_key

OUT_COLS = ["note_key", "hanviet", "nghia_vi", "loai", "tu_viet", "khac_biet", "pt_kieu",
            "pt_noi_dung", "status", "review_reason", "char_note"]
FIX_COLS = OUT_COLS + ["reviewer"]
LOAI = {"cung_dung", "khac_dung", "ghep_nghia", "hu_tu", "phien_am", "ten_rieng", "khong_giup", "yeu_to"}
STATUS = {"draft", "needs_review"}
PT_KIEU = {"cau_tao", "goi_nho", ""}
CJK = re.compile(r"[㐀-䶿一-鿿豈-﫿\U00020000-\U0002fa1f]")
ENGLISH = re.compile(r"(?<![^\W\d_])(?:[A-Za-z]{2,}[ ]+){2,}[A-Za-z]{2,}(?![^\W\d_])")
NULLS = {"null", "none", "nan"}


def read_tsv(path):
    """Trả (header|None, [(số_dòng, cells)], lỗi_decode|None). Tách dòng chỉ theo \\n."""
    raw = open(path, "rb").read()
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as e:
        return None, [], str(e)
    lines = [l[:-1] if l.endswith("\r") else l for l in text.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    if not lines:
        return None, [], None
    return lines[0].split("\t"), [(i + 2, l.split("\t")) for i, l in enumerate(lines[1:]) if l != ""], None


def load_jsonl(path):
    out = []
    for l in open(path, encoding="utf-8"):
        l = l.strip()
        if l:
            out.append(json.loads(l))
    return out


BOSUNG_DEFAULT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "02_chars", "cands_bosung.jsonl")
BOSUNG_SOURCES = {"thieuchuu", "hvpinyin", "unihan", "unihan_kVietnamese", "wiktionary", "kaikki", "cedict", "cvdict", "opencc"}


def load_cands_bosung(path):
    """Đọc 02_chars/cands_bosung.jsonl tùy chọn: mỗi dòng {"char","reading","source","evidence"}.
    source: ID nguồn trong SOURCES.md hoặc "wiktionary_web:<url>". Trả {char: [cand dict]} (rỗng nếu không có file).
    Lỗi định dạng -> SystemExit."""
    res = {}
    if not path or not os.path.exists(path):
        return res
    for ln, l in enumerate(open(path, encoding="utf-8"), 1):
        l = l.strip()
        if not l:
            continue
        x = json.loads(l)
        for f in ("char", "reading", "source", "evidence"):
            if not str(x.get(f, "")).strip():
                sys.exit(f"LỖI {path} dòng {ln}: thiếu trường {f}")
        src = x["source"].strip()
        if not (src in BOSUNG_SOURCES or src.startswith("wiktionary_web:http")):
            sys.exit(f"LỖI {path} dòng {ln}: source không hợp lệ: {src!r}")
        cd = {"reading": x["reading"].strip(), "key": reading_key(x["reading"]),
              "sources": [src], "evidence": x["evidence"].strip()}
        if str(x.get("via", "")).strip():
            cd["via"] = x["via"].strip()  # tùy chọn: chữ gốc có mục nguồn (merge dùng cho hanviet_chars.via)
        res.setdefault(x["char"], []).append(cd)
    return res


def apply_cands_bosung(item_hv, bosung):
    """Thêm ứng viên bổ sung vào cands (tại chỗ) của mọi chữ khớp; bỏ qua (char, reading_key) đã có. Trả số lần thêm."""
    n = 0
    if not bosung:
        return n
    for iv in item_hv.values():
        for c in iv.get("chars", []):
            for b in bosung.get(c.get("char"), []):
                if reading_key(b["reading"]) not in {reading_key(cd.get("reading", "")) for cd in c.setdefault("cands", [])}:
                    c["cands"].append(dict(b))
                    n += 1
    return n


def parse_hv_cands(s):
    """'手:thủ|机→機:cơ,ki' -> [[thủ],[cơ,ki]] (theo vị trí chữ)."""
    res = []
    if not s:
        return res
    for part in s.split("|"):
        _, _, rd = part.partition(":")
        res.append([r.strip() for r in rd.split(",") if r.strip()])
    return res


class Issues:
    def __init__(self):
        self.rows = []

    def add(self, level, note_key, file, code, detail):
        self.rows.append({"note_key": note_key, "file": file, "code": code, "level": level, "detail": detail})

    def err(self, *a):
        self.add("error", *a)

    def warn(self, *a):
        self.add("warn", *a)


def check_row(r, inp, cand_keys, iss, fname):
    """r: dict cột; inp: dict dòng đầu vào hoặc None; cand_keys: list[set]|None."""
    k = r["note_key"]
    E = lambda code, d: iss.err(k, fname, code, d)
    W = lambda code, d: iss.warn(k, fname, code, d)
    status, loai = r["status"], r["loai"]
    for col, v in r.items():
        if v.strip().lower() in NULLS:
            W("W_NULL_STR", f"{col}={v!r}")
    if status not in STATUS:
        E("E_STATUS", repr(status))
    if loai not in LOAI:
        E("E_LOAI", repr(loai))
    if r["pt_kieu"] not in PT_KIEU:
        E("E_PT_KIEU", repr(r["pt_kieu"]))
    if (r["pt_kieu"] == "") != (r["pt_noi_dung"] == ""):
        E("E_PT_PAIR", f"pt_kieu={r['pt_kieu']!r}, pt_noi_dung rỗng={r['pt_noi_dung'] == ''}")
    if loai == "khac_dung" and not r["khac_biet"].strip():
        E("E_KHAC_BIET", "khac_dung nhưng khac_biet rỗng")
    if loai == "yeu_to" and not r["pt_noi_dung"].strip():
        W("W_YEU_TO_NO_PT", "yeu_to nhưng pt_noi_dung rỗng")
    if r["tu_viet"].strip() and loai not in ("cung_dung", "khac_dung"):
        E("E_TU_VIET_LOAI", f"tu_viet có giá trị nhưng loai={loai}")
    if loai == "cung_dung" and not r["tu_viet"].strip():
        W("W_TU_VIET_EMPTY", "cung_dung nhưng tu_viet rỗng")
    if status == "needs_review" and not r["review_reason"].strip():
        E("E_REVIEW_REASON", "needs_review thiếu review_reason")
    nv = r["nghia_vi"]
    if not nv.strip() and status != "needs_review":
        E("E_NGHIA_EMPTY", "nghia_vi rỗng")
    if len(nv) > 80:
        W("W_NGHIA_LONG", f"{len(nv)} ký tự")
    if inp is not None:
        cv = inp.get("cv_vi", "")
        if cv and nv == cv and len(nv) > 150:
            W("W_NGHIA_COPY_CV", f"nghia_vi giống cv_vi, {len(nv)} ký tự")
    m = ENGLISH.search(nv)
    if m:
        W("W_ENGLISH", f"có thể là tiếng Anh: {m.group(0)!r}")
    if CJK.search(nv):
        W("W_HAN_IN_NGHIA", "chữ Hán trong nghia_vi")
    # hanviet
    hv = r["hanviet"].strip()
    if not hv:
        E("E_HANVIET_EMPTY", "hanviet rỗng")
        return
    hv_pre = inp.get("hv_pre", "") if inp else None
    if hv == "=":
        if hv_pre is not None and "?" in hv_pre.split():
            E("E_HV_PRE_Q_EQ", f"hv_pre={hv_pre!r} có '?' mà hanviet='='")
        elif hv_pre is not None and not hv_pre.strip():
            E("E_HANVIET_EQ_EMPTY_PRE", "hanviet='=' nhưng hv_pre rỗng")
        return
    toks = hv.split()
    hanzi = inp.get("hanzi", "") if inp else ""
    if inp:
        n = len(CJK.findall(hanzi))
        if len(toks) != n:
            E("E_HV_COUNT", f"{len(toks)} âm, hanzi có {n} chữ CJK")
    if "?" in toks and status != "needs_review":
        E("E_HV_Q_STATUS", "có '?' mà status không phải needs_review")
    if cand_keys is None:
        W("W_NO_CANDS", "không có ứng viên để kiểm âm")
        return
    for i, t in enumerate(toks):
        if t == "?" or i >= len(cand_keys):
            continue
        if reading_key(t) not in cand_keys[i]:
            E("E_HV_NOT_IN_CANDS", f"âm {i + 1} {t!r} không nằm trong cands của chữ {i + 1}")


def parent_input(fn, input_names):
    """Tên input mà out fn thuộc về: trùng tên, hoặc <stem input> + hậu tố chữ cái (batch_01a.tsv)."""
    if fn in input_names:
        return fn
    stem = fn[:-4] if fn.endswith(".tsv") else fn
    for n in input_names:
        ns = n[:-4] if n.endswith(".tsv") else n
        if stem.startswith(ns) and re.fullmatch(r"[A-Za-z]+", stem[len(ns):]):
            return n
    return None


def validate_file(path, cols, inputs_by_file, cand_for, iss, is_fix=False, parent=None):
    """Trả (list note_key theo thứ tự, dict note_key->row)."""
    fname = os.path.basename(path)
    header, rows, derr = read_tsv(path)
    keys, byk = [], {}
    if derr:
        iss.err("", fname, "E_ENCODING", derr)
        return keys, byk
    if header is None:
        iss.err("", fname, "E_HEADER", "file rỗng")
        return keys, byk
    if header != cols:
        iss.err("", fname, "E_HEADER", f"header={header}")
        return keys, byk
    inp_rows = None if is_fix else inputs_by_file.get(parent or fname)
    for ln, row in rows:
        if len(row) != len(cols):
            iss.err(row[0] if row else "", fname, "E_COLS", f"dòng {ln}: {len(row)} cột, cần {len(cols)}")
            if row:
                keys.append(row[0])
            continue
        d = dict(zip(cols, row))
        k = d["note_key"]
        keys.append(k)
        if k in byk:
            iss.err(k, fname, "E_KEY_DUP", f"trùng trong file (dòng {ln})")
            continue
        byk[k] = d
        if is_fix and not d["reviewer"].strip():
            iss.err(k, fname, "E_FIX_REVIEWER", "reviewer rỗng")
        inp = inp_rows.get(k) if inp_rows is not None else inputs_by_file.get("*", {}).get(k)
        check_row(d, inp, cand_for(k, inp), iss, fname)
    return keys, byk


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", required=True)
    ap.add_argument("--outs", required=True)
    ap.add_argument("--fixes")
    ap.add_argument("--items", default="00_base/items.jsonl")
    ap.add_argument("--item-hv", default="02_chars/item_hv.jsonl")
    ap.add_argument("--cands-bosung", default=BOSUNG_DEFAULT, help="file ứng viên bổ sung có nguồn (tùy chọn)")
    ap.add_argument("--report", required=True)
    ap.add_argument("--json", required=True)
    a = ap.parse_args()
    iss = Issues()

    items = load_jsonl(a.items)
    item_keys = [x["note_key"] for x in items]
    item_set = set(item_keys)
    item_hv = {}
    if os.path.exists(a.item_hv):
        for x in load_jsonl(a.item_hv):
            item_hv[x["note_key"]] = x
    else:
        print(f"[cảnh báo] không có {a.item_hv}; dùng hv_cands từ đầu vào", file=sys.stderr)
    apply_cands_bosung(item_hv, load_cands_bosung(a.cands_bosung))

    in_files = sorted(glob.glob(os.path.join(a.inputs, "*.tsv")))
    inputs_by_file, input_keys, all_inputs = {}, {}, {}
    for p in in_files:
        fn = os.path.basename(p)
        header, rows, derr = read_tsv(p)
        if derr or header is None:
            iss.err("", fn, "E_INPUT_UNREADABLE", derr or "rỗng")
            continue
        d, ks = {}, []
        for ln, row in rows:
            dd = dict(zip(header, row))
            if "note_key" in dd:
                d[dd["note_key"]] = dd
                ks.append(dd["note_key"])
        inputs_by_file[fn], input_keys[fn] = d, ks
        all_inputs.update(d)
    inputs_by_file["*"] = all_inputs

    def cand_for(k, inp):
        iv = item_hv.get(k)
        if iv is not None:
            res = []
            for c in iv.get("chars", []):
                s = set()
                for cd in c.get("cands", []):
                    if cd.get("reading"):
                        s.add(reading_key(cd["reading"]))
                    if cd.get("key"):
                        s.add(cd["key"])
                res.append(s)
            return res
        if inp is not None and inp.get("hv_cands") is not None:
            return [set(reading_key(r) for r in rd) for rd in parse_hv_cands(inp["hv_cands"])]
        return None

    out_files = sorted(glob.glob(os.path.join(a.outs, "*.tsv")))
    stats = {}
    global_cnt = collections.Counter()
    input_names = [n for n in inputs_by_file if n != "*"]
    group_keys = collections.defaultdict(list)   # input -> [(out file, key)]
    groups_seen = set()
    for p in out_files:
        fn = os.path.basename(p)
        par = parent_input(fn, input_names)
        if par is None:
            iss.err("", fn, "E_NO_INPUT", "out không có input cùng tên (hoặc tên input + hậu tố chữ cái)")
        else:
            groups_seen.add(par)
        keys, byk = validate_file(p, OUT_COLS, inputs_by_file, cand_for, iss, parent=par)
        for k in keys:
            global_cnt[k] += 1
            if par:
                group_keys[par].append((fn, k))
        st = stats.setdefault(fn, {"n": 0, "nr": 0, "loai": collections.Counter()})
        for d in byk.values():
            st["n"] += 1
            st["nr"] += d["status"] == "needs_review"
            st["loai"][d["loai"]] += 1
    for par in sorted(groups_seen):
        ik = set(input_keys[par])
        got = collections.defaultdict(list)
        for fn, k in group_keys[par]:
            got[k].append(fn)
        for k in sorted(ik - set(got)):
            iss.err(k, par, "E_KEY_MISSING", "có trong input, thiếu trong (các phần) out")
        for k in sorted(set(got) - ik):
            iss.err(k, par, "E_KEY_EXTRA", f"có trong out ({got[k][0]}), không có trong input")
        for k, fns in sorted(got.items()):
            if len(set(fns)) > 1:
                iss.err(k, par, "E_KEY_DUP_PARTS", f"trùng giữa các phần: {sorted(set(fns))}")
    for fn in sorted(set(input_names) - groups_seen):
        iss.err("", fn, "E_NO_OUT", "input chưa có out nào")

    missing = [k for k in item_keys if global_cnt[k] == 0]
    dup = [k for k in item_keys if global_cnt[k] > 1]
    unknown = [k for k in global_cnt if k not in item_set]
    for k in dup:
        iss.err(k, "*", "E_GLOBAL_DUP", f"xuất hiện {global_cnt[k]} lần trong các out")
    for k in unknown:
        iss.err(k, "*", "E_GLOBAL_UNKNOWN", "note_key không có trong items.jsonl")
    if missing:
        iss.err("", "*", "E_GLOBAL_MISSING", f"{len(missing)} mục của items.jsonl chưa có trong out; mẫu: {missing[:20]}")

    fix_files = sorted(glob.glob(os.path.join(a.fixes, "fixes_*.tsv"))) if a.fixes and os.path.isdir(a.fixes) else []
    for p in fix_files:
        keys, byk = validate_file(p, FIX_COLS, inputs_by_file, cand_for, iss, is_fix=True)
        for k in byk:
            if k not in item_set:
                iss.err(k, os.path.basename(p), "E_FIX_UNKNOWN", "note_key không có trong items.jsonl")

    os.makedirs(os.path.dirname(os.path.abspath(a.json)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(a.report)), exist_ok=True)
    with open(a.json, "w", encoding="utf-8", newline="\n") as f:
        for r in iss.rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    by_code = collections.Counter((r["level"], r["code"]) for r in iss.rows)
    by_file = collections.defaultdict(collections.Counter)
    for r in iss.rows:
        by_file[r["file"]][r["level"]] += 1
    n_err = sum(1 for r in iss.rows if r["level"] == "error")
    n_warn = len(iss.rows) - n_err
    L = ["# Báo cáo kiểm bản soạn\n"]
    L.append(f"- Mục trong items.jsonl: {len(item_keys)}")
    L.append(f"- Mục có đúng một bản soạn: {sum(1 for k in item_keys if global_cnt[k] == 1)}; thiếu: {len(missing)}; trùng: {len(dup)}; lạ: {len(unknown)}")
    L.append(f"- File out: {len(out_files)}; file input: {len(in_files)}; file fixes: {len(fix_files)}")
    L.append(f"- Lỗi: {n_err}; cảnh báo: {n_warn}\n")
    L.append("## Theo mã\n\n| Mức | Mã | Số lượng |\n|---|---|---|")
    for (lv, c), n in sorted(by_code.items()):
        L.append(f"| {lv} | {c} | {n} |")
    if not by_code:
        L.append("| - | (không có) | 0 |")
    L.append("\n## Theo file\n\n| File | Lỗi | Cảnh báo |\n|---|---|---|")
    for fn in sorted(by_file):
        L.append(f"| {fn} | {by_file[fn]['error']} | {by_file[fn]['warn']} |")
    tot_n = sum(s["n"] for s in stats.values())
    tot_nr = sum(s["nr"] for s in stats.values())
    tot_loai = collections.Counter()
    for s in stats.values():
        tot_loai.update(s["loai"])
    loai_order = sorted(LOAI)
    L.append("\n## needs_review theo file\n\n| File | Số mục | needs_review | Tỷ lệ |\n|---|---|---|---|")
    for fn in sorted(stats):
        s = stats[fn]
        L.append(f"| {fn} | {s['n']} | {s['nr']} | {s['nr'] / s['n']:.1%} |" if s["n"] else f"| {fn} | 0 | 0 | - |")
    if tot_n:
        L.append(f"| **Tổng** | {tot_n} | {tot_nr} | {tot_nr / tot_n:.1%} |")
    L.append("\n## Phân bố loai theo file (% mục)\n")
    L.append("| File | " + " | ".join(loai_order) + " |\n|---|" + "---|" * len(loai_order))
    for fn in sorted(stats):
        s = stats[fn]
        if s["n"]:
            L.append(f"| {fn} | " + " | ".join(f"{s['loai'][l] / s['n']:.0%}" for l in loai_order) + " |")
    if tot_n:
        L.append("| **Tổng** | " + " | ".join(f"{tot_loai[l] / tot_n:.0%}" for l in loai_order) + " |")
    L.append("\n## Lô nghi lệch\n")
    odd = []
    for fn in sorted(stats):
        s = stats[fn]
        if s["n"] < 5 or not tot_n:
            continue
        if abs(s["nr"] / s["n"] - tot_nr / tot_n) > 0.20:
            odd.append(f"- {fn}: tỷ lệ needs_review {s['nr'] / s['n']:.0%} lệch hơn 20 điểm so với chung {tot_nr / tot_n:.0%}")
        for l in loai_order:
            if abs(s["loai"][l] / s["n"] - tot_loai[l] / tot_n) > 0.25:
                odd.append(f"- {fn}: loai={l} chiếm {s['loai'][l] / s['n']:.0%} (chung {tot_loai[l] / tot_n:.0%})")
    L.extend(odd or ["(không có)"])
    with open(a.report, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print(f"lỗi={n_err} cảnh báo={n_warn} thiếu={len(missing)} trùng={len(dup)} lạ={len(unknown)}")
    sys.exit(1 if n_err else 0)


if __name__ == "__main__":
    main()
