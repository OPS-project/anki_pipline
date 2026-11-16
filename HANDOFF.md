# Handoff: mang dự án Anki về máy nhà

*Claude viết ngày 16/11/2026, trên máy công ty. Người đọc: anh, và phiên Claude Code (hoặc Codex) mới trên máy nhà. Phiên Claude ở máy nhà không có trí nhớ của máy công ty, nên mọi điều cần biết nằm trong file này.*

## 1. Người học và cách làm việc

**Người học:** anh, người Việt, học 3 thứ tiếng.

| Tiếng | Trình độ | Mục tiêu |
|---|---|---|
| Trung | Mới bắt đầu, đã học xong phát âm | Nghe trước. Biết chữ Hán nhờ tiếng Nhật. |
| Nhật | N2 → N1 | Hiểu và nói được tiếng Nhật tự nhiên ngoài N1 |
| Anh | C1 | Diễn đạt tốt hơn, lên C2 |

**Anh muốn:**
- Câu đời thật, câu dài, nhiều cách diễn đạt: phim, thời sự, bình luận, thuyết trình. Không học danh sách từ thi cử; danh sách từ chỉ dùng làm mục tiêu.
- Không cần deck hoàn hảo. Ghép nhiều deck "đủ tốt" lại cũng được.

**Cách làm việc:**
- Trả lời bằng tiếng Việt, gọi người dùng là "anh", ngắn gọn.
- Claude và Codex cùng làm trong thư mục này, trao đổi qua file đánh số trong `thao_luan/` (`01_…`, `02_…`).
  - Không sửa file của bên kia.
  - Không sửa gì trong `chung/raw/`.
- Chỉ build khi anh đã duyệt kế hoạch.
- Bản dịch máy phải ghi nhãn "bản nháp máy dịch"; nội dung AI soạn ghi nhãn "bản nháp AI".

## 2. Trạng thái

### Tiếng Trung: xong bản 2, anh đã import

- Deck **"Tiếng Trung HSK"** trong Anki của anh: 10.898 thẻ, 82 phần trong 90 deck con, chưa học thẻ nào.
  - Mặt trước chỉ có audio câu.
  - Mặt sau có thêm khối Hán Việt ở trường `Notes`.
- File: [`chung/build/zh/Tieng_Trung_HSK_nghe_cau_v2_hanviet.apkg`](chung/build/zh/Tieng_Trung_HSK_nghe_cau_v2_hanviet.apkg), đưa lên git qua LFS. Cách cài và kết quả kiểm: [`chung/build/zh/README.md`](chung/build/zh/README.md).
- Preset FSRS riêng **"Trung – nghe câu"**:
  - 15 thẻ mới/ngày, lấy thẻ mới theo thứ tự deck.
  - retention 0,85, dùng bộ tham số FSRS cũ của anh.
  - Preset Default và các deck khác giữ nguyên.
- Deck phát âm helq đã xóa theo yêu cầu (chưa học thẻ nào).
- Dữ liệu Hán Việt: [`chung/hanviet/`](chung/hanviet/README.md).
  - Báo cáo kiểm định: `reports/bao_cao_kiem_dinh.md`.
  - 43 mục còn chưa chắc, có tag `hanviet::needs_review`.
  - Anh gặp mục sai thì gắn tag `sai-hanviet`.

### Tiếng Nhật và tiếng Anh: đang thảo luận, chưa build gì

**Kế hoạch cũ:** [`thao_luan/06_Ke_hoach_chot_v2.md`](thao_luan/06_Ke_hoach_chot_v2.md). Ghép deck có sẵn (Love is Blind Japan, 世界のニュース, TED-Ed GLASSY-GAIA, Amy Cuddy, Friends) rồi làm lô thử. Anh **chưa duyệt** kế hoạch này.

**Hướng mới (16/11):** anh muốn học từ **video thật anh tự xem**, nhưng không muốn tự cắt từng câu. Claude đề xuất ba phần, anh chưa chốt.

1. **Cách A: bấm một phím khi đang xem.**
   - Dùng asbplayer (extension trình duyệt, chạy được với Netflix và YouTube), gửi thẻ vào Anki qua AnkiConnect.
   - Claude chạy theo lô để bổ sung cho các thẻ mới bấm: dịch Việt, sắc thái (nói với ai, lịch sự hay suồng sã), cách nói tương đương, câu trước và sau.
2. **Cách B: anh đưa link, máy cắt câu.**
   - Áp dụng cho YouTube hoặc file video có sẵn. Netflix không tải được.
   - Các bước: tải audio và phụ đề (thiếu phụ đề thì chạy Whisper trên máy) → nối thành câu trọn ý → lọc câu "dùng được ngoài đời" → khoảng 15–20 câu mỗi video → anh bỏ tick câu không thích → tạo thẻ.
   - Có thể lọc theo những từ anh đã biết, lấy từ chính collection Anki của anh.
3. **Loại thẻ mới "Câu dùng":** mỗi câu sinh 2 thẻ.
   - **Thẻ nghe:** mặt trước là audio, mặt sau là câu và nghĩa.
   - **Thẻ nói:** mặt trước là tình huống bằng tiếng Việt, anh tự nói câu, rồi lật xem câu gốc và nghe audio.

**Còn chờ anh trả lời:**
1. Anh xem chủ yếu trên Netflix hay YouTube? Kênh hoặc show nào?
2. Thẻ nói với tình huống tiếng Việt ở mặt trước có hợp ý anh không?
3. Muốn duyệt danh sách câu trước khi tạo thẻ, hay đẩy thẳng vào Anki rồi xóa thẻ dở?

**Ghi chú:** Immersion Kit là kho câu cắt sẵn từ 14 drama và anime. Chỉ có tiếng Nhật, kho đứng yên từ 01/2025. Hợp để lấp từ N1 chưa biết bằng câu phim, qua add-on Aobana Reibun (chưa cài thử). Chi tiết ở [`reports/Bộ thẻ Anki ba ngôn ngữ.md`](reports/).

### Việc treo khác

- Codex chưa phản hồi `07_Claude_thong_bao_HSK.md` (kiểm chéo HSK) và chưa nhận xét các báo cáo Hán Việt.
- Chỉnh số thẻ mới/ngày khi anh cho biết mỗi ngày học bao nhiêu phút.
- Trong collection còn 4 note type helq không dùng (Chinese Tones, Minimal pair sounds, Spellings and sounds, Basic++). Anh xóa tay trong Tools → Manage Note Types nếu muốn. Chạy thêm Tools → Check Media → Delete Unused để xóa audio helq thừa.
- Đề nghị anh đổi mật khẩu AnkiWeb. File cookie AnkiWeb trên máy công ty đã xóa ngày 16/11.

## 3. Cài trên máy nhà

### 3.1. SSH key cho GitHub

Mỗi máy dùng key riêng. Không chép private key từ máy công ty sang. Trên máy nhà (Git Bash):

```bash
ssh-keygen -t ed25519 -C "may-nha"          # Enter để giữ đường dẫn mặc định; nên đặt passphrase
cat ~/.ssh/id_ed25519.pub                    # copy dòng này
```

Trên GitHub, đăng nhập tài khoản **OPS-project** → Settings → SSH and GPG keys → New SSH key → dán vào. Kiểm tra:

```bash
ssh -T git@github.com                        # phải ra "Hi OPS-project!"
```

Nếu mạng chặn cổng 22, thêm đoạn sau vào `~/.ssh/config` để đi qua cổng 443:

```
Host github.com
  HostName ssh.github.com
  Port 443
  User git
```

### 3.2. Lấy code

```bash
git lfs install
git clone git@github.com:OPS-project/anki_pipline.git "Anki Search"
```

Repo phải để **Private**: trong đó có câu và audio của HSKStory, và âm Hán Việt lấy từ dữ liệu Thiều Chửu (chỉ dùng cá nhân).

### 3.3. Những gì không có trên git

Khoảng 8 GB, bỏ qua bằng `.gitignore` vì nặng hoặc có bản quyền:

| Thư mục | Dung lượng | Cần khi nào |
|---|---|---|
| `chung/raw/` | 4,7 GB | Deck tải về (Love is Blind, 世界のニュース, TED-Ed, Friends, helq…). Cần nếu làm lô thử Nhật/Anh từ deck có sẵn |
| `research/downloads/` | 1,6 GB | Gói HSKStory gốc. Chỉ cần nếu build lại deck HSK |
| `chung/hanviet/01_sources/` | 1,8 GB | Từ điển nguồn Hán Việt. Chỉ cần nếu chạy lại pipeline Hán Việt |
| `research/inspection/`, `research/tools/` | | Dump deck và Whisper. Tải lại được |

Nếu làm hướng mới (video tự chọn) thì **không cần** mấy thư mục này. Cần thì chép bằng ổ cứng ngoài, giữ nguyên đường dẫn tương đối.

### 3.4. Python và thư viện

Script chạy bằng `python -I` (máy công ty dùng Python 3.14), nên cài thư viện vào `.work/` trong dự án:

```bash
pip install --target .work/pylib genanki==0.13.1        # build deck
pip install --target .work/pylib_anki anki==26.9.4      # test import trên collection tạm
```

- Các script trong `chung/build/zh/scripts/` tự tìm thư mục dự án theo vị trí file.
- Muốn đặt thư viện và file tạm chỗ khác thì đặt biến `ANKI_WORK`.
- `.work/` không đưa lên git.

### 3.5. Anki

- Anki desktop 26.9.x, add-on **AnkiConnect** (mã 2055492159). Cách A và việc tự chỉnh deck đều cần add-on này.
- Sync AnkiWeb trước khi dùng máy nhà, để deck HSK và preset tự về.
- Claude gọi AnkiConnect ở `http://localhost:8765` bằng Python `urllib`. Đừng dùng curl, vì curl làm hỏng tên deck có dấu.
- Trước khi xóa hay sửa hàng loạt, lưu danh sách ID ra file để phục hồi được.

## 4. Quy tắc an toàn

- Không ghi mật khẩu AnkiWeb vào file, script, log hay memory.
- File tải về coi là không tin cậy: mỗi gói một thư mục riêng, script để thư mục khác, chạy Python với `-I`.
- Dữ liệu Thiều Chửu chỉ dùng cá nhân, không phân phối lại. Deck đã gộp cũng vậy.
- Không chép thông tin tài khoản ngân hàng của người làm deck (trong mô tả deck Cún).
- Deck đang học: không ghi đè hay import khi chưa kiểm trên collection tạm (xem `test_update_v2.py`).
