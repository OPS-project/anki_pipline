"""Đo quy tắc thanh điệu Hán Việt -> Mandarin trên tập chữ của deck.
Chạy: python -I tone_rule_measure.py UNIHAN_ZIP CHARS_TXT OUT_DIR
Xuất: tone_rule_table.csv, tone_rule_items.csv, tone_rule_summary.json (số liệu loại trừ)."""
import sys, re, csv, json, zipfile, unicodedata, collections
sys.stdout.reconfigure(encoding="utf-8")
UNIHAN, CHARS, OUT = sys.argv[1:4]
LEVELS = ["HSK1", "HSK2", "HSK3", "HSK4", "HSK5", "HSK6", "HSK7-9"]

data = collections.defaultdict(dict)
with zipfile.ZipFile(UNIHAN) as z:
    for fn in ("Unihan_Readings.txt", "Unihan_Variants.txt"):
        for line in z.read(fn).decode("utf-8").splitlines():
            if line.startswith("U+"):
                cp, k, v = line.split("\t", 2)
                if k in ("kVietnamese", "kMandarin", "kTraditionalVariant"):
                    data[chr(int(cp[2:], 16))][k] = v

def vn(ch):
    d = data.get(ch, {})
    if "kVietnamese" in d: return d["kVietnamese"].split(), "direct"
    for t in d.get("kTraditionalVariant", "").split():
        tc = chr(int(t[2:].split("<")[0], 16))
        if "kVietnamese" in data.get(tc, {}): return data[tc]["kVietnamese"].split(), "via-trad"
    return [], None

MT = {}
for t, cs in enumerate(["āēīōūǖ", "áéíóúǘ", "ǎěǐǒǔǚ", "àèìòùǜ"], 1):
    for c in cs: MT[c] = t
def mtone(p): return next((MT[c] for c in p if c in MT), 5)
def vtone(s):
    d = unicodedata.normalize("NFD", s.lower())
    for mark, name in (("\u0301", "sắc"), ("\u0300", "huyền"), ("\u0309", "hỏi"), ("\u0303", "ngã"), ("\u0323", "nặng")):
        if mark in d: return name
    return "ngang"
def base(s):
    b = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in b if not unicodedata.combining(c))   # đ giữ nguyên
def entering(s): return bool(re.search(r"(p|t|c|ch)$", base(s)))
SON = ("ngh", "ng", "nh", "m", "n", "l", "v", "d", "gi", "y")
def cls(s):
    b = base(s)
    return "vang" if (b.startswith(SON) or b[0] in "aeiou") else "tac"
SIMPLE = {"ngang": {1}, "huyền": {2}, "hỏi": {3}, "ngã": {3, 4}, "sắc": {4}, "nặng": {4}}

chars = []
for line in open(CHARS, encoding="utf-8"):
    c, lv, n = line.rstrip("\n").split("\t"); chars.append((c, lv, int(n)))
excl = collections.Counter(); excl_lv = collections.defaultdict(collections.Counter)
meas_lv = collections.Counter(); tot_lv = collections.Counter(); via = 0
cells = collections.Counter(); items = []
for c, lv, n in chars:
    tot_lv[lv] += 1
    r, how = vn(c); m = data.get(c, {}).get("kMandarin", "").split()
    reason = None
    if not r: reason = "khong_co_kVietnamese"
    elif len(r) > 1: reason = "nhieu_am_HV"
    elif len(m) == 0: reason = "khong_co_kMandarin"
    elif len(m) > 1: reason = "nhieu_kMandarin"
    if reason: excl[reason] += 1; excl_lv[lv][reason] += 1; continue
    meas_lv[lv] += 1; via += how == "via-trad"
    hv = r[0]; vt = vtone(hv); ent = entering(hv); cl = cls(hv); mt = mtone(m[0])
    cells[(vt, cl, "nhap" if ent else "khong", mt)] += 1
    items.append(dict(char=c, level=lv, hv=hv, via=how, kMandarin=m[0], hv_tone=vt, onset_class=cl,
                      entering="nhap" if ent else "khong", pred_simple="/".join(map(str, sorted(SIMPLE[vt]))),
                      actual=mt, match_simple=int(mt in SIMPLE[vt])))
# dự đoán theo ô (đa số trong chính tập đo: in-sample, chỉ để tham khảo)
modal = {}
for (vt, cl, en, mt), k in cells.items():
    key = (vt, cl, en)
    if key not in modal or k > cells[key + (modal[key],)]: modal[key] = mt
for it in items:
    it["pred_cell_modal"] = modal[(it["hv_tone"], it["onset_class"], it["entering"])]
    it["match_cell_modal"] = int(it["actual"] == it["pred_cell_modal"])
with open(f"{OUT}/tone_rule_items.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(items[0].keys())); w.writeheader(); w.writerows(items)
rows = []
order = ["ngang", "huyền", "hỏi", "ngã", "sắc", "nặng"]
for vt in order:
    for cl in ("tac", "vang"):
        for en in ("khong", "nhap"):
            cnt = {t: cells[(vt, cl, en, t)] for t in range(1, 6)}; n = sum(cnt.values())
            if not n: continue
            top = max(cnt, key=cnt.get)
            rows.append(dict(hv_tone=vt, onset_class=cl, entering=en, n=n, T1=cnt[1], T2=cnt[2], T3=cnt[3], T4=cnt[4], T5=cnt[5],
                             modal_tone=f"T{top}", modal_rate=f"{cnt[top]/n:.3f}"))
with open(f"{OUT}/tone_rule_table.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
summary = dict(total_chars=len(chars), measured=len(items), via_traditional_variant=via, excluded=dict(excl),
               by_level={lv: dict(total=tot_lv[lv], measured=meas_lv[lv], excluded=dict(excl_lv[lv])) for lv in LEVELS},
               simple_rule_match=sum(i["match_simple"] for i in items), cell_modal_match=sum(i["match_cell_modal"] for i in items))
json.dump(summary, open(f"{OUT}/tone_rule_summary.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(summary, ensure_ascii=False, indent=1))
for r in rows: print(r)
