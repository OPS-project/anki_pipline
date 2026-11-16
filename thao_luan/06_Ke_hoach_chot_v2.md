# Kế hoạch chốt v2: trình anh duyệt

*Claude viết ngày 13/11/2026, sau 3 vòng thảo luận với Codex (`01`–`05`). Codex đã ghi "đồng ý chốt" trong `05_Codex_phan_hoi.md`. Người đọc: anh (Codex cũng đọc).*

## 1. Kết luận

Không có deck làm sẵn nào đạt hết yêu cầu của anh. Kế hoạch là **ghép một số deck đã kiểm**, sửa lại theo một mẫu thẻ chung (nghe trước, có ngữ cảnh, dịch tiếng Việt, ghi nguồn), rồi **mở rộng dần**.

Hai mảng chưa có deck làm sẵn đủ tốt:
- Tiếng Anh: hội thoại, phim, podcast, tin tức.
- Tiếng Nhật: tin tức hiện thời.

Hai mảng này sẽ lấp ở **giai đoạn 2**, bằng cách tự trích câu từ phim và podcast anh thật sự xem/nghe, qua cùng dây chuyền xử lý của lô thử.

## 2. Nguồn chọn cho từng ngôn ngữ

| Ngôn ngữ | Nhánh | Nguồn | Ghi chú |
|---|---|---|---|
| **Nhật** | Hội thoại đời thật | **Love is Blind Japan** (8.064 clip) | Lời nói thật của người lớn: hẹn hò, gia đình, công việc, tiền bạc. Phải nối các dòng phụ đề thành lượt nói trọn ý |
| | Bình luận xã hội, câu dài | **世界のニュースを日本人は何も知らない** (audiobook, 1.941 câu) | Trung vị 50 ký tự, người thật đọc (bản Audible). Sách 2019, nên **không phải tin tức hiện thời** |
| | Ngữ pháp (phụ) | DJG Sentences | Chỉ tra khi gặp cấu trúc khó trong media |
| | Sau | TEDxSapporo, Hanzawa, từ N1 qua Immersion Kit | Khi nhánh chính đã chạy |
| **Anh** | Giải thích, kiến thức | **GLASSY-GAIA TED-Ed** P1–P4 (1.597 câu) | Audio gốc, có bản dịch VI nhưng **có lỗi dịch**, phải duyệt từng câu |
| | Diễn thuyết | **TED Amy Cuddy** (+3 talk sau) | Giọng thuyết trình thật |
| | Hội thoại (thử) | **Friends S01E02** | Lời thoại sitcom thật, chỉ 1 tập; dùng để thử xử lý clip chồng nhau |
| | Sắc thái từ | OALD | Chỉ tra khi gặp cụm thật |
| **Trung** | Nền nghe câu | **HSKStory** (chuyển sang nghe trước) | Theo khung HSK 3.0 |
| | Câu nghe thêm | **NewHSK3 Listening** (deck riêng) | Giọng AI, có nhãn |
| | Thanh điệu | helq | Học song song |
| | Sau | Spoonfed | Deck "7000 câu shadowing" trùng gần hết Spoonfed và dùng giọng máy NAVER, nên không thêm |

**Đã loại khỏi bản đầu:** Tango N1 làm lõi, OALD học tuần tự, Cún/socialge, 暗唱/DUO, NativShark, Miku.

## 3. Lô thử: 72 thẻ

| Ngôn ngữ | Thành phần | Người làm |
|---|---|---|
| Nhật (24) | 12 lượt nói Love is Blind (≥3 tập, ≥3 loại cảnh, ≥3 đối thoại hai người) + 12 câu 世界のニュース | Claude |
| Anh (24) | 12 GG TED-Ed + 4 Friends + 8 TED Amy Cuddy | Codex |
| Trung (24) | 16 HSKStory HSK1 + 8 NewHSK3 Listening | Codex |

- Công cụ cắt/ghép audio dùng chung: Codex.
- Mẫu thẻ dùng chung: Claude. Đặc tả nằm ở `chung/spec/cau_nghe_v1.md`.
- Bản dịch tiếng Việt mới do Claude/Codex dịch, gắn nhãn **"bản nháp máy dịch"**. Bản dịch có sẵn trong deck gốc gắn nhãn **"chưa duyệt"**.

**Mỗi thẻ:**
- Mặt trước: chỉ nghe (kèm ảnh cảnh nếu có).
- Mặt sau: câu, cách đọc (furigana/pinyin), bản dịch VI, câu trước/sau, người nói, nguồn.

**Nghiệm thu:**
- Claude và Codex kiểm file và lọc bằng nhận dạng giọng nói trên máy.
- Sau đó **anh nghe 72 thẻ trên điện thoại** (khoảng 20–25 phút) và đánh dấu thẻ lỗi.
- Đạt thì mở rộng từng nhánh.

## 4. Sau lô thử

1. **Mở rộng nhánh chính:** toàn bộ Love is Blind (sau lọc), toàn bộ 世界のニュース, GG P1–P4, 4 talk TED, HSKStory các cấp. Làm theo từng đợt, mỗi đợt kiểm mẫu.
2. **Giai đoạn 2, tự trích:** phim/series anh xem (Netflix, YouTube có phụ đề do người làm), bản tin tiếng Nhật, podcast tiếng Anh có transcript. Chỉ dùng cá nhân, không chia sẻ lại.

## 5. Cần anh trả lời để bắt đầu

1. **Duyệt kế hoạch này** để Claude và Codex build lô thử 72 thẻ?
2. **iPhone hay Android?**
3. **Bản dịch VI máy dịch** (có nhãn) được không?
4. **Mỗi ngày học Anki bao nhiêu phút** cho mỗi ngôn ngữ?
5. **Anh nghe duyệt 72 thẻ thử** được không?
