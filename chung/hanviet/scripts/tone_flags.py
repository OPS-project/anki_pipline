"""Gắn cờ "ngoai_le" thanh điệu cho từng chữ trong từ (TIEU_CHUAN mục 3; 03_tone/quy_tac_thanh_dieu.md mục 5).

Chạy (từ thư mục hanviet):
  python -I scripts/tone_flags.py --item-hv 02_chars/item_hv.jsonl --rules 03_tone/tone_rule_table.csv
      --out 05_validate/tone_flags.jsonl [--stats 05_validate/tone_flags_stats.json]
      [--min-rate 0.80] [--min-n 30]
Đầu vào: item_hv.jsonl (chars[].chosen/certainty/syl) hoặc bản merge (hanviet_chars[].hv/certainty; khi đó thanh
lấy từ word_pinyin nếu số âm tiết khớp số chữ).
Đầu ra: mỗi mục một dòng {"note_key", "tone_flags": [...]} (tone_flags rỗng nếu không có cờ).
Chữ chỉ được xét khi: certainty sure/chosen, có âm HV, thanh Mandarin trong từ là 1-4 (thanh 5 bỏ qua),
ô (thanh HV, lớp phụ âm, nhập thanh) có modal_rate >= min-rate và n >= min-n (đọc từ CSV).
Phân lớp vang/tắc, nhập thanh sao đúng định nghĩa trong scripts/tone_rule_measure.py.
"""
import sys, os, re, json, csv, argparse, unicodedata, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")

# --- sao nguyên văn từ tone_rule_measure.py (script đó chạy ngay khi import nên không import được) ---
def vtone(s):
    d = unicodedata.normalize("NFD", s.lower())
    for mark, name in (("́", "sắc"), ("̀", "huyền"), ("̉", "hỏi"), ("̃", "ngã"), ("̣", "nặng")):
        if mark in d:
            return name
    return "ngang"


def base(s):
    b = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in b if not unicodedata.combining(c))   # đ giữ nguyên


def entering(s):
    return bool(re.search(r"(p|t|c|ch)$", base(s)))


SON = ("ngh", "ng", "nh", "m", "n", "l", "v", "d", "gi", "y")


def cls(s):
    b = base(s)
    return "vang" if (b.startswith(SON) or b[0] in "aeiou") else "tac"
# --- hết phần sao ---

MT = {}
for _t, _cs in enumerate(["āēīōūǖ", "áéíóúǘ", "ǎěǐǒǔǚ", "àèìòùǜ"], 1):
    for _c in _cs:
        MT[_c] = _t


def tone_of_pinyin(p):
    """Thanh từ pinyin số (shou3) hoặc dấu (shǒu). Trả 1-5, hoặc None nếu không đọc được."""
    p = (p or "").strip()
    if not p:
        return None
    m = re.search(r"([0-5])$", p)
    if m:
        t = int(m.group(1))
        return 5 if t == 0 else t
    return next((MT[c] for c in p if c in MT), 5)


def load_rules(path, min_rate, min_n):
    cells = {}
    with open(path, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            n, rate = int(r["n"]), float(r["modal_rate"])
            key = (r["hv_tone"], r["onset_class"], r["entering"])
            cells[key] = dict(n=n, rate=rate, modal=int(r["modal_tone"].lstrip("T")),
                              usable=(n >= min_n and rate >= min_rate))
    return cells


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--item-hv", required=True)
    ap.add_argument("--rules", default="03_tone/tone_rule_table.csv")
    ap.add_argument("--out", required=True)
    ap.add_argument("--stats")
    ap.add_argument("--min-rate", type=float, default=0.80)
    ap.add_argument("--min-n", type=int, default=30)
    a = ap.parse_args()

    cells = load_rules(a.rules, a.min_rate, a.min_n)
    cnt = collections.Counter()
    by_cell = collections.defaultdict(lambda: collections.Counter())
    n_items = 0
    outrows = []
    for line in open(a.item_hv, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        it = json.loads(line)
        n_items += 1
        chars = it.get("chars")
        merged = chars is None
        if merged:
            chars = it.get("hanviet_chars", [])
        toks = (it.get("word_pinyin") or "").split()
        flags = []
        for i, c in enumerate(chars):
            cnt["chars_total"] += 1
            hv = c.get("hv") if merged else c.get("chosen")
            cert = c.get("certainty")
            if cert not in ("sure", "chosen") or not hv:
                cnt["skip_certainty_or_no_hv"] += 1
                continue
            if c.get("syl"):
                actual = tone_of_pinyin(c["syl"])
            elif len(toks) == len(chars):
                actual = tone_of_pinyin(toks[i])
            else:
                actual = None
            if actual is None:
                cnt["skip_no_pinyin"] += 1
                continue
            if actual == 5:
                cnt["skip_neutral_tone"] += 1
                continue
            key = (vtone(hv), cls(hv), "nhap" if entering(hv) else "khong")
            cell = cells.get(key)
            if cell is None or not cell["usable"]:
                cnt["skip_cell_not_usable"] += 1
                continue
            cnt["eligible"] += 1
            cname = "/".join(key)
            by_cell[cname]["eligible"] += 1
            by_cell[cname]["predicted"] = cell["modal"]
            if actual != cell["modal"]:
                cnt["ngoai_le"] += 1
                by_cell[cname]["ngoai_le"] += 1
                flags.append({"char": c.get("char"), "hv_tone": key[0], "class": key[1], "nhap": key[2] == "nhap",
                              "predicted": cell["modal"], "actual_in_word": actual, "flag": "ngoai_le"})
        outrows.append({"note_key": it["note_key"], "tone_flags": flags})
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "w", encoding="utf-8", newline="\n") as f:
        for r in outrows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    usable = {"/".join(k): v for k, v in cells.items() if v["usable"]}
    stats = {
        "items": n_items,
        "items_with_flag": sum(1 for r in outrows if r["tone_flags"]),
        "chars_total": cnt["chars_total"],
        "chars_eligible": cnt["eligible"],
        "chars_ngoai_le": cnt["ngoai_le"],
        "skipped": {k: v for k, v in cnt.items() if k.startswith("skip_")},
        "usable_cells": {k: {"n": v["n"], "rate": v["rate"], "predicted": v["modal"]} for k, v in usable.items()},
        "by_cell": {k: {"eligible": v["eligible"], "ngoai_le": v["ngoai_le"], "predicted": v["predicted"]}
                    for k, v in sorted(by_cell.items())},
    }
    if a.stats:
        os.makedirs(os.path.dirname(os.path.abspath(a.stats)), exist_ok=True)
        json.dump(stats, open(a.stats, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
