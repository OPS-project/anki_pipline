"""Pha 2: ghép ứng viên âm Hán Việt theo từng chữ, tạo 02_chars/item_hv.jsonl và 04_draft/input/*.tsv.
Chạy: python -I scripts/build_inputs.py   (tất định, không dùng hiểu biết mô hình)."""
import sys, os, json, re, ast, csv, unicodedata, collections, glob
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding="utf-8")
from hv_common import reading_key, display

ROOT = os.path.dirname(HERE)
P = lambda *a: os.path.join(ROOT, *a)

HARD_MAX, BATCH = 350, 700
SRC_PRI = {"hvpinyin": 0, "thieuchuu": 1, "wiktionary": 2, "unihan_kVietnamese": 3}

# ---------- pinyin ----------
TONEMAP = {"̄": "1", "́": "2", "̌": "3", "̀": "4"}


def norm_pin(p):
    """pinyin có số (u:, ü, mojibake) -> chữ thường, ü = v."""
    p = p.strip().lower()
    for a in ("ã\u009c", "ãü", "u:", "ü"):
        p = p.replace(a, "v")
    return p


def mark_to_num(s):
    d = unicodedata.normalize("NFD", s.lower())
    tone, out = "5", []
    for ch in d:
        if ch in TONEMAP:
            tone = TONEMAP[ch]
        elif ch == "̈":
            if out and out[-1] == "u":
                out[-1] = "v"
        elif unicodedata.combining(ch):
            continue
        else:
            out.append(ch)
    return unicodedata.normalize("NFC", "".join(out)) + tone


def split_syllables(word_pinyin):
    toks = []
    for t in word_pinyin.split():
        n = mark_to_num(t)
        base = n[:-1]
        # nhi hoa dính vào âm tiết: diǎnr -> diǎn + r
        if base.endswith("r") and base not in ("er", "r") and len(base) > 2:
            toks.append(mark_to_num(t[:-1]))
            toks.append("r5")
        else:
            toks.append(n)
    return toks


def toneless(p):
    return re.sub(r"[1-5]$", "", p)


# ---------- load ----------
def jl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


items = jl(P("00_base", "items.jsonl"))
chars = {c["char"]: c for c in jl(P("02_chars", "chars.jsonl"))}
words = {w["note_key"]: w for w in jl(P("02_chars", "words_source.jsonl"))}

csv_map = collections.defaultdict(list)       # (trad, pinyin|*) -> [reading raw]
csv_tl = collections.defaultdict(list)        # (trad, toneless pinyin) -> [reading raw]
with open(P("01_sources", "hvpinyin", "hanviet.csv"), encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        try:
            rd = ast.literal_eval(r["hanviet"])
        except Exception:
            rd = [r["hanviet"]]
        py = norm_pin(r["pinyin"])
        for x in rd:
            csv_map[(r["char"], py)].append(x)
            if py != "*":
                csv_tl[(r["char"], toneless(py))].append(x)

stphr = {}
with open(P("01_sources", "opencc", "STPhrases.txt"), encoding="utf-8") as f:
    for l in f:
        if l.startswith("#") or "\t" not in l:
            continue
        k, v = l.rstrip("\n").split("\t", 1)
        stphr.setdefault(k, v.split()[0])

EXACT = ("exact_pinyin", "exact_pinyin_toneless")


# ---------- trad ----------
def word_trad(it, w, syls):
    """trả về (list per-char trad list, nguồn) hoặc None."""
    h = it["hanzi"]
    mine = " ".join(syls)
    for key, mk in (("cvdict", "match_type"), ("cedict", "match_type_cedict")):
        if w.get(mk) not in EXACT:
            continue
        ents = [e for e in (w.get(key) or []) if len(e["trad"]) == len(h)]
        ex = [e for e in ents if norm_pin(e["pinyin"]) == mine] or ents
        ts = sorted({e["trad"] for e in ex})
        if len(ts) == 1:
            return [[c] for c in ts[0]], key
    ents = []
    for key, mk in (("cvdict", "match_type"), ("cedict", "match_type_cedict")):
        if w.get(mk) in EXACT:
            ents += [e for e in (w.get(key) or []) if len(e["trad"]) == len(h)]
    ents2 = [e for e in ents if norm_pin(e["pinyin"]) == mine] or ents
    if ents2:
        per = [[] for _ in h]
        for e in ents2:
            for i, c in enumerate(e["trad"]):
                if c not in per[i]:
                    per[i].append(c)
        return per, "dict_multi"
    v = stphr.get(h)
    if v and len(v) == len(h):
        return [[c] for c in v], "opencc_phrase"
    return None


def char_trad(c):
    tc = [t["char"] for t in chars.get(c, {}).get("trad_candidates", [])]
    return tc or [c]


# ---------- per-char ----------
def hint_list(h):
    out = []
    for p in (h.get("pinyin_hint") or "").split(","):
        p = norm_pin(p)
        if re.fullmatch(r"[a-z]+[1-5]", p):
            out.append(p)
    return out


def resolve_char(c, trads, lookup_syl, extra_reason, do_lookup=True):
    via = {c} | set(trads)
    cands = {}  # key -> {"disp": {src: display}, "sources": set}

    def add(reading, src):
        k = reading_key(reading)
        d = cands.setdefault(k, {"disp": {}, "sources": set()})
        d["sources"].add(src)
        d["disp"].setdefault(src, display(reading))

    tc_c = [h for h in chars.get(c, {}).get("hv_candidates", []) if h["via_char"] in via]
    for h in tc_c:
        add(h["reading"], h["source"])
    csv_keys = collections.OrderedDict()
    if do_lookup:
        for t in trads:
            for r in csv_map.get((t, lookup_syl), []) + csv_map.get((t, "*"), []):
                add(r, "hvpinyin")
                csv_keys.setdefault(reading_key(r), r)
    dropped = []
    if any(("thieuchuu" in d["sources"] or "hvpinyin" in d["sources"]) for d in cands.values()):
        for k in list(cands):
            if cands[k]["sources"] == {"unihan_kVietnamese"}:
                dropped.append(next(iter(cands[k]["disp"].values())))
                del cands[k]
    tc_keys = {reading_key(h["reading"]) for h in tc_c if h["source"] == "thieuchuu"}
    has_tc = bool(tc_keys)
    chosen_key, cert, reason = None, "uncertain", ""
    if not do_lookup:
        pass
    elif len(csv_keys) == 1:
        k = next(iter(csv_keys))
        chosen_key = k
        if k in tc_keys:
            cert, reason = "sure", "hvpinyin 1 âm cho (phồn,pinyin) và có trong Thiều Chửu"
        else:
            cert = "chosen"
            reason = "chỉ hvpinyin" if not has_tc else "hvpinyin 1 âm; Thiều Chửu không có âm này"
    elif len(csv_keys) > 1:
        keep = [k for k in csv_keys if k in tc_keys]
        if len(keep) == 1:
            chosen_key, cert, reason = keep[0], "chosen", "hvpinyin nhiều âm; lọc theo Thiều Chửu còn 1"
        elif len(keep) > 1:
            reason = "hvpinyin nhiều âm, Thiều Chửu cũng nhiều: " + ",".join(keep)
        elif has_tc:
            reason = "hvpinyin nhiều âm, không âm nào có trong Thiều Chửu: " + ",".join(csv_keys)
        else:
            reason = "hvpinyin nhiều âm, không có Thiều Chửu: " + ",".join(csv_keys)
    else:
        def tc_by(pred):
            ks = collections.OrderedDict()
            for h in tc_c:
                if h["source"] == "thieuchuu" and any(pred(p) for p in hint_list(h)):
                    ks.setdefault(reading_key(h["reading"]), 1)
            return list(ks)
        ks = tc_by(lambda p: p == lookup_syl)
        how = "pinyin_hint Thiều Chửu khớp chính xác"
        if not ks:
            ks = tc_by(lambda p: toneless(p) == toneless(lookup_syl))
            how = "pinyin_hint Thiều Chửu khớp không dấu thanh"
        if len(ks) == 1:
            chosen_key, cert, reason = ks[0], "chosen", how
        elif len(ks) > 1:
            reason = how + " nhưng nhiều âm: " + ",".join(ks)
        else:
            tl = collections.OrderedDict()
            for t in trads:
                for r in csv_tl.get((t, toneless(lookup_syl)), []):
                    tl.setdefault(reading_key(r), r)
            for r in tl.values():
                add(r, "hvpinyin")
            if len(tl) == 1:
                chosen_key, cert, reason = next(iter(tl)), "chosen", "hvpinyin khớp không dấu thanh (thanh nhẹ/biến điệu)"
            elif len(tl) > 1:
                keep = [k for k in tl if k in tc_keys]
                if len(keep) == 1:
                    chosen_key, cert, reason = keep[0], "chosen", "hvpinyin khớp không dấu thanh, lọc Thiều Chửu còn 1"
                else:
                    reason = "không có (phồn,pinyin); hvpinyin không dấu thanh nhiều âm: " + ",".join(tl)
            else:
                reason = "không có (phồn,pinyin) trong hvpinyin và không ứng viên Thiều Chửu khớp pinyin"

    def srcrank(k):
        return min(SRC_PRI.get(s, 9) for s in cands[k]["sources"])
    order = sorted(cands, key=lambda k: (k != chosen_key, srcrank(k)))
    out = []
    for k in order:
        d = cands[k]
        disp = d["disp"].get("hvpinyin") or d["disp"].get("thieuchuu") or next(iter(d["disp"].values()))
        out.append({"reading": disp, "key": k, "sources": sorted(d["sources"], key=lambda s: SRC_PRI.get(s, 9))})
    chosen = next((x["reading"] for x in out if x["key"] == chosen_key), None) if chosen_key else None
    only_hvp = bool(out) and all(set(x["sources"]) <= {"hvpinyin"} for x in out)
    return {"cands": out, "chosen": chosen, "certainty": cert,
            "reason": (reason + (" " + extra_reason if extra_reason else "")).strip(),
            "dropped": dropped, "hvpinyin_only": only_hvp}


# ---------- main ----------
def build():
    recs = []
    for it in items:
        h = it["hanzi"]
        w = words.get(it["note_key"], {})
        syls = split_syllables(it["word_pinyin"])
        flags = []
        mismatch = False
        if len(syls) == len(h):
            sylmap = list(syls)
        elif len(syls) == len(h) - 1 and h.endswith("儿"):
            sylmap = list(syls) + ["r5"]
        else:
            mismatch = True
            sylmap = [None] * len(h)
            flags.append("syllable_mismatch")
        wt = word_trad(it, w, syls)
        per_trad = wt[0] if wt else None
        chars_out = []
        multi = False
        for i, c in enumerate(h):
            trads = per_trad[i] if per_trad else char_trad(c)
            if len(trads) > 1:
                multi = True
            syl = sylmap[i]
            if mismatch:
                r = resolve_char(c, trads, "?", "", do_lookup=False)
                r["reason"] = f"syllable_mismatch ({len(syls)} âm tiết/{len(h)} chữ): {it['word_pinyin']}"
            else:
                lk, extra = syl, ""
                if c == "儿" and syl == "r5":
                    lk, extra = "er2", "儿 hóa (r) tra theo er2"
                r = resolve_char(c, trads, lk, extra)
            if len(trads) > 1:
                r["reason"] = (r["reason"] + (" multi_trad_unresolved" if not r["chosen"] else " (nhiều phồn thể; chọn âm theo pinyin)")).strip()
            chars_out.append({"char": c, "trad": trads, "syl": syl, "cands": r["cands"], "chosen": r["chosen"],
                              "certainty": r["certainty"], "reason": r["reason"], "dropped": r["dropped"],
                              "_hvp": r["hvpinyin_only"]})
        if multi:
            flags.append("multi_trad_unresolved")
        if any(c["certainty"] == "uncertain" for c in chars_out):
            flags.append("has_uncertain")
        if w.get("match_type") != "exact_pinyin":
            flags.append("cv_not_exact")
        if any(c["_hvp"] for c in chars_out):
            flags.append("hvpinyin_only")
        for c in chars_out:
            c.pop("_hvp")
        hv_pre = " ".join((c["chosen"].upper() if c["chosen"] else "?") for c in chars_out)
        recs.append({"note_key": it["note_key"], "hanzi": h, "word_pinyin": it["word_pinyin"], "hv_pre": hv_pre,
                     "chars": chars_out, "flags": flags})
    return recs


# ---------- TSV ----------
def clean(s):
    return re.sub(r"[\t\r\n]+", " ", s or "").strip()


def cut(s, n):
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def tc_meaning(c, trad, chosen):
    cands = chars.get(c, {}).get("hv_candidates", [])

    def first(via):
        pool = [h for h in cands if h["via_char"] == via and h["source"] == "thieuchuu" and h["meanings_vi"]]
        if chosen:
            pool.sort(key=lambda h: reading_key(h["reading"]) != reading_key(chosen))
        for h in pool:
            for m in h["meanings_vi"]:
                if not re.match(r"\s*Giản thể của chữ", m):
                    return m
        return None
    m = first(trad)
    if m is None and trad != c:
        m = first(c)
    if m is None:
        return None
    return cut(clean(re.sub(r"[{}]", "", m)), 60)


def tsv_row(it, rec, w):
    hv_parts, tc_parts, seen = [], [], set()
    for c in rec["chars"]:
        t = c["trad"]
        label = c["char"] + ("→" + "/".join(t) if t != [c["char"]] else "")
        hv_parts.append(f"{label}:{','.join(x['reading'] for x in c['cands'][:4])}")
        for tt in t:
            if tt in seen:
                continue
            seen.add(tt)
            m = tc_meaning(c["char"], tt, c["chosen"])
            if m:
                tc_parts.append(f"{tt}: {m}")
    mine = " ".join(split_syllables(it["word_pinyin"]))

    def mean(key, mk):
        ms = [m for e in (w.get(key) or []) if norm_pin(e["pinyin"]) == mine for m in e.get(mk, [])]
        return cut(" / ".join(ms), 150)
    row = [it["note_key"], it.get("level", ""), it["hanzi"], it["word_pinyin"], it.get("meaning_en", ""),
           it.get("sentence", ""), it.get("sentence_en", ""), rec["hv_pre"], "|".join(hv_parts),
           mean("cvdict", "meanings_vi"), mean("cedict", "meanings_en"), "; ".join(tc_parts)]
    return "\t".join(clean(x) for x in row)


HEADER = "note_key\tlevel\thanzi\tword_pinyin\tmeaning_en\tsentence\tsentence_en\thv_pre\thv_cands\tcv_vi\tce_en\ttc_char"


def main():
    recs = build()
    with open(P("02_chars", "item_hv.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    hard, easy = [], []
    for it, r in zip(items, recs):
        w = words[it["note_key"]]
        is_hard = ("has_uncertain" in r["flags"] or "multi_trad_unresolved" in r["flags"]
                   or "syllable_mismatch" in r["flags"] or w.get("match_type") in ("none", "hanzi_only"))
        (hard if is_hard else easy).append((it, r, w))
    outdir = P("04_draft", "input")
    os.makedirs(outdir, exist_ok=True)
    for fp in glob.glob(os.path.join(outdir, "*.tsv")):
        os.remove(fp)
    files = []

    def dump(group, size, prefix):
        for n, i in enumerate(range(0, len(group), size), 1):
            name = f"{prefix}_{n:02d}.tsv"
            part = group[i:i + size]
            with open(os.path.join(outdir, name), "w", encoding="utf-8", newline="\n") as f:
                f.write(HEADER + "\n")
                for it, r, w in part:
                    f.write(tsv_row(it, r, w) + "\n")
            files.append((name, len(part)))
    dump(hard, HARD_MAX, "hard")
    dump(easy, BATCH, "batch")
    cert = collections.Counter(c["certainty"] for r in recs for c in r["chars"])
    fl = collections.Counter(f for r in recs for f in r["flags"])
    hard_n = len(hard)
    lines = ["# Đầu vào cho người soạn (tự sinh bởi scripts/build_inputs.py)", "",
             "Sinh bởi Sonnet (pha 2). Nguồn ứng viên: 02_chars/item_hv.jsonl. Định dạng cột: TIEU_CHUAN.md mục 5.", "",
             "## Tiêu chí chia lô", "",
             "- Tập KHÓ (hard_NN.tsv, ≤350 mục/file): mục có cờ `has_uncertain` HOẶC `multi_trad_unresolved` HOẶC `syllable_mismatch` HOẶC match_type CVDICT là none/hanzi_only.",
             "- Tập còn lại (batch_NN.tsv, 700 mục/file) giữ thứ tự items.jsonl.", "",
             "## Số mục mỗi file", ""]
    for n, k in files:
        lines.append(f"- {n}: {k}")
    lines += ["", f"Tổng: {sum(k for _, k in files)} (items.jsonl: {len(items)}). Tập khó: {hard_n} mục; tập thường: {len(easy)} mục."]
    if hard_n > 2500:
        lines.append(f"\nCẢNH BÁO: tập khó {hard_n} > 2.500 mục; điều phối quyết định.")
    lines += ["", "## Thống kê certainty (theo số chữ-trong-mục)", ""]
    tot = sum(cert.values())
    for k in ("sure", "chosen", "uncertain"):
        lines.append(f"- {k}: {cert[k]} ({cert[k] * 100 / tot:.1f}%)")
    lines += [f"- tổng chữ-trong-mục: {tot}", "", "## Số mục mỗi cờ", ""]
    for k in ("has_uncertain", "multi_trad_unresolved", "syllable_mismatch", "cv_not_exact", "hvpinyin_only"):
        lines.append(f"- {k}: {fl[k]}")
    lines += ["", "## Ghi chú kỹ thuật", "",
              "- Nhi hóa: `r` dính (diǎnr) hoặc tách (diǎn r) ghép với 儿 ở cuối; 儿 hóa tra hvpinyin/Thiều Chửu theo `er2`.",
              "- Chữ phồn: ưu tiên entry CVDICT/CC-CEDICT khớp pinyin cùng độ dài, rồi OpenCC STPhrases, rồi STCharacters/trad_candidates. Cờ `multi_trad_unresolved` giữ khi chữ còn ≥2 phồn thể (âm vẫn có thể được chọn theo pinyin).",
              "- Bổ sung ngoài quy tắc gốc: khi không có (phồn,pinyin) trong hvpinyin và Thiều Chửu không khớp, thử hvpinyin theo pinyin không dấu thanh (thanh nhẹ/biến điệu 一 不); ghi rõ trong `reason`.",
              "- hvpinyin pinyin `*` coi là khớp mọi pinyin.",
              "- `hvpinyin_only`: mọi ứng viên của một chữ trong mục chỉ đến từ hvpinyin."]
    with open(os.path.join(outdir, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(files, cert, fl, hard_n)


if __name__ == "__main__":
    main()
