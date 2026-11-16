# 00_base: kiểm kê deck

Người làm: Sonnet. Script: `scripts/build_items.py` (chạy `python -I build_items.py <ROOT> <thư mục tạm>`). Chỉ đọc gói đã build, không sửa gói.

## Cách trích
1. Giải `collection.anki2` từ `chung/build/zh/Tieng_Trung_HSK_nghe_cau.apkg` vào thư mục tạm (scratchpad), đọc bảng `notes` (id, guid, flds tách bằng `\x1f`) theo thứ tự field trong đặc tả.
2. Duyệt `manifest_hskstory.json` theo thứ tự `items[]`; ghép mỗi mục với note theo `NoteKey`.
3. `hanzi`, `word_pinyin`, `meaning_en` lấy từ `TargetWords`. Lưu ý: `TargetWords` có span lồng nhau (`tw-hanzi` chứa các `<span class="tone ...">`), nên tách theo mốc `tw-hanzi|tw-pinyin|tw-meaning` rồi bỏ HTML.
4. `sentence` = `Sentence` bỏ HTML; `target_in_sentence` = nối các ký tự trong `<span class="target ...">` theo thứ tự; `sentence_pinyin` = `Pinyin` bỏ HTML.
5. `sentence_en` lấy từ **`SourceSubtitle`** (phụ đề EN của HSKStory). Field `Translation` trong gói hiện **trống** ở cả 10.898 mục (chờ dịch Việt).
6. `level` = field `Episode` ("HSK1".."HSK7-9"); `source_note_id` = `source_note_ids[0]` (mọi mục chỉ có 1 id).

## Số liệu kiểm
| Kiểm | Kết quả |
|---|---|
| Số dòng `items.jsonl` | 10.898 (khớp `notes` trong manifest và số note trong gói) |
| `note_key` duy nhất | 10.898 / 10.898 |
| `anki_guid` duy nhất | 10.898 / 10.898 |
| `anki_note_id` duy nhất | 10.898 / 10.898 |
| Theo cấp | HSK1 300, HSK2 197, HSK3 493, HSK4 990, HSK5 1.579, HSK6 1.777, HSK7-9 5.562 (khớp `summary` của manifest) |
| Đối chiếu với `research/inspection/hskstoryN/notes.json`, ghép theo (cấp, id gốc) | 10.898 mục đều tìm được nguồn; **0 lệch** ở Hanzi, Meaning, TonePinyin, ExampleHanzi, ExamplePinyin, ExampleEnglish (so sau khi bỏ HTML) |
| `hanzi` xuất hiện ở hơn một mục | **0** (không có đồng hình giữa các cấp). Tức 10.898 mục = 10.898 từ khác nhau |
| `hanzi` chứa ký tự không phải CJK | 0 |
| Từ một chữ | 1.503 mục |
| `hanzi` không nằm trong `sentence` | 0 |
| `target_in_sentence` khác `hanzi` | 62 mục (xem dưới) |
| Chữ CJK khác nhau trong `hanzi` | 3.088 (HSK1 248, HSK2 123, HSK3 284, HSK4 441, HSK5 431, HSK6 413, HSK7-9 1.148, tính theo cấp xuất hiện sớm nhất) |

## Điểm bất thường
- **62 mục có từ mục tiêu xuất hiện hai (hoặc ba) lần trong câu**, và cả hai lần đều được bọc `target`, nên `target_in_sentence` là `hanzi` lặp (ví dụ `喜欢喜欢`, `晚晚晚`). Không phải từ bị tách hay biến thể. Ai dùng `target_in_sentence` làm chuỗi so khớp cần xử lý lặp.
- `Translation` trống toàn bộ; tiếng Anh nằm ở `SourceSubtitle`.
- `note id` gốc trùng giữa các cấp nên mọi đối chiếu phải theo (cấp, id).
- `chars.txt`: mỗi dòng `ký tự<TAB>cấp xuất hiện sớm nhất<TAB>số mục chứa ký tự`; số mục đếm mỗi mục một lần dù chữ lặp trong từ.

## Băm
- `Tieng_Trung_HSK_nghe_cau.apkg` sha256 `4f0f0b64d608676ea17c5ce15aa1ca116e6ab9c1c07508e8c88440bfd8437562`
- `manifest_hskstory.json` sha256 `e4457d98609ed3f2aa4fb4ed474f11039ca37b140f4baea28fbbb7adc5c0d084`
