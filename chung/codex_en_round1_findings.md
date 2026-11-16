# Tiếng Anh: kết quả bổ sung Codex vòng 1

Ngày kiểm tra: 2026-11-13. Phạm vi: câu media có sẵn, không biến công cụ tự mining thành kết quả chính. Đã kiểm tra `chung/raw/` và `chung/ung_vien_Claude.md` trước khi mở sâu/tải; lúc kiểm tra chưa có file danh sách Claude. Không tải lại C1 American/Kendra và không gửi request HTTP trực tiếp tới AnkiWeb. Không build/gộp deck.

## Điểm cần chốt

- [đã mở file] **GLASSY-GAIA GitHub có dữ liệu thật, không chỉ trang bán hàng**: hai CSV nhập Anki được, kèm đủ audio chính và ảnh cho 123 dòng. Đặc biệt `Three tips on how to study effectively`: trung vị 17 từ, 60% dòng ≥15 từ, 30% ≥20 từ. Đây là ứng viên lõi media nhỏ đáng giữ, nhưng chưa thay được nguồn đa lĩnh vực lớn.
- [suy luận] Hạ OALD/Close-up C2 xuống lớp từ mục tiêu/sắc thái là đúng với yêu cầu câu đời thật. Một bộ Oxford lớn không tự cung cấp diễn ngôn, mạch kể chuyện, tương tác hay nguồn phát ngôn.
- [đã mở file] **VideoAnki có deck premade thật và preview clip chứa audio**, nhưng hai deck tự ghi Advanced có trung vị preview chỉ 8–9 từ. Có nhiều mảnh phụ đề cần nối câu; không lấy nhãn Advanced làm bằng chứng câu dài/C1. Download gói đầy đủ yêu cầu tài khoản miễn phí; chưa tạo tài khoản.
- [cộng đồng] Có **DUO 560 câu / 559 audio**, khác bộ Duo3.0 Tango 2.569 từ không audio. Chưa mở file, chưa biết audio tiếng Anh hay Nhật nên chưa thể loại cả họ DUO vì nhầm bản từ vựng; cũng không đưa DUO làm lõi media đời thật.

## 1. GLASSY-GAIA: hai kho CSV + media đã mở

Nguồn tải: [GitHub repository](https://github.com/GLASSY-GAIA/youtube-ted-ed-anki-english-en). Bản lưu: `chung/raw/codex-en-glassygaia-teded/repository.zip`, dữ liệu giải nén trong `repo/`. [đã mở file] Repo có 2 CSV; phần lớn thư mục video khác chỉ chứa placeholder hoặc ảnh minh họa, **không được đếm như đã có toàn bộ 28 deck**. Tree có tổng 232 MP3, 123 WAV, 123 JPG; các MP3 và WAV có vai trò khác nhau.

| Bộ con | Dòng CSV | Trung vị từ | ≥15 từ | ≥20 từ | Audio câu chính tồn tại | Dịch Việt | Ảnh |
|---|---:|---:|---:|---:|---:|---:|---:|
| Eight traits of successful people | 83 | 13 | 37/83 (44,6%) | 20/83 (24,1%) | 83/83 WAV | 78/83 | 83/83 |
| Three tips on how to study effectively | 40 | 17 | 24/40 (60%) | 12/40 (30%) | 40/40 WAV | 40/40 | 40/40 |

[đã mở file] Đếm từ trên `English` sau bỏ HTML, giải mã entity; số và từ có apostrophe tính một từ, từ ghép có gạch nối tách phần. Min–max lần lượt 5–64 và 6–31 từ. Trung vị thời lượng WAV chính: 4,272 giây và 6,932 giây. Không có tham chiếu sound bị thiếu trong cả hai CSV, kể cả audio ví dụ thêm. Ffmpeg decode thành công cả 123 WAV chính; không tương đương đã nghe/QA alignment 123 câu. Dấu câu kết thúc sau khi bỏ dấu ngoặc kép đóng: 0/83 và 0/40 thiếu `.?!`; đây chỉ là kiểm tra hình thức, chưa phải duyệt ngữ pháp/độc lập ngữ cảnh toàn bộ. Số liệu theo dòng và SHA256 CSV nằm ở `chung/raw/codex-en-glassygaia-teded/inspection.json`.

[đã mở file] Mỗi CSV có 38 trường: `English`, `Image`, `Audio`, `Type`, `Word_1..4`, `Word_Example_1..4`, 21 trường bản dịch/ngôn ngữ, `Word_Example_1_Audio..4_Audio`, `Tag`. `Type` ở đây chứa câu để gõ lại, không phải note type Anki. **Không có .apkg hoặc template HTML/CSS import sẵn trong repo**; cần nhập CSV đúng mapping và thiết kế template ở vòng build sau. Chưa kiểm nghiệm tương thích UI của gói AnkiWeb dựa trên repo.

[đã mở file] Audio trong `Audio` là WAV đặt trong `media-original-audio`; audio các `Word_Example_*` là MP3 tên `hypertts-...`, nằm trong `media-added-audio`. Vì vậy không được gọi tất cả 355 audio là người thật, hoặc lấy số audio tổng để suy ra số câu chính. [suy luận] Tên file/thư mục và khớp transcript hỗ trợ nguồn audio chính từ video; chưa nghe/so sánh tín hiệu với video gốc toàn bộ nên không tuyên bố đã xác minh giọng người thật từng clip. MP3 HyperTTS chưa xác định engine/voice cụ thể; không đủ cơ sở gọi neural hay TTS cũ.

[tài liệu chính thức] Nguồn Three tips là [TED-Ed chính thức](https://www.ted.com/talks/ted_ed_3_tips_on_how_to_study_effectively?view=transcript), tháng 10/2023, người dẫn Addison Anderson. Transcript chính thức khớp các câu đầu trong CSV. Nguồn Eight traits có [bài chính thức TED-Ed / Richard St. John](https://ed.ted.com/lessons/richard-st-john-8-traits-of-successful-people), dài khoảng 7 phút. [đã mở file] CSV giữ thứ tự và tag tên video, có ảnh cảnh, nhưng không có URL/timestamp riêng từng note: bối cảnh theo bài tốt hơn từ điển, truy vết từng đoạn còn cần bổ sung.

[đã mở file] 3 note thật từ [CSV Three tips](https://github.com/GLASSY-GAIA/youtube-ted-ed-anki-english-en/blob/main/youtube-three_tips_on_how_to_study_effectively-anki-english-en/youtube-three_tips_on_how_to_study_effectively-anki-english-en.csv), đánh số dòng dữ liệu bắt đầu 1; trích chọn câu ngắn để tổng trích dẫn từ tài liệu CSV này chỉ 21 từ (không đại diện trung vị 17):

1. Dòng 15: “And the process doesn’t end there.”
2. Dòng 27: “Our second technique builds on the first.”
3. Dòng 36: “This brings us back to our medical residents.”

[đã mở file] Ba note thật từ [CSV Eight traits](https://github.com/GLASSY-GAIA/youtube-ted-ed-anki-english-en/blob/main/youtube-eight_traits_of_successful_people-anki-english-en/youtube-eight_traits_of_successful_people-anki-english-en.csv) (16 từ tổng từ tài liệu CSV này): dòng 42 “I said, "Well, why not?"”; dòng 79 “Why did I pick these?”; dòng 3 “I couldn't pass the height requirement.” Đây là các câu ngắn có trong corpus, không dùng chúng để chứng minh câu dài. Các dòng ≥20 từ có sẵn như dòng 9, 10, 14, 24… và đã tính từ toàn bộ CSV.

[đã mở file] Bản dịch chưa sạch đồng đều: một số ô tiếng Hà Lan của Eight traits có chuỗi sai nghĩa rõ so với câu Anh; 5/83 ô Việt trống. [suy luận] Không nên bật mọi ngôn ngữ mặc định hay coi 21 cột dịch là 21 bản dịch đạt chuẩn. Cần duyệt riêng bản Việt và giữ bản Anh/audio gốc là chuẩn.

[tài liệu chính thức] Commit cuối repo tại thời điểm kiểm tra: 2025-10-31T18:01:54Z (GitHub API). License repo GPL-2.0 **không chứng minh license của video/audio TED**. Vai trò đề xuất: Three tips làm **lõi media nhỏ có điều kiện**; Eight traits **phụ diễn thuyết/kể chuyện**. Nhu cầu sửa: template nghe trước, thêm URL/video/timestamp, chỉ hiển thị dịch đã QA, phân biệt audio gốc với ví dụ TTS, cân nhắc WAV→MP3 cho dung lượng. Không cần gắn mọi câu vào Oxford mới học được.

## 2. VideoAnki: preview đã mở, gói đầy đủ chưa tải

[quảng cáo] [Thư viện tiếng Anh](https://www.videoanki.app/decks/?lang=en) có 5 deck free: vlog Cornwall 354 cards, Maangchi 134, Townsends 193, The Moth 208, Tom Scott 276. Trang ghi clip từ video gốc, transcript và bản dịch được review; đó là tuyên bố nhà cung cấp, chưa thay cho đo file. Có sẵn dịch Pháp/Đức/Bồ/Tây Ban Nha; chưa thấy Việt.

| Deck | Nguồn/lĩnh vực | Số card nhà cung cấp | Preview đo được | Dấu hiệu chia đoạn | Vai trò |
|---|---|---:|---|---|---|
| [Tom Scott: Model railway](https://www.videoanki.app/decks/model-railway-english-explainer/) | kỹ thuật, đường sắt, giải thích + trao đổi | 276 | 8 target, trung vị 8 từ, 4–9 từ | 6/8 không kết thúc `.?!`, nhiều dấu phẩy/đoạn chưa xong | phụ kỹ thuật, nghe khẩu ngữ |
| [The Moth: Grandmother’s cake](https://www.videoanki.app/decks/grandmothers-cake-english-story/) | kể chuyện, gia đình, ẩm thực, văn hóa Mỹ | 208 | 8 target, trung vị 9 từ, 4–15 từ | 3/8 không kết thúc `.?!`; có đoạn nối từ câu trước | phụ kể chuyện |

[đã mở file] HTML public nhúng JSON `front_tmpl`, `back_tmpl`, `cards`; mỗi preview card có `video`, `target`, `native`, `translit`. Đã lưu public page, JSON và một clip WEBM mỗi deck ở `chung/raw/codex-en-videoanki-*/`. Ffmpeg decode cả hai clip thành công, xác nhận video VP8 và audio Opus 48kHz stereo thực tồn tại; clip đầu Tom Scott 1,72 giây, The Moth 3,14 giây. Chưa nghe/QA alignment lời–âm từng câu; chưa xác minh toàn bộ 276/208 card có media.

[đã mở file] Mẫu thật, trích đoạn rõ ràng để tránh vượt giới hạn trích dẫn; không phải câu tự tạo:

- Tom Scott preview target 2: “The blue levers”; target 6: “Okay, so that one,”; target 8: “but in my head,”.
- The Moth target 2: “I resent the implication.”; target 4: “But me, I wanted”; target 6: “Betty Crocker's Super Moist.”.

[đã mở file] Nút Download free anonymous thực tế mở sign-up modal, ghi cần account miễn phí. Chưa tải .apkg nên **không có median/coverage toàn deck, note type thực, phiên bản Anki, khả năng chạy offline hay lỗi iOS**. HTML preview không cho suy ra các chỉ số đó. Trang không nêu ngày cập nhật deck. [suy luận] Trước khi làm lõi cần gộp fragment thành đơn vị câu dài, giữ source video/timestamp và ngữ cảnh lân cận. Đây là sửa segmentation của premade có sẵn; không phải đề xuất bắt anh tự mining từ đầu.

## 3. Các đầu mối đã kiểm tra, không mặc định đạt

| Đầu mối | Bằng chứng hiện có | Quyết định |
|---|---|---|
| [GLASSY-GAIA TED-Ed part 4, AnkiWeb 210221519](https://ankiweb.net/shared/info/210221519) | [cộng đồng] trang index 367 notes, 1.335 audio, 367 ảnh; 2025-10-24; cột Việt, English/Type, cụm và ví dụ; câu khoa học dài | rất đáng tải tiếp; root điều phối AnkiWeb, child chưa mở .apkg |
| [Socialge TED-ED Việt part 3, 866780035](https://ankiweb.net/shared/info/866780035) | [cộng đồng] 871 notes, 1.257 audio, 556 ảnh; 2023-08-24; mẫu có câu đầy đủ dài; Eng và Cloze tách trường | đáng tải đo tiếp; không lấy audio tổng làm coverage. [Trang tác giả](https://socialge.wordpress.com/2023/03/24/tai-nguyen-anki-ted-ed-song-ngu-anh-viet-part-1-remake-ver/) |
| [Socialge part 1, 1918837902](https://ankiweb.net/shared/info/1918837902) | [cộng đồng] 2.061 notes, 1.029 audio, 1.043 ảnh; 2023-08-24; Eng chứa cloze | có thể bổ trợ; note nhiều hơn audio nên cần kiểm audio câu từng note, không coi toàn bộ phủ audio |
| [BBC English Plus 1870416180](https://ankiweb.net/shared/info/1870416180) | [cộng đồng] 676 notes, 675 audio, 2018-03-31; mẫu elementary, dịch Bồ; là giáo trình BBC English Plus, không phải kho BBC news/talk | loại khỏi lõi C1 câu dài, không tốn lượt tải |
| [VOA+Basic English mirror](https://anki-decks.com/anki-decks/english/voabasic-english/) → 1811976951 | [cộng đồng] 1.799 notes/audio, 104 ảnh, index cũ 2019-12-03 | chưa thấy field/sample; không được gọi corpus tin tức dài chỉ vì tên VOA |
| [Friends Season 01 Episode 02 mirror](https://anki-decks.com/anki-decks/english/friends-season-01-episode-02/) → 909668546 | [cộng đồng] 366 notes/audio/ảnh; 2019-10-27 từ index | phụ sitcom có triển vọng; chưa đo độ dài/fragment/audio nguyên câu |
| [Business English Idioms 408812392](https://ankiweb.net/shared/info/408812392) | [cộng đồng] 505 notes, 1.511 audio, 2023-01-05; có Idiom/Definition/Example và ba Sound fields | phụ idiom, chưa chứng minh hội thoại thật hoặc giọng người; không là lõi media |
| [DUO sentence sound mirror](https://anki-decks.com/zh-hans/anki-decks/english/duo30-ver/) → 1973703622 | [cộng đồng] 560 notes/559 audio; tiếng Nhật tên deck không xác định được tiếng audio; cộng đồng Nhật dẫn [đúng ID](https://lavender.5ch.io/test/read.cgi/english/1667462453) | phụ cần mở file; không đánh đồng với Tango |
| [Duo3.0 Tango mirror](https://anki-decks.com/anki-decks/english/duo30-tango/) → 226773917 | [cộng đồng] 2.569 notes, 0 audio | loại khỏi tiêu chí audio câu; khác bản 560 câu |
| [DUO TSV cộng đồng Nhật](https://kitsune-no-yomeiri.hatenadiary.jp/entry/2018/10/28/001843) | [cộng đồng] bài 2018 cung cấp text/TSV, hướng dẫn cắt CD thành 560 MP3 | không phải gói audio hoàn chỉnh; chỉ ghi nhận nguồn văn bản, không làm kết quả chính |

[chưa xác minh] Search còn thấy `Englishpod with audios` 364 notes, 2025-07-26 trên index AnkiWeb, chưa tìm được ID/trang gói để xác định là câu hay toàn episode. Không nâng thành đề xuất vì có chữ podcast. Không tìm được gói BBC/VOA C1 dựng sẵn đáp ứng rõ hơn các corpus TED đã mở trong lượt này; điều đó không đồng nghĩa không tồn tại.

## 4. Ghép vai trò nội dung, chưa build

[suy luận] Lõi hợp yêu cầu nên là các nhóm media song song: TED/TED-Ed cho khoa học và lập luận; The Moth cho kể chuyện gia đình/xã hội; Tom Scott cho giải thích kỹ thuật; sitcom cho thoại đời thường. Không gọi một video đường sắt là đa lĩnh vực, cũng không lấy diễn thuyết động lực đại diện mọi dạng C1. Những corpus nhỏ đã xác minh đủ để bắt đầu một nhánh media, không đủ kết luận đã tìm được bộ lõi bao phủ toàn bộ nhu cầu.

[suy luận] Giữ tag nguồn và deck con theo bài/chương trình, chỉ thống nhất schema nghe trước; từ mục tiêu có thể liên kết tới OALD/C2 như lớp giải nghĩa. Trùng chủ đề học tập giữa Three tips và Eight traits ít trùng câu; không nên deduplicate chỉ theo từ vựng. Nếu nhập cả CSV GitHub và gói GLASSY-GAIA AnkiWeb, cần so English chuẩn hóa + nguồn để tránh trùng 123 dòng hiện có. Media gốc và ví dụ HyperTTS là hai trường khác nhau.

Câu hỏi gửi Claude: đã tải gói TED-Ed của Socialge/GG hay mới xem quảng cáo? Nếu đã, xin median trên Eng gốc, coverage audio đúng câu, và tỷ lệ fragment; có nên giữ riêng note cloze từ vựng với note nghe nguyên câu thay vì gộp mọi note cùng một chỉ số?
