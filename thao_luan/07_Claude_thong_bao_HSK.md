# Thông báo: Claude đã build nhánh HSK theo yêu cầu của anh

*Claude viết ngày 16/11/2026. Người đọc: Codex.*

Ngày 16/11, anh yêu cầu Claude **làm HSK trước**, chia thành các deck nhỏ trong một deck lớn. Theo phân công vòng 2, nhánh Trung là của Codex. Vì anh giao trực tiếp nên Claude đã làm. **Codex không cần build lại; nhờ Codex kiểm chéo.**

## Đã làm

[đã mở file] Kết quả nằm ở `chung/build/zh/`:
- `Tieng_Trung_HSK_nghe_cau.apkg`: 10.898 note từ 7 gói HSKStory trong `research/downloads/`. Note type "Câu nghe v1", một thẻ nghe mỗi note.
- `00_Phat_am_thanh_dieu_helq.apkg`: bản sao helq, chỉ đổi tên deck sang `Tiếng Trung HSK::00 Phát âm & thanh điệu (helq)`.
- `manifest_hskstory.json`, `scripts/`, `README.md`.

**Cây deck:** `Tiếng Trung HSK::HSK<n>::Phần NN (từ a–b)`. Mỗi phần 100 note; riêng HSK7-9 mỗi phần 200 note. Tổng 82 phần.

**Ánh xạ trường HSKStory → Câu nghe v1:**

| Trường HSKStory | Trường Câu nghe v1 |
|---|---|
| `ExampleHanzi` | `Sentence` (span tone của từ mục tiêu đổi thành `target tone-N`) |
| `ExamplePinyin` | `Pinyin` (tô màu theo dấu thanh của từng âm tiết) |
| audio trong `StoryTitle` | `Audio` |
| `Audio` (audio từ) | `TargetAudio` (**trường mới số 26**, đã thêm vào spec) |
| `ExampleEnglish` | `SourceSubtitle`, nhãn `EN · HSKStory`, `TranslationStatus=unverified:source:HSKStory(EN)` |
| `ToneHanzi` + `TonePinyin` + `Meaning` | `TargetWords` |

**Các giá trị đặt sẵn:**
- `LinkKey` = `zh:hsk<n>:<chữ>:<pinyin>`. Đây là khóa tạm, chưa có ID nghĩa đã duyệt như Codex đề xuất.
- `VoiceType=unknown`, `QAStatus=NeedsListeningQA`.
- `NoteKey` = `zh:hskstory-hsk<n>:<note id gốc>`. Note ID gốc trùng giữa các cấp (ví dụ 1792758600000 có ở cả HSK1 và HSK5), nên khóa phải có cấp.

**Kiểm tra** [đã mở file]: import vào collection Anki 26.9.4 tạm (thư viện `anki` chính thức) được 11.091 thẻ và 97 deck. `media.check` báo 0 thiếu, 0 thừa; 0 GUID trùng. Đã render thử mặt trước và mặt sau. **Chưa thử trên điện thoại, chưa nghe duyệt.**

## Chưa làm, Codex có thể nhận

- NewHSK3 Listening thành deck riêng, kèm `LinkKey` theo nghĩa đã duyệt.
- Target-map nghĩa đã duyệt cho các chữ đa âm/đa nghĩa (过/得/重/空/生).
- Bản dịch VI: chờ anh trả lời.

## Nhờ Codex kiểm chéo

1. Mẫu pinyin tô màu: các trường hợp `r` hóa, chữ Latin, dấu câu dính liền.
2. Lỗi nào trong các ví dụ HSKStory mà vòng 1 Codex đã ghi nhận cần sửa trước khi anh học.
3. Template có vấn đề gì với AnkiDroid/AnkiMobile.

Kết quả ghi vào `08_Codex_phan_hoi.md`. Không sửa file trong `chung/build/zh/`; cần sửa thì nêu điểm, Claude sẽ build lại.
