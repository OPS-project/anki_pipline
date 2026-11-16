# Đề xuất build: Hán Việt vào deck HSK (bản 2, chưa build)

*Điều phối, 16/11/2026, sửa theo phản hồi R6. Người đọc: anh và Codex. Cần duyệt trước khi build.*

**So với bản 1:**
- **Không thêm trường mới.** Dùng trường `Notes` có sẵn (đang trống ở cả 10.898 note).
- **Phần thu gọn giữ đủ** `char_note` và trạng thái chưa chắc.
- **Tạm ẩn cờ ngoại lệ thanh điệu.**

## 1. Dữ liệu đầu vào

Nguồn là `07_final/hanviet_10898.jsonl`. Khóa `note_key` trùng với trường `NoteKey` của deck đang học.

**Dùng để hiển thị:**
- `hanviet`, `nghia_vi`, `loai`, `tu_viet`
- `khac_biet`, `phan_tich{kieu, noi_dung}`, `char_note`
- `status`, `review_reason`, `label`

**Giữ trong JSON, không hiển thị ở bản đầu:**
- `tone_flags` (665 mục): tạm ẩn, chưa review riêng.
- `hanviet_chars[]` (nguồn từng chữ).
- Lịch sử review.

## 2. Ánh xạ: một trường `Notes`, HTML có cấu trúc

Mỗi note, build sinh nội dung `Notes` như sau:

```html
<div class="hv">
  <div class="hv-line"><b>THỦ CƠ</b> · điện thoại di động <span class="hv-tag">ghép nghĩa</span></div>
  <details class="hv-more"><summary>Hán Việt: chi tiết</summary>
    <div>Gợi nhớ: 手 tay + 機 máy → máy cầm tay</div>          <!-- phan_tich, tiền tố Cấu tạo:/Gợi nhớ: -->
    <div>Từ Việt: …</div>                                        <!-- tu_viet, nếu có -->
    <div>Khác biệt: …</div>                                      <!-- khac_biet, nếu có -->
    <div>Ghi chú âm: 宗=tông (từ Việt đọc 'tôn')</div>           <!-- char_note, GIỮ NGUYÊN -->
    <div class="hv-open">Chưa chắc: …</div>                      <!-- chỉ khi status = needs_review: review_reason -->
    <div class="hv-label">bản nháp AI</div>
  </details>
</div>
```

**Quy tắc sinh nội dung:**
- **Dòng luôn hiện** chỉ gồm âm Hán Việt, nghĩa Việt và nhãn loại.
  - Nhãn: cùng dùng / khác dùng / ghép nghĩa / yếu tố / phiên âm / tên riêng.
  - Ẩn nhãn với `khong_giup` và `hu_tu`.
  - `khac_dung` tô màu cảnh báo nhẹ.
- **Phần thu gọn** giữ đủ, theo thứ tự: phân tích, từ Việt, khác biệt, ghi chú âm, trạng thái chưa chắc, nhãn bản nháp.
  - `char_note` đưa vào **nguyên văn**, không lược. Đây là chỗ phân biệt âm có nguồn với từ Việt thông dụng, ví dụ 资源 TƯ NGUYÊN với "từ Việt đọc 'tài'".
  - Mục `needs_review` có thêm dòng "Chưa chắc: <lý do>".
- **Không** hiện `tone_flags`.

**Template:**
- Chuyển `{{Notes}}` từ cuối mặt sau lên ngay dưới ô từ mục tiêu (`TargetWords`).
- Thêm CSS cho `.hv`, `.hv-line`, `.hv-tag`, `.hv-more`, `.hv-open`.
- Mặt trước giữ nguyên (chỉ audio).
- Không dùng JS; `<details>` chạy trên Anki desktop, AnkiDroid và AnkiMobile.

Các trường khác **không đổi**:
- `TargetWords`: chữ, pinyin, nghĩa tiếng Anh.
- `SourceSubtitle`: câu tiếng Anh.
- `Translation`: vẫn trống. Dịch câu sang tiếng Việt là việc riêng.

## 3. Cập nhật deck đang học: phải kiểm trước

Cấu trúc trường không đổi (không thêm trường), chỉ đổi nội dung `Notes` và template. Rủi ro thấp hơn bản 1, nhưng vẫn **không khẳng định trước** rằng import giữ tiến độ.

**Kiểm trên collection tạm** (thư viện `anki` 26.9.4, như khi build bản HSK):
1. Import `Tieng_Trung_HSK_nghe_cau.apkg` hiện tại vào collection tạm.
2. Trả lời khoảng 50 thẻ (`col.sched.answer_card`) để có revlog, due và trạng thái FSRS.
3. Build bản mới: cùng ID note type, cùng `NoteKey` → GUID; `Notes` có khối Hán Việt; template mới.
4. Import bản mới.
5. Kiểm:
   - số note và thẻ không đổi;
   - không có note trùng;
   - revlog, due, interval và FSRS của 50 thẻ không đổi;
   - `Notes` có nội dung, template mới được dùng;
   - render đúng một mục `khac_dung`, một mục có `char_note` "từ Việt đọc", và một mục `needs_review`.
6. Chỉ khuyên anh import khi mọi điều kiện đạt. Nếu template không được cập nhật khi import, ghi lại cách áp template thủ công (Anki → Manage Note Types → Cards).

## 4. Sau bản đầu

- Anh gặp mục sai thì gắn tag `sai-hanviet` trong Anki, để vòng sau xuất ra và sửa.
- Cờ thanh điệu chỉ bật lại sau khi có quyết định riêng. Dữ liệu vẫn nằm trong JSON.
