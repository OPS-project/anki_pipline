# Công cụ pha soạn / kiểm / hợp nhất

Chạy từ thư mục `hanviet`, luôn dùng `/c/Python314/python -I scripts/<tên>.py`. Mọi script đọc/ghi UTF-8.
Pipeline: `item_hv.jsonl` -> (soạn TSV) -> `validate_drafts.py` -> `merge_drafts.py` -> `tone_flags.py` -> `merge_drafts.py --tone-flags`.

## validate_drafts.py
```
python -I scripts/validate_drafts.py --inputs 04_draft/input --outs 04_draft/out [--fixes 06_review] \
  --items 00_base/items.jsonl --item-hv 02_chars/item_hv.jsonl --report 05_validate/report.md --json 05_validate/issues.jsonl
```
Mã thoát 1 nếu có lỗi (error), 0 nếu chỉ cảnh báo. Mỗi dòng issues.jsonl: `{note_key,file,code,level,detail}`.
Out ghép: `out/<tên>a.tsv`, `out/<tên>b.tsv` (tên input + hậu tố chữ cái) được coi là các phần của input `<tên>.tsv`.
Fixes: `fixes_*.tsv`, 12 cột (11 + `reviewer`), kiểm từng dòng như out.

Lỗi (error): E_ENCODING, E_HEADER, E_COLS, E_NO_INPUT (out không thuộc input nào), E_NO_OUT (input chưa có out),
E_KEY_MISSING / E_KEY_EXTRA (so với input, hợp các phần), E_KEY_DUP (trùng trong file), E_KEY_DUP_PARTS (trùng giữa các phần),
E_GLOBAL_MISSING (tóm tắt, kèm 20 mẫu) / E_GLOBAL_DUP / E_GLOBAL_UNKNOWN (so với items.jsonl),
E_HANVIET_EMPTY, E_HANVIET_EQ_EMPTY_PRE, E_HV_COUNT (số âm khác số chữ CJK), E_HV_NOT_IN_CANDS, E_HV_Q_STATUS ('?' mà không needs_review),
E_HV_PRE_Q_EQ (hv_pre có '?' mà ghi '='), E_LOAI, E_STATUS, E_PT_KIEU, E_PT_PAIR (pt_kieu rỗng khác pt_noi_dung rỗng),
E_KHAC_BIET (khac_dung thiếu khac_biet), E_TU_VIET_LOAI (tu_viet khi loai không phải cung_dung/khac_dung),
E_REVIEW_REASON, E_NGHIA_EMPTY, E_FIX_REVIEWER, E_FIX_UNKNOWN, E_INPUT_UNREADABLE.
Cảnh báo (warn): W_TU_VIET_EMPTY (cung_dung), W_YEU_TO_NO_PT (loai yeu_to mà pt_noi_dung rỗng), W_NGHIA_LONG (>80 ký tự),
W_NGHIA_COPY_CV (giống cv_vi, >150), W_NULL_STR, W_ENGLISH (>=3 từ ASCII liền; thô), W_HAN_IN_NGHIA, W_NO_CANDS.
loai hợp lệ: cung_dung, khac_dung, ghep_nghia, hu_tu, phien_am, ten_rieng, khong_giup, yeu_to.
Kiểm âm: `reading_key(âm)` phải thuộc tập reading_key của các `cands` của chữ cùng vị trí (item_hv; nếu thiếu thì dùng cột `hv_cands` của input).
report.md: tổng theo mã, theo file, tỷ lệ needs_review và phân bố loai theo file, mục "Lô nghi lệch" (lệch >20 điểm needs_review / >25 điểm một loai so với chung).

## merge_drafts.py
```
python -I scripts/merge_drafts.py --items 00_base/items.jsonl --item-hv 02_chars/item_hv.jsonl --outs 04_draft/out \
  [--fixes 06_review] [--tone-flags 05_validate/tone_flags.jsonl] [--drafted-by-map map.json] [--default-model sonnet] \
  [--expect 10898] --out 07_final/hanviet_10898.jsonl
```
- Giữ thứ tự items.jsonl; thiếu bản soạn -> `needs_review`, `review_reason: "thiếu bản soạn"`. Thoát mã 2 nếu số dòng khác `--expect`, header/cột sai, note_key trùng giữa các out, hoặc fix cho note_key lạ. Từ chối nếu `--out` trùng một file đầu vào.
- `hanviet`: "=" -> `hv_pre` của item_hv. Âm người soạn sửa -> `chosen` đổi theo ứng viên đó, `certainty: "chosen"`, `source` = nguồn của ứng viên (nối bằng dấu phẩy), `note` = char_note. Chữ không đổi giữ nguyên certainty/chosen; `note` lấy `reason` của item_hv nếu certainty `chosen` (char_note, nếu có, ghi đè). `via`: ứng viên có `via` thì dùng, nếu không thì phồn thể duy nhất (hoặc chính chữ nếu không có phồn thể); mơ hồ thì bỏ.
- Ép `needs_review` (nối vào review_reason): âm ngoài cands, số âm lệch số chữ, còn '?', thiếu item_hv.
- `drafted_by`: `--drafted-by-map` (JSON `{"batch_01.tsv": "sonnet:batch_01"}`, tra cả tên không hậu tố) > cột tùy chọn `drafted_by` ở cuối out > `<default-model>:<tên file bỏ hậu tố a/b>`.
- Fixes (`fixes_*.tsv` theo thứ tự tên): dòng sau cùng thay cả dòng; `reviewed_by` = reviewer cuối; `history` = danh sách `{file, reviewer, old:{trường: giá trị cũ}}`.
- tone_flags: chỉ gắn nếu mục không bị đổi âm (người soạn hay fix); nếu đổi thì bỏ cờ cũ, cần chạy lại tone_flags trên bản merge rồi merge lại.
- Trường rỗng bị bỏ. Không có nghia_basis/tu_nguyen (không có đầu vào).

## tone_flags.py
```
python -I scripts/tone_flags.py --item-hv 02_chars/item_hv.jsonl --rules 03_tone/tone_rule_table.csv \
  --out 05_validate/tone_flags.jsonl [--stats 05_validate/tone_flags_stats.json]
```
Cũng nhận bản merge (dùng `hanviet_chars[].hv` và pinyin từ `word_pinyin`). Mỗi mục một dòng `{note_key, tone_flags:[...]}` (rỗng nếu không có cờ). Điều kiện: certainty sure/chosen và có âm, thanh trong từ 1-4 (thanh nhẹ bỏ), ô có `modal_rate>=0.80` và `n>=30` (`--min-rate`, `--min-n`), cờ `ngoai_le` khi thanh thực khác thanh phổ biến nhất của ô. Thống kê: chars_eligible, chars_ngoai_le, skipped theo lý do, by_cell.
Trên item_hv thật (10.898 mục): 12.197 chữ đủ điều kiện, 643 ngoại lệ, 626 mục có cờ.
