# English advanced (B2–C2) Anki decks for spoken expressiveness with full-sentence audio (state as of 2026-11-13)

Scope note for the report writer: the user's priority update (relayed mid-task) says real-life sentences matter more than word lists. A deck that covers a C1/C2, Oxford or EVP word list "like a book" counts as a FAIL even if it has sentence audio. This file is therefore ordered as follows: (1) shortlist; (2) the authentic-media route (tools and pre-made media decks); (3) word, idiom and collocation list decks, labelled "reference only, does not meet the user's goal"; (4) community searches (JP/CN/VN), copyright and takedowns; (5) sources.

Evidence labels: [VERIFIED-INSPECTED] means I downloaded or inspected the files myself. [VERIFIED-DOCS] means an official page, README, AnkiWeb's own deck data or sample cards. [COMMUNITY] means user reports or reviews. [MARKETING] means creator promotion only. [UNVERIFIED] means not confirmed.

How the AnkiWeb data was obtained: AnkiWeb deck pages are client-rendered, and WebFetch returned empty pages. I read the page's own data endpoint `https://ankiweb.net/svc/shared/item-info?sharedId=<id>`, which is the protobuf call the deck page makes. It returns title, last-updated date, note/audio/image counts, description, reviews, thumbs and the sample notes shown on the page. Samples quoted below come from that endpoint, so they are [VERIFIED-DOCS]. AnkiWeb renames sample media to 0.mp3, 1.mp3 and so on, so original filenames are not visible.

**Blocker:** throughout the session, AnkiWeb's search endpoint (`/svc/shared/list-decks`) and its deck downloads (`/svc/shared/download-deck/<id>?t=<key>`) returned HTTP 429 Too Many Requests. The IP was apparently shared with parallel research agents, and the GitHub API was rate-limited too. As a result, no AnkiWeb .apkg could be downloaded or inspected, and AnkiWeb could not be searched systematically. Deck discovery relied on web search plus direct ID look-ups. The only .apkg I inspected is the GitHub-hosted Ecattea COCA deck.

---

## Top findings & recommended shortlist

### Takeaway
I found no pre-made Anki deck that fully meets the bar with evidence at the "verified" level. That bar is authentic native speech, full-sentence or full-line native audio, C1–C2 relevance, and coverage of workplace, debate and presentation registers.

- **Best fit:** self-mined sentence decks from real media. The two routes are Netflix via Language Reactor (original audio clip per line) and your own video or audio files via subs2srs, movies2anki or mpvacious (per-line audio clips).
- **Closest pre-made decks:** these are niche, mostly unverifiable or rights-questionable media decks:
  - Glassy-Gaia (Gumroad): TED-Ed, 13 Reasons Why, Stranger Things and Despicable Me decks, with Vietnamese subtitles included. Evidence is [MARKETING] only.
  - Kelciour's pre-made subs2srs movie and TV samples: [VERIFIED-DOCS] structure, but distributed privately.
  - Kendra's connected-speech listening deck (AnkiWeb, Chinese community): verified two audio tracks per note, but phrase-level.
- **List decks:** every Oxford, EVP, idiom, phrasal-verb and collocation deck I found is "reference only". Either it has no sentence audio, or its sentence audio is TTS, or its sentences are short invented dictionary/textbook lines.

### Cited Findings
**Primary route A: Language Reactor on Netflix**
- Netflix exports keep the original show audio. YouTube exports get AI-generated audio instead. [COMMUNITY] A forum responder wrote on 2025-12-03: "The original audio is only preserved for Netflix cards… This does not work for YouTube, and playback is with AI." — [LR forum: export real youtube audio](https://forum.languagelearningwithnetflix.com/t/export-real-youtube-audio/36419). A 2024 user reported the same problem. — [LR forum: Exporting original audio from YouTube to Anki](https://forum.languagelearningwithnetflix.com/t/exporting-original-audio-from-youtube-to-anki/20178)
- Export formats are Print, Excel, Anki, CSV and JSON. Ticking "Include Media" adds audio and images. [COMMUNITY] — [LR forum: How to Export (Guide), 2024-04-25](https://forum.languagelearningwithnetflix.com/t/how-to-export-guide/19596)
- With "Include media", the export is a CSV plus media files in a zip. [COMMUNITY] — [Anki Forums: Export from Language Reactor](https://forums.ankiweb.net/t/export-from-language-reactor/40423/2)

**Primary route B: subs2srs and similar tools on your own media**
- subs2srs "parses through a subtitle file, extracts the dialog and timing information" and generates "audio clips, snapshots, and video clips for each line of dialog". It can batch-process whole TV seasons. [VERIFIED-DOCS] — [subs2srs](https://subs2srs.sourceforge.net/); [SourceForge files, v29.7](https://sourceforge.net/projects/subs2srs/files)

**Pre-made media decks**
- Kelciour's pre-made English subs2srs decks [VERIFIED-DOCS]: subtitles manually resynced; the "first 10-15 minutes or about 50-100 cards" of each film converted; a 5–15 s video clip on the front; "subtitle line and the audio file" on the back. — [Kelciour Notion, English - 3](https://kelciour.notion.site/English-3-263745ea25208026b057f019153b6378)
- Glassy-Gaia's Gumroad shop sells English media decks: TED-Ed (B1–C1, $0+), 13 Reasons Why (B2–C1, $0+), Stranger Things S1/S2 (A2–B1), Despicable Me (B1–C1, $1+), Hilda, Alice in Wonderland, Cinderella, and 100+ idioms. Subtitles are offered in 20+ languages including Vietnamese and Japanese. [MARKETING] — [Glassy-Gaia Gumroad](https://glassygaia.gumroad.com/)

**No pre-made deck for the target registers**
- I found no pre-made Anki deck with native sentence audio built from authentic workplace, meeting, negotiation, debate or presentation speech. The searches covered English, Japanese, Chinese and Vietnamese. See Gaps.

### Inferences
**Recommended shortlist (preliminary scores; rubric detail is in the per-deck section)**

The hard rule applies: "primary" requires verified full-sentence audio. Scores are on 100 points.

1. **PRIMARY: self-mined Netflix line cards via Language Reactor.** Real per-line audio; Netflix only. ~78/100.
   - Best fit for natural spoken English, humor, sarcasm and emotional register.
   - The user curates the content, so level and register are whatever they choose.
   - Main risks: export bugs, the Pro cost, and the fact that YouTube gives AI audio.
2. **PRIMARY: subs2srs, movies2anki or mpvacious on files the user owns or has legally downloaded.** ~80/100.
   - Suitable sources: dramas, talk shows, TED talks, interviews, podcasts with transcripts.
   - Verified per-line audio clips. The most control over source and register, including British content.
   - Requires work. Unfiltered decks are huge, so the user should mine selectively.
3. **CONDITIONAL / to inspect: Glassy-Gaia "13 Reasons Why" (Seasons 3–4, claimed C1) and "TED-Ed" (B1–C1).** ~70–75/100 if the claims hold.
   - Promising because the format is built around the full line, with Vietnamese subtitles.
   - Evidence is [MARKETING] only, so this is not primary until inspected.
   - TED-Ed narration is scripted explainer English, not conversation.
4. **CONDITIONAL: Kelciour pre-made subs2srs movie and TV samples.** ~65/100.
   - Authentic line audio [VERIFIED-DOCS].
   - Only the first 10–15 minutes of each title, mostly family and animated films, distributed privately for a donation or on commission.
5. **SECONDARY (listening skill, not C1 content): Kendra's Language School connected-speech deck (AnkiWeb 1364160335).** ~55/100.
   - Every note has normal-speed and slow audio [VERIFIED-DOCS].
   - Short, simple phrases, chosen to train decoding of connected speech.
6. **SCAFFOLD ONLY (fails the user's "not a book list" rule): "English. C1 Words, Idioms, Phrasal Verbs. American Accent." (AnkiWeb 524918335).** ~60/100.
   - A C1 word list with short invented example sentences, some of them workplace-flavoured. An Example Audio field is present.
   - The audio is probably TTS [UNVERIFIED].
   - Useful as a checklist of C1 items, not as a real-life sentence source.

**What is missing, and how to fill it**
- Gap: authentic multi-clause native audio in professional registers (meetings, negotiation, presentations, debate).
- Fill it by mining:
  - TED/TEDx talks and conference keynotes, for presentation rhetoric;
  - workplace or legal dramas on Netflix (via Language Reactor), for persuasion, disagreement and sarcasm;
  - interview and talk podcasts, via a transcription-to-Anki tool such as gogadget [VERIFIED-DOCS snippet only].
- Use list decks (Oxford Phrase List, PHaVE, collocations) only as a checklist of items to look for in mined material. Where a list item has no authentic example, neural TTS could voice it, but that is a fallback.

### Gaps
- No AnkiWeb .apkg could be inspected (HTTP 429). Audio durations, TTS tags and the presence of the audio files themselves in the media map are therefore unverified for every AnkiWeb deck.
- I could not run a systematic AnkiWeb keyword search (HTTP 429). Some relevant AnkiWeb decks may exist that I did not find, for example other subs2srs English TV decks, "Friends" decks or Tatoeba English audio decks.
- Glassy-Gaia decks require a Gumroad checkout with an email address. I did not provide one, so the decks themselves were not inspected.
- The Reddit post "My Anki Flashcards Collection | Pre-Made Subs2SRS English Anki Decks, Part 1" (r/Anki, 2025-03-30) returned 403 on every route I tried. Its details are known only from search-engine snippets.

---

## Authentic-media route: tools and pre-made media decks (the user's priority)

### Takeaway
The only reliable way to get advanced, natural, multi-clause native sentences with real audio is per-line clips from real media.

- **Language Reactor:** the export carries the original audio only for Netflix.
- **subs2srs-family tools:** verified per-line audio from local files.
- **asbplayer:** free and open-source, works on Netflix and YouTube. Its audio-capture details were not confirmed in the pages I could read.
- **Pre-made media decks:** they exist (Kelciour, Glassy-Gaia), but they are small or partial, distributed off AnkiWeb, and legally grey. None could be inspected.

### Cited Findings

#### 1. Language Reactor: Netflix/YouTube to Anki export (tool; produces a self-mined deck)
- **Name / creator / URL:** Language Reactor (formerly Language Learning with Netflix). Chrome extension. [Export help](https://languagereactor.com/help/export); [Pro page](https://languagereactor.com/pro-mode). Both official pages are client-rendered, and WebFetch returned only the title.
- **Saved item types:** phrases, words with context, and words without context. In Anki exports, the context appears with the marked word removed. The help page lists dialogue fields, including audio clip media filename options. [VERIFIED-DOCS via search snippet; page body not retrievable] — [LR help: export](https://languagereactor.com/help/export)
- **Export formats and media:** Print/Excel/Anki/CSV/JSON; "Include Media" adds audio and images. [COMMUNITY, 2024-04-25] — [LR forum guide](https://forum.languagelearningwithnetflix.com/t/how-to-export-guide/19596)
- **Sentence audio:** the original line audio for Netflix; AI-generated audio for YouTube. [COMMUNITY, 2024-05 and 2025-12] — [thread 36419](https://forum.languagelearningwithnetflix.com/t/export-real-youtube-audio/36419); [thread 20178](https://forum.languagelearningwithnetflix.com/t/exporting-original-audio-from-youtube-to-anki/20178)
- **Accent:** whatever the show uses (US, UK or other).
- **Known problems** [COMMUNITY]:
  - "the Anki export feature is completely broken in my opinion".
  - Cards showed the note-type name as front text.
  - Some exported cards fell back to TTS.
  - Users need the "LLNTemplate" note type and a Tab separator.
  - Sources: [LR forum Anki Export/Import](https://forum.languagelearningwithnetflix.com/t/anki-export-import/7422); [LR forum guide](https://forum.languagelearningwithnetflix.com/t/how-to-export-guide/19596)
- **Price:** Pro is about US$5/month, $14 per 3 months or $28/year according to third-party and competitor sources. [UNVERIFIED; official pricing page not readable] Pro adds "unlimited word and phrase saving" and, per the same competitor material, exports with audio, images and context. [MARKETING, competitor blog] — [Trancy: LR vs Trancy 2026](https://www.trancy.org/blog/language-reactor-pro-vs-trancy-2026-which-is-better-for-language-learners-31f9d225200580a48aa8c5f28602a2b3)
- **Platform:** Chrome desktop extension; no mobile app. [MARKETING/third-party] The resulting Anki deck works on AnkiDroid and AnkiMobile like any audio deck [inference].
- **Status in 2026:** forum active through at least 2026-05 (topic "Add Youtube Audio to Flash Cards", 2026-05-05). [VERIFIED-DOCS, forum listing] — [thread 20178](https://forum.languagelearningwithnetflix.com/t/exporting-original-audio-from-youtube-to-anki/20178). Competitor blogs are publishing "switch from Language Reactor" posts in 2026. [MARKETING] — [Trancy blog](https://www.trancy.org/blog/how-to-switch-from-language-reactor-to-trancy-in-2026-without-losing-vocabulary-35b9d22520058127ae80f77fd343131f)
- **Samples:** none obtained, since a sample would require the user's own saved items.

#### 2. asbplayer + AnkiConnect (tool)
- **Description:** "a language-learning assistant that makes it easier to learn languages through subtitled videos". Free and open-source. Comes as a website (local files) and a browser extension (streaming). [VERIFIED-DOCS] — [asbplayer docs](https://docs.asbplayer.dev/docs/intro)
- **Features** [VERIFIED-DOCS] — [GitHub killergerbah/asbplayer](https://github.com/killergerbah/asbplayer):
  - auto-detected subtitles on Netflix and YouTube;
  - a generic fallback that detects subtitles on about "85% of all other streaming services";
  - "create high-quality, multimedia flashcards";
  - requires the AnkiConnect plugin; the card creator opens with Ctrl+Shift+X;
  - licence AGPL-3.0-or-later.
- **Recent release:** the Firefox add-on was at v1.12.0, last updated 2025-09-27 (search snippet). [VERIFIED-DOCS snippet] — [AMO listing](https://addons.mozilla.org/firefox/addon/asbplayer-learn-with-subs). A Firefox-for-Android build exists. [VERIFIED-DOCS, README reviewer notes]
- **Unconfirmed:** whether and how the sentence audio clip is captured from DRM streams. The pages I fetched do not describe the audio capture mechanism. [UNVERIFIED]
- **Community guides:** mostly Japanese-focused. A Vietnamese-language version of a Netflix/YouTube sentence-mining guide exists. [COMMUNITY] — [soyuz18 Notion guide](https://soyuz18.notion.site/Sentence-mining-from-Netflix-and-YouTube-with-asbplayer-83a03590cd8349ba81ca10340645b565)

#### 3. subs2srs / Stos / mpvacious / Immersive / movies2anki / gogadget (local-file tools)
- **subs2srs:** per-line audio clips, snapshots and video clips; batch processing of episodes. Latest source release v29.7 on SourceForge. [VERIFIED-DOCS] — [subs2srs](https://subs2srs.sourceforge.net/); [files](https://sourceforge.net/projects/subs2srs/files)
- **Stos:** a newer cross-platform subs2srs-style tool that uses ffmpeg (search summary). [VERIFIED-DOCS snippet] — [Hyxogen/stos](https://www.github.com/Hyxogen/stos)
- **mpvacious:** subs2srs-style card creation in the mpv player via AnkiConnect. [VERIFIED-DOCS snippet] — [Ajatt-Tools/mpvacious](https://www.github.com/Ajatt-Tools/mpvacious)
- **Immersive (mpv plugin):** auto-generates cards with "sentence audio clips, screenshots from the video". Requires AnkiConnect. [VERIFIED-DOCS snippet] — [Ben-Kerman/immersive](https://www.github.com/Ben-Kerman/immersive)
- **gogadget (Python):** downloads audio/video, "automatically transcribing subtitles from videos and podcasts", and produces "filtered Anki decks with sentence audio / translations / screenshots / definitions". This is the relevant route for podcasts and interviews. [VERIFIED-DOCS snippet; PyPI page body failed to load] — [gogadget on PyPI](https://pypi.org/project/gogadget)
- **movies2anki:** Kelciour's add-on, which converts movies with subtitles for watching inside Anki. [VERIFIED-DOCS snippet] — [kelciour/movies2anki](https://awesome.ecosyste.ms/projects/github.com%2Fkelciour%2Fmovies2anki)

#### 4. Kelciour pre-made English subs2srs decks (movie/TV samples)
- **Creator:** Kelciour (well-known Anki deck and add-on author). [Notion: English - 3](https://kelciour.notion.site/English-3-263745ea25208026b057f019153b6378)
- **Format** [VERIFIED-DOCS]:
  - "The subtitles were manually resynced to better match the audio."
  - "The first 10-15 minutes or about 50-100 cards were converted to Anki."
  - "The front side includes the video clip about 5-15 seconds long."
  - "The back side includes the subtitle line and the audio file."
- **Titles listed** (about 60) include:
  - classic dialogue films: 12 Angry Men, All About Eve, Some Like It Hot, The Godfather, To Kill a Mockingbird, The Shawshank Redemption, Catch Me If You Can, Forrest Gump;
  - British titles: Bridget Jones's Diary, Sharpe's Rifles, Three Men in a Boat;
  - many Disney/Pixar/animated titles.
- **TV shows** [COMMUNITY via search snippets; post itself 403]: a 2025-03-30 r/Anki post, "My Anki Flashcards Collection | Pre-Made Subs2SRS English Anki Decks, Part 1 (10,000+ notes)", lists Friends, The Office, How I Met Your Mother, The Big Bang Theory, Sex and the City, Prison Break and Avatar: The Last Airbender.
  - TV decks contain "the 1st episode or 150-300 cards" and were "converted as is with a short padding added" (not resynced).
  - The decks are offered "for a cup of coffee in return or on commission".
  - A commenter questioned fair use.
  - Source: [r/Anki post mirror](https://reddit.birdcat.cafe/r/Anki/comments/1jnfayu/my_anki_flashcards_collection_premade_subs2srs). That this post is by Kelciour is [UNVERIFIED].
- **Availability:** no public download links on the Notion page; the bullet items are plain text. [VERIFIED-INSPECTED: Notion block data contains no file or link blocks for these titles]
- **Notes / audio / CEFR:** 50–100 notes per film; line audio from the film soundtrack (native, mixed US/UK accents depending on the film) [VERIFIED-DOCS]; no CEFR tagging [inference].
- **Samples:** none obtained.

#### 5. Glassy-Gaia "Learn English from … – Multilingual Anki Decks" (Gumroad)
- **Shop:** [glassygaia.gumroad.com](https://glassygaia.gumroad.com/). The GitHub repo [GLASSY-GAIA/youtube-ted-ed-anki-english-en](https://github.com/GLASSY-GAIA/youtube-ted-ed-anki-english-en) has folders for about 29 TED-Ed videos, for example "this_tool_will_help_improve_your_critical_thinking", "what_makes_something_kafkaesque", "how_could_so_many_people_support_hitler" and "why_you_procrastinate_even_when_it_feels_bad". [VERIFIED-INSPECTED repo tree] The folders hold images and placeholder files, not .apkg files. [VERIFIED-INSPECTED]
- **English products and claimed levels** [MARKETING]:
  - TED-Ed Animation Videos: $0+, "Intermediate → Advanced (B1–C1 CEFR)".
  - 13 Reasons Why (Series 1–4): $0+, "Upper-Intermediate → Advanced (B2–C1)"; Season 3 "B2+ → C1", Season 4 "Advanced (C1)".
  - Despicable Me 1–4: $1+, B1–C1.
  - Stranger Things S1/S2: $0+, "A2–B1".
  - Also: Hilda, Alice in Wonderland, Cinderella, and "Master 100+ English Idioms".
  - Sources: [TED-Ed product](https://glassygaia.gumroad.com/l/english_ted_ed_videos); [13 Reasons Why](https://glassygaia.gumroad.com/l/13_reasons_why); [Despicable Me](https://glassygaia.gumroad.com/l/despicable_me); [Stranger Things 01](https://glassygaia.gumroad.com/l/english_stranger_things_01)
- **Card design** [MARKETING]:
  - Front: "🎧 Listen carefully… 🗣️ Speak or ✍️ write what you hear… Reveal hints". This is listening-first plus dictation or production.
  - Back: subtitles and translation in the chosen language, plus "Smart Notes" explaining key words, phrases, tone and usage.
  - "Multilingual Subtitles – 20+ languages", including Vietnamese and Japanese.
- **Idiom deck** [MARKETING] — [english_idiom](https://glassygaia.gumroad.com/l/english_idiom): "Native Audio… 🔊 Idiom pronunciation 🔊 Example sentence audio"; "AI-Generated Illustrations"; 3 example levels per idiom.
- **Sample card** (from the creator's preview screenshot `card-image/back-card-ted-ed.png`, viewed as an image; [MARKETING]):
  - Line: "Say you're standing in front of a door, ready to pull it open."
  - Chinese: "假想你正站在一扇门前，准备拉门".
  - Vietnamese: "Giả dụ bạn đang đứng trước một cái cửa, sẵn sàng kéo mở nó."
  - Note: "Say: imperative to prompt imagination → Say you are planning a surprise party for a friend."
  - Note: "ready to pull it open: phrase showing preparedness → She was ready to make her presentation to the board."
  - Typed-answer check row: "Say youre standing in front of a door ready to pull it open".
  - The screenshot does not name the source TED-Ed video. The two "→" example sentences are creator-written, not from the video [inference].
- **Audio source:** presumably the original soundtrack ("Hear how native speakers sound"). [MARKETING; not inspected]
- **Licensing risk:** the decks bundle film and Netflix-series audio and stills. TED-Ed videos carry a Creative Commons licence on TED's site per an app listing [UNVERIFIED version] — [TEDICT app](https://apps.apple.com/app/id554188888).
- **Maintenance:** single creator, active in 2025–2026 (Korean drama titles from 2025 appear in the shop). [inference from product list]

#### 6. Kendra's Language School connected-speech deck (AnkiWeb 1364160335)
- **Title:** "英语短语连读听力特训—简单却不易听懂--肯德拉语言学校 - Kendra's Language School" ("English phrase connected-speech listening drills: simple but hard to catch").
- **Basics** [VERIFIED-DOCS] — [AnkiWeb 1364160335](https://ankiweb.net/shared/info/1364160335):
  - Last updated 2022-02-08; 42.4 MB; 332 notes, 664 audio, 332 images.
  - 15 thumbs up, 15 reviews, the latest 2026-05-28.
  - Description is only a YouTube playlist link.
- **Fields:** 序号 (number) / 常速 (normal speed) / 慢速 (slow) / 图片 (image) / 备注 (notes) / Tags.
- **Samples (verbatim, 2 obtained):**
  - {序号: "0269", 常速: "[sound:0.mp3]", 慢速: "[sound:1.mp3]", 图片: "[image:2.jpg]", 备注: ""}
  - {序号: "0239", 常速: "[sound:3.mp3]", 慢速: "[sound:4.mp3]", 图片: "[image:5.jpg]", 备注: ""}
  - The English text appears to live only in the image. [inference]
- **Review:** 2026-05-28: "为什么点击答案后无法自动打开图片？还要手动打开" (why doesn't the image open automatically after revealing the answer; I have to open it manually). [COMMUNITY]
- **Unknown:** whether the speakers are native, the accent, and the clip durations. [UNVERIFIED; download blocked]

### Inferences

#### Preliminary scores, media route (100 points)
Criteria and maximums: Audio 25, Naturalness 20, Level 15, Speaking chunks 15, Structure 10, Reliability 10, Extras 5.

**Self-mined Netflix deck via Language Reactor: ~78**
- Audio 21/25: real per-line clips on Netflix; AI audio on YouTube; reported glitches.
- Naturalness 19/20: authentic scripted drama dialogue.
- Level 13/15: depends on the user's selection.
- Speaking chunks 11/15: depends on mining discipline.
- Structure 3/10: no built-in progression.
- Reliability 6/10: export bugs reported.
- Extras 5/5: screenshots, translations.
- Uncertainty: high on the current Pro feature set and on export reliability in 2026.

**subs2srs-family on own files: ~80**
- Audio 22/25: verified per-line clips; timing depends on subtitle sync.
- Naturalness 19/20.
- Level 14/15: free choice, including UK media, TED, podcasts.
- Speaking chunks 11/15.
- Structure 3/10.
- Reliability 8/10: mature tools.
- Extras 3/5.
- Uncertainty: effort and setup; legality of sources.

**asbplayer: ~78 (provisional)**
- Same profile as subs2srs for streaming.
- Audio scored 20/25 provisionally because the clip mechanism was not verified this session.

**Glassy-Gaia 13 Reasons Why S3–S4 / TED-Ed: ~72 (provisional)**
- Audio 18/25: claimed, not inspected.
- Naturalness 17/20: teen-drama dialogue is very natural; TED-Ed is scripted narration.
- Level 12/15: claimed B2–C1.
- Speaking chunks 11/15: "Smart Notes" on phrases.
- Structure 7/10.
- Reliability 3/10: unverifiable, rights risk.
- Extras 4/5: Vietnamese subtitles, images.
- Uncertainty: very high.

**Kelciour subs2srs samples: ~63**
- Audio 21/25: verified per-line audio.
- Naturalness 19/20.
- Level 8/15: many animated or family films; classics are dated.
- Speaking chunks 7/15.
- Structure 2/10: first 10–15 min only.
- Reliability 3/10: private distribution.
- Extras 3/5: video clips.
- Uncertainty: availability.

**Kendra connected-speech: ~55**
- Audio 18/25: two tracks per note; speakers unverified.
- Naturalness 10/20: drill phrases.
- Level 6/15.
- Speaking chunks 8/15.
- Structure 6/10.
- Reliability 4/10: 2022 and abandoned-looking.
- Extras 3/5.
- Uncertainty: durations and content unseen.

#### Domain coverage estimate [inference]
- **Netflix/TV mining:** casual talk, humor, sarcasm, emotional expression, persuasion and disagreement; workplace too, if the user picks workplace or legal dramas.
- **TED and talks:** presentations, rhetoric, storytelling.
- **Podcasts and interviews (gogadget-type tools):** unscripted speech, critical commentary.
- **Business meetings and negotiation with authentic audio:** no pre-made source found. Self-mining from talk shows, earnings calls or panel discussions would be needed.

### Gaps
- The Language Reactor official help, pricing and Pro pages could not be read (client-rendered).
- asbplayer's audio-capture behaviour for DRM streams was not confirmed.
- Glassy-Gaia and Kelciour decks could not be downloaded. Note counts, audio durations and actual sentences are unknown, apart from one marketing screenshot.
- I found no maintained pre-made TED-talk (not TED-Ed), podcast, news or business-meeting Anki deck with native audio.
- On Immersion Kit for English: the official material found describes Immersion Kit as Japanese-only (anime sentences with audio and screenshots, exportable to Anki). I found no English-target equivalent sentence bank with Anki export. [VERIFIED-DOCS for Immersion Kit's scope] — [Tofugu: Immersion Kit](https://tofugu.com/japanese-learning-resources-database/immersion-kit); [Immersion Kit Patreon](https://www.patreon.com/immersionkit/about?l=ru-RU)

---

## Word, idiom, phrasal-verb and collocation list decks (reference only, does not meet the user's goal unless noted)

### Takeaway
- **Sentence audio present but problematic:**
  - The C1 American Accent deck (524918335) and 4000 Essential English Words have sentence audio. The first is probably TTS on invented one-liners; the second is A1–A2 level.
  - Ecattea COCA's "sentence audio" is online Microsoft neural TTS fetched by the card template at review time. [VERIFIED-INSPECTED]
- **No sentence audio:** every idiom, phrasal-verb, collocation and EVP deck found.
- **Not found as Anki decks with sentence audio:** Oxford 5000, OPAL, Oxford Phrase List, EVP, PHaVE, "in Use" and Speak English Like an American.

### Cited Findings

#### A. "English. C1 Words, Idioms, Phrasal Verbs. American Accent." (AnkiWeb 524918335)
- **Basics** [VERIFIED-DOCS] — [AnkiWeb 524918335](https://ankiweb.net/shared/info/524918335):
  - Last updated 2025-12-09; 116.9 MB; 1,731 notes; 3,039 audio; 0 images.
  - 35 thumbs up / 1 down; 36 reviews, the latest 2026-10-15.
- **Origin and audio:** "based on the popular 'Close-up Word List C1' by kelciour@gmail.com… Switched all audio to a US accent; Added lots of my own words and sentences".
  - The audio count (3,039 for 1,731 notes) suggests word audio on every note plus Example Audio on most of them [inference].
  - "Switched all audio to a US accent" across 3,000+ files strongly suggests TTS [UNVERIFIED].
- **Fields:** Front (example sentence) / Back (word) / Definition / Audio / Example Audio. The card is sentence-first recognition.
- **Samples (verbatim, AnkiWeb sample notes):**
  - {Front: "“Her reproach was clear in the meeting.”", Back: "reproach", Definition: "express disapproval", Audio: "[sound:0.mp3]", Example Audio: "[sound:1.mp3]"}
  - {Front: "“Don’t overpromise the client; it’ll backfire.”", Back: "overpromise", Definition: "promise more than possible", Audio: "[sound:2.mp3]", Example Audio: "[sound:3.mp3]"}
  - {Front: "“Be mindful of tone in emails.”", Back: "mindful", Definition: "conscious and attentive", Audio: "[sound:4.mp3]", Example Audio: "[sound:5.mp3]"}
- **Assessment** [inference]: the sentences are short, invented and workplace-flavoured. They are useful for an IT/DX professional, but they are not authentic speech.
- **Score: ~60.**
  - Audio 15/25: sentence audio present, probably TTS.
  - Naturalness 8/20: one-liners.
  - Level 13/15: C1.
  - Speaking chunks 10/15: idioms and phrasal verbs included.
  - Structure 6/10.
  - Reliability 7/10: updated 2025-12, positive reviews.
  - Extras 1/5.
  - Uncertainty: audio type.

#### B. "Advanced English Vocabulary" (AnkiWeb 1980021227) and parts II–V
- **Basics** [VERIFIED-DOCS] — [AnkiWeb 1980021227](https://ankiweb.net/shared/info/1980021227):
  - Last updated 2026-03-02; 249.8 MB; 1,400 notes; 1,400 audio; 1,412 images.
  - 205 up / 7 down; 212 reviews, the latest 2026-11-03. The deck is marked NSFW.
- **Content:** "words, phrasal verbs, idioms… aimed at advanced or, maybe, upper-intermediate learners… context (sometimes can be absent)… robotic pronunciation".
- **Card types:** Forward (image + word → definition) and Backward (definition → typed word with first/last-letter hint).
- **Samples:**
  - {Term: "clear the air", Definition: "calm anger and remove misunderstanding", Context: "We were tired of fighting, so we decided to start talking and clear the air", Audio: "[sound:1.mp3]"}
  - {Term: "jagged", Context: ""}
  - {Term: "ascetic", Context: "Ascetic life of Buddhist monks; asceticism."}
- **Assessment:** one audio file per note means term audio only, TTS. No sentence audio. Fails the hard rule.
- **Score: ~48.**
  - Audio 2/25.
  - Naturalness 7/20.
  - Level 12/15.
  - Speaking chunks 9/15.
  - Structure 6/10.
  - Reliability 8/10.
  - Extras 5/5: images.
  - Rights: the author openly says content was borrowed from other decks and apps [VERIFIED-DOCS].

#### C. Ecattea "COCA-English-Anki-Deck" (GitHub; inspected)
- **Release** [VERIFIED-INSPECTED]: COCA-English.apkg, tag 2026-04-04, 3.8 MB. Earlier tags 2025.06.16 and 2025.06.20. — [Ecattea/COCA-English-Anki-Deck](https://github.com/Ecattea/COCA-English-Anki-Deck)
- **Structure** [VERIFIED-INSPECTED]:
  - anki21b (zstd) collection; 21,788 notes, 21,788 cards.
  - Note type "COCA-English"; one template ("Card 1").
  - Fields: Word, uuid, uid, Part of Speech, Grammar, Pronunciation/IPA, Audio, Definition, Example 1–5.
  - Five sub-decks by COCA rank; 2 files in the media map.
  - 0 [sound:] references.
- **Audio** [VERIFIED-INSPECTED]:
  - The Audio field holds a remote Merriam-Webster URL, for example `https://media.merriam-webster.com/audio/prons/en/us/mp3/l/line0001.mp3`.
  - The template's `setExampleTTS()` calls third-party endpoints `https://anki-eng.0w0.live/` and `https://ms-ra-forwarder-for-ifreetime-v9q1.vercel.app/` ("ms-ra-forwarder" implies a Microsoft Read-Aloud neural TTS proxy) with `speed: -4`.
  - Consequence: all audio needs internet and depends on unofficial proxies.
- **README:** examples use TTS "with manually adjusted pacing, stress, and intonation"; licence CC BY-NC-SA 4.0. [VERIFIED-DOCS] The README does not state the source of the examples, but the inspected examples match Merriam-Webster Learner's style.
- **Samples (verbatim, randomly drawn from the collection):**
  - {Word: "line", Definition: "a long and thin rope, string, etc.", Example 1: "a fishing <em>line</em>", Example 2: "We hung the wet clothes on the <em>line</em>. [=<em>clothesline</em>]"}
  - {Word: "beautiful", Definition: "very attractive in a physical way", Example 1: "a <em>beautiful</em> young woman/child", Example 2: "You have the most <em>beautiful</em> smile/eyes."}
  - {Word: "cut", Definition: "to move suddenly in a different direction", Example 1: "The driver <em>cut</em> across three lanes of traffic to get to his exit and nearly caused an accident.", Example 2: "(<em>American football</em>) The runner <em>cut</em> to his left to avoid being tackled."}
- **Score: ~45.**
  - Audio 6/25: online TTS only.
  - Naturalness 8/20: dictionary examples.
  - Level 5/15: top 5,000 lemmas.
  - Speaking chunks 6/15.
  - Structure 9/10.
  - Reliability 7/10: maintained, but depends on fragile proxies.
  - Extras 4/5.
  - Mobile: needs JS plus network on AnkiDroid/AnkiMobile [inference].

#### D. 5mdld "anki-english-60k-decks" (eggrolls-FREQ60K-MWLD)
- **Content** [VERIFIED-DOCS] — [5mdld/anki-english-60k-decks](https://github.com/5mdld/anki-english-60k-decks):
  - 60,000 words, about 66,000 cards.
  - Merriam-Webster word audio, with Wiktionary gap-fill.
  - Example sentences "synthesized via online TTS".
  - AI-generated Chinese translations.
  - Merriam-Webster content is excluded from the licence.
- Reference only; not inspected.

#### E. "4000 Essential English Words 1 [en-en] M4R4M" (AnkiWeb 735471551)
- **Basics** [VERIFIED-DOCS] — [AnkiWeb 735471551](https://ankiweb.net/shared/info/735471551):
  - Last updated 2015-06-18; 112 MB; 600 notes; 1,800 audio; 600 images; 50 up / 4 down.
- **Audio:** "four sounds: word pronunciation; meaning; 1-second silence; example of using the word in the sentence". This is sentence audio, likely from the book's recordings [UNVERIFIED native].
- **Samples:**
  - {Front: "inform", Back: "[image:3.jpg]", Sound: "[sound:0.mp3]", Meaning: "[sound:1.mp3]", Example: "[sound:2.mp3]"}
  - {Front: "article", …, Example: "[sound:6.mp3]"}
  - The example text sits inside the image.
- **Level:** the series spans "high beginning to advance". Book 1 is roughly A1–A2 [inference].
- **Assessment:** reference only and below target. A commercial-book derivative.
- **Score: ~42.**
  - Audio 16/25.
  - Naturalness 5/20.
  - Level 2/15.
  - Speaking chunks 3/15.
  - Structure 8/10.
  - Reliability 4/10: 2015.
  - Extras 4/5.

#### F. Idiom decks without audio
- **"English Idioms & Phrases Dictionary" (AnkiWeb 1070003307)** [VERIFIED-DOCS] — [AnkiWeb 1070003307](https://ankiweb.net/shared/info/1070003307):
  - Last updated 2022-07-24; 4,773 notes; 0 audio. Based on the book by Daniel B. Smith.
  - Samples:
    - {Phrase/Idiom: "as happy as a lark", Example: "I’m as happy as a lark with my wage raise."}
    - {Phrase/Idiom: "a well-oiled machine", Example: "Last month our company was like a well-oiled machine. Thank you all for that!"}
    - {Phrase/Idiom: "life and soul of the party", Example: "I am so glad that he is here. He is the life and soul of the party."}
  - Several idioms are British ("life and soul of the party").
- **"English Idioms for Everyday Use" (AnkiWeb 1584129748)** [VERIFIED-DOCS] — [AnkiWeb 1584129748](https://ankiweb.net/shared/info/1584129748):
  - Last updated 2025-12-04; 219 notes; an Audio field exists, but there are 0 audio files.
  - Recreated from Milada Broukal's out-of-print book.
  - Samples: "to hold one's breath" / "Jane said she would come to my party, but I won't hold my breath."; "a copycat"; "on second thought".

#### G. Phrasal verbs
- **No free PHaVE-based Anki deck found.** PHaVE: Garnier & Schmitt (2015), the 150 most frequent phrasal verbs with their key senses, which cover 75%+ of occurrences in COCA. UC Davis split it into 10 Quizlet sets. [VERIFIED-DOCS] — [PHaVE repository record](https://nottingham-repository.worktribe.com/output/762398); [UC Davis page](https://globalaffairs.ucdavis.edu/node/11866)
- **Refold "English Phrasal Verbs Deck" (paid)** [MARKETING] — [Refold store](https://refold.la/decks/buy/english-phrasal-verbs-deck):
  - US$24.99 one-off; the US$9/month Toolkit does not include the Anki file.
  - "150 phrasal verb priming cards" and "330 definitions with example sentences… handwritten by English teachers".
  - "Authentic native audio with an American accent". Whether the audio covers whole sentences is not stated.
  - Started from Garnier & Schmitt's research; British-only phrasal verbs removed.
  - Score ~60, provisional:
    - Audio 12/25: scope unknown.
    - Naturalness 11/20.
    - Level 9/15.
    - Speaking chunks 12/15.
    - Structure 8/10.
    - Reliability 6/10.
    - Extras 4/5.

#### H. Oxford, EVP, collocations, "in Use", Speak English Like an American
- **Oxford Phrase List** [VERIFIED-DOCS] — [Oxford Phrase List](https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford-phrase-list); [wordlists](https://www.oxfordlearnersdictionaries.com/wordlists); [OPAL](https://www.oxfordlearnersdictionaries.com/about/wordlists/opal):
  - Idioms, phrasal verbs, collocations and prepositional phrases at A1–C1.
  - "650 common phrases" now; 750 at launch per a 2019 Oxford blog.
  - OPAL is grouped by function.
- **Oxford-list decks:** no Oxford-list deck with sentence audio found. [VERIFIED-DOCS snippets]
  - ciwga/Oxford3000_Vocab uses YouGlish integration (MIT) — [ciwga/Oxford3000_Vocab](https://github.com/ciwga/Oxford3000_Vocab).
  - winterdl's Oxford 5000 repo lists audio as a TODO — [winterdl/oxford-5000](https://github.com/winterdl/oxford-5000-vocabulary-audio-definition).
- **EVP:** no EVP-derived deck found. A C1 deck with "British audio pronunciations" (AnkiWeb 1507484008) is still indexed by search engines but now returns "missing" from AnkiWeb's API, meaning removed or unshared. [VERIFIED-INSPECTED API status, 2026-11-13]
- **"in Use" series** (English Idioms / Phrasal Verbs / Collocations in Use): no AnkiWeb decks found; only Brainscape sets. [VERIFIED-DOCS snippets] Kelciour's Notion lists in-Use-derived decks, not publicly hosted:
  - English Vocabulary in Use Advanced, 286 notes;
  - Business Vocabulary in Use Advanced, 187 notes;
  - Destination C1 & C2, 5,390 notes;
  - Common American Phrases in Everyday Contexts, 2,130 notes;
  - McGraw-Hill's Conversational American English, 464 notes;
  - Cambridge Grammar of English, 1,530 notes ("Audio recordings of all the examples from the book");
  - ESLPod Glossary, 21,811 notes;
  - 101 American English Idioms ("Native speakers read each of the 101 idioms").
  - [VERIFIED-DOCS] — [Kelciour Notion: English - 2](https://kelciour.notion.site/English-2-215745ea2520800b878ae94bc9e3d0cb)
- **Speak English Like an American:** only Brainscape sets (298 cards); no Anki deck found. [VERIFIED-DOCS snippet] — [Brainscape](https://brainscape.com/flashcards/speak-english-like-an-american-995667/packs/1819624)

#### I. Tatoeba English with native audio
- **Charles Kelly (CK) recordings:** "over 190,000 English sentences with audio files recorded by me". Audio licence CC BY-NC-ND 3.0; sentences CC BY 2.0 FR. The page does not state the accent. [VERIFIED-DOCS] — [manythings.org audio](https://www.manythings.org/sentences/audio/)
- **Vuizur tatoeba-to-anki pre-built decks:** all X→English, with English as the base language. Released 2023-03-01; 37 .apkg files, including vie_eng and jpn_eng. There is no English-target deck. Edge-TTS fallback when native audio is missing. [VERIFIED-INSPECTED release asset list; VERIFIED-DOCS README] — [Vuizur/tatoeba-to-anki](https://github.com/Vuizur/tatoeba-to-anki)
- **digitalwords.net generator:** excludes English ("too many sentences"). [VERIFIED-DOCS] — [digitalwords](https://digitalwords.net/anki/tatoeba-audio/index.eng.html)
- **"Anglais essentiel : recueil de phrases" (AnkiWeb 1878660228)** [VERIFIED-DOCS] — [AnkiWeb 1878660228](https://ankiweb.net/shared/info/1878660228):
  - Last updated 2024-09-18; 2,088 notes; 2,088 audio; English→French; basic vocabulary.
  - Samples: "I shouldn't have slept with her." / "We were born out of revolution against an empire." / "We grew up together."
  - Whether the audio is native or TTS is [UNVERIFIED].
  - Level too low. Score ~45:
    - Audio 16/25.
    - Naturalness 8/20.
    - Level 2/15.
    - Speaking chunks 5/15.
    - Structure 7/10.
    - Reliability 5/10.
    - Extras 2/5.

### Inferences
- None of the list decks meets the user's goal. Their sentences are dictionary-style, textbook-invented or AI one-liners, and their audio is mostly TTS or word-only.
- The best scaffold options are:
  - the C1 American Accent deck, for C1 item coverage with workplace-flavoured lines;
  - the Oxford Phrase List or PHaVE, used as a checklist and not studied as cards. For the minority of items never met in authentic material, the user could add neural TTS to their own example sentences.

### Gaps
- "4000 Essential English Words" Books 2–6, Oxford 5000 decks with sentence audio, and "Collocations in Use" decks were not located on AnkiWeb because search was blocked.
- I could not confirm whether the C1 American Accent deck's audio is TTS, or whether the 4000 Essential English Words audio is native.

---

## Japanese, Chinese and Vietnamese community searches; copyright and takedown status

### Takeaway
- **Japanese:** searches for DUO 3.0, 瞬間英作文 and 海外ドラマ found no shared decks with sentence audio. Bloggers recommend building your own (splitting the CD audio) for personal use only.
- **Chinese:** the community contributes the Kendra connected-speech deck and large COCA/Collins word decks without (working) sentence audio. "老友记" (Friends) and "英语口语8000句" resources exist as apps, not as Anki decks.
- **Vietnamese:** I found no Vietnamese-community English deck. The Glassy-Gaia decks ship Vietnamese subtitles.
- **Copyright:** AnkiWeb has a built-in copyright-report and suspension mechanism, and at least one candidate deck (1507484008) is now missing.

### Cited Findings
- **DUO 3.0:**
  - Search found no ready-made DUO 3.0 deck with audio. One blog splits the official "DUO 3.0 CD復習用" (review CD) per sentence; an official DUO 3.0 app exists. [COMMUNITY] — [scrapbox rmaruon DUO 3.0](https://scrapbox.io/rmaruon/%E3%80%8EDUO_3.0%E3%80%8F%E3%81%AE%E4%BE%8B%E6%96%87%E3%81%AE%E6%A7%8B%E9%80%A0%E3%82%92%E6%8A%8A%E6%8F%A1%E3%81%97%E3%81%A6%E6%B0%97%E3%81%A5%E3%81%84%E3%81%9F%E3%81%93%E3%81%A8); [appmatch DUO app guide](https://appmatch.jp/2367-2/)
  - A GitHub project, healthypackrat/duo-ldoce, generates word pronunciations from text data, not sentence audio. [VERIFIED-DOCS snippet] — [duo-ldoce](https://awesome.ecosyste.ms/projects/github.com%2Fhealthypackrat%2Fduo-ldoce)
- **瞬間英作文:** no shared deck found. Japanese results instead pointed to NGSL decks (CC BY-SA 4.0 wordlist) and Tatoeba scripts. [COMMUNITY]
- **Japanese exam books:** the levels of 鉄壁, ターゲット1900, キクタン and 速読英単語 were not verified. A general note that DUO is roughly B1–B2, ターゲット1900 roughly A2–B1 and 鉄壁 roughly B1–B2 came from a search summariser, not a source. [UNVERIFIED] Japanese university-entrance benchmarks centre on B2 — [Cambridge English Japan CEFR](https://cambridgeenglish.org/jp/exams-and-tests/cefr). None of these is C1+ speaking material [inference].
- **Chinese decks:**
  - "17641 COCA words" (AnkiWeb 1696986899): 2019-03-01; 17,641 notes; no audio ("这个没有语音", i.e. this one has no audio). Its audio version is said to be AnkiWeb 1812611404, not checked. Fields include 柯林斯解释 (Collins definitions). [VERIFIED-DOCS]
  - "coca20000fenxiang" (AnkiWeb 904136143): 2017-03-29; 14,816 notes; only 29 audio files. [VERIFIED-DOCS]
  - Both are reference only.
- **Chinese media and phrase resources (apps, not Anki):**
  - "老友记台词学英语" (learn English from Friends lines): an iOS app with line-by-line original audio for all 10 seasons. [MARKETING] — [App Store](https://apps.apple.com/us/app/%E8%80%81%E5%8F%8B%E8%AE%B0%E5%8F%B0%E8%AF%8D%E5%AD%A6%E8%8B%B1%E8%AF%AD/id6748722804)
  - "英语口语8000句" (8,000 spoken-English sentences): an app with native-speaker audio. [MARKETING] — [App Store](https://apps.apple.com/np/app/%E8%8B%B1%E8%AF%AD%E5%8F%A3%E8%AF%AD8000%E5%8F%A5-%E6%A0%87%E5%87%86%E5%8F%91%E9%9F%B3%E5%90%AC%E5%8A%9B%E9%98%85%E8%AF%BB%E8%AF%AD%E6%B3%95%E9%9F%B3%E6%A0%87%E5%AD%A6%E4%B9%A0%E6%9C%89%E5%A3%B0%E8%B5%84%E6%96%99/id1209822862)
  - A 2015 Chinese-forums post offered about 600,000 English/Chinese subtitle cards from US/UK TV shows. Links were reported dead by 2017. [COMMUNITY] — [Chinese-forums thread](https://chinese-forums.com/forums/topic/49841-here-is-huge-collection-of-simplified-chineseenglish-subtitle-anki-flashcards-from-most-of-my-favourite-tv-shows-around-600000)
- **Vietnamese:**
  - Searches ("bộ thẻ Anki tiếng Anh … audio idioms collocations") surfaced only international decks (COCA, MWLD, Refold).
  - Glassy-Gaia decks include Vietnamese subtitles, and the shop also sells a "Master Chinese Idioms – Bilingual (EN–VI)" deck. [VERIFIED-DOCS shop listing]
  - A Vietnamese-language asbplayer sentence-mining guide exists. [COMMUNITY] — [soyuz18 Notion](https://soyuz18.notion.site/Sentence-mining-from-Netflix-and-YouTube-with-asbplayer-83a03590cd8349ba81ca10340645b565)
- **Copyright mechanics on AnkiWeb:** the AnkiWeb frontend exposes `/svc/shared/report-copyright` and deck-info fields `is_copyright_holder` and `is_suspended`. [VERIFIED-INSPECTED, AnkiWeb JS bundle `frontend.CGtXrk30.mjs`]
- **Removed deck:** AnkiWeb 1507484008 (C1 deck with British audio, still in search indexes) returns `missing` as of 2026-11-13. [VERIFIED-INSPECTED]
- **Rights statements:**
  - "Advanced English Vocabulary" admits aggregating content from shared decks, apps and movies. [VERIFIED-DOCS]
  - Ecattea states Merriam-Webster content is not licensed. [VERIFIED-DOCS]
  - Tatoeba CK audio is CC BY-NC-ND 3.0. [VERIFIED-DOCS]
  - A commenter on the Reddit post questioned the fair use of pre-made TV subs2srs decks. [COMMUNITY]
- **Migaku and Trancy:**
  - Migaku advertises English learning from Netflix, YouTube and Disney+ with its own SRS. Anki conversion is mentioned on a Japanese page. [VERIFIED-DOCS snippet] — [Migaku learn-english](https://migaku.com/learn-english)
  - Trancy claims Anki vocabulary sync. [MARKETING] — [Trancy blog](https://www.trancy.org/blog/best-migaku-alternative-for-netflix-learning-2026-3609d2252005813882a5efac2ab03e64)

### Inferences
- **Book-derived decks** (in Use, DUO, Oxford/Cambridge examples, 4000 Essential English Words, ESLPod) are copyright-infringing when shared. They tend either to disappear from AnkiWeb (taken down or unshared) or to circulate privately, as with Kelciour's Notion catalogue.
- **Media decks** (Friends, Netflix series) carry the same risk.
- **Legally cleaner route** for the user: mine personally from subscribed or owned media for private study, and do not redistribute.
- **US vs UK:**
  - US-leaning: Language Reactor/Netflix (content-dependent), the C1 American Accent deck, Refold.
  - UK sources: Kelciour lists Bridget Jones's Diary, Sharpe's Rifles and Three Men in a Boat; British TV, BBC podcasts and UK talk shows would need self-mining. No ready UK-accent sentence deck was found at C1.

### Gaps
- I could not check whether DUO 3.0 decks were ever on AnkiWeb and later taken down, because AnkiWeb search was blocked.
- The Japanese Migaku blog lists of English decks were not readable (JavaScript-only).
- No B站 (Bilibili), 知乎 (Zhihu) or 小红书 (Xiaohongshu) English-Anki posts were retrieved.
- The キクタン and 速読英単語 levels were not researched.

---

## Full source list
- AnkiWeb deck pages, read through the page's `svc/shared/item-info` data endpoint:
  - [1364160335 Kendra connected speech](https://ankiweb.net/shared/info/1364160335)
  - [524918335 C1 American Accent](https://ankiweb.net/shared/info/524918335)
  - [1980021227 Advanced English Vocabulary](https://ankiweb.net/shared/info/1980021227)
  - [735471551 4000 Essential English Words 1](https://ankiweb.net/shared/info/735471551)
  - [1070003307 English Idioms & Phrases Dictionary](https://ankiweb.net/shared/info/1070003307)
  - [1584129748 English Idioms for Everyday Use](https://ankiweb.net/shared/info/1584129748)
  - [1878660228 Anglais essentiel (Tatoeba English)](https://ankiweb.net/shared/info/1878660228)
  - [252721431 English pronunciation & listening (beginner, 2017)](https://ankiweb.net/shared/info/252721431)
  - [1696986899 17641 COCA words](https://ankiweb.net/shared/info/1696986899)
  - [904136143 coca20000fenxiang](https://ankiweb.net/shared/info/904136143)
  - [1507484008 C1 British audio (now missing)](https://ankiweb.net/shared/info/1507484008)
- Language Reactor:
  - [LR help: export](https://languagereactor.com/help/export)
  - [LR Pro page](https://languagereactor.com/pro-mode)
  - [LR forum guide](https://forum.languagelearningwithnetflix.com/t/how-to-export-guide/19596)
  - [LR forum: export real youtube audio](https://forum.languagelearningwithnetflix.com/t/export-real-youtube-audio/36419)
  - [LR forum: YouTube original audio](https://forum.languagelearningwithnetflix.com/t/exporting-original-audio-from-youtube-to-anki/20178)
  - [LR forum: Anki Export/Import](https://forum.languagelearningwithnetflix.com/t/anki-export-import/7422)
  - [Anki Forums: Export from Language Reactor](https://forums.ankiweb.net/t/export-from-language-reactor/40423/2)
  - [Trancy: LR Pro vs Trancy 2026 (competitor)](https://www.trancy.org/blog/language-reactor-pro-vs-trancy-2026-which-is-better-for-language-learners-31f9d225200580a48aa8c5f28602a2b3)
- Sentence-mining tools:
  - [asbplayer docs](https://docs.asbplayer.dev/docs/intro)
  - [asbplayer GitHub](https://github.com/killergerbah/asbplayer)
  - [asbplayer AMO](https://addons.mozilla.org/firefox/addon/asbplayer-learn-with-subs)
  - [subs2srs](https://subs2srs.sourceforge.net/)
  - [subs2srs files](https://sourceforge.net/projects/subs2srs/files)
  - [Stos](https://www.github.com/Hyxogen/stos)
  - [mpvacious](https://www.github.com/Ajatt-Tools/mpvacious)
  - [Immersive](https://www.github.com/Ben-Kerman/immersive)
  - [gogadget](https://pypi.org/project/gogadget)
  - [movies2anki](https://awesome.ecosyste.ms/projects/github.com%2Fkelciour%2Fmovies2anki)
  - [Vietnamese asbplayer guide](https://soyuz18.notion.site/Sentence-mining-from-Netflix-and-YouTube-with-asbplayer-83a03590cd8349ba81ca10340645b565)
- Kelciour:
  - [English - 3 (subs2srs samples)](https://kelciour.notion.site/English-3-263745ea25208026b057f019153b6378)
  - [English - 2 (book-derived decks)](https://kelciour.notion.site/English-2-215745ea2520800b878ae94bc9e3d0cb)
  - [English (main page, not readable)](https://kelciour.notion.site/English-166745ea2520800389cde8f5a594d799)
  - [r/Anki pre-made subs2srs post (mirror; 403)](https://reddit.birdcat.cafe/r/Anki/comments/1jnfayu/my_anki_flashcards_collection_premade_subs2srs)
- Glassy-Gaia:
  - [shop](https://glassygaia.gumroad.com/)
  - [TED-Ed](https://glassygaia.gumroad.com/l/english_ted_ed_videos)
  - [13 Reasons Why](https://glassygaia.gumroad.com/l/13_reasons_why)
  - [Despicable Me](https://glassygaia.gumroad.com/l/despicable_me)
  - [Stranger Things S1](https://glassygaia.gumroad.com/l/english_stranger_things_01)
  - [100+ idioms](https://glassygaia.gumroad.com/l/english_idiom)
  - [GitHub TED-Ed repo](https://github.com/GLASSY-GAIA/youtube-ted-ed-anki-english-en)
- GitHub decks:
  - [Ecattea COCA (inspected)](https://github.com/Ecattea/COCA-English-Anki-Deck)
  - [5mdld 60k MWLD](https://github.com/5mdld/anki-english-60k-decks)
  - [ciwga Oxford3000](https://github.com/ciwga/Oxford3000_Vocab)
  - [winterdl Oxford 5000](https://github.com/winterdl/oxford-5000-vocabulary-audio-definition)
  - [Vuizur tatoeba-to-anki](https://github.com/Vuizur/tatoeba-to-anki)
- Tatoeba:
  - [manythings CK audio](https://www.manythings.org/sentences/audio/)
  - [Tatoeba wiki make-anki](https://en.wiki.tatoeba.org/articles/show/make-anki)
  - [digitalwords Tatoeba audio](https://digitalwords.net/anki/tatoeba-audio/index.eng.html)
- Lists:
  - [Oxford Phrase List](https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford-phrase-list)
  - [Oxford wordlists](https://www.oxfordlearnersdictionaries.com/wordlists)
  - [OPAL](https://www.oxfordlearnersdictionaries.com/about/wordlists/opal)
  - [PHaVE (Nottingham repository)](https://nottingham-repository.worktribe.com/output/762398)
  - [UC Davis PHaVE Quizlet page](https://globalaffairs.ucdavis.edu/node/11866)
  - [EVP C1/C2 paper](https://www.cambridge.org/core/product/418955FC7ED2455E98A499BC40C2C816)
- Paid decks:
  - [Refold English Phrasal Verbs](https://refold.la/decks/buy/english-phrasal-verbs-deck)
  - [Speakada Common English Phrases](https://speakada.com/common-english-phrases-flashcards/)
  - [BasicEnglishSpeaking 399 phrases](https://basicenglishspeaking.com/anki-399)
- Other:
  - [Brainscape Speak English Like an American](https://brainscape.com/flashcards/speak-english-like-an-american-995667/packs/1819624)
  - [Immersion Kit (Tofugu)](https://tofugu.com/japanese-learning-resources-database/immersion-kit)
  - [Immersion Kit Patreon](https://www.patreon.com/immersionkit/about?l=ru-RU)
  - [Migaku learn-english](https://migaku.com/learn-english)
  - [TEDICT app (TED CC licence note)](https://apps.apple.com/app/id554188888)
  - [Chinese-forums TV subtitle cards (2015)](https://chinese-forums.com/forums/topic/49841-here-is-huge-collection-of-simplified-chineseenglish-subtitle-anki-flashcards-from-most-of-my-favourite-tv-shows-around-600000)
  - [老友记台词学英语 app](https://apps.apple.com/us/app/%E8%80%81%E5%8F%8B%E8%AE%B0%E5%8F%B0%E8%AF%8D%E5%AD%A6%E8%8B%B1%E8%AF%AD/id6748722804)
  - [英语口语8000句 app](https://apps.apple.com/np/app/%E8%8B%B1%E8%AF%AD%E5%8F%A3%E8%AF%AD8000%E5%8F%A5-%E6%A0%87%E5%87%86%E5%8F%91%E9%9F%B3%E5%90%AC%E5%8A%9B%E9%98%85%E8%AF%BB%E8%AF%AD%E6%B3%95%E9%9F%B3%E6%A0%87%E5%AD%A6%E4%B9%A0%E6%9C%89%E5%A3%B0%E8%B5%84%E6%96%99/id1209822862)
  - [DUO 3.0 scrapbox](https://scrapbox.io/rmaruon/%E3%80%8EDUO_3.0%E3%80%8F%E3%81%AE%E4%BE%8B%E6%96%87%E3%81%AE%E6%A7%8B%E9%80%A0%E3%82%92%E6%8A%8A%E6%8F%A1%E3%81%97%E3%81%A6%E6%B0%97%E3%81%A5%E3%81%84%E3%81%9F%E3%81%93%E3%81%A8)
  - [DUO app guide](https://appmatch.jp/2367-2/)
  - [Cambridge English Japan CEFR](https://cambridgeenglish.org/jp/exams-and-tests/cefr)
