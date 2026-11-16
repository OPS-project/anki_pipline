# Nghiên cứu deck Anki cho tiếng Trung, Nhật và Anh

**Ngày kiểm tra: 13/11/2026.** Dành cho người Việt làm kỹ sư DX/IT tại Nhật; Mandarin mới bắt đầu, Nhật N2→N1, Anh khoảng C1. Các kết luận dưới đây áp dụng cho đúng phiên bản được kiểm tra, không tự động áp dụng cho mọi bản sao cùng tên.

## I. Khuyến nghị điều hành

| Ngôn ngữ | Lựa chọn tôi khuyên bắt đầu | Vì sao | Giới hạn quan trọng |
|---|---|---|---|
| **Trung** | **HSKStory HSK1**, chuyển sang audio-first; dùng cùng hệ HSK2→6→7–9 khi tiến bộ | Đã kiểm tra cả bảy gói: 10.898 note đều có câu, Pinyin câu, dịch và tham chiếu đến audio câu nằm trong gói. Nhẹ, chia cấp, ví dụ sơ cấp nhìn chung phù hợp hơn với nhu cầu hiện tại của bạn | Gộp theo dạng chữ, không phải 11.000 mục/nghĩa riêng của đề cương. Chưa xác nhận rõ nguồn giọng của toàn bộ audio là người thu hay giọng tổng hợp; chưa thẩm định phát âm toàn bộ |
| **Nhật** | **Tango N1 trong Ankidrone Essentials V9** làm khung; thêm có chọn lọc **Japanese IT Vocabulary v5.2** cho công việc | Riêng N1 có 2.023/2.023 note với audio câu đóng gói; nguồn câu và bản thu của sách ASK. IT Vocabulary bổ sung tình huống họp, xác nhận, phản biện và công việc kỹ sư | Tango vẫn là giáo trình thi; IT dùng neural TTS và có lịch sử sửa lỗi cách đọc. Không bộ nào bao phủ đầy đủ hài hước, kể chuyện, thương lượng và diễn thuyết ngoài đời |
| **Anh** | **Close-up Word List C2 — bản mẫu 225 note đã kiểm tra** làm lô thử nghiệm; **OALD/eggrolls** làm kho bổ trợ có chọn lọc | Bản mẫu C2 có audio câu ở đủ 225 note. OALD có định nghĩa theo nghĩa, nhãn dùng từ và ví dụ Anh–Mỹ, giúp đào sâu các từ bạn đã biết | **Chưa tìm được một deck C1→C2 toàn diện, có sẵn, đã kiểm chứng và đủ sức làm chương trình nói nâng cao duy nhất.** Không học tuần tự toàn bộ OALD; không coi bản mẫu C2 là bộ đầy đủ |

Tải từ [HSKStory HSK1](https://hskstory.com/anki/hsk-1), [trang tác giả Ankidrone](https://tatsumoto-ren.github.io/blog/ankidrone-essentials.html), [IT Vocabulary v5.2](https://github.com/KakkoiDev/nihongo-it-anki/releases/tag/it-vocab/v5.2), [Close-up C2](https://ankiweb.net/shared/info/804826171) và [OALD bản 26.10.20](https://github.com/5mdld/anki-english-oald-decks/releases/tag/26.10.20).

**Nếu chỉ cài ba thứ trước:** HSKStory HSK1, subdeck Tango N1 và bản mẫu Close-up C2. Với tiếng Nhật và Anh, phần phát triển nói thực sự nên đến từ việc đem cụm đã học vào câu chuyện, cuộc họp và đối thoại mới. Anki giữ lại những gì bạn cần dùng; nó không tự cung cấp phản hồi về dụng học, cách lập luận hay ứng đáp.

### Mức độ kiểm chứng

Tôi tìm bằng tiếng Anh, Nhật và Trung trên AnkiWeb, GitHub, Anki Forums, Reddit, trang chuyên môn, trang nhà xuất bản và nhà cung cấp thương mại. Ví dụ truy vấn: `HSK 3.0 2026 sentence audio`, `中国語 Anki 例文 音声`, `日语 N1 牌组 例句 音频`, `English C1 C2 collocations Anki`. Tìm kiếm cộng đồng Hoa ngữ không đưa ra được bằng chứng mạnh hơn các gói và kho mã được kiểm tra dưới đây; tôi không diễn giải kết quả tìm kiếm thành việc đã đọc được mọi diễn đàn.

Đã tải và mở **16 gói `.apkg` hoàn chỉnh**: bảy gói HSKStory, hai Ultimate HSK, Kaishi, Ankidrone V9, IT Vocabulary, N1 Grammar, Close-up C2, OALD và mẫu LexiDeck. Kiểm tra SQLite, note type, trường, template, bản đồ media và file mà các trường audio tham chiếu. **120 tệp âm thanh mẫu giải mã thành công bằng FFmpeg**, bao gồm mẫu từ các deck dẫn đầu. Đã đọc và kiểm tra trực quan bìa cùng trang từ vựng của đề cương HSK gốc, rồi trích đủ 11.000 dòng từ vựng.

**Điều chưa làm:** chưa nghe thẩm định toàn bộ audio, chưa kiểm thử trực tiếp trong AnkiDroid/AnkiMobile, chưa mua các gói trả phí, chưa kiểm tra bằng người bản ngữ mọi câu. Giải mã được file không chứng minh rằng từng thanh điệu, cách đọc hay sắc thái đều đúng. Các đánh giá độ tự nhiên bên dưới dựa trên mẫu văn bản đã xem và nguồn âm thanh được công bố, không phải một cuộc kiểm định ngữ âm toàn diện.

Ký hiệu sử dụng:

- **A — kiểm tra trong gói:** có câu và audio câu tương ứng được đóng gói; các file mẫu giải mã được. Không có nghĩa đã nghe hết.
- **B — mẫu công khai/tài liệu:** có bằng chứng về tính năng hoặc thẻ mẫu; chưa kiểm chứng toàn bộ gói.
- **U — chưa xác minh:** chỉ có lời tác giả, liên kết không truy cập được hoặc chưa đủ dữ liệu.
- **P — một phần:** có audio ví dụ nhưng không đủ mọi note, hoặc ví dụ có thể chỉ là cụm từ.

Deck chỉ có audio từ, hoặc audio câu ở mức U, **không được chọn làm deck chính**. Với mức P, chỉ những mục được chọn và xác nhận riêng mới đáp ứng yêu cầu.

## II. So sánh và đánh giá

### 1. Tiếng Trung: chuẩn HSK nào đang đúng?

Phải tách ba lớp tài liệu:

| Cấp | HSK 2.0 cũ: từ cộng dồn | Chuẩn giáo dục GF0025-2021: từ cộng dồn | Đề cương thi 11/2025: mục mới tại cấp | Đề cương thi 11/2025: mục cộng dồn |
|---|---:|---:|---:|---:|
| 1 | 150 | 500 | 300 | 300 |
| 2 | 300 | 1.272 | 200 | 500 |
| 3 | 600 | 2.245 | 500 | 1.000 |
| 4 | 1.200 | 3.245 | 1.000 | 2.000 |
| 5 | 2.500 | 4.316 | 1.600 | 3.600 |
| 6 | 5.000 | 5.456 | 1.800 | 5.400 |
| 7–9 | — | 11.092 | 5.600 | 11.000 |

Chuẩn năm 2021 xác lập **ba bậc, chín cấp**, có hiệu lực 1/7/2021; đó không phải bằng chứng rằng mọi kỳ thi cấp 1–6 đã đổi ngay năm ấy. Đề cương thi mới có bìa ghi **ban hành 11/2025, thực hiện 7/2026**. Danh sách thi mới khác danh sách 2021. [Bộ Giáo dục Trung Quốc](https://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202103/t20210329_523304.html), [cổng đề cương CTI](https://www.chinesetest.cn/syllabus), [PDF đề cương chính thức](https://hsk.cn-bj.ufileos.com/3.0/新版HSK考试大纲1219.pdf).

**Lịch thi cần chú ý tại Nhật:** CTI thông báo kỳ thi HSK3.0 chính thức toàn cầu ngày 13/12/2026. Tuy nhiên, thông báo **10/11/2026 của HSK日本実施委員会** ghi rõ Nhật chuyển từ **tháng 1/2027**, còn các kỳ trong năm 2026 dùng HSK2.0. Nhật cũng thông báo vẫn cho đăng ký thi viết và nói riêng. Vì vậy không áp quy định đăng ký nói của các kỳ thử nghiệm quốc tế lên lịch thi Nhật. [Thông báo CTI trên trang chính thức](https://www.chinesetest.cn/Development?lang=cn), [thông báo tại Nhật](https://www.hskj.jp/hsk3_info02/).

**Cách nhận ra deck sai phiên bản:** HSK1 có 150 từ thường là bộ cũ; 500 từ thường thuộc chuẩn 2021; 300 mục là dấu hiệu phù hợp đề cương thi mới, nhưng vẫn cần đối chiếu nội dung. Nhãn “HSK 3.0” tự nó không đủ.

#### Các lựa chọn cạnh tranh

| Deck / tác giả, phiên bản | Cấp và quy mô | Audio câu | Ví dụ, ngữ cảnh, hình ảnh | Giá và bảo trì | Đánh giá, nền tảng và nguồn |
|---|---|---|---|---|---|
| **HSKStory HSK1–9** / nhóm HSKStory; các gói hiện tại v8–v11 | Theo danh sách thi mới, nhưng gộp dạng chữ. 10.898 note/thẻ trong bảy gói | **A:** đủ 10.898 note có audio từ và câu; offline. Loại giọng toàn bộ **chưa xác minh rõ** | Một câu/note, Pinyin màu thanh, dịch Anh. Không có bộ ảnh minh họa từ vựng. Mẫu sơ cấp rõ và gọn; câu nâng cao thường vẫn ngắn | Miễn phí deck, không cần thuê bao đọc truyện. Có changelog và sửa ví dụ/audio trong 2026 | **Ưu tiên số 1 cho bạn.** Template mặc định nhận diện chữ; cần đổi hướng ôn nghe. Tác giả công bố hỗ trợ Desktop, AnkiDroid, AnkiMobile; phần audio câu dùng HTML/JS, chưa thử trên điện thoại. [HSK1 và các cấp liên kết](https://hskstory.com/anki/hsk-1) |
| **Ultimate Mandarin Chinese Vocabulary — New HSK3.0** / **fa9r**; HSK1 cập nhật 11/10/2026 giờ Nhật | Tác giả công bố đủ 11.000 mục, chia 1–6 và ba phần 7–9. Đã mở HSK1 **300**, HSK2 **200** note/thẻ | **A cho 500 note đã mở:** đều có `AudioSentence`. Các cấp sau chưa mở. Nguồn âm thanh được ghép từ nhiều deck; không chứng nhận tất cả là người thu | Từ, Pinyin, từ loại, câu, Pinyin câu, dịch, ảnh. Có nội dung HSK-JK được tái dùng; chất lượng ví dụ không đều theo nghĩa | Miễn phí; sửa dữ liệu trong 10/2026; có GitHub nhận lỗi | **Số 2**, hợp làm khung đối chiếu mục/nghĩa và lựa chọn thay thế. Dễ chuyển audio-first hơn HSKStory vì có trường audio câu riêng. Chưa thử mobile. [HSK1](https://ankiweb.net/shared/info/1736976202), [HSK2/trang liên kết mọi cấp](https://ankiweb.net/shared/info/801432412), [GitHub tác giả](https://github.com/fa9r/anki-chinese-new-hsk-3.0-ultimate) |
| **Spoonfed Chinese** / **promagma** | Tác giả công bố hơn 8.000 câu, tăng dần độ khó; **không phải lộ trình HSK mới** | **B/U cho gói bán hiện tại:** tác giả ghi audio người bản ngữ cho câu; chưa mua/mở gói | Câu Hanzi–Pinyin–Anh; thiên về tiếp xúc và bắt chước câu. Không phải hệ thống tách từ mới theo cấp HSK | **US$3+** tại trang bán lúc kiểm tra. Không xác nhận được lịch cập nhật gần nhất | **Bổ trợ có điều kiện**, không chọn làm deck chính đã kiểm chứng. Có phản ánh độc lập về vài file audio thiếu ở một bản người dùng. [Trang bán của tác giả](https://promagma.gumroad.com/l/IEmpwF) |
| **New HSK3.0 Mandarin Chinese Sentence Deck** / credit **tompat**, gói bổ sung do **NewHSK3** đăng | Công bố khoảng 33.000 câu/99.000 thẻ cho 11.000 mục. AnkiWeb hiện báo **18.000 note**, chỉ phần 1–4; phần 5, 6, 7–9 tải riêng | **B/U:** tài liệu nói có audio mọi câu; chưa mở được gói trong đợt kiểm tra | Ba câu/mục, Listening/Reading/Writing, giản/phồn, Pinyin, dịch; không ảnh. Có vẻ giàu ngữ cảnh hơn nhưng khối lượng rất lớn | Miễn phí; gói GitHub v1.0 ngày 31/7/2026 | **Đáng theo dõi, chưa làm core.** Không nên kích hoạt mọi hướng thẻ. AnkiWeb giới hạn tải trong phiên kiểm tra bằng HTTP429; không suy diễn là deck hỏng. [Trang deck](https://ankiweb.net/shared/info/258311532), [các gói cấp cao](https://github.com/NewHSK3/new-hsk-3-anki-deck/releases/tag/v1.0) |

Nguồn mô tả và quá trình bảo trì: [HSKStory HSK1](https://hskstory.com/anki/hsk-1), [HSKStory cập nhật](https://hskstory.com/whats-new), [Ultimate HSK2](https://ankiweb.net/shared/info/801432412), [Spoonfed](https://promagma.gumroad.com/l/IEmpwF), [Sentence Deck](https://ankiweb.net/shared/info/258311532). Các số liệu A trong bảng là kết quả mở gói, không phải suy từ số file âm thanh trên trang web.

#### Vì sao HSKStory đứng trước Ultimate cho trường hợp của bạn?

Lợi thế nhận mặt chữ của bạn làm giảm giá trị của ảnh, viết nét và thẻ Hanzi→nghĩa. Giá trị cần mua bằng thời gian ôn là **nghe ra âm tiết, thanh và cụm trong câu**. HSKStory nhỏ gọn, đủ audio câu, và ở mẫu kiểm tra diễn đạt các hư từ/từ loại khá rõ.

Một lỗi cụ thể ở **Ultimate HSK2**: mục `名` cho câu chứa `名字`; câu đó không minh họa rõ cách dùng lượng từ `名` theo đề cương. HSKStory dùng câu có cấu trúc “mười + 名 + học sinh”, đúng công dụng lượng từ. Mục `地` của Ultimate có câu mô tả cuốn sách “nằm yên lặng” trên bàn; đúng hình thức đánh dấu trạng ngữ nhưng kém điển hình về ngữ dụng. Đây là các lý do hạ điểm biên tập, không phải kết luận rằng mọi thẻ Ultimate đều sai.

**Số note HSKStory khác số mục thi:** đối chiếu 11.000 dòng của PDF, bỏ chỉ số phân biệt mục đồng hình, còn **10.896 dạng chữ**. Bảy gói HSKStory chứa **10.898 dạng chữ khác nhau**, không trùng giữa cấp. So sánh tập chữ cho thấy hai dạng trong đề cương `差点儿`, `要不` được thay bằng dạng dài hơn `差一点儿`, `要不然`; ngoài ra có thêm `有一点儿`, `有时候`. Khớp gần như toàn bộ dạng chữ **không bảo đảm** đã dạy riêng mọi nghĩa/cách đọc mà danh sách chính thức tách ra.

| Cấp | Mục mới theo đề cương thi | Note HSKStory thực tế | Ý nghĩa |
|---|---:|---:|---|
| 1 | 300 | 300 | Khởi đầu phù hợp |
| 2 | 200 | 197 | Có gộp dạng chữ |
| 3 | 500 | 493 | Có gộp/biến thể |
| 4 | 1.000 | 990 | Có gộp dạng chữ |
| 5 | 1.600 | 1.579 | Có gộp dạng chữ |
| 6 | 1.800 | 1.777 | Có gộp dạng chữ |
| 7–9 | 5.600 | 5.562 | Một nhóm cấp cao, không phải ba chương trình từ vựng độc lập |

**Phản hồi cộng đồng:** các bài cập nhật HSKStory chủ yếu do bên làm sản phẩm đăng, nên không được tính là đánh giá độc lập. Người đọc có đặt câu hỏi về AI và một giọng đọc; những thắc mắc đó chưa chứng minh chất lượng kém, nhưng ngăn tôi gắn nhãn “đã được chuyên gia bản ngữ kiểm duyệt toàn bộ”. Với Spoonfed, lời khen sử dụng lâu năm là tín hiệu hữu ích, song không thay thế kiểm tra media của phiên bản hiện tại. [Thảo luận HSKStory](https://www.reddit.com/r/ChineseLanguage/comments/1x93dpa/updated_hsk_30_anki_decks_hsk_19_with_word_and/), [Anki Forums về Spoonfed](https://forums.ankiweb.net/t/shared-deck-advanced-chinese-vocab-grammar-deck/11983), [người dùng mô tả sửa file audio thiếu](https://blog.samgould.net/post/anki-scripting).

**Nguồn dành cho người biết Nhật:** có deck Nhật→Trung luyện âm→nghĩa Nhật, nhưng mẫu tìm được vẫn ghi HSK1 150 từ và chưa có bằng chứng đủ câu kèm audio. Không chọn chỉ vì dùng tiếng Nhật làm ngôn ngữ trung gian. Dùng nghĩa Việt/Anh ở mặt sau thuận tiện hơn việc tạo thêm vòng dịch Nhật. [Ví dụ deck Nhật→Trung](https://note.com/super_knot582/n/n08a95753ee75).

Các lựa chọn khác đã sàng lọc: **HSK Illustrated** có audio câu neural TTS và cloze, nhưng chính FAQ ghi **HSK2.0**, 2.501 từ cấp 1–5; không dùng để khẳng định bám đề cương thi mới. Các deck xiehanzi tập viết không giải quyết nút thắt nghe của bạn. Deck AnthonyBogetti có mô tả khá hợp yêu cầu nhưng link AnkiWeb trong README trả về trạng thái thiếu ở thời điểm kiểm tra, nên không đưa vào danh sách cài đầu tiên. [HSK Illustrated](https://anki.si5.pl/), [AnthonyBogetti](https://github.com/AnthonyBogetti/HSK-3.0-Vocabulary-Anki-Deck).

### 2. Tiếng Nhật: N1 và tiếng Nhật nói vượt N1

**JLPT không kiểm tra trực tiếp nói, viết hay tương tác.** Việc chỉ số CEFR xuất hiện trên phiếu điểm không làm thay đổi giới hạn ấy. Không nên diễn giải “deck N1” thành “deck đào tạo người nói thành thạo”. [JLPT chính thức về CEFR](https://www.jlpt.jp/e/about/cefr_reference.html).

| Deck / tác giả, phiên bản | Trình độ và quy mô đã kiểm tra | Audio câu | Nội dung, hình ảnh, register | Giá và bảo trì | Đánh giá, tương thích và tải |
|---|---|---|---|---|---|
| **JLPT Tango N1 — Ankidrone Essentials V9** / Tatsumoto Ren và cộng tác viên; câu/audio từ sách ASK | **N1: 2.023 note/thẻ**, nằm trong gói 7.724 note gồm 6 thẻ giới thiệu | **A: 2.023/2.023** có `SentAudio`, media đi kèm; các mẫu được chọn giải mã được. Bản thu câu của sách | Từ/cụm nổi bật trong câu, furigana, dịch Anh, định nghĩa, trường pitch accent. Không phải deck ảnh hay hội thoại dài nhiều lượt | Miễn phí tải; trang hướng dẫn cập nhật 26/10/2026. Sách nguồn mua riêng nếu học kèm; đây là bản chuyển đổi cộng đồng, không phải sản phẩm Anki chính thức của ASK | **Core N1 số 1.** Dùng lọc từ chưa biết, không học lại N5. Gói V9 dùng `.webm` cho nhiều audio; không áp lỗi của V8 lên V9 nhưng phải thử thiết bị. [Trang tải tác giả](https://tatsumoto-ren.github.io/blog/ankidrone-essentials.html), [giải thích riêng N1](https://tatsumoto-ren.github.io/blog/jlpt-tango-n1-anki-deck.html) |
| **Japanese IT Vocabulary v5.2** / KakkoiDev | **1.516 note, 4.548 thẻ**, 15 nhóm. Không phải danh sách JLPT/CEFR chính thức | **A: 1.516/1.516**, MP3 trong gói; **Microsoft Edge ja-JP-KeitaNeural**, không phải người thu | Listening, Reading, Vocabulary cloze; câu họp, agile, kiến trúc, AI, thuyết trình, casual chat, email. Có register và pitch tự động; không ảnh | Miễn phí, MIT; phát hành 2/9/2026 giờ Nhật; có tài liệu sửa lỗi TTS | **Bổ trợ công việc số 1**, rất hợp kỹ sư DX. Không bật cùng lúc cả ba hướng cho mọi note. Hầu hết câu ngắn; không thay chương trình kể chuyện/tranh luận. Chưa thử mobile trực tiếp. [Bản v5.2](https://github.com/KakkoiDev/nihongo-it-anki/releases/tag/it-vocab/v5.2) |
| **Shin Kanzen Master N1 Grammar Example Sentences v2.0.0** / mxggle | **343 note/thẻ**, 20 bài; đây là deck ngữ pháp, không phải bộ từ N1 | **A: 343/343** MP3 câu. Changelog xác nhận **VOICEVOX WhiteCUL, speaker23**, đã tái tạo toàn bộ | Câu, cloze mẫu ngữ pháp, furigana, giải thích Nhật/Trung, ghi chú phong cách. Không ảnh; có câu dài, nhiều cấu trúc văn viết | Miễn phí; bản 13/8/2026; changelog nêu còn một ví dụ nguồn thiếu, không tự bịa thêm | **Bổ trợ ngữ pháp**, không làm mẫu giọng hội thoại chính. Dùng file GitHub: liên kết AnkiWeb 1584745637 trong README hiện mở ra **deck N2**. [Tải N1 v2.0.0 đúng](https://github.com/mxggle/anki-jlpt-n1-grammar-example-sentences/releases/tag/v2.0.0) |

Nguồn: [Ankidrone](https://tatsumoto-ren.github.io/blog/ankidrone-essentials.html), [IT Vocabulary](https://github.com/KakkoiDev/nihongo-it-anki), [N1 Grammar và changelog](https://github.com/mxggle/anki-jlpt-n1-grammar-example-sentences). Con số và độ phủ A được kiểm tra trong từng gói nêu trên.

#### Phân theo trình độ để tránh cài thừa

| Giai đoạn | Nguồn tham khảo tốt | Điều cần biết |
|---|---|---|
| N5–N4 | **Kaishi 1.5k v2.4.3**, hoặc phần Tango phù hợp | Kaishi có 1.500 mục học + 1 note giới thiệu, đủ audio câu cho 1.500 mục; ảnh Irasutoya, pitch tùy bật. Đây là tham khảo nền tảng, **không nên học tuần tự ở N2/N1** |
| N3–N2 | Tango N3/N2; Core2k/6k nếu cần dò lỗ hổng | Trong đúng Ankidrone V9 đã mở: N2 **1.659/1.659** note có audio câu, N3 chỉ **1.444/2.045**. Không suy rộng đặc tính N1 sang N3 |
| N1 | Tango N1; N1 Grammar cho điểm yếu ngữ pháp | Câu có nguồn và audio giúp học cách dùng, nhưng còn nhiều từ bạn đã biết hoặc ít dùng khi nói |
| Sau N1 | IT Vocabulary chọn tình huống + một nhóm nhỏ câu nguyên bản từ media/lĩnh vực của bạn | Chưa tìm thấy bộ sẵn có đã kiểm chứng bao trùm hài hước, kể chuyện, xã giao, tranh luận và diễn thuyết với đầy đủ chú giải register |

[Kaishi chính thức](https://github.com/donkuri/kaishi), [bản v2.4.3](https://github.com/donkuri/kaishi/releases/tag/v2.4.3), [bản Core2k/6k của Jouzu Juls và lời lưu ý lỗi kế thừa](https://www.jouzujuls.com/anki-decks).

**Các vấn đề chất lượng đáng kể:**

- Trong Ankidrone V9, N5 chỉ **931/1.077** note có audio câu; 146 mục còn lại không qua tiêu chí sentence audio. N4 đạt 914/914. Không giới thiệu cả gói là “mọi thẻ đều có audio câu”.
- Một số câu N1 dùng lối ghi nhiều Kanji ít thường gặp hơn văn bản hiện đại thông dụng. Hãy chọn cách viết bạn gặp trong công việc; không biến mọi cách viết trong deck thành chuẩn diễn đạt nên bắt chước.
- Trường `MakeProductionCard` của Tango hướng tới nhớ cách viết Kanji từ cách đọc. Nó **không tương đương** luyện tự nói một ý bằng tiếng Nhật.
- IT Vocabulary có tài liệu mô tả lỗi đọc Kanji, rơi âm tiết và chữ viết tắt của Edge TTS; v5.2 sửa cách đọc `力技` và `ググって`. Tính minh bạch này có ích, nhưng đối chiếu ASR tự động không thay được kiểm duyệt ngữ âm của người bản ngữ. Pitch từ UniDic là thông tin hỗ trợ, không phải chứng nhận cao độ của cả câu. [Tài liệu lỗi TTS của tác giả](https://github.com/KakkoiDev/nihongo-it-anki/blob/master/docs/tts-audio-debugging.md).
- VOICEVOX của N1 Grammar phù hợp hỗ trợ đọc/nghe cấu trúc; không ưu tiên nó để bắt chước cách thuyết trình hay hội thoại người lớn tự nhiên.

Phản hồi về Tango N1 có cả người dùng hữu ích lâu dài lẫn người thấy ít giá trị ở trình độ cao. Vì vậy tôi chọn nó làm **khung lọc N1**, không yêu cầu hoàn thành 100%. [Một hành trình dùng Tango N1](https://www.reddit.com/r/LearnJapanese/comments/1wlv597/zero_to_n1_in_5_years_literally_everything_i_did/), [ý kiến không hài lòng](https://www.reddit.com/r/LearnJapanese/comments/12fhi6w/can_anyone_suggest_an_n1_vocab_anki_deck/).

**Deck anime/drama có sẵn:** Jo Mako nói rõ chỉ *một số* game deck có sound, còn manga deck là chữ/ảnh. Không thể coi cả thư viện là đạt yêu cầu audio câu. Các bộ subs2srs toàn phim có thể hữu ích, nhưng câu bị cắt theo subtitle, lời nhân vật, tiếng nền, bản quyền và bản dịch không khớp cần kiểm tra theo từng gói. Không có một gói cụ thể đủ bằng chứng để tôi đặt lên trước Tango N1 trong báo cáo này. [Mô tả của Jo Mako](https://www.patreon.com/JoMako/about).

### 3. Tiếng Anh: ưu tiên dùng được, không sưu tầm từ hiếm

| Deck / tác giả, phiên bản | Cấp và số note/thẻ | Audio câu | Ví dụ, cụm từ, ảnh | Giá và bảo trì | Kết luận, thiết bị và nguồn |
|---|---|---|---|---|---|
| **Close-up Word List C2** / **kelciour**; cập nhật 14/10/2026 | **225 note/thẻ trong gói miễn phí đã mở**. Tác giả ghi bộ đầy đủ 1.611 note; không đánh đồng hai số | **A: 225/225** có `Example Audio`, offline; câu đọc bằng **Microsoft Azure TTS**, không phải mặc định audio bản ngữ thu | Từ/cụm, IPA, định nghĩa Anh, câu, chủ đề, trang nguồn; 65 ảnh theo metadata AnkiWeb. Có nội dung C2 nhưng xen từ chuyên biệt ít giá trị nói | Bản mẫu miễn phí; bộ đầy đủ được dẫn tới bộ sưu tập/qua email, chưa xác nhận giá hiện tại hay mở gói đầy đủ | **Lô khởi động đã kiểm chứng tốt nhất ở C2**, chọn lọc. Chưa thử mobile; template có media thông thường. [Bản mẫu](https://ankiweb.net/shared/info/804826171), [trang bộ sưu tập tác giả dẫn tới](https://hipolink.net/kelciour/products/my-english-anki-decks-collection-v2) |
| **eggrolls OALD — Oxford5k + COCA20k** / **5mdld**, bản **26.10.20** | **42.268 note/thẻ**, mỗi note một nghĩa. Subdeck C1 có **2.295 note**; không phải 42.268 từ khác nhau | **P:** 22.153/42.268 note có ít nhất một audio ví dụ. Riêng subdeck C1: **1.535/2.295**. Một số ví dụ có audio là cụm từ, không phải câu hoàn chỉnh | Định nghĩa, tối đa ba ví dụ, IPA/audio Anh–Mỹ, grammar/usage/collocation, bản dịch Nhật/Trung tùy bật. Không phải deck ảnh hay khóa hội thoại | Miễn phí; gói có audio ví dụ khoảng **1,04GB**. Bản nhỏ hơn và bản AnkiWeb thiếu audio ví dụ. Chưa có cơ sở đánh giá bảo trì dài hạn | **Kho bổ trợ mạnh nhất**, gói gốc **không đủ tiêu chuẩn core**. Chỉ chọn nghĩa có câu hoàn chỉnh + audio tương ứng. Template nhiều JS, online TTS tùy bật không đồng nghĩa offline audio. [GitHub](https://github.com/5mdld/anki-english-oald-decks/), [đúng bản có audio](https://github.com/5mdld/anki-english-oald-decks/releases/tag/26.10.20) |
| **English Phrasal Verbs** / **Refold**, giọng Ben | Trang sản phẩm ghi **150 priming**, khoảng **330 nghĩa**; danh mục hiện hiển thị 857 cards. Chưa mở gói để giải quyết chênh lệch số đếm | **B/U:** trang bán cam kết audio cho từ và câu, người bản ngữ Mỹ thu; blog xác nhận câu thực hành có giọng Ben. Chưa kiểm tra gói | Câu do giáo viên viết, ảnh, chọn nghĩa từ nghiên cứu tần suất PHaVE. Thiên về trung cấp, không tự gắn nhãn C2 | **US$24,99 mua một lần** để tải Anki. Thuê bao US$9/tháng học trên Refold **không bao gồm tải Anki** | **Bổ sung trả phí có điều kiện**, không là core đã kiểm chứng. Bạn có thể đã biết phần lớn nghĩa. [Trang mua hiện tại](https://refold.la/decks/buy/english-phrasal-verbs-deck), [cách dùng/mẫu thật](https://refold.la/blog/phrasal-verbs-deck) |
| **English. C1 Words, Idioms, Phrasal Verbs. American Accent.** / **Adam, liên hệ zyskow.ad**; cập nhật 9/12/2025 | Metadata trực tiếp hiện có **1.731 note**, không phải 2.091 của một trang tổng hợp cũ | **B/U:** mẫu AnkiWeb có trường audio từ và `Example Audio`; chưa tải được gói do HTTP429, chưa biết độ phủ cả bộ/nguồn giọng | Câu, nghĩa, idiom/phrasal verb; bản chỉnh từ Close-up C1 thêm nội dung cá nhân. Metadata hiện ghi 0 ảnh | Miễn phí; chưa xác nhận bảo trì sau 12/2025 | **Ứng viên thử sau**, không xếp làm core. Chữ “American Accent” chưa chứng minh là người thu hay audio câu đầy đủ. [Trang đúng](https://ankiweb.net/shared/info/524918335) |

Nguồn chính: [Close-up C2](https://ankiweb.net/shared/info/804826171), [OALD README](https://github.com/5mdld/anki-english-oald-decks/), [Refold sản phẩm](https://refold.la/decks/buy/english-phrasal-verbs-deck), [C1 American](https://ankiweb.net/shared/info/524918335). Số liệu A/P là từ gói đã mở; số 1.731 là metadata trực tiếp của AnkiWeb. Các số từ trang tổng hợp không được ưu tiên hơn gói hiện tại.

#### Dùng OALD đúng với trình độ C1 của bạn

Chọn bản **`eggrolls-oald-20k.apkg`**, không chọn bản có hậu tố **`no-example-audio`**. Ở bộ được kiểm tra, trường `cefr` gắn với từ đầu mục có thể khác `def_cefr` gắn với nghĩa; vì vậy dùng **subdeck C1 hoặc `def_cefr:C1`** khi muốn theo cấp nghĩa. Có 3.558 note mang trường đầu mục `cefr=C1`, nhưng subdeck C1 chỉ có 2.295 nghĩa: đây là hai cách đếm khác nhau.

Lọc có audio ví dụ trước; sau đó loại ví dụ chỉ là cụm từ, nghĩa đã biết và từ ít dùng. Ví dụ, một tổ hợp danh từ được đọc trọn vẹn vẫn không phải một câu hoàn chỉnh. Không coi hơn 22 nghìn note có file ví dụ là hơn 22 nghìn note đạt tiêu chuẩn của bạn.

Một note có ba ví dụ không có nghĩa cả ba đều có audio. Template chọn ví dụ luân phiên có thể đưa lên câu không có bản thu. Nếu làm audio-first, hãy gắn **một cặp câu–audio cố định đã kiểm tra** cho thẻ đó, thay vì lấy câu ngẫu nhiên nhưng phát một audio khác.

Về Anh–Mỹ: OALD có hai nhóm trường riêng; chọn một giọng để luyện phát âm chủ động, vẫn nghe cả hai để mở nhận diện. Refold bỏ các phrasal verb chỉ riêng Anh-Anh. Không suy rằng mọi câu trong một deck CEFR đều phản ánh cùng phương ngữ. Tư liệu từ điển tái đóng gói cũng không tự trở thành tài liệu do Oxford phát hành hay bảo chứng. [Cấu trúc và nguồn OALD do tác giả công bố](https://github.com/5mdld/anki-english-oald-decks/), [phạm vi phương ngữ Refold](https://refold.la/decks/buy/english-phrasal-verbs-deck).

#### Những tên phổ biến không được chọn làm core

- **Cambridge English Collocations in Use — Advanced**, bản 1.055 note được tìm thấy, có **0 audio** trên trang dữ liệu. Có thể làm nguồn cloze để bổ sung audio, nhưng không đạt yêu cầu nguyên trạng. [Trang bộ thẻ](https://anki-decks.com/anki-decks/english/cambridge-english-collocations-in-u/).
- **Destination C1&C2 của kelciour:** metadata 5.390 note, 2.345 audio; mẫu bài tập không có trường audio câu, mẫu từ có audio từ Anh–Mỹ. Không có căn cứ coi đây là bộ đủ sentence audio. [Deck](https://ankiweb.net/shared/info/1294764116).
- **(Cún) Vocabulary in Use — Advanced:** mẫu cho thấy trường audio từ, chưa cho thấy audio câu đóng gói; một mẫu `speaker` dùng nghĩa thiết bị âm thanh nhưng hai ví dụ nói về người nói/diễn giả. Nhiều chế độ quiz không bù được việc lệch nghĩa. [Deck](https://ankiweb.net/shared/info/1989656627).
- **English Vocabulary in Use Advanced — 1640832357:** kết quả tìm kiếm còn mô tả mẫu 7 note/ba bài đầu, dạng image occlusion, tác giả ghi chưa tối ưu mobile; truy vấn trực tiếp hiện trả trạng thái không còn. Không dùng cache để hứa tải được. [Trang được lập chỉ mục](https://ankiweb.net/shared/info/1640832357).
- **LexiDeck Multilingual:** mẫu 50 note đã mở có đủ năm audio ví dụ/note, 350 media. Tuy nhiên phần lớn mẫu là A1–B2; các ví dụ và bản dịch thay đổi nghĩa theo ngữ cảnh không luôn rõ. 5.700 từ, 28.000 câu và 38 giờ giọng người thu là tuyên bố của bộ đầy đủ, chưa thể xác nhận bằng mẫu. Không đặt lên trước nguồn C1/C2 chọn lọc. [Kho tác giả và mẫu](https://github.com/X-Trivle/LexiCore), [cấu trúc mẫu](https://github.com/X-Trivle/LexiCore/blob/main/ecosystem/lexideck-multilingual/DECK_STRUCTURE.md).

Không có cơ sở để hứa rằng GRE/SAT hay một bộ “20k words” tự giúp bạn kể chuyện hay thuyết phục tốt hơn. Với bạn, nghĩa mới của từ quen, cụm nói trọn ý, cách chuyển lập luận và cách điều chỉnh mức độ khẳng định có giá trị hơn số lượng đầu mục.

### 4. Thang điểm 100 và cách hiểu

Giữ đúng trọng số yêu cầu: **audio 25; ngữ cảnh 20; trình độ 15; từ/cụm phục vụ nói 15; bao phủ và tiến trình 10; chính xác/bảo trì 10; ảnh/tùy biến 5**.

Do chưa thẩm định nghe toàn bộ, tôi dùng **khoảng điểm đánh giá tạm**, không dùng điểm lẻ hay coi đây là khoảng tin cậy thống kê. Đầu thấp phản ánh giới hạn bằng chứng; đầu cao là mức hợp lý nếu các mẫu đại diện cho phần còn lại. Điểm chỉ so sánh **trong một ngôn ngữ, theo mục tiêu của bạn**, không phải thang đo chuẩn hóa hiệu quả học. Khoảng chồng lấn nhiều thì thứ hạng dựa trên mức phù hợp thực tế và bằng chứng, không dựa trên vài điểm tổng.

| Ngôn ngữ / phạm vi được chấm | Audio /25 | Ngữ cảnh /20 | Trình độ /15 | Nói /15 | Tiến trình /10 | Tin cậy /10 | Phụ trợ /5 | Tổng /100 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Trung: HSKStory, các gói đã kiểm tra | 17–21 | 16–18 | 14 | 10–12 | 8–9 | 6–8 | 3–4 | **74–86** |
| Trung: Ultimate, **chỉ HSK1–2 đã kiểm tra** | 17–22 | 12–16 | 13–15 | 8–10 | 9–10 | 5–7 | 4–5 | **68–85** |
| Nhật: Tango **N1** V9 | 20–24 | 15–18 | 12–14 | 10–12 | 8–9 | 6–8 | 3–4 | **74–89** |
| Nhật: IT Vocabulary v5.2 | 14–18 | 12–16 | 12–14 | 11–14 | 6–8 | 5–7 | 3–4 | **63–81** |
| Nhật: N1 Grammar v2.0.0 | 13–18 | 14–17 | 11–13 | 7–10 | 7–9 | 5–7 | 3–4 | **60–78** |
| Anh: Close-up C2, **chỉ mẫu 225 note** | 15–20 | 14–17 | 11–14 | 9–12 | 4–6 | 6–8 | 3–4 | **62–81** |

**Không chấm tổng giả cho các phạm vi còn thiếu bằng chứng:** Spoonfed bán hiện tại, toàn bộ Sentence Deck 33k câu, toàn bộ Ultimate, toàn bộ Close-up C2 1.611 note, Refold và C1 American. OALD gốc không qua cửa độ phủ audio câu; một nhóm lọc chưa cố định cũng không có điểm khóa học có ý nghĩa. Kaishi được ghi nhận chất lượng nền tảng, nhưng không xếp hạng nó như giải pháp N1→nói nâng cao.

## III. Mẫu thẻ thật

Các câu dưới đây lấy từ gói hoặc mẫu tác giả, **không phải câu tôi tự tạo rồi gán cho deck**. Khoảng trắng do HTML tô sáng được bỏ khi trình bày; nội dung từ ngữ giữ nguyên. Nghĩa Việt là diễn giải của báo cáo. Chỉ trích ngắn để minh họa, không tái bản bộ sách nguồn.

### Trung — HSKStory HSK1

| Từ và Pinyin từ | Câu thật | Pinyin câu trong deck | Nghĩa Việt | Audio |
|---|---|---|---|---|
| 一 — yī | 我买了一个苹果。 | wǒ mǎi le yí ge píng guǒ。 | Tôi đã mua một quả táo | File câu có trong gói; mẫu dài khoảng 1,90 giây ở tốc độ gốc |
| 小 — xiǎo | 这个杯子很小。 | Có trong thẻ; không trích thêm | Cái cốc này nhỏ | Có, khoảng 1,78 giây |
| 鸡蛋 — jī dàn | 我早饭吃了两个鸡蛋。 | Có trong thẻ; không trích thêm | Bữa sáng tôi ăn hai quả trứng | Có, khoảng 2,33 giây |

Cấu trúc: mặt trước `Hanzi`; mặt sau chữ/Pinyin màu thanh, nghĩa, audio từ, phần ví dụ mở ra khi nhấn. **Audio câu nằm trong HTML của trường `StoryTitle`**, không có trường `SentenceAudio` riêng ở phiên bản này. HSK1 đặt tốc độ phát câu **0,8x** trong nút bấm. Vì vậy thời lượng nghe qua nút dài hơn số đo file gốc. Khác biệt `yī` của từ và `yí` trước lượng từ ở câu là điểm cần phân biệt cách ghi từ điển với biến điệu trong lời nói. [Trang nguồn](https://hskstory.com/anki/hsk-1).

### Trung — Ultimate HSK1

| Từ | Câu thật | Pinyin câu trong deck | Nghĩa Việt | Audio |
|---|---|---|---|---|
| 在 — zài | 他一个人在公司。 | Tā yí gè rén zài gōngsī. | Anh ấy ở công ty một mình | `AudioSentence`; file trong gói, giải mã thành công |
| 再 — zài | 请你再说一遍。 | Có trong thẻ; không trích thêm | Nhờ bạn nói lại một lần | Có, riêng với audio từ |
| 做饭 — zuòfàn | 我爸爸正在做饭。 | Có trong thẻ; không trích thêm | Bố tôi đang nấu ăn | Có |

Note type gồm `Hanzi`, `Pinyin`, `Part of Speech`, `Meaning`, `SentenceHanzi`, `SentencePinyin`, `SentenceMeaning`, `AudioHanzi`, `AudioSentence`, `Image`. Cấu trúc này tốt cho tùy biến; nó không tự bảo đảm mọi nghĩa đã được minh họa đúng. [Bản HSK1](https://ankiweb.net/shared/info/1736976202).

**Spoonfed:** chưa tiếp cận gói trả phí để trích ba thẻ thật; không dựng mẫu thay thế. **Sentence Deck:** trang AnkiWeb có ba note mẫu cho `作业`, `乘坐`, `举行`, nhưng chưa kiểm tra được gói/media, nên không dùng chúng như bằng chứng đạt cửa audio. [Mẫu công khai](https://ankiweb.net/shared/info/258311532).

### Nhật — Tango N1, Ankidrone V9

| Từ/cụm thật | Câu thật | Công dụng và sắc thái | Audio |
|---|---|---|---|
| 真相 | 真相はまだ闇の中だ。 | Sự thật phía sau sự việc còn chưa sáng tỏ; hữu ích khi thuật lại tình huống | `SentAudio = N1_1430_2.webm`, có trong gói, đã giải mã mẫu |
| 思惑 | 大臣の思惑は不明だ。 | Ý đồ/tính toán chưa rõ; sắc thái khác với một ý kiến được phát biểu công khai | `N1_1499_2.webm`, có |
| 再現 | 現場で事故を再現する。 | Tái hiện sự việc; có thể liên hệ việc tái hiện sự cố kỹ thuật | `N1_1410_2.webm`, có |

Trường gồm `SentKanji`, `SentFurigana`, `SentEng`, `SentAudio`, từ/cách đọc/pitch/định nghĩa và `VocabAudio`. Đây là bằng chứng cụ thể về **audio câu khác audio từ**. Có thể thay mặt trước bằng `{{SentAudio}}`; không cần mua dịch vụ TTS để nghe những câu này. [Nguồn N1 và audio sách](https://tatsumoto-ren.github.io/blog/jlpt-tango-n1-anki-deck.html).

### Nhật — IT Vocabulary v5.2

| Cụm đích | Câu thật | Tình huống / register trong gói | Audio |
|---|---|---|---|
| 懸念 | パフォーマンスについて懸念があります。 | Nêu quan ngại về hiệu năng; `polite`, Communication–Concern | MP3 `tier3_008`, có và giải mã được |
| 念のため | 念のため確認させてください。 | Xin xác nhận lại; `polite`, Meeting–Confirm | `tier12_009`, có |
| 確定 | 異論がなければこれで確定します。 | Chốt quyết định khi không có phản đối; `polite`, Meeting–Decide | `tier12_083`, có |

Ba hướng có sẵn: nghe audio không chữ; đọc câu; cloze vào từ đích với gợi ý nghĩa. Câu thứ ba cũng cho thấy nói tự nhiên trong họp không nhất thiết phải dài. Để nâng khả năng lập luận, cần bổ sung lý do, điều kiện và phương án đối lập trong bài nói ngoài thẻ. [Nguồn](https://github.com/KakkoiDev/nihongo-it-anki).

### Nhật — N1 Grammar v2.0.0

| Mẫu | Trích ngắn từ câu thật trên mặt đáp án | Cách dùng cần nhận ra | Audio |
|---|---|---|---|
| ～を限りに | 今日を限りに… | Lấy thời điểm làm mốc chấm dứt; câu đầy đủ nói quyết tâm bỏ thuốc | `第2課 - 8_28.mp3`, có |
| ～かたがた | ご報告かたがた… | Kết hợp mục đích báo cáo và ghé thăm; cách nói trang trọng | `第7課 - 5_107.mp3`, có |
| ～までもない | …傘をさすまでもない。 | Chưa đến mức cần thực hiện hành động | `第18課 - 1_281.mp3`, có |

Mặt trước khuyết cấu trúc; mặt sau có câu đầy đủ, cách đọc, bản dịch và giải thích. Bảng giới hạn trích dẫn, không có nghĩa audio chỉ đọc phần trích. File audio đã được giải mã; **giọng là VOICEVOX**, không được gọi là bản thu người Nhật. [Gói nguồn đúng](https://github.com/mxggle/anki-jlpt-n1-grammar-example-sentences/releases/tag/v2.0.0).

### Anh — Close-up C2, mẫu 225 note

| Từ | Câu thật | Điều cần học | Audio |
|---|---|---|---|
| exit | James exited the room without saying goodbye. | Diễn đạt rời khỏi; so với cách nói thông dụng hơn trong hội thoại | `Example Audio` riêng, có trong gói |
| distrustful | Granddad is extremely distrustful of all politicians. | Kết hợp tính từ với giới từ | Có |
| reciprocal | The ceasefire took place under a reciprocal agreement. | Sự tương hỗ trong thỏa thuận; ngữ vực trang trọng | Có |

Template có `Word`, IPA, từ loại, định nghĩa, `Example`, `Audio`, `Example Audio`, bài/chủ đề. Câu khác trong bộ có thể dài hơn nhiều; mẫu đã kiểm tra có cả chủ đề tự nhiên học ít cần cho nói của bạn. Do đó không nên học mọi mục chỉ vì nhãn C2. [Nguồn](https://ankiweb.net/shared/info/804826171).

### Anh — OALD, ba mục đáp ứng riêng yêu cầu câu + audio

| Từ | Câu thật | Trọng tâm thực dụng | Audio |
|---|---|---|---|
| subtle | I decided to try a more subtle approach. | Cách tiếp cận kín đáo/tinh tế hơn | Audio Mỹ ví dụ1 `u_subtle__uss_3.mp3`, có và giải mã được |
| compromise | I refuse to compromise my principles. | Không đánh đổi nguyên tắc | Audio Mỹ ví dụ1 `u_compromise__uss_9.mp3`, có |
| concede | He reluctantly conceded the point to me. | Miễn cưỡng thừa nhận lập luận của người khác | Audio Mỹ ví dụ3 `u_concede__uss_3.mp3`, có |

Ở thẻ cuối phải dùng **ví dụ3 và audio3** cùng nhau. Đây là lý do không lấy bất kỳ audio nào của note rồi ghép với câu khác. Các mục cụ thể này đã được kiểm tra; không mở rộng kết luận sang cả 42.268 note. [Nguồn và bản tải](https://github.com/5mdld/anki-english-oald-decks/).

### Anh — Refold: ba mẫu công khai, chưa mở gói

Để giữ trích dẫn ngắn, bảng chỉ in **đoạn câu thật**, không trình bày chúng như câu đầy đủ:

| Cụm | Trích đoạn từ câu mẫu của tác giả | Audio |
|---|---|---|
| check out | …new cafe in town. | Tác giả nói phần practice có giọng Ben; gói chưa xác minh |
| shut down | Shut your computer down before you go home. | Như trên |
| put on | …pants on backwards this morning. | Như trên |

Blog nói rõ các ví dụ này đến từ deck. Điều đó xác minh nguồn văn bản mẫu, chưa xác minh file âm thanh được giao trong lần mua hiện tại. [Mẫu gốc và hướng dẫn](https://refold.la/blog/phrasal-verbs-deck).

**C1 American:** ba note mẫu thật gồm tình huống trách móc trong cuộc họp, hứa quá mức với khách hàng và chú ý giọng điệu email. Chúng có trường `Example Audio` trên AnkiWeb. Vì chưa mở gói nên không đưa thêm câu mẫu hay coi ba tham chiếu đó là độ phủ toàn bộ. [Trang nguồn](https://ankiweb.net/shared/info/524918335).

## IV. Bộ học đề xuất và cách tránh trùng

### Mandarin

1. **Core:** HSKStory HSK1, nghe trước; tiến lần lượt HSK2 và HSK3. Giữ thứ tự cấp, nhưng không bỏ qua từ chỉ vì nhận mặt chữ.
2. **Bổ trợ:** Ultimate để đối chiếu một nghĩa/cách đọc còn thiếu hoặc xem thêm ví dụ. **Không kích hoạt đồng thời hai bộ toàn phần.**
3. **Nghe/shadowing:** các truyện âm thanh cùng cấp; hiểu nội dung trước, rồi nhắc và đổi thông tin. Đừng nhầm việc deck miễn phí với toàn bộ thư viện truyện miễn phí. [HSKStory thông tin dịch vụ](https://hskstory.com/about).
4. **Nâng cao sau này:** tiếp tục HSK4→6→7–9, đồng thời chuyển sang đoạn nói thật. Khi gần kỳ thi, đối chiếu các mục đồng hình/đa âm trong đề cương, không chỉ kiểm số dạng chữ. Không cần cài deck thành ngữ 414 mục ngay từ đầu.

Hai tuần đầu nên học riêng hệ thống âm và thanh với người có thể sửa phát âm. Tiếng Nhật giúp bạn đọc chữ, nhưng không cho biết liệu bạn có nghe ra thanh 2/3 hoặc phân biệt phụ âm Mandarin chính xác. Tạm bắt đầu **5–8 từ/ngày**, mỗi từ một thẻ nghe; đây là mức thử tải, không phải “liều tối ưu” đã được nghiên cứu cho bạn.

### Nhật

1. **Core N1:** Tango N1. Suspend mục đã biết cả nghĩa, cách đọc lẫn cách dùng. Chỉ nhận mặt chữ mà chưa nghe/nói được thì chưa tính là đã biết hoàn toàn.
2. **Bổ trợ nghề nghiệp:** IT Vocabulary, ưu tiên nhóm 5–8, 11–12; chọn câu đúng công việc hiện tại. Nhóm email/ticket mang văn viết không nên tự động đưa vào bài luyện hội thoại.
3. **Ngữ pháp:** N1 Grammar chỉ cho mẫu bạn thực sự hay gặp hoặc cần thi. Không cố đưa cấu trúc văn viết nặng vào lời nói thân mật.
4. **Sau N1:** thêm khoảng **100–200 câu/cụm có audio nguyên bản**, lựa từ nội dung bạn đã xem/nghe. Đây là phần bù nhỏ, không yêu cầu xây lại hàng nghìn thẻ. Phân bố giữa thảo luận nghề nghiệp, đối thoại đời thường và kể chuyện.

Không cần thêm Kaishi/Core2k từ đầu. IT Vocabulary và Agentic Lab Priority Path của cùng tác giả có câu lặp; chọn một nhánh phù hợp thay vì học cả hai toàn bộ. Dò trùng theo **câu hoặc cụm + nghĩa**, không chỉ chuỗi chữ: một từ có hai nghĩa khác nhau không nhất thiết là thẻ thừa.

### Anh

1. **Lô core thử nghiệm:** Close-up C2 bản 225 note; suspend ngay mục đã biết hoặc ít dùng. Nếu bộ này không tạo ra khoảng trống đáng học, không mua bộ đầy đủ chỉ để hoàn thành một danh sách.
2. **Bổ trợ nghĩa/collocation:** OALD, bắt đầu ở C1, chỉ chọn mục có câu hoàn chỉnh và bản thu tương ứng. Tập trung từ/cụm cần dùng khi phản biện, xác nhận mức độ chắc chắn, mô tả đánh đổi, kể kết quả công việc.
3. **Phrasal verbs:** Refold chỉ nếu kiểm danh sách PHaVE cho thấy bạn còn nhiều nghĩa không truy xuất được. Đây là nguồn có lý do chọn từ, nhưng không phải khóa rhetoric C2. [Nghiên cứu PHaVE của Garnier & Schmitt](https://eric.ed.gov/?id=EJ1075475), [phạm vi Refold](https://refold.la/decks/buy/english-phrasal-verbs-deck).
4. **Diễn đạt C1+/C2:** một nhóm nhỏ câu từ phỏng vấn, podcast chuyên môn và thuyết trình. Lưu ngữ cảnh người nói đang phản đối, nhượng bộ, đùa hay kể chuyện; chỉ lưu câu chữ sẽ mất phần subtext.

Để tránh trùng, không học cùng lúc Close-up C1, C1 American và cả nguồn C1 của nó; C1 American được tác giả mô tả là bản sửa từ Close-up C1. OALD là kho chọn nghĩa, không là nhiệm vụ phải hoàn thành 42 nghìn thẻ.

### Bổ sung audio nguyên bản với ít thao tác

[asbplayer](https://github.com/asbplayer/asbplayer) có thể tạo thẻ từ video/subtitle, kèm đoạn âm thanh và ảnh. Dùng cùng AnkiConnect, kiểm tra điểm đầu/cuối câu và đúng audio track, rồi lưu vào media để ôn trên điện thoại. Đó là phương án bổ sung thực tế cho hài hước, tranh luận và kể chuyện mà các deck giáo trình còn thiếu.

Nếu dùng [movies2anki](https://ankiweb.net/shared/info/939347702), lưu ý tài liệu tác giả nói cấu hình mặc định có thể chỉ phát đoạn của file gốc qua mpv. Muốn dùng độc lập trên điện thoại cần chức năng tạo media mobile. Một thẻ có timecode tới phim trên máy tính chưa đáp ứng yêu cầu “audio trong deck”. Chỉ dùng nguồn bạn có quyền truy cập và giữ các thẻ trích phục vụ học cá nhân.

## V. Thiết kế thẻ phù hợp mục tiêu nói

### Chọn hướng truy xuất theo kỹ năng

| Kiểu thẻ | Mặt trước | Mặt sau / cách chấm | Phù hợp nhất |
|---|---|---|---|
| **Audio-first recognition** | Audio câu, không Hanzi/Kanji/Pinyin | Câu, nghĩa đích, cách đọc; Good khi nghe hiểu ý và nhận ra mục đích, không cần dịch từng chữ | Mandarin; tăng liên kết âm→nghĩa |
| **Targeted sentence** | Câu có một từ/cụm được đánh dấu | Giải thích nghĩa đang dùng, audio câu | Củng cố nghĩa theo ngữ cảnh ở Nhật/Anh |
| **Cloze theo cụm** | Câu khuyết cả cụm cần nói; gợi ý ý định/register | Cụm, câu hoàn chỉnh, audio; chấp nhận đáp án khác nếu thực sự tự nhiên | Collocation, giới từ, nhượng bộ, xác nhận |
| **Tình huống→cụm nói** | Một tình huống ngắn bằng Việt/Anh/Nhật phù hợp | Một hoặc hai phương án mẫu + khác biệt mức lịch sự | Truy xuất chủ động trong họp và hội thoại |
| **Production chọn lọc** | Ý cần diễn đạt và ràng buộc ngắn | Nói ra trước khi lật; so ý, cấu trúc và sắc thái, không bắt khớp mọi chữ | Khoảng 10–20% mục thật sự muốn dùng; tùy tải thực tế |
| **Shadowing** | Audio ngắn, có thể nghe lại | Transcript và trọng âm/nhịp; luyện riêng, không gộp mọi lỗi vào một điểm nhớ | Phát âm, nối âm, ngữ điệu |
| **Retell/paraphrase** | Đoạn nói hoặc một ý đã hiểu | Kể lại bằng cách khác, đưa ví dụ mới; cần phản hồi ngoài Anki | N1+/C1+ |

Truy xuất nghĩa và truy xuất từ để nói là hai bài toán khác nhau. Một nghiên cứu nhỏ với 18 sinh viên và từ giả cho thấy hướng luyện truy xuất ảnh hưởng kết quả kiểm tra; nó hỗ trợ việc tách dạng bài, **không chứng minh** rằng lật thẻ ngược sẽ tự tạo fluency. [Yanagisawa, 2016](https://www.jstage.jst.go.jp/article/katejournal/30/0/30_11/_article/-char/en).

### Tối ưu riêng cho bạn

**Mandarin:** ban đầu giấu cả chữ lẫn Pinyin. Nghe lần đầu để hiểu; lần hai kiểm âm/đích; lật để xem chữ quen tương ứng với âm Mandarin nào. Đừng dùng ảnh hay màu thanh ở mặt trước để đoán đáp án. Chấm tách tiêu chí nghe với phát âm: nghe hiểu nhưng tự nói sai thanh không nên làm mất ý nghĩa thống kê của thẻ nghe. Chọn ít mục để luyện nói riêng với phản hồi.

**Nhật:** không tạo reverse Kanji cho toàn bộ Tango. Ưu tiên khuyết cả cụm, ràng buộc casual/polite/formal, và thêm một tình huống của chính công việc. Giữ pitch từ như tham khảo; nhịp và ngữ điệu câu cần nghe nguyên bản. Không dùng mẫu công văn như mẫu trao đổi thân mật.

**Anh:** đặt nghĩa theo ngữ cảnh và người nghe lên trước “từ khó”. Định nghĩa đơn ngữ phù hợp ở C1; gợi ý Việt ngắn vẫn hữu ích nếu giúp phân biệt ý cần nói. Đừng học một phrasal verb bằng một nghĩa duy nhất rồi mặc định đúng ở mọi ngữ cảnh.

**Câu dài:** giữ câu đầy đủ và audio đầy đủ ở mặt đáp án để không mất quan hệ mệnh đề; trên mặt hỏi chỉ kiểm một cụm hoặc một quan hệ lập luận. Với đoạn quá dài, tạo các thẻ riêng từ những câu hoàn chỉnh bên trong, giữ thêm bối cảnh đoạn. Không cắt đến mức chỉ còn vài âm không tạo thành câu. Thông số khoảng 5–12 giây cho thẻ thường hoặc 10–20 giây cho câu nâng cao là gợi ý vận hành, không phải ngưỡng khoa học bắt buộc.

**Reverse cards:** chỉ bật khi có một kỹ năng cần đo riêng. Chuyển toàn bộ deck hai chiều thường tăng tải nhanh; dịch Việt→Nhật/Anh cả câu có nhiều đáp án đúng và dễ biến thành học thuộc một bản dịch. Cloze có gợi ý đủ rõ hoặc tình huống→cụm thường dễ chấm hơn.

### FSRS

1. Cập nhật các ứng dụng trước; bật FSRS trong Anki. Không chép thông số trí nhớ của người khác.
2. Bắt đầu desired retention **0,90**; chia preset khi độ khó nghe Mandarin và cụm nâng cao Nhật/Anh khác hẳn nhau. Điều chỉnh theo tải thực tế.
3. Dùng ít learning steps, chẳng hạn `10m`; tránh bước từ một ngày trở lên khi dùng FSRS. Tùy chọn để FSRS quản lý bước ngắn có tính thử nghiệm, không bắt buộc bật.
4. Quên thì **Again**; **Hard là vẫn nhớ nhưng khó**, không phải “sai gần đúng”. Bury sibling để các hướng của cùng note không nhắc đáp án cho nhau trong ngày.
5. Tối ưu khi đã có lịch sử đủ hữu ích, khoảng mỗi tháng; không liên tục đổi scheduler để xử lý một thẻ quá dài hoặc mơ hồ.

Đây là hướng dẫn phù hợp tài liệu hiện tại. Các mẹo Easy Bonus/Hard Interval từ bài cũ theo SM-2 không phải thông số cần sao chép vào FSRS. [Hướng dẫn FSRS chính thức của Anki](https://docs.ankiweb.net/manual/deck-options#fsrs).

### Phần bắt buộc nằm ngoài Anki

Mỗi tuần chọn 5–10 cụm muốn dùng, đưa vào một cuộc nói có mục đích: giải thích đánh đổi kiến trúc, phản đối lịch dự án, kể lại một sự cố, thuyết trình một đề xuất. Thu âm rồi nhận phản hồi về độ rõ ý, tự nhiên, register và nhịp nói. Có thể nói cùng một chủ đề theo vòng **4/3/2 phút**, sau đó thử chủ đề mới để kiểm tra chuyển giao; đây là kỹ thuật có nghiên cứu thực nghiệm nhỏ, không phải bảo đảm đạt C2. [De Jong & Perfetti, 2011](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9922.2010.00620.x).

Anki đo được bạn có truy xuất mục đã học hay không. Nó không tự đánh giá được bạn có đọc sai ý người nghe, dùng câu đùa đúng lúc, đổi chiến thuật thương lượng hay trả lời phản biện mới tốt đến đâu.

## VI. Cài đặt đầu tiên và phán quyết cuối

### 1. Mandarin — cài HSKStory HSK1 trước

**Xếp hạng:** (1) HSKStory; (2) Ultimate HSK3.0 để đối chiếu/thay thế; (3) Spoonfed bổ trợ có điều kiện. Sentence Deck 33k câu giữ ở danh sách cần kiểm tra thêm.

- Tải [HSK1 v11 trực tiếp](https://audio.hskstory.com/downloads/anki/hskstory-hsk1-anki-v11.apkg), hoặc dùng [trang HSK1](https://hskstory.com/anki/hsk-1) để lấy bản mới hơn.
- Import `.apkg` trên Anki Desktop, sync cả media. Không cần tạo audio bằng add-on hay mua thuê bao để ôn deck này offline.
- Sau đó chuyển sang nghe trước. Tôi chuẩn bị sẵn **`HSKStory_HSK1_SentenceAudio.tsv`**, gồm 300 cặp Hanzi→tên file audio câu **đã có trong gói v11**; không phát sinh audio mới.

**Áp tệp bổ sung:**

1. Import gói HSKStory HSK1 trước; tạo bản sao lưu.
2. Trong Manage Note Types, chọn `HSKStory HSK 1 Recognition v1` → Fields → thêm trường tên chính xác **`SentenceAudio`**.
3. Import TSV, chọn đúng note type ấy; map cột1 vào `Hanzi`, cột2 vào `SentenceAudio`, để các trường khác không được map và giữ nội dung hiện có. Chọn **cập nhật note hiện có khi trường đầu tiên khớp**, match scope theo note type, không tạo một deck 300 note mới. Kiểm tra vài dòng preview và kết quả import; nếu tạo 300 note mới thay vì cập nhật thì Undo và kiểm tra lại note type/field đầu tiên. [Cơ chế import/cập nhật của Anki](https://docs.ankiweb.net/manual/importing/text-files).
4. Mặt trước của card dùng đúng dòng sau; giữ mặt sau gốc để xem ví dụ/Pinyin/dịch:

```html
{{SentenceAudio}}
```

Tệp TSV chỉ thêm liên kết đến media; chưa được thử import trong ứng dụng sống. Kiểm tra vài thẻ, rồi chạy Check Media và sync xong trước khi ôn trên điện thoại. File âm thanh gốc phát ở tốc độ gốc bằng cơ chế Anki, khác nút HTML 0,8x của HSKStory; chọn tốc độ chậm ở app nếu bạn cần và app hỗ trợ.

Khi lên cấp, tải từ [HSK2](https://hskstory.com/anki/hsk-2), [HSK3](https://hskstory.com/anki/hsk-3), [HSK4](https://hskstory.com/anki/hsk-4), [HSK5](https://hskstory.com/anki/hsk-5), [HSK6](https://hskstory.com/anki/hsk-6), [HSK7–9](https://hskstory.com/anki/hsk-7-9). Overlay đi kèm **chỉ dành cho HSK1 v11**, không tự áp cho các cấp hoặc bản cập nhật đổi tên file.

### 2. Nhật — Tango N1, rồi IT Vocabulary chọn lọc

**Xếp hạng:** (1) Tango N1; (2) IT Vocabulary v5.2 cho công việc; (3) N1 Grammar v2.0.0 cho điểm yếu cụ thể. Sau N1 cần thêm audio nói thật theo nhu cầu, chưa có bộ sẵn nào ở đây thay được phần đó.

- Từ [trang tác giả](https://tatsumoto-ren.github.io/blog/ankidrone-essentials.html), tải **Ankidrone Essentials V9.apkg**, import rồi chọn **5. JLPT Tango N1**. Suspend các cấp dưới và thẻ giới thiệu nếu không dùng.
- Dùng mặt trước `{{SentAudio}}` nếu muốn ôn nghe, mặt sau giữ nguyên. Chỉ thêm thẻ nói cho mục thực sự cần.
- Tải **`it-vocab-complete.apkg`** từ [v5.2](https://github.com/KakkoiDev/nihongo-it-anki/releases/tag/it-vocab/v5.2). Audio đã đóng gói; không cần chạy Edge TTS để bắt đầu. Chọn Listening hoặc Vocabulary cho từng nhu cầu, hạn chế nhân ba tải ôn.
- Với iPhone, thử audio V9 ngay sau sync. Tác giả có bài về lỗi container của bản cũ; **chưa có kiểm thử thiết bị của tôi để bảo đảm tương thích mọi iOS**. Chỉ chuyển container/MP3 khi thật sự gặp lỗi, không đổi tên đuôi file suông. [Hướng dẫn tác giả](https://tatsumoto.neocities.org/blog/ankidrone-decks-audio-issues-on-ios).
- Nếu cần ngữ pháp, dùng [gói N1 GitHub đúng](https://github.com/mxggle/anki-jlpt-n1-grammar-example-sentences/releases/tag/v2.0.0), tránh link N2 bị gắn nhầm trong README.

### 3. Anh — thử bộ nhỏ trước khi trả tiền

**Xếp hạng theo khả năng bắt đầu ngay:** (1) Close-up C2 mẫu đã kiểm tra; (2) OALD làm nguồn chọn nghĩa/câu có audio; (3) Refold Phrasal Verbs nếu thật sự còn thiếu nghĩa; C1 American chỉ là ứng viên cần kiểm tra độ phủ.

- Import [Close-up C2](https://ankiweb.net/shared/info/804826171). Chỉ 225 note là bản đã kiểm tra. Có thể đổi mặt trước thành `{{Example Audio}}`; mặt sau giữ câu, định nghĩa và audio. Không cần AwesomeTTS để phát các file đi kèm.
- Nếu chọn OALD, tải đúng **bản có example audio** ở [release 26.10.20](https://github.com/5mdld/anki-english-oald-decks/releases/tag/26.10.20). Gói lớn, cần chờ sync media. Giữ online TTS tắt nếu muốn đánh giá chính xác phần audio offline đã có.
- Trong Browse, chọn subdeck `eggrolls-OALD-20k::01-CEFR::C1`, rồi chỉ giữ các nghĩa có câu hoàn chỉnh và audio ghép đúng. Các trường audio ví dụ là `exm_phonetics_am_audio1`/`br_audio1`, tương tự cho ví dụ2–3. Một bộ lọc chỉ kiểm “field không rỗng” mới là vòng sàng lọc đầu, chưa kiểm tra câu có hoàn chỉnh hay không.
- Chỉ mua [Refold](https://refold.la/decks/buy/english-phrasal-verbs-deck) nếu cần tập trung phrasal verbs Mỹ. Mua một lần mới có Anki download; không chọn thuê bao online với kỳ vọng nhận `.apkg`. Chưa đủ bằng chứng để tôi cam kết gói hiện tại đáp ứng mọi tiêu chí bạn đặt ra.

**Phán quyết:** Mandarin có giải pháp gần nhu cầu của bạn nhất và nên được ưu tiên thay đổi thiết kế thẻ ngay. Nhật có khung N1 tốt nhưng cần bổ sung lời nói và tình huống thật. Anh không thiếu danh sách nâng cao; điểm thiếu là một bộ đã biên tập tốt cho **sử dụng chủ động theo tình huống**. Bắt đầu từ các gói đã xác minh, chọn ít mục đúng nhu cầu và thêm một lớp luyện nói có phản hồi là lựa chọn đáng tin hơn việc tải thêm hàng chục nghìn từ.

## Phụ lục — dấu vết kiểm tra và giới hạn tái lập

| Gói được mở | Note / card | Độ phủ trường audio câu hoặc ví dụ | File tham chiếu thiếu trong kiểm tra |
|---|---:|---:|---:|
| HSKStory HSK1 v11 | 300 / 300 | 300 | 0 |
| HSKStory HSK2 v10 | 197 / 197 | 197 | 0 |
| HSKStory HSK3 v9 | 493 / 493 | 493 | 0 |
| HSKStory HSK4 v10 | 990 / 990 | 990 | 0 |
| HSKStory HSK5 v8 | 1.579 / 1.579 | 1.579 | 0 |
| HSKStory HSK6 v9 | 1.777 / 1.777 | 1.777 | 0 |
| HSKStory HSK7–9 v8 | 5.562 / 5.562 | 5.562 | 0 |
| Ultimate HSK1 | 300 / 300 | 300 | 0 |
| Ultimate HSK2 | 200 / 200 | 200 | 0 |
| Kaishi v2.4.3 | 1.501 / 1.501 | 1.500; một note giới thiệu | 0 |
| Ankidrone Essentials V9 | 7.724 / 7.724 | 6.971 `SentAudio`; xem phân cấp ở trên | 0 |
| IT Vocabulary v5.2 | 1.516 / 4.548 | 1.516 | 0 |
| N1 Grammar v2.0.0 | 343 / 343 | 343 | 0 |
| Close-up C2 sample | 225 / 225 | 225 | 0 |
| eggrolls OALD 26.10.20 | 42.268 / 42.268 | 22.153 có ít nhất một audio ví dụ; chưa loại cụm từ | 0 |
| LexiDeck sample | 50 / 50 | 50 có đủ năm audio ví dụ | 0 |

“0 thiếu” nghĩa là tham chiếu tìm thấy trong bản đồ media và thành viên archive; không có nghĩa mọi câu đều được đọc đúng. Các file mẫu còn được giải mã riêng. Bản đồ media có thể dùng lại một file cho nhiều thẻ, nên số file audio không phải số câu/note có audio.

Mã SHA-256 để phân biệt bản đã kiểm tra:

```text
HSKStory HSK1 v11
374a9195065796b05291af4f6287628db3242b0c93975ded39c7f98ef7996bad

Ankidrone Essentials V9
d8baeb206963fa456aa7edb03a0594c4089ec8e1886b2ed2f34d6b72e211c9cd

Close-up C2 sample
7b6d480bf1a62ed32ba2e80e6d9e4a38e2fea26ca00aa1ec3bc8f0e1546ed243

eggrolls OALD 26.10.20
2d0718504ba2b81b968df23fe45b79e9df12e7acbe344e0442a249db49ae092e
```

Các trang có thể đổi nội dung hoặc số note sau ngày kiểm tra. Nếu tải bản có hash khác, giữ kết luận tổng quát về hướng học nhưng kiểm tra lại những khẳng định về độ phủ media, trường và template. Tôi không dùng số lượt tải hay số upvote làm điểm chất lượng học tập.
