# Nghe trước, đọc sau: chọn Anki cho ba ngôn ngữ

*Báo cáo này do Claude (Claude Code) soạn ngày 2026-11-13.*

**Không có bộ thẻ dựng sẵn nào đáp ứng trọn vẹn mục tiêu ở cả ba ngôn ngữ. Dù vậy, ngôn ngữ nào cũng có một lời giải rõ ràng và bắt tay làm được ngay.**

Với tiếng Trung, thước đo đúng là đề cương thi HSK 3.0 (《HSK考试大纲》, công bố 2025-11, ghi "2026-07 实施"). Đề cương có 300 / 500 / 1.000 / 2.000 / 3.600 / 5.400 / 11.000 từ tích lũy và áp dụng cho kỳ HSK 1–6 mới, ra mắt toàn cầu ngày 13/12/2026. Đây **không** phải danh sách GF0025-2021 (11.092 từ), dù phần lớn bộ thẻ gắn nhãn "HSK 3.0" vẫn dùng danh sách này. Chỉ hai bộ vừa bám danh sách 2025, vừa có audio câu đầy đủ đã được kiểm tra file:

- **"New HSK 3.0 Mandarin Chinese Sentence Deck"**: thẻ Listening có mặt trước chỉ là âm thanh, nhưng cả câu lẫn giọng đều do AI tạo.
- **HSKStory "HSK 3.0 (2026)"**: gọn, khớp danh sách, nhưng mặt trước hiện chữ Hán, nên phải sửa thành thẻ nghe-trước.

Giọng người thật cho câu tiếng Trung chỉ có ở các bộ không theo HSK, như Spoonfed Chinese và MaoMi.

Với tiếng Nhật và tiếng Anh, mọi bộ dạng "danh sách từ" đều trượt mục tiêu. Lời giải chính là **tự đào câu từ drama, phim, reality show, podcast và các bài talk**: dùng Yomitan cùng asbplayer hoặc mpvacious, đổ vào note type Lapis/Senren (với tiếng Anh thì một note type đào câu đơn giản). Riêng tiếng Nhật có thêm các kho câu kèm clip gốc:

- **Immersion Kit**: đã kiểm tra file, 6/6 thẻ xuất có audio dài 2,1–10,2 s, lấy từ các drama như Legal High và 獣になれない私たち.
- **Nadeshiko**: 1,53 triệu câu, gồm 17.123 câu Terrace House và khoảng 28.500 câu YouTube; mới xác minh qua tài liệu.

Ankidrone Tango N1, bộ ngữ pháp 新完全掌握 N1 và "English. C1 Words, Idioms, Phrasal Verbs" chỉ còn vai trò khung từ vựng phụ.

Nghiên cứu có hai giới hạn lớn. Thứ nhất, AnkiWeb chặn tải và tìm kiếm (HTTP 429, yêu cầu đăng nhập) suốt phiên, nên nhiều bộ chỉ được đánh giá qua metadata và note mẫu mà AnkiWeb công khai. Thứ hai, không ai trong nhóm nghe được audio, nên độ tự nhiên và thanh điệu chưa được thẩm định bằng tai.

## Nhãn bằng chứng và giới hạn: AnkiWeb đóng cửa suốt phiên nghiên cứu

Mọi nhận định quan trọng đều kèm một trong các nhãn sau:

| Nhãn | Ý nghĩa |
|---|---|
| **[đã tự kiểm tra file]** | Nhóm nghiên cứu tự tải và mở gói `.apkg` hoặc file âm thanh: đọc collection và media map, đo thời lượng từ header MP3/Opus/WebM, đọc thẻ ID3. |
| **[đã kiểm tra audio mẫu]** | Chỉ tải được 3–6 file âm thanh AnkiWeb công khai cho note mẫu, chưa mở được cả bộ. |
| **[tài liệu chính thức]** | Trang chính thức, README, release notes, và dữ liệu chính AnkiWeb trả về qua endpoint `item-info`: số note, số file audio, ngày cập nhật, ba note mẫu. |
| **[cộng đồng]** | Review và diễn đàn. |
| **[quảng cáo]** | Lời người bán. |
| **[chưa xác minh]** | Chưa có xác nhận. |
| **[suy luận]** | Lập luận của nhóm, không phải dữ kiện có nguồn. |

**AnkiWeb bị chặn suốt phiên.** Endpoint tải của AnkiWeb trả về HTTP 429 "Please log in to download more decks", còn tìm kiếm ẩn danh trả "Please log in to perform more searches". Vì vậy không bộ nào chỉ có trên AnkiWeb được mở file. Các bộ sau chỉ được đánh giá qua metadata, note mẫu và (với tiếng Trung) vài file audio mẫu: NewHSK3 HSK 1–4, Ultimate, Last HSK, hnsaw, mọi bản Spoonfed, MaoMi, ChineseAudioFlashcards, Core 2k/6k, "Japanese Core Grammar (w/audio)", "C1 American Accent" và Kendra.

**Những gì thực sự được mở file:**

- HSKStory HSK 1–3 (tải trực tiếp).
- NewHSK3 HSK 5 (từ GitHub, đọc bằng HTTP range).
- Ankidrone Essentials V9 (qua Yandex).
- mxggle N1 v2.0.0, eggrolls JLPT10k v3.5, Kaishi v2.4.3, coolmule0.
- Sáu file xuất từng câu của Immersion Kit.
- Các deck mẫu của Lapis 1.7.0, Senren v5.1.0 và jp-mining-note.
- Ecattea COCA.
- Bản PDF 406 trang của đề cương HSK chính thức.

**Không mua hàng trả phí:** Spoonfed Gumroad v2, MaoMi, Refold, Mandarin Blueprint, Glassy-Gaia, PLAYNESE, JIVX. **Nadeshiko** trả 403 cho script và cần API key.

**Nguồn giọng được suy ra, không nghe bằng tai.** Nhóm dựa vào chữ ký encoder, thẻ ID3, nhãn AIGC và lời tác giả. Với tài khoản AnkiWeb của riêng bạn, việc tải deck nhiều khả năng diễn ra bình thường [suy luận từ chính thông báo lỗi].

## Phần I — Khuyến nghị điều hành: ba ngôn ngữ, ba trục khác nhau

### Tiếng Trung: danh sách 2025 là thước đo, thẻ nghe-trước là điều kiện bắt buộc

**Ba lớp chuẩn đang cùng tồn tại và rất dễ nhầm.**

- **HSK 2.0** có 6 cấp, 150 / 300 / 600 / 1.200 / 2.500 / 5.000 từ tích lũy. Theo một nguồn thứ cấp, nó vẫn được dùng cho các kỳ HSK 1–6 đến ngày 07/11/2026 ([studycli](https://studycli.org/hsk/the-new-hsk/)).
- **GF0025-2021** 《国际中文教育中文水平等级标准》 do Bộ Giáo dục và 国家语委 ban hành, hiệu lực từ 01/07/2021. Chuẩn gồm 三等九级 với tổng cộng 1.110 âm tiết, 3.000 chữ, 11.092 từ và 572 điểm ngữ pháp ([MOE 2021](http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202103/t20210329_523304.html)). Đây là nền của kỳ HSK 7–9, thi chính thức lần đầu ngày 26/11/2022 ([China Daily](https://www.chinadaily.com.cn/a/202211/05/WS6365aa87a3105ca1f22742c8.html)).
- **Đề cương HSK 3.0** 《HSK考试大纲》 do 中外语言交流合作中心 công bố tháng 11/2025, ghi "2026-07 实施". Bản PDF 406 trang có đủ 任务、话题、词汇、汉字、语法大纲 cho cấp 1–6 và 7–9. Nhóm tự parse toàn bộ 词汇大纲 và ra đúng **300 + 200 + 500 + 1.000 + 1.600 + 1.800 + 5.600 = 11.000 từ** [đã tự kiểm tra file] ([PDF đề cương chính thức](https://hsk.cn-bj.ufileos.com/3.0/%E6%96%B0%E7%89%88HSK%E8%80%83%E8%AF%95%E5%A4%A7%E7%BA%B21219.pdf)).

**Lịch thi.** Theo thông báo của CTI, HSK 3.0 cấp 1–6 **chính thức ra mắt toàn cầu ngày 13/12/2026**. Hạn đăng ký thi giấy là 24:00 ngày 16/11/2026; thi trên máy là 24:00 ngày 03/12/2026 [tài liệu chính thức] ([CTI](https://admin.chinesetest.cn/gonewcontent.do?id=51336883)). Trước đó đã có đợt thi thử toàn cầu ngày 31/01/2026, trong đó phần thi nói bắt buộc đi kèm cấp 3–6 ([ChinaNews](https://www.chinanews.com.cn/edu/2025/12-19/10536380.shtml)). Mốc "tháng 7/2026" mà Wikipedia nêu là ngày *thực thi đề cương*, không phải ngày chuyển kỳ thi ([Wikipedia](https://en.wikipedia.org/wiki/Hanyu_Shuiping_Kaoshi)).

| Lớp | Văn bản | Trạng thái năm 2026 | Số từ tích lũy theo cấp | Dấu hiệu nhận ra deck |
|---|---|---|---|---|
| HSK 2.0 | Danh sách HSK 2015 | Kỳ HSK 1–6 cũ, sitting cuối 07/11/2026 (nguồn thứ cấp) | 150 / 300 / 600 / 1.200 / 2.500 / 5.000 | 6 cấp, HSK1 = 150 từ |
| GF0025-2021 | 《国际中文教育中文水平等级标准》 | Hiệu lực từ 01/07/2021; nền của HSK 7–9 | 500 / 1.272 / 2.245 / 3.245 / 4.316 / 5.456 / 11.092 | Tổng 11.092 hoặc "11.0xx" note; HSK1 = 500 |
| Đề cương HSK 3.0 (2025) | 《HSK考试大纲》, 2025-11 发布, 2026-07 实施 | Kỳ HSK 1–6 mới từ 13/12/2026 | 300 / 500 / 1.000 / 2.000 / 3.600 / 5.400 / 11.000 | Tổng 11.000; HSK1 = 300 |

**Vì sao chênh lệch giữa hai danh sách quan trọng.** Chỉ **263/300 từ HSK1 năm 2025** có trong cấp 1 của danh sách 2021. 37 từ còn lại, như 一下, 不要, 你好, 便宜, 公司, 可以, 怎么样, bị đặt sai cấp. Toàn bộ hai danh sách chỉ chung khoảng 9.694 từ [đã tự kiểm tra file, phép so sánh của nhóm dựa trên [krmanik/HSK-3.0](https://github.com/krmanik/HSK-3.0)]. Cộng đồng đã gọi GF0025 là "HSK 3.0" từ năm 2021, nên nhãn trên deck không chứng minh được gì. Cách kiểm tra nhanh nhất là đếm số note theo cấp.

Đề cương 2025 cũng là thước đo pinyin. Nó ghi biến điệu 一/不 ngay trên từ đầu mục (一下 yíxià, 不客气 bú kèqi) và ghi thanh nhẹ (谢谢 xièxie, 朋友 péngyou) [đã tự kiểm tra file]. Với người mới bắt đầu, mục tiêu đúng là danh sách 2025.

**Hai bộ trên danh sách 2025 có audio câu đã được mở file.**

**"New HSK 3.0 Mandarin Chinese Sentence Deck"** (tác giả tompat, GitHub NewHSK3):

- **Cấu trúc:** ba câu cho mỗi từ; mỗi câu sinh ba note Listening / Reading / Writing.
- **Thẻ Listening chỉ có audio câu ở mặt trước.** Đây đúng là thứ người học này cần.
- **Gói HSK 5 [đã tự kiểm tra file]:**
  - 1.593/1.600 từ khớp danh sách chính thức.
  - 4.799/4.800 tham chiếu audio có file thật; mẫu 30 file dài 3,4–6,3 s.
  - Pinyin áp biến điệu nhất quán: "bú shì" xuất hiện 59 lần, dạng gốc 0 lần ([GitHub v1.0](https://github.com/NewHSK3/new-hsk-3-anki-deck/releases/tag/v1.0)).
- **Giọng do AI tạo.** Mọi file MP3 mang nhãn AIGC kiểu Trung Quốc `"Label":"1","ContentProducer":"HUABABSpeech7E01"`. Câu cũng được viết với sự hỗ trợ của ChatGPT.
- **Tác giả tự cảnh báo:** giọng nam "dễ lệch chuẩn phát âm hơn", và tác giả "chưa nghe hết từng câu" [tài liệu chính thức] ([AnkiWeb 258311532](https://ankiweb.net/shared/info/258311532)).

**HSKStory "HSK 3.0 (2026)"** [đã tự kiểm tra file] ([hskstory.com](https://hskstory.com/anki/hsk-1)):

- Khớp tuyệt đối 300/300 từ HSK1. Mọi note có clip câu, dài 1,3–4,4 s (trung vị 2,3–2,8 s).
- Pinyin câu có biến điệu và thanh nhẹ.
- File nhỏ (HSK1 chỉ 5,2 MB), cập nhật 24/10/2026.

Điểm yếu nằm ở thiết kế thẻ. Bộ chỉ có một thẻ "Recognition" với mặt trước là `{{Hanzi}}`. Audio được nhúng bằng thẻ HTML5 `<audio>` chứ không phải `[sound:]`, nên không tự phát; câu còn bị phát chậm 0,8x. Tức là đúng kiểu "đọc chữ trước khi nghe" mà chính người học đã cảnh báo. Nguồn giọng không được công bố: trang web quảng cáo "native-speaker voices Luna and Kai" [quảng cáo], còn định dạng 24 kHz không metadata gợi ý neural TTS [suy luận] ([HSKStory about](https://hskstory.com/about)).

**Giọng người thật cho câu chỉ có ở các bộ không theo HSK.**

- **Spoonfed Chinese** (khoảng 7.300–8.000 câu, sắp xếp i+1) có clip câu dài 2,8–4,6 s, mang dấu hiệu bản ghi người (LAME, MP3Gain) [đã kiểm tra audio mẫu]. Bản AnkiWeb đầy đủ nhất, `spoonfed_arty`, có 7.364 file audio cho 7.386 note nhưng đã cũ ([AnkiWeb 1307319045](https://ankiweb.net/shared/info/1307319045)). Nhiều bản khác thiếu khoảng 36% audio, và bản "Forkfed" lấp chỗ trống bằng Piper TTS ([AnkiWeb 772959041](https://ankiweb.net/shared/info/772959041)).
- **MaoMi** (£4, 2.361 note, một giọng giáo viên bản ngữ, có sẵn thẻ Audio) là lựa chọn gọn, nhưng nhóm chưa mua để kiểm tra ([MaoMi](https://maomichinese.com/product/anki1/)).
- **"🔥 New HSK 3.0: Ultimate"** của fa9r thay ví dụ và audio của 2.683 từ bằng bản thu thủ công "HSK - JK", và có ảnh trên mọi thẻ. Tuy vậy, nhóm chưa mở được file. Bộ này cũng đã đổi pinyin 一/不 về dạng từ điển (一下 yīxià), trái với cách ghi của đề cương [tài liệu chính thức] ([AnkiWeb 1736976202](https://ankiweb.net/shared/info/1736976202)).

**Khuyến nghị cho tiếng Trung:**

- **Lõi HSK:** NewHSK3 (chỉ dùng subdeck Listening) cộng HSKStory đã sửa thành thẻ nghe-trước.
- **Giai đoạn 0:** bộ luyện tai "Mandarin ear training with IPA/Pinyin/Zhuyin for Beginners" của helq, gồm 8.655 clip âm tiết bản ngữ phát ngẫu nhiên ([AnkiWeb 854183352](https://ankiweb.net/shared/info/854183352)).
- **Khi muốn nghe giọng người:** thêm Spoonfed hoặc MaoMi.
- **Gia sư là bắt buộc.** Cả hai bộ lõi đều dùng audio AI/TTS, nên phản hồi thanh điệu từ gia sư là phần không thể thay thế.

### Tiếng Nhật: dẫn đầu bằng câu thật từ drama, reality show và YouTube

**Không có bộ N1 nào dùng câu đời thực.** Nhóm không tìm thấy bộ N1 nào sắp theo cấp JLPT mà câu lấy từ nguồn đời thực có audio bản ngữ. Mọi bộ N1 kiểm chứng được đều dùng câu sách (JLPT Tango, 新完全マスター) hoặc cụm từ kiểu từ điển. Audio của chúng hoặc là giọng nhà xuất bản đọc câu ngắn, hoặc là neural TTS (VOICEPEAK, VOICEVOX). Theo tiêu chí người dùng đã làm rõ, các bộ này đều trượt.

**Lời giải chính là lộ trình đào câu**, gồm năm mắt xích:

- **Yomitan** để tra từ.
- **asbplayer** (Netflix, YouTube, phần lớn trang streaming) hoặc **mpvacious / Memento** (file trên máy) để cắt clip câu và ảnh chụp.
- **Anki Miner** để xử lý cả một mùa phim.
- **Lapis** hoặc **Senren** làm note type nhận dữ liệu.

Cả chuỗi đang được bảo trì tích cực trong năm 2026 [tài liệu chính thức] ([Yomitan](https://github.com/yomidevs/yomitan); [asbplayer](https://github.com/asbplayer/asbplayer); [Anki Miner](https://github.com/0xzerolight/anki_miner)):

| Công cụ | Phiên bản mới nhất |
|---|---|
| Yomitan | 26.11.2.0 (03/11/2026) |
| asbplayer | v1.22.0 (14/10/2026) |
| mpvacious | v26.10.18.0 |
| Anki Miner | v3.12.0 (08/11/2026) |

Khi mở note mẫu của Lapis và Senren, trường `SentenceAudio` đều chứa clip câu dài 1,4–5,5 s, so với 0,7–1,5 s của audio từ [đã tự kiểm tra file] ([Lapis](https://github.com/donkuri/lapis); [Senren](https://github.com/BrenoAqua/Senren)).

**Hai kho câu biến việc đào thành việc chọn.**

**Immersion Kit** [đã tự kiểm tra file] ([Immersion Kit](https://www.immersionkit.com/)):

- 14 drama Nhật (khoảng 81.680 câu) cùng khoảng 438.936 câu anime.
- Mỗi câu có clip phát sóng gốc, ảnh chụp và furigana; lọc được theo JLPT.
- Tải từng câu dưới dạng `.apkg`, hoặc đẩy thẳng vào Anki qua AnkiConnect.
- Sáu file xuất được mở đều có audio, dài 2,11–10,20 s, khớp timestamp trong tên file.

Các phim có giá trị nhất cho người đi làm [suy luận từ tiêu đề và các câu đã kiểm tra]:

- Legal High và Border: tranh luận pháp lý.
- 獣になれない私たち và 今日は会社休みます。: keigo công sở.
- 新聞記者: báo chí, chính trị.
- カルテット: hội thoại người lớn gián tiếp, mỉa mai.

Điểm trừ: index đứng yên từ 11/01/2025; API cũ trong tài liệu đã chết; câu thường chỉ là một mảnh phụ đề; còn ký hiệu phụ đề TV; bản dịch tiếng Anh đôi khi lệch.

**Nadeshiko** lớn hơn và "đời" hơn ([Nadeshiko stats](https://nadeshiko.co/en/stats)):

- Hơn 1.529.673 câu.
- Khoảng 55.000 câu live-action, trong đó **17.123 câu từ Terrace House Tokyo 2019–2020** (reality show không kịch bản).
- Khoảng 28.500 câu YouTube (podcast, vlog).
- Bản dịch tiếng Anh 94,8% do người dịch; thống kê cập nhật ngày 12/11/2026.

Tuy vậy, nhóm chưa lấy được câu mẫu hay file nào (trang trả 403, API cần key). Add-on **Aobana Reibun** tự điền câu, audio, ảnh và bản dịch từ Immersion Kit hoặc Nadeshiko vào bất kỳ danh sách từ nào ([AnkiWeb 1429349152](https://ankiweb.net/shared/info/1429349152)), nhưng cũng chưa được cài thử. Vì vậy cả Nadeshiko và Aobana Reibun được xếp **"điều kiện"**: nên thử ngay, nhưng chưa đủ bằng chứng để gọi là khuyến nghị chính.

**Khoảng trống còn lại là tiếng Nhật công sở.** Đếm trên API của Immersion Kit, trong phần drama có 0 câu chứa 納期, 1 câu 検討させていただきます, 1 câu 恐れ入りますが, 1 câu 株価 [đã tự kiểm tra file]. Nhóm cũng không tìm thấy bộ thẻ nào, miễn phí hay trả phí, cho họp, đàm phán, thuyết trình hay tranh luận có audio câu tự nhiên, dù đã tìm bằng tiếng Anh, Nhật, Trung và Việt.

**Phần mở rộng tối thiểu:** một danh sách 150–300 cụm nói chuyên nghiệp, chạy qua Aobana Reibun hoặc Immersion Kit; phần còn thiếu thì đào bổ sung từ drama công sở, YouTube tin tức – bình luận và podcast có transcript.

**Các bộ thi được giữ đúng nhãn "chỉ tham khảo / khung từ vựng phụ — không đáp ứng mục tiêu":**

- **Ankidrone Essentials V9 – Tango N1**: audio câu bản ngữ phủ 100% (2.023/2.023 note N1, giọng đọc của NXB ASK, trung vị 4,0 s). Nhưng câu là câu sách một mệnh đề, trung vị 18 ký tự, không câu nào dài từ 30 ký tự [đã tự kiểm tra file] ([Ankidrone Essentials](https://tatsumoto.neocities.org/blog/ankidrone-essentials)).
- **新完全掌握 N1 语法例句 (mxggle)**: câu dài hơn (trung vị 32 ký tự), nhưng audio là VOICEVOX TTS ([mxggle](https://github.com/mxggle/anki-jlpt-n1-grammar-example-sentences)).

### Tiếng Anh: đào thoại thật từ Netflix, talk và podcast

**Không bộ dựng sẵn nào đạt chuẩn.** Tiếng Anh lặp lại bài toán của tiếng Nhật, chỉ là ít công cụ chuyên biệt hơn. Chuẩn cần đạt gồm: lời nói bản ngữ thật, audio trọn câu đã xác minh, mức C1–C2, và có ngữ vực công sở, tranh luận, thuyết trình.

**Lời giải chính là thẻ dòng thoại tự đào**, từ ba nhóm công cụ:

- **asbplayer** cho Netflix, YouTube và các trang streaming. Tài liệu mô tả audio được ghi trực tiếp từ video, và có tùy chọn "Re-encode audio as mp3" [tài liệu chính thức] ([asbplayer settings](https://docs.asbplayer.dev/docs/reference/settings)).
- **Họ công cụ subs2srs / mpvacious / movies2anki** cho file của chính bạn. Chúng tạo "audio clips, snapshots, and video clips for each line of dialog" [tài liệu chính thức] ([subs2srs](https://subs2srs.sourceforge.net/)).
- **Language Reactor** cho Netflix, với một điều kiện quan trọng: chỉ dòng Netflix giữ audio gốc; dòng YouTube bị thay bằng giọng AI [cộng đồng] ([diễn đàn Language Reactor](https://forum.languagelearningwithnetflix.com/t/export-real-youtube-audio/36419)).

**Bộ media dựng sẵn có tồn tại, nhưng chưa bộ nào qua được quy tắc bắt buộc:**

- **Glassy-Gaia** bán bộ "13 Reasons Why" (mùa 3–4 được quảng cáo ở mức C1) và "TED-Ed" (B1–C1), với thẻ nghe-trước và phụ đề tiếng Việt. Rất hấp dẫn cho người học này, nhưng chỉ có bằng chứng [quảng cáo] ([Glassy-Gaia](https://glassygaia.gumroad.com/)).
- **Kelciour** có mẫu subs2srs từ khoảng 60 phim (12 Angry Men, All About Eve, Bridget Jones's Diary…), với audio dòng thoại từ phim. Tuy vậy, mỗi phim chỉ có 10–15 phút đầu và không có link tải công khai [tài liệu chính thức] ([Kelciour Notion](https://kelciour.notion.site/English-3-263745ea25208026b057f019153b6378)).
- **Bộ connected-speech của Kendra's Language School** có hai tốc độ cho mỗi note, nhưng chỉ là cụm ngắn để luyện giải mã chuỗi âm nối ([AnkiWeb 1364160335](https://ankiweb.net/shared/info/1364160335)).

**Các bộ danh sách chỉ làm khung.** Mọi bộ Oxford, EVP, idiom, phrasal verb, collocation tìm được đều rơi vào một trong ba trường hợp: không có audio câu, audio câu là TTS, hoặc câu là one-liner tự đặt. Chúng là **"chỉ tham khảo / khung từ vựng phụ — không đáp ứng mục tiêu"**. Oxford Phrase List và PHaVE nên dùng làm danh sách mục tiêu để săn trong media, không học như thẻ ([Oxford Phrase List](https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford-phrase-list); [PHaVE](https://nottingham-repository.worktribe.com/output/762398)).

## Phần II — Bảng so sánh: điểm cao nhất thuộc về phương pháp, không thuộc về deck

Thang 100 điểm áp dụng riêng cho từng ngôn ngữ:

| Tiêu chí | Điểm tối đa |
|---|---|
| Audio trọn câu | 25 |
| Độ tự nhiên/phong phú của ví dụ | 20 |
| Phù hợp trình độ | 15 |
| Cụm từ hướng tới nói | 15 |
| Độ phủ/lộ trình | 10 |
| Chính xác/bảo trì | 10 |
| Ảnh/tùy biến/phụ trợ | 5 |

Điểm lấy từ đánh giá sơ bộ trong ghi chú nghiên cứu. Biên ± thể hiện độ bất định: phần lớn do không nghe được audio và không mở được file AnkiWeb. Không nên đọc điểm như một phép đo chính xác. Chênh lệch dưới khoảng 5 điểm nằm trong vùng sai số.

### Tiếng Trung

| Deck | Người tạo | Cấp độ | Note/thẻ | Audio câu: có/chất lượng | Chất lượng ví dụ | Ảnh | Ngữ cảnh/cụm từ | Giá | Bảo trì | Đánh giá chung | Link chính thức |
|---|---|---|---|---|---|---|---|---|---|---|---|
| New HSK 3.0 Mandarin Chinese Sentence Deck | tompat (GitHub NewHSK3) | HSK 1–9, danh sách 2025 | HSK 1–4: 18.000 note (AnkiWeb). HSK 5: 14.400 note, 4.800 thẻ mỗi subdeck. Trọn bộ khoảng 99.000 thẻ [quảng cáo] | Có ở 100% câu (HSK 5: 4.799/4.800 file; 3,4–6,3 s). **AI** (nhãn AIGC) [đã tự kiểm tra file HSK 5; HSK 1–4 chỉ qua metadata]. Không có audio từ | 3 câu/từ, AI viết; pinyin biến điệu nhất quán | Không | Thẻ Listening chỉ audio; Reading có ô gõ; Writing dạng cloze + nét chữ (cần internet) | Miễn phí | v1.0, 01/08/2026; 1 commit | **75 ±7** — lõi nghe tốt nhất | [AnkiWeb 258311532](https://ankiweb.net/shared/info/258311532), [GitHub v1.0](https://github.com/NewHSK3/new-hsk-3-anki-deck/releases/tag/v1.0) |
| HSKStory "HSK 3.0 (2026)" | HSKStory | HSK 1–9, danh sách 2025 | 300 / 197 / 493 / 990 / 1.579 / 1.777 / 5.562 = 10.898 note; 1 thẻ/note | Có, khoảng 100% (HSK1: 296 clip/300 note); 1,3–4,4 s. Nguồn không công bố; "native-speaker voices" [quảng cáo]; khả năng là neural TTS [suy luận]. HTML5, phát 0,8x | 1 câu/từ, ngắn, đời thường | Không | Chỉ thẻ chữ Hán → nghĩa | Miễn phí, `.apkg` trực tiếp | Cập nhật 24/10/2026 | **72 ±6** — nhập môn tốt nhất, nhưng phải sửa thẻ | [hskstory.com/anki/hsk-1](https://hskstory.com/anki/hsk-1), [AnkiWeb 1703580298](https://ankiweb.net/shared/info/1703580298) |
| 🔥 New HSK 3.0: Ultimate | fa9r | HSK 1–9, danh sách 2025 | HSK1: 300 note / 565 audio / 258 ảnh; HSK7 phần 1: 1.867 note | Có, theo mô tả và note mẫu. Audio của 2.683 từ là bản thu thủ công "HSK - JK" [cộng đồng/tác giả]; phần còn lại không rõ engine; chưa mở file | 1 câu/từ, một phần được tuyển tay | Có, hầu hết thẻ | Chỉ chữ Hán → tiếng Anh; pinyin 一/不 theo dạng từ điển | Miễn phí, CC BY-NC-SA | 10–11/10/2026 | **67 ±10** — điều kiện | [AnkiWeb 1736976202](https://ankiweb.net/shared/info/1736976202) |
| Spoonfed Chinese (bản `spoonfed_arty` / Gumroad v2) | promagma (v2); người re-upload trên AnkiWeb | Không theo HSK; sơ → trung cấp; i+1 | 7.386 note / 7.364 audio (bản 1307319045); v2 "over 8000 sentences" [quảng cáo] | Có, giọng người (LAME/MP3Gain, 2,8–4,6 s) [đã kiểm tra audio mẫu]; độ phủ suy từ số file; các bản khác thiếu khoảng 36% | Câu đời thường; về sau có câu lạ; errata 437 dòng | Không | Thẻ Trung → Anh, Anh → Trung; v2 có ghi chú ngữ pháp | Bản arty miễn phí; Gumroad gợi ý $3 | AnkiWeb 23/01/2023; v2 không rõ ngày | **73 ±7** — giọng người tốt nhất, nhưng không theo HSK | [AnkiWeb 1307319045](https://ankiweb.net/shared/info/1307319045), [Gumroad](https://promagma.gumroad.com/l/IEmpwF) |
| MaoMi Chinese – Beginner to Advanced | MaoMi Chinese (giọng "Molly") | Không theo HSK; sơ → cao cấp | 2.361 note, khoảng 7.000 thẻ | Có, theo trang bán (giáo viên bản ngữ). Clip câu 2,6–3,3 s chỉ thấy trong một bản re-upload trái phép; chưa mua bản gốc | Câu thực dụng xen từ | Không | Có sẵn thẻ Audio | £4 | Đang bán năm 2026 | **72 ±10** — lựa chọn trả phí gọn | [MaoMi](https://maomichinese.com/product/anki1/) |
| Chinese HSK 1 – 150 Words, 300 Example Sentences | ChineseAudioFlashcards | HSK 2.0 cấp 1 | 451 note / 450 audio | Có, người thật tên Chang/Susu (ID3), 128 kbps [đã kiểm tra audio mẫu] | Gò bó trong từ vựng HSK1; có báo lỗi dịch/pinyin [cộng đồng] | 1 | Câu cơ bản | Miễn phí (HSK 2–5 trả phí) | 2016 | **63 ±8** — đệm tuần đầu | [AnkiWeb 1578796058](https://ankiweb.net/shared/info/1578796058) |
| Mandarin ear training with IPA/Pinyin/Zhuyin | helq | Phát âm sơ cấp | 98 note / 8.655 audio | Không phải câu: âm tiết bản ngữ phát ngẫu nhiên (~1 s) | Không áp dụng | 2 | Nhận diện thanh, âm đầu, vần; có IPA/Zhuyin | Miễn phí | 17/07/2023 | Ngoài thang điểm câu; mức phù hợp cho phát âm 9/10 | [AnkiWeb 854183352](https://ankiweb.net/shared/info/854183352) |

Điểm chi tiết theo tiêu chí, lấy từ ghi chú. Các bộ bị loại có Refold Mandarin 1k (~67, audio "AI-generated" theo FAQ chính thức), Last HSK 3.0 2026 (~60, lỗi dữ liệu) và Mandarin Blueprint (~69 ±12, $449, thiết kế đọc-trước).

| Deck | Audio /25 | Ví dụ /20 | Cấp độ /15 | Nói /15 | Độ phủ /10 | Chính xác /10 | Phụ trợ /5 | Tổng |
|---|---|---|---|---|---|---|---|---|
| NewHSK3 | 21 | 15 | 10 | 11 | 9 | 7 | 2 | 75 ±7 |
| Spoonfed | 20 | 13 | 13 | 10 | 9 | 5 | 3 | 73 ±7 |
| HSKStory | 19 | 13 | 14 | 9 | 9 | 7 | 1 | 72 ±6 |
| MaoMi | 19 | 13 | 13 | 11 | 7 | 6 | 3 | 72 ±10 |
| Ultimate | 16 | 13 | 11 | 7 | 9 | 7 | 4 | 67 ±10 |
| CAF HSK1 | 18 | 10 | 14 | 9 | 6 | 4 | 2 | 63 ±8 |

Spoonfed xếp điểm ngang HSKStory. Nhưng người dùng yêu cầu tiếng Trung đi theo cấu trúc HSK, nên Spoonfed giữ vai trò bổ sung giọng người, không phải lõi.

### Tiếng Nhật

| Deck / nguồn | Người tạo | Cấp độ | Note/thẻ | Audio câu: có/chất lượng | Chất lượng ví dụ | Ảnh | Ngữ cảnh/cụm từ | Giá | Bảo trì | Đánh giá chung | Link chính thức |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tự đào câu: Lapis/Senren + Yomitan + asbplayer/mpvacious/Memento/Anki Miner | donkuri, BrenoAqua, yomidevs, asbplayer, Ajatt-Tools, 0xzerolight | N1+ (tùy nguồn bạn chọn) | Tùy số câu bạn đào | Có: clip cắt từ nguồn; note mẫu 1,4–5,5 s, Opus [đã tự kiểm tra file note mẫu] | Do bạn chọn: drama, reality show, YouTube, tin tức | Có (ảnh chụp) | Toàn quyền chọn cụm; Lapis có chế độ thẻ audio | Miễn phí (trừ phí streaming) | Các công cụ đều cập nhật năm 2026 | **~85 ±10** — chấm cho phương pháp | [Lapis](https://github.com/donkuri/lapis), [Yomitan](https://github.com/yomidevs/yomitan), [asbplayer](https://github.com/asbplayer/asbplayer) |
| Immersion Kit (phần drama) | Mathew | N1+, lọc được theo JLPT | 81.680 câu drama / 14 phim; 438.936 câu anime | Có: clip phát sóng gốc ở 6/6 file xuất (2,11–10,20 s) [đã tự kiểm tra file] | Thoại người lớn có kịch bản; nhiều mảnh ngắn; bản dịch EN đôi khi lệch | Có | Tìm theo cụm (`exactMatch`); xem được câu lân cận | Miễn phí | Index đứng yên từ 11/01/2025; API cũ đã chết | **~76 ±8** — chính | [immersionkit.com](https://www.immersionkit.com/) |
| Nadeshiko | Natsume / BrigadaSOS | N1+ | Hơn 1.529.673 câu; live-action ~55.000 (Terrace House 17.123); YouTube ~28.500 | Có, theo tài liệu chính thức; chưa mở file (403, cần API key) | Tự nhiên nhất (reality show, podcast, vlog); dịch EN 94,8% do người | Có | Export to Anki; có API và SDK | Miễn phí (cần key) | Rất tích cực; v2.6.0; thống kê 12/11/2026 | **~79 ±10** — điều kiện | [nadeshiko.co](https://nadeshiko.co/en/) |
| Aobana Reibun (add-on) | Wyzmic | Theo danh sách của bạn | Không áp dụng | Kế thừa từ Immersion Kit/Nadeshiko; chưa cài thử | Câu thật | Có | Biến danh sách cụm thành thẻ câu thật | Miễn phí | 1.0, đã thử trên Anki 26.9 | **~78 ±10** — điều kiện | [AnkiWeb 1429349152](https://ankiweb.net/shared/info/1429349152), [GitHub](https://github.com/Wyzmic/Aobana-Reibun) |
| Ankidrone Essentials V9 — Tango N1/N2 | Tatsumoto Ren / AJATT-Tools | N5–N1 | 7.718 note; N1 2.023; N2 1.659 | Có, 100% ở N1/N2; giọng đọc NXB (ASK), WebM/Opus, trung vị 4,0 s [đã tự kiểm tra file]; rủi ro không phát trên iOS | Câu sách một mệnh đề, trung vị 18 ký tự | N1: 240 ảnh | Có pitch; thẻ production tùy chọn | Miễn phí (bản quyền vùng xám) | Bản V9, 22/08/2026 | **~60 ±6 — chỉ tham khảo / khung từ vựng phụ — không đáp ứng mục tiêu** | [Ankidrone Essentials](https://tatsumoto.neocities.org/blog/ankidrone-essentials) |
| 新完全掌握 N1 语法例句 | mxggle | Ngữ pháp N1 | 343 note | Có, 343/343, nhưng **VOICEVOX TTS**, trung vị 5,40 s [đã tự kiểm tra file] | Câu sách nhiều mệnh đề, trung vị 32 ký tự | Không | Giải thích tiếng Trung; có ghi chú ngữ vực (StyleNotes) | Miễn phí (giấy phép mâu thuẫn) | v2.0.0, 13/08/2026 | **~57 ±5 — chỉ tham khảo / khung từ vựng phụ — không đáp ứng mục tiêu** | [GitHub mxggle](https://github.com/mxggle/anki-jlpt-n1-grammar-example-sentences) |
| Core 2k/6k [Pitch Graphs, Optimized, Links] | Cộng đồng (nội dung iKnow) | Khoảng N4–N2 | 5.996 note / 11.910 audio | Rất có thể có (có trường Sentence Audio; giọng iKnow); chưa mở file | Câu iKnow ngắn | Không rõ | Một số từ công việc | Miễn phí (bản quyền không rõ) | 25/07/2025 | **~55 ±10 — chỉ tham khảo / khung từ vựng phụ — không đáp ứng mục tiêu** | [AnkiWeb 1487314101](https://ankiweb.net/shared/info/1487314101) |

| Nguồn | Audio /25 | Ví dụ /20 | Cấp độ /15 | Nói /15 | Độ phủ /10 | Chính xác /10 | Phụ trợ /5 | Tổng |
|---|---|---|---|---|---|---|---|---|
| Tự đào câu | 22 | 19 | 15 | 13 | 4 | 7 | 5 | ~85 ±10 |
| Nadeshiko | 19 | 18 | 12 | 13 | 4 | 8 | 5 | ~79 ±10 |
| Aobana Reibun | 19 | 17 | 13 | 13 | 6 | 5 | 5 | ~78 ±10 |
| Immersion Kit | 21 | 17 | 12 | 12 | 4 | 5 | 5 | ~76 ±8 |
| Ankidrone Tango N1 | 19 | 7 | 10 | 6 | 9 | 6 | 3 | ~60 ±6 |
| mxggle N1 | 14 | 8 | 13 | 7 | 6 | 7 | 2 | ~57 ±5 |
| Core 2k/6k | 18 | 9 | 7 | 9 | 7 | 3 | 2 | ~55 ±10 |

Các bộ khác đã kiểm tra nhưng không vào bảng:

- **Kaishi 1.5k**: audio câu bản ngữ đầy đủ, nhưng quá dễ so với N2. Điểm khoảng 58–61 cho người học này; tổng các tiêu chí con là 61, ghi chú làm tròn còn ~58 ([Kaishi](https://github.com/donkuri/Kaishi)).
- **【egg rolls】JLPT N1-N5 一万词 (~50)**: ví dụ N1 chủ yếu là cụm, không phải câu trọn, audio là VOICEPEAK TTS, nên trượt quy tắc audio trọn câu ([eggrolls](https://github.com/5mdld/anki-jlpt-decks)).
- **"Japanese Core Grammar JLPT N5-N1 (w/audio)" (~35 ±15)**: làm "with the help of ai", nguồn audio chưa rõ ([AnkiWeb 1723302220](https://ankiweb.net/shared/info/1723302220)).

Immersion Kit đứng trên Nadeshiko trong khuyến nghị dù điểm thấp hơn, vì đây là kho duy nhất qua được bước kiểm tra file.

### Tiếng Anh

| Deck / nguồn | Người tạo | Cấp độ | Note/thẻ | Audio câu: có/chất lượng | Chất lượng ví dụ | Ảnh | Ngữ cảnh/cụm từ | Giá | Bảo trì | Đánh giá chung | Link chính thức |
|---|---|---|---|---|---|---|---|---|---|---|---|
| asbplayer (+ Yomitan tùy chọn) | killergerbah / asbplayer | Tùy nguồn | Tùy | Có: audio ghi từ video [tài liệu chính thức]; hành vi cụ thể trên Netflix (DRM) chưa kiểm chứng trong phiên | Thoại thật do bạn chọn | Ảnh chụp | Trường Source/URL; "update last card" | Miễn phí (AGPL) | v1.22.0, 14/10/2026 | **~78 (tạm)** — chính | [GitHub](https://github.com/killergerbah/asbplayer), [docs](https://docs.asbplayer.dev/docs/intro) |
| subs2srs / mpvacious / movies2anki / gogadget (trên file của bạn) | Nhiều tác giả | Tùy nguồn: TED, talk show, podcast | Tùy | Có: clip từng dòng thoại [tài liệu chính thức]; riêng gogadget chỉ biết qua snippet | Thoại thật; podcast thì không kịch bản | Ảnh chụp/video | Cắt theo dòng, xử lý hàng loạt | Miễn phí | subs2srs v29.7; mpvacious 10/2026 | **~80** — chính | [subs2srs](https://subs2srs.sourceforge.net/), [mpvacious](https://github.com/Ajatt-Tools/mpvacious), [gogadget](https://pypi.org/project/gogadget) |
| Language Reactor (Netflix) | Language Reactor | Tùy nguồn | Tùy | Netflix: audio gốc [cộng đồng]. YouTube: **giọng AI** | Thoại drama thật | Có | Từ đánh dấu bị bỏ trống trong câu ngữ cảnh | Pro khoảng $5/tháng [chưa xác minh] | Có báo lỗi export [cộng đồng] | **~78** — phụ, có điều kiện | [LR help](https://languagereactor.com/help/export) |
| Glassy-Gaia: 13 Reasons Why S3–S4; TED-Ed | Glassy-Gaia | B2–C1 [quảng cáo] | Không rõ | "Native" [quảng cáo]; chưa mở file | Thoại teen drama; TED-Ed là lời dẫn có kịch bản | Có | "Smart Notes"; phụ đề tiếng Việt | Từ $0 | Hoạt động 2025–2026 | **~72 (tạm)** — điều kiện | [13 Reasons Why](https://glassygaia.gumroad.com/l/13_reasons_why), [TED-Ed](https://glassygaia.gumroad.com/l/english_ted_ed_videos) |
| Mẫu subs2srs của Kelciour | Kelciour | Không gắn CEFR | 50–100 note/phim | Có audio dòng thoại từ phim [tài liệu chính thức] | Phim kinh điển, phim gia đình | Video clip | 5–15 s video ở mặt trước | Đổi bằng ủng hộ/đặt hàng; không có link công khai | Phân phối riêng | **~63** — điều kiện | [Kelciour Notion](https://kelciour.notion.site/English-3-263745ea25208026b057f019153b6378) |
| Kendra's Language School connected-speech | Kendra's Language School | Luyện giải mã chuỗi âm | 332 note / 664 audio / 332 ảnh | Có, hai tốc độ; người nói chưa rõ | Cụm ngắn đơn giản | Có (chữ nằm trong ảnh) | Không | Miễn phí | 08/02/2022 | **~55** — phụ | [AnkiWeb 1364160335](https://ankiweb.net/shared/info/1364160335) |
| English. C1 Words, Idioms, Phrasal Verbs. American Accent. | Người làm lại từ "Close-up Word List C1" của Kelciour | C1 | 1.731 note / 3.039 audio | Có trường Example Audio; khả năng là TTS [chưa xác minh] | One-liner tự đặt, hơi hướng công sở | 0 | Idiom, phrasal verb | Miễn phí | 09/12/2025 | **~60 — chỉ tham khảo / khung từ vựng phụ — không đáp ứng mục tiêu** | [AnkiWeb 524918335](https://ankiweb.net/shared/info/524918335) |

| Nguồn | Audio /25 | Ví dụ /20 | Cấp độ /15 | Nói /15 | Độ phủ /10 | Chính xác /10 | Phụ trợ /5 | Tổng |
|---|---|---|---|---|---|---|---|---|
| Họ subs2srs trên file của bạn | 22 | 19 | 14 | 11 | 3 | 8 | 3 | ~80 |
| Language Reactor (Netflix) | 21 | 19 | 13 | 11 | 3 | 6 | 5 | ~78 |
| asbplayer | 20 (tạm) | — | — | — | — | — | — | ~78 (tạm) |
| Glassy-Gaia | 18 | 17 | 12 | 11 | 7 | 3 | 4 | ~72 (tạm) |
| Kelciour | 21 | 19 | 8 | 7 | 2 | 3 | 3 | ~63 |
| C1 American Accent | 15 | 8 | 13 | 10 | 6 | 7 | 1 | ~60 |
| Kendra | 18 | 10 | 6 | 8 | 6 | 4 | 3 | ~55 |

**Về điểm asbplayer.** Điểm asbplayer bị hạ tạm thời vì nhóm tiếng Anh không đọc được tài liệu về cơ chế ghi âm. Nhóm thiết kế thẻ thì đọc được tài liệu: audio "recorded from the video", trên trang streaming được ghi theo thời gian thực, và có nút "Re-record" ([asbplayer settings](https://docs.asbplayer.dev/docs/reference/settings)). Vì vậy điểm thực của asbplayer nhiều khả năng ngang nhóm subs2srs [suy luận].

**Các bộ danh sách khác đều chỉ tham khảo:**

- "Advanced English Vocabulary" (~48): một file audio mỗi note, giọng "robotic", không có audio câu.
- Ecattea COCA (~45): "audio câu" là TTS Microsoft lấy qua proxy không chính thức lúc ôn [đã tự kiểm tra file].
- "4000 Essential English Words 1" (~42): mức A1–A2.
- Refold English Phrasal Verbs (~60, trả phí): không nói rõ audio có phủ cả câu hay không.

## Phần III — Thẻ mẫu thật: chỉ chép nguyên văn từ ghi chú

Mọi mẫu dưới đây được chép nguyên văn từ ghi chú nghiên cứu, kèm cách lấy. Bộ nào không có mẫu thật thì nói rõ là không có; không có mẫu nào được tự viết ra.

### Tiếng Trung

**NewHSK3 — gói HSK 5.** Mẫu lấy bằng cách đọc collection `.anki21b` và media map qua HTTP range từ bản release GitHub [đã tự kiểm tra file]. Mẫu thứ tư là note mẫu của gói HSK 1–4 do AnkiWeb công khai [tài liệu chính thức].

| # | Từ | Câu | Pinyin câu | Dịch | Audio |
|---|---|---|---|---|---|
| 1 | 对比 · duìbǐ · to compare; comparison, contrast | 通过对比两份报告，我们发现数据差距很大。 | Tōngguò duìbǐ liǎng fèn bàogào, wǒmen fāxiàn shùjù chājù hěn dà. | By comparing the two reports, we found that the gap in the data was very large. | `[sound:通过对比两份报告，我们发现数据差距很大。.mp3]` · không ảnh |
| 2 | 毛笔 · máobǐ · writing brush | 他从小学习书法，对毛笔的选择很讲究。 | Tā cóng xiǎo xuéxí shūfǎ, duì máobǐ de xuǎnzé hěn jiǎngjiu. | He has studied calligraphy since childhood and is very particular about his choice of writing brush. | `[sound:他从小学习书法，对毛笔的选择很讲究。.mp3]` · Yun: yes |
| 3 | 病情 · bìngqíng · illness condition | 经过治疗，他的病情已经明显好转。 | Jīngguò zhìliáo, tā de bìngqíng yǐjīng míngxiǎn hǎozhuǎn. | After treatment, his condition has clearly improved. | (ghi chú không chép trường audio của note này) |
| 4 | 作业 · zuòyè · homework (HSK 1–4) | 老师说明天要交作业。 | Lǎoshī shuō míngtiān yào jiāo zuòyè. | The teacher said the homework must be handed in tomorrow. | (note mẫu AnkiWeb) |

Trường `Yun` có giá trị "yes" ở 2.400/4.800 note, nhiều khả năng là cờ đánh dấu giọng nam [suy luận].

**HSKStory.** Mẫu trích từ gói `.apkg` v11 (HSK1) và v9 (HSK3) tải trực tiếp [đã tự kiểm tra file]. Không note nào có ảnh.

| # | Cấp | Từ · pinyin đầu mục · nghĩa | Câu ví dụ | Pinyin câu | Dịch | File audio từ / câu |
|---|---|---|---|---|---|---|
| 1 | HSK1 | 一下 · yī xià · "(after a verb) a bit; a little …" | 我想休息一下，下午再学习。 | wǒ xiǎng xiū xi yí xià， xià wǔ zài xué xí。 | I want to rest for a bit and study again this afternoon. | `hskstory-hsk1-002.mp3` / `hskstory-hsk1-example-08dd25995eaf.mp3` |
| 2 | HSK1 | 不客气 · bù kè qi · you're welcome | 不客气，很高兴你喜欢我做的饭。 | bú kè qi， hěn gāo xìng nǐ xǐ huan wǒ zuò de fàn。 | You're welcome; I'm glad you like my cooking. | `hskstory-hsk1-019.mp3` / `hskstory-hsk1-example-2ef0a640f4d1.mp3` |
| 3 | HSK1 | 没有 · méi yǒu · not have; there is not; have not | 我没有姐姐，有一个弟弟。 | wǒ méi yǒu jiě jie， yǒu yí ge dì di。 | I do not have an older sister; I have a younger brother. | `hskstory-hsk1-212.mp3` / `hskstory-hsk1-example-1c4c438f86e9.mp3` |
| 4 | HSK3 | 不用 · bù yòng · need not | 明天学校放假，我们不用上课。 | míng tiān xué xiào fàng jià， wǒ men bú yòng shàng kè。 | School is on break tomorrow, so we don't need to attend class. | `hskstory-hsk3-012.mp3` / `hskstory-hsk3-example-f7ce9fab7be2.mp3` |

Các mẫu này cho thấy một điểm không nhất quán: pinyin đầu mục ghi dạng gốc (一下 yī xià), còn pinyin câu ghi đúng biến điệu (yí xià).

**Spoonfed Chinese `spoonfed_arty` (1307319045).** Ba note mẫu AnkiWeb công khai [tài liệu chính thức]; thời lượng đo từ file `mpreview` [đã kiểm tra audio mẫu].

| # | English | Pinyin | Hanzi | Audio |
|---|---|---|---|---|
| 1 | There are people pirating textbooks. | Yǒu rén dào shuā jiàokēshū. | 有人盗刷教科书。 | `[sound:0.mp3]` → 3,21 s |
| 2 | Since the weather became sunny, let's hang our clothes. | Jìrán tiānqíng le, wǒmen bǎ yīfu liàng le ba. | 既然天晴了，我们把衣服晾了吧。 | `[sound:1.mp3]` → 3,06 s |
| 3 | My little sister very much resembles my mother. | wǒ mèimei hěn xiàng wǒ māma. | 我妹妹很像我妈妈。 | `[sound:2.mp3]` → 2,80 s |

**Các bộ phụ và bổ trợ:**

- **Ultimate:** có ba note mẫu AnkiWeb [tài liệu chính thức]:
  - 路上 | lùshang | 我在路上看见了老师。 | Wǒ zài lùshang kànjiàn le lǎoshī. | I saw the teacher on the road.
  - 白色 | báisè | 我喜欢白色的衣服。 | Wǒ xǐhuan báisè de yīfu.
  - 外 | wài | 外面在下雨。 | Wàimian zài xiàyǔ.
- **CAF HSK1:** có ba mẫu [tài liệu chính thức + đã kiểm tra audio mẫu]:
  - 这个苹果一块钱。 | Zhège píngguǒ yīkuài qián. | This apple costs one yuan. (3,06 s)
  - 我家没有电脑 | Wǒjiā méiyǒu diànnǎo | I don't have a computer at home. (3,13 s)
  - 她是我们的好朋友。 | Tā shì wǒmen de hǎo péngyǒu. (4,08 s)
- **MaoMi:** bản demo chính thức chỉ có mẫu là từ đơn (是 shì, 上海 Shànghǎi, 二 Èr). Mẫu câu duy nhất nằm trong bản re-upload trái phép, nên không chép ở đây. **Chưa có mẫu câu hợp lệ.**
- **helq:** ghi chú chỉ có một mẫu nguyên văn: `Pinyin=guo | Zhuyin=ㄍㄨㄛ | IPA=[ku̯ɔ] | Audio 1=[sound:0.mp3] … [sound:7.wav]`. **Không đủ ba mẫu.**

### Tiếng Nhật

**Immersion Kit (drama).** Năm mẫu đầu lấy từ file `.apkg` xuất từng câu qua `apiv2.immersionkit.com/download_sentence` [đã tự kiểm tra file]. Ba mẫu sau lấy từ JSON tìm kiếm của API; thời lượng tính từ timestamp trong tên file. Bản gốc của mẫu 1 chứa ký tự vô hình U+202A/U+202C.

| # | ID | Câu (nguyên văn) | Dịch tiếng Anh đi kèm | Audio |
|---|---|---|---|---|
| 1 | `drama_weakest_beast_000005202` (獣になれない私たち 第07話) | 「（晶） あっ ご足労いただき恐縮です」 | Thank you for coming today. | 3,36 s; có ảnh |
| 2 | `drama_legal_high_season_1_000000035` | 「（男性）わずか ２分ほどの 一駅区間ならば→ 席を譲る必要もないどころか→ 立ち座りの動作を 余計に強いるのみと判断し→ 申し出なかったまで。 以上。 何か反論は？」 | Since there's just two minutes between his stations... ...there was no need to strongly pressure someone to give up their seat for him... ...and make them stand until a proper judgment could be made otherwise. That is all. Do you have any objections? | `Legal_High_01_0.03.57.720-0.04.07.930.mp3`, 10,20 s |
| 3 | `drama_weakest_beast_000002511` (第03話) | 「要するに 小さな欠点や 問題に関してはオッケーとする」 | In short, we're okay with small flaws and problems. | 5,38 s |
| 4 | `drama_overprotected_kahoko_000004762` | 「“加穂子には ママが必要なの” って言えばいいんじゃねえのか」 | Well, if you just want her to come home, you should say, "I need you, Mama." Right? | 4,18 s |
| 5 | `drama_the_journalist_000002724` | 「おっしゃるとおり」 | Precisely. | 2,11 s |
| 6 | `drama_weakest_beast_000003684` (từ API) | 「恐れ入りますが もう一度 ご用件を…」 | Would it be possible to explain it again? | 2,83 s |
| 7 | `drama_border_000000480` (từ API) | 「謙遜なのか値段交渉なのか どっちなんだ？」 | Are you being modest, or are you trying to negotiate with me? | 3,2 s |
| 8 | `drama_legal_high_season_1_000000638` (từ API) | 「暗黙のルールと されている手順を踏むこと→ そのものがマナーなんです。 反論 ありますか？」 | Going through the proper procedures is the tacit rule behind good manners. Do you have any objections? | 6,1 s |

Mẫu 2 và 8 cho thấy rõ các nhược điểm: ký hiệu `→` của phụ đề TV, nhãn người nói, và bản dịch tiếng Anh dịch thoáng hơn câu gốc.

**Kết quả mẫu của lộ trình tự đào (Lapis, Senren).** Đây là note ví dụ đi kèm gói note type, được mở bằng script của nhóm [đã tự kiểm tra file]. Chúng chứng minh định dạng thẻ mà lộ trình tạo ra, không phải nội dung bạn sẽ đào.

- **Lapis:** 十中八九 / 「十中八九 せこい小遣い稼ぎだと思う」.
  - `SentenceAudio` = `shoushiminseries04_08m44s853ms_08m47s653ms.ogg` (Opus, 3,05 s), so với `ExpressionAudio` 1,51 s.
  - Có ảnh webp, giải nghĩa J-J từ 三省堂国語辞典 第八版 và JMdict, pitch "nakadaka".
  - `MiscInfo`: "Shoushimin_Series EP04 (08m46s485ms)".
- **Senren:** 精霊 — 「一瞬 僕には見えないはずの桜の精霊が 見えた気がした」, audio `nihoneyoukosoelfsan12_14m27s891ms_14m33s396ms.ogg`.

Ghi chú không có mẫu thứ ba nguyên văn cho nhóm này.

**Nadeshiko và Aobana Reibun: không có mẫu thật.** Nadeshiko trả 403 cho script và API cần key; Aobana chưa được cài. Không mẫu nào được dựng thay.

**Ankidrone Tango N1 (tham khảo).** Mẫu trích từ `collection.anki21b` của file V9, đọc qua HTTP range [đã tự kiểm tra file].

| # | Câu | Dịch | Audio câu | Từ mục tiêu |
|---|---|---|---|---|
| 1 | 喘息が酷くなって、息が出来ない。 | My asthma has worsened, and I can't breathe. | `[sound:N1_0877_2.webm]` | 喘息 · ゼンソク / 0 · asthma · `[sound:N1_0877_1.webm]` |
| 2 | そんな理由では、てんで話にならない。 | That can't be a reason at all. | `N1_1683_2.webm` | てんで · テンデ/0 · "(not) at all; completely; utterly; entirely; altogether" |
| 3 | 感動で涙が止まらなかったが、所詮架空の話だ。 | I was so moved I couldn't stop crying, but it's only a fictitious story. | `N1_1086_2.webm` | 所詮 (furigana 所詮[しょせん / そせん]) · ショセン/0 |
| 4 (N2, có lỗi) | 犬は主人に忠実だ。 | — | `N2_0870_Chap7-Sec4_2.webm` | SentFurigana ghi 犬[けん] — sai, đúng phải là いぬ |

**mxggle 新完全掌握 N1 (tham khảo).** Trích từ gói `.apkg` v2.0.0 trên GitHub [đã tự kiểm tra file]. Ba mẫu:

1. **Lesson 19.** Câu: 失業している上、子供にもお金がかかり、生活が苦しいこと極まりない。
   - Mẫu ngữ pháp: ～極まる・～極まりない
   - Dịch: 不仅失业，而且养孩子也很花钱，生活真是艰难至极。
   - Audio: `[sound:第19課 - 18_319.mp3]`
   - StyleNotes: 硬い言い方
2. **Lesson 9.** Câu: 子供のためとあれば、わたしはどんなことでも我慢しますよ。
   - Mẫu ngữ pháp: ～とあれば
   - Audio: `[sound:第9課 - 1_131.mp3]`
3. **Lesson 12.** Câu: 犬や猫じゃあるまいし、上の人の言葉に従うだけなんてごめんだ。
   - Mẫu ngữ pháp: ～ではあるまいし
   - StyleNotes: 話し言葉 (口语)
   - Audio: `[sound:第12課 - 8_184.mp3]`

### Tiếng Anh

**Các lộ trình dẫn đầu (asbplayer, subs2srs/mpvacious, Language Reactor) không có mẫu thật.** Thẻ của chúng được tạo từ nội dung chính bạn chọn, nên ghi chú không có và không thể có mẫu. Kelciour cũng không có mẫu nào lấy được.

**Glassy-Gaia (bằng chứng quảng cáo).** Mẫu duy nhất đọc từ ảnh preview của chính người bán [quảng cáo]:

- **Dòng thoại:** "Say you're standing in front of a door, ready to pull it open."
- **Bản tiếng Việt:** "Giả dụ bạn đang đứng trước một cái cửa, sẵn sàng kéo mở nó."
- **Bản tiếng Trung:** "假想你正站在一扇门前，准备拉门".
- **Ghi chú:** "Say: imperative to prompt imagination → Say you are planning a surprise party for a friend."
- **Hàng kiểm tra gõ đáp án:** "Say youre standing in front of a door ready to pull it open".

Ảnh không ghi video TED-Ed nguồn. Các câu sau dấu "→" do người bán tự viết [suy luận]. **Chỉ có một mẫu.**

**Kendra (connected speech).** Hai note mẫu AnkiWeb [tài liệu chính thức]: `{序号: "0269", 常速: "[sound:0.mp3]", 慢速: "[sound:1.mp3]", 图片: "[image:2.jpg]", 备注: ""}` và `{序号: "0239", 常速: "[sound:3.mp3]", 慢速: "[sound:4.mp3]", 图片: "[image:5.jpg]", 备注: ""}`. Chữ tiếng Anh dường như chỉ nằm trong ảnh [suy luận].

**C1 American Accent (tham khảo).** Ba note mẫu AnkiWeb [tài liệu chính thức]:

| Front (câu) | Back | Definition | Audio |
|---|---|---|---|
| “Her reproach was clear in the meeting.” | reproach | express disapproval | `[sound:0.mp3]` + Example Audio `[sound:1.mp3]` |
| “Don’t overpromise the client; it’ll backfire.” | overpromise | promise more than possible | `[sound:2.mp3]` + `[sound:3.mp3]` |
| “Be mindful of tone in emails.” | mindful | conscious and attentive | `[sound:4.mp3]` + `[sound:5.mp3]` |

**Ecattea COCA (tham khảo).** Rút ngẫu nhiên từ collection [đã tự kiểm tra file]:

- line — `We hung the wet clothes on the <em>line</em>. [=<em>clothesline</em>]`
- beautiful — `You have the most <em>beautiful</em> smile/eyes.`
- cut — `The driver <em>cut</em> across three lanes of traffic to get to his exit and nearly caused an accident.`

Không có `[sound:]` nào; audio câu được gọi TTS trực tuyến lúc ôn.

## Phần IV — Learning stack: mỗi ngôn ngữ một lõi, không chạy hai bộ cùng danh sách

### Tiếng Trung: tai trước, chữ sau, và lõi đi lệch nhau một cấp

Stack tiếng Trung xếp theo thứ tự ưu tiên của người học: nhận diện lời nói, rồi thanh điệu, rồi ngữ cảnh, rồi nối âm với chữ Hán đã biết.

**Giai đoạn 0 (2–4 tuần): bộ helq.** Mỗi ngày 10–20 thẻ. Bộ này phát một âm tiết bản ngữ ngẫu nhiên và yêu cầu đoán thanh, âm đầu hoặc vần, nên người học không thể đoán theo thứ tự thẻ ([GitHub helq](https://github.com/helq/pinyin-beginners-anki-deck)). Lý do đặt nó trước: huấn luyện nhận diện thanh điệu biến thiên cao, nhiều người nói, đã cho mức tăng khoảng 21%, tổng quát hóa được sang từ và người nói mới, và còn giữ sau 6 tháng ([Wang et al. 1999](https://doi.org/10.1121/1.428217)).

**Cùng lúc: HSKStory HSK1, đã sửa thành thẻ nghe-trước.** Nhịp khoảng 10 từ mới mỗi ngày.

**Từ khi xong HSK1: thêm subdeck Listening của NewHSK3, đi sau HSKStory một cấp.** Khi HSKStory ở HSK2 thì NewHSK3 chạy Listening HSK1 (900 thẻ); HSK2 có 600 thẻ, HSK3 có 1.500 thẻ.

- **Lợi ích:** câu AI của NewHSK3 rơi vào vùng từ đã biết, nên thẻ nghe thực sự luyện hiểu chứ không luyện đoán từ mới [suy luận].
- **Tạm ngưng Reading và Writing** cho đến khi bắt đầu luyện nói và viết. Ba loại thẻ là ba note riêng biệt, nên tùy chọn "bury siblings" không tách chúng ra; suspend theo subdeck là cách chắc chắn [suy luận].

**Sau HSK3 (tùy chọn): giọng người thật.** Thêm Spoonfed `spoonfed_arty` hoặc MaoMi, bật thẻ audio-only, tối đa 5 câu mới mỗi ngày. Áp dụng danh sách errata 437 dòng của Tclack88 cho Spoonfed ([errata](https://github.com/Tclack88/misc-analysis/blob/main/mandarin_frequency_analysis/chinese_anki_backup/spoonfed_chinese_deck_corrections.txt)).

**Lớp thành ngữ:** HSKStory có bộ Chengyu 414 câu, có audio từ và audio câu ([AnkiWeb 926470945](https://ankiweb.net/shared/info/926470945)). Chỉ nên dùng từ khoảng HSK 5 [suy luận].

**Shadowing:** gắn thẻ `shadow` cho các câu ngắn 2–4 s và luyện trong buổi riêng, không lồng vào lúc ôn thẻ.

**Chống trùng lặp:**

- Không chạy song song HSKStory, Ultimate và Last HSK: cùng một danh sách 2025.
- Không dùng bất kỳ deck nào trên danh sách 2021, như "Another HSK 3.0 vocabulary deck" (11.088 note) hay Mega Mandarin (11.092 từ) ([AnkiWeb 549107549](https://ankiweb.net/shared/info/549107549)).
- Chọn một trong hai: Spoonfed hoặc MaoMi.
- Không dùng thẻ đọc chữ Hán làm thẻ đầu tiên của bất kỳ bộ nào.

### Tiếng Nhật: một deck đào câu duy nhất, các nguồn chỉ là đầu vào

| Lớp | Nguồn | Liều lượng gợi ý | Cách tránh trùng |
|---|---|---|---|
| Lõi | Deck Lapis tự đào: asbplayer với Netflix/YouTube có phụ đề Nhật, mpvacious với file trên máy | 5–10 thẻ/tập phim; 10–15 phút đào mỗi buổi | Mọi nguồn đổ về **một** note type, một deck |
| Lõi bổ sung | Immersion Kit (Legal High, Border, 獣になれない私たち, 今日は会社休みます。, 新聞記者, カルテット), qua nút "Add to Anki" hoặc Aobana Reibun | Theo danh sách cụm mục tiêu | Ánh xạ trường vào Lapis để không sinh note type thứ hai |
| Cụm diễn đạt nâng cao | Danh sách 150–300 cụm: keigo, nối ý khi thảo luận, phản hồi, rào đón | 10–20% số thẻ có thêm thẻ production | Gắn tag ngữ vực: `会議`, `敬語`, `タメ口`, `皮肉`, `相槌` |
| Nghe/shadowing | Nadeshiko (Terrace House, YouTube) khi có API key; các clip 2–8 s tag `shadow` | 4 buổi × ≥10 phút/tuần, có tự ghi âm | Shadowing chạy trên filtered deck, không tạo note mới |
| Khung phụ (tham khảo) | Ankidrone Tango N1 làm checklist từ vựng N1; mxggle N1 để đọc cấu trúc | Suspend toàn bộ từ đã biết qua công việc | Dùng danh sách N1 làm **đầu vào** cho Aobana Reibun, để từ thi được gắn câu drama thật |

**Ngữ vực.** Drama có kịch bản (Immersion Kit) cho audio rõ và ngữ vực người lớn: lập luận ở tòa, keigo công sở, mỉa mai. Reality show và YouTube (Nadeshiko) gần hội thoại tự phát hơn: từ đệm, rào đón, nói chồng lên nhau. Hai nguồn bổ sung cho nhau, nhưng nên tách bằng tag thay vì tách deck.

**Không cài các bộ này:** Kaishi và Core 2k/6k gần như trùng hoàn toàn với vốn N2 hiện có (Kaishi được dựng từ Core2k, Core10k và Tango N4/N5). Không nhập hai bộ từ vựng N1 cùng lúc.

### Tiếng Anh: thoại thật làm lõi, danh sách làm bản đồ săn

| Lớp | Nguồn | Liều lượng gợi ý | Cách tránh trùng |
|---|---|---|---|
| Lõi | Thẻ dòng thoại tự đào: asbplayer với Netflix/streaming; mpvacious với TED/TEDx, talk show, podcast có phụ đề | 5–10 thẻ mới/ngày | Một note type đào câu duy nhất |
| Lõi bổ sung | Language Reactor nếu đã có Pro (chỉ dòng Netflix) | Thay thế, không chạy song song với asbplayer | Chọn một công cụ cho Netflix |
| Cụm diễn đạt nâng cao | Oxford Phrase List, PHaVE, phrase tự ghi ở công ty, dùng làm **danh sách săn** | 10–20% thẻ có thẻ production | Chỉ tạo thẻ khi gặp cụm trong media thật |
| Nghe/shadowing | Clip 2–8 s tag `shadow`; tùy chọn Kendra connected-speech để luyện giải mã chuỗi âm nối | 4 buổi × ≥10 phút/tuần | Kendra là bộ kỹ năng, không trùng nội dung |
| Khung phụ (tham khảo) | "C1 Words, Idioms, Phrasal Verbs. American Accent" | Chỉ đọc lướt như checklist | Không ôn song song với deck đào câu |

**Về giọng Anh – Anh.** Nhóm không tìm thấy bộ câu giọng Anh – Anh ở mức C1. Kelciour có Bridget Jones's Diary và Three Men in a Boat, nhưng nếu muốn giọng UK thì phải tự đào từ phim, talk show và podcast Anh.

## Phần V — Thiết kế thẻ: Anki xây kho truy xuất, không xây độ trôi chảy khi nói

### Thẻ nghe-trước (audio-first recognition)

**Thiết kế:**

- **Mặt trước:** chỉ audio câu (có thể thêm ảnh chụp với thẻ đào từ media), không chữ.
- **Nhiệm vụ:** hiểu câu; với tiếng Trung, nói được thanh của từ mục tiêu.
- **Mặt sau:** transcript (chữ Hán + pinyin có dấu hoặc số thanh + màu thanh), nghĩa, và audio phát lại.

**Bằng chứng.** Với thanh điệu, màu giúp ích nhưng hơi kém đường nét cao độ hoặc số thanh ([Godfroid et al. 2017](https://doi.org/10.1111/lang.12246)). Vì vậy nên hiện dấu hoặc số *kèm* màu, không chỉ màu.

**Tiếng Trung: bắt buộc giấu chữ Hán ở mặt trước.** Người đọc được chữ Hán qua tiếng Nhật sẽ đọc vượt qua audio.

**Ba trường hợp cụ thể:**

- **NewHSK3:** thẻ Listening đã đúng mẫu này.
- **Spoonfed:** Card 1 hiện chữ Hán rồi mới phát audio sau một khoảng lặng 1 giây (`[sound:_silence.mp3]`) "to give you a moment to test your Hanzi recognition" ([Gumroad](https://promagma.gumroad.com/l/IEmpwF)). Phải đổi thành `{{Audio}}` ở mặt trước. Các trường English / Pinyin / Hanzi / Audio tách riêng, nên sửa mất vài phút.
- **HSKStory:** cần thêm trường vì audio nằm trong HTML (xem mục mở rộng ở Phần VI).

Mẫu template minh họa, chưa thử trong Anki [suy luận]:

```
Mặt trước:   {{SentenceAudio}}
Mặt sau:     {{SentenceAudio}}
             <div class="zh">{{ExampleHanzi}}</div>
             <div>{{ExamplePinyin}}</div>
             <div>{{ExampleEnglish}}</div>
             <hr>{{Hanzi}} · {{TonePinyin}} · {{Meaning}} {{WordAudio}}
```

**Ràng buộc kỹ thuật** ([manual — Field replacements](https://docs.ankiweb.net/templates/fields.html)):

- Tham chiếu media phải nằm *trong trường* (`[sound:file.mp3]`); không ghép được trong template từ giá trị trường.
- `{{FrontSide}}` không phát lại audio mặt trước, nên phải đặt trường audio lại ở mặt sau.
- `{{hint:}}` không giấu được audio.

**Với tiếng Nhật và tiếng Anh:**

- Lapis có sẵn chế độ `IsAudioCard`: phát audio câu, giấu từ; nếu không có audio câu thì lùi về audio từ ([Lapis](https://github.com/donkuri/lapis)).
- Thẻ xuất từ Immersion Kit đặt audio ở mặt sau, nên phải sửa template.

### Thẻ câu và cloze

**Bản thân ngữ cảnh câu không có phép màu.** Học từ trong một câu có chú giải và học theo cặp từ không khác biệt đáng kể trên 10 thước đo ([Webb 2007](https://doi.org/10.1177/1362168806072463)). Học theo bản dịch cho nhiều từ hơn, nhưng người học yếu khó chuyển sang ngữ cảnh L2 ([Prince 1996](https://doi.org/10.1111/j.1540-4781.1996.tb05468.x)). Giá trị thật của thẻ câu với người học này nằm ở: audio đời thực, collocation, ngữ dụng, và cơ hội luyện sản sinh trong ngữ cảnh.

**Cloze chưa có nghiên cứu đối đầu nghiêm túc.** Nhóm không tìm thấy nghiên cứu đối đầu nào được lặp lại giữa cloze và flashcard. Căn cứ của cloze là lý thuyết Involvement Load ([Laufer & Hulstijn 2001](https://doi.org/10.1093/applin/22.1.1)), còn các tuyên bố "cloze vượt trội" đến từ nhà bán [quảng cáo].

**Quy tắc thực hành:**

- Cloze **một** cụm duy nhất, ví dụ `{{c1::to keep someone in the loop}}`.
- Phát audio trọn câu ở mặt sau, hoặc cả mặt trước nếu muốn "cloze có audio hỗ trợ".
- Không đặt c1/c2/c3 trên cùng một câu dài: mỗi cloze thành một thẻ, khối lượng ôn nhân lên.
- Anki hỗ trợ `{{type:cloze:Text}}` để gõ đáp án và `{{tts en_US:cloze-only:Text}}` cho TTS chỉ đọc phần bị che [tài liệu chính thức].

### Thẻ gợi nhớ cụm từ theo ngữ cảnh và thẻ sản sinh

**Thiết kế thẻ biểu đạt → ngữ cảnh (dành cho N1+ và C2):**

- **Mặt trước:** một tình huống hoặc lời diễn giải, ví dụ "từ chối đề xuất một cách lịch sự nhưng vẫn để ngỏ".
- **Nhiệm vụ:** *nói to* cụm hoặc câu mục tiêu.
- **Mặt sau:** câu bản ngữ kèm audio để so.

**Bằng chứng:**

- Đây là mức gợi nhớ chủ động, mức khó nhất trong thang độ khó của [Laufer & Goldstein 2004](https://doi.org/10.1111/j.0023-8333.2004.00260.x).
- Học theo chiều sản sinh cho lợi ích lớn hơn về kiến thức sản sinh ([Webb 2009](https://doi.org/10.1177/0033688209343854)).
- Dạng recall vượt dạng recognition ở kiến thức chính tả sản sinh ([Nakata 2016](https://doi.org/10.1515/iral-2015-0022)).
- Truy xuất vượt bắt chước kiểu "repeat after me" với từ vựng ngoại ngữ ([Kang, Gollan & Pashler 2013](https://doi.org/10.3758/s13423-013-0450-z)).
- Bắt chép từ mới khi chưa nắm nghĩa lại *làm giảm* khả năng học sản sinh ([Barcroft 2006](https://doi.org/10.1191/0267658306sr276oa)). Vì vậy ô gõ chỉ nên dùng cho cụm đã quen.

**Kiểm soát khối lượng.** Chỉ 10–20% note nên có thẻ sản sinh. Cách làm: thêm trường `Produce` và tạo card type có mặt trước bọc trong `{{#Produce}}…{{/Produce}}`; Anki chỉ sinh thẻ khi trường này có nội dung [suy luận dựa trên tài liệu]. Lapis chỉ có một card type cho mỗi note, nên thẻ sản sinh riêng cần nhân bản note type.

### Thẻ đảo chiều (reverse)

**Giá trị và chi phí.** Thẻ đảo chiều có giá trị cho kiến thức sản sinh (Webb 2009). Nhưng mỗi thẻ là một thẻ đầy đủ và khó hơn; sinh cho mọi note sẽ xấp xỉ nhân đôi số lượt ôn [chưa xác minh, ước tính].

**Với tiếng Trung:** thẻ đảo nên là "nghĩa/hình → nói từ với đúng thanh, rồi nghe audio đối chiếu". Không nên là "gõ chữ Hán", trừ khi viết chữ trở thành mục tiêu — khớp với ưu tiên "chỉ viết khi thật cần". Thẻ Writing của NewHSK3 (cloze + nét chữ, cần internet) chỉ bật ở giai đoạn đó. Lưu ý thêm: người dùng phản ánh thẻ Anh → Trung của Spoonfed mơ hồ [cộng đồng] ([AnkiWeb 1271086873](https://ankiweb.net/shared/info/1271086873)).

### Thẻ thân thiện với shadowing

**Bằng chứng về shadowing:**

- Shadowing cải thiện cảm nhận âm vị; riêng nhóm trình độ thấp cải thiện cả hiểu nghe ([Hamada 2016](https://doi.org/10.1177/1362168815597504)).
- Người học nên đi từ "shadowing for listening" sang "shadowing for speaking" ([Hamada 2019](https://doi.org/10.1177/0033688218771380)).
- 8 tuần, ít nhất 4 lần/tuần, mỗi lần ít nhất 10 phút, có tự ghi âm, đã cải thiện mức dễ hiểu và độ trôi chảy, nhưng không đổi độ nặng giọng ([Foote & McDonough 2017](https://doi.org/10.1075/jslp.3.1.02foo)).

**Thiết kế:**

- **Clip:** một dòng phụ đề, 2–8 s audio; transcript giấu ở mặt trước; có nút phát lại.
- **Tách buổi:** shadowing chạy trong buổi riêng (filtered deck theo tag `shadow`), không lồng vào lúc ôn, vì ôn thẻ tối ưu cho truy xuất chứ không cho bắt chước.
- **Tự ghi âm:** AnkiDroid 2.25 cho phép template ghi âm, tiện để tự kiểm tra ([AnkiDroid 2.25 changelog](https://forums.ankiweb.net/t/ankidroid-2-25-changelog/71237)).
- **Audio chậm:** Anki không có điều khiển tốc độ phát cho từng clip. Cách làm là sinh thêm một file chậm, ví dụ `edge-tts --rate=-20%`, vào trường `SentenceAudioSlow` (tùy chọn `--rate` đã chạy được khi nhóm thử ngày 13/11/2026) ([edge-tts](https://github.com/rany2/edge-tts)).

### Câu dài

**Giữ *nhiệm vụ* của thẻ nguyên tử: một cụm mục tiêu.** Câu dài để làm ngữ cảnh ở mặt sau, hoặc cắt clip xuống mệnh đề chứa cụm mục tiêu: dùng thanh trượt khoảng thời gian của asbplayer, hoặc menu `a` của mpvacious cho câu nhiều dòng. FSRS gán một trạng thái trí nhớ cho mỗi thẻ; nếu thẻ gộp nhiều điểm chưa biết, quên bất kỳ điểm nào cũng làm hỏng cả thẻ [suy luận].

**Với Immersion Kit thì làm ngược lại.** Ở đây vấn đề là câu quá *ngắn*: phụ đề cắt nhỏ thành mảnh 1,5–3 s. Dùng endpoint `sentence_with_context` để ghép 2–3 dòng kề nhau thành một đơn vị nghe dài hơn.

### Thiết lập FSRS (Anki cuối 2026)

**Phiên bản hiện tại** ([Anki releases](https://github.com/ankitects/anki/releases); [AnkiMobile 26.10](https://forums.ankiweb.net/t/ankimobile-26-10-is-out/74202)):

- **Anki desktop:** bản ổn định mới nhất là **26.09.4** (04/11/2026). Bản beta 26.11b1 (12/11/2026) thêm `{{type:ci:}}`, nên trên 26.09.4 có thể chưa dùng được.
- **FSRS-6** (21 tham số) có từ 25.07; bản 26.09 dùng fsrs-rs 6.6.2.
- **Di động:** AnkiDroid **2.25.3** (17/10/2026), AnkiMobile **26.10** (03/11/2026).

Hướng dẫn chính thức ([manual — Deck Options](https://docs.ankiweb.net/deck-options.html)):

- Retention mặc định 90%; trên 97% thì khối lượng "can be overwhelming".
- Tối ưu khoảng mỗi tháng là đủ.
- Learning steps dưới 1 ngày ("10m or 30m are good").
- 20 thẻ mới/ngày tương đương khoảng 200 lượt ôn/ngày.
- Không bấm Hard cho câu trả lời đã quên.

| Thiết lập | ZH-HSK | JA-mined | EN-mined |
|---|---|---|---|
| Desired retention | 0,90 | 0,90; hạ xuống 0,85–0,88 nếu quá tải (kiểm bằng Help Me Decide) | Như JA |
| Learning / relearning steps | `10m 30m` (hoặc một bước `15m`) / `10m` | Như ZH | Như ZH |
| Thẻ mới/ngày | ~10 | ~10 | 5–10 |
| Optimize | Mỗi tháng, khi preset đã có vài trăm lượt ôn; bật health check | Như ZH | Như ZH |
| Bury siblings | Bật cho new, review, interday | Như ZH | Như ZH |
| Easy Days | "Reduced" vào ngày bận | Như ZH | Như ZH |

**Ghi chú vận hành:**

- **Ba preset riêng cho ba ngôn ngữ**, vì manual khuyên tách preset cho các deck có độ khó rất khác nhau. Không vượt 0,95 retention.
- **Chấm điểm trung thực:** chấm Again khi không nói ra được cụm ở thẻ sản sinh.
- **Lỗi đã biết:** một báo cáo cộng đồng cho biết simulator Help Me Decide hỏng im lặng khi preset có dưới 21 tham số sau khi nâng cấp ([forum](https://forums.ankiweb.net/t/bug-fsrs-desired-retention-simulator-expects-21-parameters-but-decks-support-less-than-that-leading-to-silent-failure/70285)).

**Quy tắc di động:**

- Add-on không chạy trên AnkiDroid/AnkiMobile. Thứ gì add-on đã ghi vào trường thì đồng bộ được: audio, furigana, HTML pitch, span màu thanh (cần CSS trong template).
- Trên iOS nên dùng **mp3**. AnkiMobile có vấn đề với Opus, và Lockdown Mode tắt Opus/AVIF ([mpvacious](https://github.com/Ajatt-Tools/mpvacious)).
- Hệ quả: audio WebM/Opus của Ankidrone có thể không phát trên iPhone nếu chưa chuyển đổi [cộng đồng; chưa thử trên V9] ([forum Ogg/AnkiMobile](https://forums.ankiweb.net/t/ogg-files-suported-in-anki-mobile/4171)).
- Audio HTML5 của HSKStory trên di động cũng chưa được xác minh.

### Anki làm được gì và không làm được gì so với luyện nói bên ngoài

**Anki làm được:**

- Liên kết hình thức – nghĩa bền vững nhờ truy xuất và giãn cách ([Karpicke & Roediger 2008](https://doi.org/10.1126/science.1152408); [Kim & Webb 2022](https://doi.org/10.1111/lang.12479)). Kim & Webb tổng hợp 98 effect size: giãn cách có hiệu ứng trung bình đến lớn; giãn đều và giãn tăng dần tương đương nhau.
- Kiến thức "từ vựng hóa", truy cập tự động ([Elgort 2011](https://doi.org/10.1111/j.1467-9922.2010.00613.x)).
- Cảm nhận thanh điệu và âm vị qua thẻ nghe-trước.
- Gợi nhớ sản sinh các cụm đã chọn.

**Anki không làm được:**

- Độ trôi chảy được "thủ tục hóa": trong bài luyện nói 4/3/2 phút, mức tăng chỉ được giữ lại ở người nói lặp lại cùng bài ([de Jong & Perfetti 2011](https://doi.org/10.1111/j.1467-9922.2010.00620.x)).
- Sản sinh có phản hồi, luân phiên lượt lời và ngữ dụng thời gian thực.
- Thay đổi độ nặng giọng.

Theo mô hình bốn mạch của Nation, flashcard chỉ thuộc mạch "language-focused learning", khoảng một phần tư thời gian học ([Nation 2007](https://doi.org/10.2167/illt039.0)).

**Nhịp luyện nói hàng tuần gợi ý [suy luận]:**

- **Tiếng Nhật:** 2 buổi gia sư × 30–60 phút về chủ đề DX (giải thích hệ thống, đàm phán tiến độ, keigo trong họp), mang theo các thẻ `Produce` của tuần. Mỗi ngày 10 phút shadowing cộng một lần kể lại 4/3/2 có ghi âm.
- **Tiếng Anh:** nói 4/3/2 cùng một chủ đề mỗi tuần. Luyện diễn giải lại một clip talk rồi đối chiếu với câu gốc; khoảng hở nào lộ ra thì thành thẻ cloze/sản sinh.
- **Tiếng Trung:** 2–3 buổi gia sư × 30 phút để được sửa thanh điệu.
- **Gia sư AI giọng nói:** cho khối lượng lớn với chi phí thấp, nhưng chất lượng sửa thanh điệu và trọng âm cao độ chưa được kiểm chứng. Nên dùng AI cho khối lượng, dùng người cho phát âm.

## Phần VI — Phán quyết cuối cùng: thứ tự cài đặt, các bước, giới hạn, phần mở rộng tối thiểu

### Tiếng Trung — xếp hạng

| Hạng | Lựa chọn | Vai trò | Link (từ ghi chú) |
|---|---|---|---|
| 1 | New HSK 3.0 Mandarin Chinese Sentence Deck, **chỉ subdeck Listening** | Lõi nghe theo danh sách 2025; audio AI | [AnkiWeb 258311532](https://ankiweb.net/shared/info/258311532) (HSK 1–4) · [GitHub v1.0](https://github.com/NewHSK3/new-hsk-3-anki-deck/releases/tag/v1.0) (HSK 5, 6, 7-8-9: 243 MB / 309 MB / 1,05 GB) |
| 2 | HSKStory "HSK 3.0 (2026)", **sau khi sửa thành thẻ nghe-trước** | Lõi từ vựng + nối âm với chữ Hán đã biết; nhập môn nhẹ nhất | [hskstory.com/anki/hsk-1](https://hskstory.com/anki/hsk-1) · [tải trực tiếp HSK1 v11](https://audio.hskstory.com/downloads/anki/hskstory-hsk1-anki-v11.apkg) · [AnkiWeb 1703580298](https://ankiweb.net/shared/info/1703580298) |
| 3 | Mandarin ear training (helq) | Luyện thanh điệu, âm đầu, vần ở giai đoạn 0; âm tiết bản ngữ | [AnkiWeb 854183352](https://ankiweb.net/shared/info/854183352) |
| 4 | Spoonfed Chinese (`spoonfed_arty` hoặc Gumroad v2) | Bổ sung giọng người, không theo HSK | [AnkiWeb 1307319045](https://ankiweb.net/shared/info/1307319045) · [Gumroad](https://promagma.gumroad.com/l/IEmpwF) |
| 5 | MaoMi Beginner→Advanced | Thay cho Spoonfed nếu muốn bản gọn, một giọng | [MaoMi](https://maomichinese.com/product/anki1/) |
| 6 | 🔥 New HSK 3.0: Ultimate | Điều kiện: một phần audio người thu, có ảnh; cần kiểm tra file, pinyin dạng từ điển | [AnkiWeb 1736976202](https://ankiweb.net/shared/info/1736976202) |
| 7 | ChineseAudioFlashcards HSK 1 | Đệm tuần đầu bằng giọng người; danh sách HSK 2.0 | [AnkiWeb 1578796058](https://ankiweb.net/shared/info/1578796058) |

**Cài trước tiên:** Anki desktop 26.09.4, bộ helq và HSKStory HSK1 (5,2 MB, tải trực tiếp, không cần AnkiWeb).

**Các bước cài đặt:**

1. **Tạo preset `ZH-HSK`** và bật FSRS với retention 0,90, steps `10m 30m`, relearning `10m`, khoảng 10 thẻ mới/ngày.
2. **Đăng nhập AnkiWeb rồi tải bộ helq.** Chạy 10–20 thẻ/ngày trong 2–4 tuần. Nếu bản desktop gặp vấn đề tự phát, README hướng dẫn tắt autoplay và dùng add-on "Replay buttons".
3. **Nhập HSKStory HSK1**, sao lưu trước (File → Create Backup).
4. **Thêm trường cho HSKStory.** Trong Manage Note Types, thêm hai trường `SentenceAudio` và `WordAudio` vào note type "HSKStory HSK n Recognition v1" (n là số cấp).
5. **Lấp hai trường mới bằng một trong hai cách:**
   - **(a) HyperTTS** (cách có tài liệu): chạy batch với nguồn `ExampleHanzi` → đích `SentenceAudio`, xoay 2–3 giọng zh-CN để mô phỏng huấn luyện biến thiên cao ([HyperTTS](https://vocab.ai/hypertts)).
   - **(b) Giữ audio gốc của HSKStory:** chép `StoryTitle` sang `SentenceAudio`, rồi dùng Find and Replace có regex trong Browser để biến `<audio src="X">…` thành `[sound:X]`; làm tương tự cho trường `Audio` → `WordAudio` [suy luận, chưa thử].
   - Bản AnkiWeb của HSKStory có bố cục trường khác (WordAudio, SentenceAudio, …) [tài liệu chính thức]; nó có dùng `[sound:]` hay không thì chưa xác minh.
6. **Tạo card type "Listen"** theo mẫu ở Phần V, rồi suspend thẻ "Recognition" (tìm trong Browser theo tên card type).
7. **Sau khi xong khoảng HSK1:** tải NewHSK3 HSK 1–4 từ AnkiWeb (235,9 MB, định dạng `.anki21b`, cần Anki đời mới). Suspend toàn bộ subdeck Reading và Writing. Trong Listening, chỉ mở HSK1 và luôn đi sau HSKStory một cấp.
8. **Tùy chọn trên desktop:** Chinese Support V4 (AnkiWeb 1240761427, bản sửa cho Anki 25.07+) để điền màu thanh vào trường. Add-on chỉ chạy trên desktop, nhưng trường đã điền vẫn đồng bộ, và màu cần CSS trong template ([Chinese Support V4](https://shigeyukey.github.io/shige-addons-wiki/chinese-support-v4.html)).
9. **Từ khoảng HSK3 (tùy chọn):** thêm Spoonfed với template audio-only, tối đa 5 câu/ngày, kèm errata. Song song, đặt 2–3 buổi gia sư mỗi tuần.

**Giới hạn:**

- Cả hai bộ lõi đều không phải giọng bản ngữ đã xác minh. NewHSK3 là AI có nhãn; HSKStory không rõ nguồn và nhiều khả năng là TTS.
- NewHSK3 rất nặng: 9 note/từ, trọn bộ khoảng 99.000 thẻ. Bản v1.0 chỉ có 1 commit và không có file license.
- Tác giả NewHSK3 cho rằng bộ hợp hơn với người đã học "at least a small amount of beginner Mandarin".
- HSKStory chỉ có một câu mỗi từ.
- Không bộ nào có bản dịch tiếng Nhật hay tiếng Việt cho danh sách 2025. Nhóm không tìm thấy deck HSK 3.0 nào bằng tiếng Trung, Nhật hay Việt có audio câu.
- Thanh điệu trong audio chưa ai nghe kiểm.

**Phần mở rộng tối thiểu.** Không deck nào đồng thời có danh sách 2025, audio câu giọng người và bản dịch tiếng Nhật/Việt. Phần mở rộng khả thi gồm bốn lớp nhỏ:

- **(1) Thẻ nghe-trước** như các bước trên.
- **(2) QA audio TTS:**
  - Lọc bằng regex các câu chứa chữ đa âm rủi ro cao: 行 长 了 得 还 重 觉 便 为 地 着 都 和 乐 数 好 少 种 差 只 调 发 干 处 当 看 教 空 假 背 薄 倒.
  - Đánh dấu thêm chuỗi từ hai thanh 3 trở lên, và các câu có 一/不.
  - Nghe 100% câu bị đánh dấu và 5–10% số còn lại [chưa xác minh — quy trình đề xuất].
  - Sửa bằng SSML của Azure, ví dụ `<phoneme alphabet="sapi" ph="ni 3 hao 3">你好</phoneme>` ([Azure phonetic sets](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-ssml-phonetic-sets)).
  - Chi phí: khoảng 3.000 câu tiếng Trung × 25 ký tự nằm gọn trong hạn mức miễn phí 0,5 triệu ký tự/tháng của Azure F0 [cộng đồng] ([MS Learn Q&A](https://learn.microsoft.com/en-us/answers/questions/1654938/text-to-speech-s0-standard-tier-0-5-million-charac)).
- **(3) Các trường "cầu nối chữ Hán":** `On'yomi`, `Hán-Việt`, và cờ `同形異義`. Tự điền từ các tài liệu học thuật: [許雪華 2014](https://da.lib.kobe-u.ac.jp/da/kernel/0100487720/0100487720.pdf) đếm hơn 12.000 từ đồng hình Nhật – Trung; [bài TNU](https://jst.tnu.edu.vn/jst/article/view/4951) lập bảng đối ứng vần Hán-Việt ↔ tiếng Trung. Ưu tiên luyện các cặp tối thiểu n/ng, l/r (người Nhật hay vấp, theo [東方書店](https://www.toho-shoten.co.jp/export/sites/default/toho/toho368-chen.pdf)), zh/ch/sh với z/c/s, ü, và thanh 2 với thanh 3.
- **(4) Tùy chọn cho kỹ sư:** tự build [RyanGibb/anki-hsk3](https://github.com/RyanGibb/anki-hsk3).
  - Nội dung: 10.999 từ theo danh sách 2025 cộng 2.038 thẻ ngữ pháp, mỗi thẻ hiện câu ví dụ chính thức từ chinesetest.cn và phát audio của câu đó [tài liệu chính thức; nguồn giọng chưa xác minh].
  - Chi phí build: tải khoảng 1,2 GB Wiktionary và khoảng 300 MB bản ghi; cần Azure key riêng cho phần thiếu audio.
- **Bản dịch tiếng Nhật có người dịch:** Tatoeba có 1.650 câu tiếng Trung kèm audio liên kết với bản dịch tiếng Nhật. Nhưng phần lớn audio có trường license trống, nghĩa là "may not reuse the audio outside the Tatoeba project" ([Tatoeba downloads](https://tatoeba.org/en/downloads)).

### Tiếng Nhật — xếp hạng

| Hạng | Lựa chọn | Vai trò | Link (từ ghi chú) |
|---|---|---|---|
| 1 | Tự đào câu: Lapis + Yomitan + asbplayer (thêm mpvacious/Memento cho file trên máy, Anki Miner cho cả mùa phim) | Lõi chính | [Lapis](https://github.com/donkuri/lapis) · [Lapis.apkg 1.7.0](https://github.com/donkuri/lapis/releases/download/1.7.0/Lapis.apkg) · [Yomitan](https://github.com/yomidevs/yomitan) · [asbplayer](https://github.com/asbplayer/asbplayer) · [mpvacious](https://github.com/Ajatt-Tools/mpvacious) · [Memento](https://github.com/ripose-jp/Memento) · [Anki Miner](https://github.com/0xzerolight/anki_miner) |
| 2 | Immersion Kit (drama) | Kho câu chính, đã kiểm tra file | [immersionkit.com](https://www.immersionkit.com/) |
| 3 | Nadeshiko | Kho câu tự phát nhất; điều kiện (chưa mở file) | [nadeshiko.co](https://nadeshiko.co/en/) · [live action](https://nadeshiko.co/en/media?category=JDRAMA) · [YouTube](https://nadeshiko.co/en/media?category=YOUTUBE) |
| 4 | Aobana Reibun | Biến danh sách cụm hoặc từ N1 thành thẻ câu thật; điều kiện | [AnkiWeb 1429349152](https://ankiweb.net/shared/info/1429349152) · [GitHub](https://github.com/Wyzmic/Aobana-Reibun) |
| 5 | Ankidrone Essentials V9 – Tango N1 | **Chỉ tham khảo / khung từ vựng phụ — không đáp ứng mục tiêu** | [Ankidrone Essentials](https://tatsumoto.neocities.org/blog/ankidrone-essentials) |
| 6 | 新完全掌握 N1 语法例句 (mxggle) | **Chỉ tham khảo / khung từ vựng phụ — không đáp ứng mục tiêu** (TTS) | [GitHub mxggle](https://github.com/mxggle/anki-jlpt-n1-grammar-example-sentences) |
| 7 | Core 2k/6k, Kaishi | **Chỉ tham khảo / khung từ vựng phụ — không đáp ứng mục tiêu**; phần lớn đã nằm trong vốn N2 | [AnkiWeb 1487314101](https://ankiweb.net/shared/info/1487314101) · [Kaishi](https://github.com/donkuri/Kaishi) |

**Cài trước tiên:** AnkiConnect, Lapis và Yomitan. Ba thứ này là bộ khung mà mọi nguồn khác đổ vào.

**Các bước cài đặt:**

1. **Cài Anki desktop 26.09.4 và add-on AnkiConnect.** AnkiConnect là bắt buộc cho asbplayer, Yomitan, nút "Add to Anki" của Immersion Kit và Anki Miner. Tạo preset `JA-mined`.
2. **Nhập `Lapis.apkg` 1.7.0** (cần Anki 23.10+). Cài AJT Japanese (AnkiWeb 1344485230) để ghi furigana và pitch NHK/Kanjium vào trường ([AJT Japanese](https://github.com/Ajatt-Tools/Japanese)).
3. **Cài Yomitan** trên Chrome/Edge. Nạp JMdict, một từ điển đơn ngữ J-J cho trình độ N1+, từ điển pitch và danh sách tần suất. Ánh xạ vào các trường Lapis.
4. **Cài extension asbplayer.**
   - Ánh xạ Sentence → `Sentence`, Audio → `SentenceAudio`, Image → `Picture`, Source/URL → `MiscInfo`.
   - **Bật "Re-encode audio as mp3".**
   - Padding gợi ý 100–250 ms đầu và 300–500 ms cuối; ảnh tối đa khoảng 640 px [suy luận].
   - Dùng luồng không hộp thoại: tạo thẻ bằng Yomitan, rồi `Ctrl+Shift+U` để "update last card". Đóng Browser của Anki trong lúc làm, vì đây là lỗi AnkiConnect đã biết ([asbplayer one-click mining](https://docs.asbplayer.dev/docs/guides/one-click-mining)).
   - Có sẵn hướng dẫn asbplayer bằng tiếng Việt ([Notion soyuz18](https://soyuz18.notion.site/Sentence-mining-from-Netflix-and-YouTube-with-asbplayer-83a03590cd8349ba81ca10340645b565)).
5. **Cài mpvacious** (mpv ≥ 0.41.0) cho file trên máy. Đặt audio mp3, hoặc Opus trong container m4a, để an toàn với AnkiMobile.
6. **Immersion Kit:** cấu hình ánh xạ trường AnkiConnect sang Lapis. Tìm với `exactMatch` trong category `drama` ([Immersion Kit API docs](https://docs.immersionkit.com/Public%20API/search/); endpoint sống hiện là `apiv2.immersionkit.com`).
7. **Aobana Reibun** (cần Anki có Qt6): chạy trên note danh sách cụm. Immersion Kit không cần key, tốc độ khoảng 1 request/2 s, tức 100 note mất khoảng 3,5 phút. Nadeshiko cần key miễn phí, hạn mức 150 request/phút và 5.000 request/tháng.
8. **Bật chế độ thẻ:** đặt cờ `IsAudioCard` cho note đào được; dùng `IsClickCard` cho câu dài.

**Giới hạn:**

- **Immersion Kit:** index đứng yên từ 01/2025; bản dịch có chỗ lệch; điều khoản dịch vụ không cấp phép cho clip. Tên file mang tag nhóm rip (`720p_HDTV_x264_AAC-DoA`), gợi ý nguồn không chính thức [suy luận]. Chỉ dùng cho học cá nhân.
- **Nadeshiko:** chưa được kiểm chứng ở mức file.
- **Đào câu trên di động hạn chế:** jidoujisho đã archive ngày 20/10/2025; iOS không có công cụ đào từ video, chỉ có Hoshi Reader cho đọc sách ([Hoshi Reader](https://github.com/Manhhao/Hoshi-Reader)).
- **Thời gian:** chi phí thật nằm ở thời gian đào, ước tính 10–30 s mỗi thẻ ở luồng không hộp thoại [chưa xác minh].
- **Hội thoại ở công ty:** chỉ ghi âm khi được đồng ý.

**Phần mở rộng tối thiểu:**

1. **Lập danh sách 150–300 cụm**, ví dụ từ ghi chú: 恐れ入りますが, 差し支えなければ, おっしゃることは分かりますが, 一理ありますね, 念のため確認させてください, 持ち帰って検討します, 前向きに検討します, 落としどころ, 要するに, 逆に言うと, ぶっちゃけ, それはそうなんですけど, 認識合わせ, 巻き取る.
2. **Chạy danh sách** qua Aobana Reibun hoặc nút "Add to Anki" của Immersion Kit, với `exactMatch`.
3. **Sửa template** để audio phát ở mặt trước. Ghép các dòng kề nhau bằng `sentence_with_context`.
4. **Cụm có 0–2 kết quả:** đào bằng asbplayer hoặc Anki Miner từ drama công sở, pháp lý, chính trị có phụ đề Nhật, và từ YouTube tin tức – bình luận có phụ đề Nhật thật. Phụ đề tự động có lỗi ASR, phải sửa tay.
5. **Tin tức, kinh tế, AI/công nghệ:** không có deck NHK thường nào. Dùng chế độ audio + transcript của Anki Miner cho podcast hoặc radio có transcript.
6. **Giữ tag ngữ vực** trên mọi thẻ.

### Tiếng Anh — xếp hạng

| Hạng | Lựa chọn | Vai trò | Link (từ ghi chú) |
|---|---|---|---|
| 1 | asbplayer + note đào câu (Netflix, YouTube, streaming, file trên máy) | Lõi chính | [GitHub](https://github.com/killergerbah/asbplayer) · [docs](https://docs.asbplayer.dev/docs/intro) |
| 2 | mpvacious / subs2srs / movies2anki trên file của bạn (TED, talk show, podcast có phụ đề) | Lõi chính cho talk và podcast | [mpvacious](https://github.com/Ajatt-Tools/mpvacious) · [subs2srs](https://subs2srs.sourceforge.net/) · [movies2anki](https://awesome.ecosyste.ms/projects/github.com%2Fkelciour%2Fmovies2anki) |
| 3 | Language Reactor (chỉ dòng Netflix) | Phụ/điều kiện: audio gốc chỉ có bằng chứng cộng đồng; export hay lỗi | [LR help](https://languagereactor.com/help/export) · [hướng dẫn export](https://forum.languagelearningwithnetflix.com/t/how-to-export-guide/19596) |
| 4 | Glassy-Gaia 13 Reasons Why S3–S4 / TED-Ed | Điều kiện: phải tự kiểm tra trước (từ $0, cần email Gumroad); có phụ đề tiếng Việt | [13 Reasons Why](https://glassygaia.gumroad.com/l/13_reasons_why) · [TED-Ed](https://glassygaia.gumroad.com/l/english_ted_ed_videos) |
| 5 | Mẫu subs2srs của Kelciour | Điều kiện: chỉ 10–15 phút đầu, phân phối riêng | [Kelciour Notion](https://kelciour.notion.site/English-3-263745ea25208026b057f019153b6378) |
| 6 | Kendra connected-speech | Phụ: kỹ năng giải mã chuỗi âm, không phải nội dung C1 | [AnkiWeb 1364160335](https://ankiweb.net/shared/info/1364160335) |
| 7 | English. C1 Words, Idioms, Phrasal Verbs. American Accent. | **Chỉ tham khảo / khung từ vựng phụ — không đáp ứng mục tiêu** | [AnkiWeb 524918335](https://ankiweb.net/shared/info/524918335) |

**Cài trước tiên:** asbplayer cùng một note type đào câu tự tạo.

**Các bước cài đặt:**

1. **Tạo preset `EN-mined`.** Tạo note type với các trường `Sentence`, `SentenceAudio`, `Picture`, `Target`, `Definition`, `Hint/Gloss`, `Source`, `Produce`. Card 1 là thẻ nghe-trước; card 2 điều kiện theo `{{#Produce}}`.
2. **Cài asbplayer.** Ánh xạ trường, **bật "Re-encode audio as mp3"**, đặt padding và cỡ ảnh như với tiếng Nhật. Mở hộp thoại xuất bằng `Ctrl+Shift+X` để chỉnh khoảng thời gian, cắt về đúng mệnh đề chứa cụm mục tiêu.
3. **Cài mpvacious** cho file video và podcast có phụ đề. Mỗi dòng xuất bằng `Ctrl+n`; câu nhiều dòng dùng menu `a`.
4. **Podcast hoặc phỏng vấn không có phụ đề:** dùng một mô hình chuyển giọng nói thành văn bản chạy cục bộ để tạo phụ đề, rồi nạp vào asbplayer hoặc mpv và soát lỗi ASR [suy luận]. gogadget mô tả đúng luồng này nhưng mới chỉ biết qua snippet [chưa xác minh] ([gogadget](https://pypi.org/project/gogadget)).
5. **Nếu đã có Language Reactor Pro:**
   - Xuất định dạng Anki với "Include Media".
   - Nhập bằng template "LLNTemplate" (AnkiWeb 1580143799), ký tự phân cách tab.
   - Chép thư mục `media` vào `collection.media`.
   - Tắt "Only new items since last export" nếu thấy thiếu mục.
   - Chỉ dùng cho dòng Netflix.
6. **Danh sách săn:** dùng Oxford Phrase List và PHaVE (150 phrasal verb tần suất cao nhất, phủ hơn 75% số lần xuất hiện trong COCA) làm checklist.

**Giới hạn:**

- Giá Pro của Language Reactor chỉ có từ nguồn đối thủ [chưa xác minh].
- Hành vi ghi audio của asbplayer trên Netflix (DRM) chưa được kiểm chứng trong phiên.
- Không có nguồn dựng sẵn nào cho họp, đàm phán, thuyết trình với audio thật.
- Hỗ trợ từ điển tiếng Anh của Yomitan chưa được kiểm tra.
- Deck media chia sẻ công khai có rủi ro bản quyền. Ví dụ, deck C1 giọng Anh 1507484008 vẫn còn trong chỉ mục tìm kiếm nhưng nay trả "missing" trên AnkiWeb.

**Phần mở rộng tối thiểu:**

- **Kho cụm mục tiêu:** lấy từ Oxford Phrase List, PHaVE và các câu nghe được ở công ty.
- **Săn trong media thật:** TED/TEDx và keynote cho tu từ thuyết trình; drama công sở/pháp lý trên Netflix cho thuyết phục, phản bác, mỉa mai; podcast phỏng vấn cho bình luận không kịch bản.
- **Fallback TTS cho cụm không có ví dụ thật:** dùng neural TTS en-US/en-GB qua HyperTTS hoặc edge-tts (edge-tts có các giọng en-GB như Libby, Ryan, Sonia). Gắn tag `tts` và loại khỏi danh sách shadowing. Đây là lối thoát cuối, không phải lõi.
- **Không phải nguồn chính:** Tatoeba có 850.274 câu tiếng Anh kèm audio, gồm hơn 190.000 câu do Charles Kelly thu âm (CC BY-NC-ND 3.0). Nhưng đó là câu ngắn, không phải lời nói đời thực ([manythings](https://www.manythings.org/sentences/audio/); [Tatoeba stats](https://tatoeba.org/en/stats/sentences_by_language)).

## Kết luận

**Nút thắt thực sự khác nhau ở ba ngôn ngữ.**

- **Tiếng Trung sơ cấp:** độ phủ đã được giải quyết, vì hai bộ khớp đến từng từ với đề cương 2025. Thứ còn thiếu là *nguồn gốc giọng nói*: thị trường đã chuyển sang audio AI nhanh hơn tốc độ có ai nghe kiểm nó. Một người học ưu tiên thanh điệu không nên tin bất kỳ deck nào thay cho tai của gia sư.
- **Tiếng Nhật N1+ và tiếng Anh C1+:** bài toán không còn là "chọn deck" mà là "chọn danh sách cụm và chọn nguồn". Đơn vị có giá trị là một danh sách biểu đạt do chính bạn viết, ghép với một kho câu có clip. Deck chỉ là sản phẩm phụ của quy trình đó.

**Hai hệ quả thực tế.** Thứ nhất, nhãn "HSK 3.0" và nhãn "N1/C1" đều không còn là tín hiệu chất lượng: con số note (11.000 hay 11.092) và độ dài câu (18 ký tự hay một dòng thoại 10 giây) mới là tín hiệu. Thứ hai, với một kỹ sư DX, lợi thế lớn nhất là tự động hóa. API của Immersion Kit, Aobana Reibun, HyperTTS/edge-tts và AnkiConnect cho phép biến "bộ thẻ" thành một pipeline tái tạo được. Khi nguồn mới xuất hiện — một drama công sở, một podcast có transcript, hay bản cập nhật danh sách HSK — chỉ cần chạy lại pipeline thay vì chờ ai đó chia sẻ deck mới.
