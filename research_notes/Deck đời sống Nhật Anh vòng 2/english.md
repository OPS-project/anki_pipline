# English round 2: real-life, advanced, long sentences with full-sentence audio (state as of 2026-11-13)

Scope: pre-made decks for a C1 learner (TOEIC L&R 935) who wants near-native comprehension and expression across daily life, relationships, humor and emotion, news, film and TV, podcasts, commentary, presentations, speeches, debate and work. Word-list decks count only as target lists. This round builds on `research_notes/Bộ thẻ Anki ba ngôn ngữ/english_advanced_decks.md` and does not repeat its items (Language Reactor, asbplayer, subs2srs, Glassy-Gaia Gumroad, Kelciour subs2srs, Ecattea COCA, Tatoeba, eggrolls OALD, Close-up C2).

Evidence labels: **[đã mở file]** = I downloaded the .apkg and inspected it with my own script. **[tài liệu chính thức]** = AnkiWeb's own deck data (title, counts, description, sample notes, from the logged-in `item-info` endpoint) or the creator's official page. **[cộng đồng]** = user reports or reviews. **[quảng cáo]** = creator promotion. **[chưa xác minh]** = not confirmed. **[suy luận]** = my inference.

How the measurements were made:
- Inspected decks are in `chung/raw/<slug>/deck.apkg`. The inspector is `scratchpad/scripts/r2-en/inspect_en.py`. Raw outputs are in `scratchpad/scripts/r2-en/out/insp_*.txt`.
- **Words per sentence:** counted after stripping HTML and `[sound:]` tags.
- **Audio coverage:** the share of notes whose sentence-audio field has a `[sound:]` reference whose file is present in the media map.
- **Durations:** from MP3 frame headers or MP4 `mdhd` on a random sample of 80 clips per field.
- **Voice type:** inferred only from encoder tags (ID3 `TSSE`, LAME/Lavc strings), sample rate, channels, filenames and the deck description. **I cannot listen, so nothing here judges naturalness by ear.**

**Important limitation — AnkiWeb search hit its daily cap.** After 6 successful queries ("TED", "podcast", "BBC", "VOA", "ESL", "conversation"), AnkiWeb's search endpoint returned HTTP 429 with the body `Daily limit exceeded; please try again tomorrow.`. The account and IP are shared with the other researchers. The `item-info` and download endpoints kept working, and the login session did not expire.
- I could therefore not run the planned English, Japanese, Chinese and Vietnamese title searches (sitcom, Friends, movie, interview, speech, debate, 英会話, 美剧, 老友记, giao tiếp, Cún, and so on).
- Discovery came from four sources: the 481 rows those 6 queries returned (the search is a substring match, so "TED" also matched "Updated", "Targeted" and so on); the Japanese researcher's saved search rows in `scratchpad/out-r2ja/s1.txt` (例文, 上級, 会話); web search; and known IDs.
- The prioritised query list for a rerun tomorrow is ready: `scratchpad/scripts/r2-en/queries_pri.txt` (79 queries) and `queries1.txt`/`queries2.txt`. Run `aw_batch_search.py` with `AW_GAP=20`.

---

## 1. Top findings & shortlist

### Takeaway (in the user's frame)
- **The best pre-made real-audio sentence decks found this round are all built on TED or TED-Ed.**
  - **[GLASSY-GAIA] TED-Ed (AnkiWeb, 4 parts, 1,597 notes, 40 videos):** the best single find. Every line has its original audio clip (median 7.1 s). Sentences are long (median 16 words; 57% ≥15). Each line carries LLM-style chunk glosses with TTS example sentences, plus Vietnamese, Japanese and Chinese subtitles. The card is listening-first with a typing field. [đã mở file, Part 1]
  - **Real TED talks (presentation and speech register):** a Chinese creator's "逐句精听TED / 视频跟读TED" series has one deck per talk, with one MP4 clip per sentence (Amy Cuddy, Julian Treasure, Lera Boroditsky, Robert Waldinger). [đã mở file, Amy Cuddy]
  - **Vietnamese-made TED-Ed decks:**
    - "(Cún) [Shadowing] A philosophical inquiry from Ted": philosophy topics, word-timed shadowing UI, Vietnamese translation, but ASR transcript errors and low-bitrate audio.
    - socialge "[English - Vietsub] TED-ED song ngữ": subs2srs-cut clips with Vietnamese subtitles and dictation cloze, but fragmentary lines.
- **Nothing found covers sitcoms, film, podcasts, news, relationships or humor with real audio.** These are the areas the user cares most about.
  - The only AnkiWeb drama-like hit was a video game: Kingdom Come: Deliverance, medieval register, about 10% audio coverage.
  - Systematic AnkiWeb searching was cut short (see the limitation above), so this is **not** proof of absence.
  - For these domains the realistic route remains self-mining (Language Reactor on Netflix, asbplayer, subs2srs; audio2anki or gogadget for podcasts). Codex's lead VideoAnki (The Moth / Tom Scott) may also help.
- **TTS sentence decks for production practice (Japanese creators):**
  - "英語例文 暗唱・スピーキング練習デッキ" (1,000 cue→speak sentences, B1–B2, Japanese notes);
  - DUO 3.0 with Azure TTS (560 dense sentences, Japanese prompt).
  - Both are textbook or LLM-style, short-to-medium sentences (median 11–12 words). They are useful as a production drill, not as C1 real-life input.
- **Target lists (no change from round 1, plus two new ones):**
  - C1 American: HyperTTS, median 10 words. [đã mở file]
  - 英検1級パス単 AI例文: 2,400 Gemini-written sentences with Google Cloud TTS. [tài liệu chính thức]
  - TOEFL3800 例文: Gemini sentences with Google WaveNet en-US-Wavenet-H. [tài liệu chính thức]

### Shortlist with roles and scores
Rubric (100 points): sentence audio 25, naturalness and richness 20, level fit 15, speaking-useful expressions 15, coverage and progression 10, accuracy and maintenance 10, extras 5. Each score carries about ±6 points of uncertainty: they are judgments from inspected samples, not measurements.

| # | Deck | Role | Score | Why (short) |
|---|---|---|---|---|
| 1 | [GLASSY-GAIA] youtube-ted-ed-anki-english-en, Parts 1–4 (AnkiWeb 635719672 / 994314683 / 1941960573 / 210221519) | **Core (listening + chunks)** | **~77** (audio 22, natural 14, level 13, speaking 11, coverage 6, accuracy 6, extras 5) | Original line audio 100%; long sentences; chunk glosses with TTS examples; Vietnamese, Japanese and Chinese translations; listening-first plus typing. Domain is explainer narration plus some live-talk anecdotes, not conversation. |
| 2 | 逐句精听TED / 【视频跟读】TED series (e.g. AnkiWeb 499194989 Amy Cuddy; 159376863 Julian Treasure; 2070886245 Lera Boroditsky; 1988506665 Robert Waldinger) | **Listening-shadowing (presentation/speech register)** | **~66** (21/15/12/8/3/5/2) | Real, partly spontaneous TED speech with per-sentence video clips. The only verified source for presentation rhetoric. One talk per deck (107–255 lines). The translation field is empty or polluted. ASR glitches. |
| 3 | (Cún) [Shadowing] A philosophical inquiry from Ted P1/P2 (AnkiWeb 444003606 / 1397881535) | **Listening-shadowing (+ Vietnamese)** | **~66** (20/13/13/8/4/4/4) | Original TED-Ed audio; median 16 words, 61% ≥15. Shadowing UI: word timing, click a word to replay from it, speed control, GIF. Weak points: **ASR transcript errors**, 16 kHz / 40 kbps audio, a sponsor read included, Vietnamese that reads like machine translation. |
| 4 | [English - Vietsub] Anki TED-ED song ngữ Anh-Việt P1–P3 (AnkiWeb 1918837902 / 1250980978 / 866780035) | **Supplementary listening and dictation (+ Vietnamese)** | **~64** (20/13/10/7/6/5/3) | subs2srs clips with Vietnamese subtitles and Cambridge definitions. Subtitle-line fragments (median 13 words; 39% ≥15). Cloze targets single words. Not updated since 2023. |
| 5 | 英語例文 暗唱・スピーキング練習デッキ (AnkiWeb 1190669808) | **Supplementary speaking drill (production)** | **~57** (15/8/8/12/6/5/3) | 1,000 cue + audio → say the sentence; Japanese translation and notes; grammar-pattern tags. Images are missing from the package. TTS. B1–B2. |
| 6 | duo3.0 日本語例文 音声付き（音声更新ver）(AnkiWeb 1973703622) | **Supplementary production (Japanese → English)** | **~56** (15/10/9/11/6/3/2) | 560 dense DUO sentences, many short two-line dialogues; Azure TTS; Japanese prompt card. Copyrighted book content. |
| 7 | English. C1 Words, Idioms, Phrasal Verbs. American Accent. (AnkiWeb 524918335) | **Target list** | **~55** | HyperTTS; median 10 words; IT and creator-workplace slant plus slang. (Round 1 called it a scaffold; now inspected.) |
| 8 | Kendra's Language School 连读听力 (AnkiWeb 1364160335) | **Listening warm-up only** | **~48** | Native normal and slow audio, but 3–4-word phrases with the text only in an image. Too basic for C1. |

### Merge notes (what to combine, overlaps, fixes)
- **Suggested combination:** #1 (all 4 parts) as the core; #2 for the presentation and speech register; one of #3 or #4 for extra TED-Ed listening with Vietnamese. Add #5 **or** #6 (not both) as a production drill. Use #7 and the Japanese AI decks only as target lists for mining.
- **Overlaps:**
  - #1 and #3 share at least 2 TED-Ed videos: "This tool will help improve your critical thinking" and "What if you experienced every human life in history?". Glassy-Gaia lists them in Part 2; Cún has them in P1 and P2.
  - #4's video set (bats, bees, OCD, Brutus, Channel Tunnel, power plants and others) seems mostly disjoint from #1's 40 videos. #1 Part 4 has "How the world's longest underwater tunnel was built", which may match #4's "underwater_tunne" subdeck. [suy luận; not text-diffed]
  - Dedupe all TED-Ed sources on a normalized English line.
- **Target note type when merging:** Sentence | SentenceAudio | Context (source video or talk, speaker, URL, tag) | Chunks (glossed expressions) | Chunk examples (+audio) | EN meaning | VI | JA | Image.
  - #1 maps almost one-to-one: tags hold the video slug, and Word_1..4 hold the chunks.
  - #3 has a YouTube URL field.
  - #4 has a timestamped audio filename (usable as context).
  - #2 has no context field, but its deck name is the talk title.
- **Fixes needed:**
  - **#1:**
    - Hide the 15+ unused language fields.
    - Spot-check translation alignment. I saw a Dutch field that was word salad, a Chinese_CH field truncated to one clause, and a duplicated Japanese line.
    - The chunk examples are TTS (NAVER Clova via HyperTTS). Keep them, or re-voice with a better neural TTS.
  - **#2:**
    - Fill the Translation field (LLM or MT, Vietnamese or Japanese).
    - Fix ASR glitches.
    - Optionally extract audio-only from the MP4s to shrink size and support mobile.
  - **#3:**
    - Proof-read the transcripts against the official TED-Ed subtitles (e.g. "attempting offer" should be "tempting offer"; "Xeno of Cyprus" should be "Zeno of Citium").
    - Delete outro and sponsor lines.
  - **#4:**
    - Merge adjacent fragment clips into full sentences. Filenames carry start and end timestamps, so concatenation with ffmpeg is straightforward.
    - Add a sentence-level (not single-word) chunk cloze.
  - **#5 and #6:** source sentences are textbook or LLM-written, so do not treat them as "real-life". Optionally re-voice with a better neural TTS.

---

## 2. Candidate table

| Deck | Link / ID | Domains (sampled) | Median words | % ≥15 words | Sentence audio (type · coverage · accent) | Context fields | Translation | Notes | Updated | Evidence | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [GLASSY-GAIA] TED-Ed P1 (P2–P4 same format) | [635719672](https://ankiweb.net/shared/info/635719672) · [994314683](https://ankiweb.net/shared/info/994314683) · [1941960573](https://ankiweb.net/shared/info/1941960573) · [210221519](https://ankiweb.net/shared/info/210221519) | Science/health 9, history/food culture 7, psychology/motivation 6, first-person TED-talk anecdote 7, writing 1 (of 30) | 16 | 57% | Original video soundtrack (stereo 44.1 kHz, 320 kbps, ffmpeg-cut) · 100% · TED-Ed narrators, mostly US [suy luận]. Chunk-example audio: NAVER TTS (`TSSE=nVoiceTTS@NAVER`, 24 kHz mono) | Video slug in tags and subdeck; image per line | VI 427/432, JA 390/432, ZH-CN 430/432 (+18 more language fields) | 432 / 391 / 407 / 367 notes; 40 videos | 2025-10-24 | [đã mở file] P1; [tài liệu chính thức] P2–P4 | **Core** |
| 逐句精听TED: Amy Cuddy "Your body language may shape who you are" | [499194989](https://ankiweb.net/shared/info/499194989) (+ 159376863, 2070886245, 1988506665) | Psychology research talk ~16, personal story/emotion ~7, audience address/rhetoric ~7 (of 30) | 12 | 40% | Original TED talk, MP4 video clip per sentence (audio track 44.1 kHz) · 100% · US | Deck name = talk; Source and Backlink fields empty | **None** (field empty; on 2070886245 it holds an ad string) | 255 notes; 4 sibling decks of 107–164 notes | 2025-10-12 | [đã mở file] (Amy Cuddy); [tài liệu chính thức] (others) | **Listening-shadowing (speech register)** |
| (Cún) [Shadowing] Philosophical inquiry from TED P1 | [444003606](https://ankiweb.net/shared/info/444003606) · P2 [1397881535](https://ankiweb.net/shared/info/1397881535) | Philosophy explainer 30/30 (love/emotion 8, meaning of life/existentialism 9, Stoicism/Cynicism 5, critical thinking 3, thought experiments 5) | 16 | 61% | Original TED-Ed audio, downsampled (16 kHz mono, 40 kbps, Lavf62) · 100% · mostly US [suy luận] | YouTube URL; GIF clip | VI (likely MT) [suy luận] | 372 + 321 notes | 2026-04-09 | [đã mở file] P1; [tài liệu chính thức] P2 | **Listening-shadowing** |
| [English - Vietsub] TED-ED song ngữ Anh-Việt P1 | [1918837902](https://ankiweb.net/shared/info/1918837902) · P2 [1250980978](https://ankiweb.net/shared/info/1250980978) · P3 [866780035](https://ankiweb.net/shared/info/866780035) | Science/nature/health 9, history 8, engineering/architecture 6, psychology 4, narration filler 3 (of 30) | 13 | 39% | Original audio, subs2srs-style cuts (stereo 44.1 kHz, 128 kbps, `TCON=Speech`) · 100% of dictation notes · mostly US [suy luận] | Video tag; timestamped filename; screenshot | VI (TED subtitle style) | P1: 1,030 lines × 2 note types (dictation + vocab cloze); P2 1,033 notes / 557 audio; P3 871 / 1,257 | 2023-08-24 | [đã mở file] P1; [tài liệu chính thức] P2–P3 | **Supplementary** |
| 英語例文 暗唱・スピーキング練習デッキ | [1190669808](https://ankiweb.net/shared/info/1190669808) | Daily life ~13, workplace ~9, grammar showcase ~6, opinion/discourse ~3 (overlapping, of 30) | 11 | 7% | TTS (24 kHz mono; files named `deck_2025…`) · 100% · voice accent not determinable | Cue words; grammar tag; notes (157/1000) | JA | 1,000 notes; Image field holds filenames but **no images in package** | 2026-02-25 | [đã mở file] | **Supplementary (speaking drill)** |
| duo3.0 日本語例文 音声付き（音声更新ver） | [1973703622](https://ankiweb.net/shared/info/1973703622) | Daily dialogues ~11, news/society ~9, academic/abstract ~6, misc ~4 (of 30) | 12 | 26% | **Azure TTS** (`azure-*.mp3`, 24 kHz mono) · 100% · not determinable | none | JA (prompt side) | 560 notes; +144 thumbs | 2021-08-15 | [đã mở file] | **Supplementary (production)** |
| English. C1 Words, Idioms, Phrasal Verbs. American Accent. | [524918335](https://ankiweb.net/shared/info/524918335) | Creator/IT workplace ~11, slang/social media ~8, city/travel ~8, emotions ~3 (of 30) | 10 | 8% | HyperTTS (example 24 kHz mono 160 kbps; word 44.1 kHz) · 100% · US (title) | none | none (EN definition) | 1,731 notes | 2025-12-09 | [đã mở file] | **Target list** |
| Kendra 英语短语连读听力特训 | [1364160335](https://ankiweb.net/shared/info/1364160335) | Everyday phrases | 3–4 (from images) | 0% | Native teacher, normal + slow (stereo 44.1 kHz, Lavc58) · 100% · US | number only; text in image | ZH (in image) | 332 notes | 2022-02-08 | [đã mở file] | Listening warm-up / reject for C1 |
| Illustrated Everyday Idioms with Stories (Kelciour sample) | [665597838](https://ankiweb.net/shared/info/665597838) | Basic idioms, daily-life mini-dialogues | Dialogue 20; examples 8 | Dialogue 92% | Publisher recordings (`TPE1=Compass Media`, 22 kHz stereo) for phrase, examples and dialogue; Azure TTS (UK Libby) for meaning · 100% | Dialogue, caption, illustration | none | 120 of 600 (full set sold via hipolink) | 2026-10-14 | [đã mở file] | Reject (A2–B1) |
| 英検1級パス単 AI例文 | [1107102763](https://ankiweb.net/shared/info/1107102763) | Eiken-1 (≈C1) vocabulary in LLM sentences | ~12–14 (samples) | ? | Google Cloud TTS · ~100% (2,400/2,400) | none | JA | Gemini 2.5 Flash-Lite sentences | 2026-01-17 | [tài liệu chính thức] | Target list |
| TOEFL3800 例文 | [1579676728](https://ankiweb.net/shared/info/1579676728) | TOEFL vocabulary in LLM sentences | ~8–14 (samples) | ? | Google WaveNet en-US-Wavenet-H · 3,846/3,846 | none | JA | Gemini sentences | 2025-11-23 | [tài liệu chính thức] | Target list |

---

## 3. Per-deck details with real samples

### 3.1 [GLASSY-GAIA] youtube-ted-ed-anki-english-en (Parts 1–4) — core
- **Basics** [tài liệu chính thức]:
  - P1 635719672: 432 notes, 1,338 audio, 432 images, 208 MB, updated 2025-10-24.
  - P2 994314683: 391 notes, 1,308 audio.
  - P3 1941960573: 407 notes, 1,339 audio.
  - P4 210221519: 367 notes, 1,335 audio.
  - 10 TED-Ed videos per part, 40 in total. The descriptions claim "Intermediate → Advanced (B1–C1 CEFR)" [quảng cáo]. Previous round knew only the Gumroad and GitHub side; **these AnkiWeb copies are free downloads.**
- **Videos by part:**
  - P1: cheese, 8 traits of successful people, support for Hitler, coffee, naps, playing an instrument, sugar, motivation, study tips, suspenseful writing.
  - P2: practice, talking to yourself, posture, Chinese zodiac, Berlin Wall, pregnancy, critical thinking, migraine, "every human life", depression.
  - P3: heroes, procrastination, solar desert, Salem witch trials, muscles, water, Kafkaesque, dreams, vitamins, a riddle.
  - P4: a riddle, alcohol, tea, money laundering, History vs Napoleon, antidepressants, the underwater tunnel, Hawking's paradox, heart transplants, managing emotions.
  - [tài liệu chính thức]
- **Structure (P1)** [đã mở file]:
  - 432 notes / 432 cards; one note type, "Basic (English)+".
  - Fields: English, Image, Audio, Type, Word_1–4, Word_Example_1–4, then 21 subtitle-language fields (Arabic … Vietnamese), then Word_Example_1–4_Audio.
  - **Front:** image + autoplaying line audio; the English text is hidden behind a toggle (H key); `{{type:Type}}` dictation box. This is a **listening-first** card.
  - **Back:** English, the chosen subtitle languages (toggleable), chunk glosses, and chunk examples with their own audio.
- **Line audio:**
  - 432/432 notes (100%) have audio present.
  - Median 7.1 s (p25 4.8, p75 8.8, max 25.2).
  - Stereo 44.1 kHz, 320 kbps, Lavc60 / `TSSE=Lavf58.76`. This is the YouTube soundtrack cut per subtitle line, so it is a native recording. TED-Ed animations usually have a music bed under the narration [suy luận, not heard].
- **Chunk examples:**
  - Word_Example_1 is present on 423/432 notes; examples are 9 words median.
  - Example audio is `hypertts-*`, `TSSE=nVoiceTTS@NAVER`, 24 kHz mono. That is **NAVER Clova TTS via HyperTTS**.
  - The glosses and examples read as LLM-generated [suy luận].
- **Sentence length:** median 16 words; 57% ≥15. 132/432 lines contain I/we/you; 8 carry "(Laughter)" or "(Applause)". The "8 traits" video is Richard St. John's TED talk, so some lines are live speech.
- **Translations:** VI 427/432, JA 390/432, ZH-CN 430/432.
  - Quality varies. The Japanese looks like official TED-translator subtitles [suy luận].
  - Some Vietnamese lines read as machine translation (e.g. "deck of that little boat" → "thân máy của thuyền nhỏ").
  - The Dutch on one AnkiWeb sample is word salad.
  - On one sample the ZH_CH field holds only the first clause ("對鄂蘭來說，", also in Traditional script).
  - One Japanese field repeats a line twice.
- **Domains (30 random lines):** science/health 9; history/food culture 7; psychology, motivation and study 6; first-person TED-talk anecdote with humor 7; writing craft 1. No relationship or small-talk dialogue.
- **Samples (verbatim; other subtitle languages omitted):**
  1. `English: A common opinion at the time was that the Third Reich was a historical oddity;<br>a perfect storm of uniquely evil leaders<br>supported by German citizens looking for revenge<br>after their defeat in World War I.` · `Audio: [sound:how_could_so_many_people_support_hitler_007.mp3]` · `Word_1: historical oddity: something unusual in history` · `Word_2: a perfect storm: a rare combination of factors leading to disaster` · `Word_3: looking for revenge: seeking retribution` · `Word_Example_2: The financial crash was caused by a perfect storm of economic missteps.` · `Japanese: 第三帝国は歴史的にいびつな存在であり 第１次世界大戦の敗北に復讐を求める<br>ドイツ市民によって支持された 特異で悪魔的な指導者が<br>引き起こした最悪の事態というのが<br>当時の一般的な見解でした` · `Vietnamese: Một ý kiến phổ biến vào thời điểm đó là Đệ tam Đế chế là một sự kỳ lạ lịch sử;<br>một cơn bão hoàn hảo của các lãnh đạo độc ác độc nhất<br>…` (tags `how_could_so_many_people_support_hitler ted-ed`)
  2. `English: I never went after the money, and it's not that important to me."` · `Audio: [sound:eight_traits_of_successful_people_037.mp3]` · `Word_1: went after: actively pursued` · `Word_2: not that important: phrase for downplaying importance` · `Word_Example_1: He went after his dream job with determination.` · `Chinese_CH: 我从未追逐过金钱`
  3. `English: Broccoli, for example, has no effect,<br>which probably explains<br>why it's so hard to get kids to eat their veggies.` · `Audio: [sound:how_sugar_affects_the_brain_036.mp3]` · `Word_1: for example: phrase introducing illustration` · `Word_2: so hard to: emphasizes difficulty` · `Japanese: 例えばブロッコリーには何も作用がありません<br>だから子供たちに野菜を 食べさせるのは難しいのかもしれません<br>だから子供たちに野菜を 食べさせるのは難しいのかもしれません` (note the duplicated Japanese line) · `Vietnamese: Ví dụ, bông cải xanh,<br>có lẽ điều đó giải thích<br>tại sao rất khó để cho trẻ ăn rau.`
  4. (from the random list) `It turns out that while listening to music engages the brain in some pretty interesting activities, playing music is the brain's equivalent of a full-body workout.`
- **Score:** ~77 ±6. Best available pre-made "long sentence + real audio + chunks + VI/JA" deck. Limited to the explainer register.

### 3.2 逐句精听TED / 【视频跟读】TED series — real talks, presentation register
- **Series on AnkiWeb** [tài liệu chính thức]:
  - 499194989 Amy Cuddy, "Your Body Language May Shape Who You Are": 255 notes, 103 MB.
  - 159376863 Julian Treasure, "How to speak so that people want to listen": 158 notes.
  - 2070886245 Lera Boroditsky, "How language shapes the way we think": 164 notes.
  - 1988506665 Robert Waldinger, "What makes a good life?": 107 notes.
  - All updated 2025-10, audio count shows "None" because the media are MP4.
  - The descriptions promise "卡片背面: 对应的中英文字幕" (Chinese and English subtitles on the back) [quảng cáo]. In the Amy Cuddy deck the Translation field is **empty on all 255 notes** [đã mở file]. On 2070886245 the AnkiWeb samples show an advertising string in Translation ("同学，这个资源是免费的…加qq群…") [tài liệu chính thức].
- **Structure (Amy Cuddy)** [đã mở file]:
  - Note type "Aisten Sentence QA_2025-09-22". Fields: Audio, Sentence, Translation, Note, Backlink, Source.
  - Front = `{{Audio}}` only, i.e. **listening-first** with the video clip. Back = sentence (+ empty Source, Translation and Note).
  - The template loads marked.js from cdnjs to render the Note field.
- **Audio:** 255/255 (100%) MP4 clips; median 4.2 s (p25 2.3, p75 6.1, max 18.6); audio-track timescale 44.1 kHz. The speech is the speaker's own (native US).
- **Sentence length:** median 12 words; 40% ≥15.
- **Transcript style:** verbatim with disfluencies ("Um", "what what what"), suggesting ASR or auto-captions [suy luận]. There are merge errors such as `they're being judged.ges are trained…`.
- **Domains (30):** psychology research explanation ~16; personal story, emotion and impostor feelings ~7; direct audience address and rhetorical moves ("So I want to ask you first…", "Give it away.") ~7.
- **Samples (verbatim):**
  1. `Audio: [sound:DA63F2A5-A215-47A8-B1F7-6B992972F070.mp4]` · `Sentence: There's some evidence that they do.`
  2. `Audio: [sound:1538BB54-7B24-4C76-8461-C230E38CE4C2.mp4]` · `Sentence: It's five minutes long, they are being recorded, they're being judged.ges are trained to give no non-verbal feedback.`
  3. `Audio: [sound:8139878D-0E2D-4D54-893F-EC7D718065F3.mp4]` · `Sentence: So in the animal kingdom, they are about expanding.`
  4. (random list) `We're gonna come back to that in a few minutes, and I'm hoping that if you sort of learn to tweak this a little bit, it could significantly change the way your life unfolds.`
- **Score:** ~66 ±7. Unique as the verified real presentation and speech source. Small per deck and no translation.

### 3.3 (Cún) [Shadowing] A philosophical inquiry from Ted (P1/P2) — Vietnamese shadowing decks
- **Basics** [tài liệu chính thức]: P1 444003606, 372 notes / 372 audio, 176 MB; P2 1397881535, 321 notes, 204 MB; both updated 2026-04-09. Creator watermark "carles._cun" (TikTok/Facebook links in the template). The description targets B1→C1 [quảng cáo] and stresses "Audio thật từ TED", i.e. real TED audio rather than a robot voice.
- **Structure (P1)** [đã mở file]:
  - Note type "(Cún) -00- [English] Listening only Gif". Fields: Audio (plain filename), Audio gốc (`[sound:]`), Sentence (word-timed `<span data-start data-end>`), Sentence1 (plain), Meaning (VI), Gif, Youtobe link.
  - One template, "[Listening]". It is a custom HTML5 player with speed buttons (0.5×–…) and a seek bar. Words are masked until clicked; clicking replays from that word's timestamp.
  - Listening and shadowing first.
- **Audio:**
  - 372/372 (100%); median 6.7 s (p25 4.9, p75 8.6, max 14.0).
  - 16 kHz mono, 40 kbps, Lavc62. This is original TED-Ed audio, heavily downsampled [đã mở file].
  - Word timestamps plus spelling errors suggest a Whisper-style ASR transcript, not official subtitles [suy luận].
- **Sentence length:** median 16 words; 61% ≥15.
- **Accuracy problems:**
  - ASR and spelling errors: "It may seem like attempting offer" (tempting offer); "Xeno of Cyprus" (Zeno of Citium); "Diogenies'"; "re -imagined"; "self -centered".
  - P2 has an Audible sponsor line as a card ("Every free trial created through this link encourages audible…", AnkiWeb sample).
  - The Vietnamese reads as MT in places [suy luận].
- **Domains:** 100% philosophy narration (TED-Ed "philosophy" series). Emotionally rich vocabulary (love, loneliness, anger in P2), abstract argument.
- **Samples (verbatim):**
  1. `Audio gốc: [sound:The philosophy of stoicism_audio_25.mp3]` · `Sentence1: After his release and eventual victory, Mandela stressed peace and reconciliation, believing that while the injustices of the past couldn't be changed, his people could confront them in the present and seek to build a better, more just future.` · `Meaning: Sau khi được trả tự do và chiến thắng cuối cùng, Mandela nhấn mạnh hòa bình và hòa giải, tin rằng mặc dù những bất công trong quá khứ không thể thay đổi nhưng người dân của ông có thể đương đầu với chúng trong hiện tại và tìm cách xây dựng một tương lai tốt đẹp hơn, công bằng hơn.` · `Youtobe link: https://youtu.be/R9OCA6UFE-0?si=2XRrk-YEGi78EsyF` · `Sentence: <div class="speaker-block" style="line-height: 2.0;"><span data-start="0.0" data-end="0.64"> After</span> <span data-start="0.64" data-end="0.84"> his</span> …`
  2. `Audio gốc: [sound:Why do we love_audio_30.mp3]` · `Sentence1: Siddhartha Gautama, who became known as the Buddha or the Enlightened One, probably would have had some interesting arguments with Russell.` · `Meaning: Siddhartha Gautama, người được mệnh danh là Đức Phật hay Đấng giác ngộ, có lẽ đã có một số tranh luận thú vị với Russell.`
  3. `Audio gốc: [sound:The philosophy of cynicism_audio_29.mp3]` · `Sentence1: Diogenies' ideas have been adopted and re -imagined over and over again.` · `Meaning: Ý tưởng của Diogenies đã được áp dụng và tưởng tượng lại nhiều lần.`
  4. (random list) `Though we might never know why we fall in love, we can be certain that it'll be an emotional roller coaster ride.`
- **Score:** ~66 ±6. Excellent shadowing UI and long sentences; transcript accuracy and audio fidelity are the weak points.

### 3.4 [English - Vietsub] Anki TED-ED song ngữ Anh-Việt (P1–P3, creator "socialge")
- **Basics** [tài liệu chính thức]:
  - P1 1918837902: 2,061 notes / 1,029 audio, 121 MB.
  - P2 1250980978: 1,033 notes / 557 audio.
  - P3 866780035: 871 notes / 1,257 audio.
  - All updated 2023-08-24. Guide at socialge.wordpress.com. Built for IELTS academic vocabulary.
- **Structure (P1)** [đã mở file]:
  - Two note types, 1,030 + 1,031 notes, with identical fields: Eng (cloze), Audio, Img, Meaning (Cambridge definition), Viet, Other.
  - "Cloze Dictate": front = audio + screenshot + Vietnamese + Meaning + type-in cloze. This is **listening/dictation first**.
  - "Cloze Vocabulary": front has no audio (reading cloze).
  - 40 subdecks: one `_voca` and one `_dictate` per video.
- **Audio:**
  - 1,030/1,030 dictation notes (100%); median 4.3 s (p25 3.4, p75 6.0).
  - Stereo 44.1 kHz, 128 kbps, `TSSE=Lavf57.82`, `TCON=Speech`.
  - Filenames carry subtitle timestamps (e.g. `The_truth_about_bats_1_0.0.10.218-0.0.22.686.mp3`). These are subs2srs-style cuts of the original soundtrack.
- **Sentence length:** median 13 words; 39% ≥15. Many lines are subtitle fragments ("to {{c1::consistently}} generate more power each year.").
- **Samples (verbatim):**
  1. `Eng: OCD is considered a neurobiological {{c1::disorder}}.` · `Audio: [sound:myths_of_OCD_1_0.2.58.765-0.3.02.236.mp3]` · `Img: <img src="myths_of_OCD_1_0.3.00.501.jpg">` · `Viet: OCD được coi là một loại rối loạn sinh học thần kinh.`
  2. `Eng: The moment they had been waiting for came on {{c1::March 15}}.` · `Audio: [sound:conspiracy_1_0.2.58.185-0.3.01.706.mp3]` · `Viet: Thời khắc mà họ chờ đợi đã đến, vào ngày 15 tháng 3.`
  3. `Eng: to {{c1::consistently}} generate more power each year.` · `Audio: [sound:power_plant_1_0.4.50.659-0.4.54.509.mp3]` · `Meaning: (Adj)&nbsp;in a way that does not change` · `Viet: tạo ra nhiều điện hơn mỗi năm.`
  4. (random list) `He {{c1::claimed descent from}} Lucius Junius Brutus, {{c2::who had helped}} {{c3::overthrow the tyrannical king}} known as Tarquin the Proud.`
- **Score:** ~64 ±6.

### 3.5 英語例文 暗唱・スピーキング練習デッキ (1190669808) — speaking drill
- **Basics:** 1,000 notes / 1,000 audio, 38 MB, updated 2026-02-25. The description claims "B1〜C1位の１０００例文" (about B1–C1) and says the front shows an image, three cue words and audio [tài liệu chính thức].
- **Structure** [đã mở file]:
  - Note type "StashLog English Stash". Fields: Sentence, Translation (JA), IPA, Cue, Audio, Image, Note.
  - Front = image + cue chips + audio; back = sentence, Japanese, IPA, notes.
  - **The Image field holds bare filenames (e.g. `deck_20250803_192411_meeting_date_confusion.jpg`) and the package contains no images**, so the visual cue is missing.
- **Audio:** 1,000/1,000 (100%); median 3.6 s; 24 kHz mono (953 MP3 + 47 WAV). Filenames are generated from the sentence text. This is TTS [suy luận from format and naming; service not identifiable].
- **Sentence length:** median 11; 7% ≥15. Many grammar-pattern tags (inversion, future perfect continuous, causative). This is textbook or LLM style [suy luận].
- **Samples (verbatim):**
  1. `Sentence: I thought the meeting was today. Actually, it&#x27;s scheduled for tomorrow.` · `Translation: 会議は今日だと思っていました。実は、明日に予定されています。` · `Cue: thought ,meeting ,today` · `Audio: [sound:deck_20250803_192411_I_thought_the_meeting_was_today._Actually_it_s_scheduled_for_tomorrow..mp3]` (tag `Actually,`)
  2. `Sentence: This report deals with the effects of climate change on agriculture.` · `Translation: この報告書は気候変動が農業に及ぼす影響を扱っている。` · `IPA: /ðɪs rɪˈpɔːrt diːlz wɪð ði ɪˈfɛkts əv ˈklaɪmət tʃeɪndʒ ɒn ˈæɡrɪˌkʌltʃər/`
  3. `Sentence: If she had taken that job, she would be living abroad now.` · `Translation: その仕事を受けていたら今海外に住んでいただろう。` · `Cue: taken ,job ,would` (tag `conditional Mixed`)
- **Score:** ~57 ±6.

### 3.6 duo3.0 日本語例文 音声付き（音声更新ver）(1973703622)
- **Basics:** 560 notes / 559 audio, 34 MB, +144/−1 votes, updated 2021-08-15. The description says the audio was "updated to sound more natural" than an earlier upload (2099827505) [tài liệu chính thức]. **New versus round 1**, which found no DUO deck with audio.
- **Structure** [đã mở file]: Front (EN), Back (JA), Sound. The single template shows **Japanese on the front**, with English and audio on the back. That is Japanese→English production, not listening-first.
- **Audio:** **Azure TTS** (filenames `azure-…mp3`), 24 kHz mono, 96 kbps, LAME3.100; median 4.7 s; 100%.
- **Sentence length:** median 12; 26% ≥15. Dense collocations and idioms, many mini-dialogues. There is a typo in an AnkiWeb sample ("anytmore").
- **Samples (verbatim):**
  1. `Front: What do you do? "I'm a college student, a freshman at Harvard." "What's your major?" "Philosophy."` · `Back: 「普段は何をなさっているんですか？」 「大学生です。ハーバードの1年です。」 「専攻は？」 「哲学です。」` · `Sound: [sound:azure-a3fec1cb-50e3e522-ff053f4c-d2de1528-7ec70d7f.mp3]`
  2. `Front: Don't beat around the bush! What am I supposed to do? "Just wait and see. Time will tell."`
  3. `Front: A senior official is suspected of accepting bribes from a company, but there isn't sufficient evidence to arrest him.` · `Back: ある政府高官が企業から賄賂を受け取った容疑をかけられている。しかし、逮捕するには証拠が不十分だ。`
- **Score:** ~56 ±6. Book content is copyrighted, so takedown risk applies [suy luận].

### 3.7 English. C1 Words, Idioms, Phrasal Verbs. American Accent. (524918335) — already in `chung/raw/`, now inspected
- **Structure** [đã mở file]:
  - 1,731 notes. Fields: Front (sentence with partial-letter `<b>` hints), Back (word), Definition, Audio, Example Audio.
  - Front shows sentence + definition (reading cloze); audio only on the back.
- **Audio:** HyperTTS (`hypertts-*`). Sentence audio is 24 kHz mono 160 kbps, median 2.7 s, 100%. Word audio is 44.1 kHz (`TSSE=Lavf60.16`), median 0.9 s.
- **Sentences:** median 10 words; 8% ≥15. Invented. Strong slant toward creator and IT work (render, storyboard, sprint, workflow, Slack) and youth slang (slay, stan, glow up, lit, main squeeze).
- **Samples (verbatim):** `Front: “That old design looks c<b>lappe</b>d compared to the new one.”` · `Back: clapped` · `Definition: unattractive / bad` | `Front: “The party was l<b>i</b>t last night.”` · `Back: lit` · `Definition: amazing, exciting` | `Front: “I’m ready to get my feet wet with motion graphics.”` · `Back: get your feet wet` · `Definition: try something new`.
- **Verdict:** target list; ~55. Codex also measured this package (`chung/kiem_chung_Codex_vong1/c1-american/`).

### 3.8 Kendra's Language School 连读 deck (1364160335) — already in `chung/raw/`, now inspected
- **Structure** [đã mở file]:
  - 332 notes. Fields: 序号 (number), 常速 (normal speed), 慢速 (slow), 图片 (image), 备注 (notes). **The English text exists only inside the JPG**, together with Chinese, so it is not searchable.
  - Front = normal-speed audio; back = slow audio + image.
- **Audio:** normal median 2.6 s; slow median 2.8 s; stereo 44.1 kHz, 64 kbps, Lavc58. A video-soundtrack extract of a native US teacher.
- **Samples (verbatim fields + image text I viewed):**
  - `序号: 0026` · `常速: [sound:0026-2.mp3]` · `慢速: [sound:0026-3.mp3]` · `图片: <img src="0026.jpg">`. Image: "What did he say?" / 他说了什么?
  - 0167: "It was great." / 非常精彩。
  - 0280: "Give me a hand." / 帮我一下。
- **Verdict:** 3–4-word phrases; useful only as a connected-speech warm-up; ~48.

### 3.9 Illustrated Everyday Idioms with Stories (Kelciour sample, 665597838) — checked, rejected for level
- **Contents** [đã mở file]:
  - 120 notes. Fields: Phrase, Meaning, Example 1/2, Dialogue, Caption, Illustration, and six audio fields.
  - Phrase, example, caption and dialogue audio are publisher recordings (`TPE1=Compass Media`, `TIT2=Everyday Idioms 1-06`; 22 kHz stereo). The dialogue median is 6.6 s.
  - Meaning audio is Azure TTS (the description names "English (UK) Libby (Neural)").
  - The full 600-note version is sold via hipolink [tài liệu chính thức].
- **Sample:** `Phrase: drop off` · `Dialogue: A: Where are you going?B: I’m going to drop off my rollerblades at Sue’s house. She is going to use them tomorrow.` · `Audio Dialogue: [sound:6.mp3]` (AnkiWeb sample).
- **Sample:** `Phrase: be fond of` · `Example 1: Romeo and Juliet <b>were</b> very <b>fond of</b> each other.` · `Dialogue: A: Have you heard of Picasso?<br>B: Yes, I <b>am fond of</b> his paintings.` [đã mở file]
- **Sample:** `Phrase: at any time` · `Caption: She may give birth <b>at any time</b>.`
- **Verdict:** native recordings and a clean design, but A2–B1 idioms.

---

## 4. Rejected or deprioritised (one line each)
- **Kingdom Come: Deliverance — English Dialogues** (AnkiWeb 1815005512): original game voice acting (.ogg), but 23,169 notes against only 2,375 audio files (≤10% coverage), medieval register, Portuguese translation. [tài liệu chính thức]
- **BBC English Plus** (1870416180): 676 beginner sentences ("Bakers make bread."), Portuguese, 2018. [tài liệu chính thức]
- **English conversational connectors** (1603189802): useful idea (discourse connectors), but 155 notes / 113 audio, audio type unknown, 2023. Small; possible target list. [tài liệu chính thức]
- **Illustrated Everyday Expressions with Stories** (1423879629 Vietnamese version, +71; 1529703377 and 1851481059, Books 1–2): same Compass series as 3.9; A2–B1. [tài liệu chính thức]
- **ネイティブがよく使う英会話表現ランキング** (461623741): 1,422 short conversation expressions with audio, 3 per situation, Japanese prompts. Phrases, not long sentences. Audio type not checked. [tài liệu chính thức]
- **必ずものになる 話すための英文法 Step 7［上級編］** (921553106): 110 sentences + Japanese + audio from an e-book. Small, and the deck itself says it needs the book. [tài liệu chính thức]
- **英検1級パス単 AI例文** (1107102763) and **TOEFL3800 例文** (1579676728): LLM sentences with Google TTS; target lists only. [tài liệu chính thức]
- **English C1 Advanced (CAE) exam preparation** (1795462055): 87 notes, no audio. [tài liệu chính thức]
- **"English B1–B2: Essential Conversation Chunks for Fluency"** (41856907): 485 chunks, no audio, Spanish. [tài liệu chính thức]
- **Anglais — Français thématique 1–6** (2428949188 and siblings, +89): native British volunteer recordings, but at word or phrase level, with French as the base language. [tài liệu chính thức]
- **4000 Essential English Words, Oxford 3000, English Profile Vocabulary (697931574), AWL, GRE and Magoosh decks:** word lists. Not opened.
- **"English Conversation - audio deck for begining students" (1781884134), "English File Elementary / Pre-int", "ESL 1 Unit 1":** beginner level.
- **Kelciour "My English Anki Decks Collection v2"** (hipolink, $10 against a listed $19.99): the page lists no contents. [tài liệu chính thức] The TV and film subs2srs decks known from round 1 are presumably inside, but this is [chưa xác minh].

---

## 5. Gaps and next steps
- **Rerun AnkiWeb title search after the daily reset.** Use `scratchpad/scripts/r2-en/queries_pri.txt` with `AW_GAP=20` and stop on the first 429.
  - High-value queries never run: sitcom, Friends, movie/film, subs2srs, interview, speech, debate, Netflix, slang, idiom, phrasal, "English conversation", 英会話, 海外ドラマ, 映画, フレーズ, 美剧, 老友记, 口语, 演讲, 地道, tiếng Anh, giao tiếp, Vietsub, song ngữ, Cún, GLASSY.
  - The last two would reveal other decks by these two creators, e.g. whether Glassy-Gaia's 13 Reasons Why or Despicable Me decks also exist free on AnkiWeb.
- **Not done:**
  - Codex's queue asked Claude for AnkiWeb metadata on NHK decks 620593953, 1192131968 and 1123167619. They are Japanese, outside this English task, and not done.
  - Codex's `codex-en-glassygaia-p4` and `codex-en-socialge-teded-p3` folders contain only `_meta.json` (no .apkg) as of 11:51. My `en-glassygaia-teded-p1` and `en-vietsub-teded-p1` are other parts, so there are no duplicates.
- **Self-mining tools** for domains no deck covers (podcasts and interviews), new since round 1: **audio2anki** (osteele; Whisper transcription + segmentation + audio snippets; accepts an existing transcript) and **LingoAnki**. Both are [chưa xác minh], from search snippets.

---

## 6. Sources
- **AnkiWeb deck pages** (data via logged-in `item-info`; downloads via `download-deck`):
  - Glassy-Gaia TED-Ed: [635719672](https://ankiweb.net/shared/info/635719672), [994314683](https://ankiweb.net/shared/info/994314683), [1941960573](https://ankiweb.net/shared/info/1941960573), [210221519](https://ankiweb.net/shared/info/210221519)
  - 逐句精听TED / 视频跟读TED: [499194989](https://ankiweb.net/shared/info/499194989), [159376863](https://ankiweb.net/shared/info/159376863), [2070886245](https://ankiweb.net/shared/info/2070886245), [1988506665](https://ankiweb.net/shared/info/1988506665)
  - Cún TED-Ed philosophy: [444003606](https://ankiweb.net/shared/info/444003606), [1397881535](https://ankiweb.net/shared/info/1397881535)
  - socialge Vietsub TED-Ed: [1918837902](https://ankiweb.net/shared/info/1918837902), [1250980978](https://ankiweb.net/shared/info/1250980978), [866780035](https://ankiweb.net/shared/info/866780035)
  - Japanese sentence decks: [1190669808](https://ankiweb.net/shared/info/1190669808), [1973703622](https://ankiweb.net/shared/info/1973703622)
  - Already in `chung/raw/`: [524918335](https://ankiweb.net/shared/info/524918335), [1364160335](https://ankiweb.net/shared/info/1364160335)
  - Kelciour idioms sample: [665597838](https://ankiweb.net/shared/info/665597838)
  - Japanese AI and LLM target lists: [1107102763](https://ankiweb.net/shared/info/1107102763), [1579676728](https://ankiweb.net/shared/info/1579676728)
  - Rejected: [1815005512](https://ankiweb.net/shared/info/1815005512), [1870416180](https://ankiweb.net/shared/info/1870416180), [1603189802](https://ankiweb.net/shared/info/1603189802), [1423879629](https://ankiweb.net/shared/info/1423879629), [1851481059](https://ankiweb.net/shared/info/1851481059), [461623741](https://ankiweb.net/shared/info/461623741), [921553106](https://ankiweb.net/shared/info/921553106), [1795462055](https://ankiweb.net/shared/info/1795462055), [41856907](https://ankiweb.net/shared/info/41856907), [2428949188](https://ankiweb.net/shared/info/2428949188)
- **Downloaded packages (this round):** `chung/raw/en-glassygaia-teded-p1`, `en-cun-ted-philosophy-p1`, `en-vietsub-teded-p1`, `en-zh-ted-amycuddy-video`, `en-jp-reigun-anshou-speaking`, `en-jp-duo30-audio`, `en-kelciour-idioms-stories-sample`. Each has a `_meta.json`.
- **Glassy-Gaia GitHub:** [GLASSY-GAIA/youtube-ted-ed-anki-english-en](https://github.com/GLASSY-GAIA/youtube-ted-ed-anki-english-en). Repo list via the GitHub API: there is no English Netflix repo, only `little-fox-stories-anki-english-en`.
- **Other creators' pages:**
  - socialge guide: [socialge.wordpress.com Part 1 guide](https://socialge.wordpress.com/2023/03/24/tai-nguyen-anki-ted-ed-song-ngu-anh-viet-part-1-remake-ver/)
  - Kelciour collection: [hipolink: My English Anki Decks Collection v2](https://hipolink.net/kelciour/products/my-english-anki-decks-collection-v2)
- **AnkiWeb forum thread** (led to the CAE deck): [My English learning and self-development decks support](https://forums.ankiweb.net/t/my-english-learning-and-self-development-decks-support/14733)
- **Tools:**
  - [osteele/audio2anki](https://github.com/osteele/audio2anki)
  - [jonathanfox5/gogadget](https://awesome.ecosyste.ms/projects/github.com%2Fjonathanfox5%2Fgogadget)
  - [lbesnard/LingoAnki](https://awesome.ecosyste.ms/projects/github.com%2Flbesnard%2Flingoanki)
- **Coordination files read:** `chung/ung_vien_Codex.md`; `chung/raw/codex-*/_meta.json`; the Japanese researcher's search log `scratchpad/out-r2ja/s1.txt`.
