# Japanese beyond N1: Anki decks and deck-generating resources for natural, spoken adult Japanese (state as of 2026-11-13)

Scope: authentic native sentences with full-sentence native audio, for a Vietnamese IT/DX engineer in Japan (N2, preparing for N1). Level-organized N5–N1 decks (Core/Kaishi/Tango/Ankidrone) are covered by another researcher and are left out here. Per the coordinator's priority update, the focus is real-life sentences from drama, film, reality TV, YouTube, podcasts and news. Textbook-style invented sentences rank lower.

Evidence labels: [VERIFIED-INSPECTED] means I downloaded or queried the files/API myself; [VERIFIED-DOCS] means an official page, README or embedded site data; [COMMUNITY] means user reports; [MARKETING] means creator promotion only; [UNVERIFIED] means not confirmed. I cannot listen to audio, so nothing here judges naturalness by ear. Audio durations come from MP3 Xing/CBR headers, Opus granule positions, or the start–end timestamps embedded in clip filenames.

Work done: I wrote my own inspector (Python 3.14, `compression.zstd`) and used it to inspect 6 Immersion Kit single-sentence `.apkg` exports, Lapis 1.7.0, Senren v5.1.0 and jp-mining-note 0.11.0.6 (arbyste fork) example decks. I queried the live Immersion Kit API (`apiv2.immersionkit.com`) and scraped Nadeshiko's public media and stats pages. AnkiWeb could not be inspected: shared-deck pages are a JavaScript SPA, its RPC endpoint returned HTTP 429, and a retry was blocked, so I stopped as instructed.

---

## Top findings & recommended shortlist

### Takeaway
I found **no existing pre-made deck that covers workplace, negotiation, presentation or debate Japanese with natural full-sentence native audio**, in English, Japanese, Chinese or Vietnamese searches. The realistic route beyond N1 is a **sentence corpus with clip audio, used as a deck generator**. Immersion Kit's ~80k live-action drama lines are the only one I verified by inspection. Nadeshiko adds more spontaneous speech (Terrace House, YouTube, live-action dramas) but was verified from docs only. Fill the remaining gaps by **self-mining** with Yomitan + asbplayer/mpvacious/Memento/Anki Miner into Lapis or Senren.

### Cited Findings — shortlist (preliminary scores out of 100; details and per-criterion lines below)

| Rank | Resource | Type | Full-sentence native audio? | Live-action / spoken share | Score | Status |
|---|---|---|---|---|---|---|
| 1 (primary, route) | **Self-mined deck: Lapis or Senren + Yomitan + asbplayer / mpvacious / Memento / Anki Miner** | Generator pipeline | YES: `SentenceAudio` clip cut from the source. Example notes inspected: 1.4–5.5 s Opus clips vs 0.7–1.5 s word audio [VERIFIED-INSPECTED] | Whatever you choose (business dramas, reality TV, YouTube debate/news) | ~85 (±10; depends on effort) | All tools active in 2026 [VERIFIED-DOCS via GitHub API] |
| 2 (primary) | **Immersion Kit, drama category** (14 Japanese TV dramas incl. Legal High, 獣になれない私たち, 今日は会社休みます。, 新聞記者, カルテット) | Searchable corpus with per-sentence `.apkg` export, AnkiConnect button and public API | YES: 6/6 exports had the audio file present, 2.11–10.20 s, matching filename timestamps [VERIFIED-INSPECTED] | ~81.7k drama lines + ~439k anime lines (site table) [VERIFIED-DOCS] | ~76 (±8) | Live. Index last updated 2025-01-11 and the documented old API is dead [VERIFIED-INSPECTED] |
| 3 (primary on docs; not inspected) | **Nadeshiko** (nadeshiko.co) | Searchable corpus with "Export to Anki", API/SDK and Discord bot | Site states every sentence has audio + screenshot [VERIFIED-DOCS]. Not inspected: search returned 403 to scripts and the API needs a key | 1.53M sentences. Live action ~55k lines (incl. Terrace House Tokyo 2019-2020: 17,123), YouTube ~28k, plus anime and light-novel audiobooks [VERIFIED-DOCS] | ~79 (±10) | Very active (v2.6.0; stats updated 2026-11-12) [VERIFIED-DOCS] |
| 4 (generator add-on) | **Aobana Reibun** Anki add-on (AnkiWeb 1429349152) | Backfills sentence, audio, screenshot and translation from Immersion Kit, Nadeshiko or local files into any word/expression deck | Yes, inherited from IK/Nadeshiko [VERIFIED-DOCS]. Not installed or tested | Same as sources | ~78 (±10) | 1.0 release, tested on Anki 26.9 [VERIFIED-DOCS] |
| — not primary | Jo Mako's subs2srs anime/movie decks (MediaFire) | Pre-made subs2srs decks | Likely subs2srs line audio [COMMUNITY/UNVERIFIED] | Anime and film only, no live action mentioned | ~50 (high uncertainty) | Last thread activity Oct 2020 [VERIFIED-DOCS] |
| — not primary | PLAYNESE "N2 Business" (Payhip, $13.99+) | Paid vocab+grammar deck | "Example sentences with audio"; native vs TTS not stated [MARKETING] | Textbook-style (inference) | ~41 | Updated 2026-09-14, no reviews [VERIFIED-DOCS] |
| — not primary | Kotoba Inc book-bundled decks (*101 Common Japanese Idioms in Plain English*, *Sound Words in Japanese*, *Business Japanese*) | Decks bundled with books | Claims native voice-actor audio including example sentences [MARKETING] | Learner-written examples. *Business Japanese* is beginner level | ~45–54 | Not inspected |

Key status/abandonment flags:
- Immersion Kit's "Anki Decks" page now lists only one pre-made deck (NieR:Automata, 840 sentences), and its download URL returns **404**. I found no "Immersion Kit versions of Core/Kaishi" on the site [VERIFIED-INSPECTED].
- Immersion Kit's public docs still describe `api.immersionkit.com/look_up_dictionary`. That host did not respond on 2026-11-13. The site now uses `apiv2.immersionkit.com` [VERIFIED-INSPECTED].
- Immersion Kit's News (5 local Aso clips, 147 lines) and Literature (91 children's/Aozora texts) categories still appear in the site's information table, but the v2 search returns 0 hits for them, even for a word in a news title (稲刈り) [VERIFIED-INSPECTED].
- jidoujisho (Android immersion suite) was **archived 2025-10-20**. The original jp-mining-note repo was last pushed 2023-07-17, and an "arbyste" bug-fix fork was last pushed 2025-11-06 [VERIFIED-DOCS, GitHub API].
- jpdb.io's FAQ says nothing about Anki export. The only related tools I found go the other way: a userscript embeds Immersion Kit examples into jpdb, and an extension pulls media from Anki into jpdb [VERIFIED-DOCS].

### Inferences
- For an N2→N1+ adult professional, the best "deck" is a **personal expression-driven deck**: a list of target chunks (keigo set phrases, discussion connectors, reactions, hedges), filled with drama, reality-TV and YouTube clips through Immersion Kit and Nadeshiko (manually or with Aobana Reibun). Business words that are rare in fiction (納期 has 0 drama hits; 検討させていただきます 1) must then be mined from business dramas, news and YouTube.
- Scripted drama (Immersion Kit) gives clear audio and adult registers (court argument, office keigo, sarcasm). Reality TV and YouTube (Nadeshiko) are closer to spontaneous conversation (fillers, hedging, overlap). The two complement each other.

### Gaps
- No AnkiWeb shared deck could be inspected (SPA + rate limit). Some AnkiWeb drama or keigo decks may exist that I could not see.
- Nadeshiko clips, field layout and export format were not inspected, and no authentic Nadeshiko samples were obtained.

---

## Media-sentence decks and sites with native audio (per-resource entries)

### Takeaway
Immersion Kit and Nadeshiko are the only two maintained, searchable corpora of Japanese live-action TV lines with per-line native audio and screenshots that export to Anki. Neither ships a ready-made advanced or business deck; both work as **deck generators**. Community subs2srs drama decks exist only as scattered file-host uploads of unknown status.

### Cited Findings

#### 1. Immersion Kit (immersionkit.com)
- **Creator / maintainer:** Mathew ("Developer and maintainer of Immersion Kit and Game2Text"). Jo Mako contributed "many of the anime decks used by Immersion Kit Dictionary" [VERIFIED-DOCS] — [About](https://www.immersionkit.com/about).
- **What it is:** "a full-text search engine for sentences in Japanese media", with translation, sound, screenshot and furigana [VERIFIED-DOCS] — [Docs: Background](https://docs.immersionkit.com/background/). Clips are cut by subtitle timings "using apps like subs2srs and movies2anki" [VERIFIED-DOCS] — [Docs: media extraction](https://docs.immersionkit.com/background/media-extraction/).
- **Size (site's embedded "information" table):** Anime 74 titles / 438,936 sentences; Drama 14 titles / 81,680; Games 3 / 1,089; News 5 / 147; Literature 91 / 13,555 [VERIFIED-INSPECTED, parsed from the site JS bundle] — [immersionkit.com/information](https://www.immersionkit.com/information).
  - The live search index (`/index_meta`, `lastUpdatedTimestamp` = **2025-01-11**) lists 80 anime, 14 drama and 3 game titles. It includes *Legal High Season 1*, which the information table omits, so the table is slightly stale [VERIFIED-INSPECTED] — [apiv2 index_meta](https://apiv2.immersionkit.com/index_meta).
  - Tofugu independently describes "over 400,000 different Japanese sentences from various anime series" with screenshot + line audio and downloadable flashcards [COMMUNITY/review; date not shown] — [Tofugu](https://www.tofugu.com/japanese-learning-resources-database/immersion-kit/).
- **Drama titles and line counts** (information table) [VERIFIED-INSPECTED]: 1 Litre of Tears 7,056; Border 5,005; Good Morning Call S1 9,678; S2 5,939; I am Mita, Your Housekeeper 7,956; I'm Taking the Day Off 7,264; Million Yen Woman 3,596; Mob Psycho 100 (live action) 4,045; Overprotected Kahoko 9,251; Quartet 5,089; Sailor Suit and Machine Gun (2006) 3,124; Smoking 2,709; The Journalist 2,941; Weakest Beast 8,027. *Legal High Season 1* is also in the search index, but its count is not listed.
  - Clip filenames confirm the Japanese originals for several: 獣になれない私たち, Kyou_wa_Kaisha_Yasumimasu (今日は会社休みます。), Kahogo_no_Kahoko (過保護のカホコ), Kaseifu_no_Mita (家政婦のミタ), Legal_High, The.Journalist.S01 [VERIFIED-INSPECTED].
- **Domains (inference from titles, partly confirmed by hits):** office life and keigo (Weakest Beast, I'm Taking the Day Off), legal argument and debate (Legal High, Border), politics and press (The Journalist), adult indirect and sarcastic conversation (Quartet), family and romance (Kahoko, Good Morning Call). No news, economics or tech domain.
- **How to get cards** [VERIFIED-INSPECTED from the live API and JS bundle, 2026-11-13]:
  - (a) **Per-sentence `.apkg`:** `https://apiv2.immersionkit.com/download_sentence?id=<sentence id>&modelType=` returns `Content-Type: application/apkg`, one note per file.
  - (b) **"Add to Anki" through AnkiConnect** (port 8765). Default deck "Immersion Kit", model "ImmersionKitCard", tag "ImmersionKit", configurable field mapping, optional preview through `guiAddCards`.
  - (c) **Search API:** `GET apiv2.immersionkit.com/search?q=&category=anime|drama|games&sort=sentence_length:asc|desc&exactMatch=&limit=&offset=&jlpt=&wk=`, plus `/sentence_with_context?sentenceId=` for surrounding lines and `/index_meta`.
  - (d) **Media URLs:** `https://immersionkit.s3.bhs.io.cloud.ovh.net/media/<category>/<Title>/media/<file>` (one audio fetch returned HTTP 200, 54,245 bytes).
  - The site handles HTTP 429 rate limits. Patreon/VIP subscribers are routed to a faster `apiv2express` host.
  - The published docs still describe the old `api.immersionkit.com/look_up_dictionary?keyword=&category=&sort=shortness|longness&min_length=&max_length=&tags[]=&jlpt=&wk=`, which did not respond (curl 000) [VERIFIED-INSPECTED] — [Docs: Public API](https://docs.immersionkit.com/Public%20API/search/).
- **Inspected export structure** (6 files) [VERIFIED-INSPECTED]:
  - Legacy `collection.anki2` + JSON media map; deck "Immersion Kit"; note type **"Immersion Kit Sentence"**.
  - Fields: `Expression`, `English`, `Reading` (furigana), `Screenshot` (`<img>`), `Audio Sentence` (`[sound:…mp3]`), `ID`.
  - One template, "Sentence". Front = Japanese text + screenshot; back = English, furigana and audio. **Audio is on the back**, so for listening-first practice you must edit the template. No `<script>` in the template.
  - Audio file present in all 6, MP3 with Xing header. Measured durations: 3.36 s, 10.20 s, 5.38 s, 4.18 s, 2.11 s and 3.02 s, all ≥2 s, i.e. whole subtitle lines, not headword audio.
- **Sample notes (verbatim; IDs, filenames and durations as obtained):**
  1. `drama_weakest_beast_000005202`, 獣になれない私たち 第07話. 「‪（晶）‬ ‪あっ ご足労いただき恐縮です‬」 — EN "Thank you for coming today." — audio `獣になれない私たち_第07話本音を彼にぶつけた日堂々巡りの恋に大きな決断が720p_HDTV_x264_AAC-DoA_0.21.30.776-0.21.34.112.mp3` (3.36 s measured), screenshot yes [VERIFIED-INSPECTED: .apkg downloaded].
  2. `drama_legal_high_season_1_000000035`, Legal High ep 1. 「（男性）わずか ２分ほどの 一駅区間ならば→ 席を譲る必要もないどころか→ 立ち座りの動作を 余計に強いるのみと判断し→ 申し出なかったまで。 以上。 何か反論は？」 — EN "Since there's just two minutes between his stations... ...there was no need to strongly pressure someone to give up their seat for him... ...and make them stand until a proper judgment could be made otherwise. That is all. Do you have any objections?" — audio `Legal_High_01_0.03.57.720-0.04.07.930.mp3` (10.20 s), screenshot yes [VERIFIED-INSPECTED].
  3. `drama_weakest_beast_000002511`, 第03話. 「要するに 小さな欠点や 問題に関してはオッケーとする」 — EN "In short, we're okay with small flaws and problems." — 5.38 s, screenshot yes [VERIFIED-INSPECTED].
  4. `drama_overprotected_kahoko_000004762`, Kahogo_no_Kahoko_06. 「“加穂子には ママが必要なの” って言えばいいんじゃねえのか」 — EN "Well, if you just want her to come home, you should say, "I need you, Mama." Right?" — 4.18 s [VERIFIED-INSPECTED].
  5. `drama_the_journalist_000002724`, The Journalist S01E06. 「おっしゃるとおり」 — EN "Precisely." — 2.11 s [VERIFIED-INSPECTED].
  6. From search JSON only (durations from filename timestamps):
     - `drama_legal_high_season_1_000000638`: 「暗黙のルールと されている手順を踏むこと→ そのものがマナーなんです。 反論 ありますか？」 — "Going through the proper procedures is the tacit rule behind good manners. Do you have any objections?" (6.1 s).
     - `drama_weakest_beast_000003684`: 「恐れ入りますが もう一度 ご用件を…」 — "Would it be possible to explain it again?" (2.83 s).
     - `drama_border_000000480`: 「謙遜なのか値段交渉なのか どっちなんだ？」 — "Are you being modest, or are you trying to negotiate with me?" (3.2 s).
     - `drama_legal_high_season_1_000001846`: 「（井手）最初から？ （三木）和解交渉こそ→ 大貫 善三が 最も得意とするところだ。」 — "Settlement negotiations are Onuki Zenzo's strong point." (4.42 s).
     - `anime_from_the_new_world_000004899`: 「このような むさ苦しい所まで 足をお運びいただき 誠に恐縮です」 — "It shames me that you had to come to such a foul place." (5.08 s) [VERIFIED-INSPECTED, API JSON].
- **Hit counts for target expressions** (live API, all categories, 2026-11-13; counts may be inflated by fuzzy morpheme matching, see problems) [VERIFIED-INSPECTED]:

  | Expression | Anime | Drama | Games | Main drama sources |
  |---|---|---|---|---|
  | 会議 | 166 | 25 | 45 | |
  | 取引先 | 6 | 10 | 10 | |
  | 見積 | 4 | 7 | 5 | all Weakest Beast |
  | 交渉 | 107 | 11 | 87 | |
  | 御社 | 56 | 43 | 8 | Weakest Beast 17, Legal High 10 |
  | 弊社 | 4 | 10 | 3 | |
  | 恐れ入りますが | 2 | 1 | 5 | |
  | 検討させていただきます | 2 | 1 | 0 | |
  | プレゼン | 349 | 90 | 17 | |
  | 反論 | 14 | 3 | 4 | |
  | おっしゃる通り | 25 | 15 | 5 | |
  | 承知しました | 16 | 93 | 4 | 88 from Mita, a catchphrase |
  | 納期 | 1 | 0 | 0 | |
  | 予算 | 49 | 17 | 3 | |
  | 株価 | 5 | 1 | 2 | |
  | 景気 | 18 | 7 | 20 | |
  | ていうか | 2,849 | 712 | 657 | |
  | マジで | 440 | 76 | 33 | |
  | 冗談でしょ | 66 | 18 | 27 | |
  | 申し訳ございません | 52 | 16 | 3 | |
- **Known problems** [VERIFIED-INSPECTED unless noted]:
  - **Line boundaries:** units follow subtitle lines, often fragments (「おっしゃるとおり」, 2.1 s).
  - **TV-caption artefacts:** speaker labels （晶）, `→` continuation arrows, `[ｽﾋﾟｰｶ]` tags, invisible U+202A/U+202C marks.
  - **EN translation misalignment** in several samples. 「反論して」 (Border) is paired with "It was purposefully designed to be a small-scale bomb."; the Quartet line's EN covers more than the JP; 「御社とは 業務内容にも接点があり」 is paired with "A get-together? Yes. I thought we might be able to cooperate…".
  - **Fuzzy matching:** a 御社 query returned a sentence without 御社, so use `exactMatch`.
  - **Server errors:** one HTTP 500 on a common query (お母さん).
  - **No new titles since 2025-01-11.**
- **Licensing:** the ToS is a generic "Terms and Conditions Generator" template with no licence for the media clips [VERIFIED-INSPECTED]. Clip filenames carry release-group tags (`720p_HDTV_x264_AAC-DoA`, `WEB-DL…MagicStar`), which suggests the clips come from unofficial rips (inference). Treat it as personal-study use only.
- **Price:** free. Donations through Patreon and Ko-fi ("free and accessible") [VERIFIED-DOCS] — [Donate](https://www.immersionkit.com/donate).
- **Mobile:** exported notes are plain HTML + `[sound:]` + `<img>` with no JS. They should work unchanged on AnkiDroid and AnkiMobile (inference from the inspected template). Adding cards from the website through AnkiConnect requires desktop Anki.
- **Score (preliminary): ~76/100 (±8)**
  - Full-sentence audio 25 → **21**: every line has an original-broadcast clip (6/6 verified, 2–10 s), but clips are subtitle-line fragments.
  - Naturalness 20 → **17**: genuine adult TV dialogue (court rhetoric, office keigo, sarcasm), but scripted, and many lines are short.
  - Target level 15 → **12**: native speed and register, good for N1+. Translations sometimes misaligned.
  - Speaking chunks 15 → **12**: rich in reactions, keigo set phrases and casual markers; can be searched by expression.
  - Coverage/progression 10 → **4**: no curriculum and no pre-made decks; thin on business vocabulary (see counts).
  - Accuracy/maintenance 10 → **5**: index frozen since 2025-01; docs and API out of sync; caption artefacts.
  - Images/extras 5 → **5**: screenshot, furigana, context lines, AnkiConnect mapping.
  - Uncertainty: drama total includes the stale table; translation-error rate not measured beyond a ~15-line sample.

#### 2. Nadeshiko (nadeshiko.co)
- **What it is:** "Search over a million Japanese sentences from anime, J-drama and YouTube, each with audio, screenshot and translations in context. Built for sentence mining." Features listed: "Export to Anki — Save any sentence to Anki including screenshot, audio, and multiple languages", context view, downloads, Discord bot [VERIFIED-DOCS] — [Nadeshiko home](https://nadeshiko.co/en/).
- **Team / licence / version:** founder Natsume; contributor Xyaman "helped implement Anki support". Site code AGPL-3.0, DMCA page, "Nadeshiko v2.6.0 | 2024 - 2026" [VERIFIED-DOCS] — [About](https://nadeshiko.co/en/about/); [GitHub BrigadaSOS/Nadeshiko](https://github.com/BrigadaSOS/Nadeshiko).
- **Stats ("Updated Nov 12, 2026"):** 1,529,673+ sentences; 130,927 unique words; 361 titles; 5,297 episodes; 1,343.9 dialogue hours. English translations 100% (94.8% human, 5.2% DeepL); Spanish 100% (87.5% human, 12.5% DeepL) [VERIFIED-DOCS] — [Stats](https://nadeshiko.co/en/stats).
- **Live-action titles (lines)** [VERIFIED-DOCS] — [Media: Live Action](https://nadeshiko.co/en/media?category=JDRAMA):
  - Godzilla Minus One (950, movie)
  - The Naked Director (3,871)
  - **Terrace House: Tokyo 2019-2020 (17,123)**, an unscripted reality show
  - Jin (Final) (6,271)
  - Jin (5,268)
  - My Undead Yokai Girlfriend (2,690)
  - **Extremely Inappropriate! (5,631)**
  - Teasing Master Takagi-san (1,821)
  - I Cannot Reach You (1,829)
  - The Makanai: Cooking for the Maiko House (4,051)
  - Alice in Borderland (2,746)
  - 17.3 about a sex (2,805)
  - Total ≈ 55,000 lines (my sum).
- **YouTube channels (lines)** [VERIFIED-DOCS] — [Media: YouTube](https://nadeshiko.co/en/media?category=YOUTUBE): Japanese Podcast with Hana (7,621 / 20 videos), Tassin Shima (2,746), HIRO BEAUTY CHANNEL (2,732), Shiori no Nantonaku Nichijou (1,380), Suzukawa Ayako ch (3,098), Kozue Chiba / Manga Artist (1,170), Kupio lives in his car (5,005), Yuka (2,415), 東京限定雑学 / Tokyo Trivia (2,291). Total ≈ 28,500 (my sum). There is also an Audiobook (light-novel) category.
- **Maintenance:** a public roadmap shows titles added Jan–Sep 2026 (e.g., Odd Taxi, Bakuman, Serial Experiments Lain). Recent additions are mostly anime [VERIFIED-DOCS] — [Roadmap](https://nadeshiko.co/en/roadmap).
- **API:** npm `@brigadasos/nadeshiko-sdk` and PyPI `nadeshiko-sdk` [VERIFIED-DOCS, README]. A key is required (free from its developer page); quota 150 requests/min and 5,000/month per key [VERIFIED-DOCS, via the Aobana Reibun README] — [Aobana Reibun](https://github.com/Wyzmic/Aobana-Reibun).
- **Inspection:** search pages returned **HTTP 403** to my scripted requests and the API needs a key. **No authentic Nadeshiko samples, field layout or audio files were obtained.**
- **Domains:** natural casual adult conversation (Terrace House: dating, flat-share friction, teasing), workplace and generational comedy (Extremely Inappropriate!), business and negotiation in the AV industry (Naked Director), historical medical drama (Jin), YouTube vlog and podcast talk. Little news, economics or tech (inference from titles).
- **Score (preliminary): ~79/100 (±10)**
  - Audio 25 → **19**: per-line audio claimed for all lines, not inspected.
  - Naturalness 20 → **18**: the only corpus with a large unscripted reality-show set plus YouTube talk.
  - Level 15 → **12**
  - Speaking chunks 15 → **13**: reactions, fillers, teasing.
  - Coverage 10 → **4**: search tool only; heavy anime and light-novel share.
  - Maintenance 10 → **8**: active 2026; translations mostly human.
  - Extras 5 → **5**: screenshot, context, EN/ES, API, Discord.
  - Uncertainty: not inspected; account or API key needed; export details unknown.

#### 3. Aobana Reibun (Anki add-on, AnkiWeb code 1429349152) — generator
- Fills notes with "Japanese example sentences, plus matching audio, screenshots, translations, and source info" from a word field, for a whole deck (Tools → Aobana Reibun → Run) or selected notes. One undo step per run [VERIFIED-DOCS] — [GitHub](https://github.com/Wyzmic/Aobana-Reibun); [AnkiWeb](https://ankiweb.net/shared/info/1429349152).
- **Sources:**
  - Nadeshiko: "anime, live action and YouTube"; key required.
  - Immersion Kit: anime, drama, games; no key; about 1 request per 2 s, so 100 notes take ≈3.5 min.
  - Aobana: local subtitles, books and manga, with an i+1 mode.
  - Options: Skip/Replace/Append modes, fallback between sources, reading filter, bolding [VERIFIED-DOCS].
- **Version:** "1.0 release", requires Qt6, tested on Anki 26.9. AnkiDroid/AnkiMobile not mentioned (the filled notes are ordinary fields + media, so they should sync; inference) [VERIFIED-DOCS].
- This is the most direct way to make "Immersion Kit versions" of any list, e.g. your own 相槌/keigo/discussion-phrase list, or Kaishi/Core [inference]. I found no pre-made "IK Core/Kaishi" deck on the Immersion Kit site.
- Related browser tools: the **Immersion Kit Mining Helper** Chrome extension (c-ehrlich/immersionkit-mining-ext; sends the chosen IK sentence, image and audio to your latest Anki note through AnkiConnect; repo last pushed 2026-03-10, 0 stars) [VERIFIED-DOCS] — [GitHub](https://github.com/c-ehrlich/immersionkit-mining-ext). The **JPDB Immersion Kit Examples** userscript (embeds IK examples into jpdb.io; last pushed 2026-11-07) [VERIFIED-DOCS] — [Greasy Fork](https://greasyfork.org/en/scripts/507408-jpdb-immersion-kit-examples).
- **Score (preliminary): ~78/100 (±10)**
  - Audio 25 → **19**: inherited IK/Nadeshiko clips; add-on not tested by me.
  - Naturalness 20 → **17**: authentic media lines.
  - Level 15 → **13**
  - Speaking chunks 15 → **13**: you choose the expression list.
  - Coverage 10 → **6**: structure comes from your list, but coverage is capped by corpus hits.
  - Maintenance 10 → **5**: brand-new 1.0; Nadeshiko quota of 5,000 requests/month.
  - Extras 5 → **5**: screenshot, translation, source, context, furigana.
  - Uncertainty: not installed; depends on the third-party APIs staying up.

#### 4. Community subs2srs anime/drama/film decks
- **Jo Mako's Shared Deck** (Anki Forums, first post 2020-06-23, last reply 2020-10-05): subs2srs decks for anime such as *A Silent Voice* and *Little Witch Academia*, plus movie, game and manga decks. "Decks based on shows are too big to be posted on Anki web", so they are on **MediaFire**, indexed in a Google Sheet. `{{Audio}}` sentence field autoplays on the front. AnkiWeb author pages /shared/byauthor/1988124792 and /1813538357. No live-action drama mentioned [VERIFIED-DOCS] — [Anki Forums thread](https://forums.ankiweb.net/t/jo-makos-shared-deck/422). Not downloaded; link health unknown; anime-heavy; likely the origin of some IK anime decks.
- **Score (preliminary): ~50/100, high uncertainty**: audio 15 (probably subs2srs line audio, unverified); naturalness 12; level 8; chunks 7; coverage 3; maintenance 2 (2020); extras 3. **Not primary** (audio unverified).
- TheMoeWay's resource page lists **no** pre-made anime/drama sentence decks. It points instead to sentence-search sites (Immersion Kit, Nadeshiko, コツ探索/kotu.io "anime, audiobooks, news, TV, YouTube", SentenceSearch, Youglish, Filmot), condensed-audio archives and subtitle sources (Kitsunekko, Jimaku.cc, JP-Subbers, Japanese Movie Subtitles repo) [VERIFIED-DOCS] — [TheMoeWay resources](https://learnjapanese.moe/resources/).
- **SentenceSearch** (neocities): "Search more then 45 Thousand! sentences, all with native audio"; audio hosted on Firebase/Mega; "Anki integration!". The sources appear to be curated collections, not live-action media (my reading of the page; collection sources not inspected) [VERIFIED-DOCS] — [SentenceSearch](https://sentencesearch.neocities.org/).
- **Glassy-Gaia "Learn Japanese from Studio Ghibli Movies – Multilingual Anki Decks"** (Gumroad, paid): screenshots and original audio per search snippet. A listed movie was rated "Upper Beginner Level (N5–N4)" [MARKETING; product page body not retrievable] — [Gumroad](https://glassygaia.gumroad.com/l/japanese_ghibli_movies). Low relevance (anime film, beginner framing).
- **kotu.io (コツ探索):** the page could not be read (encoding/JS) [UNVERIFIED].

### Inferences
- For "real-life listening at an advanced level", use **Nadeshiko's Terrace House + YouTube** for spontaneous speech, **IK's Legal High / Weakest Beast / I'm Taking the Day Off / The Journalist** for argumentation and office keigo, and **IK's Quartet** for indirect, ironic adult conversation (based on titles and inspected lines; not judged by ear).
- Neither corpus gives multi-clause sentences reliably. Subtitle segmentation produces many 1.5–3 s fragments. Use the context endpoint or view (`sentence_with_context`) to merge 2–3 adjacent lines into one card for longer listening units.

### Gaps
- Full live-action list for Nadeshiko beyond the first media page (it showed 12 titles; page 2 repeated them, so 12 is probably complete) [VERIFIED-DOCS, not certain].
- No reliable source located for pre-made NHK News (regular, not Easy) sentence decks with audio. Search results only turned up generic tools (Anki Miner radio/podcast mode, Tatoeba generators) — [web search summary, no deck found].
- No podcast-derived decks found (e.g., Nihongo con Teppei); there is no evidence that such a deck exists.

---

## Expression decks with sentence audio (慣用句・ことわざ・四字熟語・オノマトペ・敬語・ビジネス・若者言葉・相槌・会議/プレゼン/議論)

### Takeaway
I found **no free expression, keigo or business deck with verified full-sentence native audio**. The candidates are paid or book-bundled, and their audio claims are marketing-level. Textbook-derived decks (上級へのとびら, 中級から上級への日本語, ニュースで学ぶ日本語, 日本語上級話者への道) turned up no Anki deck with audio.

### Cited Findings
- **PLAYNESE "N2 Business" (Payhip, $13.99 minimum, ~370 MB .apkg):** "Over 1700 Vocabulary Cards", a grammar deck, pictures, "Example sentences with audio". Native vs TTS not stated; last update "2026/09/14 (Fixed typos, added sentences)"; "There are no reviews yet" [MARKETING/VERIFIED-DOCS] — [Payhip](https://payhip.com/b/84suD). **Not primary** (audio type unverified; sentences probably written for learners; inference). Score ~41 (audio 8, naturalness 6, level 6, chunks 5, coverage 7, maintenance 5, extras 4).
- **Kotoba Inc (Clay & Yumi Boutwell) book-bundled decks:**
  - *101 Common Japanese Idioms in Plain English*: "a free Anki deck with the sound of all the idioms… three accompanying sound files… recorded by native Japanese voice actors and actresses" [MARKETING] — [Nextory listing](https://nextory.com/de/book/101-common-japanese-idioms-in-plain-english-2544647).
  - *Sound Words in Japanese* (99 onomatopoeia): Anki deck included; "sound files include both the sound word and its example sentence" [MARKETING] — [Storytel listing](https://storytel.com/sg/books/sound-words-in-japanese-99-essential-sound-and-action-words-in-japanese-1871346).
  - *Business Japanese* (2022, *Learn Japanese Through Dialogues* book 6/8): 7 dialogues (job interview, copies for a meeting, two product/advertising meetings); "Crafted especially for beginners and upper beginners"; the page says both "a free Anki flashcard deck for each dialogue line" and "…with the phrases" [MARKETING] — [Storytel](https://www.storytel.com/sg/books/business-japanese-1717164). Too low-level for this user.
  - **Not primary** (not inspected). Idioms/onomatopoeia score ~54: audio 15, naturalness 10, level 7, chunks 10, coverage 5, maintenance 5, extras 2.
- **"Speak Naturally in Japanese" (BOOTH):** a free deck for Kindle-book readers ("Audio for listening practice (if applicable)"; password in the book; personal use only) and an extended ¥700 deck of 50+ cards on うまい/まずい/すみません/だいじょうぶ [MARKETING] — [BOOTH 6920715](https://booth.pm/en/items/6920715); [BOOTH 6922021](https://booth.pm/ja/items/6922021). Small, intermediate, audio uncertain.
- **Keigo deck demand:** a Bunpro community thread asking for a keigo deck got a suggestion to make one yourself [COMMUNITY] — [Bunpro forum](https://community.bunpro.jp/t/keigo-deck/122776).
- **上級へのとびら:** no Anki deck found. The publisher's web audio exists for the *intermediate* とびら book (readings, dialogues, vocab lists) [VERIFIED-DOCS] — [tobiraweb](https://tobiraweb.9640.jp/?p=1945).
- **Japanese/Chinese/Vietnamese searches** ("ビジネス日本語 Anki デッキ 音声", "敬語 Anki 共有デッキ 音声", "商务日语 Anki 牌组 音频", "日剧 Anki 牌组 音频", "日语 高级 口语 Anki 牌组", "Anki tiếng Nhật giao tiếp nâng cao audio") returned no dedicated deck. Results were textbooks with CDs (e.g., 『オフィスで使うビジネス日本語2300 : 825文例付』 in a Japan Foundation booklist), the Kotoba/BOOTH items above, and the Anki Miner tool [search summaries] — [JF booklist PDF](https://www.jpf.go.jp/j/urawa/j_library/booklist/dl/BL16-2018.pdf).

### Inferences
- For keigo, business email and meeting phrases, textbook audio (CD books such as 『オフィスで使うビジネス日本語2300』) is the only *native-recorded* full-sentence source. But it is invented learner-oriented language and would need personal digitisation (copyright: personal use).
- For 慣用句/四字熟語/オノマトペ, the efficient route is to take a list (any free word-only deck) and backfill **authentic** drama/YouTube examples with Aobana Reibun or Immersion Kit. That gives native sentence audio in real context instead of TTS.

### Gaps
- None of the paid or bundled decks was purchased or inspected.
- AnkiWeb keigo, business and idiom decks could not be enumerated (access blocked).

---

## Sentence-mining ecosystem (the realistic route beyond N1) — brief and practical

### Takeaway
The 2026 toolchain is mature and actively maintained. Yomitan handles lookup and card creation. asbplayer (browser: Netflix, YouTube, most streaming), mpvacious (mpv) or Memento (desktop player) cut the **sentence audio + screenshot** for the subtitle line. Anki Miner batch-builds whole episodes or series. Lapis or Senren are the note types. Mobile is limited: Android Firefox for asbplayer/Yomitan; iOS reading only, via Hoshi Reader + AnkiMobile.

### Cited Findings
- **Yomitan:** latest release 26.11.2.0 (2026-11-03), repo pushed 2026-11-12, 2,937 stars [VERIFIED-DOCS, GitHub API] — [GitHub](https://github.com/yomidevs/yomitan). "Yomitan works on Android devices"; "Turn lookups into rich Anki flashcards… Export audio straight to your Anki flashcards" [VERIFIED-DOCS] — [yomitan.wiki](https://yomitan.wiki/).
- **asbplayer:** v1.22.0 (2026-10-14), pushed 2026-11-11. Auto-detected subtitles on Netflix and YouTube; a fallback detector works "on 85% of all other streaming services"; Firefox for Android build; requires AnkiConnect; AGPL-3.0 [VERIFIED-DOCS] — [GitHub](https://github.com/asbplayer/asbplayer).
- **mpvacious:** v26.10.18.0 (2026-10-18), "Adds mpv keybindings to create Anki cards from movies and TV shows"; ships a `subs2srs.conf` [VERIFIED-DOCS, GitHub API] — [GitHub](https://github.com/Ajatt-Tools/mpvacious).
- **Memento** (mpv-based player for studying Japanese): v2.0.2 (2026-07-04), Windows/macOS builds [VERIFIED-DOCS] — [GitHub](https://github.com/ripose-jp/Memento).
- **Anki Miner** (GPL-3.0): v3.12.0 (2026-11-08). Inputs: video + subtitles, batch folders, "YouTube or Bilibili URLs", whole series into "one frequency-ranked deck", plus audiobooks, podcasts and radio as audio+transcript pairs. Outputs: screenshots, audio clips, definitions from Yomitan dictionaries, pitch accent, frequency. Windows/macOS/Linux plus a separate Android app; requires AnkiConnect [VERIFIED-DOCS] — [GitHub](https://github.com/0xzerolight/anki_miner). PyPI pages mention Lapis as the default field mapping in some versions [VERIFIED-DOCS, version-dependent] — [PyPI](https://pypi.org/project/anki-miner/).
- **Lapis note type:** 1.7.0 (2026-01-20), 545 stars [VERIFIED-DOCS]. **Inspected [VERIFIED-INSPECTED]:**
  - Fields: `Expression, ExpressionFurigana, ExpressionReading, ExpressionAudio, SelectionText, MainDefinition, DefinitionPicture, Sentence, SentenceFurigana, SentenceAudio, Picture, Glossary, Hint, IsWordAndSentenceCard, IsClickCard, IsSentenceCard, IsAudioCard, PitchPosition, PitchCategories, Frequency, FreqSort, MiscInfo`.
  - One "Mining" template with JS. Card modes are switched by flag fields, including an **audio card** mode useful for listening practice.
  - Example note: 十中八九 / 「十中八九 せこい小遣い稼ぎだと思う」. `SentenceAudio` = `shoushiminseries04_08m44s853ms_08m47s653ms.ogg` (3.05 s Opus) vs `ExpressionAudio` 1.51 s. Screenshot webp. J-J glossary from 三省堂国語辞典 第八版 + JMdict; pitch "nakadaka"; frequency list; MiscInfo "Shoushimin_Series EP04 (08m46s485ms)".
  - [GitHub](https://github.com/donkuri/lapis)
- **Senren note type:** v5.1.0 (2026-02-21) [VERIFIED-DOCS]. **Inspected [VERIFIED-INSPECTED]:**
  - Fields: `word, reading, sentence, sentenceFurigana, sentenceTranslation, sentenceCard, audioCard, notes, hint, picture, wordAudio, sentenceAudio, selectionText, definition, glossary, pitchAccents, pitchPositions, pitchCategories, frequencies, freqSort, miscInfo, dictionaryPreference`.
  - Template loads Font Awesome from a CDN and bundles JS files.
  - Example sentence audio 1.38–5.53 s vs word audio 0.73–1.08 s. Example: 精霊 — 「一瞬 僕には見えないはずの桜の精霊が 見えた気がした」, `nihoneyoukosoelfsan12_14m27s891ms_14m33s396ms.ogg`. Linked from yomitan.wiki.
  - [GitHub](https://github.com/BrenoAqua/Senren)
- **jp-mining-note:** the original repo was last pushed 2023-07-17. Fork "arbyste" (self-described "Temporary bugfix fork for JPMN"): release 0.11.0.6 (2024-03-09), repo pushed 2025-11-06 [VERIFIED-DOCS]. **Inspected:** 38 fields incl. `SentenceAudio`, `WordAudio`, `PAGraphs`, `PASilence`, `AJTWordPitch`; 4 templates (Mining, PA Sentence, PA Word, Cloze); ~200 KB auto-generated templates with 6 scripts. Example sentence audio 2.9–5.4 s; some sentence-audio fields hold .mp4/.webm [VERIFIED-INSPECTED] — [GitHub fork](https://github.com/Arbyste/jp-mining-note). Flag: maintenance is fragile.
- **Kiku** note type is also listed by TheMoeWay [VERIFIED-DOCS] — [Kiku docs](https://kiku-docs.vercel.app/) (not inspected).
- **Mobile:**
  - **jidoujisho**: archived 2025-10-20 (last release 2.9.1) — **abandoned**.
  - **Hoshi Reader** (iOS EPUB reader): Yomitan dictionaries, "AnkiMobile integration with one-click mining", Lapis handlebars, App Store + TestFlight; no sentence-audio or audiobook support mentioned [VERIFIED-DOCS] — [GitHub](https://github.com/Manhhao/Hoshi-Reader).
  - asbplayer has a Firefox-for-Android build [VERIFIED-DOCS].
  - Video mining on iOS: no tool found.
- **Paid alternative, Migaku:** from $10/month [VERIFIED-DOCS, migaku.com snippet]. Anki export and sentence-audio behaviour **not verified** [UNVERIFIED] — [Migaku](https://migaku.com/learn-japanese).
- **jpdb.io:** FAQ mentions only a "Play sentence audio" shortcut; no Anki export documented [VERIFIED-DOCS] — [jpdb FAQ](https://jpdb.io/faq).
- **Setup effort (inference):** Yomitan + AnkiConnect + Lapis/Senren takes ~1–2 h on desktop. asbplayer adds ~30 min. Anki Miner trades setup for batch output. Fields produced: sentence, sentence audio, screenshot, J-J/J-E definitions, pitch accent, frequency, source/timestamp (confirmed in inspected example notes).

### Inferences
- **Score for the self-mined route (Lapis/Senren + Yomitan + asbplayer/mpvacious/Memento/Anki Miner): ~85/100 (±10)**
  - Full-sentence audio 25 → **22**: every mined card gets the source clip of the line (the field is present in all inspected example notes; 1.4–5.5 s vs ~1 s word audio). Quality depends on subtitle timing.
  - Naturalness 20 → **19**: you choose the sources, which can include spontaneous talk, news and debate.
  - Level 15 → **15**: i+1 by construction.
  - Speaking chunks 15 → **13**: as good as your selection.
  - Coverage/progression 10 → **4**: only what you mine; slow; no curriculum.
  - Accuracy/maintenance 10 → **7**: tools actively maintained in 2026, but YouTube auto-captions and subtitle timing add errors.
  - Extras 5 → **5**: screenshot, pitch accent, J-J definitions, frequency, card-mode flags.
  - Uncertainty: this scores a method, not a downloadable deck; real value depends on hours invested.
- For this user, the minimum viable stack is Yomitan (with a J-J dictionary) + asbplayer on desktop Chrome/Edge + Lapis. Mine Netflix/Prime Japanese-subtitled dramas and YouTube Japanese captions. Use Anki Miner when a whole season of a business drama is worth batch-processing. Review on AnkiDroid or AnkiMobile; the inspected templates use JS but are designed for mobile Anki (not tested by me).

### Gaps
- Status of GameSentenceMiner, ShareX audio-capture workflows and movies2anki was not checked (GitHub API rate limit).
- **"ShadowingDecks"** could not be found under that name [search returned nothing relevant].

---

## Is there ANY existing deck for workplace / negotiation / presentation / debate Japanese with natural full-sentence audio?

### Takeaway
**No.** I found no pre-made deck, free or paid, in any of the four search languages that covers workplace meetings, negotiation, presentations or debate with natural native full-sentence audio. The closest options are Immersion Kit's office and legal dramas (verified audio, thin vocabulary), Nadeshiko's live-action set (docs-verified) and paid textbook-style business decks (audio unverified). The gap must be filled by targeted generation and mining.

### Cited Findings
- Immersion Kit drama contains office and legal registers, but business terms are sparse: 納期 0 drama hits, 検討させていただきます 1, 恐れ入りますが 1, 反論 3, 株価 1. Debate lines are concentrated in Legal High, keigo in Weakest Beast and I'm Taking the Day Off [VERIFIED-INSPECTED, API counts above].
- Nadeshiko's live action includes workplace/comedy (Extremely Inappropriate!), industry and negotiation drama (The Naked Director) and unscripted social talk (Terrace House 17,123 lines) [VERIFIED-DOCS].
- Business-labelled decks found: PLAYNESE N2 Business (paid; audio type unknown) and Kotoba *Business Japanese* (beginner; 7 dialogues) [MARKETING].

### Inferences — minimal way to fill the gap (ordered by effort)
1. **Build a 150–300-item target list** of spoken professional chunks, e.g.:
   - 恐れ入りますが, 差し支えなければ, おっしゃることは分かりますが, 一理ありますね, 念のため確認させてください, 持ち帰って検討します, 前向きに検討します
   - 落としどころ, 要するに, 逆に言うと, ぶっちゃけ, それはそうなんですけど, 認識合わせ, 巻き取る
   - Run it through **Aobana Reibun** (Immersion Kit, no key; Nadeshiko with a free key) or the IK website "Add to Anki" button, using `exactMatch`.
2. **Edit the template** so the audio plays on the front. Merge adjacent context lines for multi-clause listening units.
3. **For items with 0–2 hits**, mine with asbplayer or Anki Miner from Japanese-subtitled business, legal or political dramas you can legally stream. Use Japanese captions on business, news and debate YouTube (e.g., news-commentary and pitch shows). Check that a Japanese caption track exists; auto-captions contain ASR errors that must be corrected by hand.
4. **For news, economics and AI/tech:** no NHK-regular deck exists (gap above). Use Anki Miner's audio+transcript mode on news podcasts or radio with transcripts, or mine NHK video items that carry captions. Expect to verify transcripts by hand.
5. Keep **register tags** on each card (e.g., `会議`, `敬語`, `タメ口`, `皮肉`, `相槌`) to separate spontaneous conversation (Terrace House, YouTube) from formal or scripted speech (court and press-conference scenes, keigo set phrases).

### Gaps
- I did not verify which specific business-drama titles have Japanese subtitle tracks on streaming services available in Japan in 2026.

---

## Source list

**Immersion Kit**
- Home: https://www.immersionkit.com/
- About: https://www.immersionkit.com/about
- Donate: https://www.immersionkit.com/donate
- Information (embedded source table): https://www.immersionkit.com/information
- Anki Decks page: https://www.immersionkit.com/anki_decks
- Dead NieR deck link: https://immersionkit.s3.bhs.io.cloud.ovh.net/anki-decks/games/NieR_Automata.apkg
- ToS: https://www.immersionkit.com/tos
- Docs: https://docs.immersionkit.com/ ; https://docs.immersionkit.com/background/ ; https://docs.immersionkit.com/background/media-extraction/ ; https://docs.immersionkit.com/Public%20API/search/
- Live API: https://apiv2.immersionkit.com/index_meta ; https://apiv2.immersionkit.com/search?q=… ; https://apiv2.immersionkit.com/sentence_with_context?sentenceId=… ; https://apiv2.immersionkit.com/download_sentence?id=…&modelType=
- Tofugu review: https://www.tofugu.com/japanese-learning-resources-database/immersion-kit/

**Nadeshiko**
- https://nadeshiko.co/en/ ; https://nadeshiko.co/en/about/ ; https://nadeshiko.co/en/stats ; https://nadeshiko.co/en/media?category=JDRAMA ; https://nadeshiko.co/en/media?category=YOUTUBE ; https://nadeshiko.co/en/media?category=AUDIOBOOK ; https://nadeshiko.co/en/roadmap ; https://github.com/BrigadaSOS/Nadeshiko

**Generators, browser tools and add-ons**
- Aobana Reibun: https://github.com/Wyzmic/Aobana-Reibun ; https://ankiweb.net/shared/info/1429349152
- Immersion Kit Mining Helper: https://github.com/c-ehrlich/immersionkit-mining-ext
- JPDB Immersion Kit Examples: https://greasyfork.org/en/scripts/507408-jpdb-immersion-kit-examples ; https://github.com/AwooDesu/JPDB-Immersion-Kit-Examples

**Community decks and resource lists**
- Jo Mako thread: https://forums.ankiweb.net/t/jo-makos-shared-deck/422
- TheMoeWay resources: https://learnjapanese.moe/resources/
- SentenceSearch: https://sentencesearch.neocities.org/
- Glassy-Gaia: https://glassygaia.gumroad.com/l/japanese_ghibli_movies

**Mining tools and note types**
- Yomitan: https://github.com/yomidevs/yomitan ; https://yomitan.wiki/
- asbplayer: https://github.com/asbplayer/asbplayer
- mpvacious: https://github.com/Ajatt-Tools/mpvacious
- Memento: https://github.com/ripose-jp/Memento
- Anki Miner: https://github.com/0xzerolight/anki_miner ; https://pypi.org/project/anki-miner/
- Lapis: https://github.com/donkuri/lapis (release asset https://github.com/donkuri/lapis/releases/download/1.7.0/Lapis.apkg)
- Senren: https://github.com/BrenoAqua/Senren (https://github.com/BrenoAqua/Senren/releases/download/v5.1.0/Senren.v5.1.0.apkg)
- jp-mining-note: https://github.com/Aquafina-water-bottle/jp-mining-note ; fork https://github.com/Arbyste/jp-mining-note (https://github.com/Arbyste/jp-mining-note/releases/download/0.11.0.6/0.11.0.6-jpmn_example_cards.apkg)
- Kiku: https://kiku-docs.vercel.app/
- jidoujisho (archived): https://github.com/arianneorpilla/jidoujisho
- Hoshi Reader: https://github.com/Manhhao/Hoshi-Reader

**Other services**
- jpdb FAQ: https://jpdb.io/faq
- Migaku: https://migaku.com/learn-japanese

**Paid, bundled and expression decks**
- PLAYNESE N2 Business: https://payhip.com/b/84suD
- Kotoba *Business Japanese*: https://www.storytel.com/sg/books/business-japanese-1717164
- *101 Common Japanese Idioms*: https://nextory.com/de/book/101-common-japanese-idioms-in-plain-english-2544647
- *Sound Words in Japanese*: https://storytel.com/sg/books/sound-words-in-japanese-99-essential-sound-and-action-words-in-japanese-1871346
- BOOTH: https://booth.pm/en/items/6920715 ; https://booth.pm/ja/items/6922021
- Bunpro keigo thread: https://community.bunpro.jp/t/keigo-deck/122776
- Tobira web audio: https://tobiraweb.9640.jp/?p=1945
- JF booklist: https://www.jpf.go.jp/j/urawa/j_library/booklist/dl/BL16-2018.pdf

**Inspection scripts and downloads (local, for reproducibility)**
- `C:\Users\trinh-v\AppData\Local\Temp\claude\ad1c1fd31c67307a\43f64388-07fc-4045-ac80-4a54f3550946\scratchpad\scripts\jp-advanced\inspect_apkg.py`, `ik_probe.py`, `ik_samples.py`, `ik_info_parse.py`, `tmpl_check.py`, `aw_search.py`
- Downloads under `C:\Users\trinh-v\AppData\Local\Temp\claude\ad1c1fd31c67307a\43f64388-07fc-4045-ac80-4a54f3550946\scratchpad\downloads\` (`immersionkit-single`, `ik-drama_*`, `lapis`, `senren`, `jpmn`)
