# Công cụ chuẩn bị pha review ngữ nghĩa

Chạy từ thư mục `hanviet`, dùng `/c/Python314/python -I scripts/<tên>.py`. Chỉ đọc đầu vào, UTF-8. Cả hai cần JSON hợp nhất (`merge_drafts.py`).

## char_consistency.py

```
python -I scripts/char_consistency.py --merged 07_final/hanviet_10898.jsonl --item-hv 02_chars/item_hv.jsonl \
  --out-md 06_review/char_consistency.md --out-tsv 06_review/char_consistency.tsv [--examples 6]
```
- Gom âm Hán Việt đã dùng (`hanviet_chars[].hv`, so bằng `reading_key`) theo (chữ giản thể, âm tiết pinyin có số thanh từ `item_hv.chars[].syl`) và theo riêng chữ (syl = `*`).
- MD: nhóm có >=2 âm, sắp theo số mục; mỗi nhóm: các âm + số mục, danh sách ứng viên có nguồn (cands của item_hv), tối đa 6 ví dụ (xoay vòng giữa các âm): hanzi, word_pinyin, hanviet, âm chữ này, nghia_vi, note_key, drafted_by.
- Mục cuối: chữ có âm `certainty: chosen` mà khác `chosen` của item_hv (người soạn đổi so với script tự chọn), thống kê theo chữ: `hv_pre -> âm mới` và số lần.
- TSV: `char syl reading count note_keys` (note_keys nối bằng `,`); các dòng `syl=*` là nhóm theo riêng chữ.
- Nhiều âm cho cùng (chữ, pinyin) không nhất thiết sai (đa âm HV theo nghĩa/từ); đây là danh sách để soi.

## make_review_inputs.py

```
python -I scripts/make_review_inputs.py --merged 07_final/hanviet_10898.jsonl --inputs 04_draft/input \
  --outdir 06_review/inputs [--seed 20261116] [--split 400]
```
Tập không chồng nhau, ưu tiên theo thứ tự:
1. `set_hard`: mọi mục thuộc `hard_*.tsv`.
2. `set_needs`: `status=needs_review` (ngoài set_hard). Gồm cả mục thiếu bản soạn.
3. `set_khac`: `loai=khac_dung` (ngoài hai tập trên).
4. `set_sample`: mẫu phân tầng từ phần còn lại: theo level x loai lấy `max(3, ceil(5%))` mỗi ô (ô nhỏ hơn thì lấy hết; chọn bằng `random.Random(f"{seed}:{level}:{loai}")` trên danh sách sắp theo note_key, nên tái lập), cộng toàn bộ mục `loai` thuộc `phien_am`, `ten_rieng`.

Đầu ra: `set_<tên>.tsv` (hoặc `set_<tên>_NN.tsv` nếu `--split N`, mỗi file <=N dòng), `manifest.json` (seed, cột, tập -> note_keys, tập -> file). In kích thước các tập và bảng ô mẫu.

Cột (22): `note_key` | ngữ cảnh lấy từ input TSV theo note_key: `level hanzi word_pinyin meaning_en sentence sentence_en hv_cands cv_vi ce_en tc_char` | giá trị hiện tại từ bản hợp nhất: `hanviet` (chuỗi âm đầy đủ, không dùng "=") `nghia_vi loai tu_viet khac_biet pt_kieu pt_noi_dung status review_reason char_note drafted_by`.
- `pt_kieu`, `pt_noi_dung` = `phan_tich.kieu`, `phan_tich.noi_dung`.
- `char_note`: ghép ghi chú theo chữ trong bản hợp nhất, dạng `chữ: note; ...` (từ `hanviet_chars[].note`).
- Tab/xuống dòng trong giá trị bị đổi thành khoảng trắng.
