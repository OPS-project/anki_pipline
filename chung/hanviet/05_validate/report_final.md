# Báo cáo kiểm bản soạn

- Mục trong items.jsonl: 10898
- Mục có đúng một bản soạn: 10898; thiếu: 0; trùng: 0; lạ: 0
- File out: 33; file input: 19; file fixes: 18
- Lỗi: 15; cảnh báo: 15

## Theo mã

| Mức | Mã | Số lượng |
|---|---|---|
| error | E_HV_COUNT | 1 |
| error | E_HV_NOT_IN_CANDS | 1 |
| error | E_TU_VIET_LOAI | 13 |
| warn | W_ENGLISH | 13 |
| warn | W_HAN_IN_NGHIA | 2 |

## Theo file

| File | Lỗi | Cảnh báo |
|---|---|---|
| batch_01b.tsv | 13 | 0 |
| batch_02b.tsv | 0 | 2 |
| batch_03a.tsv | 0 | 1 |
| batch_03b.tsv | 0 | 1 |
| batch_05b.tsv | 0 | 1 |
| batch_06a.tsv | 0 | 1 |
| batch_07b.tsv | 0 | 1 |
| batch_08a.tsv | 1 | 1 |
| batch_08b.tsv | 0 | 1 |
| batch_09b.tsv | 0 | 1 |
| batch_10b.tsv | 0 | 1 |
| batch_11a.tsv | 0 | 1 |
| batch_11b.tsv | 1 | 0 |
| batch_12b.tsv | 0 | 1 |
| fixes_r4_set_cd_04.tsv | 0 | 1 |
| hard_03.tsv | 0 | 1 |

## needs_review theo file

| File | Số mục | needs_review | Tỷ lệ |
|---|---|---|---|
| batch_01a.tsv | 350 | 1 | 0.3% |
| batch_01b.tsv | 350 | 1 | 0.3% |
| batch_02a.tsv | 350 | 2 | 0.6% |
| batch_02b.tsv | 350 | 0 | 0.0% |
| batch_03a.tsv | 350 | 0 | 0.0% |
| batch_03b.tsv | 350 | 0 | 0.0% |
| batch_04a.tsv | 350 | 2 | 0.6% |
| batch_04b.tsv | 350 | 1 | 0.3% |
| batch_05a.tsv | 350 | 2 | 0.6% |
| batch_05b.tsv | 350 | 1 | 0.3% |
| batch_06a.tsv | 350 | 1 | 0.3% |
| batch_06b.tsv | 350 | 1 | 0.3% |
| batch_07a.tsv | 350 | 0 | 0.0% |
| batch_07b.tsv | 350 | 0 | 0.0% |
| batch_08a.tsv | 350 | 0 | 0.0% |
| batch_08b.tsv | 350 | 5 | 1.4% |
| batch_09a.tsv | 350 | 4 | 1.1% |
| batch_09b.tsv | 350 | 4 | 1.1% |
| batch_10a.tsv | 350 | 0 | 0.0% |
| batch_10b.tsv | 350 | 1 | 0.3% |
| batch_11a.tsv | 350 | 3 | 0.9% |
| batch_11b.tsv | 350 | 3 | 0.9% |
| batch_12a.tsv | 350 | 0 | 0.0% |
| batch_12b.tsv | 350 | 0 | 0.0% |
| batch_13a.tsv | 350 | 0 | 0.0% |
| batch_13b.tsv | 350 | 0 | 0.0% |
| batch_14a.tsv | 350 | 0 | 0.0% |
| batch_14b.tsv | 350 | 1 | 0.3% |
| batch_15.tsv | 6 | 0 | 0.0% |
| hard_01.tsv | 350 | 2 | 0.6% |
| hard_02.tsv | 350 | 1 | 0.3% |
| hard_03.tsv | 350 | 1 | 0.3% |
| hard_04.tsv | 42 | 1 | 2.4% |
| **Tổng** | 10898 | 38 | 0.3% |

## Phân bố loai theo file (% mục)

| File | cung_dung | ghep_nghia | hu_tu | khac_dung | khong_giup | phien_am | ten_rieng | yeu_to |
|---|---|---|---|---|---|---|---|---|
| batch_01a.tsv | 9% | 43% | 9% | 4% | 6% | 0% | 0% | 29% |
| batch_01b.tsv | 26% | 41% | 5% | 7% | 6% | 1% | 0% | 15% |
| batch_02a.tsv | 24% | 45% | 4% | 7% | 5% | 0% | 0% | 13% |
| batch_02b.tsv | 26% | 46% | 5% | 8% | 5% | 1% | 0% | 10% |
| batch_03a.tsv | 29% | 45% | 3% | 6% | 7% | 0% | 0% | 11% |
| batch_03b.tsv | 39% | 39% | 3% | 9% | 3% | 0% | 1% | 6% |
| batch_04a.tsv | 31% | 47% | 1% | 9% | 5% | 0% | 0% | 7% |
| batch_04b.tsv | 35% | 45% | 1% | 7% | 5% | 0% | 0% | 8% |
| batch_05a.tsv | 33% | 44% | 1% | 7% | 6% | 1% | 0% | 9% |
| batch_05b.tsv | 34% | 48% | 3% | 7% | 3% | 0% | 1% | 3% |
| batch_06a.tsv | 36% | 50% | 2% | 4% | 4% | 0% | 0% | 5% |
| batch_06b.tsv | 26% | 55% | 1% | 5% | 7% | 1% | 0% | 6% |
| batch_07a.tsv | 29% | 52% | 2% | 5% | 4% | 0% | 0% | 9% |
| batch_07b.tsv | 25% | 60% | 1% | 6% | 3% | 0% | 0% | 5% |
| batch_08a.tsv | 27% | 61% | 2% | 5% | 1% | 0% | 0% | 4% |
| batch_08b.tsv | 29% | 60% | 2% | 3% | 3% | 1% | 0% | 3% |
| batch_09a.tsv | 26% | 62% | 0% | 4% | 6% | 1% | 0% | 2% |
| batch_09b.tsv | 31% | 55% | 2% | 4% | 5% | 0% | 0% | 3% |
| batch_10a.tsv | 27% | 65% | 1% | 3% | 2% | 0% | 0% | 2% |
| batch_10b.tsv | 22% | 61% | 0% | 7% | 6% | 0% | 0% | 3% |
| batch_11a.tsv | 16% | 66% | 0% | 4% | 11% | 0% | 0% | 3% |
| batch_11b.tsv | 25% | 65% | 1% | 4% | 3% | 1% | 0% | 1% |
| batch_12a.tsv | 17% | 71% | 0% | 4% | 5% | 0% | 0% | 4% |
| batch_12b.tsv | 23% | 60% | 1% | 5% | 8% | 0% | 0% | 3% |
| batch_13a.tsv | 16% | 68% | 1% | 3% | 6% | 0% | 0% | 5% |
| batch_13b.tsv | 30% | 56% | 1% | 3% | 5% | 1% | 0% | 4% |
| batch_14a.tsv | 21% | 65% | 0% | 4% | 7% | 0% | 0% | 3% |
| batch_14b.tsv | 23% | 63% | 0% | 5% | 4% | 1% | 0% | 4% |
| batch_15.tsv | 17% | 67% | 0% | 0% | 0% | 0% | 0% | 17% |
| hard_01.tsv | 23% | 27% | 10% | 8% | 16% | 0% | 0% | 16% |
| hard_02.tsv | 23% | 50% | 3% | 4% | 9% | 0% | 0% | 11% |
| hard_03.tsv | 19% | 51% | 1% | 3% | 17% | 0% | 0% | 9% |
| hard_04.tsv | 12% | 50% | 2% | 2% | 17% | 0% | 0% | 17% |
| **Tổng** | 26% | 54% | 2% | 5% | 6% | 0% | 0% | 7% |

## Lô nghi lệch

- hard_01.tsv: loai=ghep_nghia chiếm 27% (chung 54%)
