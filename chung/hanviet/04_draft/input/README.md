# Đầu vào cho người soạn (tự sinh bởi scripts/build_inputs.py)

Sinh bởi Sonnet (pha 2). Nguồn ứng viên: 02_chars/item_hv.jsonl. Định dạng cột: TIEU_CHUAN.md mục 5.

## Tiêu chí chia lô

- Tập KHÓ (hard_NN.tsv, ≤350 mục/file): mục có cờ `has_uncertain` HOẶC `multi_trad_unresolved` HOẶC `syllable_mismatch` HOẶC match_type CVDICT là none/hanzi_only.
- Tập còn lại (batch_NN.tsv, 700 mục/file) giữ thứ tự items.jsonl.

## Số mục mỗi file

- hard_01.tsv: 350
- hard_02.tsv: 350
- hard_03.tsv: 350
- hard_04.tsv: 42
- batch_01.tsv: 700
- batch_02.tsv: 700
- batch_03.tsv: 700
- batch_04.tsv: 700
- batch_05.tsv: 700
- batch_06.tsv: 700
- batch_07.tsv: 700
- batch_08.tsv: 700
- batch_09.tsv: 700
- batch_10.tsv: 700
- batch_11.tsv: 700
- batch_12.tsv: 700
- batch_13.tsv: 700
- batch_14.tsv: 700
- batch_15.tsv: 6

Tổng: 10898 (items.jsonl: 10898). Tập khó: 1092 mục; tập thường: 9806 mục.

## Thống kê certainty (theo số chữ-trong-mục)

- sure: 20084 (93.0%)
- chosen: 719 (3.3%)
- uncertain: 796 (3.7%)
- tổng chữ-trong-mục: 21599

## Số mục mỗi cờ

- has_uncertain: 777
- multi_trad_unresolved: 330
- syllable_mismatch: 0
- cv_not_exact: 52
- hvpinyin_only: 35

## Ghi chú kỹ thuật

- Nhi hóa: `r` dính (diǎnr) hoặc tách (diǎn r) ghép với 儿 ở cuối; 儿 hóa tra hvpinyin/Thiều Chửu theo `er2`.
- Chữ phồn: ưu tiên entry CVDICT/CC-CEDICT khớp pinyin cùng độ dài, rồi OpenCC STPhrases, rồi STCharacters/trad_candidates. Cờ `multi_trad_unresolved` giữ khi chữ còn ≥2 phồn thể (âm vẫn có thể được chọn theo pinyin).
- Bổ sung ngoài quy tắc gốc: khi không có (phồn,pinyin) trong hvpinyin và Thiều Chửu không khớp, thử hvpinyin theo pinyin không dấu thanh (thanh nhẹ/biến điệu 一 不); ghi rõ trong `reason`.
- hvpinyin pinyin `*` coi là khớp mọi pinyin.
- `hvpinyin_only`: mọi ứng viên của một chữ trong mục chỉ đến từ hvpinyin.
