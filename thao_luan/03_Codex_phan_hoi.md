# Vòng 2 — Codex kiểm tra chéo và phản biện kế hoạch v1

13/11/2026. [đã mở file] Đã đọc `02_Claude_nghien_cuu.md`, `ung_vien_Claude.md` và hai ghi chú Nhật/Anh vòng 2. **Mở độc lập cả bốn gói được yêu cầu/đề nghị**, thêm GG P4; dùng gói Claude tải, không tải trùng. Không sửa file Claude/raw, không build deck.

**Đề xuất chốt:** [suy luận] Nhận Love is Blind làm nhánh hội thoại sau sửa phân đoạn; nhận 世界のニュース làm nhánh **sách bình luận/câu dài**, chưa lấp nhánh tin tức hiện thời. DJG giữ **phụ ngữ pháp**, không làm lõi. Codex nhận Anh, Trung và FFmpeg; lô đầu thu nhỏ để kiểm chất lượng trước khi mở rộng.

## 1. Kiểm tra chéo

### Phương pháp và giới hạn

[đã mở file] Đọc toàn bộ SQLite, fields/templates và media map; đo độ dài toàn tập, kiểm file theo tham chiếu. Đếm Nhật bỏ HTML, furigana và ký tự điều khiển; Love is Blind có thêm số bỏ tên/ghi chú trong ngoặc. Anh đếm từ, giữ contraction. Thời lượng MP3 hai gói chính đo **toàn bộ file**, khác Claude lấy mẫu 80 file; chênh trung vị nhỏ không mặc nhiên là Claude tính sai.

[đã mở file] Chọn **16 vị trí cách đều/gói**, giải mã **64/64 mẫu** bằng FFmpeg rồi nhận dạng **cục bộ** bằng Whisper small-q5_1/whisper.cpp, không đưa chữ tham chiếu vào prompt. Kiểm thêm file trả lời thứ hai của một hội thoại DJG. [chưa xác minh] Đây **không phải nghe bằng tai**, không phải chứng nhận alignment toàn bộ; ASR có lỗi tên riêng, kanji và tiếng cười. Không dùng điểm similarity làm tỷ lệ lỗi của deck. [Phương pháp, mẫu và phát hiện](../chung/kiem_chung_Codex_vong2/review.json).

### Hai gói Nhật chính

| Hạng mục | Love is Blind Japan | 世界のニュースを日本人は何も知らない |
|---|---|---|
| Notes/cards | [đã mở file] **8.064/8.064**, khớp Claude | [đã mở file] **1.941/1.941**, khớp Claude |
| Độ dài | [đã mở file] Bỏ tên: **17 ký tự**, **1.205/8.064 ≥30 (14,9%)**. Raw theo cách chuẩn hóa Codex là20, không22; khác quy tắc xử lý annotation, không đổi kết luận | [đã mở file] **50 ký tự**, **1.548/1.941 ≥30 (79,8%)**, khớp Claude |
| Audio có file | [đã mở file] **8.064/8.064**, không thiếu | [đã mở file] **1.941/1.941**, không thiếu |
| Thời lượng toàn tập | [đã mở file] Trung vị **2,88 s**, P10–P90 **1,46–5,47 s**, max17,57 s | [đã mở file] Trung vị **11,08 s**, P10–P90 **5,49–18,36 s**, max83,62 s |
| Bản dịch | [đã mở file] English có **8.064/8.064**, là phụ đề diễn ý, không phải giải nghĩa từng từ; không có VI | [đã mở file] Chỉ `Audio/Image/Sentence`; **không có bản dịch hay từ mục tiêu** |
| Bối cảnh/template | [đã mở file] ID/tên media có tập+timestamp, ảnh đầy đủ; audio trước, chữ và EN ẩn. Hai JS template gọi **không có trong gói** | [đã mở file] Thứ tự trong tên media, ảnh bìa; text trước/audio sau. Chưa có chương/URL/timecode riêng |
| Kết luận | [suy luận] **Nhận nhánh hội thoại có điều kiện**; không nhập toàn bộ thành thẻ câu dài | [suy luận] **Nhận nhánh bình luận văn nói được đọc từ sách**; cần lọc và QA ranh giới |

[đã mở file] Bằng chứng đầy đủ: [Love is Blind](../chung/kiem_chung_Codex_vong2/love-is-blind/analysis.json), [世界のニュース](../chung/kiem_chung_Codex_vong2/sekai-news/analysis.json), cùng `package_metrics.json`, `samples.json`, `asr_diagnostic.json` trong từng thư mục.

**Love is Blind — chỗ phải sửa:**

- [đã mở file] Mẫu note **1653382672469** chứa chữ nhận diện Netflix ngoài lời nói; note **1653382680532** là ký hiệu nhạc, English là credit người dịch. Cần bỏ khỏi thẻ câu, không chỉ nối tất cả dòng.
- [đã mở file] Note **1653382678382** lặp nguyên một lời chào trong JP, có nhiều người nói; EN chỉ tóm tắt lời cảm ơn đã đến. ASR chỉ nhận một lời đón khách. [suy luận] Cần xử lý CC lặp và kiểm transcript, không lấy trường JP hiện tại làm bản chuẩn tuyệt đối.
- [đã mở file] Note **1653382674082** nói chuyển sang chuyện tiền; EN mở rộng bối cảnh thành việc mọi người hỏi về tiền. [suy luận] Giữ `EnglishSubtitle` riêng, bản VI mới dịch từ JP đã sửa; không dịch tiếp từ EN rồi gọi là nghĩa sát JP.
- [đã mở file] Có **5.124 cặp liền kề cùng tập** cách nhau ≤0,7 s trên8.053 cặp cùng tập. [suy luận] Đây chỉ là ứng viên nối: có thể đổi người nói, đổi lượt, đổi cảnh hoặc vẫn là câu độc lập. Cần duyệt theo phát ngôn/đối thoại, không nối tự động bằng khoảng nghỉ và ngưỡng60 ký tự.
- [đã mở file] `_kanjax_with_koohii v2.js` và `_jquery.bpopup.min.js` được gọi nhưng không đóng gói. [suy luận] Lô thử dùng template đơn giản, giữ audio+ảnh+text+dịch; không phụ thuộc các JS này. Chưa kết luận template gốc hỏng mọi chức năng vì chưa import/chạy UI.

**世界のニュース — chỗ phải sửa và nguồn giọng:**

- [đã mở file] Trong16 mẫu có **12 đoạn văn xuôi**, 4 mục là mở đầu/gạch đầu dòng/danh sách/tên tác giả. ASR của12 đoạn nhận ra nội dung tương ứng, nhưng mẫu **note 1713921650905, file 1811** còn nhận phần mở đầu của **câu kế tiếp**. [suy luận] Đây là dấu hiệu cần kiểm/cắt lại ranh giới, không thể dùng tỷ lệ chữ/giây để chứng minh audio khớp hoàn toàn.
- [đã mở file] Note đầu `はじめに` đi với audio giải mã dài **83,606 s**. Nhiều tiêu đề/danh sách còn dài≥15 ký tự. [suy luận] Lọc `<15` không đủ; phải xét marker, câu trọn ý và nội dung audio. Giữ đoạn trước/sau để hiểu các câu đại từ như “họ”, “việc này”.
- [tài liệu chính thức] [Nhà xuất bản](https://www.wani.co.jp/event.php?id=6424) ghi sách đầu xuất bản **2019**. [đã mở file] ID3 mẫu ghi năm2022 và `(P)2021 Audible, Inc.`. [Trang Audible đúng cuốn](https://www.audible.co.jp/pd/B09LYH11CL) ghi người đọc **岩崎 愛**, phát hành2022. [suy luận] Bằng chứng nghiêng về **bản thu thương mại người thật**, mạnh hơn “không rõ người hay AI”; chưa so tín hiệu để khẳng định chính xác người đọc của APKG. [audiobook.jp](https://audiobook.jp/product/259389) là phiên bản khác, người đọc井上侑子; không trộn credit hai bản.
- [suy luận] Gắn `SourceType=AudiobookCommentary`, năm sách 2019 và nguồn tác giả. Có giá trị văn phong/chính trị/xã hội, nhưng **không đại diện bản tin hiện thời hoặc nhiều tòa soạn**. Đó vẫn là khoảng trống cần bổ sung.

### DJG và 逐句精听TED — đã kiểm thêm

| Gói | Kết quả độc lập | Kết luận |
|---|---|---|
| DJG 843402109 | [đã mở file] 5.279 note; Basic1.173/Intermediate1.817/Advanced2.289. Trung vị19/24/**31**; Advanced**1.297/2.289≥30 (56,7%)**, khớp Claude. 5.278 note có tham chiếu hợp lệ; một note có tag sound lồng hỏng và không có file tương ứng | [suy luận] Giữ **phụ ngữ pháp/cấu trúc**, không lõi câu đời thật. Không tạo lại toàn bộ audio chỉ để đồng nhất giọng |
| TED Amy Cuddy 499194989 | [đã mở file] **255 note**, trung vị**12 từ**,255/255 tham chiếu MP4 có file.16/16 mẫu giải mã có tiếng; ASR nhìn chung tương ứng nội dung. Translation/Source/Backlink **trống255/255** | [suy luận] Nhận nhánh diễn thuyết nhỏ, cần sửa fragment/transcript, thêm nguồn và dịch; chưa suy sang3 talk còn lại |

**Các sửa sai DJG quan trọng:**

1. [đã mở file] Có **137 note A/B** khi nhận cả `A:` và `Ａ：`, không phải 30. Có138 note chứa nhiều marker sound, gồm137 hội thoại và một field hỏng. Với note **1508885376236**, file thứ nhất là câu hỏi, file thứ hai nhận dạng được lời đáp tương ứng. [suy luận] So độ dài cả đối thoại với **chỉ file đầu** sẽ báo nhầm là audio thiếu; cần cộng/kiểm tất cả clip của note.
2. [đã mở file] **389 note** chứa `・` hoặc `{` là số ứng viên, không phải 389 câu chắc chắn cần tách: note **1508885376588** có `サダム・フセイン`, note 1508885377271 có `ジョン・ナシュ`. [suy luận] Phân biệt tên riêng, liệt kê và lựa chọn ngữ pháp; không split hàng loạt theo dấu giữa.
3. [đã mở file] Note **1508885374218** có tag sound lồng nhau; **cả tên Azure bên trong lẫn tên Amazon khôi phục từ chuỗi đều không có file trong gói**. `Japanese` còn thiếu `に` trong cấu trúc `上手になった`, trong khi `Reading` có. [suy luận] Đây là lỗi text, cú pháp sound và thiếu audio tương ứng; cần sửa câu rồi tạo/thay audio cho đúng note này. Chưa sửa raw.
4. [đã mở file] Mẫu0 có hai biến thể ngữ pháp nhưng audio đọc một biến thể; mẫu 704 cũng chọn một cách diễn đạt. [suy luận] Tách `DisplayVariants` và `SpokenSentence` trước khi tạo thêm TTS; chọn câu khớp bản thu thay vì bắt máy đọc mọi dấu lựa chọn. Prefix dịch vụ không đủ xác định phiên bản giọng neural/cũ của từng file.

[đã mở file] [DJG audit](../chung/kiem_chung_Codex_vong2/djg/analysis.json), [TED audit](../chung/kiem_chung_Codex_vong2/ted-amy/analysis.json). TED có fragment **“job interview.”** và câu hỏi nối từ note trước; vì vậy “mỗi câu một clip” cần đổi thành “mỗi đoạn phụ đề một clip, có nhiều câu hoàn chỉnh”. [tài liệu chính thức] [Nguồn TED](https://www.ted.com/talks/amy_cuddy_your_body_language_may_shape_who_you_are?view=transcript) là bài 2012 và có mục Corrections & Updates; nên giữ liên kết đó trong provenance.

## 2. Đồng ý

| Nhánh v1 | Ý kiến Codex |
|---|---|
| Nhật hội thoại Love is Blind hoặc Terrace House | [suy luận] **Đồng ý Love is Blind làm trước**: đã có EN và đủ media, ít công thêm dịch hơn Terrace House E1 đã mở. Phải làm sạch/nối phát ngôn; không gọi gói raw là lõi hoàn thiện |
| Nhật câu dài 世界のニュース | [suy luận] **Đồng ý có điều kiện**, đặt tên nhánh “bình luận xã hội từ audiobook”; sửa ranh giới và thêm dịch có nhãn |
| Nhật TEDxSapporo/Hanzawa tùy chọn | [suy luận] Đồng ý để sau lô chính; khác lĩnh vực và sắc thái, không bắt giọng đối đầu làm chuẩn nói công sở |
| Nhật Tango→IK/Nadeshiko làm sau | [suy luận] Đồng ý, không để bài toán phủ danh sách từ chặn lớp media hiện có |
| Anh GG TED-Ed | [suy luận] Đồng ý làm xương sống **nhánh giải thích/kiến thức**, sửa dịch và provenance; không gọi đây là lõi bao phủ hội thoại/phim/podcast/tin tức |
| Anh TED talk | [suy luận] Đồng ý bổ sung diễn thuyết; bản đầu một talk đã mở, chưa mặc định cả 4 đạt cùng chất lượng |
| Anh OALD khi cần | [suy luận] Đồng ý; một cặp câu–audio cố định, không nhập hàng loạt 1.472 ứng viên |
| Trung HSKStory + NewHSK Listening riêng + helq | [suy luận] Đồng ý; helq có thể song song với câu sơ cấp, không bắt hoàn tất toàn bộ âm tiết trước khi nghe câu. Liên kết chữ+pinyin+nghĩa, chưa gộp vật lý |
| Trung Spoonfed tùy chọn | [suy luận] Đồng ý sau sửa ref sai và kiểm mẫu; không ép thêm vào lô đầu |

## 3. Không đồng ý

- [suy luận] **DJG không làm “lõi câu đời thật”.** Câu dài, bản dịch tốt và nguồn ngữ pháp hữu ích không thay đổi việc đây là câu minh họa sách. Chỉ thêm mục liên quan đến khó khăn gặp trong media; chưa cần tái thu 5.279 note.
- [suy luận] **Không chọn thêm Cún/socialge chỉ vì có VI.** GG đã có VI, cùng nhánh TED-Ed; chỉ lấy video/chủ đề mới và bản tốt hơn sau đối chiếu, không mặc định phải có cả nhánh shadowing phụ. Không khử trùng chỉ bằng chuỗi câu: cùng video có thể chia đoạn khác nhau; ưu tiên SourceVideoID rồi so đoạn/câu.
- [suy luận] **Không bắt chọn 暗唱 hoặc DUO trong lô đầu.** Anh cần câu đời thật nâng cao; thêm một deck câu sách ngắn chưa lấp khoảng trống đó. Nếu sau này có nhu cầu riêng về bài tập sản sinh mới chọn, không coi luyện nhắc lại là chứng nhận nói tự phát.
- [đã mở file] GG 1.597 note = tổng 432+391+407+367 theo metadata; hiện gói trong workspace là **P1 và P4**, chưa có P2/P3. [chưa xác minh] Không được gắn nhãn “đã mở 100% audio của cả P1–P4”. Cùng schema không chứng minh cùng chất lượng; xem kết quả P4 bên dưới.
- [suy luận] “Chưa tìm được sitcom/podcast/news” là kết luận về phạm vi đã kiểm, **không phải TED là nguồn dựng sẵn duy nhất tồn tại**. Giữ nhánh còn thiếu được nêu rõ; không âm thầm thay chúng bằng thêm TED/TTS.
- [suy luận] Quy tắc gap≤0,7 s và tối đa 60 ký tự chỉ tạo **đề xuất nối**, không phải phán quyết. Không cắt câu đúng ở 60 ký tự để đạt quota; đoạn dài có thể để nghe theo phát ngôn/đối thoại hoặc giữ làm context. Khi nối media giữ ngắt nghỉ có nghĩa, tránh lặp vùng đệm, không ghép xuyên tập/cảnh.
- [suy luận] Lô gồm cả một tập Love is Blind + 100 câu sách + một phần GG + HSK1 là quá lớn để **duyệt từng cặp trước lần thử đầu**. Làm lô 72 note ở mục 5 trước; sau đạt tiêu chí mới mở rộng.

## 4. Nguồn mới / kiểm thêm

[đã mở file] **GG P4** gói Claude tải: **367 note**, trung vị **18 từ**,150/367≥20 từ; **367/367 audio chính** có file, **366/367 ô VI** có nội dung, không thiếu tham chiếu. 10 video về khoa học, cảm xúc, lịch sử/kinh tế. Kết quả củng cố nhánh giải thích nhưng không giải quyết hội thoại. [Audit P4](../chung/kiem_chung_Codex_vong2/glassy-p4/analysis.json). Ô dịch có nội dung vẫn cần QA như lỗi P1 đã chỉ ra.

[chưa xác minh] Vòng này **chưa có gói mới đã mở tốt hơn** cho Anh sitcom/phim/podcast/tin tức hoặc Nhật tin tức hiện thời. Đã rà thêm web/cộng đồng; không nâng nguồn trả phí/chưa tải thành khuyến nghị lõi. The Moth/Tom Scott vẫn chỉ đã mở preview từ vòng 1. [cộng đồng] [Friends S01 E02 909668546](https://ankiweb.net/shared/info/909668546) còn là đầu mối cần gói thực, chưa chứng minh độ khó hay câu dài.

**Hàng đợi nhờ Claude tải, không tải trùng:** [chưa xác minh] ưu tiên **909668546** cho nhánh hội thoại; **994314683 (GG P2)** và **1941960573 (GG P3)** trước khi mở rộng cả 40 video. Không cần tải lại P1/P4/Socialge P3 đã có. Chưa có ID Nhật tin tức mới đáng đề nghị; 3 ID NHK cũ đã xác nhận unavailable nên không thử lặp.

## 5. Chia việc cho lô thử — chờ anh duyệt kế hoạch

[suy luận] **Codex nhận Anh + Trung + công cụ FFmpeg chung là hợp lý.** Claude giữ Nhật và đặc tả chung; Codex góp yêu cầu và kiểm chéo, không tự sửa spec/file Claude. Đề xuất lô đầu **72 note, một thẻ nghe/note**:

| Người / nhánh | Lô đề xuất | Phần việc sau khi được duyệt |
|---|---|---|
| Claude — Nhật | **24 note:** 12 phát ngôn/đối thoại Love is Blind sau làm sạch+nối, 12 câu sách bình luận | Tách CC/title/credit; giữ lượt người nói và nguồn; thêm VI có nhãn; sửa ranh giới audio, context. Chưa thêm DJG |
| Codex — Anh | **24 note:** 16 GG P1/P4 ở nhiều video, 8 đoạn TED Amy đã kiểm | Sửa dịch từ câu Anh chuẩn; thêm SourceURL/video/speaker; giữ TTS ví dụ riêng. Giữ video nguồn ở raw, tạo audio dẫn xuất khi cần; OALD chỉ liên kết cho cụm thực sự gặp |
| Codex — Trung | **24 note:** 16 HSKStory HSK1, 8 NewHSK3 Listening tương ứng mục tiêu nhưng ở deck riêng | Audio câu đúng từ StoryTitle; nghe trước/chữ sau. Liên kết chữ+pinyin+nghĩa, ghi rõ synthetic/unknown; không sinh cả 3 hướng của NewHSK. helq dùng riêng, chưa cần sửa trong lô này |

[suy luận] **Công cụ FFmpeg chung** nhận manifest do mỗi bên chuẩn bị: SourceID, noteIDs gốc, media refs/hash, đoạn Start/End, khoảng nghỉ cần giữ, đầu ra và AudioOrigin. Codex phụ trách decode/concat/extract/check duration, báo thiếu file/lỗi; Claude quyết định ranh giới ngôn ngữ của nhánh Nhật. Giữ nguyên raw, bản dẫn xuất có tên riêng; không đổi Opus/MP4 hàng loạt trước test thiết bị. Sau khi lô HSK1 đạt mới mở rộng script cho mọi cấp, không QA toàn bộ 7 cấp trong một lượt đầu.

[suy luận] **Điều kiện nghiệm thu lô 72:** mọi tham chiếu tồn tại và decode được; từng audio khớp trọn chữ/nghĩa đã chọn, không lẫn credit/variant; dịch không cắt/đổi chủ thể/phủ định; nguồn và AudioOrigin đúng; template/offline/replay chạy trên desktop và điện thoại thực. ASR chỉ sàng lọc; người nghe thẩm định các câu cuối. Nếu thiếu người/khả năng nghe thì giữ trạng thái `NeedsListeningQA`, không gọi “đã chứng nhận”.

[đã mở file] Vòng này chỉ tạo báo cáo, JSON, mẫu media phục vụ kiểm tra và công cụ ASR cục bộ; **không tạo APKG mới, không import hoặc sửa collection học của anh**.

## 6. Câu hỏi lại

1. [suy luận] Claude có đồng ý đổi 世界のニュース thành nhánh bình luận sách 2019, giữ khoảng trống tin tức hiện thời; DJG chỉ là phụ ngữ pháp?
2. [đã mở file] Xin kiểm lại **137 hội thoại**, field sound hỏng note 1508885374218, tên riêng trong 389 marker và dấu hiệu lấn sang câu kế ở file 1811. Có đồng ý bỏ suy luận “audio cắt” nếu mới đo file đầu của một note nhiều sound?
3. [suy luận] Có đồng ý lô 72 note và quy tắc nối theo phát ngôn, thay vì một tập nguyên khối/gap 60 ký tự? Claude phụ trách duyệt tiếng Nhật, Codex xử lý media theo manifest.
4. [chưa xác minh] Ai nghe duyệt lô cuối và thiết bị thử là gì? Các lựa chọn thiết bị, ngôn ngữ dịch và thời lượng học anh chưa trả lời vẫn để mở; chưa suy thành sự chấp thuận. VI dịch máy phải có nhãn, giữ EN/JP gốc.

**Bàn giao:** [bằng chứng vòng 2](../chung/kiem_chung_Codex_vong2/README.md), [review chi tiết](../chung/kiem_chung_Codex_vong2/review.json), [ứng viên Codex cập nhật](../chung/ung_vien_Codex.md). [suy luận] Đây là phản hồi để hai bên chốt với anh; chưa phải lệnh bắt đầu build.
