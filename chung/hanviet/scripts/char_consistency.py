"""Báo cáo nhất quán âm Hán Việt theo chữ / (chữ, pinyin) trên JSON hợp nhất (chuẩn bị cho pha review ngữ nghĩa).

Chạy (từ thư mục hanviet):
  python -I scripts/char_consistency.py --merged <merged.jsonl> --item-hv 02_chars/item_hv.jsonl
      --out-md <report.md> --out-tsv <table.tsv> [--examples 6]
Chỉ đọc đầu vào. Âm so bằng reading_key; âm tiết pinyin lấy từ item_hv (chars[].syl).
"""
import sys, os, json, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
from hv_common import reading_key, display


def load_jsonl(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def esc(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def pick_examples(entries, n):
    """Chọn <=n ví dụ, xoay vòng giữa các âm khác nhau."""
    by = collections.defaultdict(list)
    for e in entries:
        by[e["rk"]].append(e)
    order = sorted(by, key=lambda k: -len(by[k]))
    out = []
    i = 0
    while len(out) < n and any(by[k] for k in order):
        k = order[i % len(order)]
        if by[k]:
            out.append(by[k].pop(0))
        i += 1
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--merged", required=True)
    ap.add_argument("--item-hv", required=True)
    ap.add_argument("--out-md", required=True)
    ap.add_argument("--out-tsv", required=True)
    ap.add_argument("--examples", type=int, default=6)
    a = ap.parse_args()

    merged = load_jsonl(a.merged)
    ihv = {x["note_key"]: x for x in load_jsonl(a.item_hv)}

    by_cs = collections.defaultdict(list)
    by_c = collections.defaultdict(list)
    cands_of = {}      # char -> {reading_key: (reading, sources set)}
    changed = collections.defaultdict(list)   # char -> entries chosen đổi khác hv_pre
    for m in merged:
        iv = ihv.get(m["note_key"])
        ichars = iv["chars"] if iv else []
        for i, hc in enumerate(m.get("hanviet_chars", [])):
            hv = hc.get("hv")
            if not hv:
                continue
            ic = ichars[i] if i < len(ichars) and ichars[i].get("char") == hc["char"] else None
            syl = (ic or {}).get("syl") or "?"
            e = {"char": hc["char"], "syl": syl, "hv": hv, "rk": reading_key(hv), "nk": m["note_key"],
                 "hanzi": m["hanzi"], "wp": m.get("word_pinyin", ""), "hanviet": m.get("hanviet", ""),
                 "nghia": m.get("nghia_vi", ""), "by": m.get("drafted_by", ""), "cert": hc.get("certainty")}
            by_cs[(hc["char"], syl)].append(e)
            by_c[hc["char"]].append(e)
            if ic:
                cs = cands_of.setdefault(hc["char"], {})
                for cd in ic.get("cands", []):
                    cs.setdefault(reading_key(cd["reading"]), (cd["reading"], set()))[1].update(cd.get("sources", []))
                pre = ic.get("chosen")
                e["pre"] = pre
                if hc.get("certainty") == "chosen" and pre and reading_key(pre) != e["rk"]:
                    changed[hc["char"]].append(e)

    def groups(src):
        res = []
        for key, ents in src.items():
            rds = collections.Counter(e["rk"] for e in ents)
            if len(rds) >= 2:
                res.append((key, ents, rds))
        res.sort(key=lambda t: (-len(t[1]), str(t[0])))
        return res

    def disp_of(ents):
        d = {}
        for e in ents:
            d.setdefault(e["rk"], e["hv"])
        return d

    def cand_str(ch):
        cs = cands_of.get(ch, {})
        return ", ".join(f"{r}({'+'.join(sorted(s)) or '-'})" for r, s in cs.values()) or "(không có)"

    g_cs, g_c = groups(by_cs), groups(by_c)

    with open(a.out_tsv, "w", encoding="utf-8", newline="\n") as f:
        f.write("char\tsyl\treading\tcount\tnote_keys\n")
        for src in (by_cs, by_c):
            star = src is by_c
            for key, ents, rds in groups(src):
                ch, syl = (key, "*") if star else key
                dd = disp_of(ents)
                for rk, n in rds.most_common():
                    nks = ",".join(e["nk"] for e in ents if e["rk"] == rk)
                    f.write(f"{ch}\t{syl}\t{dd[rk]}\t{n}\t{nks}\n")

    L = []
    nchar_total = sum(len(v) for v in by_c.values())
    L.append("# Nhất quán âm Hán Việt theo chữ")
    L.append("")
    L.append(f"- Mục: {len(merged)}; chữ-trong-mục có âm: {nchar_total}; chữ khác nhau: {len(by_c)}; cặp (chữ, pinyin): {len(by_cs)}.")
    L.append(f"- Nhóm (chữ, pinyin) có >=2 âm: {len(g_cs)}; chữ có >=2 âm (không phân biệt pinyin): {len(g_c)}.")
    L.append("- Lưu ý: nhiều âm cho cùng (chữ, pinyin) có thể hợp lệ (đa âm HV theo nghĩa/từ); báo cáo chỉ để reviewer soi.")
    L.append("")

    def render(gs, title, star):
        L.append(f"## {title}")
        L.append("")
        for key, ents, rds in gs:
            ch, syl = (key, "*") if star else key
            dd = disp_of(ents)
            parts = ", ".join(f"**{dd[rk]}** x{n}" for rk, n in rds.most_common())
            L.append(f"### {ch} ({syl}): {len(ents)} mục; {parts}")
            L.append(f"Ứng viên có nguồn: {cand_str(ch)}")
            L.append("")
            L.append("| hanzi | word_pinyin | hanviet | âm chữ này | nghia_vi | note_key | drafted_by |")
            L.append("|---|---|---|---|---|---|---|")
            for e in pick_examples(ents, a.examples):
                L.append(f"| {esc(e['hanzi'])} | {esc(e['wp'])} | {esc(e['hanviet'])} | {esc(e['hv'])} | {esc(e['nghia'])} | {e['nk']} | {esc(e['by'])} |")
            L.append("")

    render(g_cs, "Nhóm (chữ, pinyin) có >=2 âm, sắp theo số mục", False)
    render(g_c, "Nhóm theo riêng chữ (mọi pinyin) có >=2 âm", True)

    L.append("## Chữ có âm chosen do người soạn đổi khác hv_pre (script tự chọn có thể sai)")
    L.append("")
    L.append(f"Tổng: {len(changed)} chữ, {sum(len(v) for v in changed.values())} lần.")
    L.append("")
    L.append("| chữ | số mục | hv_pre -> âm mới (số lần) | ví dụ note_key |")
    L.append("|---|---|---|---|")
    for ch, ents in sorted(changed.items(), key=lambda t: (-len(t[1]), t[0])):
        tr = collections.Counter(f"{display(e['pre'])} -> {e['hv']}" for e in ents)
        tr_s = "; ".join(f"{k} x{n}" for k, n in tr.most_common())
        L.append(f"| {ch} | {len(ents)} | {esc(tr_s)} | {ents[0]['nk']} |")
    L.append("")
    with open(a.out_md, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L))

    print(f"nhóm (chữ,pinyin) >=2 âm: {len(g_cs)}; chữ >=2 âm: {len(g_c)}; chữ bị đổi chosen: {len(changed)}")
    print("Top 15 nhóm (chữ, pinyin):")
    for key, ents, rds in g_cs[:15]:
        dd = disp_of(ents)
        print(f"  {key[0]} {key[1]}: {len(ents)} mục; " + ", ".join(f"{dd[rk]} x{n}" for rk, n in rds.most_common()))


if __name__ == "__main__":
    main()
