# Tiếng Nhật — kiểm tra bổ sung của Codex, vòng 1

Ngày kiểm tra: 2026-11-13. Phạm vi: deck/corpus dựng sẵn ngoài ImmersionKit, Nadeshiko, Aobana mà Claude đang phụ trách. Không xây, ghép hoặc sửa deck học thật. Trước tải đã kiểm tra `chung/raw/`; lúc kiểm tra chưa có `chung/ung_vien_Claude.md`. Không dùng thông tin đăng nhập; không gửi HTTP trực tiếp tới AnkiWeb.

## Kết luận để chốt vòng 1

[suy luận] Không nên lấy nhãn **Advanced**, số media hoặc thời lượng clip làm bằng chứng rằng một deck dạy **câu nói dài hoàn chỉnh**. Trong ba preview VideoAnki, bài giải thích thiên văn hợp mục tiêu nhất; vlog mahjong tuy ghi Advanced lại chủ yếu là mẩu phụ đề ngắn. Gói Terrace House thực tế mở được cũng chủ yếu là subtitle chunks. Chưa có ứng viên mới nào trong nhánh này được kiểm chứng đủ để làm CORE Nhật độc lập, đa lĩnh vực.

[suy luận] Phương án hợp lý là giữ nguồn phim/reality làm tầng hội thoại tự nhiên và bổ sung nguồn monologue/explainer/news cho cấu trúc dài; đánh giá tiếp kết quả coverage của Claude trước khi chọn CORE. Không thay kết luận này bằng danh sách Tango/Core vocabulary.

## 1. VideoAnki: ba preview công khai đã mở

[đã mở file] Mỗi nguồn đã lưu **8 card preview**, hai template hiển thị và 8 WebM công khai vào ba thư mục `chung/raw/codex-ja-videoanki-*`. Đây **không phải** toàn bộ APKG. Nút Download free hiện yêu cầu đăng ký tài khoản; không đăng ký, không dùng tài khoản AnkiWeb sang dịch vụ này. `public_preview.json`, `inspection.json`, `_meta.json` và video mẫu nằm trong từng thư mục.

| Nguồn dựng sẵn | Quy mô trang công bố | Mẫu mở thực tế | Median ký tự mẫu | Media có audio stream | Đánh giá câu |
|---|---:|---:|---:|---:|---|
| [Light-year / 宇宙ヤバイch](https://www.videoanki.app/decks/light-year-japanese-explainer/) | 146 card, 20 phút | 8 | 39; range 28–57 | 8/8 | 7 mẫu có kết thúc câu; 1 kết ở liên từ `が、` |
| [Karaage / コウケンテツ](https://www.videoanki.app/decks/karaage-japanese-cooking/) | 108 card, 16 phút | 8 | 28; range 15–43 | 8/8 | Có câu trọn ý, nhưng cũng có danh ngữ và mệnh đề chờ tiếp |
| [Mahjong / 西村歩乃果](https://www.videoanki.app/decks/mahjong-cousin-japanese-vlog/) | 313 card, 15 phút | 8 | 12; range 6–25 | 8/8 | Ít nhất 3/8 kết ở biểu thức tiếp nối; đa phần ngắn |

[đã mở file] Median tính sau bỏ HTML, giải mã entity và bỏ whitespace; số của bảng chỉ đúng với **8 mẫu được website chọn** mỗi nguồn. Ffmpeg nhận diện audio stream trong 24/24 WebM; điều này **không chứng minh** audio hoàn chỉnh theo ranh giới câu hoặc nghe rõ mọi tiếng. Chưa nghe đối chiếu thủ công toàn bộ media. Không suy rộng coverage 100% ra toàn deck.

[đã mở file] Card preview có bốn trường dữ liệu công khai: `video`, `target`, `native`, `translit`; có front/back template. Đây là schema của widget, **chưa xác minh schema Anki note thật**. Mẫu có video cảnh thật và bản dịch; Light-year/Karaage mẫu đang là tiếng Anh, mahjong mẫu trả bản dịch Hàn. Trang liệt kê thêm ngôn ngữ tải; chưa thấy tiếng Việt. Không thấy usage/nuance note có hệ thống, âm từ riêng, sentence source URL theo từng card hoặc cập nhật phiên bản đầy đủ. Có original video/channel ở trang deck.

[quảng cáo] Website nói clip và tiếng nói lấy từ video gốc, có người rà transcript/dịch từng câu, có cập nhật về sau. Chưa có bằng chứng độc lập về quy trình rà soát, nguồn giọng thiên văn có phải người thật hay TTS trong **video gốc**, hoặc ngày cập nhật gói. Vlog/cooking có người xuất hiện trong hình; không tự động suy ra mọi deck trong thư viện đều có human voice.

[suy luận] **Light-year: shortlist B**, hợp rèn trình bày/giải thích, đối chiếu và mệnh đề nhượng bộ, nhưng chỉ một chủ đề thiên văn. **Karaage: bổ sung B**, lời hướng dẫn và texture/cooking, chưa đủ khó/lĩnh vực để làm CORE. **Mahjong: loại khỏi CORE câu dài**, có thể dùng làm tầng casual conversation nếu thích nội dung. Không lấy chủ đề camera trong vlog làm nền IT.

Ba trích đoạn rất ngắn từ mỗi preview, nhằm nhận diện mẫu (không phải ba câu độc lập hoàn chỉnh): Light-year — “一光年”, “アポロ11号”, “しかし宇宙には”; Karaage — “できたー”, “皮なんですよね”, “最高ですね”; Mahjong — “あら見えた?”, “冷却用吸入口もある”, “後なんでねそれは”. Các ví dụ cuối của mahjong thể hiện chính vấn đề fragment.

## 2. Terrace House Tokyo 2020 Ep1 — đã mở gói thật

[đã mở file] Download công khai từ [Mediafire](https://www.mediafire.com/file/4tskz79aqv3tfe5/Terrace_House_Tokyo_2020_Ep1.apkg/file), được tìm qua [Japanese like a breeze: subs2srs decks](https://www.japanese-like-a-breeze.com/decks/). Gói nằm tại `chung/raw/codex-ja-terrace-house-tokyo-ep1/deck.apkg`, 56.70 MB, SHA256 `30ae20571b3c490a17a0d0ddfe6584cde1da60b7b72b682ad831a4b2efdb8bd3`. Mediafire ghi ngày tạo bản upload 2019-09-21; đây không phải bằng chứng deck còn được bảo trì.

| Hạng mục | Đo từ gói |
|---|---|
| Notes / cards / model | 791 / 791 / `MIA Japanese`, một template `Sentence` |
| Fields | Expression, Reading, Meaning, Focus, Snapshot, Audio, Audio on Front, Sequence Marker |
| Text / hình / audio | Expression, Snapshot, Audio, Sequence Marker đều 791/791 có dữ liệu |
| Đọc, dịch, nuance | Reading, Meaning, Focus đều **0/791** |
| File audio theo reference | 791/791 trỏ tới file tồn tại, không thiếu reference; 1.583 media tổng |
| Độ dài Expression | Median **18 ký tự** sau bỏ HTML/whitespace/ký tự điều khiển định dạng; min 2, max 37 |
| Nhạy với nhãn người nói | Bỏ nội dung ngoặc toàn chiều rộng: median **13**, max 36 |
| Câu dài theo số ký tự | Chỉ 13/791 ≥30 ký tự; 0/791 ≥40. Bỏ nhãn người nói còn 4/791 ≥30 |
| Thời lượng MP 3 thật | Median **2,184 giây**; range 0,816–6,624 |
| Front / back mặc định | Front hiển thị Expression; back phát Audio và hiện Snapshot. Audio on Front trống 791/791 |

[đã mở file] Lấy 20 chỉ số cách đều từ 0 tới 790 để đọc cùng note trước/sau: ít nhất 4 mẫu là phần tiếp nối/chưa trọn câu và 1 mẫu chỉ ghi tiếng cười. Đây là audit định tính, không phải ước lượng xác suất toàn gói. Ngay đầu chương trình, note thứ 2 mang phần giới thiệu kết ở chủ ngữ+số người và trợ từ `が`; note thứ 3 mới hoàn tất vị ngữ. Một số note còn trộn lời hai người. Vì vậy **791/791 có audio không đồng nghĩa 791 câu audio trọn vẹn**.

[đã mở file] Ba mẫu ngắn từ ba note khác nhau: “こんばんは”, “えっ？”, “全然分かんない”. Đó là lời thật trong thoại nhưng cho thấy độ ngắn, không phải N1 sentences. Đã lưu audit 20 mẫu, templates, notes và thống kê để kiểm tra lại; chưa ghép/cắt audio.

[suy luận] **Không chọn nguyên gói làm CORE câu dài**. Điểm mạnh: giọng hội thoại/reality, cảnh để nhớ ngữ cảnh, sequence marker giúp quay lại đoạn gốc. Nếu dùng, cần ghép subtitle thành lượt lời/câu hoàn chỉnh và kiểm audio sau ghép, bỏ tiếng cười, thêm dịch/nuance và đổi audio-front. Mức công sức sửa **vừa–cao**, không phải chỉnh CSS là xong. Không cần MIA add-on để chứng minh field audio/hình tồn tại; chưa kiểm khả năng chạy template JS cũ trên Anki hiện hành.

[cộng đồng] Người duy trì [mirror Jlab](https://www.japanese-like-a-breeze.com/decks/) cảnh báo kho lộn xộn, có gói thiếu hình hoặc sai audio. API public folder có 1.404 gói; thấy các bản Terrace House cả season từ 221 MB tới 3 GB. Không lấy con số archive làm bằng chứng chất lượng. Blogspot cũ `japanesedecks.blogspot.com` hiện trả 404 khi kiểm trực tiếp.

## 3. News NHK và shadowing: có lead, chưa xác minh package phù hợp

[cộng đồng] [FreeMdict, tác giả dax](https://forum.freemdict.com/t/topic/10915/1) tách hai bộ: **623 bài NHK** (2022-02-25) từ公众号初心日语联盟, Nhật/Trung đối chiếu; **7.613 ví dụ ngữ pháp** (2022-02-26), trộn Forvo với iFlytek TTS. Không được gọi bộ 7.613 là native newsaudio. Template news công khai dùng `Japanese`, `Chinese`, `Pronunciation` và đoạn `<p>`; [suy luận] có vẻ note nguyên bài, cần kiểm. Ba ID được post chung: `620593953`, `1192131968`, `1123167619`; **root đã kiểm public metadata và cả 3 unavailable**, chưa map được ID nào với nguồn nào. News bản mới chia sẻ qua Baidu, chưa tải/mở APKG; median, coverage, ngày bản tin, ranh giới audio và ba câu mẫu đều **[chưa xác minh]**. Đây là lead news đáng giữ, chưa đủ làm khuyến nghị đã kiểm.

[quảng cáo] [Seller Anki中文资源网](https://file.ankichinas.cn/card/62886333cebb67uH) bán `日语影子跟读（初中级）.apkg`,60 MB,￥28.99, cập nhật 2026-08-26. Trang có 411 card trong bảng nhưng mô tả ghi 1.208 câu; không xác minh số notes. Nói có bản 中上級, human voice, furigana có lỗi đa âm; tuy nhiên link 中上級 thực tế sang sản phẩm greenbook N1 khác. Không có preview tải công khai; không mua/nhắn seller. **[chưa xác minh] deck 中上級 cụ thể, median, full-sentence audio, dịch và schema**.

[tài liệu chính thức] [くろしお出版](https://www.9640.jp/shadowing/) xác nhận **sách** 新・シャドーイング日本語を話そう！中〜上級 có hội thoại phức tạp, phỏng vấn, business, thuyết trình; bản 2022 có cả ấn bản dịch Việt. Audio web dành cho người đã mua sách. Điều này xác minh nguồn sách/audio, **không xác minh deck Anki thương mại ở trên**; không tải audio theo điều kiện độc giả khi chưa có bằng chứng sở hữu sách.

## 4. Podcast / paid sentence banks: đã tìm, không đổi nhầm thành core

[cộng đồng] [Squintina JP101 Listening deck, 2025](https://community.wanikani.com/t/squintinas-listening-srs-for-japanese-pod-101/71327) chỉ chứa **link lesson**, cần JP101 subscription; có Advanced Audio Blog, Business nhưng không phải offline sentence-audio deck. Không chọn cho yêu cầu hiện tại.

[cộng đồng] [Teppei first 10 episodes](https://www.reddit.com/r/LearnJapanese/comments/i89p9i) là deck beginner và tác giả thừa nhận captions tự động có nhiều lỗi; không phù hợp N2→N1. [Jiten Mai podcast](https://jiten.moe/decks/media/141595/detail) xuất danh sách **từ vựng** theo media; chưa thấy sentence-audio export trong trang đã đọc. Không tính nó là corpus audio câu dựng sẵn.

[quảng cáo] [BritVSJapan Sentence Bank](https://www.britvsjapan.com/free-high-quality-japanese-anki-decks/) có phim/TV/YouTube đa dạng; mô tả phần lớn có original audio và ảnh, furigana tự động, dictionary nghĩa cần tự thêm. Terrace House Opening New Doors được ghi chỉ text hoặc một phần audio. Trang liệt kê tier $1/$5 nhưng danh sách mốc 2021; chưa kiểm giá/hoạt động subscription hiện tại hoặc tải gói. [Nukemarine Terrace House](https://www.patreon.com/LetsLearnJapanese/posts/currently-house-18790442) mô tả 2018 có sentence + vocab, audio từ subs2srs lẫn TTS cho vocab; chưa mở package. Hai nguồn chỉ là lead có sản phẩm, không được chấm coverage 100%.

## Công việc tiếp theo có giá trị

1. Đối chiếu kết quả nguồn Claude đang mở để xem có thực sự thiếu monologue/news dài; không tải lại archive vô chọn lọc.
2. Nếu cần thử VideoAnki, lấy đúng Light-year full APKG bằng tài khoản riêng được phép rồi audit ngẫu nhiên 30–50 note cả đầu/giữa/cuối: câu trọný, audio khớp, giọng người/TTS, dịch, provenance. Chưa hứa nó thay CORE.
3. Với NHK 623, mở đúng gói nếu có link public hoạt động; nếu note nguyên bài thì đây là tầng nghe bài, chưa phải tầng luyện câu. Không trộn với 7.613 grammar examples TTS.
4. Nếu thích shadowing sách, ưu tiên bản 中上級 đúng ấn bản 2022+; cần package/sample thật trước khi mua hoặc tự động chuyển đổi. Chưa có căn cứ nói “không tồn tại deck” và cũng chưa có căn cứ nói “đã tìm được deck 中上級 hoàn chỉnh”.
