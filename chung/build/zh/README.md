# Tiếng Trung HSK: deck nghe câu

## Bản 2 (16/11/2026): thêm Hán Việt

File mới: **`Tieng_Trung_HSK_nghe_cau_v2_hanviet.apkg`**. File bản 1 vẫn giữ nguyên, không bị ghi đè.

**Cập nhật deck đang học:**
1. Trong Anki: **File → Create Backup** (để chắc ăn).
2. **File → Import** file v2. Anki sẽ cập nhật 10.898 note có sẵn, không tạo thẻ mới.
3. Sync lên AnkiWeb, rồi sync điện thoại.

**Đã kiểm trên collection Anki 26.9.4 tạm** (script `scripts/test_update_v2.py`):
- Import bản 1, học thử 50 thẻ với FSRS, rồi import bản 2.
- 0 note mới, 10.898 note cập nhật, số thẻ không đổi.
- revlog và lịch (due, interval, FSRS) của 50 thẻ đã học **không đổi**.
- Template mới được áp; 10.898/10.898 note có khối Hán Việt.
- **Chưa thử trên điện thoại.**

**Trên thẻ:**
- Mặt trước vẫn chỉ có audio.
- Mặt sau, dưới ô từ mục tiêu, có thêm:
  - **Dòng luôn hiện:** âm Hán Việt · nghĩa Việt · nhãn (cùng dùng / khác dùng / ghép nghĩa / yếu tố…). Nhãn "khác dùng" tô màu cam, vì đó là bẫy nghĩa.
  - **"Hán Việt: chi tiết"** (bấm để mở): phân tích / gợi nhớ, từ Việt, khác biệt, ghi chú âm, "Chưa chắc: …" (nếu có), nhãn "bản nháp AI".
- Cờ thanh điệu tạm ẩn.

**Tìm thẻ trong Anki:**
- `tag:hanviet::needs_review` cho 43 thẻ có âm Hán Việt chưa chắc.
- Gặp mục sai thì gắn tag `sai-hanviet`.

Dữ liệu nguồn và báo cáo kiểm định: `chung/hanviet/`.

---

## Bản 1

*Claude build ngày 16/11/2026 theo `chung/spec/cau_nghe_v1.md`. Người đọc: anh.*

## Cài đặt

1. Trong Anki desktop, chọn **File → Import**, import lần lượt:
   - `00_Phat_am_thanh_dieu_helq.apkg` (phát âm, thanh điệu: 193 thẻ)
   - `Tieng_Trung_HSK_nghe_cau.apkg` (HSK1–9: 10.898 thẻ)
2. Cả hai tự vào chung một deck lớn **"Tiếng Trung HSK"**.
3. Sync lên AnkiWeb, rồi sync về điện thoại.

## Cấu trúc deck

```
Tiếng Trung HSK
├── 00 Phát âm & thanh điệu (helq)   ← học 2–4 tuần đầu, song song HSK1
├── HSK1      3 phần × 100 từ
├── HSK2      2 phần
├── HSK3      5 phần
├── HSK4     10 phần
├── HSK5     16 phần
├── HSK6     18 phần
└── HSK7-9   28 phần × 200 từ
```

**Bấm học ở deck lớn "Tiếng Trung HSK".** Anki sẽ tự lấy thẻ mới theo thứ tự trên: hết Phần 01 mới sang Phần 02. Muốn ôn riêng một phần thì bấm vào phần đó.

## Mỗi thẻ

- **Mặt trước:** chỉ có audio câu. Nghe, cố hiểu ý, rồi nói lại theo.
- **Mặt sau:**
  - Audio câu phát lại.
  - Chữ Hán; từ đang học được gạch chân và tô màu theo thanh.
  - Pinyin cả câu tô màu theo thanh: đỏ = 1, xanh lá = 2, xanh dương = 3, tím = 4, nâu = nhẹ. Pinyin ghi theo cách đọc trong câu, ví dụ 一 đọc **yí** trước 个.
  - Nghĩa tiếng Anh.
  - Ô từ mục tiêu: chữ, pinyin, nghĩa, kèm audio của riêng từ đó.

**Chấm:** nghe hiểu cả câu → Good; hiểu lờ mờ hoặc phải nhìn chữ mới hiểu → Again.

## Nên chỉnh trong Anki (Deck options của "Tiếng Trung HSK")

- **New cards/day:** 10–15 lúc đầu, mỗi thẻ khoảng 1 phút kể cả ôn. Anh chưa cho biết thời gian học, nên đây chỉ là gợi ý.
- **FSRS:** bật, Desired retention **0,90**.
- **New card gather order:** để mặc định **Deck**, để thẻ đi đúng thứ tự phần.

## Giới hạn hiện tại

- **Bản dịch là tiếng Anh**, lấy từ HSKStory, chưa duyệt. Anh chưa trả lời có muốn tiếng Việt máy dịch không; trường `Translation` để trống sẵn, khi cần thì thêm sau mà không mất tiến độ học.
- **Giọng đọc HSKStory chưa xác minh** là người thật hay giọng máy (`VoiceType=unknown`). Chưa ai nghe duyệt toàn bộ.
- **Chưa có:** NewHSK3 Listening (câu nghe thêm, để sau), Spoonfed.
- Thứ tự từ trong mỗi cấp giữ theo HSKStory (xếp theo chữ), không theo độ khó.

## Cập nhật sau này

Mỗi note có khóa ổn định (`NoteKey`). Bản build sau, ví dụ khi thêm bản dịch tiếng Việt, import đè lên sẽ **cập nhật nội dung mà giữ nguyên lịch ôn**.

## Kỹ thuật

- Nguồn: `research/downloads/hskstory1–7.apkg` (Codex tải), `chung/raw/helq-mandarin-ear-training/`. Không sửa file nguồn.
- Script: `scripts/`. Manifest từng note: `manifest_hskstory.json`.
- Đã import thử vào collection Anki 26.9.4 tạm: 11.091 thẻ, 97 deck, không thiếu media, không trùng.
