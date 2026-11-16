# Vòng 3 — Codex: audit và chốt kế hoạch v2

[đã mở file] 13/11/2026. Đã đọc file 04 và danh sách Claude, mở độc lập đủ bốn gói mới; dùng raw có sẵn. Kiểm toàn bộ tham chiếu/thời lượng, đọc dịch và chạy ASR cục bộ trên **16 mẫu/gói, 64/64 mẫu giải mã được**. [chưa xác minh] Không phải nghe bằng tai hay chứng nhận toàn bộ alignment/giọng/thanh điệu. [Bằng chứng và mẫu thật](../chung/kiem_chung_Codex_vong3/README.md).

## 1. Audit

| Gói | Kết quả | Vai trò |
|---|---|---|
| **Friends S01E02** | [đã mở file] **366 note, 366/366 audio+ảnh**, trung vị **6 từ**, audio **5,28s**; dòng trước/sau có ở 365/366 note mỗi phía. Không có dịch. **325/365 cặp clip liền nhau chồng timeline**, phần chồng trung vị **2,79s**; ASR thường nhận cả lời ngoài Target line. Có credit/nhãn SDH cần loại | [suy luận] **Đáng làm ca thử A thứ hai**: hội thoại/hài hước và trường ngữ cảnh tốt. Cần cắt lại rồi hợp nhất khoảng thời gian, không concat MP3 nguyên khối gây lặp lời. Chưa đủ một chương trình hội thoại C1 |
| **GG P2** | [đã mở file] **391 note**, audio chính **391/391**, trung vị **17 từ /7,11s**, VI **391/391**.16 mẫu ASR nhìn chung tương ứng câu. Có dịch sai/cắt: note 1759738470397 đổi bóng chày thành bóng rổ; note 1759803631237 mất vị ngữ nói việc kinh doanh thay đổi qua đêm | [suy luận] Giữ nhánh giải thích; QA dịch từng câu được chọn, không mặc định toàn bộ đạt |
| **GG P3** | [đã mở file] **407 note**, audio chính **407/407**, trung vị **16 từ /6,77s**, VI **407/407**.16 mẫu ASR nhìn chung tương ứng câu. Note1759921074019 dịch `plot lines` thành “âm mưu”; note 1760535791424 chỉ còn “Trước đây, người ta nghĩ rằng”, mất nội dung chính | [suy luận] Giữ nhánh giải thích sau sửa dịch. Audio ví dụ bổ sung vẫn tách khỏi audio video chính |
| **7000 câu Trung–VI** | [đã mở file] **7.335 note**, **7.334 note có audio**, **7.325 file phân biệt**, trung vị **9 ký tự /2,11s**. Cả 7.325 file có tag **nVoiceTTS@NAVER**, 24 kHz. VI/pinyin có ở 7.335/7.335 note, lần lượt nằm trong `Part of Speech`/`Phrase Chinese`. **7.330/7.335 câu trùng nguyên văn với Spoonfed** | [suy luận] Phụ VI/TTS, **không phải nguồn giọng người mới**, không thêm thành nhánh lõi hoặc nhập cả hai bộ trùng câu |

[đã mở file] Deck Trung: note **1780156028821** thiếu audio; `Phrase Vietnamese` trống toàn bộ dù tên gợi ý bản dịch. Mẫu **1780156034657** đổi sắc thái 纷纷纭纭 thành “lan nhanh như cháy rừng”. [suy luận] Có thể tận dụng VI đã duyệt cho câu Spoonfed tương ứng, không sao chép dịch hàng loạt. [chưa xác minh] Chưa xác định voice/model NAVER; ASR có khác biệt giản/phồn và đồng âm nên không dùng điểm thấp để phán phát âm/thanh điệu sai.

## 2. Đặc tả

[suy luận] Đồng ý một note type và một thẻ nghe, offline, audio trước; sửa các điểm sau trước khi build:

1. **GUID:** bỏ `Start` khỏi khóa định danh. Dùng `Language:SourceID:SourceSegmentID`; SegmentID lấy từ ID note gốc hoặc ID phân đoạn được cấp và giữ ổn định. Sửa timestamp không đổi GUID. Nếu SourceID là video/bài và Start trống như một số nguồn hiện có, khóa cũ còn có nguy cơ trùng. ID gốc, danh sách note được nối và hash media giữ trong manifest.
2. **QA:** giữ `QAStatus=NeedsListeningQA` sau khi chạy ASR; lưu kết quả ASR riêng trong manifest/tag. Chỉ chuyển `ListenedOK` sau anh nghe; không dùng `ASRScreened` thay trạng thái còn chờ nghe. `TranslationStatus` phải chứa **draft/unverified/reviewed**, không chỉ tên nguồn/model; VI có sẵn cũng bắt đầu `source-unverified`.
3. **Nguồn âm:** tách loại giọng (`human/tts:<engine>/unknown`, theo bằng chứng) khỏi thao tác crop/merge/đổi định dạng trong manifest. `original-merged` không tự chứng minh giọng người. Giữ tên media có namespace+SegmentID, kèm hash để tránh đè file khi sửa.
4. **Riêng Trung:** thêm **`Pinyin` cho cả câu**, giữ dạng text có dấu; `Reading` dành furigana Nhật. `Sentence` đã chứa Hanzi nên không cần nhân đôi `Hanzi/Answer`. HSK phải giữ từ mục tiêu, cách đọc và nghĩa mục tiêu trong trường hoặc target-map; **không để mất vì TargetWords trống**. `LinkKey` trỏ ID nghĩa đã duyệt, không dùng bản dịch có thể sửa làm khóa. Tô màu thanh điệu chỉ ở mặt sau; biến điệu/cách đọc thực ghi chú khi đã kiểm, không tự coi pinyin từ điển là phiên âm thực tế.
5. **Bớt trường hiển thị:** Start/End, hash và log xử lý không cần hiện mặc định trên thẻ. Giữ `SourceSubtitle` với ngôn ngữ/nguồn rõ; bản VI mới không ghi đè phụ đề gốc. Đối thoại có thể có nhiều người trong `Speaker`, không ép một tên cho cả đoạn. HSK không cần buộc có ảnh hay gõ chữ trong lô nghe đầu.

## 3. Đồng ý chốt / Còn bất đồng

**[suy luận] Đồng ý chốt kế hoạch v2 để trình anh**, với chỉnh đặc tả ở mục 2. Không còn bất đồng về nguồn chính hay chia việc; chưa có sự duyệt build của anh.

- [suy luận] Đề xuất đưa **4 đoạn Friends đã sửa** thay 4/16 GG trong lô: Anh vẫn 24 = **12 GG + 4 Friends + 8 TED**; Nhật 24, Trung 24, tổng **72 note**. Như vậy thử thêm ca chồng clip mà không tăng tải nghe duyệt. Chưa đưa 7000 câu Trung vào lô đầu.
- [suy luận] **Đồng ý dây chuyền tự trích là giai đoạn 2**, sau khi lô thử đạt; ưu tiên nguồn anh thực sự xem/nghe, không kéo dài tìm deck vô hạn.
- [suy luận] **Codex nhận căn transcript–audio loại B**, cùng manifest/FFmpeg: dùng transcript chính thức làm chuẩn, đối chiếu với ASR có timestamp, đánh dấu thiếu/thừa và kiểm ranh giới; không thay transcript bằng lời máy nhận dạng. Whisper hiện có tạo dữ liệu sàng lọc, **chưa phải bộ forced alignment đã kiểm xong**.
- [đã mở file] Gói 世界のニュース hiện là các clip rời. [suy luận] Lô đầu chứng minh được kiểm/sửa ranh giới clip có sẵn; **chưa chứng minh trọn dây chuyền B từ audio dài + transcript độc lập**. Ca kiểm đó cần đầu vào tương ứng ở giai đoạn 2, không ghép ngược các clip rời rồi coi là nguồn âm gốc đầy đủ.

## 4. Câu hỏi lại

1. [suy luận] Claude có thể chốt spec với khóa SegmentID ổn định, tách ASR khỏi trạng thái chờ nghe và giữ target-map riêng cho HSK như trên?
2. [suy luận] Có thống nhất thay 4 GG bằng 4 Friends, giữ lô 72 và dùng Friends để kiểm xử lý khoảng chồng? Thiết bị/ngôn ngữ dịch cuối vẫn chờ anh xác nhận khi duyệt, không cần mở thêm vòng săn deck cho các nhánh đã chốt.

[đã mở file] Đã cập nhật [ứng viên Codex](../chung/ung_vien_Codex.md). Không sửa file Claude/raw, không build/import deck.
