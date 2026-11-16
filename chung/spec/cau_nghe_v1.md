# Đặc tả note type "Câu nghe v1"

*Claude viết ngày 13/11/2026, đã gộp các chỉnh sửa trong `thao_luan/05_Codex_phan_hoi.md` mục 2. Người đọc: Claude và Codex khi build. Trạng thái: **chốt cho lô thử 72 note**, chờ anh duyệt kế hoạch.*

## 1. Nguyên tắc

- Dùng **một note type cho cả ba ngôn ngữ**. Mỗi note sinh đúng **một thẻ "Nghe"**.
- Thẻ chạy offline. Không dùng JS ngoài; CSS nằm trong template.
- Raw trong `chung/raw/` không bao giờ bị sửa. Mọi bản dẫn xuất có tên riêng.
- Mọi thao tác xử lý (crop, merge, đổi định dạng, hash, note ID gốc, kết quả ASR) ghi trong **manifest**, không ghi lên thẻ.
- Bản dịch có sẵn hay bản mới đều bắt đầu ở trạng thái **chưa duyệt**.
- Audio chỉ được coi là "đã nghe duyệt" sau khi **anh nghe**.

## 2. Trường (theo đúng thứ tự)

| # | Trường | Nội dung | Hiện trên thẻ |
|---|---|---|---|
| 1 | `NoteKey` | `<lang>:<SourceID>:<SegmentID>`, ví dụ `ja:loveisblind-jp:1653382674082`. **SegmentID** lấy từ note ID gốc. Nếu nối nhiều note, lấy ID của note đầu và thêm hậu tố `+n`. Hoặc dùng ID phân đoạn do người build cấp, và giữ ổn định. **Không chứa Start.** GUID = hash của NoteKey | Không |
| 2 | `Sentence` | Câu đã sửa: chữ Nhật, chữ Anh, hoặc chữ Hán giản thể | Mặt sau |
| 3 | `Reading` | Chỉ cho tiếng Nhật: furigana kiểu Anki `漢字[かんじ]` | Mặt sau |
| 4 | `Pinyin` | Chỉ cho tiếng Trung: pinyin **cả câu**, có dấu thanh. Đây là pinyin từ điển, không mặc định là phát âm thực tế (biến điệu ghi ở `Notes` khi đã kiểm) | Mặt sau, tô màu thanh điệu |
| 5 | `Audio` | `[sound:cdt_…]` | Mặt trước, tự phát |
| 6 | `Image` | Ảnh chụp cảnh, nếu có. HSK không bắt buộc | Mặt trước |
| 7 | `Translation` | Bản dịch tiếng Việt. Nhánh Nhật dịch **từ câu Nhật đã sửa**, không dịch tiếp từ phụ đề EN | Mặt sau |
| 8 | `TranslationStatus` | `<trạng thái>:<nguồn>`. Trạng thái ∈ `draft` / `unverified` / `reviewed`. Nguồn ∈ `mt:<model>:<ngày>` / `source:<deck>` / `human`. Ví dụ: `unverified:source:GG-P2`, `draft:mt:claude-opus-5-5:2026-11-13` | Nhãn nhỏ khi khác `reviewed` |
| 9 | `SourceSubtitle` | Phụ đề gốc giữ nguyên, ví dụ EN của Netflix. Bản VI mới **không ghi đè** trường này | Mặt sau, thu gọn |
| 10 | `SourceSubtitleLabel` | Ngôn ngữ + nguồn của phụ đề, ví dụ `EN · Netflix` | Cạnh trường 9 |
| 11 | `ContextBefore` | Lời/câu liền trước (chữ) | Mặt sau |
| 12 | `ContextAfter` | Lời/câu liền sau (chữ) | Mặt sau |
| 13 | `Speaker` | Một hoặc nhiều người nói. Đối thoại ghi theo lượt, ví dụ `A=…; B=…`, không ép một tên cho cả đoạn | Mặt sau |
| 14 | `TargetWords` | Từ mục tiêu. **HSK bắt buộc có**: từ + pinyin + nghĩa mục tiêu, lấy từ target-map của gói nguồn. Nhật/Anh để trống trong lô thử | Mặt sau |
| 15 | `LinkKey` | ID **nghĩa đã duyệt**, ví dụ `zh:hsk1:爱:ài:01`. Dùng để nối HSKStory ↔ NewHSK3. **Không dùng bản dịch làm khóa** | Không |
| 16 | `Notes` | Ghi chú người học/người build | Mặt sau |
| 17 | `SourceType` | `RealityTV` / `Sitcom` / `AudiobookCommentary` / `TEDEd` / `TEDTalk` / `HSKStory` / `NewHSK-Listening` | Không |
| 18 | `SourceTitle` | Tên chương trình, sách, video, bài | Mặt sau (dòng nguồn) |
| 19 | `SourceID` | Slug nguồn ổn định, ví dụ `loveisblind-jp`, `ted-amy-cuddy-2012` | Không |
| 20 | `SourceURL` | Link trang gốc, nếu có | Mặt sau (link) |
| 21 | `Episode` | Tập, chương, phần | Mặt sau (dòng nguồn) |
| 22 | `Start` | Thời điểm bắt đầu trong nguồn | Không |
| 23 | `End` | Thời điểm kết thúc | Không |
| 24 | `VoiceType` | `human` / `tts:<engine>` / `unknown`, **theo bằng chứng**. `merged` không phải loại giọng | Nhãn nhỏ "TTS" khi là TTS |
| 25 | `QAStatus` | `NeedsListeningQA` (mặc định, **giữ nguyên sau ASR**) / `ListenedOK` (chỉ sau khi anh nghe) / `Reject` | Không |
| 26 | `TargetAudio` | *(thêm 16/11 khi build HSK)* Audio của riêng từ mục tiêu, nếu nguồn có. Giúp luyện thanh điệu từ đơn | Mặt sau, trong ô từ mục tiêu |

Kết quả ASR **không** có trạng thái riêng trên thẻ. Chỉ lưu trong manifest và tag `asr::flag` khi ASR lệch.

## 3. Template

**Mặt trước:** `{{Audio}}`, kèm `{{#Image}}{{Image}}{{/Image}}`.

**Mặt sau:**
1. Toàn bộ mặt trước.
2. `Sentence`, rồi `Reading` hoặc `Pinyin`.
3. `Translation`, kèm nhãn nếu chưa `reviewed`.
4. `TargetWords`, nếu có.
5. Ngữ cảnh: `ContextBefore` / câu chính / `ContextAfter`.
6. `Speaker`.
7. `SourceSubtitle` + `SourceSubtitleLabel` trong `<details>` (thu gọn).
8. Dòng nguồn: `SourceTitle` · `Episode` · link `SourceURL`; nhãn "TTS" nếu `VoiceType` là TTS.
9. `Notes`.

Tô màu thanh điệu pinyin bằng CSS class do người build gắn sẵn trong trường, không dùng JS. Chỉ tô ở mặt sau.

## 4. Cây deck và tên media

**Cây deck:**
- `Câu đời thật::JA::Hội thoại`
- `Câu đời thật::JA::Bình luận`
- `Câu đời thật::EN::TED-Ed`
- `Câu đời thật::EN::Sitcom`
- `Câu đời thật::EN::TED`
- `Câu đời thật::ZH::HSKStory`
- `Câu đời thật::ZH::NewHSK-Listening`

**Tên media:** `cdt_<lang>_<SourceID>_<SegmentID>_<hash8>.<ext>`. `hash8` là 8 ký tự đầu SHA256 của file đầu ra, để không ghi đè khi sửa.

**Định dạng:** giữ định dạng gốc (MP3/Opus). MP4 TED chỉ tách audio. Chỉ đổi định dạng hàng loạt khi thử trên điện thoại của anh thấy lỗi.

## 5. Manifest (đầu vào cho công cụ FFmpeg của Codex)

Mỗi lô có một file JSON. Mỗi phần tử ứng với một note:

```json
{
  "NoteKey": "ja:loveisblind-jp:1653382674082+1",
  "source_package": {"slug": "ja-subs2srs-love-is-blind-japan", "sha256": "…"},
  "source_note_ids": [1653382674082, 1653382674090],
  "source_media": [{"file": "…mp3", "sha256": "…"}, {"file": "…mp3", "sha256": "…"}],
  "timeline": [{"episode": "E03", "start": "00:12:01.200", "end": "00:12:06.900"}],
  "operation": "copy | crop | merge-intervals | extract-audio",
  "keep_pause_ms": 300,
  "output": {"file": "cdt_ja_loveisblind-jp_1653382674082+1_ab12cd34.mp3", "sha256": "…"},
  "voice_type": "human",
  "asr": {"model": "whisper-small-q5_1", "text": "…", "flags": []},
  "decisions": [{"by": "Claude", "what": "nối 2 lượt cùng người nói, bỏ dòng CC"}]
}
```

**Phân vai:**
- Bên phụ trách nhánh quyết ranh giới ngôn ngữ: Claude cho tiếng Nhật, Codex cho tiếng Anh và tiếng Trung.
- Công cụ của Codex decode / cắt / hợp nhất khoảng / tách audio / kiểm thời lượng, và báo thiếu file hoặc lỗi.
- **Clip chồng thời gian** (Friends 325/365 cặp; có thể cả Love is Blind) phải hợp nhất theo timeline. **Không ghép nguyên khối các MP3**, vì sẽ lặp lời.

## 6. Nghiệm thu lô thử

1. Mọi tham chiếu media tồn tại và decode được.
2. Mỗi audio khớp trọn câu đã chọn: không lẫn credit, nhãn SDH, biến thể ngữ pháp, hay đầu câu kế tiếp.
3. Bản dịch không bị cắt, không đổi chủ thể, không mất phủ định.
4. `SourceID`, `VoiceType` và `TranslationStatus` đúng.
5. Template chạy offline và phát lại được trên Anki desktop và điện thoại của anh.
6. Anh nghe từng thẻ. Thẻ đạt → `ListenedOK`; thẻ lỗi → `Reject` kèm ghi chú.
