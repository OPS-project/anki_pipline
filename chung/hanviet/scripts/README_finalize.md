# finalize.py: tạo bộ dữ liệu bàn giao cuối

Chạy từ thư mục `hanviet`:
```
/c/Python314/python -I scripts/finalize.py [--outdir 07_final] [--tmp <thư mục tạm>]
```
Chạy được cả khi chưa có `log_r5_*` / `fixes_r5_*` (vòng nào có file thì tính vòng đó). Không sửa đầu vào.

## Các bước
1. `merge_drafts.py` (có `--fixes 06_review`, `--drafted-by-map`, `--expect 10898`) -> `tone_flags.py` trên bản merge -> merge lại (file trung gian ở `--tmp`).
2. Khôi phục `char_note` cấp mục: lấy từ dòng mới nhất của note_key (theo thứ tự `04_draft/out/*.tsv`, rồi `06_review/fixes_*.tsv` theo tên file), dọn đoạn rác (log script: "hvpinyin nhiều âm", "lọc theo Thiều Chửu còn", chuỗi chỉ gồm khóa kiểu `qua5,qua1`) và đoạn trùng (tách theo `; ` hoặc ` | `, nối lại bằng `; `). Dòng mới nhất có char_note rỗng thì mục không có char_note.
3. Cờ thanh `tone_flags` lấy thẳng từ kết quả `tone_flags.py` chạy trên bản merge (khớp âm hiện tại; merge_drafts tự bỏ cờ của mọi mục có dòng fix nên script gắn lại).
4. Gắn `label` và `reviewed_in`.
5. Kiểm cuối (thoát mã 1 nếu sai): đủ 10.898 dòng đúng thứ tự `items.jsonl`; note_key duy nhất; số âm = số chữ CJK; mọi `hv` (trừ `?`) có reading_key trong `cands` của item_hv; `loai`/`status` hợp lệ.

## Đầu ra trong `--outdir`
- `hanviet_10898.jsonl`: đầy đủ (`hanviet_chars`, `phan_tich`, `history`, `tone_flags`...).
- `hanviet_10898.tsv`: phẳng, UTF-8 BOM, mở bằng Excel.
- `needs_review.tsv`: mục `needs_review` kèm lý do.
- `stats.json`, `stats.md`: thống kê.

## Trường thêm so với merge
- `label`: luôn `bản nháp AI`. Không có trạng thái "đã xác minh".
- `char_note`: ghi chú cấp mục về cách đọc chữ (đã dọn).
- `reviewed_in`: danh sách vòng đã KIỂM mục: `r1` (có trong fixes_r1_doc_am), `r2:<tập>`, `r4:<tập>`, `r5:<tập>` (theo `log_r*_<tập>.tsv`). Được kiểm khác với đã xác minh.
- `tone_ngoai_le` (TSV): `chữ:thanh_thực→thanh_dự_đoán`, vd `境:3→4`.
- `status`, `review_reason`, `drafted_by`, `reviewed_by`, `history`: giữ từ merge.

## Thống kê
Theo loai/status/level, số mục có phân tích, có cờ thanh ngoại lệ, độ phủ review theo vòng, drafted_by, số mục được sửa theo vòng (tên file `fixes_<vòng>_*`) và theo reviewer.
