# Kiểm tra độc lập Codex — vòng 3

[đã mở file] Ngày 13/11/2026. Đọc bốn APKG Claude đã tải; không đổi raw, không tạo deck hoặc import collection. [Phản hồi chính](../../thao_luan/05_Codex_phan_hoi.md).

| Kết quả | Gói nguồn trong chung/raw | Kiểm tra |
|---|---|---|
| friends | en-sitcom-friends-s01e02 | 366 note, toàn bộ tham chiếu/thời lượng, 16 mẫu giải mã và ASR |
| gg-p2 | en-glassygaia-teded-p2 | 391 note, toàn bộ tham chiếu/thời lượng/ô VI, 16 mẫu giải mã và ASR |
| gg-p3 | en-glassygaia-teded-p3 | 407 note, toàn bộ tham chiếu/thời lượng/ô VI, 16 mẫu giải mã và ASR |
| zh-7000 | zh-vi-7000-shadowing | 7.335 note, toàn bộ tham chiếu/thời lượng/ô VI, metadata của cả 7.325 audio, 16 mẫu giải mã và ASR; đối chiếu câu với Spoonfed |

[đã mở file] Mỗi thư mục có `package_metrics.json` (SHA256 nguồn, fields/templates, media counts), `analysis.json`, `notes.json`, `durations.json`, `samples.json`, `asr_diagnostic.json`. Có 64/64 mẫu giải mã thành PCM và nhận dạng cục bộ; không truyền audio sang dịch vụ ngoài. Mẫu là 16 vị trí cách đều, không phải mẫu xác suất để ước tính tỷ lệ lỗi toàn gói.

[đã mở file] Đếm Anh bằng regex chữ/số, contraction/hyphen nội bộ là một token; bỏ HTML theo ranh giới block, không tách chữ trang trí thành từ mới. Trung đếm ký tự không có khoảng trắng, gồm dấu câu và tên Latin. Các số ≥20 có thể chênh Claude do quy tắc token. “Có audio” là tham chiếu đúng file; không có nghĩa đã nghe chứng nhận.

[đã mở file] Chạy lại từ workspace:

1. `python thao_luan/codex_vong3_audit.py`
2. `python thao_luan/codex_vong3_asr.py`

[đã mở file] ASR dùng Whisper small-q5_1/whisper.cpp v1.9.2 đã lấy ở vòng 2, không cung cấp câu tham chiếu làm prompt. [chưa xác minh] ASR có nhầm tên riêng, đồng âm, giản/phồn thể và tiếng cười; không dùng similarity để kết luận tỷ lệ phát âm sai, đặc biệt không suy ra thanh điệu đúng/sai. Chưa nghe bằng tai hoặc thử UI/điện thoại.

## Phát hiện cần tra cứu

- [đã mở file] `friends/interval_overlap.json`: 325/365 cặp clip liền nhau chồng khoảng thời gian, median phần chồng 2,79 giây. Hai clip đầu là 1,377–5,794s và 3,004–9,048s. ASR của nhiều mẫu chứa lời trước/sau Target line; cần cắt/ghép theo timeline, không concat nguyên file.
- [đã mở file] `zh-7000/voice_metadata.json`: cả 7.325 audio có `TSSE=nVoiceTTS@NAVER`, 24kHz. Chưa định danh voice/model neural hay cũ. `spoonfed_overlap.json`: 7.330/7.335 câu trùng nguyên văn sau bỏ HTML với gói Spoonfed đã có, 7.331 sau chuẩn hóa thêm dấu câu/chữ. Đây là trùng nội dung, không tự chứng minh lịch sử sao chép.
- [đã mở file] `zh-7000/analysis.json`: chỉ note 1780156028821 (“我真不聪明。”) không có Audio Chinese; không có tham chiếu audio trỏ file mất. 7.334 note dùng 7.325 tên file phân biệt. `Part of Speech` chứa VI, `Phrase Chinese` chứa pinyin; `Phrase Vietnamese` trống toàn bộ.
- [đã mở file] `translation_lengths` trong analysis là ứng viên theo hình thức, **không phải danh sách mọi lỗi dịch**. Kiểm ngữ nghĩa bên dưới được ghi riêng.

## Mẫu lỗi/giới hạn dịch đã đọc

| Nguồn/note | Nhận xét |
|---|---|
| GG P2 1759738470397 | [đã mở file] Ví dụ `throwing a baseball` thành “ném bóng vào rổ”; đổi môn thể thao. |
| GG P2 1759803631237 | [đã mở file] Câu về công việc kinh doanh thay đổi sau một đêm; VI chỉ giữ danh ngữ “Việc kinh doanh mà bạn gây dựng qua nhiều thế hệ”, mất vị ngữ. |
| GG P2 1759803631213 | [đã mở file] Câu về quay ngược thời gian rồi tái sinh; VI dừng sau quay ngược thời gian, mất vế tái sinh. Đây là mẫu bổ sung ngoài 16 vị trí. |
| GG P3 1759921073992 | [đã mở file] Câu hỏi so sánh ba nhân vật với anh hùng thần thoại; VI bỏ Frodo và thêm mở đầu “Điều gì đã làm nên…”. |
| GG P3 1759921074019 | [đã mở file] `plot lines` thành “âm mưu”, mất nghĩa các tuyến truyện trong bối cảnh cấu trúc kể chuyện. |
| GG P3 1760535791426 | [đã mở file] VI rút còn khắt khe với bản thân làm đe dọa đáng sợ hơn; mất cơ chế thêm cảm xúc tiêu cực gắn với công việc. |
| GG P3 1760535791424 | [đã mở file] Câu nói quan niệm người trì hoãn cần kỷ luật/quản lý thời gian; VI chỉ “Trước đây, người ta nghĩ rằng”. Mẫu bổ sung ngoài 16 vị trí. |
| ZH 1780156034657 | [đã mở file] 纷纷纭纭 trong câu tin đồn được dịch thành “lan truyền nhanh như cháy rừng”; chuyển sắc thái nhiều lời/phiên bản rối rắm sang tốc độ. |
| Friends 1571962152737 | [đã mở file] Chỉ nhãn phụ đề SDH, ASR blank; không phải lời thoại cần học. |

[đã mở file] GG P2/P3 có VI ở mọi note và audio chính ở mọi note, nhưng các ví dụ trên bác bỏ suy luận “ô không trống = dịch đủ/đúng”. Audio phụ trong Word_Example vẫn tách khỏi audio chính; nguồn chính theo video/provenance, chưa nghe chứng nhận từng clip.

[suy luận] Friends dùng làm ca kiểm loại A có chồng clip; GG P2/P3 bổ sung nhánh giải thích sau QA câu được chọn; ZH7000 là bản câu gần trùng Spoonfed với NAVER TTS và VI, không phải nhánh giọng người mới. Không thêm toàn bộ vào bộ học hoặc tự động lấy mọi ô VI làm chuẩn.
