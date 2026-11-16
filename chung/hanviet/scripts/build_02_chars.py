"""Build 02_chars/chars.jsonl, words_source.jsonl, coverage.md from 01_sources.
Usage: python -I -X utf8 build_02_chars.py <hanviet_dir>
Chỉ đọc dữ liệu nguồn (JSON/CSV/văn bản), không thực thi gì từ nguồn.
"""
import sys, os, json, re, csv, ast, unicodedata, collections

H = sys.argv[1]
S = os.path.join(H, '01_sources')
OUT = os.path.join(H, '02_chars')
nfc = lambda s: unicodedata.normalize('NFC', s)
cp = lambda c: 'U+%04X' % ord(c)
isc = lambda c: '一' <= c <= '鿿' or '㐀' <= c <= '䶿' or '\U00020000' <= c <= '\U0002ffff'

# ---------- base
chars = []
for l in open(f'{H}/00_base/chars.txt', encoding='utf8'):
    p = l.rstrip('\n').split('\t')
    chars.append((p[0], p[1], int(p[2])))
items = [json.loads(l) for l in open(f'{H}/00_base/items.jsonl', encoding='utf8')]

# ---------- Unihan
uni = collections.defaultdict(dict)
for fn in ('Unihan_Readings.txt', 'Unihan_Variants.txt'):
    for l in open(f'{S}/unihan/ex/{fn}', encoding='utf8'):
        if l.startswith('#') or not l.strip():
            continue
        u, k, v = l.rstrip('\n').split('\t', 2)
        uni[chr(int(u[2:], 16))][k] = v
def uvar(c, k):
    v = uni.get(c, {}).get(k)
    if not v: return []
    return [chr(int(x.split('<')[0][2:], 16)) for x in v.split()]

# ---------- OpenCC
st = {}
for l in open(f'{S}/opencc/STCharacters.txt', encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k, v = l.rstrip('\n').split('\t'); st[k] = v.split()
ts = {}
for l in open(f'{S}/opencc/TSCharacters.txt', encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k, v = l.rstrip('\n').split('\t'); ts[k] = v.split()

# ---------- Thieu Chuu (dataV4.json; OCR/gõ lại từ bản 1942)
t = open(f'{S}/thieuchuu/hanviet/dataV4.json', encoding='utf8').read()
tc_list = json.loads(t[t.index('['):t.rindex(']') + 1])
tc = collections.defaultdict(list)
for x in tc_list:
    tc[x['ky_tu']].append(x)
tc_simp = collections.defaultdict(set)   # giản thể -> {phồn} theo trường tu_lien_quang_2
for x in tc_list:
    for s in re.findall(r'\S', x.get('tu_lien_quang_2', '') or ''):
        if isc(s) and s != x['ky_tu']:
            tc_simp[s].add(x['ky_tu'])

def short_meanings(nghia, n=2, mx=140):
    out = []
    for ln in nghia.split('\n'):
        ln = re.sub(r'\s+', ' ', ln).strip()
        if len(ln) < 3: continue
        out.append(ln if len(ln) <= mx else ln[:mx].rstrip() + '…')
        if len(out) >= n: break
    return out

# ---------- hvpinyin (ph0ngp, MIT)
hp = collections.defaultdict(list)
with open(f'{S}/hvpinyin/hanviet.csv', encoding='utf8', newline='') as f:
    for r in csv.DictReader(f):
        try: rd = ast.literal_eval(r['hanviet'])
        except Exception: rd = [r['hanviet']]
        hp[r['char']].append((rd, r['pinyin']))

# ---------- kaikki (Wiktionary) nếu có
kk = collections.defaultdict(list)
kpath = f'{S}/kaikki/viet_readings.json'   # do script trích riêng (extract_kaikki.py)
if os.path.exists(kpath):
    for c, v in json.load(open(kpath, encoding='utf8')).items():
        kk[c] = v

TONEMARKS = {'́': 's', '̀': 'f', '̉': 'r', '̃': 'x', '̣': 'j'}
def rd_key(r):
    d = unicodedata.normalize('NFD', r.lower()); t = ''; base = ''
    for ch in d:
        if ch in TONEMARKS: t = TONEMARKS[ch]
        else: base += ch
    return unicodedata.normalize('NFC', base).replace('y', 'i') + t

def norm_rd(r):
    return nfc(r.strip().lower())

# ---------- build chars
SRCN = ['thieuchuu', 'hvpinyin', 'unihan_kVietnamese', 'wiktionary']
rows = []
for c, lvl, cnt in chars:
    # trad candidates
    tcands = {}
    def addt(ch, src):
        if ch != c:
            tcands.setdefault(ch, [])
            if src not in tcands[ch]: tcands[ch].append(src)
    for ch in uvar(c, 'kTraditionalVariant'): addt(ch, 'unihan_kTraditionalVariant')
    for ch in st.get(c, []): addt(ch, 'opencc_STCharacters')
    for ch in sorted(tc_simp.get(c, [])): addt(ch, 'thieuchuu_tu_lien_quang')
    tlist = [{'char': ch, 'source': ss} for ch, ss in tcands.items()]
    # chữ tra: chính nó + các phồn thể
    via = [c] + list(tcands)
    hv = []
    for v in via:
        for x in tc.get(v, []):
            for rd in re.split(r'[,;]', x['am_han']):
                rd = norm_rd(rd)
                if rd:
                    hv.append({'reading': rd, 'source': 'thieuchuu', 'via_char': v,
                               'meanings_vi': short_meanings(x['nghia']),
                               'pinyin_hint': x['pinyin'] or None})
        for rds, py in hp.get(v, []):
            for rd in rds:
                hv.append({'reading': norm_rd(rd), 'source': 'hvpinyin', 'via_char': v,
                           'meanings_vi': [], 'pinyin_hint': None if py == '*' else py})
        kv = uni.get(v, {}).get('kVietnamese')
        if kv:
            for rd in kv.split():
                hv.append({'reading': norm_rd(rd), 'source': 'unihan_kVietnamese', 'via_char': v,
                           'meanings_vi': [], 'pinyin_hint': None})
        for rd, hint in kk.get(v, []):
            hv.append({'reading': norm_rd(rd), 'source': 'wiktionary', 'via_char': v,
                       'meanings_vi': [], 'pinyin_hint': hint})
    # bỏ trùng hoàn toàn
    seen = set(); hv2 = []
    for h in hv:
        k = (h['reading'], h['source'], h['via_char'])
        if k in seen: continue
        seen.add(k); hv2.append(h)
    hv = hv2
    flags = []
    for h in hv: h['reading_key'] = rd_key(h['reading'])
    rds_all = {h['reading_key'] for h in hv}
    if not hv: flags.append('no_hv')
    if len(rds_all) > 1: flags.append('multi_hv')
    if len(tlist) > 1: flags.append('multi_trad')
    bysrc = collections.defaultdict(set)
    for h in hv: bysrc[h['source']].add(h['reading_key'])
    if len(bysrc) >= 2:
        sets = list(bysrc.values())
        if any(a != b for a in sets for b in sets): flags.append('hv_sources_disagree')
        if any(not (a & b) for i, a in enumerate(sets) for b in sets[i + 1:]): flags.append('hv_sources_disjoint')
    if c not in tc and not any(v in tc for v in via) and hv: pass
    rows.append({'char': c, 'level': lvl, 'count': cnt, 'trad_candidates': tlist, 'hv_candidates': hv,
                 'mandarin': {'kMandarin': uni.get(c, {}).get('kMandarin'),
                              'kHanyuPinyin': uni.get(c, {}).get('kHanyuPinyin')},
                 'flags': flags})
with open(f'{OUT}/chars.jsonl', 'w', encoding='utf8') as f:
    for r in rows: f.write(json.dumps(r, ensure_ascii=False) + '\n')

# ---------- pinyin chuẩn hóa
TONE = {'ā': ('a', 1), 'á': ('a', 2), 'ǎ': ('a', 3), 'à': ('a', 4), 'ē': ('e', 1), 'é': ('e', 2), 'ě': ('e', 3), 'è': ('e', 4),
        'ī': ('i', 1), 'í': ('i', 2), 'ǐ': ('i', 3), 'ì': ('i', 4), 'ō': ('o', 1), 'ó': ('o', 2), 'ǒ': ('o', 3), 'ò': ('o', 4),
        'ū': ('u', 1), 'ú': ('u', 2), 'ǔ': ('u', 3), 'ù': ('u', 4), 'ǖ': ('v', 1), 'ǘ': ('v', 2), 'ǚ': ('v', 3), 'ǜ': ('v', 4)}
def py_marked(s):
    s = nfc(re.sub(r'<[^>]+>', '', s)).lower().replace('ü', 'v')
    out = ''
    for syl in re.split(r"[\s'·\-]+", s):
        if not syl: continue
        tone = 5; r = ''
        for ch in syl:
            if ch in TONE: ch, tone = TONE[ch]
            r += ch
        out += r + str(tone)
    return out.replace('u:', 'v')
def py_numeric(s):
    out = ''
    for syl in re.split(r"[\s'·\-]+", s.lower()):
        syl = syl.replace('u:', 'v').replace('ü', 'v')
        if not syl: continue
        if not syl[-1].isdigit(): syl += '5'
        out += syl
    return out

def load_cc(path):
    d = collections.defaultdict(list)
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        m = re.match(r'^(\S+) (\S+) \[([^\]]*)\] /(.*)/\s*$', l)
        if not m: continue
        tr, sm, py, defs = m.groups()
        d[sm].append({'trad': tr, 'pinyin': py, 'defs': [x for x in defs.split('/') if x], 'pn': py_numeric(py)})
    return d
cv = load_cc(f'{S}/cvdict/CVDICT.u8')
ce = load_cc(f'{S}/cedict/cedict_ts.u8')

def match(d, hz, pn):
    es = d.get(hz, [])
    ex = [e for e in es if e['pn'] == pn]
    if ex: return 'exact_pinyin', ex
    # khớp pinyin bỏ thanh (ví dụ khác thanh nhẹ)
    ex = [e for e in es if re.sub(r'\d', '', e['pn']) == re.sub(r'\d', '', pn)]
    if ex: return 'exact_pinyin_toneless', ex
    if es: return 'hanzi_only', es
    return 'none', []

stats = collections.Counter(); bylvl = collections.defaultdict(collections.Counter)
with open(f'{OUT}/words_source.jsonl', 'w', encoding='utf8') as f:
    for it in items:
        hz = it['hanzi']; pn = py_marked(it['word_pinyin'])
        m1, e1 = match(cv, hz, pn); m2, e2 = match(ce, hz, pn)
        f.write(json.dumps({'note_key': it['note_key'], 'level': it['level'], 'hanzi': hz, 'word_pinyin': it['word_pinyin'],
                            'match_type': m1, 'match_type_cedict': m2,
                            'cvdict': [{'trad': e['trad'], 'pinyin': e['pinyin'], 'meanings_vi': e['defs']} for e in e1],
                            'cedict': [{'trad': e['trad'], 'pinyin': e['pinyin'], 'meanings_en': e['defs']} for e in e2],
                            'meaning_en_deck': it.get('meaning_en')}, ensure_ascii=False) + '\n')
        for nm, m in (('cvdict', m1), ('cedict', m2)):
            stats[(nm, m)] += 1; bylvl[it['level']][(nm, m)] += 1
        bylvl[it['level']]['n'] += 1

# ---------- coverage.md
lv = sorted({r['level'] for r in rows})
L = []
L.append('# Độ phủ nguồn (tự sinh bởi scripts/build_02_chars.py)\n')
L.append(f'Tập chữ: 00_base/chars.txt ({len(rows)} chữ giản thể/chung). Tập từ: 00_base/items.jsonl ({len(items)} mục).\n')
L.append('Cột "cấp" lấy theo cấp thấp nhất của chữ trong chars.txt.\n')
def has(r, s): return any(h['source'] == s for h in r['hv_candidates'])
L.append('## Chữ: có ≥1 âm Hán Việt có nguồn\n')
L.append('| cấp | số chữ | hợp (≥1 nguồn) | giao (cả 3 nguồn chính) | thieuchuu | hvpinyin | unihan kVietnamese | wiktionary | không có âm |')
L.append('|---|---|---|---|---|---|---|---|---|')
tot = collections.Counter()
for l in lv + ['ALL']:
    rs = [r for r in rows if l == 'ALL' or r['level'] == l]
    u = sum(1 for r in rs if r['hv_candidates'])
    i = sum(1 for r in rs if has(r, 'thieuchuu') and has(r, 'hvpinyin') and has(r, 'unihan_kVietnamese'))
    L.append(f"| {l} | {len(rs)} | {u} | {i} | {sum(has(r,'thieuchuu') for r in rs)} | {sum(has(r,'hvpinyin') for r in rs)} | {sum(has(r,'unihan_kVietnamese') for r in rs)} | {sum(has(r,'wiktionary') for r in rs)} | {len(rs)-u} |")
L.append('\n## Cờ\n')
fl = collections.Counter(x for r in rows for x in r['flags'])
for k, v in sorted(fl.items()): L.append(f'- {k}: {v}')
L.append('\n| cấp | multi_hv | multi_trad | hv_sources_disagree | hv_sources_disjoint | no_hv |')
L.append('|---|---|---|---|---|---|')
for l in lv + ['ALL']:
    rs = [r for r in rows if l == 'ALL' or r['level'] == l]
    L.append(f"| {l} | " + ' | '.join(str(sum(k in r['flags'] for r in rs)) for k in ('multi_hv', 'multi_trad', 'hv_sources_disagree', 'hv_sources_disjoint', 'no_hv')) + ' |')
L.append('\n## Từ: độ phủ theo nguồn (khớp theo chữ giản thể + pinyin chuẩn hóa)\n')
L.append('exact_pinyin_toneless = trùng pinyin nhưng khác thanh (thường thanh nhẹ/đổi thanh). Cột "≥ chữ" = exact_pinyin + toneless + hanzi_only.\n')
L.append('| cấp | số mục | CVDICT exact | CVDICT toneless | CVDICT hanzi_only | CVDICT none | CEDICT exact | CEDICT toneless | CEDICT hanzi_only | CEDICT none |')
L.append('|---|---|---|---|---|---|---|---|---|---|')
for l in sorted(bylvl) + ['ALL']:
    if l == 'ALL':
        g = lambda nm, m: sum(v for (a, b), v in stats.items() if a == nm and b == m); n = len(items)
    else:
        g = lambda nm, m, l=l: bylvl[l][(nm, m)]; n = bylvl[l]['n']
    L.append(f'| {l} | {n} | ' + ' | '.join(str(g(nm, m)) for nm in ('cvdict', 'cedict') for m in ('exact_pinyin', 'exact_pinyin_toneless', 'hanzi_only', 'none')) + ' |')
nohv = [r for r in rows if not r['hv_candidates']]
L.append(f'\n## Chữ KHÔNG có âm HV từ bất kỳ nguồn nào ({len(nohv)})\n')
for r in nohv:
    L.append(f"- {r['char']} ({r['level']}, {r['count']} mục) trad={''.join(t['char'] for t in r['trad_candidates']) or '-'} kMandarin={r['mandarin']['kMandarin']}")
only1 = [r for r in rows if r['hv_candidates'] and len({h['source'] for h in r['hv_candidates']}) == 1]
L.append(f'\n## Chữ chỉ có đúng 1 nguồn ({len(only1)}): theo nguồn\n')
c1 = collections.Counter(next(iter({h['source'] for h in r['hv_candidates']})) for r in only1)
for k, v in c1.items(): L.append(f'- {k}: {v}')
open(f'{OUT}/coverage.md', 'w', encoding='utf8').write('\n'.join(L) + '\n')
print('\n'.join(L[:60]))
