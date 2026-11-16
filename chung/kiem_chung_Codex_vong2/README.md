# Bằng chứng kiểm tra chéo Codex — vòng 2

Ngày 13/11/2026. [đã mở file] Đây là kết quả đọc gói và mẫu kiểm tra; **không phải deck học đã build**. Raw của Claude được đọc nguyên trạng. [Phản hồi chính](../../thao_luan/03_Codex_phan_hoi.md).

## Nguồn và phạm vi

| Thư mục kết quả | APKG nguồn trong chung/raw | Kiểm tra |
|---|---|---|
| love-is-blind | ja-subs2srs-love-is-blind-japan | Toàn 8.064 note/media;16 mẫu PCM+ASR |
| sekai-news | ja-subs2srs-audiobook-sekai-no-news | Toàn 1.941 note/media;16 mẫu PCM+ASR |
| djg | ja-djg-grammar-sentences-audio | Toàn 5.279 note/media;16 mẫu PCM+ASR, thêm file trả lời của một hội thoại |
| ted-amy | en-zh-ted-amycuddy-video | Toàn 255 note/tham chiếu;16 mẫu MP4 giải mã+ASR |
| glassy-p4 | en-glassygaia-teded-p4 | Toàn 367 note/media, độ dài và ô dịch; không lấy mẫu ASR vòng này |

[đã mở file] Mỗi thư mục có `package_metrics.json`: SHA256 gói nguồn, fields/templates, note/card/deck counts, media và tham chiếu hỏng; `analysis.json`: thống kê độc lập. Bốn gói chính còn có `notes.json`, `durations.json`, `samples.json`, các mẫu âm thanh và `asr_diagnostic.json`. [review.json](review.json) ghi kết luận định tính, mẫu có lỗi/đáng kiểm và giới hạn.

## Quy tắc đo

- [đã mở file] Text bỏ HTML, ruby readings, furigana bracket và control; không tạo khoảng trắng giả quanh inline styling. Nhật đếm ký tự có dấu câu, bỏ whitespace. Love is Blind thêm bản bỏ ngoặc ghi tên người/annotation; **không bỏ ngoặc ngữ pháp trong DJG khi so với Claude**. Anh giữ contraction và hyphen nội bộ thành một token.
- [đã mở file] `nonempty_fields` đếm text hiển thị, vì thế field chỉ chứa ảnh/audio có thể bằng0. Dùng **`nonempty_raw_fields`** để biết field có dữ liệu HTML/sound thực; dùng audio_present_notes cho độ phủ file. Không nhầm ảnh bị strip HTML với thiếu ảnh.
- [đã mở file] Thời lượng MP3 Love is Blind và Sekai đo toàn bộ file duy nhất bằng mutagen. DJG có 1.532 file không đọc được durationbằng mutagen; **không coi chúng là file hỏng**. Các mẫu đó giải mã FFmpeg thành công. MP4 TED cũng lấy thời lượng từ PCM đã giải mã, không suy từ duration rỗng trong mutagen.
- [đã mở file] `sample_decode_success` và thời lượng PCM ghi trong analysis; 64/64 mẫu chính giải mã được. Mẫu lấy16 chỉ số cách đều từ đầu đến cuối, **không phải mẫu ngẫu nhiên**, không dùng để ước tính phần trăm lỗi toàn bộ.
- [đã mở file] ASR chạy tại máy, dùng [whisper.cpp v1.9.2](https://github.com/ggml-org/whisper.cpp/releases/tag/v1.9.2) và [Whisper small-q5_1](https://huggingface.co/ggerganov/whisper.cpp). Không cung cấp câu đúng làm prompt. CLI/model và nguồn/SHA256 nằm tại `research/tools/whisper-cpp-v1.9.2/sources.json`.
- [chưa xác minh] ASR không phải người nghe, có thể nhận sai từ đồng âm/tên riêng và hallucinate với tiếng cười/nhạc. Similarity văn bản không phải CER/WER đã chuẩn hóa theo cách đọc. Lần đầu chỉ lấy file audio đầu/note; DJG 3167 được kiểm thêm file trả lời để tránh kết luận nhầm cắt đối thoại.

## Tái lập

[đã mở file] Chạy bằng Python từ workspace, với `PYTHONIOENCODING=utf-8`:

1. `python thao_luan/codex_vong2_audit.py` — mở bốn APKG và xuất dữ liệu/mẫu; không tạo cards/deck.
2. `python thao_luan/codex_vong2_setup_asr.py` — lấy CLI/model công khai về thư mục công cụ riêng, không dùng tài khoản.
3. `python thao_luan/codex_vong2_asr.py` — nhận dạng64 mẫu, lưu kết quả.

[đã mở file] `codex_vong2_review.py` tổng hợp ghi chú chuyên môn và cần hai mẫu `dialogue_3167_part0/1` đã trích riêng từ hai sound refs của note 1508885376236; đây là bằng chứng bổ sung, không phải output learning cards. GG P4 được kiểm thêm bằng hàm load/lengths của `codex_vong1_audit.py`, lưu kết quả riêng trong glassy-p4.

[suy luận] Khi build được duyệt, cần chọn câu và nghe duyệt thật từng mục trong lô; không biến mọi file trong thư mục kiểm tra thành thẻ học.
