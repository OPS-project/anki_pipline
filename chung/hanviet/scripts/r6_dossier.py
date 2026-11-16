"""R6: lập hồ sơ bằng chứng cho các chữ có âm Hán Việt đáng ngờ (chỉ đọc nguồn, không quyết âm).

Chạy (từ thư mục hanviet):
  python -I scripts/r6_dossier.py [--kaikki-cache <file jsonl tạm>] [--web <file json bằng chứng web>]
Ghi: 06_review/r6/ho_so_nghi_van.md, 06_review/r6/ho_so_nghi_van.tsv
Lần đầu quét kaikki-Chinese.jsonl (1,2 GB) và lưu dòng khớp vào --kaikki-cache; lần sau dùng cache.
"""
import sys, os, re, json, csv, argparse, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
from hv_common import reading_key
from validate_drafts import load_jsonl

ROOT = os.path.dirname(HERE)
P = lambda *a: os.path.join(ROOT, *a)

MANDATORY = list("兔吹")
R1_UNSURE = list("咱姥踹椎歪滴哨吗撞晃挣钉刹呵哈吭什缅")
MD_MAX_ITEMS = 25


def hexu(ch):
    return format(ord(ch), "x")


def load_unihan():
    var, viet = collections.defaultdict(lambda: collections.defaultdict(set)), collections.defaultdict(list)
    cp = re.compile(r"U\+([0-9A-F]+)")
    for line in open(P("01_sources", "unihan", "ex", "Unihan_Variants.txt"), encoding="utf-8"):
        if line.startswith("#") or "\t" not in line:
            continue
        u, k, v = line.rstrip("\n").split("\t", 2)
        if k in ("kSemanticVariant", "kZVariant", "kTraditionalVariant", "kSimplifiedVariant",
                 "kSpecializedSemanticVariant"):
            c = chr(int(u[2:], 16))
            for m in cp.finditer(v):
                var[c][k].add(chr(int(m.group(1), 16)))
    for line in open(P("01_sources", "unihan", "ex", "Unihan_Readings.txt"), encoding="utf-8"):
        if line.startswith("#") or "\t" not in line:
            continue
        u, k, v = line.rstrip("\n").split("\t", 2)
        if k == "kVietnamese":
            viet[chr(int(u[2:], 16))] = v.split()
    return var, viet


def load_tc():
    t = open(P("01_sources", "thieuchuu", "hanviet", "dataV4.json"), encoding="utf-8").read()
    d = json.loads(t[t.index("["): t.rindex("]") + 1])
    by = collections.defaultdict(list)
    for i, e in enumerate(d):
        e["_idx"] = i
        by[e["ky_tu"]].append(e)
    lien = collections.defaultdict(list)
    for e in d:
        for f in ("tu_lien_quang_1", "tu_lien_quang_2"):
            for c in (e.get(f) or ""):
                if "㐀" <= c:
                    lien[c].append(e)
    return d, by, lien


def load_hvp():
    res = collections.defaultdict(list)
    with open(P("01_sources", "hvpinyin", "hanviet.csv"), encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            res[r["char"]].append((r["hanviet"], r["pinyin"]))
    return res


def scan_kaikki(chars, cache):
    if os.path.exists(cache):
        return [json.loads(l) for l in open(cache, encoding="utf-8") if l.strip()]
    out = []
    keys = {c: '"word": "%s"' % c for c in chars}
    with open(P("01_sources", "kaikki", "kaikki-Chinese.jsonl"), encoding="utf-8", errors="replace") as f:
        for l in f:
            m = re.search(r'"word": "(.)"', l[:20000] if len(l) > 20000 else l)
            if not m or m.group(1) not in chars:
                continue
            try:
                out.append(json.loads(l))
            except Exception:
                pass
    with open(cache, "w", encoding="utf-8", newline="\n") as f:
        for e in out:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    return out


def kaikki_summary(e):
    """Trả danh sách chuỗi ngắn: âm tiếng Việt / nhắc Sino-Vietnamese / descendants vi."""
    res = []
    for s in e.get("sounds", []):
        txt = json.dumps(s, ensure_ascii=False)
        if re.search(r"Vietnam|Sino-Xenic|Hán Việt", txt):
            res.append("sounds:" + txt[:200])
    def walk(ds):
        for d in ds or []:
            if d.get("lang_code") == "vi":
                res.append("descendant_vi:" + json.dumps({k: d.get(k) for k in ("word", "raw_tags", "tags", "roman")},
                                                         ensure_ascii=False))
            walk(d.get("descendants"))
    walk(e.get("descendants"))
    blob = json.dumps({k: v for k, v in e.items() if k not in ("descendants", "sounds")}, ensure_ascii=False)
    for m in re.finditer(r"Sino-Vietnamese|Hán Việt|Vietnamese", blob):
        s = blob[max(0, m.start() - 80): m.end() + 120]
        res.append("text:" + s)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kaikki-cache")
    ap.add_argument("--web", help="JSON {char: [{url, date, readings, quote}]} do người chạy nhập tay từ WebFetch")
    a = ap.parse_args()
    cache = a.kaikki_cache or os.path.join(ROOT, "06_review", "r6", "_kaikki_cache.jsonl")

    fin = load_jsonl(P("07_final", "hanviet_10898.jsonl"))
    ihv = {x["note_key"]: x for x in load_jsonl(P("02_chars", "item_hv.jsonl"))}
    chars_db = {}
    for l in open(P("02_chars", "chars.jsonl"), encoding="utf-8"):
        if l.strip():
            x = json.loads(l)
            chars_db[x["char"]] = x
    var, uviet = load_unihan()
    tc_all, tc_by, tc_lien = load_tc()
    hvp = load_hvp()
    kviet = json.load(open(P("01_sources", "kaikki", "viet_readings.json"), encoding="utf-8"))
    web = json.load(open(a.web, encoding="utf-8")) if a.web else {}

    occ = collections.defaultdict(list)        # char -> [(rec, idx)]
    g3 = collections.defaultdict(set)
    for r in fin:
        iv = ihv[r["note_key"]]
        for i, c in enumerate(r.get("hanviet_chars", [])):
            ch = c["char"]
            occ[ch].append((r, i))
            hv = c.get("hv")
            if not hv or hv == "?":
                continue
            cands = iv["chars"][i].get("cands", [])
            if not any(reading_key(cd["reading"]) == reading_key(hv) and "thieuchuu" in cd.get("sources", []) for cd in cands):
                g3[ch].add(hv)

    cats = collections.OrderedDict()
    for c in MANDATORY:
        cats.setdefault(c, []).append("1-bat_buoc")
    for c in R1_UNSURE:
        cats.setdefault(c, []).append("2-R1_khong_chac")
    for c in g3:
        cats.setdefault(c, []).append("3-khong_Thieu_Chuu")
    targets = list(cats)

    # biến thể: Unihan + trad của item_hv
    variants = {}
    for ch in targets:
        vs = {}
        for k, s in var.get(ch, {}).items():
            for v in s:
                vs.setdefault(v, set()).add("Unihan:" + k)
        for r, i in occ[ch][:1]:
            for t in ihv[r["note_key"]]["chars"][i].get("trad", []):
                if t != ch:
                    vs.setdefault(t, set()).add("item_hv.trad")
        # một bậc nữa qua trad (phồn -> các dị thể của phồn)
        for v in list(vs):
            if "item_hv.trad" in vs[v]:
                for k, s in var.get(v, {}).items():
                    for w in s:
                        if w != ch and w not in vs:
                            vs.setdefault(w, set()).add(f"Unihan:{k}(của {v})")
        variants[ch] = vs

    all_chars = set(targets)
    for ch in targets:
        all_chars |= set(variants[ch])
    kk = scan_kaikki(all_chars, cache)
    kk_by = collections.defaultdict(list)
    for e in kk:
        kk_by[e["word"]].append(e)

    rows_tsv, md_sections, summary = [], [], []
    for ch in targets:
        items = occ[ch]
        used = collections.Counter()
        for r, i in items:
            used[r["hanviet_chars"][i].get("hv", "?")] += 1
        group = chars_db.get(ch, {})
        srcmap = collections.defaultdict(set)   # reading -> {nguồn}
        for cd in group.get("hv_candidates", []):
            for s in str(cd.get("source", "")).split(","):
                srcmap[cd["reading"]].add(s.strip() + (f"(via {cd['via_char']})" if cd.get("via_char") not in (None, ch) else ""))
        # cands đầu mục (có sources đầy đủ)
        for r, i in items:
            for cd in ihv[r["note_key"]]["chars"][i].get("cands", []):
                for s in cd.get("sources", []):
                    srcmap[cd["reading"]].add(s)
        extra = []   # (reading, nguồn trực tiếp)
        tcl = []
        for v in [ch] + list(variants[ch]):
            for e in tc_by.get(v, []):
                for rd in [x.strip() for x in e["am_han"].split(",") if x.strip()]:
                    extra.append((rd, f"thieuchuu[{v}]" if v != ch else "thieuchuu[trực tiếp]"))
                tcl.append((v, e))
            for rd, py in hvp.get(v, []):
                for x in re.findall(r"[^\[\]', ]+", rd):
                    extra.append((x, f"hvpinyin[{v},{py}]"))
            for x in uviet.get(v, []):
                extra.append((x, f"unihan_kVietnamese[{v}]"))
            for x in kviet.get(v, []):
                extra.append((x[0], f"kaikki_viet_readings[{v}]"))
        for e in tc_lien.get(ch, []):
            tcl.append((e["ky_tu"] + "(tu_lien_quang→" + ch + ")", e))
        for w in web.get(ch, []):
            for x in w.get("am", []):
                extra.append((x, "wiktionary_web"))
        am_nguon = collections.OrderedDict()
        for rd, s in list(extra):
            am_nguon.setdefault(rd, set()).add(s)
        for rd, ss in srcmap.items():
            am_nguon.setdefault(rd, set()).update("cands:" + s for s in ss)
        am_str = "|".join(f"{rd}:{'+'.join(sorted(ss))}" for rd, ss in am_nguon.items())
        # kaikki
        kl = []
        for v in [ch] + list(variants[ch]):
            for e in kk_by.get(v, []):
                for s in kaikki_summary(e):
                    kl.append(f"[{v}/{e.get('pos')}] {s}")
        wb = list(web.get(ch, [])) + [w for v in variants[ch] for w in web.get(v, [])]
        wb_str = "; ".join(f"{w['url']} ({w['date']}): {w['readings']}" for w in wb)
        note = []
        if ch == "兔":
            note.append("TC bản số hóa ghi 兔 'thỏ'; 'thố' chỉ thấy trong mục 菟 ('thỏ, thố, đồ'; 'Cũng đọc là chữ thố') — xem md; Wiktionary web (trang 兔) ghi Hán Việt = thố, Nôm = thỏ/thò/xỏ")
        if ch == "吹":
            note.append("TC: am_han 'xuy, xúy'; cùng mục 吹 ('Một âm là xúy. Cổ xúy [鼓吹]')")
        if wb_str:
            note.append("web: " + wb_str)
        for r, i in items:
            c = r["hanviet_chars"][i]
            rows_tsv.append([ch, r["note_key"], r["hanzi"], r.get("word_pinyin", ""), c.get("hv", "?"),
                             am_str, " ; ".join(note)])
        summary.append((ch, cats[ch], len(items), used, am_nguon, wb))

        # md
        L = [f"## {ch}  (nhóm {', '.join(cats[ch])}; {len(items)} mục)", ""]
        L.append(f"- Âm đang dùng: {', '.join(f'{k} ×{v}' for k, v in used.most_common())}")
        L.append(f"- Dị thể (nguồn): " + (", ".join(f"{v} [{'; '.join(sorted(s))}]" for v, s in variants[ch].items()) or "(không)"))
        L.append("- Âm theo nguồn:")
        for rd, ss in am_nguon.items():
            L.append(f"  - **{rd}**: {', '.join(sorted(ss))}")
        L.append("- Thiều Chửu (dataV4.json) — entry:")
        if not tcl:
            L.append("  - (không có entry cho chữ này hoặc dị thể)")
        for v, e in tcl:
            nghia = re.sub(r"\s+", " ", e["nghia"]).strip()
            L.append(f"  - [{v}] U+{e['unicode'].upper()} (dòng dữ liệu #{e['_idx']}, bộ {e['bo_thu']}, {e['so_net_1']}-{e['so_net_2']} nét) "
                     f"am_han=`{e['am_han']}` pinyin=`{e['pinyin']}` nghĩa: {nghia[:600]}")
        L.append("- hvpinyin (hanviet.csv): " + ("; ".join(f"{v}:{rd}/{py}" for v in [ch] + list(variants[ch]) for rd, py in hvp.get(v, [])) or "(không có)"))
        L.append("- Unihan kVietnamese: " + ("; ".join(f"{v}:{' '.join(uviet[v])}" for v in [ch] + list(variants[ch]) if uviet.get(v)) or "(không có)"))
        L.append("- kaikki viet_readings.json (descendants vi): " + ("; ".join(f"{v}:{kviet[v]}" for v in [ch] + list(variants[ch]) if v in kviet) or "(không có)"))
        L.append("- kaikki-Chinese.jsonl (Wiktionary dump), nhắc Vietnamese/Sino-Vietnamese:")
        L.extend(["  - " + x[:420] for x in kl] or ["  - (không có)"])
        if wb:
            L.append("- Wiktionary web:")
            for w in wb:
                L.append(f"  - {w['url']} (truy cập {w['date']}): {w['readings']}; trích: {w.get('quote', '')}")
        L.append(f"- Mục chứa chữ ({len(items)}" + (f"; hiển thị {MD_MAX_ITEMS}, đủ trong TSV" if len(items) > MD_MAX_ITEMS else "") + "):")
        L.append("")
        L.append("| note_key | hanzi | pinyin | hanviet | âm chữ | nghĩa_vi | loai | tu_viet | pt_noi_dung | char_note | status |")
        L.append("|---|---|---|---|---|---|---|---|---|---|---|")
        esc = lambda s: str(s or "").replace("|", "/").replace("\n", " ")
        for r, i in items[:MD_MAX_ITEMS]:
            c = r["hanviet_chars"][i]
            L.append("| " + " | ".join(esc(x) for x in (
                r["note_key"], r["hanzi"], r.get("word_pinyin"), r["hanviet"], c.get("hv", "?"), r.get("nghia_vi"),
                r.get("loai"), r.get("tu_viet"), (r.get("phan_tich") or {}).get("noi_dung"), r.get("char_note"),
                r.get("status"))) + " |")
        L.append("")
        md_sections.append("\n".join(L))

    # phần riêng 兔 và 吹
    extra_sec = ["## Ghi chú riêng", ""]
    for e in tc_by.get("菟", []):
        extra_sec.append(f"- 菟 (Thiều Chửu #{e['_idx']}): am_han=`{e['am_han']}`; nghĩa: {re.sub(chr(10), ' ', e['nghia']).strip()}")
    extra_sec.append("- Trích Thiều Chửu 吹: " + "; ".join(re.sub(r"\s+", " ", e["nghia"]).strip() for e in tc_by.get("吹", [])))
    # từ trong deck có 鼓吹 / cổ xúy / tâng bốc
    extra_sec += ["", "### Mục deck có 鼓吹, hoặc nghĩa có 'tâng bốc / cổ súy / cổ xúy / cổ vũ'", ""]
    pat = re.compile(r"鼓吹|tâng bốc|cổ súy|cổ xúy|cổ vũ|xúy|súy")
    found = [r for r in fin if "吹" in r["hanzi"] and (pat.search(r["hanzi"]) or pat.search(json.dumps(r, ensure_ascii=False)))]
    for r in found:
        extra_sec.append(f"- {r['note_key']} {r['hanzi']} ({r.get('word_pinyin')}) hanviet={r['hanviet']} nghĩa={r.get('nghia_vi')}")
    others = [r for r in fin if "吹" not in r["hanzi"] and re.search(r"tâng bốc|cổ súy|cổ xúy|鼓吹", json.dumps(r, ensure_ascii=False))]
    if others:
        extra_sec.append("- (mục khác không chứa 吹 nhưng nhắc các cụm trên): " + "; ".join(f"{r['hanzi']}={r['hanviet']}" for r in others[:30]))
    # 兔: mục chứa 兔/兎/菟/免? chỉ 兔
    # bảng tóm tắt
    head = ["# Hồ sơ bằng chứng chữ nghi vấn (R6)", "",
            "Người lập: Sonnet (không quyết âm). Chỉ ghi nguồn nào có âm nào. Nhóm 1 = bắt buộc (兔 吹); nhóm 2 = R1 ghi 'không chắc'; "
            "nhóm 3 = âm đang dùng không có trong Thiều Chửu (so reading_key với cands có nguồn thieuchuu trong item_hv.jsonl).", "",
            f"Số chữ: {len(targets)} (nhóm 3: {len(g3)}).", "",
            "| Chữ | Nhóm | Số mục | Âm đang dùng | Âm có nguồn (reading: nguồn) |", "|---|---|---|---|---|"]
    for ch, ct, n, used, am, wb in summary:
        head.append(f"| {ch} | {','.join(c.split('-')[0] for c in ct)} | {n} | {', '.join(f'{k}×{v}' for k, v in used.most_common())} | "
                    + "; ".join(f"{rd} ({', '.join(sorted({s.split('[')[0].replace('cands:', '') for s in ss}))})" for rd, ss in am.items()) + " |")
    head.append("")
    os.makedirs(P("06_review", "r6"), exist_ok=True)
    with open(P("06_review", "r6", "ho_so_nghi_van.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(head) + "\n" + "\n".join(extra_sec) + "\n\n" + "\n".join(md_sections))
    with open(P("06_review", "r6", "ho_so_nghi_van.tsv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, quotechar=None)
        w.writerow(["char", "note_key", "hanzi", "word_pinyin", "hv_hien_tai_cua_chu", "cac_am_co_nguon", "ghi_chu_bang_chung"])
        for r in rows_tsv:
            w.writerow([str(x).replace("\t", " ").replace("\n", " ") for x in r])
    print(f"{len(targets)} chữ, nhóm 3 = {len(g3)}, {len(rows_tsv)} dòng TSV")
    print("nhóm3:", " ".join(sorted(g3)))


if __name__ == "__main__":
    main()
