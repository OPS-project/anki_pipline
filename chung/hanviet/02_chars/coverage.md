# Độ phủ nguồn (tự sinh bởi scripts/build_02_chars.py)

Tập chữ: 00_base/chars.txt (3088 chữ giản thể/chung). Tập từ: 00_base/items.jsonl (10898 mục).

Cột "cấp" lấy theo cấp thấp nhất của chữ trong chars.txt.

## Chữ: có ≥1 âm Hán Việt có nguồn

| cấp | số chữ | hợp (≥1 nguồn) | giao (cả 3 nguồn chính) | thieuchuu | hvpinyin | unihan kVietnamese | wiktionary | không có âm |
|---|---|---|---|---|---|---|---|---|
| HSK1 | 248 | 248 | 218 | 248 | 248 | 218 | 127 | 0 |
| HSK2 | 123 | 123 | 107 | 123 | 123 | 107 | 48 | 0 |
| HSK3 | 284 | 284 | 231 | 283 | 284 | 231 | 98 | 0 |
| HSK4 | 441 | 441 | 346 | 437 | 441 | 347 | 110 | 0 |
| HSK5 | 431 | 431 | 336 | 429 | 431 | 337 | 84 | 0 |
| HSK6 | 413 | 413 | 290 | 412 | 413 | 290 | 51 | 0 |
| HSK7-9 | 1148 | 1148 | 618 | 1124 | 1147 | 623 | 81 | 0 |
| ALL | 3088 | 3088 | 2146 | 3056 | 3087 | 2153 | 599 | 0 |

## Cờ

- hv_sources_disagree: 1275
- hv_sources_disjoint: 557
- multi_hv: 1312
- multi_trad: 103

| cấp | multi_hv | multi_trad | hv_sources_disagree | hv_sources_disjoint | no_hv |
|---|---|---|---|---|---|
| HSK1 | 130 | 9 | 129 | 35 | 0 |
| HSK2 | 57 | 6 | 57 | 19 | 0 |
| HSK3 | 143 | 12 | 142 | 40 | 0 |
| HSK4 | 193 | 19 | 187 | 70 | 0 |
| HSK5 | 194 | 14 | 188 | 80 | 0 |
| HSK6 | 161 | 14 | 160 | 69 | 0 |
| HSK7-9 | 434 | 29 | 412 | 244 | 0 |
| ALL | 1312 | 103 | 1275 | 557 | 0 |

## Từ: độ phủ theo nguồn (khớp theo chữ giản thể + pinyin chuẩn hóa)

exact_pinyin_toneless = trùng pinyin nhưng khác thanh (thường thanh nhẹ/đổi thanh). Cột "≥ chữ" = exact_pinyin + toneless + hanzi_only.

| cấp | số mục | CVDICT exact | CVDICT toneless | CVDICT hanzi_only | CVDICT none | CEDICT exact | CEDICT toneless | CEDICT hanzi_only | CEDICT none |
|---|---|---|---|---|---|---|---|---|---|
| HSK1 | 300 | 298 | 1 | 1 | 0 | 298 | 1 | 1 | 0 |
| HSK2 | 197 | 188 | 9 | 0 | 0 | 188 | 9 | 0 | 0 |
| HSK3 | 493 | 487 | 6 | 0 | 0 | 487 | 6 | 0 | 0 |
| HSK4 | 990 | 982 | 6 | 2 | 0 | 982 | 6 | 2 | 0 |
| HSK5 | 1579 | 1576 | 3 | 0 | 0 | 1578 | 1 | 0 | 0 |
| HSK6 | 1777 | 1772 | 3 | 0 | 2 | 1776 | 1 | 0 | 0 |
| HSK7-9 | 5562 | 5543 | 8 | 1 | 10 | 5554 | 4 | 2 | 2 |
| ALL | 10898 | 10846 | 36 | 4 | 12 | 10863 | 28 | 5 | 2 |

## Chữ KHÔNG có âm HV từ bất kỳ nguồn nào (0)


## Chữ chỉ có đúng 1 nguồn (26): theo nguồn

- hvpinyin: 26
