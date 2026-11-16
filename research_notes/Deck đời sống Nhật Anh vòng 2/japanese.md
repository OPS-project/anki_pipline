# Japanese, round 2: real-life, advanced, long sentences with full-sentence audio (state as of 2026-11-13)

**Learner frame:** Vietnamese IT engineer in Japan, N2 → N1 and beyond. The goal is to understand real Japanese across daily life, relationships, emotion and humor, news, TV and reality shows, commentary, speeches and the workplace. The ideal card is a target expression, a long natural sentence, audio of the whole sentence, context, and a translation.

**Evidence labels:** [đã mở file] = I downloaded and parsed the .apkg. [tài liệu chính thức] = the deck's own page or the AnkiWeb API. [cộng đồng] = reviews, forums, catalogue sheets. [quảng cáo] = seller claims. [chưa xác minh] = not checked. [suy luận] = my inference.

**Units:**
- Sentence length = characters of the sentence field after removing HTML, `[sound:]`, furigana brackets/`<rt>`, whitespace and Unicode direction marks. Punctuation is counted.
- For subtitle decks marked "cleaned", full-width speaker labels such as （ミドリ） were also removed.
- "Audio coverage" = notes whose sentence-audio field points to a file that exists in the media map. Durations come from MP3 headers on a random sample of 80 files.
- I could not listen to any audio. Voice type is inferred from metadata only.

**Tooling note (important for the next round):** The logged-in AnkiWeb session worked, but the **search endpoint (`list-decks`) went into permanent HTTP 429** after my first 10 queries plus "shadowing" and "Japanese conversation". It stayed blocked for over 40 minutes. Another process on the same IP was running `aw_batch_search.py` at the time. `info` and `download` kept working, and the session never expired (no 403 or login redirect). So I discovered AnkiWeb decks through site-restricted web search, then called `info`/`download` on them. Some AnkiWeb decks may still be unseen.

---

## 1. Top findings & shortlist

### Takeaway
No single deck gives "advanced + long + natural + full-sentence native audio + translation". The best result comes from combining three kinds of deck I downloaded and inspected:

1. **Audiobook-to-SRS decks** from the community *Subs2SRS Japanese Deck Catalogue*:
   - *世界のニュースを日本人は何も知らない*: median **50 chars**, **80 % ≥30 chars**, 100 % narrated audio, about 11 s per clip.
   - *日本の教養365*: median 42 chars.

   These are the only decks found where long, real published Japanese sentences each come with their own audio clip. They are Japanese-only, with no translation and no target word.
2. **Live-action subs2srs decks**:
   - **Love is Blind Japan (JP-EN)**: spontaneous adult relationship talk, with a listening-first template.
   - **Hanzawa Naoki (JP-EN)**: workplace and banking rhetoric.
   - **TEDxSapporo (JP only)**: talks and presentations.

   All have native audio on 100 % of lines plus screenshots. Their lines are **short subtitle chunks** (median 15–22 chars), so they need line-merging to become "long sentences".
3. **Dictionaries of Japanese Grammar — Sentences (w/audio)**, AnkiWeb 843402109:
   - The only AnkiWeb deck found with **many long, expressive sentences plus English plus audio on every note**. The Advanced subdeck has 2,289 notes, median 31 chars, 57 % ≥30.
   - The audio is a **mix of TTS engines** (Naver Clova, Azure, Amazon, Vocalware), not native recordings.

The known lead "Miku Real Japanese Shadowing" (252860248) turned out to be **beginner level** (Level 1, N5–N4 grammar, median 14 chars). It is not suitable.

### Shortlist (scores /100: sentence audio 25 · naturalness & richness 20 · level fit 15 · speaking-useful 15 · coverage/progression 10 · accuracy/maintenance 10 · extras 5)

| # | Deck | Role | Score | Why | Merge notes / fixes |
|---|---|---|---|---|---|
| 1 | **Love is Blind Japan JP-EN** (subs2srs, Mediafire) | Core real-life (relationships, emotion, small talk) + listening/shadowing | **~74 ±8** (audio 21, natural 18, level 9, speaking 12, coverage 5, accuracy 5, extras 4) | 8,064 native clips at 100 %, screenshots, English. The front template hides the text, so it is already a **listening-first card**. Real unscripted adult talk: hedging, reactions, opinions about partners and work | Merge consecutive lines (SequenceMarker/timestamps) into utterances. Move speaker labels into a Speaker field. Remove duplicated CC lines. EN is Netflix subtitle English (loose), so add a VI/EN machine translation flagged as machine. Same genre as Codex's Terrace House ep1 deck: pick one show first |
| 2 | **世界のニュースを日本人は何も知らない** (audiobook-to-SRS, Mediafire) | Core for news/current affairs/commentary listening; long-sentence shadowing | **~70 ±8** (audio 22, natural 16, level 14, speaking 7, coverage 4, accuracy 6, extras 1) | 1,941 sentences. **Median 50 chars, 79.8 % ≥30.** Median clip 10.8 s. Alignment check is tight (3.3–5.4 chars/s for 80 % of clips). Topics: international politics, education, immigration, business, culture | No translation and no target word. Add an LLM translation (VI) and a frequency-based target word. Filter about 5 % headings and lists. Change the front to audio-first. Whether the narrator is human or AI is not stated: [chưa xác minh] |
| 3 | **Dictionaries of Japanese Grammar — Sentences (w/audio)**, [843402109](https://ankiweb.net/shared/info/843402109) | Core for long, expressive, formal and written sentences with translation | **~69 ±7** (audio 16, natural 11, level 13, speaking 9, coverage 9, accuracy 7, extras 4) | 5,279 sentences from Makino & Tsutsui (Basic, Intermediate, Advanced), each with a grammar point, explanation and English. Audio on 100 % of notes. Advanced: median 31, 56.7 % ≥30 | TTS is mixed (Naver Clova 2,042 / Azure 1,528 / Amazon 846 / Vocalware 629 / Naver 368 files). Regenerate with **one neural voice**. Fix 389 sentences with `・`/`{…}` alternatives and 30 A/B dialogues (2 voices needed). Maintainer stopped updates in Dec 2024 but published errata. Overlaps grammar points with mxggle N1 / Shin Kanzen decks |
| 4 | **TEDxSapporo** (subs2srs, Mediafire) | Supplementary: speeches, presentations, opinion rhetoric | **~68 ±8** (audio 21, natural 15, level 10, speaking 11, coverage 4, accuracy 4, extras 3) | 10 talks, 3,419 native clips (100 %). Many presentation moves: こう言ったら誤解を受けるかもしれないんですけども…, それぐらい変化って激しいんだ | **No translation** (Meaning field empty). Median 19 chars, so merge lines. Talk title is available in tags and subdecks, so it can serve as context. 2016 one-off upload |
| 5 | **Hanzawa Naoki JP-EN** (subs2srs, Mediafire) | Supplementary: workplace, finance, confrontation keigo | **~67 ±8** (audio 21, natural 14, level 8, speaking 10, coverage 5, accuracy 6, extras 3) | 7,550 native clips (100 %), English, screenshots. Banking and business vocabulary (再建案, 金融庁検査, 議事録) and authoritative register (下がりたまえ, 申し開きは以上です) | Very short lines (median 15, 1.7 % ≥30), so merging is essential. Subtitle symbols (☎, ≪, ➡) and 364 notes tagged `duplicate` need cleaning. The register is theatrical, so do not copy it in real meetings |
| 6 | **日本の教養365** (audiobook-to-SRS, Mediafire) | Supplementary: cultural literacy, explanatory written register | **~61 ±8** (audio 20, natural 12, level 12, speaking 4, coverage 7, accuracy 5, extras 1) | 11,341 sentences, median 42, 70.6 % ≥30, median clip 10.4 s. Japanese history, religion, arts, literature, science | Very encyclopedic (names, dates), so it is less "real life". About 15–20 % are fragments or headings ("1．", "豆 知 識1．"), visible as clips under 2 chars/s, so filter by length ≥15. No translation |
| — | **Immersion Kit / Nadeshiko** (known from round 1) | Generator for target-word cards with real clips | (round 1: ~76 / ~79) | Not re-inspected. Use them with Aobana Reibun to attach real clips to N1 target lists | — |
| — | NativShark "4,217 Japanese Sentences w/ Audio", [126242908](https://ankiweb.net/shared/info/126242908) | Optional warm-up for casual spoken forms only | **~63 ±8** (audio 22, natural 10, level 4, speaking 11, coverage 7, accuracy 6, extras 3) | Human male + female audio, but **median 11 chars**, only 3.2 % ≥30. Beginner to intermediate | Female audio is missing in 15.4 % of notes. Not worth importing for an N2→N1 learner, except to drill casual contractions |

### Inferences
- [suy luận] **For "long sentence + real audio", audiobooks are the only ready-made source.** Subtitle-based decks (drama, reality, TED) always cut speech into 1–4 s chunks. They become "long sentences" only after merging adjacent lines. Each subs2srs note has an episode-and-timestamp SequenceMarker, so merging can be scripted: group lines with a gap under about 0.7 s in the same episode, then concatenate the MP3s.
- [suy luận] A practical stack for this learner:
  - **Love is Blind** (or Terrace House) for spoken interaction.
  - **世界のニュース** for news and commentary listening at full sentence length.
  - **DJG Advanced** for formal and written structures with English.
  - Immersion Kit/Nadeshiko via Aobana Reibun to fill N1 target words with real clips.

  Hanzawa, TEDx and 日本の教養 are optional domain add-ons.
- [suy luận] Translation is the biggest shared gap. Only DJG (book English), Love is Blind and Hanzawa (subtitle English) have one. A Vietnamese machine-translation field should be added to every deck and labeled as machine output.

### Gaps
- The AnkiWeb search block means I could not run the planned Chinese, Vietnamese and Japanese-title query sets: 日语, 日剧, 听力, 口语, 敬語, 慣用句, オノマトペ, ことわざ, tiếng Nhật, JapanesePod101, Glossika, Assimil, Satori. Web search with `site:ankiweb.net` partly covered them.
- **Glossika Japanese Fluency 1–3 (pdf + mp3)** exists on AnkiWeb (each about 1,000 notes / 2,000 audio, updated 2026-04-07 per search snippet), but I could not get the IDs. [chưa xác minh]
- I found no expression deck (慣用句/ことわざ/四字熟語/敬語) that has **long** example sentences with sentence audio. Expression decks exist only with word audio or no audio (see Rejected).
- Narrator identity for the audiobook decks is unknown. The catalogue marks one other audiobook deck "(Neural AI Voice)", which suggests unmarked ones are original audiobooks. [suy luận, chưa xác minh]
- Codex's NHK news lead (forum.freemdict "NHKニュース听力623篇", AnkiWeb 620593953 / 1192131968 / 1123167619 unavailable) stays unverified.

---

## 2. Candidate table

| Deck | Link / ID | Domains (random sample, my classification) | Median sentence length | % ≥30 chars | Sentence audio (type + coverage) | Context fields | Translation | Notes | Updated | Evidence | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 世界のニュースを日本人は何も知らない (audiobook) | [Mediafire](https://www.mediafire.com/file_premium/yvbfe9ylj3de33z/) via [catalogue](https://docs.google.com/spreadsheets/d/15ELElkomfixdS4-dNrpxrNl14mlJUZrdD0h7N6iEE2k/htmlview) | Intl. politics/society 10, education 6, immigration/nationality 4, business 4, culture 4, headings 2 (n=30) | **50** | **79.8 %** | Audiobook narration, 1,941/1,941 (100 %), median 10.8 s, 44.1 kHz | Book cover image only; sequence number in filename | None | 1,941 notes. Front = text, back = audio | Package 2024-04-24 | [đã mở file] | **Core (news/commentary)** |
| 日本の教養365 (audiobook) | [Mediafire](https://www.mediafire.com/file_premium/8zmlbuw5l8bejey/) via catalogue | History 14, religion/shrines 5, arts/literature 6, science 2, headings 3 (n=30) | 42 | 70.6 % | Audiobook narration, 11,341/11,341, median 10.4 s, 22 kHz/64 kbps | Cover image | None | ~15–20 % headings/fragments | 2024-04-26 | [đã mở file] | Supplementary |
| Love is Blind Japan JP-EN | [Mediafire](https://www.mediafire.com/file/7gizhqvujil1u28/Love_is_Blind_Japan_JP-EN.apkg/file) via catalogue | Relationships/dating 14, daily small talk 15, emotion/reaction 6, work/career 3, humor 2 (n=40) | raw 22 / cleaned **17** | raw 27.1 % / cleaned **15.0 %** | Native TV clip, 8,064/8,064, median 3.0 s | Screenshot, episode ID + timestamp, speaker names in text | EN (Netflix subs) | Listening-first front; 11 episodes | 2022-05-24 | [đã mở file] | **Core (real-life spoken)** |
| TEDxSapporo | [Mediafire](https://www.mediafire.com/file/qd36sd1mtq8dmby/TEDxSapporo.apkg/file) via catalogue | Science/tech 9, personal narrative 9, opinion/rhetoric 8, work/education 4 (n=30) | 19 | 15.4 % | Native talk clip, 3,419/3,419, median 3.1 s | Screenshot, talk title (subdeck + tag), timestamp | **None** | 10 talks | 2016-08 | [đã mở file] | Supplementary (speech) |
| Hanzawa Naoki JP-EN | [Mediafire](https://www.mediafire.com/file/rngx63thceds4xi/Hanzawa_Naoki.apkg/file) via catalogue | Workplace/banking 22, conflict/rhetoric 10, family 5, misc 3 (n=40) | cleaned 15 | 1.7 % | Native drama clip, 7,550/7,550, median 3.0 s | Screenshot, episode + timestamp | EN | Subtitle symbols; 364 `duplicate` tags | 2015–2020 | [đã mở file] | Supplementary (workplace) |
| DJG Sentences (w/audio) | [843402109](https://ankiweb.net/shared/info/843402109) | Daily life 14, society/opinion 7, business/economy news-style 4, narrative 3, work/IT 2 (n=30) | 25 (Adv 31 / Int 24 / Basic 19) | 35.5 % (Adv **56.7 %**) | **Mixed TTS** (Naver Clova, Azure, Amazon, Vocalware), 5,278/5,279 | Grammar point, explanation, level, page | EN | Recognition card only. Errata list | Notes to 2024-08; AnkiWeb 2024-12-29 | [đã mở file] + [tài liệu chính thức] | **Core (long formal sentences)** |
| NativShark 4,217 Sentences | [126242908](https://ankiweb.net/shared/info/126242908) | Casual daily conversation ~20/30 | 11 | 3.2 % | Human M 100 % / F 84.6 % | Word breakdown, note, lesson link (dead domain) | EN + literal | Beginner–intermediate | 2017 (AnkiWeb 2024-03-12) | [đã mở file] | Optional only |
| Miku Real Japanese Shadowing | [252860248](https://ankiweb.net/shared/info/252860248) | Beginner daily conversation | 14 (Grammar notes) | 1.6 % | Native YouTube audio, 100 % on 451 grammar + 30 dialogues (median 19 s) | YouTube link, grammar point | EN | Level 1 (N5–N4) | 2024-02-25 | [đã mở file] | Reject (level) |
| Natural Adult Japanese: Friendship, Boundaries… | [1810272637](https://ankiweb.net/shared/info/1810272637) | Social talk, invitations, boundaries | JP-only text 16 | 22.6 % | **None** | Category, notes | EN | Note type "Codex Adult Japanese Basic", so likely AI-generated | 2026-05-10 | [đã mở file] | Reject (no audio, phrase-level) |
| Terrace House Tokyo 2020 ep1 (Codex) | [japanese-like-a-breeze](https://japanese-like-a-breeze.com/decks/) | Reality, social | 18 (13 without names) | 13/791 | TV clip, 791/791 | Screenshot, Sequence Marker | **None** | Codex inspected it | Upload 2019 | [đã mở file] by Codex | Same genre as Love is Blind; cite only |
| Terrace House Tokyo 2019-2020 E1-19 w/ Eng Subs | [Mediafire](https://www.mediafire.com/file/7bl7ufafy8t5j1a/Terrace_House-2019-2020_E1-19_w_Eng_Subs.apkg/file) | Reality | — | — | Live link, 1.18 GB (HEAD) | — | EN (title) | Not downloaded (near the 1.2 GB cap) | — | [cộng đồng] catalogue + HEAD | Alternative to Love is Blind |

---

## 3. Per-deck details with real samples

Samples are verbatim from the parsed collections. Whitespace is collapsed; HTML is kept where present.

### 3.1 世界のニュースを日本人は何も知らない (audiobook-to-SRS) [đã mở file]
- **Source:** Subs2SRS Japanese Deck Catalogue (Google Sheet `15ELElkomfixdS4…`, tab "Where to Find Decks", MISCELLANEOUS → "Book: Sekai no News wo Nihonjin wa Nanimo Shiranai").
  - Mediafire link live on 2026-11-13 (HEAD 200, 355,839,922 bytes).
  - Downloaded to `chung/raw/ja-subs2srs-audiobook-sekai-no-news/`.
- **Structure:** 1,941 notes / 1,941 cards. Note type "audiobook to srs". Fields: Audio, Image, Sentence.
  - Single template: front `{{Sentence}}`, back `{{Audio}}` + `{{Image}}`. Reading-first, so it needs a listening-first template.
- **Audio:**
  - 100 % present. Median 10.83 s (min 2.82, max 25.70).
  - MP3 44.1 kHz stereo 128 kbps, re-encoded with Lavf60.16.100.
  - ID3 tags carry the book title, author 谷本 真由美 and the publisher blurb. No narrator credit.
- **Alignment check:** chars/s median 4.57, p10 3.33, p90 5.41. Only 1 % of clips are under 2 chars/s, and those are headings ("ドイツ人、実は……欧州一スケベ"). [suy luận] Segmentation looks consistent. A shifted-by-one error would not show up in this test.
- **Voice type:** audiobook narration. [chưa xác minh] Human vs AI is unknown.
- **Sentence source:** a published non-fiction book (author is a former UN agency staff member, per bunshun/agora reviews). Written but conversational commentary register.
- **Samples:**
  - `Audio: [sound:世界のニュースを日本人は何も知らない-663.mp3] | Image: <img src="世界のニュースを日本人は何も知らない.jpg"> | Sentence: 自国では医療制度が崩壊しているので、どうしても海外で治療を受けさせたかったのです。`
  - `Audio: [sound:世界のニュースを日本人は何も知らない-808.mp3] | Sentence: 一九九九年まで血統主義を守ってきたドイツでは、両親ともドイツ人ではない外国人労働者とその子どもには、たとえ何年住んでいても国籍は与えられませんでした。`
  - `Audio: [sound:世界のニュースを日本人は何も知らない-1333.mp3] | Sentence: また非認知能力が高い少年少女は、自己管理能力が育まれているので勉強でも高い成果を上げられるだけでなく、反社会的な行動や犯罪に走ったり、一〇代で望まない妊娠をしてしまったりする率が低い傾向にあります。`
  - `Audio: [sound:世界のニュースを日本人は何も知らない-148.mp3] | Sentence: オリンピックや豪華な公共施設に莫大な資金をつぎ込んでいる日本は、他の国の人の目には奇異に映っているのです。`
  - Noise example: `Sentence: ・レバノン大統領がイスラエルのドローン攻撃は宣戦布告と述べる` (list item) and `Sentence: ジョージ・Ｈ・Ｗ・ブッシュ氏 七九％ 一九九一年四月` (table row).

### 3.2 日本の教養365 (audiobook-to-SRS) [đã mở file]
- **Source:** same catalogue ("Book: Ichinichi Ichi Page Yomu Dake de Minitsuku Nihon no Kyouyou 365"). Mediafire, 793,638,341 bytes. Downloaded to `chung/raw/ja-subs2srs-audiobook-nihon-no-kyouyou-365/`.
- **Structure:** 11,341 notes. Same "audiobook to srs" note type and template. ID3 author 齋藤 孝.
- **Audio:**
  - 100 % present. Median 10.41 s. MP3 22.05 kHz stereo 64 kbps.
  - Chars/s median 3.80, but **19.7 % under 2 chars/s**. [suy luận] These are mostly fragments and headings (14.7 % of sentences are under 15 chars) whose clips include pauses.
- **Samples:**
  - `Audio: [sound:Nihon365-791.mp3] | Image: <img src="Nihon365.jpg"> | Sentence: 江戸時代に国内海運は飛躍的な発展を遂げた。`
  - `Audio: [sound:Nihon365-5305.mp3] | Sentence: 『農業全書』成立の背景には本草学があったのである。`
  - `Audio: [sound:Nihon365-6468.mp3] | Sentence: 昭和に入ると、独自の様式を確立した、飯塚琅玕斎（1890～1958）、その息子の飯塚小玕斎（1919～2004）、生野祥雲斎（1904～1974）、二代田辺竹雲斎（一竹斎、1910～2000）らの竹工芸作家が現れた。`
  - Noise: `Audio: [sound:Nihon365-10664.mp3] | Sentence: 2．`
- **Siblings in the same catalogue, not downloaded:** 世界の教養365 現代編 (744 MB), コンビニ人間 (119 MB). Links were live by HEAD. [cộng đồng/chưa xác minh] Same format by the look of the file names.

### 3.3 Love is Blind Japan JP-EN (subs2srs) [đã mở file]
- **Source:** catalogue DRAMAS row "Love is Blind Japan | English | 160p." Mediafire, 492,258,072 bytes. Downloaded to `chung/raw/ja-subs2srs-love-is-blind-japan/`.
- **Structure:**
  - 8,064 notes. Note type "Japanese Morphman Audio Ankiweb-2f355". Fields: ID, Expression, English, Reading (furigana), Screenshot, Audio_Sentence, Audio_Extra, Morph, Definition, focus morph. The last four are empty.
  - One "Sentence" card. **The front shows audio + screenshot with Reading and English set to `visibility:hidden`, so it is a listening-first card.**
  - The template loads `_kanjax_with_koohii v2.js` from media. Not executed. Review it before importing.
- **Audio:**
  - 100 % present (8,064/8,064). Median 3.04 s (0.82–9.62). MP3 48 kHz 128 kbps (Lavf56). Chars/s median 5.66.
  - About 2 % of clips are over 12 chars/s. Those are lines whose CC text is duplicated (for example "てか もう疲れてるんだけど てか もう疲れてるんだけど…").
- **Text:**
  - Netflix Japanese CC subtitles. They include speaker labels （ミドリ）, U+202A direction marks and ⸺.
  - Raw median 22 / 27.1 % ≥30. **Cleaned median 17 / 15.0 % ≥30.**
- **Translation:** English Netflix subtitles. They are loose: "しんどいですね それは" is rendered "You're right. That's not fair at all."
- **Samples:**
  - `ID: 08_5339_0.19.57.070 | Expression: ‪優しいから ‪いいわけじゃないでしょうね | English: Or am I using kindness as an excuse… | Reading: ‪ 優[やさ]しいから‪いいわけじゃないでしょうね | Screenshot: <img src="Love_is_Blind_Japan_08_0.19.58.217.jpg"> | Audio_Sentence: [sound:Love_is_Blind_Japan_08_0.19.57.070-0.19.59.364.mp3]`
  - `ID: 11_7773_0.47.55.080 | Expression: ‪（ミドリ）PODSの中だけ？ ‪（藤井）ご存じでした？ ‪あの PODSの時に こうやって ‪やってたんですって | English: Did you know about that? They wrote each other in the pods. | Screenshot: <img src="Love_is_Blind_Japan_11_0.47.57.041.jpg"> | Audio_Sentence: [sound:Love_is_Blind_Japan_11_0.47.55.080-0.47.59.001.mp3]`
  - `ID: 02_1238_0.27.45.789 | Expression: ‪しんどいですね それは ‪それは しんどいかな | English: You're right. That's not fair at all. | Audio_Sentence: [sound:Love_is_Blind_Japan_02_0.27.45.789-0.27.49.459.mp3]`
  - `ID: 05_3241_0.23.19.064 | Expression: ‪すごいびっくりしました ‪きれいすぎて 広くて | English: I was so surprised. It's so nice and spacious. | Audio_Sentence: [sound:Love_is_Blind_Japan_05_0.23.19.064-0.23.23.485.mp3]`
- **Longer examples from the random sample (cleaned):**
  - 自分の感じてきた人生とまあ 今 彼女が感じてる 人生っていうのは共通する部分が あるんじゃないかなと思いました
  - 始まりは 誰とでもいいんですけど 終わりがナナコさんじゃなきゃ 嫌だなって思ったんで

### 3.4 TEDxSapporo (subs2srs) [đã mở file]
- **Source:** catalogue DRAMAS row "TEDxSapporo | None | 360p." Mediafire, 214,076,057 bytes. Downloaded to `chung/raw/ja-subs2srs-tedxsapporo/`.
- **Structure:**
  - 3,419 notes, standard subs2srs note type. Fields: SequenceMarker, Audio, Snapshot, Video (empty), Expression, Meaning (**empty**), Reading (empty), Notes (empty).
  - Front: audio + snapshot + Expression. Back: Reading + Meaning.
  - Subdecks and tags give the talk title, for example "The new way of working | Kazutaka Muraguchi".
- **Audio:** 100 %. Median 3.12 s. MP3 44.1 kHz (Lavf57). Chars/s median 6.28.
- **Text:** median 19 chars, 15.4 % ≥30.
- **Samples:**
  - `SequenceMarker: 1_174_0.10.03.950 | Audio: [sound:The_significance_of_being_unique_What_Slime_Molds_Told_Me_Toshiyuki_Nakagaki_TEDxSapporo_1_0.10.03.950-0.10.08.300.mp3] | Snapshot: <img src="…_0.10.06.125.jpg"> | Expression: ベストな状態にして実現するっていうことが不可能な問題なんですね`
  - `SequenceMarker: 1_219_0.13.32.720 | Audio: [sound:The_new_way_of_working_Kazutaka_Muraguchi_TEDxSapporo_1_0.13.32.720-0.13.35.360.mp3] | Expression: よしこれを一つ産業化していこう`
  - `SequenceMarker: 1_198_0.10.59.100 | Audio: [sound:Hope_Invites_Tsutomu_Uematsu_TEDxSapporo_1_0.10.59.100-0.11.02.690.mp3] | Expression: お金で自信を買うようになって 身を飾るようになったり`
  - `SequenceMarker: 1_114_0.06.27.620 | Expression: 神社の中で例えばですよ 水神様とか弁天様`

### 3.5 Hanzawa Naoki JP-EN (subs2srs) [đã mở file]
- **Source:** catalogue DRAMAS row "Hanzawa Naoki | English | 160p." Mediafire, 457,144,778 bytes. Downloaded to `chung/raw/ja-subs2srs-hanzawa-naoki/`.
- **Structure:** 7,550 notes, note type "JA subs2srs". Same template as TEDx. Meaning (EN) is filled on 7,550 notes. 364 notes are tagged `duplicate`.
- **Audio:** 100 %. Median 3.02 s. MP3 48 kHz (Lavf55). Chars/s median 4.82. 6.7 % are under 2 chars/s: one-word lines such as 課長 or はい.
- **Text:** cleaned median **15**, 1.7 % ≥30. Contains TV-caption symbols ☎ 《 》 ≪ ➡ and half-width katakana (ﾌｫｽﾀｰ).
- **Samples:**
  - `SequenceMarker: 5_2096_0.1.56.500 | Audio: [sound:Hanzawa_5_0.1.56.500-0.2.00.820.mp3] | Snapshot: <img src="Hanzawa_5_0.1.58.660.jpg"> | Expression: 半沢には 東南アジアの零細企業に 行ってもらうことになる | Meaning: Hanzawa will be transferred to a small business in Southeast Asia.`
  - `SequenceMarker: 4_1514_0.4.53.690 | Audio: [sound:Hanzawa_4_0.4.53.690-0.4.56.150.mp3] | Expression: 私に どんな問題があると？ | Meaning: Pray tell what my problem is.`
  - `SequenceMarker: 1_0594_0.43.48.780 | Audio: [sound:Hanzawa_Naoki_1_0.43.48.780-0.43.51.060.mp3] | Expression: あとのことは全て任せます | Meaning: I'll leave everything to you.`
  - `SequenceMarker: 2_0097_0.7.35.310 | Expression: (相模)一つ 気になることが 何？ | Meaning: There's one thing that caught my attention. - What? - Last year on July 3rd,`. This shows EN and JP segments that are not one-to-one.

### 3.6 Dictionaries of Japanese Grammar — Sentences (w/audio), AnkiWeb 843402109 [đã mở file] [tài liệu chính thức]
- **AnkiWeb:**
  - 5,279 notes, 5,423 audio, +36/−0. Updated 2024-12-29.
  - Description: "all sentences in the book series 'A Dictionary of Japanese Grammar', one card for each sentence". The author says "I'll no longer be providing updates" and lists errata.
  - Downloaded to `chung/raw/ja-djg-grammar-sentences-audio/`.
- **Structure:**
  - Subdecks: 1 - Basic, 2 - Intermediate, 3 - Advanced. Fields: Japanese, Reading, English, Grammar Point, Explanation, AwesomeTTS, Level, Page Number, Extra Notes.
  - One "recognition" card. Front: Grammar Point + hint:Explanation + furigana:Reading. Back adds audio and English. No listening card.
- **Audio:**
  - 5,278/5,279 notes OK. Median 4.09 s (1.54–16.15).
  - 22–24 kHz mono, 48–96 kbps. File-name prefixes are AwesomeTTS service tags: naverclovapremium 2,042, azure 1,528, amazon 846, vocalware 629, naver 368, hypertts 7, googletts 4.
  - [suy luận] This means mixed neural TTS (Clova, Azure, Polly) plus older concatenative TTS (Vocalware). Voice changes from card to card.
  - About 1 % of a 300-note sample read over 12 chars/s, all on A/B dialogues (for example 49 chars in 2.3 s). [suy luận] These clips are truncated or partial.
- **Length by level:** Advanced n=2,289, median 31.0, ≥30 56.7 %, ≥50 12.8 %. Intermediate 24.0 / 26.4 %. Basic 19.0 / 8.3 %.
- **Samples:**
  - `Japanese: 友達に聞いたところによると、フィンランドのメーデーは学生も集まって春を祝う祭りの日だそうだ。 | English: According to my friend, May Day in Finland is a day when everyone, including students, joins in a festival to celebrate spring. | Grammar Point: によると | Explanation: According to; based on | A compound particle that is used to identify the source of information provided in the sentence. | AwesomeTTS: [sound:azure-9694de2c-750e0b7c-826cae7a-1093c9bf-750f115d.mp3] | Level: Advanced | Page Number: 459`
  - `Japanese: エンジンに故障があったとかで、飛行機の出発が五時間も遅れた。 | English: The flight departure was five hours late for some reason like there was engine trouble. | Grammar Point: とかで | AwesomeTTS: [sound:naverclovapremium-a3a124b9-9246cd08-1a841a26-df5a5920-7d67c0e5.mp3] | Level: Intermediate | Page Number: 498`
  - `Japanese: 彼はどちらかと言うと話すより書く方が得意だ | English: He is better at writing than speaking. | Grammar Point: どちらかと言うと | AwesomeTTS: [sound:azure-8c4c61ca-8bdeef8a-b13748d3-13d1e385-6709f585.mp3] | Level: Advanced | Page Number: 78`
  - From the AnkiWeb sample: `Japanese=交通事故のこと伺いました。お怪我などなかった由、ほっといたしております。 | English=I heard about the trafﬁc accident. I am relieved to hear that you were not hurt. | Grammar Point=由・よし | Level=Advanced | Page Number=738`
- **Text defects:** 389 sentences contain `・` or `{…}` alternatives, for example "私は三時間ごとに薬を飲んだ・飲みました。" TTS reads these awkwardly. 30 notes are A/B dialogues.
- A no-audio sibling exists: "Japanese Sentences" [54897524](https://ankiweb.net/shared/info/54897524) (8,547 notes, 2017). Reviews say it uses the same DJG source. It is superseded by 843402109.

### 3.7 NativShark "4,217 Japanese Sentences w/ Audio", AnkiWeb 126242908 [đã mở file]
- **AnkiWeb:** 4,127 notes, 7,665 audio. Updated 2024-03-12. Description: "Sentence written by a native speaker. Male & female human audio (native speakers) at natural speed."
- **Structure:**
  - Card "Comprehension (i.e. Reading) Practice": front Sentence J, back reading, English, literal, audio, notes, lesson link.
  - Lesson links point to courses.nihongoshark.com. [suy luận] Likely dead.
- **Audio:**
  - Male 4,125 present, median 2.40 s. Female 3,491/4,127 present (**84.6 %**).
  - LAME 3.99, 44.1 kHz mono 128 kbps. ID3 artist "NihongoShark.com".
  - 50 "Bonus" anime clips.
- **Text:** median **11**, 3.2 % ≥30.
- **Samples:**
  - `Sentence J: 夜ご飯を作ろうとしたとき、用事を思い出した。 | Sentence K: よるごはん を つくろう と した とき、 ようじ を おもいだした。 | English: Just when I was about to make dinner, I remembered something I needed to do. | Note: The nuance is that the speaker did not continue making dinner right then. The action was interrupted. | Audio (Male): [sound:NDL_0772_Male.mp3] | Audio (Female): [sound:NDL_0772_Female.mp3] | Lesson #: 59`
  - `Sentence J: 一万円札しかない。 | English: I don't have anything but 10,000 yen bills. // I only have 10,000 yen bills. | Note: For example, when splitting the check with a friend. | Audio (Male): [sound:NDL_0396_Male.mp3]`
  - `Sentence J: 仕事終わった？ | English: Are you done with work? | Literal English: work + finished? | Audio (Male): [sound:NDL_2653_Male.mp3]`

### 3.8 Miku Real Japanese YouTube Shadowing Deck, AnkiWeb 252860248 [đã mở file]
- 671 notes (+7/−0), updated 2024-02-25.
- Subdecks are "!🍜Miku_RJ_lvl1::…" grammar units (te-form, たら, ないといけない…). Note types:
  - Conversation (30): full-dialogue audio, median 19.25 s.
  - Conjugation (190): word audio of about 0.9 s.
  - Grammar (451): sentence audio, median 2.12 s, median 14 chars.
- Audio is 320 kbps from Miku's videos. Each note has a YouTube link.
- **Samples:**
  - `Sentence: 明日 晴れたら 海 に行こう！ | Sentence Translation: If it gets sunny tomorrow, let's go to the beach. | Sentence Audio: [sound:3 明⽇晴れたら海に⾏こう！.mp3] | videoLink: https://www.youtube.com/watch?v=OrnjEazL4dg | Grammar Point: たら - if`
  - `Sentence: 疲れすぎて トイレで 寝た。 | Sentence Translation: I got too tired and fell asleep on the toilet. | Grammar Point: すぎた- I did to much`
  - Conversation note `03-09-1-00c`: `ST2SP1-JAP: 年上[としうえ]の 人[ひと]とデートし<b>たことある</b>? | ST2SP1-TRAD: Have you ever gone on a date with someone older than you? | ST3SP1-JAP: 今度[こんど] 先輩[せんぱい]とデートするんだけど、`
- **Verdict:** native and well made, but N5–N4. Not for this learner.

### 3.9 Natural Adult Japanese: Friendship, Boundaries, and Social Confidence, AnkiWeb 1810272637 [đã mở file]
- 702 notes, no media, 2026-05-10. Note type is literally named **"Codex Adult Japanese Basic"**. [suy luận] Generated with an AI coding tool.
- Japanese-only text: median 16, 22.6 % ≥30. Topics: social search phrases (Yokohama circles), museum talk, invitations, boundary language, aizuchi.
- **Samples:**
  - `Front: <div class='prompt'>English → Japanese</div><div class='en'>Of course, I know you have your schedule and family too, so please do not force it.</div> | Back: … もちろん、<ruby>予定<rt>よてい</rt></ruby>やご<ruby>家庭<rt>かてい</rt></ruby>のこともあると<ruby>思う<rt>おもう</rt></ruby>ので、<ruby>無理<rt>むり</rt></ruby>しないでください。 | Category: Invitations | Notes: Softens invitation.`
  - `Front: … <ruby>意外<rt>いがい</rt></ruby>と<ruby>毒舌<rt>どくぜつ</rt></ruby>ですね。でも<ruby>面白い<rt>おもしろい</rt></ruby>です。 | Back: You are surprisingly sharp-tongued. But it is funny. | Category: Playful teasing`
  - `Front: … <ruby>横浜<rt>よこはま</rt></ruby> <ruby>英会話<rt>えいかいわ</rt></ruby>サークル <ruby>平日<rt>へいじつ</rt></ruby> <ruby>昼<rt>ひる</rt></ruby> | Back: Yokohama English conversation circle weekday daytime | Category: Social search`
- **Verdict:** reject. No audio, AI-written, and a personal or niche scope (it even includes "avoid" cards such as 既婚女性を狙う).

### 3.10 Source: the Subs2SRS Japanese Deck Catalogue [cộng đồng]
- Google Sheet "Subs2SRS Japanese Deck Unofficial User's Guide", tab "Where to Find Decks". Exported as CSV on 2026-11-13.
  - Rows: ANIME 1,751, MOVIES 157, **DRAMAS 136**, MISCELLANEOUS 280 (audiobooks, light novels, games).
  - Mostly Mediafire links, many with Wayback archive links.
  - Most drama rows have native-language translation "None", meaning JP-only.
- **Live-action rows relevant to this learner:**
  - Reality: Terrace House S1–S5 (several splits, one S5 "w Eng Subs"), Love is Blind Japan (EN).
  - Business: Hanzawa Naoki (EN), Haru 総合商社の女, 株価暴落, 監査役 野崎修平, 空飛ぶタイヤ.
  - Legal: Legal High (EN), Legal V.
  - Other: 新聞記者 (movies section), Midnight Diner S1–2, 東京独身男子, ワカコ酒, MIU 404, Unnatural, TEDxSapporo.
- **Link health checked by HEAD on 2026-11-13:** Love is Blind, Hanzawa, TEDxSapporo, Terrace House 2019-20 Eng, and the four audiobook decks are live. "Kantaro – The Sweet Tooth Salaryman" returns **404 (dead)**.
- The catalogue warns: "Some degree of oddities is to be expected. Standards vary by maker." Japanese-like-a-breeze's own Mediafire folder page says "Many decks are broken (e.g. have no image or wrong audio)". Expect to QA each deck.

---

## 4. Rejected (one line each)
- **Miku Real Japanese Shadowing** [252860248](https://ankiweb.net/shared/info/252860248): inspected. Level 1 (N5–N4), median 14 chars.
- **Natural Adult Japanese** [1810272637](https://ankiweb.net/shared/info/1810272637): inspected. No audio, AI-generated note type, phrase-level.
- **NativShark 4,217** [126242908](https://ankiweb.net/shared/info/126242908): inspected. Human audio, but median 11 chars. Optional warm-up only, not core.
- **Japanese N3 N2 N4 Anime, Sentence, images, audio** [716786929](https://ankiweb.net/shared/info/716786929): 344 notes, anime only. Reviews: "many of the translations are wrong".
- **QUARTET: Intermediate (Complete Edition)** [1357880192](https://ankiweb.net/shared/info/1357880192): 3,034 notes, vocabulary only, no audio.
- **日本語能力試験２級 – JLPT N2 – 聴解** [1466939656](https://ankiweb.net/shared/info/1466939656): 3,915 notes, but audio is word-level (word-listening cards).
- **All Japanese sentences with audio from Tatoeba** [1823020002](https://ankiweb.net/shared/info/1823020002): 1,283 short sentences, 2019.
- **JAPANESE SENTENCES A1-C2 UNFINISHED** [241565247](https://ankiweb.net/shared/info/241565247): "used ChatGPT to make the sentences", no audio, abandoned.
- **Japanese Sentences** [54897524](https://ankiweb.net/shared/info/54897524): DJG text without audio, superseded by 843402109.
- **Japanese Keigo practice** [1172156364](https://ankiweb.net/shared/info/1172156364): 29 notes, no audio.
- **Japanese Yojijukugos 四字熟語** [1342560157](https://ankiweb.net/shared/info/1342560157): 1,503 idioms with word audio only (Migaku, 2021). No sentences.
- **Onomato Project 2** [847397596](https://ankiweb.net/shared/info/847397596): 108 notes, no audio.
- **Onomatopoeia 擬音語と擬態語** [935796174](https://ankiweb.net/shared/info/935796174): 182 notes, short sample sentences (シャツはびしょびしょだった). Good for its niche, not long sentences.
- **【EN/中文/日本語】Onomatopoeia (Lapis)** [1883048818](https://ankiweb.net/shared/info/1883048818): 544 notes, short dictionary sentences (どかんという大きな音がした).
- **Human Japanese Intermediate Complete** [1704302605](https://ankiweb.net/shared/info/1704302605): elementary, kana-spaced (ジョンさん、どの わしょくが 一番 すき？), 2017.
- **Anime Japanese, Explained by a Native** [1196360131](https://ankiweb.net/shared/info/1196360131): 34 notes, N5, no audio.
- **(Cún) [Shadowing] A philosophical inquiry from Ted P1/P2** [444003606](https://ankiweb.net/shared/info/444003606) / [1397881535](https://ankiweb.net/shared/info/1397881535): English TED with Vietnamese translation, not Japanese. Relevant to the English report only.
- **NHK Easy Japanese 2019 / for Korean** [1467451973](https://ankiweb.net/shared/info/1467451973), [1666913008](https://ankiweb.net/shared/info/1666913008): beginner course.
- **NHK Easy Japanese – Skit Sentences** [198914030](https://ankiweb.net/shared/info/198914030): no audio, beginner.
- **Pimsleur Japanese** [1044963126](https://ankiweb.net/shared/info/1044963126): beginner course audio. Reviewer says it no longer matches the updated course.
- **13000 Advanced Japanese Words with Audio** [1619721766](https://ankiweb.net/shared/info/1619721766): vocabulary, word audio from Forvo/Google (per description).
- **"Speak Naturally in Japanese" free deck (Booth, Anki-ya)** [booth 6920715](https://booth.pm/en/items/6920715): 355 KB zip, password inside a Kindle book, about 50 cards.
- **新标准日本语 中级/高级 教材原版发音** [1285132737](https://ankiweb.net/shared/info/1285132737) and siblings: textbook vocabulary decks per titles and snippets. [chưa xác minh]
- **Glossika Japanese Fluency 1–3**: exists on AnkiWeb per search snippet, but IDs were not obtained (search blocked). Likely an unlicensed copy of a paid course. [chưa xác minh]
- **Kantaro – The Sweet Tooth Salaryman (subs2srs)**: Mediafire 404.

---

## 5. Merge and fix plan (practical)
1. **Love is Blind (and/or Terrace House):**
   - Script a line-merger that groups lines from the same episode with gaps ≤0.7 s up to about 60 chars and concatenates the MP3s with ffmpeg.
   - Move （名前） into a Speaker field. Collapse duplicated CC text.
   - Add VI/EN machine translation, keeping the Netflix EN as "Subtitle EN".
   - Keep the existing listening-first front.
2. **世界のニュース / 日本の教養:**
   - Drop notes under 15 chars or under 2.5 chars/s.
   - Add Translation (VI), a Target word (rarest word by JPDB/BCCWJ frequency) and a Context field (previous and next sentence, rebuilt from the clip index in the filename).
   - Add an audio-first card.
3. **DJG:**
   - Re-voice all sentences with one neural voice. Options: Azure ja-JP-Nanami/Keita, or locally with the Irodori-TTS add-on (github.com/mattias/anki-irodori-audio, updated 2026-11-11) or VOICEVOX.
   - Use two voices for the 30 A/B dialogues. Expand the 389 `・`/`{…}` alternatives before TTS.
   - Add a listening card. Suspend Basic.
4. **Target lists** (Tango N1, Core, etc. from round 1): fill them with real clips via Aobana Reibun (Immersion Kit + Nadeshiko), as recommended in round 1.

---

## 6. Sources
- Previous notes: `research_notes/Bộ thẻ Anki ba ngôn ngữ/japanese_beyond_n1_decks.md`, `japanese_jlpt_decks.md` (round 1).
- Codex candidates: `chung/ung_vien_Codex.md`. Terrace House ep1 and VideoAnki previews are cited from there, not re-inspected.
- Subs2SRS Japanese Deck catalogue: https://docs.google.com/spreadsheets/d/15ELElkomfixdS4-dNrpxrNl14mlJUZrdD0h7N6iEE2k/htmlview (tab "Where to Find Decks", gid 1386920750).
- Mediafire files (downloaded 2026-11-13; `_meta.json` in each `chung/raw/ja-subs2srs-*` folder):
  - Love is Blind Japan: https://www.mediafire.com/file/7gizhqvujil1u28/Love_is_Blind_Japan_JP-EN.apkg/file
  - Hanzawa Naoki: https://www.mediafire.com/file/rngx63thceds4xi/Hanzawa_Naoki.apkg/file
  - TEDxSapporo: https://www.mediafire.com/file/qd36sd1mtq8dmby/TEDxSapporo.apkg/file
  - 世界のニュース: https://www.mediafire.com/file_premium/yvbfe9ylj3de33z/ (full URL in `_meta.json`)
  - 日本の教養365: https://www.mediafire.com/file_premium/8zmlbuw5l8bejey/ (full URL in `_meta.json`)
- AnkiWeb (info via logged-in API; downloads in `chung/raw/ja-*`): [843402109](https://ankiweb.net/shared/info/843402109), [126242908](https://ankiweb.net/shared/info/126242908), [252860248](https://ankiweb.net/shared/info/252860248), [1810272637](https://ankiweb.net/shared/info/1810272637). Info only: 716786929, 1357880192, 1466939656, 444003606, 1823020002, 1883048818, 241565247, 54897524, 1172156364, 1342560157, 847397596, 935796174, 1196360131, 1704302605.
- Japanese-like-a-breeze decks page (Mediafire folder warning): https://www.japanese-like-a-breeze.com/decks/
- Booth Anki-ya: https://booth.pm/en/items/6920715
- Reddit thread on Terrace House decks (via search snippet; the page could not be fetched): r/LearnJapanese 1jwkx28 (Apr 2025).
- Author background for 世界のニュース: https://bunshun.jp/articles/-/52775 , https://agora-web.jp/archives/250629010125.html
- Tools: https://github.com/mattias/anki-irodori-audio , https://github.com/Wyzmic/Aobana-Reibun
- Scripts (mine): `scratchpad/scripts/r2-ja/inspect_ja.py`, `field_stats.py`, `cps_check.py`, `show_tmpl.py`. Outputs in `scratchpad/out-r2ja/i_*.txt`.
