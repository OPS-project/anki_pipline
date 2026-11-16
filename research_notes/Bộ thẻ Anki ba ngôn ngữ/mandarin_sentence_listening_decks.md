# Mandarin sentence / listening / tone Anki decks for a Hanzi-literate (Japanese-reading) beginner — research notes (state as of 2026-11-13)

Scope: sentence decks with full-sentence audio, listening-first and tone/pronunciation decks, resources for Japanese (and Vietnamese) readers of Hanzi. HSK-organized vocabulary decks and HSK 3.0 facts are covered by another researcher; HSK mappings are noted only where a deck has one.

Evidence labels: [VERIFIED-INSPECTED] = I fetched and analysed the data/files myself; [VERIFIED-DOCS] = official page / README / AnkiWeb listing incl. AnkiWeb's own sample notes; [COMMUNITY] = user reviews/forums; [MARKETING] = creator promo only; [UNVERIFIED].

**Inspection method and its limits (read first).**
- AnkiWeb pages are client-rendered. I read each deck's metadata through AnkiWeb's own public JSON/protobuf endpoint `https://ankiweb.net/svc/shared/item-info?sharedId=<id>`. This gives the title, note count, **audio-file count**, image count, last-updated date, description, AnkiWeb's 3 sample notes (all fields, verbatim) and the user reviews. I label this [VERIFIED-DOCS], because it is the same data the AnkiWeb page shows.
- **Full .apkg downloads were blocked.** `/svc/shared/download-deck/<id>` returned HTTP 429 "Please log in to download more decks", and anonymous AnkiWeb search was also blocked ("Please log in to perform more searches"). So **no collection database, note-type definition, card template or media map was inspected for any deck.**
- Partial workaround: AnkiWeb serves the media used by the sample notes publicly at `https://ankiweb.net/shared/mpreview/<id>/<file>`. I downloaded those sample audio files (3–6 per deck) and parsed the MP3 frame headers to get duration, bitrate and sample rate, plus the encoder strings (LAME/Lavf) and ID3 tags. I label this [VERIFIED-INSPECTED (sample audio)]. I cannot listen, so **no claims about naturalness by ear** are made.
- I did not buy paid decks (Spoonfed Gumroad v2, MaoMi, Mandarin Blueprint, Refold, Fluent Forever, Hacking Chinese).
- Tatoeba: I downloaded the official exports and computed current Mandarin audio coverage myself [VERIFIED-INSPECTED].

---

## Top findings & recommended shortlist

### Takeaway
- **Spoonfed Chinese is still the only large (7,300–8,000+ sentences), i+1-ordered Mandarin sentence deck with human full-sentence audio.** It is the default primary pick. You must choose the copy carefully: several free AnkiWeb copies lack audio on about 36% of notes, and one "fixed" fork fills those gaps with Piper TTS.
- **MaoMi Chinese "Beginner to Advanced" (£4, 2,361 notes, one native teacher's voice, built-in listening card)** is the best small paid alternative.
- **ChineseAudioFlashcards HSK 1 (free, 300 sentences, named native speakers)** is a clean first-month deck.
- For tones, the free **"Mandarin ear training with IPA/Pinyin/Zhuyin for Beginners"** deck (randomized native syllable audio, maintained 2023) is the best start.
- **No Japanese-translated Mandarin sentence deck with good audio and active maintenance was found.** The closest is a small 2018 deck built from the Keio (慶應外語) textbook. No Vietnamese-language one was found either.
- Several popular "sentence decks with audio" turn out to use **TTS**: Refold's Mandarin 1k (official FAQ: AI audio), the LTL Flexi decks, and the 20k movie-subtitle "Chinese Sentences" deck. For the last two, the encoder signature shows 24 kHz constant-bitrate cloud-TTS output, and a user review of LTL says "This TTS is impressive!".

### Shortlist (primary = VERIFIED complete-sentence audio)
| Rank | Deck | Role | Sentence audio evidence | Price | Prelim. score /100 |
|---|---|---|---|---|---|
| 1 | **Spoonfed Chinese**: paid Gumroad v2 (promagma), or the best free AnkiWeb copy **`spoonfed_arty` 1307319045** | PRIMARY main sentence/listening deck | [VERIFIED-INSPECTED (sample audio)] 2.8–4.1 s full-sentence clips, human-style LAME/MP3Gain files; 7,364 audio files for 7,386 notes | Gumroad pay-what-you-want, $3 suggested; AnkiWeb copies free | **73** (±7) |
| 2 | **MaoMi Chinese – Mandarin Chinese (Beginner to Advanced)** | PRIMARY (conditional) alternative or second deck | [VERIFIED-DOCS] every card voiced by "Molly", a native teacher. Sentence clips of 2.6–3.3 s seen only in an unauthorised AnkiWeb re-upload; the official demo's samples are words | £4 | **72** (±10) |
| 3 | **Chinese HSK 1 – 150 Words, 300 Example Sentences, with Audio** (ChineseAudioFlashcards) AnkiWeb 1578796058 | PRIMARY for weeks 1–4 | [VERIFIED-INSPECTED (sample audio)] 3.1–4.1 s, 128 kbps; ID3 tags name the speakers "Chang" and "Susu"; 450 audio files / 451 notes | Free (HSK 2–5 paid) | **63** (±8) |
| — | **Mandarin ear training with IPA/Pinyin/Zhuyin for Beginners** (helq) 854183352 | PRIMARY pronunciation/tone trainer (no sentences) | Syllable audio only (~1 s); 8,655 native-recorded clips from pinyin charts | Free | n/a on the sentence rubric (pronunciation fit 9/10) |
| s | Keio 慶應外語 中国語 基礎級 2092205295 / 79846616 (日⇒中) | Japanese-translation supplement | [VERIFIED-INSPECTED (sample audio)] 1.0–3.35 s sentence clips; source looks like textbook audio | Free (copyright unclear) | 63 (±10) |
| s | Tatoeba "All Mandarin (官话) sentences with audio" 110314713 | Small supplement / build-your-own base | [VERIFIED-INSPECTED (sample audio)] 2.8–3.2 s volunteer recordings | Free, but the audio licence forbids reuse outside Tatoeba | 59 (±8) |
| s | Chinese listening drills 1405939111 (Spoonfed audio-first fork) | Template model for audio-first cards | [VERIFIED-INSPECTED (sample audio)] 3.8–4.6 s, 128 kbps 44.1 kHz; but only 5,475 audio files for 8,142 notes | Free | ~58 (±10) |
| ✗ | Refold Mandarin 1k; LTL Flexi Levels 1–5; "Chinese Sentences" (movie subs) 167123156 / 480561007; Spoonfed "Forkfed" 772959041 | Not primary (TTS on all or part of the sentences) | see entries | — | 45–67 |
| ✗ | Chinese Grammar Wiki Study Deck 782551504 | Grammar reference, **0 audio files** | [VERIFIED-DOCS] | Free | 49 |
| ✗ | Mandarin Blueprint | Commercial course; native audio claimed; not inspectable; reading/mnemonic-first | [MARKETING]/[VERIFIED-DOCS] | $449 Foundation Bundle | 69 (±12), poor value and poor fit |

### Inferences (for the report writer)
- **"Guess from characters" risk.** Spoonfed's default Card 1 shows the Hanzi, then plays the audio after a deliberate 1-second `[sound:_silence.mp3]` pause "to give you a moment to test your Hanzi recognition" ([Gumroad](https://promagma.gumroad.com/l/IEmpwF)). For this learner that is exactly the false-progress pattern. Every recommended sentence deck should be switched to an **audio-only front** (Hanzi, pinyin and translation on the back), as the 2016 "Chinese listening drills" fork did ([AnkiWeb 1405939111](https://ankiweb.net/shared/info/1405939111)). This is a template edit (`{{Audio}}` on the front; `{{Hanzi}}`/`{{Pinyin}}`/`{{English}}` on the back). Spoonfed's fields are all separate (English / Pinyin / Hanzi / Audio, per AnkiWeb samples), so the edit is trivial.
- **Suggested sequence:**
  1. Weeks 0–3: the ear-training deck, plus a tone-pair deck.
  2. Weeks 1–4: CAF HSK1, audio-first.
  3. Then Spoonfed (or MaoMi), audio-first, at 5–10 new sentences a day.
  4. Add a shadowing habit, and a production card (English → speak Chinese) only after about 1,000 sentences. Reviewers say Spoonfed's EN→ZH cards are ambiguous ([AnkiWeb 1271086873 reviews](https://ankiweb.net/shared/info/1271086873)).
- **Note on HSK alignment.** None of the top sentence decks is organized by HSK 3.0. CAF uses the 2012 HSK 1 list (150 words). Pair them with the HSK vocabulary deck that the other researcher recommends.

---

## Q1. Which Mandarin sentence decks with complete-sentence audio are most respected and actually good?

### Takeaway
Spoonfed Chinese remains the community default and has genuine full-sentence human audio. Its weaknesses are documented: translations, some odd sentences, a few audio/text mismatches, and missing audio in many free copies. MaoMi Chinese and ChineseAudioFlashcards are smaller deck families with native audio. Refold 1k, LTL, the movie-subtitle "Chinese Sentences" decks and most "generator" projects use TTS. No legitimate ChinesePod, Glossika, HSK Standard Course, Du Chinese or Mandarin Companion sentence deck with audio was found.

### Cited Findings

#### 1. Spoonfed Chinese (several distributions)
**Paid Gumroad v2 ("promagma").**
- Product: "Spoonfed Chinese". Seller: promagma. Pay-what-you-want with a suggested price of $3 (`price_cents` 300, `pwyw.suggested_price_cents` 300). Two variants, "Simplified Hanzi" and "Traditional Hanzi", each one APKG of about 369 MB. Rating 4.6/5 from 118 ratings (82% five-star, 7% one-star). [VERIFIED-DOCS] — [Gumroad page (product JSON)](https://promagma.gumroad.com/l/IEmpwF)
- Meta description: "This is an updated version of the old deck posted for free on Ankiweb. The update features a much better ordering of sentences, improved grammar notes..." [MARKETING] — [Gumroad](https://promagma.gumroad.com/l/IEmpwF)
- Claims: "over 8000 sentences (2-4 years worth of learning)", "ordered incrementally, with each new sentence introducing only 1 or 2 new words", and "Hear the Chinese, spoken by a native speaker". [MARKETING] — [Gumroad](https://promagma.gumroad.com/l/IEmpwF)
- Template facts from the install guide: note type is **"SpoonFedNote"**. The default of 20 new cards/day "means 10 new sentences per day", i.e. 2 cards per note. Card 1's front template contains `[sound:_silence.mp3]`, a 1-second pause before the audio so you can test Hanzi recognition. The notes system marks alternatives "(also …)", common mistakes "(no …)" and literal glosses "(literally …)". Supported on AnkiDroid (free) and AnkiMobile (paid); no add-ons mentioned. [VERIFIED-DOCS] — [Gumroad](https://promagma.gumroad.com/l/IEmpwF)
- The Gumroad page shows no last-updated date [gap].

**Original free AnkiWeb deck "Chinese Sentences and audio, spoon fed" (2003820603).** It was recommended in 2015 for "natural audio reading the whole sentence" ([chinese-forums 49721](https://chinese-forums.com/forums/topic/49721-what-sentence-focused-decks-are-available-for-anki)). It now returns "missing" from AnkiWeb's API. [VERIFIED-INSPECTED] — [AnkiWeb 2003820603](https://ankiweb.net/shared/info/2003820603)

**Free AnkiWeb re-uploads (all [VERIFIED-DOCS] from item-info unless noted):**

| AnkiWeb ID | Title | Updated | Notes | Audio files | Size | +/- | Comment |
|---|---|---|---|---|---|---|---|
| [1307319045](https://ankiweb.net/shared/info/1307319045) | spoonfed_arty | 2023-01-23 | 7,386 | **7,364** | 124 MB | 6/1 | Most complete native audio of the free copies. One reviewer (2023-09-29) calls it "an ancient version"; another (2024-03-18) criticises alternative translations written "in pinyin, much less without tones", duplicate English and capitalisation |
| [1271086873](https://ankiweb.net/shared/info/1271086873) | Spoonfed Chinese | 2024-04-02 | 7,335 | 4,649 | 80 MB | 11/3 | "copy of [1307319045] with … standardization to formatting". A 2024-06-18 review: "Missing files: 2659" (names like tmpj0hpl0.mp3) |
| [848063603](https://ankiweb.net/shared/info/848063603) | Spoonfed Chinese | 2026-04-04 | 7,335 | 4,682 | 82 MB | 0/0 | Same lineage, gaps persist |
| [627958412](https://ankiweb.net/shared/info/627958412) | Spoonfed Chinese with russian translate | 2026-10-04 | 7,335 | 4,682 | 71 MB | 0/0 | Sample 3 references `tmpnhwdal.mp3`; the preview returns **HTTP 404**, i.e. the file is missing [VERIFIED-INSPECTED] |
| [772959041](https://ankiweb.net/shared/info/772959041) | Spoonfed Chinese (Forkfed?) | 2025-10-21 | 7,335 | 7,315 | 122 MB | 2/0 | Fills the missing audio "via Piper TTS (zh_CN-huayan-medium.onnx)", leaving "incorrect translations or Pinyin" untouched |
| [1405939111](https://ankiweb.net/shared/info/1405939111) | Chinese listening drills | 2016-10-12 | 8,142 | 5,475 | 238 MB | 8/2 | "SpoonFed Chinese with altered cards so that only audio is presented on side 1". Reviews: "Has a variety of speakers", "some of the audio files are missing" (2019); "only 5 cards are loaded" (2017); import problems (2024) |

**Sample notes, verbatim** (AnkiWeb sample notes via item-info [VERIFIED-DOCS]; audio measured from `mpreview` [VERIFIED-INSPECTED]):
- 1307319045
  - English=There are people pirating textbooks. | Pinyin=Yǒu rén dào shuā jiàokēshū. | Hanzi=有人盗刷教科书。 | Audio=[sound:0.mp3] → 3.21 s
  - English=Since the weather became sunny, let's hang our clothes. | Pinyin=Jìrán tiānqíng le, wǒmen bǎ yīfu liàng le ba. | Hanzi=既然天晴了，我们把衣服晾了吧。 | Audio=[sound:1.mp3] → 3.06 s
  - English=My little sister very much resembles my mother. | Pinyin=wǒ mèimei hěn xiàng wǒ māma. | Hanzi=我妹妹很像我妈妈。 | Audio=[sound:2.mp3] → 2.80 s
- 1271086873
  - English=We climbed the steep slope. | Pinyin=Wǒmen páshàng le yī gè dǒupō. | Hanzi=我们爬上了一个陡坡。 | Audio=[sound:0.mp3] → 2.95 s
  - English=Bread is made of flour. | Pinyin=Miànbāo shì yòng miànfěn zuò de. | Hanzi=面包是用面粉做的。 | Audio=[sound:1.mp3] → 3.32 s
  - English=The president is the head of the U.S. government. | Pinyin=Zǒngtǒng shì měiguó zhèngfǔ de shǒunǎo. | Hanzi=总统是美国政府的首脑。 | Audio=[sound:2.mp3] → 4.13 s
- 1405939111 (audio-first fork)
  - English=The West and East have different moral standards. | Pinyin=Xīfāng de dàodé biāozhǔn gēn dōngfāng de dàodé biāozhǔn bù tóng. | Hanzi=西方的道德标准跟东方的道德标准不同。 | Audio=[sound:0.mp3] → 4.55 s
  - English=Miss, can I please ask how to get to the railway station? | Pinyin=Xiǎojiě, qǐng wèn huǒchē zhàn zěnme zǒu? | Hanzi=小姐，请问火车站怎么走？ | Audio=[sound:1.mp3] → 3.79 s
  - English=Are you accustomed to Chinese food? | Pinyin=Nǐ shìfǒu xíguàn Zhōngguó de yǐnshí? | Hanzi=你是否习惯中国的饮食？ | Audio=[sound:2.mp3] → 3.87 s
- 772959041 (Forkfed)
  - Hanzi=我正在回家的途中。 [sound:0.mp3] → 1.78 s
  - Hanzi=警察举起了盾牌。 [sound:1.mp3] → 3.32 s
  - Hanzi=家庭暴力是伦理问题。 [sound:2.mp3] → 2.43 s

**Audio forensics (sample audio) [VERIFIED-INSPECTED (sample audio)]:**
- All Spoonfed-lineage clips are full sentences of **2.8–4.6 s**. The 1307319045 and 1271086873 copies use LAME 3.99, VBR, 22.05 kHz, and several carry `MP3GAIN_UNDO` ID3 tags (volume-normalised). The 1405939111 fork has higher-quality files: LAME 3.92, 44.1 kHz, up to 128 kbps. This suggests the AnkiWeb copies were re-encoded down from an earlier master.
- In Forkfed 772959041, samples 0 and 2 are **ffmpeg-encoded (TSSE "Lavf60.16.100", Lavc60.31), CBR 64 kbps**. That signature differs from the original LAME/MP3Gain files and matches the description's Piper TTS fill. Sample 1 keeps the original signature. So **in Forkfed, roughly 2,666 of the sentences (7,315 − 4,649) are TTS**, identifiable by encoder tag. (Inference from the counts plus the tags.)
- These files are consistent with human recordings that were later processed. The text/audio mismatches in the errata (below) are also consistent with human recordings, since TTS would not diverge from the text. This is not proof of nativeness.

**Sentence and audio source.**
- Unknown. A 2015 forum guess says the sentences overlap iKnow ("HerrPetersen thinks it uses iKnow sentences") [COMMUNITY/UNVERIFIED] — [chinese-forums 49721](https://chinese-forums.com/forums/topic/49721-what-sentence-focused-decks-are-available-for-anki).
- A 2016 post says Spoonfed compiles "native-audio sentences from other decks" [COMMUNITY/UNVERIFIED] — [chinese-forums 50600](https://chinese-forums.com/forums/topic/50600-we%E2%80%99ve-made-anki-flashcard-decks-for-all-character-in-hsk-1-2-and-3-with-two-example-sentences-per-character-and-native-audio-for-all-cards).
- Therefore **the licensing/provenance is unclear**.

**Known problems [COMMUNITY]:**
- "The deck is probably still 95% correct". The reviewer's errata list covers audio cut off, pinyin errors, hanzi typos and translations; the sentences get less useful later on and "occasionally, the i+1 structure drops off" (2025-09-20) — [AnkiWeb 1271086873](https://ankiweb.net/shared/info/1271086873).
- The errata file has 437 lines, e.g. "明天下午之前我将把它完成. 将 is given, but the audio says 会", "我们看见孩子上了车。 I … only heard 我, not 我们", "我和她外出了几个月 Audio cut off" [VERIFIED-INSPECTED: file read] — [Tclack88 errata on GitHub](https://github.com/Tclack88/misc-analysis/blob/main/mandarin_frequency_analysis/chinese_anki_backup/spoonfed_chinese_deck_corrections.txt).
- "Extremely bad pronunciation by esp..one of the speakers - non-standard dialect … Some confusing dialogue with A/B saying more on audio than written on the card" (2025-04-21); English cards look "produced by plugging in Chinese phrases into Google Translate" (2025-05-08) — [AnkiWeb 1271086873](https://ankiweb.net/shared/info/1271086873).
- Errors are "mostly in the pinyin" (matteo, 2020) and "the majority of the mistakes … are inaccurate or incomplete translations" (haveheart, 2020). One learner covered ~2,400 words in 304 days — [chinese-forums 58255 p2](https://chinese-forums.com/forums/topic/58255-spoonfed-chinese/page/2).
- A Feb 2026 Anki Forums thread reports the free copy lacks audio for "roughly half"; the reply suggests the iKnow deck or sentence mining — [Anki Forums 68791](https://forums.ankiweb.net/t/spoonfed-chinese-missing-audio-files-should-i-make-my-own/68791).
- "Not ordered by HSK level"; "most of the sentences are a bit easy" [COMMUNITY via aggregators] — [chinese-forums 49721](https://chinese-forums.com/forums/topic/49721-what-sentence-focused-decks-are-available-for-anki).

**Spoonfed record summary.**
- HSK mapping: none.
- Translation: English (the Russian fork adds Russian).
- Fields: English, Pinyin (sentence pinyin, with tone marks), Hanzi, Audio. No images, no word-level audio, no tone colouring (per samples).
- Templates: ZH→EN and EN→ZH, plus audio in the listening fork. No cloze.
- Price and licence: free copies, or Gumroad $3+. The licence is undocumented.
- Maintenance: Gumroad date unknown; AnkiWeb forks updated 2023–2026, but only for formatting or audio fixes.

#### 2. MaoMi Chinese – "Mandarin Chinese (Beginner to Advanced) Anki Deck – 2361 cards"
- £4.00. "About 7000 cards (listening, reading and translation) = about 2333 unique cards". "A variety of words and sentences but with a focus on sentences". "Each card has audio made by Molly (a native Chinese speaker who teaches it professionally)". "The deck gradually increases in difficulty". No refunds. 5 reviews, 5.0. One review (2022) notes occasional ~1 s silence before the audio and rare audio/text mismatches; the owner replied to a review on 2026-07-14. [VERIFIED-DOCS] / [COMMUNITY] — [MaoMi product page](https://maomichinese.com/product/anki1/)
- Official demo V-2.0 (AnkiWeb [1213344518](https://ankiweb.net/shared/info/1213344518)): updated 2020-12-26; 102 notes / 99 audio files; 16/2. "For each work/sentence, there are 3 cards: Chinese Hanzi Reading - English Translation - Audio". [VERIFIED-DOCS]
- Demo samples (words), verbatim: English=To be | Hanzi=是 | Pinyin=shì | Audio=[sound:0.mp3] (1.96 s); English=Shanghai | Hanzi=上海 | Pinyin=Shànghǎi (2.14 s); English=Two, 2 | Hanzi=二 | Pinyin=Èr (2.27 s). Single words lasting about 2 s implies leading/trailing silence, consistent with the review. Files are LAME, 64 kbps, 44.1 kHz. [VERIFIED-INSPECTED (sample audio)]
- Older demo [398296825](https://ankiweb.net/shared/info/398296825) (2019-06-19, 67/15, 4 cards per note). The owner says it is "the old version and no longer updated". [VERIFIED-DOCS]
- **Unauthorised re-upload** "Mandarin Chinese - from beginner to advanced" [857246025](https://ankiweb.net/shared/info/857246025): 2,361 notes, 2,390 audio files. Reviewers state it was "Stolen from Maomi Chinese. It literally only costs £4". The creator's family asked for removal: "My wife spent countless hours … recording this audio". [COMMUNITY]
  - Its sample notes show sentence cards, verbatim: English=He looks very friendly. | Hanzi=他看起来很友好。 | Audio=[sound:0.wav]; English=You should shower now | Hanzi=该洗澡了 | Audio=[sound:1.mp3] (2.59 s); English=We were soaked to the skin. | Hanzi=我们全淋湿了。 | Audio=[sound:2.mp3] (3.34 s). [VERIFIED-INSPECTED (sample audio)]
  - **Do not use the re-upload. Buy the original.**
- Record summary: no HSK mapping; English translation; fields English / Hanzi / Pinyin / Audio; no images; templates are reading, translation (EN→ZH) and an audio (listening) card; actively sold.

#### 3. ChineseAudioFlashcards – "Chinese HSK 1 - 150 Words, 300 Example Sentences, with Audio" (AnkiWeb [1578796058](https://ankiweb.net/shared/info/1578796058))
- Updated 2016-10-03; 451 notes / 450 audio / 1 image; 23 MB; **105 up / 11 down** (93 reviews). [VERIFIED-DOCS]
- "All sentences are made up using only characters from the HSK 1 set"; "All sentences are written and read by native mandarin speakers". Paid HSK 2–5 decks are sold at ChineseAudioFlashcards.com (coupon "anki"). [VERIFIED-DOCS]/[MARKETING]
- Samples, verbatim: Hanzi=这个苹果一块钱。 | Pinyin=Zhège píngguǒ yīkuài qián. | English=This apple costs one yuan. | Audio=[sound:0.mp3] (3.06 s); Hanzi=我家没有电脑 | Pinyin=Wǒjiā méiyǒu diànnǎo | English=I don't have a computer at home. (3.13 s); Hanzi=她是我们的好朋友。 | Pinyin=Tā shì wǒmen de hǎo péngyǒu. (4.08 s).
  - Audio is LAME 3.98, CBR 128 kbps, 44.1 kHz. ID3 tags: TPE1 "HSK", TXXX "Full Name: Chang 1-50" / "Susu 1-100" — **named human speakers**. [VERIFIED-INSPECTED (sample audio)]
- Reviews [COMMUNITY]:
  - "Great for a beginner!" (2026-08-23).
  - "a decent amount of audio that's mixed up" (2024-10-15).
  - "English translations are full of mistakes, the audio is terrible … errors with the pinyin" (2025-09-05).
  - On the **paid** decks: "no tags… HSK4 and HSK5 are mixed together" (2026-05-21).
  - CSS tip: hide `.traditional` to show only simplified.
- A 2016 forum launch thread mentions an audio start delay of ~2 s and apparently auto-generated pinyin with a tone error — [chinese-forums 50600](https://chinese-forums.com/forums/topic/50600-we%E2%80%99ve-made-anki-flashcard-decks-for-all-character-in-hsk-1-2-and-3-with-two-example-sentences-per-character-and-native-audio-for-all-cards).
- HSK mapping: **HSK 2.0 (2012) level 1**, not HSK 3.0.

#### 4. Tatoeba-based decks
- **AnkiWeb [110314713](https://ankiweb.net/shared/info/110314713) "All Mandarin Chinese (官话) sentences with audio from Tatoeba".**
  - Updated **2019-12-29**; 1,678 notes / 1,678 audio files; 3/1. Ordered "according to difficulty using MorphMan". Translations in French, German, English, Wu and Spanish. **There is no pinyin field** (fields: sentence_id, cmn, audio, fra, deu, eng, wuu, spa, MorphMan_*). [VERIFIED-DOCS]
  - Samples, verbatim:
    - cmn=我不觉得她像她妈妈。 | eng=I don't think she takes after her mother. | audio=[sound:0.mp3] (2.82 s)
    - cmn=男孩躺着听收音机。 | eng=The boy lay listening to the radio. (3.19 s)
    - cmn=那就是问题所在了。 | eng= (empty) (2.77 s)
  - Files: LAME 3.98, 64 kbps — the same signature as Tatoeba user fucongcong's recordings that I downloaded directly. [VERIFIED-INSPECTED (sample audio)]
  - Review: "translation doesn't have English… It's messy" (2020) [COMMUNITY].
- **Current Tatoeba data (my own analysis of the official exports, 2026-11-13)** [VERIFIED-INSPECTED] — [Tatoeba downloads](https://tatoeba.org/en/downloads), files `sentences_with_audio.tar.bz2` and `per_language/cmn/*`:
  - 89,289 Mandarin sentences in total; **5,825 have audio** (one recording each).
  - Recordings by user: LeviHighway 4,066; fucongcong 1,675; GlossaMatik 69; zhoucantd 15.
  - Translation links among the audio sentences: English 4,618; **Japanese 1,650**; Vietnamese 39. Across all Mandarin sentences: 14,573 link to Japanese and 667 to Vietnamese.
  - Audio-sentence length: median 9 characters (p10 5, p90 15).
  - 8 sampled MP3s last 1.28–3.37 s.
  - LeviHighway's samples are in **Traditional** script (繞過去。, 我以為我們能贏。, 大家在聊什麼？). LeviHighway's profile: Traditional-Chinese interface translator, member since 2025-03-26, 4,066 recordings, no country stated — [Tatoeba profile](https://tatoeba.org/en/user/profile/LeviHighway). Taiwan-accented audio is likely but not confirmed [inference].
- **Licence:** 5,741 of the 5,825 recordings have an empty licence field, and 84 are CC BY-NC 4.0. Tatoeba: "If the license field is empty, you may not reuse the audio outside the Tatoeba project" [VERIFIED-DOCS] — [Tatoeba downloads](https://tatoeba.org/en/downloads). So redistributed Tatoeba-audio decks such as 110314713 are not licence-clean.
- Generator: [digitalwords.net](https://digitalwords.net/anki/tatoeba-audio/index.eng.html) (2019-12-21) takes target and native languages as ISO 639-3 codes, so `jpn` translations are possible. It also lists sentences sorted with MorphMan [VERIFIED-DOCS]. [Vuizur/tatoeba-to-anki](https://www.github.com/Vuizur/tatoeba-to-anki) falls back to TTS when native audio is missing [VERIFIED-DOCS via search snippet].
- **LTL Flexi Classes decks (Levels 1–5)** (AnkiWeb [944908397](https://ankiweb.net/shared/info/944908397), 846358735, 639645850, 867085963, 70735552) — **TTS**:
  - Level 1: 1,999 notes / 3,998 audio files (Chinese + English audio); updated 2021-07-08; English sentences "taken from the Tatoeba Project". [VERIFIED-DOCS]
  - Sample audio: 24 kHz, CBR 96 kbps, no encoder tag [VERIFIED-INSPECTED (sample audio)]. That matches a cloud-TTS output format; a review says "This TTS is impressive!" (2021). Other reviews: "really weird sentences … 'man doesn't eat man'" (2023) [COMMUNITY].
  - Sample: Front=是十月三日。 | Back=It's the third of October. | Audio= [sound:0.mp3] (1.90 s) | Eng Audio= [sound:1.mp3] | Pinyin=shì shíyuè sānrì 。

#### 5. Movie-subtitle "Chinese Sentences" decks (same author, 56 shared items) — **TTS signature**
- [167123156](https://ankiweb.net/shared/info/167123156) "Chinese Sentences": 20,092 notes / 11,450 audio; updated 2024-12-29; 15/3. "Source of Chinese sentences: Movie subtitles. Source of English translations: Machine translation"; sorted easiest → hardest. [VERIFIED-DOCS]
- [480561007](https://ankiweb.net/shared/info/480561007) "[zh] Chinese: Commonly Used Sentences w/ Word Explanations": 602 notes / 600 audio; 2024-12-22. Part 2 is on Google Drive. [VERIFIED-DOCS]
- Sample audio from both: 24 kHz CBR at 32 or 64 kbps, no encoder tags, 0.77–1.75 s. These are short sentences in a cloud-TTS-style format [VERIFIED-INSPECTED (sample audio); TTS is an inference]. They are **not** the original film audio.
- Review: "average length of 4-5 characters! Only 271 sentences (2.5%) have at least 10 characters … There are plenty of decks out there with 1000+ natural sentences with either recorded human speakers or higher quality text-to-speech" (2024-12-29) [COMMUNITY].
- Samples, verbatim: Sentence=一个男人。 | Pinyin=Yīgè nánrén. | Sentence (English)=A man. | [1]=[sound:0.mp3]; Sentence=画就刻在后面。…; Sentence=是不是这样？…

#### 6. Refold Mandarin 1k ("Fundamental Vocabulary to Learn Mandarin Chinese", ZH1K) — exists; **AI audio**
- 1,000 core words, each with a custom example sentence, an image and audio for the word and the sentence. FAQ: "**The audio is AI-generated**" ("clear, consistent AI voices"). Simplified Chinese, Mainland-optimised. $24.99 one-time for the .apkg (includes updates) or a $9/month online Toolkit; 30-day refund. The page gives no update date or frequency source. [VERIFIED-DOCS] — [Refold deck page](https://refold.la/decks/buy/fundamental-vocabulary-to-learn-mandarin)
- Refold also has a free "Traditional Chinese - 2000 Most Frequent Words - (Refold)" deck, updated 2021-02-21 [VERIFIED-DOCS via search snippet] — [AnkiWeb 216385733](https://ankiweb.net/shared/info/216385733)
- No sample notes obtained.

#### 7. Mandarin Blueprint (commercial)
- Checkout "The Mandarin Blueprint Method: Foundation Bundle": **$449.00 USD** one-time (`basePrice` 44900 cents); "2,517 lessons", "1,011 HD videos", "**5,900 digital SRS flashcards with native audio (male and female)**"; it teaches learners to "Use the Spaced Repetition Software Anki"; "Produce all tones and tone pairs accurately". [VERIFIED-DOCS/MARKETING] — [MB checkout](https://courses.mandarinblueprint.com/offers/uLvswoUD/checkout) (fetched with curl; WebFetch got 403)
- The 2026 homepage advertises a Free tier ("first 20 levels … over 900 lessons … ready-made native-audio flashcards") and "Fluency Lab" (price via sales call; full 88-level curriculum; "thousands of high-frequency conversational sentences"; custom "Language Islands" sentences with native audio; its own practice app with "hide the pinyin" and recall mode). **The homepage no longer mentions Anki.** [VERIFIED-DOCS] — [mandarinblueprint.com](https://www.mandarinblueprint.com/)
- Order: characters → words → sentences by frequency, via the "Hanzi Movie Method" (mnemonics) [VERIFIED-DOCS]. Third-party reviews say there are "Over 11,000 flashcards with audio" and "premade Anki flashcard decks with native audio" [COMMUNITY] — [alllanguageresources](https://www.alllanguageresources.com/mandarin-blueprint/), [mezzoguild](https://mezzoguild.com/mandarin-blueprint-review).
- Not inspected; no sample cards.

#### 8. Leiming's Ultimate Chinese [Simplified] (AnkiWeb [2024475494](https://ankiweb.net/shared/info/2024475494))
- The AnkiWeb part is a character deck: 3,109 notes / 3,563 audio; updated 2023-11-12; 16/2. "Full deck link" on Google Drive (file "Ultimate Chinese (shared Nov 23).apkg"; size not shown; Drive serves a virus-scan warning page). [VERIFIED-DOCS]/[VERIFIED-INSPECTED]
- The description claims about 22,000 sentences:
  - "8000 sentences from Spoonfed. Native speaker recordings!"
  - "2600 sentences from HSK. Native speaker recordings!"
  - "1700 sentences from Domino Chinese. (I'm not sure how these were sourced.)"
  - "11000 sentences straight from Chinese native movies and shows"
  - Characters: "Some have native speaker recordings, some text-to-speech".
  - "I can't promise to maintain it much".
  - [VERIFIED-DOCS]
- Sample: Hanzi=赢 | Pinyin=yíng | Audio=[sound:0.mp3] (0.99 s) | SentenceSimplified=结果他们赢了。 | SentencePinyin.1=Jiéguǒ tāmen yíng le. | SentenceMeaning=They ended up winning. | SentenceAudio=[sound:2.mp3] (2.48 s). Both are 256 kbps with no encoder tag, so the source is unknown. [VERIFIED-INSPECTED (sample audio)]

#### 9. Chinese Grammar Wiki (AllSet Learning) decks — **no audio**
- "Chinese Grammar Wiki Study Deck" [782551504](https://ankiweb.net/shared/info/782551504) by Chris Dodge: 5,864 notes / **0 audio** / 0 images; updated 2018-03-10; 101/2; A1–C1 ("HSK1 to HSK5"); CC BY-NC-SA 3.0. [VERIFIED-DOCS]
  - Sample: 中文=你要让他自己做，只有这样他才能学会。 | Pinyin=Nǐ yào ràng tā zìjǐ zuò, zhǐyǒu zhèyàng tā cái néng xuéhuì. | English=… | Grammar Construct=Condition, 这样 + Result / Purpose | Source URL=… | Tags=B1 …
  - Some cards have an empty Pinyin field. A 2024 review notes a `<br>` rendering fix. [VERIFIED-DOCS]/[COMMUNITY]
- The 2012 East Asia Student A1/A2 decks have no audio mentioned and auto-generated pinyin — [eastasiastudent.net](https://eastasiastudent.net/china/mandarin/cgw-anki-decks/).
- The HelloChina deck below was "created with the help of" the Grammar Wiki.

#### 10. Small native-audio decks
- **HelloChina 100 essential Chinese sentences with Audio** [817140045](https://ankiweb.net/shared/info/817140045): 100 notes / 100 audio; 2016-08-10; "audio is from Native Chinese speakers". [VERIFIED-DOCS]
  - Samples: Hanzi=他和他弟弟都很帅。 | Pinyin=Tā hé tā dìdi dōu hěn shuài.[sound:1.mp3] (3.34 s); Hanzi=你叫什么名字？ | Pinyin=nǐ jiào shénme míngzì?[sound:2.mp3] (2.87 s); Hanzi=再見 | zàijiàn[sound:0.mp3] (2.04 s). The audio sits *inside the Pinyin field*. [VERIFIED-INSPECTED (sample audio)]
- **Systematic Approach to Chinese HSK 1 (with Audio)** [364591273](https://ankiweb.net/shared/info/364591273): 160 notes / 150 audio; 2016; "human audio (actual native speaker, no computer voice!)". Sample clips 2.6–6.0 s. [VERIFIED-INSPECTED (sample audio)]
  - **Broken on current AnkiDroid**: "uses a comment block to hide the sound control: <!--{{Sound}}--> … no longer supported on ankidroid" (2026-02-02); "Audio do not work properly" (2026-10-13). [COMMUNITY] Abandoned.
- **Medical Mandarin Chinese – DLI LSK** [1848818773](https://ankiweb.net/shared/info/1848818773): 640 notes / 640 audio; 2014; built from public-domain Defense Language Institute survival-kit audio. Niche (medical phrases), but licence-clean. [VERIFIED-DOCS]
- **Pimsleur Mandarin I** deck [915822283](https://ankiweb.net/shared/info/915822283): 299 notes / 293 audio; 2024-07-06. Commercial Pimsleur audio, so the copyright is doubtful. [VERIFIED-DOCS]
- **HSK 1-4** [1281990477](https://ankiweb.net/shared/info/1281990477): 4,368 notes / 2,582 audio, with "Sentence Audio" fields. Sample audio is 24 kHz CBR 96 kbps with no tags, i.e. TTS-style [VERIFIED-INSPECTED (sample audio); TTS inferred].

#### 11. ChinesePod / Glossika / textbooks / graded-reader apps
- Glossika: [dseevr/glossika-anki-decks](https://github.com/dseevr/glossika-anki-decks) is Ruby code that builds personal-use decks from Glossika PDFs [VERIFIED-DOCS via search snippet]. Forum view: sharing decks with "original example sentences and native audio" would be "immoral and illegal" [COMMUNITY] — [chinese-forums 50600](https://chinese-forums.com/forums/topic/50600-we%E2%80%99ve-made-anki-flashcard-decks-for-all-character-in-hsk-1-2-and-3-with-two-example-sentences-per-character-and-native-audio-for-all-cards).
- Past takedowns: the "HSK 2012" deck "was deleted after an Anki copyright takedown" [COMMUNITY] — [chinese-forums 49721](https://chinese-forums.com/forums/topic/49721-what-sentence-focused-decks-are-available-for-anki). The smart.fm-based "Mastering the Chinese Characters" decks with sentence audio were removed from AnkiWeb in April 2015, "likely for copyright reasons" [COMMUNITY] — [chinese-forums 35194](https://chinese-forums.com/forums/topic/35194-mandarin-core-2000-anki-deck).
- ChinesePod: a forum reply points to an export tool at chinesepod.com/tools/export [UNVERIFIED, search snippet] — [ChinesePod forum](https://forum.chinesepod.com/t/anyone-using-glossika-lets-discuss-resources/453). No legitimate shared ChinesePod sentence deck was found.
- HSK标准教程 (HSK Standard Course): no deck with 课文/dialogue audio was found; searches returned only HSK word-list decks [gap].
- Du Chinese / The Chairman's Bao / Mandarin Companion: no derived Anki decks or official Anki exports were found. Mandarin Corner flashcards reportedly require a supporter tier [UNVERIFIED, Reddit snippet via search]. Mandarin Mosaic can import Anki/CSV sentence lists [VERIFIED-DOCS] — [mandarinmosaic guide](https://mandarinmosaic.com/guide/anki-import).
- Generators (all TTS): [ethanngit/mandarinankigenerator](https://awesome.ecosyste.ms/projects/github.com%2Fethanngit%2Fmandarinankigenerator) (Google/Azure TTS); [SimonCadge/Mandarin-Card-Generator](https://github.com/SimonCadge/Mandarin-Card-Generator) (synthesised speech); [ChineseIsEasy v3.0](https://github.com/AxelDlv00/ChineseIsEasy) (MIT; French-oriented; words use `gtts` audio; releases 2026-02-02: Dictionary 457 MB, Chengyu 624 MB, TonePairs 985 MB) [VERIFIED-DOCS].

#### 12. Chinese drama/film subs2srs decks
- "Spirited Away Simplified Chinese" [554870338](https://ankiweb.net/shared/info/554870338): 876 notes / 893 audio / 876 snapshots; 2022-04-11; 13/1; made with subs2srs from the Chinese dub. Pinyin comes from the "Pinyin Helper" add-on. Reviews say English meaning does not show on Android (2024). [VERIFIED-DOCS]/[COMMUNITY]
  - Sample: Expression=我 有 急 事 一 定 要 先 走 你 可 以 放 了 我 吗 | Meaning=I have emergency, I must go first. Can you let me go? | Audio=[sound:0.mp3] | Snapshot=[image:1.jpg]
- Chinese-forums "Subs2SRS Anki Deck Index" (2016-09 to 2017-03): 21 decks (e.g. 20 Once Again 1,743 notes; You Are the Apple of my Eye 1,346; FenDou ep01 658; 4 TED talks). Google Drive short links; liveness and copyright not discussed. [COMMUNITY] — [chinese-forums 52517](https://chinese-forums.com/forums/topic/52517-subs2srs-anki-deck-index)
- These are copyrighted-media derivatives. They are noisy for beginners (fast speech, background audio) [inference].

### Inferences
- The free Spoonfed copies split into a **near-complete native-audio lineage (1307319045)** and a **~36%-missing-audio lineage (1271086873 → 848063603 / 627958412)**. Forkfed (772959041) is complete but mixes Piper TTS into about a third of the cards.
- For a learner whose priority is pronunciation, choose (a) the paid Gumroad v2 (claimed better ordering; audio completeness unverified) or (b) 1307319045. In Forkfed, the TTS cards can be found by encoder tag and suspended.
- MaoMi is the only actively sold small deck with one consistent native voice and a built-in audio card. Good if the learner prefers a cleaner, shorter path, but it is unverifiable without purchase.
- Audio-quality signatures generalise: 24 kHz CBR files with no encoder tag (LTL, the movie-subtitle decks, HSK 1-4) are strongly suggestive of cloud TTS. LAME VBR/44.1 kHz files with speaker-name or MP3Gain tags point to human recordings.

### Gaps
- No .apkg could be downloaded (AnkiWeb login wall), so note types, card templates, the full media maps and per-note audio coverage are unverified for every deck. Audio coverage is inferred only from AnkiWeb's file counts.
- Origin of Spoonfed's sentences and speakers, and the Gumroad v2 update date and audio completeness: not found.
- The MaoMi full deck and the Mandarin Blueprint / Refold decks were not inspected (paid).
- No HSK Standard Course dialogue deck, Du Chinese / Chairman's Bao / Mandarin Companion deck, or legitimate ChinesePod/Glossika deck was found.

---

## Q2. Tone and pronunciation decks — which are best for a beginner and how do they integrate?

### Takeaway
The best free start is **helq's "Mandarin ear training with IPA/Pinyin/Zhuyin for Beginners"**. It plays random native recordings and makes you identify the tone, initial or final, which defeats card-order guessing. Follow it with a **tone-pair (disyllable) deck**: the free Forvo-audio deck built on Hacking Chinese's list (old, crowd-sourced audio), or the paid Hacking Chinese / Fluent Forever trainers. Tone decks use word or syllable audio by design, so none qualifies as a "sentence" primary.

### Cited Findings
- **Mandarin ear training with IPA/Pinyin/Zhuyin for Beginners** (helq) — [AnkiWeb 854183352](https://ankiweb.net/shared/info/854183352), [GitHub](https://github.com/helq/pinyin-beginners-anki-deck)
  - 98 notes / **8,655 audio files** / 2 images; 165 MB; updated **2023-07-17**; 19/1 [VERIFIED-DOCS].
  - The deck chooses "a random sound … and you have to guess which tone (or initial or final) it corresponds to", via anki-persistence JS.
  - Tested in Anki Desktop 2.1.60 and AnkiDroid 2.15.6; "reported to work in Anki iOS". Some desktop versions need autoplay off plus the "Replay buttons" add-on [VERIFIED-DOCS].
  - Recordings are credited to the AllSet, Yabla, Yoyo, ArchChinese, PinPin etc. pinyin charts: "I don't own any of the recordings" [VERIFIED-DOCS].
  - Sample notes include IPA/Zhuyin, e.g. Pinyin=guo | Zhuyin=ㄍㄨㄛ | IPA=[ku̯ɔ] | Audio 1=[sound:0.mp3] … [sound:7.wav], plus a "tones practice" note and a pair-sound note (-ao / -ou / -uo).
  - Of the 89 sample clips I fetched, 75 were MP3 and 14 WAV; the MP3s are syllable-length, median 0.98 s, max 1.7 s [VERIFIED-INSPECTED (sample audio)].
  - Reviews: "10/10 card for learning pinyin"; "I recommend that people add more minimal pairs … z & zh, c & ch, s & sh, r & l" (2023) [COMMUNITY].
- **Tone pair practice with audio** — [AnkiWeb 849955173](https://ankiweb.net/shared/info/849955173)
  - 798 notes / 1,115 audio; updated **2016-05-20**; 5/1. "uses the words listed in this blog post" (Hacking Chinese tone pairs) and "adds native prononciation from forvo.com" [VERIFIED-DOCS].
  - Audio-first by design. Samples, verbatim: Front=[sound:0.mp3] | Back=舅舅 jiùjiu; Front=[sound:1.mp3][sound:2.mp3] | Back=地址 dìzhǐ; Front=[sound:3.mp3][sound:4.mp3] | Back=以为 yǐwéi.
  - ID3 tags: TPE1 "Forvo", TALB "Pronunciation in Mandarin Chinese", plus a Forvo licence URL. Clips last 2.1–2.6 s, i.e. word plus silence [VERIFIED-INSPECTED (sample audio)].
  - No translations; abandoned.
- **Chinese Tone Pairs – ALL Chinese TONES in all combinations** — [AnkiWeb 2124722609](https://ankiweb.net/shared/info/2124722609)
  - 20 notes (40 cards) / 20 audio / 20 images; 2020-05-02; 7/1 [VERIFIED-DOCS].
  - "Yoyo Chinese tone pairs in forward (only audio first) and reverse (only pinyin first)" [COMMUNITY]. Audio ID3 says "This video is about Untitled Project 2", i.e. ripped from a video [VERIFIED-INSPECTED].
  - Very small; Italian fields.
- **Hacking Chinese**
  - Tone-pair article with word lists by tone combination and a separate list of 1,000 tone pairs sorted by HSK/TOCFL [VERIFIED-DOCS via search] — [Hacking Chinese tone pairs](https://www.hackingchinese.com/focusing-on-tone-pairs-to-improve-your-mandarin-pronunciation/).
  - Paid course "Tones: Speaking with Confidence": "400+ audio files", ten examples per tone pattern "in both male and female voices", native speakers, online member area. The course page shows no price or Anki mention [VERIFIED-DOCS] — [course page](https://www.hackingchinese.com/courses/tones/).
  - Hacking Chinese's dictation article says the pronunciation course "comes with an Anki deck with audio already attached" [VERIFIED-DOCS] — [HC article 2019-02-27](https://www.hackingchinese.com/free-and-easy-audio-flashcards-for-chinese-dictation-practice-with-anki/). The same article builds audio-only dictation cards with TTS and calls TTS "good enough" for listening, not pronunciation [VERIFIED-DOCS/COMMUNITY].
- **Fluent Forever Pronunciation Trainer (English → Chinese (Mandarin))**
  - **$12**, an Anki deck plus YouTube videos [VERIFIED-DOCS] — [FF product page](https://fluent-forever.com/product/fluent-forever-pronunciation-trainer/).
  - Card types "What sound does this make?" / "identify the tone", tone progression, picture words, an optional spelling test. Version 3.0 dated 2018-06-14 [VERIFIED-DOCS] — [FF trainer resources](https://method.fluent-forever.com/?p=58917).
  - FF help: Anki products are still purchasable but support is "limited" (search snippet; page 403 to fetch) [VERIFIED-DOCS, partial] — [FF help](https://help.fluent-forever.com/hc/en-us/articles/360031417711-Anki-Resources-Post-App).
  - Not inspected.
- **Sinosplice Tone Pair Drills**: character/pinyin charts with audio, licensed **CC BY-NC-SA 2.5** [VERIFIED-DOCS via search] — [Sinosplice](https://www.sinosplice.com/learn-chinese/tone-pair-drills). A community "Mandarin Chinese Tone Practice" AnkiWeb deck based on them was posted on 2011-11-01; no ID given and not located [COMMUNITY] — [chinese-forums 35472](https://chinese-forums.com/forums/topic/35472-mandarin-chinese-tone-practice).
- **Refold Mandarin Minimal Pairs Trainer**: paid, about $14.99, "dozens of tone pairs" (search snippets). The official pages fetched did not show details [UNVERIFIED] — [Refold store](https://refold.la/es/store/decks/mandarin-minimal-pairs-trainer).
- **"Anki with Tones"**: an AnkiDroid fork with tone graphs and recording, plus a sample "Mandarin Tone Pair Drills" deck. Android only [VERIFIED-DOCS via search] — [koendv/Anki-Android](https://github.com/koendv/Anki-Android).
- **ChineseIsEasy TonePairs** (985 MB): its README says word audio uses `gtts`, a TTS engine, and so is unsuitable as a tone model [VERIFIED-DOCS] — [ChineseIsEasy](https://github.com/AxelDlv00/ChineseIsEasy).

### Inferences
- Integration:
  - Run the helq deck first (2–4 weeks, 10–20 cards a day) until tone and initial/final identification is reliable.
  - In parallel, start a tone-pair deck. The Forvo deck is free but crowd-sourced; the Hacking Chinese course or Fluent Forever trainer give controlled voices.
  - Then move to sentence decks with audio-first fronts.
  - Keep tone-pair cards as a daily warm-up. Shadow each sentence card aloud: Spoonfed's own guide says "Practice the pronunciation! … mimicking the native speaker".
- For a Japanese/Vietnamese speaker, prioritise these contrasts in custom minimal-pair cards: n/ng; l/r (flagged for Japanese speakers by [東方書店 PDF](https://www.toho-shoten.co.jp/export/sites/default/toho/toho368-chen.pdf)); zh/ch/sh vs z/c/s; ü; and tone 2 vs 3. The helq deck reviewers also ask for the retroflex pairs.

### Gaps
- No free, maintained, native-voiced tone-pair deck with controlled studio audio was found.
- Contents of the Fluent Forever, Hacking Chinese and Refold decks: not inspected.

---

## Q3. Resources for Japanese speakers (and the Vietnamese angle)

### Takeaway
Japanese-language resources for Mandarin Anki are **sparse**. The only Japanese-translated Mandarin sentence deck with audio found is the 2018 Keio (慶應外語) 中国語 基礎級 deck pair. No Anki deck for 日中同形語 (false friends) or for 音読み↔pinyin correspondence was found, though academic lists exist. Tatoeba holds 1,650 Mandarin audio sentences with Japanese translations, which can be used to build a deck. Vietnamese-language Mandarin sentence decks with audio were not found; a peer-reviewed Hán-Việt ↔ Mandarin rhyme-correspondence table exists.

### Cited Findings
- **慶應外語 中国語 基礎級 KFLS Chinese Basic Class ver0.94** — [AnkiWeb 2092205295](https://ankiweb.net/shared/info/2092205295); reverse JP→ZH version [AnkiWeb 79846616](https://ankiweb.net/shared/info/79846616)
  - 429 notes / 529 audio; 21.9 MB; updated **2018-04-16**. "慶應外語 中国語 基礎級(2012年10月1日 第三版)の基本文型、例文、練習問題、単語、会話文をAnki データとしてまとめました" [VERIFIED-DOCS].
  - Samples, verbatim:
    - ID=Basic05_02_18 | Section=第5課 | Item=例文 | Unit=19.反復疑問文 | Front=你有没有手表？[sound:2.mp3] | Pinyin=Nǐ yǒu mei you shǒubiǎo? | Back=あなたは腕時計を持っていますか？ (2.12 s)
    - ID=Basic05_03_03 | Front=他有一百零八张邮票。[sound:1.mp3] | Back=彼は108枚の切手(邮票 yóupiào)を持っています。 (3.35 s)
    - ID=Basic09_04_06 | Front=写错。说错。[sound:0.mp3] | Back=[错 cuò 間違える]書き間違える。言い間違える。 (2.27 s)
    - JP→ZH deck: Front=他是谁？[sound:2.mp3]他是铃木一郎。[sound:3.mp3] | Back=彼は誰ですか？－鈴木一郎です。
  - Sample audio is a mix: 16 kHz/16 kbps low-bitrate files and 44.1 kHz/160 kbps LAME files, 1.0–3.35 s, full sentences [VERIFIED-INSPECTED (sample audio)].
  - Audio sits inside the Front field together with the Hanzi, so an audio-first template needs field surgery [inference]. Provenance looks like the course textbook's audio, so the copyright is unclear [inference].
  - Reviews: "中国語初心者の私は、毎日これを使って勉強しています。" (2019) [COMMUNITY].
- Searches for "中国語 Anki デッキ 例文 音声", "中国語 発音 声調 Anki 共有デッキ", "中検 Anki デッキ" and "日中同形語 Anki" found no Japanese shared decks. Results were generic articles (studycli.org/ja) and JLPT decks [VERIFIED: searches] — e.g. [studycli JA](https://studycli.org/ja/chinese-tools/chinese-flashcards/).
- 日中同形語 material for self-built cards:
  - 許雪華 (2014) counts over 12,000 Japanese–Chinese homographs [VERIFIED-DOCS via search snippet] — [Kobe Univ. PDF](https://da.lib.kobe-u.ac.jp/da/kernel/0100487720/0100487720.pdf).
  - A 國學院 dissertation builds a classified "同形異義語リスト" as teaching material [VERIFIED-DOCS via search snippet] — [k-rain repository PDF](https://k-rain.repo.nii.ac.jp/record/2001765/files/bunkou_264.pdf).
- 音読み↔pinyin:
  - 邢振雷 et al. (2010) propose a kanji-reading learning system based on the pinyin–on'yomi relationship [VERIFIED-DOCS via search snippet] — [JSiSE PDF](https://www.jsise.org/wp-content/uploads/2022/07/27_211.pdf).
  - Japanese learners have trouble with l/r and n/ng [VERIFIED-DOCS via search snippet] — [東方書店](https://www.toho-shoten.co.jp/export/sites/default/toho/toho368-chen.pdf).
  - No Anki deck found.
- **Tatoeba as a Japanese-translation source** (my analysis): **1,650** of the 5,825 Mandarin sentences with audio link to a Japanese translation, and 14,573 Mandarin sentences in total link to Japanese [VERIFIED-INSPECTED] — [Tatoeba exports](https://tatoeba.org/en/downloads). Examples: 请问鸡蛋在哪里？ → すみません、卵はどこにありますか？; 大家在聊什麼？ → みんな何の話してるの？; 我们把书桌整理干净吧。 → 机の上を片付けよう。 The audio licence restricts reuse outside Tatoeba (see Q1).
- **Vietnamese**:
  - TNU Journal article "Quan hệ đối ứng giữa vần trong tiếng Trung Quốc và vần trong âm Hán Việt" builds a correspondence table between Mandarin finals and Hán-Việt rhymes [VERIFIED-DOCS via search] — [TNU JST 4951](https://jst.tnu.edu.vn/jst/article/view/4951).
  - An HCMUE paper notes that Sino-Vietnamese words underwent Vietnamese phonological change, which brings both advantages and difficulties [VERIFIED-DOCS via search] — [HCMUE](https://journal.hcmue.edu.vn/index.php/hcmuejos/article/download/1102/1093/1103).
  - Another notes that one Vietnamese Sino word often maps to two or more Chinese words, so meaning must be checked [VERIFIED-DOCS via search] — [vjol](https://vjol.info.vn/ngonngu/article/download/135871/111445/).
  - No Vietnamese-translated Mandarin sentence deck with audio was found [VERIFIED: search].
  - Tatoeba: only 39 Mandarin audio sentences have Vietnamese links (667 Mandarin sentences in total).

### Inferences
- For this learner, a "linking sound to known Hanzi" add-on deck is best self-built:
  - Take words from the sentence deck and add on'yomi and Hán-Việt fields.
  - Add a 同形異義 flag drawn from the academic list.
  - Use the audio-first sentence card as the anchor.
- Japanese translations can be bolted onto Spoonfed only by machine translation. Tatoeba gives human JP translations for about 1.6k audio sentences.
- The Keio deck is a reasonable 2–3 week grammar-pattern supplement with Japanese explanations, not a main deck.

### Gaps
- note.com and はてなブログ posts about Mandarin Anki decks did not surface in searches. Japanese-language deck sharing, e.g. on BOOTH, was not found.
- I could not search AnkiWeb by "日本語" or "tiếng Việt" (login wall).

---

## Q4. Chinese-language community views (知乎, 小红书, 贴吧, B站)

### Takeaway
Sparse. Chinese-language searches returned general "how to use Anki" articles (少数派/sspai, CSDN) and English-site translations. No 知乎 or 小红书 threads recommending Mandarin-for-foreigners sentence decks surfaced.

### Cited Findings
- The query "Anki 中文 例句 音频 牌组 外国人 学中文" returned only English AnkiWeb and forum pages [VERIFIED: search] — e.g. [AnkiWeb 1578796058](https://ankiweb.net/shared/info/1578796058).
- The query "知乎 Anki 牌组 推荐 汉语 例句 音频 外国人" returned no 知乎 results, only sspai posts on generic Anki use and .apkg import [VERIFIED: search] — [sspai 65095](https://sspai.com/post/65095), [sspai 57250](https://sspai.com/post/57250).

### Inferences
- Native-Chinese communities make Anki decks for *their* foreign-language study (English, Japanese). Mandarin-for-foreigners decks are discussed almost exclusively in English communities (Chinese-Forums, Reddit, AnkiWeb reviews).

### Gaps
- 小红书, 贴吧 and B站 were not directly searchable with the available tools. Reddit mirrors failed with an SSL error.

---

## Q5. Audio-first / hide-Hanzi customisation, pinyin, tone colouring, word audio, images

### Takeaway
All the leading sentence decks keep Hanzi, pinyin, translation and audio in **separate fields** (Spoonfed, CAF HSK1, MaoMi, Tatoeba). Audio-first cards are therefore a two-minute template change. The exceptions are the Keio and HelloChina decks, where the audio is embedded in the Front/Pinyin field. Only MaoMi (an "Audio" card) and the "Chinese listening drills" fork ship audio-first cards. None of the top sentence decks has tone colouring, images or separate word audio. Leiming's mega-deck has both word and sentence audio fields plus cloze fields.

### Cited Findings
| Deck | Separate fields | Sentence pinyin | Audio-first card shipped | Word audio | Tone colour | Images | Source |
|---|---|---|---|---|---|---|---|
| Spoonfed (AnkiWeb) | English / Pinyin / Hanzi / Audio | yes | no (Card 1 = Hanzi + delayed audio); yes in fork 1405939111 | no | no | no | [AnkiWeb 1307319045](https://ankiweb.net/shared/info/1307319045), [Gumroad](https://promagma.gumroad.com/l/IEmpwF) |
| MaoMi | English / Hanzi / Pinyin / Audio | yes | **yes** ("Audio" card) | words are separate notes | no | no | [AnkiWeb 1213344518](https://ankiweb.net/shared/info/1213344518) |
| CAF HSK1 | Hanzi / Pinyin / English / Audio | yes | not stated | word notes have audio | no | no | [AnkiWeb 1578796058](https://ankiweb.net/shared/info/1578796058) |
| Tatoeba 110314713 | cmn / audio / translations | **no** | no | no | no | no | [AnkiWeb 110314713](https://ankiweb.net/shared/info/110314713) |
| Keio KFLS | Front (Hanzi+audio) / Pinyin / Back (JP) | yes | no | yes (単語 items) | no | no | [AnkiWeb 2092205295](https://ankiweb.net/shared/info/2092205295) |
| Leiming Ultimate | Audio, SentenceAudio, SentencePinyin.1/2, *Cloze fields, Color | yes | "Listen" card type | yes | "Color" field | stroke GIFs | [AnkiWeb 2024475494](https://ankiweb.net/shared/info/2024475494) |
| Refold 1k | n/a | n/a | n/a | yes (AI) | n/a | **yes** | [Refold](https://refold.la/decks/buy/fundamental-vocabulary-to-learn-mandarin) |
| CGW Study Deck | 中文 / Pinyin / English / Grammar Construct / Source URL | partial | n/a (no audio) | no | no | no | [AnkiWeb 782551504](https://ankiweb.net/shared/info/782551504) |

- Tone colouring can be added with the Chinese Support add-ons (e.g. [AnkiWeb add-on 1128979221](https://ankiweb.net/shared/info/1128979221), linked from the Tatoeba deck) [VERIFIED-DOCS]. TTS can be added with AwesomeTTS / HyperTTS. Hacking Chinese and vocab.ai describe audio-only card setups [VERIFIED-DOCS] — [HC dictation article](https://www.hackingchinese.com/free-and-easy-audio-flashcards-for-chinese-dictation-practice-with-anki/), [vocab.ai](https://vocab.ai/tutorials/awesometts-creating-audio-flashcards-in-mandarin-or-cantonese).
- Mobile compatibility:
  - Spoonfed works in AnkiDroid/AnkiMobile [VERIFIED-DOCS].
  - Systematic Approach HSK1's `<!--{{Sound}}-->` hack breaks audio on AnkiDroid [COMMUNITY].
  - helq's deck is tested on AnkiDroid [VERIFIED-DOCS].
  - Spirited Away: the meaning field is not shown on Android [COMMUNITY].

### Inferences
- Recommended card set per sentence note for this learner:
  1. **Listen**: audio only → understand the meaning; back shows Hanzi, pinyin, translation.
  2. **Dictate** (optional): audio → type pinyin with tones.
  3. **Speak** (later): translation → say it, back plays the audio.
- Remove or suspend the Hanzi-front recognition card, since this learner would pass it by reading. If kept, put the audio *before* the Hanzi.

### Gaps
- Exact templates (front/back HTML) of all decks are unverified because the .apkg files could not be downloaded.

---

## Q6. Best progression from simple to complex sentences with reliable native audio (beginner)

### Takeaway
**Spoonfed** has the best long progression: i+1 ordering with 1–2 new words per sentence, about 8k sentences. It needs an audio-first template, the errata list, and a version with complete audio. **CAF HSK1** (300 HSK1-only sentences) is a cleaner, smaller on-ramp. **MaoMi** is the tidy paid middle option. Tatoeba/MorphMan decks are ordered but small, stale and without pinyin.

### Cited Findings
- Spoonfed: "ordered incrementally, with each new sentence introducing only 1 or 2 new words"; "Start from the beginning, or in the middle according to your level" [MARKETING] — [Gumroad](https://promagma.gumroad.com/l/IEmpwF). A long-term user: "better in the beginning … occasionally, the i+1 structure drops off and 2-3 new words will be present" [COMMUNITY] — [AnkiWeb 1271086873](https://ankiweb.net/shared/info/1271086873).
- CAF HSK1: "All sentences are made up using only characters from the HSK 1 set" [VERIFIED-DOCS] — [AnkiWeb 1578796058](https://ankiweb.net/shared/info/1578796058).
- MaoMi: "The deck gradually increases in difficulty, from beginner to higher levels" [VERIFIED-DOCS] — [MaoMi](https://maomichinese.com/product/anki1/).
- Tatoeba deck: "arranged according to difficulty using MorphMan" [VERIFIED-DOCS] — [AnkiWeb 110314713](https://ankiweb.net/shared/info/110314713).

### Preliminary 100-point scores (rubric: audio 25 / naturalness 20 / level fit 15 / speaking chunks 15 / structure 10 / accuracy & maintenance 10 / extras 5)

**Spoonfed Chinese (Gumroad v2, or free 1307319045) — 73 (uncertainty ±7; paid v2 not inspected)**
- Audio 20/25: human full-sentence clips (2.8–4.6 s), several speakers; near-complete in 1307319045. Minus points for cut-offs/mismatches, one reportedly non-standard speaker, and ~36% missing audio in other free copies.
- Naturalness 13/20: everyday early sentences; later some bookish or odd ones; translations criticised.
- Level fit 13/15: designed for absolute beginners.
- Speaking 10/15: many conversational lines and A/B exchanges; EN→ZH cards ambiguous.
- Structure 9/10: i+1 ordering over 7.3–8k sentences.
- Accuracy/maintenance 5/10: about 95% correct per a user; a 437-line errata list; forks only cosmetic; v2 date unknown.
- Extras 3/5: no images, word audio or colour; simple fields, easy to customise; grammar notes in v2.

**MaoMi Chinese Beginner→Advanced — 72 (±10; only demo and re-upload samples seen)**
- Audio 19: a single native teacher on every card; sentence clips 2.6–3.3 s; some leading silence and rare mismatches.
- Naturalness 13: practical everyday sentences mixed with words.
- Level fit 13: starts very simple.
- Speaking 11: conversation-oriented; three skills per note.
- Structure 7: 2,361 notes, gradual.
- Accuracy 6: active seller in 2026, but no changelog.
- Extras 3: built-in audio card; no images.

**ChineseAudioFlashcards HSK1 — 63 (±8)**
- Audio 18: named native speakers at 128 kbps, full sentences; some mix-ups reported.
- Naturalness 10: restricted HSK1 vocabulary makes it stilted.
- Level fit 14: ideal for weeks 1–4.
- Speaking 9: basic sentences.
- Structure 6: only 300 sentences free; paid sequels reportedly disorganised.
- Accuracy 4: 2016; translation and pinyin errors reported.
- Extras 2.

**Keio 慶應外語 中国語 基礎級 (JP) — 63 (±10)**
- Audio 15: full sentences, uneven bitrate.
- Naturalness 12: textbook.
- Level fit 13: beginner; Japanese translations and grammar labels.
- Speaking 10: patterns plus dialogues.
- Structure 6: 429 notes in lessons and grammar units.
- Accuracy 4: v0.94 from 2018; copyright unclear.
- Extras 3: JP grammar notes.

**Tatoeba 官话 audio deck 110314713 — 59 (±8)**
- Audio 18: volunteer native recordings (fucongcong signature).
- Naturalness 11: variable; many sentences translated from English.
- Level fit 9: MorphMan-sorted but no pinyin.
- Speaking 9.
- Structure 6: 1,678 notes, now stale (Tatoeba has 5,825).
- Accuracy 4: 2019; translation gaps; licence problem.
- Extras 2.

**Chinese listening drills 1405939111 — ~58 (±10)**
- Audio 15: best-quality Spoonfed audio, but ~2,667 notes lack it.
- Naturalness 13.
- Level fit 12.
- Speaking 9.
- Structure 7.
- Accuracy 2: 2016; import problems reported.
- Extras 0: audio-first template only.

**Spoonfed "Forkfed" 772959041 — ~62 (±8)**
- As Spoonfed, but audio 13 (about a third Piper TTS) and accuracy 5. Its value is completeness: the TTS cards can be suspended by encoder tag.

**Refold Mandarin 1k — 67 (±10; not inspected)**
- Audio 10: AI-generated, consistent, but risky on tone sandhi and neutral tones for pronunciation modelling.
- Naturalness 14: custom sentences.
- Level fit 13.
- Speaking 11.
- Structure 8.
- Accuracy 6.
- Extras 5: images.
- **Not primary** (AI audio).

**Mandarin Blueprint — 69 (±12; not inspected; $449)**
- Audio 18: native male and female voices claimed.
- Naturalness 12.
- Level fit 7: mnemonic Hanzi-first course is largely redundant for a Hanzi-literate learner, and its reading-first design risks exactly the false-progress problem.
- Speaking 11: pronunciation module plus tutors (Fluency Lab).
- Structure 9.
- Accuracy 8.
- Extras 4.
- **Not primary** (unverified, poor fit and value).

**Leiming's Ultimate Chinese — ~55 (±15)**
- Audio 13: mixed native and TTS; source unknown for some sentences.
- Naturalness 12.
- Level fit 8: overwhelming mega-deck.
- Speaking 9.
- Structure 6.
- Accuracy 3: unmaintained since 2023-11; absorbs others' decks, including commercial Domino Chinese content.
- Extras 4.

**LTL Flexi decks — ~45**
- Audio 8: TTS.
- Naturalness 8: "weird sentences".
- Level fit 10.
- Speaking 7.
- Structure 6.
- Accuracy 4: 2021.
- Extras 2.

**Movie-subtitle "Chinese Sentences" 167123156 — ~45**
- Audio 8: TTS-style.
- Naturalness 10: subtitle lines, very short.
- Level fit 8.
- Speaking 9.
- Structure 6.
- Accuracy 2: machine translations.
- Extras 2.

**Chinese Grammar Wiki Study Deck — 49**
- Audio 0: none.
- Naturalness 12.
- Level fit 11.
- Speaking 8.
- Structure 8: A1–C1 tags.
- Accuracy 7.
- Extras 3.
- Becomes a ~60 with HyperTTS, but that is TTS.

**helq ear-training deck** — not scored on the sentence rubric (no sentences). Pronunciation-trainer fit 9/10: randomized native syllables, IPA/Zhuyin, maintained 2023.

**Tone pair practice (Forvo) 849955173** — pronunciation fit 6/10: audio-first and Hacking Chinese word list, but crowd-sourced audio, no meanings, 2016.

### Inferences
- Beginner path:
  1. helq deck plus a tone-pair deck (2–4 weeks).
  2. CAF HSK1, audio-first (300 sentences).
  3. Spoonfed (v2, or 1307319045), audio-first, 5–10 new sentences a day, applying the Tclack88 errata and deleting odd sentences as long-term users advise. MaoMi is the alternative.
  4. Sentence-mine from graded audio content at the intermediate level.
- This order serves priorities 1–3 (spoken recognition, tones, context vocabulary). Hanzi-linking (priority 4) comes free on the back of each card.

### Gaps
- No deck offers HSK 3.0 mapping plus native sentence audio plus Japanese or Vietnamese translations. That combination would have to be self-built.

---

## Sources

**AnkiWeb deck pages** (metadata, sample notes and reviews read via `https://ankiweb.net/svc/shared/item-info?sharedId=<id>`; sample audio via `https://ankiweb.net/shared/mpreview/<id>/<file>`):
- https://ankiweb.net/shared/info/1307319045 — spoonfed_arty
- https://ankiweb.net/shared/info/1271086873 — Spoonfed Chinese
- https://ankiweb.net/shared/info/848063603 — Spoonfed Chinese
- https://ankiweb.net/shared/info/627958412 — Spoonfed Chinese with russian translate
- https://ankiweb.net/shared/info/772959041 — Spoonfed Chinese (Forkfed?)
- https://ankiweb.net/shared/info/1405939111 — Chinese listening drills
- https://ankiweb.net/shared/info/2003820603 — original spoon fed deck (now missing)
- https://ankiweb.net/shared/info/1213344518 — MaoMi demo V-2.0
- https://ankiweb.net/shared/info/398296825 — MaoMi old demo
- https://ankiweb.net/shared/info/857246025 — unauthorised MaoMi re-upload (evidence only)
- https://ankiweb.net/shared/info/1578796058 — ChineseAudioFlashcards HSK1
- https://ankiweb.net/shared/info/110314713 — Tatoeba 官话 audio
- https://ankiweb.net/shared/info/944908397 — LTL Level 1
- https://ankiweb.net/shared/info/167123156 — Chinese Sentences (movie subtitles)
- https://ankiweb.net/shared/info/480561007 — Commonly Used Sentences
- https://ankiweb.net/shared/info/2024475494 — Leiming's Ultimate Chinese
- https://ankiweb.net/shared/info/782551504 — Chinese Grammar Wiki Study Deck
- https://ankiweb.net/shared/info/817140045 — HelloChina 100
- https://ankiweb.net/shared/info/364591273 — Systematic Approach HSK1
- https://ankiweb.net/shared/info/1848818773 — DLI Medical Mandarin
- https://ankiweb.net/shared/info/915822283 — Pimsleur Mandarin I
- https://ankiweb.net/shared/info/1281990477 — HSK 1-4
- https://ankiweb.net/shared/info/554870338 — Spirited Away
- https://ankiweb.net/shared/info/854183352 — Mandarin ear training (helq)
- https://ankiweb.net/shared/info/849955173 — Tone pair practice with audio
- https://ankiweb.net/shared/info/2124722609 — Chinese Tone Pairs
- https://ankiweb.net/shared/info/2092205295 — 慶應外語 中国語 基礎級
- https://ankiweb.net/shared/info/79846616 — 慶應外語 (日⇒中)
- https://ankiweb.net/shared/info/160608290, https://ankiweb.net/shared/info/433610546, https://ankiweb.net/shared/info/243834318, https://ankiweb.net/shared/info/1643896747, https://ankiweb.net/shared/info/276380336, https://ankiweb.net/shared/info/1616770061, https://ankiweb.net/shared/info/697918796 — checked, minor
- https://ankiweb.net/shared/info/216385733 — Refold Traditional 2000 (search snippet)

**Commercial / official pages:**
- https://promagma.gumroad.com/l/IEmpwF — Spoonfed Chinese, Gumroad (product JSON parsed)
- https://maomichinese.com/product/anki1/ — MaoMi Chinese
- https://refold.la/decks/buy/fundamental-vocabulary-to-learn-mandarin — Refold ZH1K
- https://refold.la/es/store/decks/mandarin-minimal-pairs-trainer — Refold minimal pairs (details not retrievable)
- https://courses.mandarinblueprint.com/offers/uLvswoUD/checkout — Mandarin Blueprint Foundation Bundle, $449
- https://www.mandarinblueprint.com/ — MB homepage 2026
- https://fluent-forever.com/product/fluent-forever-pronunciation-trainer/ — Fluent Forever trainer, $12
- https://method.fluent-forever.com/?p=58917 — FF Mandarin trainer resources
- https://help.fluent-forever.com/hc/en-us/articles/360031417711-Anki-Resources-Post-App — FF help (403; snippet only)
- https://www.hackingchinese.com/courses/tones/ — Hacking Chinese Tones course
- https://www.hackingchinese.com/focusing-on-tone-pairs-to-improve-your-mandarin-pronunciation/ — tone-pair list
- https://www.hackingchinese.com/free-and-easy-audio-flashcards-for-chinese-dictation-practice-with-anki/ — audio-only dictation cards
- https://www.sinosplice.com/learn-chinese/tone-pair-drills — Sinosplice tone pair drills (CC BY-NC-SA 2.5)
- https://eastasiastudent.net/china/mandarin/cgw-anki-decks/ — CGW A1/A2 decks (2012)

**Tatoeba:**
- https://tatoeba.org/en/downloads — licence and column documentation
- https://downloads.tatoeba.org/exports/sentences_with_audio.tar.bz2 — analysed
- https://downloads.tatoeba.org/exports/per_language/cmn/cmn_sentences.tsv.bz2 — analysed
- https://downloads.tatoeba.org/exports/per_language/cmn/cmn-jpn_links.tsv.bz2, …/cmn-vie_links.tsv.bz2, …/cmn-eng_links.tsv.bz2 — analysed
- https://downloads.tatoeba.org/exports/per_language/jpn/jpn_sentences.tsv.bz2, …/vie/vie_sentences.tsv.bz2 — analysed
- https://tatoeba.org/audio/download/<audio_id> — 8 sample MP3s analysed
- https://tatoeba.org/en/user/profile/LeviHighway
- https://digitalwords.net/anki/tatoeba-audio/index.eng.html
- https://www.github.com/Vuizur/tatoeba-to-anki

**GitHub:**
- https://github.com/Tclack88/misc-analysis/blob/main/mandarin_frequency_analysis/chinese_anki_backup/spoonfed_chinese_deck_corrections.txt — Spoonfed errata, read in full
- https://github.com/helq/pinyin-beginners-anki-deck — README read
- https://github.com/AxelDlv00/ChineseIsEasy — README and release assets read
- https://github.com/dseevr/glossika-anki-decks
- https://github.com/SimonCadge/Mandarin-Card-Generator
- https://awesome.ecosyste.ms/projects/github.com%2Fethanngit%2Fmandarinankigenerator
- https://github.com/koendv/Anki-Android

**Forums / community:**
- https://chinese-forums.com/forums/topic/58255-spoonfed-chinese/page/2
- https://chinese-forums.com/forums/topic/49721-what-sentence-focused-decks-are-available-for-anki
- https://chinese-forums.com/forums/topic/50600-we%E2%80%99ve-made-anki-flashcard-decks-for-all-character-in-hsk-1-2-and-3-with-two-example-sentences-per-character-and-native-audio-for-all-cards
- https://chinese-forums.com/forums/topic/35194-mandarin-core-2000-anki-deck
- https://chinese-forums.com/forums/topic/35472-mandarin-chinese-tone-practice
- https://chinese-forums.com/forums/topic/52517-subs2srs-anki-deck-index
- https://forums.ankiweb.net/t/spoonfed-chinese-missing-audio-files-should-i-make-my-own/68791
- https://forum.chinesepod.com/t/anyone-using-glossika-lets-discuss-resources/453 (snippet)
- https://mandarinmosaic.com/guide/anki-decks — aggregator; app vendor
- https://mandarinmosaic.com/guide/anki-import
- https://www.alllanguageresources.com/mandarin-blueprint/
- https://mezzoguild.com/mandarin-blueprint-review

**Japanese / Vietnamese / academic:**
- https://da.lib.kobe-u.ac.jp/da/kernel/0100487720/0100487720.pdf
- https://k-rain.repo.nii.ac.jp/record/2001765/files/bunkou_264.pdf
- https://www.jsise.org/wp-content/uploads/2022/07/27_211.pdf
- https://www.toho-shoten.co.jp/export/sites/default/toho/toho368-chen.pdf
- https://studycli.org/ja/chinese-tools/chinese-flashcards/
- https://jst.tnu.edu.vn/jst/article/view/4951
- https://journal.hcmue.edu.vn/index.php/hcmuejos/article/download/1102/1093/1103
- https://vjol.info.vn/ngonngu/article/download/135871/111445/
- https://sspai.com/post/65095, https://sspai.com/post/57250

**Not accessible / blocked:**
- AnkiWeb .apkg download and search: login wall (HTTP 429).
- GitHub REST API: rate-limited; HTML pages used instead.
- Reddit mirror: SSL error.
- Mandarin Blueprint and Fluent Forever help pages: 403 to WebFetch (MB retrieved with curl).
- Google Drive full Leiming deck: virus-scan interstitial; not downloaded.
