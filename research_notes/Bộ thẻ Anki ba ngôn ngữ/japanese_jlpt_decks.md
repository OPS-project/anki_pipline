# Japanese JLPT-organized Anki decks (N5–N1) with full-sentence audio — N2→N1 focus

State as of 2026-11-13. Learner: Vietnamese IT/DX engineer in Japan, JLPT N2, preparing N1, uses Japanese daily at work, ultimately wants natural, articulate spoken Japanese. Priority update from the user (applied throughout): book-style N1 decks (short invented sentences in word-list order) do NOT meet the goal; N1 decks are judged mainly on whether their sentences are realistic, natural and long enough for real-world comprehension, with native full-sentence audio. N5–N4 and N3–N2 are kept brief, as foundation reference.

Evidence labels: [VERIFIED-INSPECTED] = I downloaded/read the .apkg myself (scripts in the scratchpad; method in the Sources section); [VERIFIED-DOCS] = official README / release notes / AnkiWeb's own metadata API; [COMMUNITY] = user reviews/reports; [MARKETING] = creator promo only; [UNVERIFIED] = not confirmed. I cannot listen to audio, so nothing here judges naturalness or pitch by ear. Durations come from MP3 frame headers, Ogg granule positions or WebM headers.

How AnkiWeb data was read: AnkiWeb pages are JavaScript-rendered, so I called AnkiWeb's own public endpoint (`/svc/shared/item-info?sharedId=<id>`). It returns title, last-updated, thumbs up/down, reviews, note count, **audio-file count**, image count and 3 sample notes. I checked the counts against my own inspection of Kaishi: AnkiWeb reports 1,501 notes / 2,972 audio / 1,382 images, and my .apkg inspection gives 1,501 notes / 2,972 mp3 / 1,382 images (1,331 webp + 35 png + 16 jpg). AnkiWeb downloads and searches returned HTTP 429 (rate-limited) for the whole session, so I could not inspect any AnkiWeb-only deck file; those are labelled [VERIFIED-DOCS] from metadata.

---

## Top findings & recommended shortlist

### Takeaway
I found **no ready-made, JLPT-level-organized N1 deck whose sentences come from authentic real-life sources (drama/anime/news/business) with native full-sentence audio.** Every level-organized N1 deck I could verify uses either textbook sentences (JLPT Tango book, 新完全マスター/新完全掌握) or dictionary-style phrases. Where they have sentence audio, it is either the publisher's native narration of short textbook sentences or neural TTS (VOICEPEAK, VOICEVOX). So under the user's updated criteria, **no deck in my scope qualifies as a primary "real-life comprehension" deck.** The real-life sentence deck has to come from the authentic-media track, which another researcher covers. The decks below are best used as a light N1 **scaffold** next to that deck.

### Cited Findings — shortlist (scores are preliminary /100; details in the per-deck entries)

| Rank | Deck (band) | Full-sentence audio? | Sentence style | Role for this learner | Score |
|---|---|---|---|---|---|
| 1 | **Ankidrone Essentials V9 – JLPT Tango N1 / N2 subdecks** (N1 vocab) | YES, 100% of N1 (2,023/2,023) and N2 (1,659/1,659) notes have a sentence-audio file present, and all refs resolve in the media map. Native publisher narration, WebM/Opus, sentence clips median ~4.0 s (N1) / 4.5 s (N2) vs ~0.8 s for word clips [VERIFIED-INSPECTED] | Textbook (JLPT Tango book), median 18 chars, 0% ≥30 chars | **Reference / scaffold only. Textbook-style, so it does not meet the user's goal.** Best verified N1 vocabulary deck with native sentence audio. | ~60 |
| 2 | **新完全掌握 N1 语法例句 (mxggle)** (N1 grammar) | YES, 343/343, but **VOICEVOX TTS** (WhiteCUL voice) [VERIFIED-INSPECTED + VERIFIED-DOCS] | Textbook (Shin Kanzen Master N1 grammar), but multi-clause: median 32 chars, 66% ≥30 chars | **Reference only (book + TTS).** It is still the only N1 grammar deck I could verify that has full-sentence audio. Chinese explanations, plus an English meaning per pattern. | ~57 |
| 3 | **Core 2k/6k [Pitch Graphs, Optimized, Links]** (N4→N2, some N1) | Very likely YES: 11,910 audio files for 5,996 notes, and the sample note has a "Sentence Audio" field. iKnow audio by "two popular Japanese voice talents" [VERIFIED-DOCS]. Not inspected (AnkiWeb 429). | iKnow-written sentences, short | Consolidation / scaffold. Includes some business vocabulary. | ~55 (±10) |
| 4 | **Kaishi 1.5k v2.4.3** (N5–N4 foundation) | YES, 1,500/1,501 notes, all 1,477 files present, median 2.7 s [VERIFIED-INSPECTED]. 294 clips are ASK Publishing (JLPT Tango) narration per ID3 tags; the rest are Core-derived per the README (inference); no TTS indicators. | Textbook/Core, median 13 chars | Foundation reference only. Too easy for an N2 learner. | ~58 for this learner (it would score much higher for a beginner) |
| 5 | **【egg rolls】JLPT N1-N5 一万词 v3.5** (N5–N1 vocab, Chinese) | Every note has example audio, but it is **VOICEPEAK TTS**, and N1 examples are mostly phrase fragments (median 8 chars, 0% end in 。) [VERIFIED-INSPECTED] | Collocation/phrase snippets | **Does not meet the hard rule** (not full sentences). Possible collocation scaffold, but only if the learner reads Chinese. | ~50 |

- Hard-rule check: by the user's rule (verified complete-sentence audio), only #1, #2 and #4 are inspection-verified. #3 is strongly indicated by metadata but not inspected. #5 fails because its examples are mostly fragments. None of them meets the updated "realistic, natural, long enough" criterion. Each is labelled "reference / scaffold" for that reason.
- **No N1 grammar deck with native sentence audio** was found. These decks have no audio at all, per AnkiWeb metadata [VERIFIED-DOCS]: Jtest4you (4,281 notes), "Japanese Grammar 6500 example sentences" (copied from JLPT Sensei), SKM N2/N3 grammar, and the DOJG deck (no audio mentioned anywhere on its download page). "Japanese Core Grammar JLPT N5-N1 (w/audio)" has 399 audio files for 400 notes, but its author says it was made "with the help of ai", and the audio type could not be verified [VERIFIED-DOCS/UNVERIFIED].
- **Authentic, level-filtered sentences exist only as a tool, not as a deck:** Immersion Kit has 400k+ anime sentences (drama, games, news and literature are being added). Each sentence has a screenshot and the line's audio, results can be filtered by JLPT level, and whole cards can be downloaded for Anki. It is free ([Tofugu resource DB](https://tofugu.com/japanese-learning-resources-database/immersion-kit)) [VERIFIED-DOCS, third-party description]. I found no published, ready-made "Core/Kaishi/N1 list with Immersion Kit sentences" deck [UNVERIFIED that one exists; searches in EN/JA/ZH returned none].
- Copyright: the decks with the best native sentence audio (Ankidrone/Tango, Kaishi's Tango portion, the Core 2k/6k copies) redistribute commercial publisher audio (ASK Publishing, iKnow). Their legal status is grey to unlicensed [VERIFIED-INSPECTED ID3 tags "アスク出版 / ASK PUBLISHING"; [Tatsumoto Tango N1 page](https://tatsumoto.neocities.org/blog/jlpt-tango-n1-anki-deck): audio "downloaded from the publisher's website"].

### Inferences
- Practical stack for this learner: (a) a real-life sentence deck from the authentic-media track as the **primary**; (b) **Ankidrone Tango N1** as the N1 vocabulary scaffold. Suspend cards for words already known from work, and use its native sentence audio only for word-in-context listening. (c) **mxggle 新完全掌握 N1 grammar** as a grammar pattern reference, read for structure and not used as a listening model, because the audio is TTS. Kaishi and Core 2k/6k would mostly duplicate what an N2 holder already knows. Use them only to patch gaps.
- Overlap and duplication: Kaishi and Core 2k/6k overlap heavily, since Kaishi was built from Core2k, Core10k, Tango N4 and Tango N5. Ankidrone N1 and eggrolls N1 overlap in vocabulary but not in sentences. A scaffold deck will not duplicate an authentic-media deck's sentences, only some headwords. Use the Anki "suspend if known" approach rather than importing two full N1 vocab decks.
- For speaking: none of these decks teaches register switching (敬語/タメ口) or business set phrases systematically. The closest are eggrolls' collocations (Chinese glosses only) and the iKnow Core sentences, which include some business vocabulary.

### Gaps
- Could not download or inspect any AnkiWeb-only deck (Core 2k/6k, Core Grammar w/audio, GameGogakuen, Ankidrone Foundation) because of HTTP 429 all session. Their audio type and durations are inferred from metadata only.
- Could not find any existing Anki deck for 日本語単語スピードマスター, 新完全マスター語彙 N1, 総まとめ N1 語彙, 红宝书 or 蓝宝书 with sentence audio. Searches in English, Japanese, Chinese and Vietnamese turned up nothing verifiable. Either none exist publicly or they are not indexed. Try/TRY! N1 and Bunpro-derived exports with audio: none found. Bunpro's own N2/N1 vocab-cloze audio is Microsoft Azure TTS and stays inside the Bunpro app ([Bunpro forum](https://community.bunpro.jp/t/n2-and-n1-vocab-cloze-update-aug-29-2024/99138)).
- Core 10k / "Ultimate Core 10k": the Reddit post could not be fetched (403), so it is unverified.

---

## Per-deck entries — N1 band (vocabulary & grammar)

### Takeaway
For N1 vocabulary, the only verified deck with native full-sentence audio is Ankidrone Essentials' JLPT Tango N1, which is textbook-style. For N1 grammar, the only verified deck with full-sentence audio is mxggle's 新完全掌握 N1 grammar, which uses TTS. Both are scaffolds, not real-life comprehension decks.

### Cited Findings

#### A. Ankidrone Essentials V9 — JLPT Tango N1 (and N2) subdecks
- **Exact name / creator / URL:** "Ankidrone Essentials V9.apkg". Maintained by Tatsumoto Ren (AJATT-Tools community). N1 was made by a volunteer team; N5/N4 came from "Anonymous from DJT" and N3 from Perditio ([Ankidrone Essentials page](https://tatsumoto.neocities.org/blog/ankidrone-essentials)) [VERIFIED-DOCS]. Download: Yandex Disk folder `disk.yandex.com/d/adEb8n9uhOacHw`, mirror on Telegram `t.me/ajatt_tools/60` (same page).
- **Version / updated:** V9 file is 163,517,435 bytes, modified 2026-08-22 according to the Yandex public API [VERIFIED-INSPECTED]. The page shows "updated October 26, 2026". The changelog listed on that page only goes up to v8 (typo fixes in N1/N2, updated audio, katakana words suspended) [VERIFIED-DOCS]. **Actively maintained.**
- **Counts [VERIFIED-INSPECTED]:** note type "Japanese sentences", 7,718 notes, plus 6 "Ankidrone Info" README notes. Cards per subdeck: Tango N5 1,077 · N4 914 · N3 2,045 · N2 1,659 · **N1 2,023**. 225 cards are suspended by default.
- **Fields [VERIFIED-INSPECTED]:** SentKanji, SentFurigana, SentEng, SentAudio, VocabKanji, VocabFurigana, VocabPitchPattern, VocabPitchNum, VocabDef, VocabAudio, Image, Notes, MakeProductionCard, Focus.
- **Sentence audio [VERIFIED-INSPECTED]:** N1 has 2,023/2,023 notes with a SentAudio file, N2 1,659/1,659, N4 914/914, N3 1,444/2,045, N5 931/1,077. Every N1 note also has VocabAudio. All audio is **.webm** (Opus in WebM), with files named `N1_0877_2.webm` (sentence) and `N1_0877_1.webm` (word). Source: native narration from the book's publisher. Per the [Tango N1 page](https://tatsumoto.neocities.org/blog/jlpt-tango-n1-anki-deck), "You can download audio recordings for all the sentences in the book from the publisher's website" [VERIFIED-DOCS]. All 2,058 N1 sentence-audio refs resolve to files in the media map. N1 sentence clips have a median of 4.00 s (sample of 15; range 1.63–5.52 s), against 0.78 s for word clips, so the sentence clips are full-sentence recordings [VERIFIED-INSPECTED].
- **Sentence source & style [VERIFIED-INSPECTED]:** sentences come from the book *3000 Essential Vocabulary for the JLPT N1* (JLPT Tango N1). The page says there are "~2000 sentence items" [VERIFIED-DOCS]. Length: N1 median 18 characters, 38% ≥20 chars, **0% ≥30 chars**; 99% end with 。. N2 median 17. These are **single-clause textbook sentences, so the deck is book-style and reference only.**
- **Card template:** bilingual targeted sentence card. The front shows the sentence with the target word highlighted. Filling `MakeProductionCard` turns it into a kana→kanji production card. Furigana and pitch were machine-generated with the AJT add-ons ([N1 page](https://tatsumoto.neocities.org/blog/jlpt-tango-n1-anki-deck); [N2 page](https://tatsumoto.neocities.org/blog/jlpt-tango-n2-anki-deck)) [VERIFIED-DOCS]. Images: N1 240 notes, N2 927 notes [VERIFIED-INSPECTED]. The N1 page says the images came from a Vietnamese Tango deck that was later deleted from AnkiWeb. Pitch: VocabPitchPattern (katakana) and VocabPitchNum filled for 2,016 of the N1 notes [VERIFIED-INSPECTED]. Translations: English.
- **Real sample notes** (obtained by extracting `collection.anki21b` from the V9 .apkg with HTTP range reads; verbatim, HTML stripped) [VERIFIED-INSPECTED]:
  1. N1 · SentKanji: 喘息が酷くなって、息が出来ない。 · SentFurigana: 喘息[ぜんそく]が 酷[ひど]くなって、 息[いき]が 出来[でき]ない。 · SentEng: My asthma has worsened, and I can't breathe. · SentAudio: `[sound:N1_0877_2.webm]` · VocabKanji: 喘息 · Pitch: ゼンソク / 0 · VocabDef: asthma · VocabAudio: `[sound:N1_0877_1.webm]` · Notes: JLPT Tango N1 item 0877 · no image.
  2. N1 · そんな理由では、てんで話にならない。 · EN: That can't be a reason at all. · SentAudio `N1_1683_2.webm` · word てんで, pitch テンデ/0, def "(not) at all; completely; utterly; entirely; altogether".
  3. N1 · 感動で涙が止まらなかったが、所詮架空の話だ。 · EN: I was so moved I couldn't stop crying, but it's only a fictitious story. · SentAudio `N1_1086_2.webm` · word 所詮 (furigana 所詮[しょせん / そせん]), pitch ショセン/0.
  4. N2 (shows an error) · 犬は主人に忠実だ。 · **SentFurigana: 犬[けん]は 主人[しゅじん]に忠実[ちゅうじつ]だ。** This reading is wrong; it should be いぬ. · SentAudio `N2_0870_Chap7-Sec4_2.webm`. Another N2 note has the translation typo "depanment store".
- **Known problems:** machine-generated furigana errors. The authors admit this ("readings may contain errors"; [N2 page](https://tatsumoto.neocities.org/blog/jlpt-tango-n2-anki-deck)), and I found one myself (above) [VERIFIED-INSPECTED]. iOS: AnkiMobile plays only formats iOS supports. Anki forum threads say Ogg/Opus does not play on iOS, and Opus works only in .caf or MP4 containers ([Anki forum: Ogg in AnkiMobile](https://forums.ankiweb.net/t/ogg-files-suported-in-anki-mobile/4171); [Anki forum: Opus/CAF](https://forums.ankiweb.net/t/opus-caf-audios-no-longer-working-with-newer-ffmpeg-and-sharex/43962)) [COMMUNITY]. A reviewer of the sister deck Ankidrone Foundation says that for iOS "you must run the script below to convert .ogg files to .mp3" (AnkiWeb 917377946 review, 2025-11-27) [COMMUNITY]. **So the .webm audio is likely not to play in AnkiMobile without conversion [UNVERIFIED on V9 specifically]. On desktop and AnkiDroid, Opus is generally supported [UNVERIFIED].** For AnkiDroid, the [JP1K page](https://tatsumoto.neocities.org/blog/jp1k-anki-deck) notes that the sister deck "doesn't work properly in AnkiDroid" without updating and syncing media [VERIFIED-DOCS]. No add-on is required to study the deck.
- **License:** none stated. The site footer reads "Copyright © Tatsumoto Ren 2020-2026". The content redistributes the book's text and audio, so it is a copyright grey area [VERIFIED-DOCS].
- **Score (preliminary): ~60/100**
  - Full-sentence audio 19/25: 100% coverage at N1/N2, native publisher narration, median ~4 s clips. Minus points for short, single-clause clips and the WebM/Opus iOS risk.
  - Naturalness/richness 7/20: invented textbook sentences, single clause, median 18 chars.
  - Suitability N2→N1+ 10/15: real N1 headwords, but the sentence difficulty is low. The book's author says the vocabulary felt easier than expected [UNVERIFIED; that remark appears only in a search snippet].
  - Speaking chunks 6/15: some adverbs and set phrases (てんで話にならない), no register work.
  - Coverage/progression 9/10: clean N5→N1 subdecks, ~7.7k notes.
  - Accuracy/maintenance 6/10: maintained in 2026, but contains furigana errors and typos.
  - Extras 3/5: pitch, production toggle, some images.
  - Uncertainty: ±6.

#### B. 新完全掌握 N1 语法例句｜音频・中文解析 (mxggle) — N1 grammar with full-sentence audio (TTS)
- **URL:** [GitHub mxggle/anki-jlpt-n1-grammar-example-sentences](https://github.com/mxggle/anki-jlpt-n1-grammar-example-sentences); AnkiWeb [925682506](https://ankiweb.net/shared/info/925682506). The README also cites AnkiWeb 1584745637, which is the N2 sibling deck. N2 version: [mxggle N2 repo](https://github.com/mxggle/anki-jlpt-n2-grammar-example-sentences), latest tag 1.7.0.
- **Version / updated:** v2.0.0, released 2026-08-13: "全量内容校订与音频重制". It corrected 246 Japanese sentences and rewrote or fixed 331 Chinese translations ([CHANGELOG](https://raw.githubusercontent.com/mxggle/anki-jlpt-n1-grammar-example-sentences/main/CHANGELOG.md)) [VERIFIED-DOCS]. AnkiWeb copy last updated 2026-10-15, 343 notes, 343 audio, 2 thumbs up [VERIFIED-DOCS]. **Actively maintained.**
- **Counts [VERIFIED-INSPECTED]:** release asset `JLPT_N1_N1__-v2.0.0.apkg` is 15.3 MB. Note type "Japanese Grammar Enhanced Model++ (N1)+", 343 notes / 343 cards, subdecks 新完全掌握N1语法例句::Lesson 01–20.
- **Fields [VERIFIED-INSPECTED]:** FrontSentence (with 【…】 blank), GrammarPattern, LessonInfo, BackSentence, ReadingFurigana (empty in all notes), Translation (Chinese), AudioFile, GrammarFormation, RichGrammarFormation, StyleNotes, ExplanationJapanese, ExplanationChinese, EnglishMeaning, ChineseMeaning, AdditionalNotes, AdditionalNotesZh, VocabularyNotes (empty), DetailedExplanation (Chinese word-by-word analysis), Level, SortOrder. One template: cloze-style front (sentence with the pattern blanked).
- **Audio [VERIFIED-INSPECTED + VERIFIED-DOCS]:** 343/343 notes have audio, and all 343 files are present. Durations (all 343 files): min 2.28 s, **median 5.40 s**, max 9.36 s, so these are full-sentence clips. Format: MPEG-2 Layer III, 24 kHz, 64 kbps. That matches the changelog: "使用 VOICEVOX WhiteCUL（speaker 23）…重新生成全部 343 个 MP3…24 kHz、单声道、64 kbps". **So this is neural TTS (VOICEVOX), not native recording.**
- **Sentence source & style:** the book 《新完全掌握日本语能力考试N1级语法》, the Chinese edition of 新完全マスター文法 N1 (3A Corporation) ([README](https://github.com/mxggle/anki-jlpt-n1-grammar-example-sentences)) [VERIFIED-DOCS]. Length [VERIFIED-INSPECTED]: BackSentence median 32 chars, 66% ≥30 chars, 100% end in 。. These are multi-clause sentences, longer than any vocab deck here, but still invented textbook examples. **Reference only.** StyleNotes labels register, e.g. 硬い言い方 or 話し言葉 (口语).
- **Real sample notes** (from the GitHub v2.0.0 .apkg; verbatim) [VERIFIED-INSPECTED]:
  1. Lesson 19 · Front: 失業している上、子供にもお金がかかり、生活が苦しいこと【…】。 · Back: 失業している上、子供にもお金がかかり、生活が苦しいこと極まりない。 · Pattern: ～極まる・～極まりない · Translation: 不仅失业，而且养孩子也很花钱，生活真是艰难至极。 · Audio `[sound:第19課 - 18_319.mp3]` · StyleNotes: 硬い言い方 · EnglishMeaning: Extremely/Utterly (usually negative).
  2. Lesson 9 · 子供のためとあれば、わたしはどんなことでも我慢しますよ。 · ～とあれば · 如果是为了孩子，无论什么事我都可以忍受。 · `[sound:第9課 - 1_131.mp3]` · EN: If it is the case that~.
  3. Lesson 12 · 犬や猫じゃあるまいし、上の人の言葉に従うだけなんてごめんだ。 · ～ではあるまいし · StyleNotes: 話し言葉 (口语) · `[sound:第12課 - 8_184.mp3]`.
  - No images and no pitch accent in any note.
- **License / known problems:** the README badge says CC BY-NC 4.0, but the GitHub sidebar says MIT. The two conflict. The content is derived from a commercial textbook ("仅供学习交流使用") [VERIFIED-DOCS]. The changelog notes that one 15課 example (～にひきかえ) is missing from the book itself. Explanations are in Chinese, with only a one-line English meaning, so this is a barrier for a learner who does not read Chinese.
- **Score: ~57/100**
  - Audio 14/25: full coverage of whole sentences, but TTS with a single voice.
  - Naturalness 8/20: book sentences, though multi-clause.
  - Suitability 13/15: exactly the N1 grammar syllabus.
  - Speaking 7/15: some spoken-register patterns are flagged.
  - Coverage 6/10: one book, 343 items.
  - Accuracy/maintenance 7/10: full 2026 revision; license conflict.
  - Extras 2/5: word-by-word analysis, Chinese only.
  - Uncertainty: ±5.

#### C. 【egg rolls】JLPT N1-N5 一万词 v3.5 (5mdld) — Chinese-community JLPT vocab deck (N1 portion)
- **URL / creator:** [GitHub 5mdld/anki-jlpt-decks](https://github.com/5mdld/anki-jlpt-decks), "egg rolls", 3,135 stars, last pushed 2026-10-22 [VERIFIED-DOCS via GitHub API]. Release 26.09.06 (2026-09-06): `eggrolls-JLPT10k-v3.5.apkg`, 404.5 MB. Releases come roughly every 1–2 months: 26.04.26, 26.05.15, 26.06.13, 26.07.13, 26.09.06 [VERIFIED-DOCS]. **Very actively maintained.** License CC BY-NC 4.0; the README warns that paid resale on 闲鱼/拼多多 is unauthorized [VERIFIED-DOCS].
- **Counts [VERIFIED-INSPECTED]:** 10,641 notes / 10,641 cards. **N1 4,045** (高频 598 / 中频 1,302 / 低频 2,145), N2 3,215, N3 1,817, N4 757, N5 807. Templates: 日-中 (default) and 中-日 (off by default). Note type has 36 fields: VocabKanji, VocabPitch (e.g. ⓪①), VocabPoS, VocabFurigana, VocabDefSC/TC, VocabPlus, VocabAudio, then up to four example slots (SentType, SentKanji, SentFurigana, SentDefSC, SentDefTC, SentAudio), plus Order and Alt1/Alt2.
- **Audio [VERIFIED-INSPECTED + VERIFIED-DOCS]:** VocabAudio on 10,641 notes; files are named like `真実_シ＼ンジツ_1_NHK-2016-260118.mp3` (NHK accent dictionary) or `…_Shinmeikai-8-…`, sample median 1.20 s. SentAudio1 is present on 10,641 notes (10,578 unique files, all present); files are named `voicepeak-….mp3`; sample median 1.92 s (n=80); 48 kHz, 64 kbps. The README says: "单词音频：绝大部分为真人播音员录制。例句音频：使用 VOICEPEAK 生成，并经过人工校对" ([README](https://github.com/5mdld/anki-jlpt-decks)). **So the example audio is commercial neural TTS.** Some example slots hold NHK word audio for related or antonym words.
- **Sentence style [VERIFIED-INSPECTED]:** N1 SentKanji1 median 8 characters, 2% ≥20 chars, **0% end with sentence punctuation**. These are mostly collocation fragments, so the deck **fails the full-sentence hard rule** and is reference only. Sentence source: not stated in the README [UNVERIFIED].
- **Real sample notes** (from the release .apkg; verbatim) [VERIFIED-INSPECTED]:
  1. N1高频 · 真実 · ① · 名・ナ形・副 · 真实情况；真的 · `[sound:真実_シ＼ンジツ_1_NHK-2016-260118.mp3]` · 例1 真実を語る / 讲述真实的情况 / `[sound:voicepeak-870966f83ace45d4-260202.mp3]` · 例2 真実あなたが好きだ / 我真的喜欢你 · 対 虚偽.
  2. N1低频 · 実質的 · ⓪ · ナ形 · 例1 実質的な贈り物を選ぶ · 例2 実質的には年収が減っている / 实质上年收入正在减少 · `[sound:voicepeak-31-実質的には年収が減っている-260206.mp3]`.
  3. N1低频 · 監視 · ⓪ · 名・他動3 · 行動を監視する / 监视行动 · `[sound:voicepeak-05-行動を監視する-260203.mp3]`.
  4. N1高频 · 模倣 · 模倣がうまい / 善于模仿.
- **Compatibility / problems (README) [VERIFIED-DOCS]:** requires the latest official Anki or AnkiDroid. AnkiDroid v2.16.0beta2 from "Anki 中国" is incompatible, and downloads may get a `.bin` suffix before AnkiDroid v2.20.1. Word audio can play twice on Windows/macOS. Importing an update overwrites local edits. Optional online TTS buttons need a self-hosted Microsoft-voice proxy.
- **Score: ~50/100**
  - Audio 8/25: present for every example, but the examples are fragments and the voice is TTS.
  - Naturalness 4/20.
  - Suitability 11/15: large N1 list with exam-frequency tiers.
  - Speaking chunks 10/15: collocations are genuinely useful chunks.
  - Coverage 9/10.
  - Maintenance 6/10: excellent maintenance, but the translations are Chinese-only, a risk for a Vietnamese user.
  - Extras 2/5.
  - Uncertainty: ±5.

#### D. "Japanese Core Grammar JLPT N5-N1 (w/audio)" — AnkiWeb 1723302220
- **Metadata [VERIFIED-DOCS, AnkiWeb API]:** 7.2 MB, updated 2026-06-06, 1 thumbs up, 400 notes, 399 audio files. Sample note: 〜にかたくない · N1 · Frequency "Literary" · Sentence: 彼の落胆ぶりは、想像にかたくない。その時の彼女の喜びは、察するにかたくない。 · Audio `[sound:0.mp3]`. Second sample: 〜でしょう · N4 · 明日の 試験は 難しいでしょう。
- **Description [MARKETING]:** "every grammar point is taught through natural Japanese sentences taken from realistic contexts… Full sentence Audio". Also: "I had the help of ai to make the ui and the flashcards". **The audio source (TTS or native) is not stated [UNVERIFIED].** A search snippet mentioned HyperTTS compatibility [UNVERIFIED]. Could not download (HTTP 429).
- **Score: ~35/100, low confidence (±15).** It covers all levels, but with only 400 points that is thin for N1. The AI-generated content is unproofed (1 review) and the audio provenance is unknown. Not recommended until inspected.

#### E. N1-relevant decks checked and found WITHOUT sentence audio (excluded from primary)
- **Japanese Grammar 6500 Example sentences for all 850 GrPoints** (AnkiWeb [841549763](https://ankiweb.net/shared/info/841549763)): 6,623 notes, **0 audio**, 507 images, updated 2022-08-20. The description says "Copied from JLPT sensei… Deck still not finished yet". Sample: 見たいドラマがある日に限って残業で帰りが遅くなってしまう。 (N2) [VERIFIED-DOCS]. Thread: [WaniKani forum](https://community.wanikani.com/t/ultimative-grammar-anki-deck-all-850-grammar-points-with-6500-example-sentences/57855). **Abandoned.**
- **JLPT Grammar from Jtest4you** (AnkiWeb [1696628291](https://ankiweb.net/shared/info/1696628291)): 4,281 notes, 0 audio, updated 2016-04-04, +58/−5 [VERIFIED-DOCS]. **Abandoned.**
- **新完全マスター grammar decks**: "JLPT N2 Grammar" (AnkiWeb [623320804](https://ankiweb.net/shared/info/623320804), 138 notes, 2017) and "SKM N3 Grammar" (AnkiWeb [713504705](https://ankiweb.net/shared/info/713504705), 673 notes, 2019) have 0 audio [VERIFIED-DOCS]. The SKM N1 grammar deck exists only as a Google Drive file ([nathanotabi substack](https://nathanotabi.substack.com/p/optimize-how-you-learn-grammar)); no audio is mentioned [UNVERIFIED].
- **DOJG deck** (Dictionary of Japanese Grammar, MEGA download via [itazuraneko](https://kenrick95.github.io/itazuraneko/grammar/dojg/dojgdeck.html)): fields go up to example 15_jp/en, with cloze and recognition cards. **No audio is mentioned** [VERIFIED-DOCS].
- **GameGogakuen's Japanese Production Flashcards** (AnkiWeb [1898331135](https://ankiweb.net/shared/info/1898331135)): 250.3 MB, updated 2026-05-01, 15,884 notes, 5,147 audio, 6,129 images. Contents: iKnow Core sentences, DOJG (Basic/Intermediate/Advanced) example sentences, and video-game sentences, as production clozes. In the sample notes, the DOJG examples have an empty Audio field (e.g. ジョージは何もすることがないので退屈で仕方がない{{c1::らしい}}。 · Notes "pg608"). **So only part of the deck has audio. It is not JLPT-organized.** Its video-game sentences are the only authentic-source material in any deck I found in this band [VERIFIED-DOCS].
- **PLAYNESE N1 Native Presell** (Payhip, $13.95): 110 cards at present, "To be released: Within 2027". It claims "Example sentences with audio" without saying whether the audio is native or TTS ([Payhip](https://payhip.com/b/p5M1J)) [MARKETING]. Not usable yet.
- **JIVX N1 deck**: subscriber-only. Its pitch is "Advanced — nuance & abstract topics" with "native-quality" audio and male/female voices. Prompts are English→Japanese. The sentence source and whether the audio is native or TTS are not disclosed ([jivx.com/anki](https://jivx.com/anki)) [MARKETING]. Only the free N5 deck (500 sentences) could be checked without paying; I did not inspect it.

### Inferences
- The best "N1 with sentence audio" options are all book or TTS based. An N2-level engineer who already reads work email will find the Tango N1 sentences short and the vocabulary list exam-oriented. Its value is quick headword coverage plus a native audio cue. It does not train comprehension.
- mxggle's grammar deck has the longest and most natural-structured sentences in this scope (median 32 chars, multi-clause). It is useful for N1 grammar recognition, but its TTS audio should not be used for shadowing or prosody work.

### Gaps
- Ankidrone duration stats are based on a 15-file sample per level (not a full census), because the file had to be read through a throttled Yandex mirror.
- Could not verify the audio source of AnkiWeb 1723302220.
- Whether AnkiMobile (iOS) plays Ankidrone V9's .webm files was not tested. The evidence is only general forum reports about Ogg/Opus on iOS.

---

## Per-deck entries — N3–N2 band (consolidation)

### Takeaway
Core 2k/6k is the classic consolidation deck with native sentence audio (iKnow voice talents). The best-maintained full copy on AnkiWeb is "Core 2k/6k [Pitch Graphs, Optimized, Links]", updated 2025-07-25. It is textbook-ish and covers up to the 6,000th most frequent word (≈ N3–N2, partly N1). Ankidrone's Tango N2/N3 subdecks (book audio) are the alternative. All of these are scaffolds, not real-life sentence decks.

### Cited Findings

#### F. Core 2k/6k family (iKnow sentences and audio)
- **Origin / audio source:** iKnow's "Japanese Core 6000" course. "Each item features an example sentence and audio from two popular Japanese voice talents" ([iKnow](https://iknow.jp/content/japanese)) [VERIFIED-DOCS]. iKnow is a paid service, and the AnkiWeb copies are community re-uploads. Several were removed and re-uploaded: "Reuploading since previous version was deleted" (1237389412); "The old decks were taken down" (1312109116) [VERIFIED-DOCS]. Copyright status: unlicensed redistribution [inference].
- **Best-maintained full copy: "Core 2k/6k [ Pitch Graphs, Optimized, Links ]"** (AnkiWeb [1487314101](https://ankiweb.net/shared/info/1487314101)). 233.1 MB, **updated 2025-07-25**, 20 thumbs up / 0 down, **5,996 notes, 11,910 audio files** (≈ word + sentence audio per note). Sample note fields: Expression 大衆 · Meaning "the masses, the populace" · Audio · Sentence 能は元々大衆の文化でした。 · Sentence-Kana · Sentence-English "Noh drama was originally the culture of the masses." · **Sentence Audio** [VERIFIED-DOCS, AnkiWeb API]. The description mentions Takoboto dictionary links and sentence+word on the front. Per a search summary of its reviews, reviewers praised the audio and natural sentences, and the author fixed a missing-audio issue [COMMUNITY, via search snippet; not read in full].
- **Other copies (status) [VERIFIED-DOCS, AnkiWeb API]:**
  - "Core 2k/6k Optimized Japanese Vocabulary with Sound Part 01" ([1880390099](https://ankiweb.net/shared/info/1880390099)): 2,000 notes, 3,989 audio, 704 images, last updated **2017-06-19 (abandoned)**, +108/−12. Sample: 何か / 道に何か落ちています。 / "Something has fallen on the road." / Notes "Core 2000 Step 05 - 117".
  - "Core 2k/6k Optimized Japanese Vocabulary" ([1237389412](https://ankiweb.net/shared/info/1237389412)): 6,000 notes but **only 5 audio files (text-only)**, 2016. Sample 前年に比べて利益が上がりました。 (Core 6000 Step 09).
  - "Remastered Japanese Core 6k Deck Part 1" ([1607129785](https://ankiweb.net/shared/info/1607129785)): 2,999 notes, 5,949 audio, 2022-04-06 (dormant). Sample 先月の七日に孫が生まれました。
  - "Japanese Core 6K Vocab | Natural Audio, Mnemonics, and Type" ([2027003999](https://ankiweb.net/shared/info/2027003999)): part 6 of 6 (words 5001–6000), 1,000 notes, 2,005 audio, updated 2025-08-28. Sample 半導体はさまざまな製品に使われているよ。
  - "Japanese Core 6000 Vocab + Pitch Accent" ([1863168610](https://ankiweb.net/shared/info/1863168610)): 1,000 notes (6th thousand), 2,005 audio, 2021. Sample 労働者がストをしたそうだよ。
  - "Japanese Core 6000 Step 01 (Listening Sentence & Vocab)" ([1312109116](https://ankiweb.net/shared/info/1312109116)): 4,035 notes, 4,038 audio, 2015 (abandoned). It keeps raw iKnowIDs, e.g. "sentence:273068"; sample 彼は盗みの疑いをかけられたの。
  - The original "Core 2k/6k Optimized" deck was removed. A 2016 Google Doc says "my version of Core 6k Optimized Japanese Vocabulary Anki deck(removed) with audio" ([Google Doc](https://docs.google.com/document/d/1zyyuiWkiz2IF2CCROeJebl8mgRdHBqNfS5D7MFjDTzE/edit)) [VERIFIED-DOCS].
- **Criticism [COMMUNITY/VERIFIED-DOCS]:** Kaishi's authors say "Core 2k… had multiple mistranslations, missing or unrelated pictures and some of the sentences weren't very useful, sometimes not even reflecting the meaning of the word used" ([Kaishi README](https://github.com/donkuri/Kaishi)). A Kaishi AnkiWeb reviewer (2026-10-22) says Core 2k has "a random sort of vocab/sentences" [COMMUNITY].
- **Sentence style:** short iKnow-written sentences (samples are 10–20 chars). **Textbook-style, reference/scaffold only** [VERIFIED-DOCS samples; length not measured on the full deck].
- **Score (1487314101): ~55/100 (±10, not inspected)**
  - Audio 18/25: native voice talents, ~2 files per note. Full coverage is likely but not inspected.
  - Naturalness 9/20.
  - Suitability 7/15: mostly ≤N2.
  - Speaking 9/15: everyday plus some business vocabulary.
  - Coverage 7/10.
  - Accuracy/maintenance 3/10: unlicensed copy, known mistranslations, single maintainer.
  - Extras 2/5: pitch graphs, links.

#### G. Ankidrone Tango N3 / N2 subdecks
- Same file and note type as entry A. N2: 1,659 notes, 100% sentence audio, 927 with images. N3: 2,045 notes, 1,444 (71%) with sentence audio. N2 sentence median 17 chars [VERIFIED-INSPECTED]. N2 sentences come from *2500 Essential Vocabulary for the JLPT N2*. "The actual number of sentence items is 1546". It was made by seven volunteers ([N2 page](https://tatsumoto.neocities.org/blog/jlpt-tango-n2-anki-deck)) [VERIFIED-DOCS]. Book-style, reference only.

#### H. coolmule0 "Core Japanese Vocabulary Extended" (JLPT N5–N1, GitHub) — word audio only, excluded
- [GitHub coolmule0/JLPT-N5-N1-Japanese-Vocabulary-Anki](https://github.com/coolmule0/JLPT-N5-N1-Japanese-Vocabulary-Anki), release v2.4 (2026-08-06), GPL-3.0 [VERIFIED-DOCS]. Inspection of `Core.Japanese.Vocabulary.Extended.apkg` (39.7 MB) [VERIFIED-INSPECTED]:
  - Counts: 7,734 notes, 15,468 cards (Recognition + Recall templates). Fields: Expression, English definition, Reading, Grammar, Additional definitions, Example JP, Example EN, Sound.
  - **Sound: only 2,871 notes**, median 1.01 s, so this is **word or kanji-reading audio, not sentence audio**. File names look like kanji-reading clips (`chou-naga(i)_06_e.mp3` on 長期). There is at least one audio mismatch: 効果 → `ha(tasu)_06_c.mp3`.
  - Examples are Tatoeba-style, e.g. トレイシーは眼鏡をなくした。 Reading errors: 眼鏡[がんきょう].
  - **Fails the hard rule.**
  - Score ~25/100.
- **jamsinclair open-anki-jlpt-decks:** the N1 .apkg is 786,650 bytes (v0.3.0, 2025-08-11) ([releases](https://github.com/jamsinclair/open-anki-jlpt-decks)) [VERIFIED-DOCS]. That is too small to contain meaningful audio [inference]. Excluded.

### Inferences
- For an N2 holder working in Japanese, Core 6k's main value is the native iKnow sentence audio for words in the 4k–6k range. Its JLPT alignment is loose. Kaishi already supersedes the 2k part.

### Gaps
- Not inspected: actual iKnow sentence-audio durations, missing-file rate and sentence lengths of AnkiWeb 1487314101 (download blocked by 429).
- Core 10k / "Ultimate Core 10k": unverified (Reddit 403).

---

## Per-deck entries — N5–N4 foundation band (reference only)

### Takeaway
Kaishi 1.5k is the best-maintained modern foundation deck with complete native sentence audio. It is far below this learner's level. Use it only as a reference or for checking pitch.

### Cited Findings

#### I. Kaishi 1.5k v2.4.3 (donkuri)
- **URL / version:** [GitHub donkuri/Kaishi](https://github.com/donkuri/Kaishi), release v2.4.3 published 2026-09-15 (`Kaishi.1.5k.v2.4.3.apkg`, 108.7 MB). Earlier releases: v2.4.2 2026-08-15, v2.4.1 2026-06-05, v2.4.0 2026-04-13, v2.3 2025-11-17. Repo last pushed 2026-10-25, 1,594 stars, no license file [VERIFIED-DOCS via GitHub API]. AnkiWeb [1196762551](https://ankiweb.net/shared/info/1196762551): "Kaishi 1.5k - Basic Japanese Vocabulary", updated 2026-09-15, **325 thumbs up / 12 down**, 337 reviews [VERIFIED-DOCS]. Requires Anki 2.1.50+ ([README](https://github.com/donkuri/Kaishi)) [VERIFIED-DOCS]. **Actively maintained.**
- **Counts / structure [VERIFIED-INSPECTED]:** `collection.anki21b` (new format). Note type "Kaishi 1.5k", 1,501 notes / 1,501 cards, one template "Card 1": front `{{Word}}` + `{{Sentence}}`; back has furigana, meanings, `{{Word Audio}}` `{{Sentence Audio}}`, Picture, and optional pitch blocks. 14 fields: Word, Word Reading, Word Meaning, Word Furigana, Word Audio, Sentence, Sentence Meaning, Sentence Furigana, Sentence Audio, Notes, Pitch Accent, Pitch Accent Notes, Frequency, Picture.
- **Audio [VERIFIED-INSPECTED]:**
  - Sentence Audio: 1,500 notes, 1,477 unique files, **all present**. Full census of durations: min 0.89 s, **median 2.69 s**, max 7.37 s (<1.5 s: 39; 1.5–3 s: 896; 3–6 s: 535; 6–10 s: 7).
  - Sentence-audio sources, from ID3 tags and filenames: **294 files are JLPT Tango book audio** (`JLPT_Tango_N5_0001.mp3`; ID3 album "[Sentence Only] JLPT N5 単語1000" / "JLPT単語 N4 1500", artist "アスク出版"/"ASK PUBLISHING"; median 3.68 s). 967 are md5-named files (median 2.46 s; source not identifiable from metadata). 236 are Core-style `####S.mp3`/`js####a.mp3` (median 2.74 s). 4 are Tatoeba recordings (ID3 "tatoeba.org - Japanese Audio", users Rieko A/huizi99, Mizu, Yomi).
  - Word Audio: 1,499 notes, median 0.86 s, mostly `<word>_<kana-pitch>_<n>_NHK-2016.mp3`. The README says word audio and pitch came from the AJT Japanese add-on.
  - Since the deck was built from Core2k, Core10k, Tango N4 and Tango N5 ([README](https://github.com/donkuri/Kaishi)), the non-Tango sentence audio is most likely Core/iKnow-derived [inference]. Nothing indicates TTS. All files are present, so there are no broken references.
- **Sentence style [VERIFIED-INSPECTED]:** median 13 chars, 5% ≥20 chars, 99% end in 。. These are beginner textbook/Core sentences. ~120 of the 1,500 sentences were "fixed" by the team (README) [VERIFIED-DOCS]. Whether the audio still matches the edited sentences was not checked [UNVERIFIED].
- **Extras [VERIFIED-INSPECTED]:**
  - Pitch Accent filled on 1,500 notes (katakana with HTML marks), Pitch Accent Notes on 60, Notes on 56.
  - Picture on 1,500 notes (irasutoya; 1,331 webp).
  - Pitch data was verified by two people (karifurai, cindsa), per the README [VERIFIED-DOCS].
  - The deck is modular: templates can be switched to word, sentence or audio cards.
- **Real sample notes** (from the v2.4.3 .apkg; verbatim) [VERIFIED-INSPECTED]:
  1. 静か · しずか · quiet · 静[しず]か · `[sound:静か_シ＼ズカ_1_NHK-2016.mp3]` · 静かな所が好きです。 · I like quiet places. · `[sound:JLPT_Tango_N5_0878.mp3]` · Pitch シズカ · Frequency 635 · picture present.
  2. 証拠 · しょうこ · proof, evidence · `[sound:af36c5dd4b7fc50c2b13ca2258c6e52c.mp3]` · 証拠を見つけるまで逮捕はできません。 · It is not possible to make an arrest until evidence is found. · `[sound:271b1d86e2f385a1ca1936c868b77950.mp3]` · Pitch ショーコ · Frequency 1316.
  3. お願い · `[sound:336V.mp3]` · お願いがあります。 · I have a favor to ask. · `[sound:336S.mp3]` · Pitch オネカ°イ.
  4. 失礼します · しつれいします · pardon me, excuse me (e.g. when leaving) · (no Word Audio in this note) · Sentence 失礼します。 · Excuse me. · `[sound:JLPT_Tango_N5_0895.mp3]` · Pitch Accent: シツレイシマス* · Pitch Accent Notes: "You can't really hear the drop in ま＼す for the most part but it's there." · picture present.
- **Known problems:** the README notes audio for 次 and あげる reported as "wrong" (nasal g, i.e. 鼻濁音), and pictures that don't match sentences [VERIFIED-DOCS]. A 2026 AnkiWeb reviewer says "The images make no sense…" and finds the nasal-g overdone [COMMUNITY].
- **Score for this learner: ~58/100**
  - Audio 22/25: complete and native, but short.
  - Naturalness 7/20.
  - **Suitability 2/15: far below N2.**
  - Speaking 7/15: basic everyday phrases.
  - Coverage 9/10.
  - Maintenance 9/10.
  - Extras 5/5.
  - For a true beginner it would be ~80. Uncertainty ±4.

#### J. Other foundation decks (brief)
- **Ankidrone Tango N5/N4 subdecks:** same file as entry A. N4 has 100% sentence audio and N5 86% [VERIFIED-INSPECTED].
- **Ankidrone Foundation V7 (JP1K method)**, AnkiWeb [917377946](https://ankiweb.net/shared/info/917377946): 1,520 notes, 3,374 audio, 619 images, updated 2025-09-30, +47/−3 [VERIFIED-DOCS]. Its page says "Each word along with each sentence has native audio" ([JP1K page](https://tatsumoto.neocities.org/blog/jp1k-anki-deck)) [VERIFIED-DOCS]. Reviews mention obscure ateji such as 仏蘭西 and 亜米利加, misspellings, and iOS needing .ogg→.mp3 conversion [COMMUNITY].
- **Refold "Fundamental Vocabulary to Learn Japanese" (JP1K v3):** paid ($29.99). Sentences are "handwritten by Japanese teachers". The word list was chosen by analyzing 16 slice-of-life anime and cross-checking dramas, and the audio is "recorded by a native Japanese speaker". The page doesn't say whether that covers words, sentences or both ([Refold store](https://refold.la/decks/buy/fundamental-vocabulary-to-learn-japanese)) [MARKETING]. Beginner-only, not relevant here.

### Inferences
- If the learner wants a pitch-accent refresher on high-frequency words, Kaishi's verified pitch field and NHK word audio are the cleanest source. The sentences add nothing at N2.

### Gaps
- None material for this band.

---

## Audio durations and presence — Ankidrone Essentials V9 (final values)
- **Presence [VERIFIED-INSPECTED]:** the media map holds 16,112 files. Every `[sound:]` reference resolves to a file in it:
  - Tango N1: 2,058 sentence-audio refs and 2,051 word-audio refs, all present.
  - Tango N2: 1,667 sentence and 1,660 word refs, all present.
  - N3: 1,445 sentence and 2,104 word. N4: 914 sentence and 917 word. N5: 954 sentence and 1,416 word. All present.
  - Ref counts are slightly above note counts because some notes carry several sound tags.
- **Durations [VERIFIED-INSPECTED]** (random sample of 15 per group, WebM header Duration; all files are WebM/Opus):
  - N1 sentence audio: min 1.63 s, **median 4.00 s**, max 5.52 s.
  - N1 word audio: min 0.49 s, median 0.78 s.
  - N2 sentence audio: min 3.23 s, **median 4.46 s**, max 5.59 s.
  - N2 word audio: median 1.26 s.
  - The SentAudio field therefore holds whole-sentence recordings, not headword audio.
- **AnkiWeb download attempts:** the download endpoint `/svc/shared/download-deck/<id>` returned HTTP 429 on 7 consecutive tries over ~9 minutes for AnkiWeb 1723302220. I gave up as instructed, so no AnkiWeb-hosted deck file was inspected.

---

## Sources

Deck pages, repositories and metadata (all accessed 2026-11-13):
- Kaishi GitHub README and releases: https://github.com/donkuri/Kaishi · https://github.com/donkuri/Kaishi/releases · AnkiWeb https://ankiweb.net/shared/info/1196762551
- egg rolls JLPT10k: https://github.com/5mdld/anki-jlpt-decks · README raw https://raw.githubusercontent.com/5mdld/anki-jlpt-decks/main/README.md · release https://github.com/5mdld/anki-jlpt-decks/releases/download/26.09.06/eggrolls-JLPT10k-v3.5.apkg
- Ankidrone Essentials: https://tatsumoto.neocities.org/blog/ankidrone-essentials (mirror https://tatsumoto-ren.github.io/blog/ankidrone-essentials.html) · Yandex folder https://disk.yandex.com/d/adEb8n9uhOacHw
- JLPT Tango N1 deck page: https://tatsumoto.neocities.org/blog/jlpt-tango-n1-anki-deck
- JLPT Tango N2 deck page: https://tatsumoto.neocities.org/blog/jlpt-tango-n2-anki-deck
- JP1K / Ankidrone Foundation: https://tatsumoto.neocities.org/blog/jp1k-anki-deck · https://ankiweb.net/shared/info/917377946
- mxggle N1 grammar: https://github.com/mxggle/anki-jlpt-n1-grammar-example-sentences · releases https://github.com/mxggle/anki-jlpt-n1-grammar-example-sentences/releases · CHANGELOG https://raw.githubusercontent.com/mxggle/anki-jlpt-n1-grammar-example-sentences/main/CHANGELOG.md · AnkiWeb https://ankiweb.net/shared/info/925682506 · N2 sibling https://github.com/mxggle/anki-jlpt-n2-grammar-example-sentences · https://ankiweb.net/shared/info/1584745637
- coolmule0: https://github.com/coolmule0/JLPT-N5-N1-Japanese-Vocabulary-Anki
- jamsinclair: https://github.com/jamsinclair/open-anki-jlpt-decks
- Core 2k/6k AnkiWeb copies: https://ankiweb.net/shared/info/1487314101 · https://ankiweb.net/shared/info/1880390099 · https://ankiweb.net/shared/info/1237389412 · https://ankiweb.net/shared/info/2027003999 · https://ankiweb.net/shared/info/1863168610 · https://ankiweb.net/shared/info/1607129785 · https://ankiweb.net/shared/info/1312109116
- Core 6k Optimized (removed) note: https://docs.google.com/document/d/1zyyuiWkiz2IF2CCROeJebl8mgRdHBqNfS5D7MFjDTzE/edit
- iKnow Core course page: https://iknow.jp/content/japanese
- GameGogakuen: https://ankiweb.net/shared/info/1898331135 · https://sites.google.com/view/gamegogakuen-flashcards/home/core-2k6k-decks
- Grammar decks: https://ankiweb.net/shared/info/841549763 · https://community.wanikani.com/t/ultimative-grammar-anki-deck-all-850-grammar-points-with-6500-example-sentences/57855 · https://ankiweb.net/shared/info/1696628291 · https://ankiweb.net/shared/info/623320804 · https://ankiweb.net/shared/info/713504705 · https://ankiweb.net/shared/info/1723302220 · https://nathanotabi.substack.com/p/optimize-how-you-learn-grammar
- DOJG deck: https://kenrick95.github.io/itazuraneko/grammar/dojg/dojgdeck.html
- Immersion Kit description: https://tofugu.com/japanese-learning-resources-database/immersion-kit · site https://www.immersionkit.com/
- JIVX: https://jivx.com/anki
- PLAYNESE N1 presell: https://payhip.com/b/p5M1J
- Refold JP1K store page: https://refold.la/decks/buy/fundamental-vocabulary-to-learn-japanese
- Bunpro N2/N1 vocab cloze (Azure TTS, in-app): https://community.bunpro.jp/t/n2-and-n1-vocab-cloze-update-aug-29-2024/99138
- AnkiMobile/iOS audio-format threads: https://forums.ankiweb.net/t/ogg-files-suported-in-anki-mobile/4171 · https://forums.ankiweb.net/t/opus-caf-audios-no-longer-working-with-newer-ffmpeg-and-sharex/43962
- ASK Publishing book pages (word and example-sentence download audio included with books): https://ask-books.com/jp/978-4-87217-982-8/

Inspection method (reproducible; scripts in `C:\Users\trinh-v\AppData\Local\Temp\claude\ad1c1fd31c67307a\43f64388-07fc-4045-ac80-4a54f3550946\scratchpad\scripts\jlpt\`):
- `inspect_apkg.py`: opens the .apkg as a zip (locally, or remotely via HTTP Range requests for the 163 MB Yandex file). It extracts `collection.anki21b` (zstd, decompressed with Python 3.14 `compression.zstd`) or `collection.anki21`, decodes the media map (JSON or zstd-protobuf), and reads note types, fields and templates (new `notetypes`/`fields`/`templates` tables or old `col.models`). It counts `[sound:]` refs per field, checks each against the media map, and samples MP3 frame headers, Ogg granules and WebM Duration for clip lengths and ID3 tags.
- `audio_census.py`: full per-field audio census.
- `sample_notes.py`: verbatim sample notes and sentence-length statistics.
- `ankiweb.py`: AnkiWeb `/svc/shared/item-info` metadata.
- Nothing from any download was executed. Python was run with `-I` from the scripts directory.
