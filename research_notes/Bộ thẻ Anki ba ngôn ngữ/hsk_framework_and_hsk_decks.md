# HSK framework (official state as of 2026-11-13) and HSK-organized Mandarin Anki decks with full-sentence audio

Evidence labels: [VERIFIED-INSPECTED] = I downloaded/extracted and inspected the file myself (scripts and work files are in the session scratchpad; no AnkiWeb .apkg could be downloaded, see Gaps). [VERIFIED-DOCS] = official page, README, or AnkiWeb's own metadata/sample-note API (`https://ankiweb.net/svc/shared/item-info?sharedId=<id>`, which returns the deck's real sample notes, note/audio/image counts, size, update date and reviews). [COMMUNITY] = user reviews/replies. [MARKETING] = creator promo only. [UNVERIFIED] = not confirmed. "INFERENCE" = my reasoning, not a sourced fact.

---

## Top findings & recommended shortlist

### Takeaway
The exam that counts from now on is **HSK 3.0 (2025 syllabus, levels 1–6 + combined 7–9)**. Its first regular worldwide sitting is **13 Dec 2026**, and its word list (300/500/1,000/2,000/3,600/5,400/11,000 cumulative) is **not** the 2021 GF0025 list (500/1,272/2,245/3,245/4,316/5,456/11,092). Most older decks labelled "HSK 3.0" are built on the 2021 list, so their level placement is wrong for the new exam. Two decks have verified full-sentence audio on the 2025 list, and they are the primary recommendations:
1. **HSKStory "HSK 3.0 (2026)" per-level decks.** Best first deck for HSK 1–3: short sentences, one sentence-audio clip per word (inspected), tone-coloured pinyin, small files.
2. **"New HSK 3.0 Mandarin Chinese Sentence Deck" (NewHSK3 / tompat).** Best listening-first deck: dedicated audio-only Listening cards and three sentences per word. Both the sentences and the voices are AI-generated (the AI label is inspected in the audio files).

### Cited Findings (shortlist)
- **PRIMARY A: HSKStory "HSK 3.0 (2026) – HSK n Vocabulary".**
  - Matches the 2025 list (HSK1 300/300, HSK2 197/197, HSK3 491/493 headwords inside the official level list; the remaining HSK2/HSK3 gaps are only homographs already taught at a lower level) [VERIFIED-INSPECTED].
  - Every note has a word clip and an example-sentence clip. Sentence clips last 1.3–4.4 s (median 2.3–2.8 s) and word clips 0.6–1.6 s [VERIFIED-INSPECTED].
  - Has a single Hanzi→meaning card type. Audio is embedded as HTML5 `<audio>`, not `[sound:]`, so nothing autoplays [VERIFIED-INSPECTED].
  - Free direct .apkg downloads — [hskstory.com/anki/hsk-1](https://hskstory.com/anki/hsk-1); AnkiWeb copy [1703580298](https://ankiweb.net/shared/info/1703580298).
- **PRIMARY B: "New HSK 3.0 Mandarin Chinese Sentence Deck".**
  - 3 sentences per word × Listening / Reading / Writing cards. The Listening card front is the sentence audio only [VERIFIED-INSPECTED on the HSK 5 package].
  - HSK 5 coverage is 1,593/1,600 official 2025 L5 words; the rest are homograph/notation splits [VERIFIED-INSPECTED].
  - 4,799 of 4,800 HSK 5 sentence-audio refs are present (one sentence shares a file). A 30-file sample lasts 3.4–6.3 s [VERIFIED-INSPECTED].
  - The MP3s carry a Chinese AIGC label (`"Label":"1","ContentProducer":"HUABABSpeech7E01"`), so the speech is AI-generated [VERIFIED-INSPECTED].
  - HSK 1–4 come from AnkiWeb ([258311532](https://ankiweb.net/shared/info/258311532)); HSK 5 / 6 / 7-8-9 from [GitHub v1.0](https://github.com/NewHSK3/new-hsk-3-anki-deck/releases/tag/v1.0) (243 MB / 309 MB / 1.05 GB) [VERIFIED-DOCS].
- **SECONDARY / CONDITIONAL: "🔥 New HSK 3.0: Ultimate Mandarin Chinese Vocabulary" (fa9r).**
  - Covers the 2025 list with word + sentence audio and an image on every card [MARKETING / VERIFIED-DOCS samples].
  - The examples and audio of 2,683 words were replaced with the manually recorded "HSK - JK" material [VERIFIED-DOCS description + COMMUNITY author reply].
  - Not inspected: AnkiWeb download was blocked.
  - Weak spots for this learner: it converted 一/不 sandhi pinyin to dictionary form ("一下 yíxià → yīxià"), and it has only Hanzi→English cards [VERIFIED-DOCS]. Remaining audio is inherited from "Last HSK 3.0" (engine unknown).
- **Not primary:**
  - "Last HSK 3.0 2026 (From official list)": data errors such as Kangxi-radical look-alike characters and pinyin errors, documented by the derivative [VERIFIED-DOCS].
  - hnsaw "NEW HSK 3.0 2026 (Hanzi, Eng, Sentence, Audio, Pic,)": local Microsoft TTS, "some cards have audio while some don't" [VERIFIED-DOCS].
  - krmanik Anki-xiehanzi: word audio only.
  - RyanGibb/anki-hsk3: self-build only, and needs your own Azure key for sentence TTS.
  - Every deck built on the 2021 list ("Another HSK 3.0 vocabulary deck", "Mandarin Chinese: New HSK 3.0 Vocabulary and Characters", Mega Mandarin).
  - Every legacy HSK 2.0 deck (HSK 1 - JK, ChineseAudioFlashcards HSK 1, etc.). They can be good audio material, but the level mapping is wrong for the 2026+ exam.
- **Language coverage:** I found no Chinese-, Japanese- or Vietnamese-language HSK 3.0 Anki deck with sentence audio. Search results only surfaced English-gloss decks and web tools ([JP search](https://studycli.org/ja/chinese-tools/hsk-3-vocabulary/), [CN search](https://studycli.org/zh-CN/chinese-tools/hsk-3-vocabulary/)).

### Inferences
- **Suggested setup for this learner (INFERENCE):**
  - Start with HSKStory HSK 1 → 2 → 3 for "sound ↔ known Hanzi" linking. Tap the sentence audio every review.
  - In parallel, run only the **Listening** subdeck of NewHSK3 for HSK 1–3 (900 / 600 / 1,500 sentence cards). Suspend Reading/Writing until speaking practice starts.
  - Hanzi recognition from Japanese makes the Reading cards low-value early. Listening cards target the stated weakness directly.
- Neither primary deck can be called native-speaker audio. The NewHSK3 audio is verified AI. The HSKStory audio is 24 kHz MPEG-2 with no recorder metadata, and the site markets "native-speaker voices Luna and Kai" [MARKETING]. Treat both as neural TTS until proven otherwise.

### Gaps
- No AnkiWeb .apkg could be downloaded: `/svc/shared/download-deck` returned HTTP 429 "Please log in to download more decks."
  - So Ultimate, Last HSK, hnsaw and NewHSK3 HSK 1–4 are evidenced only by AnkiWeb metadata and sample notes, not by file inspection.
- I cannot listen, so naturalness and tone correctness of any audio is not judged by ear.

---

## Q1. What is the current official HSK standard and exam as of 2026-11-13?

### Takeaway
**Three layers coexist:**
1. **Legacy HSK 2.0** (6 levels, 5,000 words): still used for HSK 1–6 sittings through 7 Nov 2026.
2. **GF0025-2021 national standard** (3 stages / 9 bands, 11,092 words): effective 2021-07-01. It underpins the HSK 7–9 exam (first sitting 26 Nov 2022).
3. **HSK 3.0 exam syllabus (《HSK考试大纲》)**: published 2025-11 by CLEC/中外语言交流合作中心, "2026-07 实施".
   - Its new word list is 300 / +200 / +500 / +1,000 / +1,600 / +1,800 / +5,600 = 11,000.
   - The new HSK 1–6 exams on this syllabus launch worldwide on **2026-12-13** (after pilots on 2026-01-31 and 2026-09-20).

### Cited Findings
**A. HSK 3.0 exam syllabus (2025)**

- **Cover page:** "中文水平考试 HSK 考试大纲 Syllabus for the Chinese Proficiency Test / 中外语言交流合作中心 发布 / 2025-11 发布 / 2026-07 实施". The PDF is 406 pages, with sections 任务大纲, 话题大纲, 词汇大纲, 汉字大纲 and 语法大纲 for levels 一 to 六 and 七—九 [VERIFIED-INSPECTED] — [official PDF](https://hsk.cn-bj.ufileos.com/3.0/%E6%96%B0%E7%89%88HSK%E8%80%83%E8%AF%95%E5%A4%A7%E7%BA%B21219.pdf)
  - PDF metadata: creationDate 2025-12-17, modDate **2026-10-30** (the hosted file was re-saved recently). Embedded title "HSK（1-9级）词汇大纲.xlsx".
  - My parse of the current file still gives exactly the counts below, so the vocabulary counts are unchanged.
- **Vocabulary (my full parse of 词汇大纲; serial numbers 1–11,000 are continuous)** [VERIFIED-INSPECTED]:

  | Level | New words at this level | Cumulative |
  |---|---|---|
  | 1 | 300 | 300 |
  | 2 | 200 | 500 |
  | 3 | 500 | 1,000 |
  | 4 | 1,000 | 2,000 |
  | 5 | 1,600 | 3,600 |
  | 6 | 1,800 | 5,400 |
  | 7–9 | 5,600 | **11,000** |

  — [official PDF](https://hsk.cn-bj.ufileos.com/3.0/%E6%96%B0%E7%89%88HSK%E8%80%83%E8%AF%95%E5%A4%A7%E7%BA%B21219.pdf)
  - Same cumulative totals reported by secondary sources — [Wikipedia](https://en.wikipedia.org/wiki/Hanyu_Shuiping_Kaoshi), [studycli](https://studycli.org/hsk/the-new-hsk/).
  - 102 entries carry a secondary-level marker such as "1（4）", "2（3）" or "1（2）（4）". These mark senses/parts of speech added at a later level, e.g. 好 "1（2）（4）", 一下 "1（4）". Homographs are numbered (本1, 面1) [VERIFIED-INSPECTED].
- **Pinyin conventions in the official 2025 list** [VERIFIED-INSPECTED]:
  - It writes **一/不 tone sandhi** on the headword: 一下 yíxià, 一起 yìqǐ, 一样 yíyàng, 一定 yídìng, 不客气 bú kèqi, 不要 búyào, 不用 búyòng, 不错 búcuò.
  - It writes **neutral tones**: 谢谢 xièxie, 朋友 péngyou, 东西 dōngxi, 对不起 duìbuqǐ, 差不多 chàbuduō.
  - This is a useful benchmark for judging decks.
- **Characters (my count of 汉字大纲)** [VERIFIED-INSPECTED; regex-based count, small risk of off-by-few]:

  | Level | New 认读字 (recognition) | Cumulative |
  |---|---|---|
  | 1 | 246 | 246 |
  | 2 | 125 | 371 |
  | 3 | 284 | 655 |
  | 4 | 441 | 1,096 |
  | 5 | 431 | 1,527 |
  | 6 | 413 | 1,940 |
  | 7–9 | 1,148 | 3,088 |

  - 书写字 (handwriting): 100 (L1–2), 150 each (L3–6), 500 (L7–9), total 1,200.
- **Grammar counts:** not extracted (see Gaps).
- **Relation to GF0025:** the syllabus's 7–9 task section says "本大纲研制中参考了《国际中文教育中文水平等级标准》…" — the syllabus *references* GF0025 but is a separate document with a different list [VERIFIED-INSPECTED].

**B. Launch announcements and dates**

- **2025-11-14…16, World Chinese Language Conference:** 语合中心 "推出中文水平考试HSK3.0版". It integrates leveled and cross-level testing, keeps a cross-level "一卷三试" HSK 7–9 exam, and adds translation from the mother tongue into Chinese at 7–9. Products follow "《国际中文教育中文水平等级标准》《HSK3.0考试大纲》" — [MOE / 中国教育报, 2025-11-17](http://www.moe.gov.cn/jyb_xwfb/s5147/202511/t20251117_1420566.html)
- **Global pilot of HSK 3.0, levels 1–6** [VERIFIED-DOCS]:
  - Held **2026-01-31**; registration opened 2025-12-19 (paper until 2026-01-07, iBT until 2026-01-15).
  - Speaking test is mandatory alongside levels 3–6. Results came out 2026-03-14 and are valid 2 years.
  - Sources: [ChinaNews 2025-12-19](https://www.chinanews.com.cn/edu/2025/12-19/10536380.shtml), [Beijing gov EN 2025-12-22](https://english.beijing.gov.cn/studyinginbeijing/news/202512/t20251222_4355931.html)
- **Second pilot on 2026-09-20; last regular HSK 2.0 sitting 2026-11-07** [VERIFIED-DOCS, secondary only] — [studycli](https://studycli.org/hsk/the-new-hsk/). Not found on a CTI page.
- **CTI announcement: "HSK 3.0 will be officially launched worldwide on December 13, 2026!"** [VERIFIED-DOCS]
  - Registration: paper-based until 24:00, 16 Nov 2026; internet-based until 24:00, 3 Dec 2026.
  - Sources: [chinesetest.cn news 51336883](https://www.chinesetest.cn/news/51336883) (text read via [admin.chinesetest.cn mirror](https://admin.chinesetest.cn/gonewcontent.do?id=51336883)).
  - Same notice in Chinese on CTI's X account ([post](https://x.com/HSKTestOfficial/status/2097633616931041329)). Its ID decodes to **2026-09-09 10:30 UTC** (INFERENCE from the X snowflake ID; page returned 402).
- **CTI 2027 calendar** for HSK 1–6 + speaking was published — [CTI 51619013](https://admin.chinesetest.cn/gonewcontent.do?id=51619013). Secondary source: 11 dates, 9 Jan – 11 Dec 2027 ([studycli](https://studycli.org/hsk/the-new-hsk/)).
- **Conflict on dates:** Wikipedia/GoEast say "full rollout July 2026". That date is the syllabus *implementation* date, not the exam switch. CTI's own announcement makes 2026-12-13 the first worldwide HSK 3.0 sitting — [Wikipedia](https://en.wikipedia.org/wiki/Hanyu_Shuiping_Kaoshi) vs [CTI](https://admin.chinesetest.cn/gonewcontent.do?id=51336883).

**C. GF0025-2021 《国际中文教育中文水平等级标准》**

- Released by 教育部 and 国家语委. Effective **2021-07-01**. Defines 三等九级 and a 四维基准 (音节、汉字、词汇、语法) — [MOE 2021-03-29](http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202103/t20210329_523304.html); PDF attachment [W020210329527301787356.pdf](http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202103/W020210329527301787356.pdf)
- **表1 语言量化指标总表**, read from rendered page images of the official PDF (scanned images, no text layer). Format is "new / cumulative" [VERIFIED-INSPECTED]:

  | Band | Syllables | Characters | Words | Grammar |
  |---|---|---|---|---|
  | 1 | 269 | 300 | 500 | 48 |
  | 2 | 199 / 468 | 300 / 600 | 772 / 1,272 | 81 / 129 |
  | 3 | 140 / 608 | 300 / 900 | 973 / 2,245 | 81 / 210 |
  | 4 | 116 / 724 | 300 / 1,200 | 1,000 / 3,245 | 76 / 286 |
  | 5 | 98 / 822 | 300 / 1,500 | 1,071 / 4,316 | 71 / 357 |
  | 6 | 86 / 908 | 300 / 1,800 | 1,140 / 5,456 | 67 / 424 |
  | 7–9 | 202 / 1,110 | 1,200 / 3,000 | 5,636 / **11,092** | 148 / 572 |

  - Totals: 1,110 syllables, 3,000 characters, 11,092 words, 572 grammar points.

**D. HSK 7–9 exam**

- First global formal sitting **2022-11-26**, based on the 2021 standard — [China Daily 2022-11-05](https://www.chinadaily.com.cn/a/202211/05/WS6365aa87a3105ca1f22742c8.html)
- Wikipedia says "officially launched in March 2022" — [Wikipedia](https://en.wikipedia.org/wiki/Hanyu_Shuiping_Kaoshi). That was the earlier plan; China Daily (Nov 2022) reports the first test as 26 Nov 2022 (conflict noted).

**E. Legacy HSK 2.0**

- Cumulative 150 / 300 / 600 / 1,200 / 2,500 / 5,000 words — [Wikipedia citing chinesetest HSK-2015.xlsx](https://en.wikipedia.org/wiki/Hanyu_Shuiping_Kaoshi) [VERIFIED-DOCS secondary].
- The same counts appear on legacy deck sites — [hskcore](https://hskcore.com/hsk-anki-decks/).

### Inferences
- **2021 vs 2025 overlap (my own comparison: krmanik's OCR of the 2021 list vs my parse of the 2025 PDF):**
  - Only **263 of the 300** 2025-HSK1 words are in the 2021 band-1 list. 37 are not, e.g. 一下, 不要, 你好, 便宜, 公司, 出租车, 可以, 怎么样, 苹果, 猫, 狗.
  - Only about 9,694 headwords are shared between the two lists overall.
  - A deck built from the 2021 list therefore puts many words at the wrong level for the Dec 2026+ exam, even though both are called "HSK 3.0" in the community [VERIFIED-INSPECTED computation].
- **"HSK 3.0" is ambiguous.** Since 2021 the community used it for GF0025. Since Nov 2025 the official name "HSK3.0" refers to the new exam and its 2025 syllabus. A deck's "HSK 3.0" label proves nothing; check per-level counts:
  - 2025 syllabus: 300 / 200 / 500 / 1,000 / 1,600 / 1,800 / 5,600.
  - 2021 standard: 500 / 772 / 973 / 1,000 / 1,071 / 1,140 / 5,636.
  - Telltale totals: 11,092 or "11,0xx" notes → 2021 list; 11,000 → 2025 list.
- For a learner starting now, the relevant target is the 2025 syllabus (HSK 1 = 300 words).

### Gaps
- Grammar counts per level in the 2025 syllabus were not parsed (table layout).
- No official statement found on whether GF0025-2021 itself is being revised. The MOE 2025 article cites both documents as current.
- Exact publication day of the 2025 syllabus: Wikipedia says 2025-11-15 (secondary); the PDF only says "2025-11 发布".

---

## Q2. Community data sets used to build HSK 3.0 decks

### Takeaway
elkmovie/hsk30 and drkameleon/complete-hsk-vocabulary are **2021 (GF0025) lists**, with no 2025 update. krmanik/HSK-3.0 has **both** a 2021-03 folder (MOE OCR) and a 2025-11 folder (from the 2025 syllabus PDF), actively maintained to Nov 2026. RyanGibb/anki-hsk3 parses the 2025 syllabus.

### Cited Findings
- **elkmovie/hsk30**
  - Header: "HSK 3.0 word list / OCR'ed but not extensively proofread (yet) / Copyright (c) 2021 Pleco Inc." Extracted from the MOE 2021 PDF.
  - Errata come only as commits, e.g. 2021-12-03 "3498 人手 -> 入手". Last commits 2021-12 (charlist 2023-11). No 2025 data [VERIFIED-INSPECTED clone] — [GitHub](https://github.com/elkmovie/hsk30)
- **drkameleon/complete-hsk-vocabulary**
  - Takes HSK 3.0 "new" levels from elkmovie/hsk30 and HSK 2.0 from clem109/hsk-vocabulary; levels `new-1…new-6` + `new-7` (7–9) — **2021-based**.
  - No audio. Meanings from CC-CEDICT [VERIFIED-DOCS README] — [GitHub](https://github.com/drkameleon/complete-hsk-vocabulary)
- **krmanik/HSK-3.0** [VERIFIED-INSPECTED clone] — [GitHub](https://github.com/krmanik/HSK-3.0)
  - **2021 folder:** "HSK List" files hold 500 / **771** / 973 / 1,000 / 1,071 / 1,140 / 5,636 lines. Band 2 is one short of the official 772.
  - **2025 folder:** created 2025-12-19, grammar added 2026-06-14, latest commits 2026-11-07/08 ("Fix typo chars", "Restore char orders in pinyin"), and 2026-10-24 "Replace HSK 2025 word audio with Yue Tan's voice throughout".
  - The 2025 word files hold 300 / 204 / 507 / 1,019 / 1,638 / 1,815 / 5,622 lines. They exceed 200/500/… because words are **also listed at their secondary level** (e.g. 多, 好, 给, 那 reappear in L2; numbered homographs such as 点1/点2 are kept).
  - The repo also holds BCT and YCT lists.
- **RyanGibb/anki-hsk3** [VERIFIED-DOCS README]
  - Merges two extractions of the 2025 syllabus (hsk-2025-data and hsk-syllabus-vocabulary-parser), which agree on 10,940 words. The deck has 300 / 200 / 500 / 1,000 / 1,600 / 1,800 / 5,599 = 10,999 words.
  - Grammar sentences are taken from chinesetest.cn — [GitHub](https://github.com/RyanGibb/anki-hsk3)

### Inferences
- Any deck that cites elkmovie or drkameleon, or shows 11,092 / 11,0xx words, is on the 2021 list, not the exam syllabus that starts 2026-12-13.

### Gaps
- No published errata list for the 2025 syllabus was found in any repo. Errata appear only as commits.

---

## Q3. Which decks follow which list? Do counts match? Per-band (non-cumulative) separation?

### Takeaway
2025-list decks with sentence audio:
- HSKStory, per-level new words, deduplicated.
- NewHSK3 sentence deck (tompat): per level, 3 sentences per word.
- Last HSK 3.0 2026, per level.
- fa9r Ultimate (derived from Last HSK), per level.
- hnsaw NEW HSK 3.0 2026 (only HSK 1 confirmed).

2021-list decks labelled "HSK 3.0": krmanik's older xiehanzi decks, "Another HSK 3.0 vocabulary deck", "Mandarin Chinese: New HSK 3.0 Vocabulary and Characters", Mega Mandarin. None of these has sentence audio.

### Cited Findings (count checks)
- **HSKStory (2025 list)** [VERIFIED-INSPECTED HSK1–3 + VERIFIED-DOCS counts for 4–9 from [hskstory.com](https://hskstory.com/anki/hsk-1)]:
  - Deck notes: HSK1 300, HSK2 197, HSK3 493, HSK4 990, HSK5 1,579, HSK6 1,777, HSK7–9 5,562 = 10,898. These are **new words per level, with cross-level duplicates removed**.
  - Inspected decks vs the official per-level list:
    - HSK1: 300/300 match.
    - HSK2: 197/197 in L2; the missing official item is 点, already in L1.
    - HSK3: 491/493 in L3. Missing are 会, 只, 地, 得, 站, 过去, 还, 长, all already taught at lower levels. 有一点儿 and 有时候 are written out where the official list uses 有（一）点儿 / 有时（候）.
  - Only 81 of HSKStory's 197 HSK2 words are in the 2021 band-2 list. This confirms it is not 2021-based.
- **NewHSK3 sentence deck (2025 list)** [VERIFIED-INSPECTED HSK 5; VERIFIED-DOCS HSK 1–4]:
  - HSK 5 package: 1,596 distinct focus words, 1,593 of them in the official 2025 L5 list. The others are 拼音 and the homograph splits 称1 / 称2.
  - 14,400 notes = 1,600 × 3 sentences × 3 note types.
  - AnkiWeb HSK 1–4 package shows 18,000 notes = (300 + 200 + 500 + 1,000) × 9 ✓ — [AnkiWeb](https://ankiweb.net/shared/info/258311532)
- **Last HSK 3.0 2026** [VERIFIED-DOCS]:
  - Packages hold 300 / 200 / 500 / 1,000 / 1,600 / 1,800 / 1,867 + 1,867 + 1,866, labelled "Cumulative total: 300 … 5,400". Each package contains only that level's words.
  - AnkiWeb notes: HSK1 300, HSK4 1,000, HSK6 1,800 — [HSK1](https://ankiweb.net/shared/info/1623336797), [HSK4](https://ankiweb.net/shared/info/562028400), [HSK6](https://ankiweb.net/shared/info/395921696)
- **Ultimate (fa9r)** [VERIFIED-DOCS]: HSK1 300 notes, HSK2 200, HSK7 part 1 1,867. Description: "about 11,000 words … one sub-deck per level" — [HSK1](https://ankiweb.net/shared/info/1736976202), [HSK2](https://ankiweb.net/shared/info/801432412), [HSK7 p1](https://ankiweb.net/shared/info/1145295418)
- **hnsaw NEW HSK 3.0 2026** [VERIFIED-DOCS]: HSK1 deck has 301 notes. It lists levels as "HSK 2 (500 Words) … HSK 7–9 (11000 Words)", i.e. 2025 cumulative labels. Whether those level decks are uploaded is unclear: a reviewer asked "Please upload the rest" — [AnkiWeb](https://ankiweb.net/shared/info/413677233)
- **krmanik xiehanzi** [VERIFIED-DOCS]:
  - New "(2025)" decks hold 44,292 notes = 4 card-type subdecks; per subdeck about 11.07k entries, consistent with the 2025 list including secondary-level duplicates. Updated 2025-12-22/23 — [397871109](https://ankiweb.net/shared/info/397871109), [701666449](https://ankiweb.net/shared/info/701666449)
  - Older decks (11,042 notes, 2023–2025) are 2021-based — [239300382](https://ankiweb.net/shared/info/239300382), [536858343](https://ankiweb.net/shared/info/536858343), [1063372083](https://ankiweb.net/shared/info/1063372083)
- **Decks labelled "HSK 3.0" but on the 2021 list** [VERIFIED-DOCS]:
  - "Another HSK 3.0 vocabulary deck": 11,088 notes, updated 2024-01-15 — [549107549](https://ankiweb.net/shared/info/549107549)
  - "Mandarin Chinese: New HSK 3.0 Vocabulary and Characters": "11092 words and 3000 characters", 14,092 notes, 2021-09-22 — [1144807196](https://ankiweb.net/shared/info/1144807196)
  - Mega Mandarin HSK 3.0: "all 11,092 words on the proposed HSK 3.0 list", paid, demo 2022-01-08 — [2062516907](https://ankiweb.net/shared/info/2062516907)
  - "HSK 3.0 levels 1 2 and 3": 2,245 notes = 2021 cumulative band 3; no audio — [85606670](https://ankiweb.net/shared/info/85606670)

### Inferences
- Per-band (non-cumulative) separation is the norm in all 2025-list decks above. HSKStory additionally removes words already taught at lower levels. That is cleaner for progression but drops the official "second sense at a higher level" entries (e.g. 点 in L2).

### Gaps
- Could not verify NewHSK3 HSK 1–4 file contents (AnkiWeb download blocked); relied on AnkiWeb counts and samples.

---

## Q4. Per-deck inspection, samples and preliminary scores (100 pts)

Scoring rubric (weights): full-sentence audio quality & coverage 25; naturalness/richness of examples 20; suitability for target level 15; speaking-oriented vocab/chunks 15; coverage, structure, progression 10; accuracy, reliability, maintenance 10; images, customization, extras 5. Pronunciation/tone accuracy and beginner listening suitability are weighted heavily when interpreting.

### 4.1 HSKStory "HSK 3.0 (2026) – HSK n Vocabulary · HSKStory" — PRIMARY A

#### Identity, sources and size
- **Creator:** HSKStory, the graded-reader site/app.
- **URLs:**
  - [hskstory.com/anki/hsk-1](https://hskstory.com/anki/hsk-1); level pages /anki/hsk-2 … /anki/hsk-7-9.
  - Direct downloads: `https://audio.hskstory.com/downloads/anki/hskstory-hsk1-anki-v11.apkg`, `…hsk2-anki-v10`, `…hsk3-anki-v9`, `…hsk4-anki-v10`, `…hsk5-anki-v8`, `…hsk7-9-anki-v8`.
  - AnkiWeb copies: HSK1 [1703580298](https://ankiweb.net/shared/info/1703580298), HSK2 [223368909](https://ankiweb.net/shared/info/223368909), HSK3 [1226554191](https://ankiweb.net/shared/info/1226554191), HSK5 [2047844854](https://ankiweb.net/shared/info/2047844854), HSK7-9 [735797420](https://ankiweb.net/shared/info/735797420). There is also a Chengyu deck: 414 idioms, word + sentence audio, [926470945](https://ankiweb.net/shared/info/926470945).
- **Version / updated:** all direct files have Last-Modified 2026-10-24 [VERIFIED-INSPECTED HTTP headers]. AnkiWeb HSK1 updated 2026-10-23 [VERIFIED-DOCS].
- **File sizes:** HSK1 5.2 MB, HSK2 3.7 MB, HSK3 9.5 MB, HSK5 32 MB, HSK7–9 98 MB [VERIFIED-INSPECTED].

#### Structure and fields
- **Counts and format** [VERIFIED-INSPECTED]: HSK1 300 notes/300 cards; HSK2 197/197; HSK3 493/493. Old-schema `collection.anki2` plus a JSON media map.
- **Note type:** "HSKStory HSK n Recognition v1". Fields: Hanzi, ToneHanzi, TonePinyin, Meaning, Audio, ExampleHanzi, ExamplePinyin, ExampleEnglish, StoryURL, StoryTitle.
  - The sentence-audio HTML sits inside the **StoryTitle** field. The word-audio HTML is in Audio.
  - The AnkiWeb copy's sample shows a different field layout (WordAudio, SentenceAudio, …) [VERIFIED-DOCS].
- **Template** [VERIFIED-INSPECTED]: a single "Recognition" card.
  - Front: `{{Hanzi}}` only.
  - Back: tone-coloured Hanzi and pinyin, word-audio button, meaning, example (Hanzi, pinyin, English) with a sentence-audio button, and a hide-example toggle stored in localStorage.
  - Audio is `<audio src="…mp3">` with JS play buttons: word plays at `playbackRate=1`, **sentence at `playbackRate=0.8`** (slowed). It is not `[sound:]`, so there is no autoplay and no Anki replay key.
  - **No listening-first or production card.** Hiding characters or pinyin would need a custom template plus JS (INFERENCE).

#### Audio
- **Sentence audio** [VERIFIED-INSPECTED]: present for every note.
  - Unique clips: HSK1 296 for 300 notes, HSK2 195/197, HSK3 492/493. The few notes without their own clip share a sentence file with another note.
  - Durations: HSK1 median 2.33 s (1.37–4.32 s, n=296); HSK2 median 2.71 s (1.32–4.37); HSK3 median 2.83 s (sample 200, 1.80–4.32).
  - Rate: about 3.6–3.8 Hanzi/s at file speed (HSK1/HSK3).
  - Encoding: MPEG-2 Layer III, 24 kHz, 32–64 kbps; only ID3 tag is TSSE=Lavf62.12.102.
- **Word audio** [VERIFIED-INSPECTED]: medians 0.65 / 0.67 / 0.72 s.
- **Source:** not disclosed on the Anki page ("Mandarin audio"). The site says stories are "read aloud by native-speaker voices… Luna and Kai" [MARKETING] — [hskstory.com](https://hskstory.com/about).
  - INFERENCE: named voice personas, word-synced narration and 24 kHz output point to neural TTS. Not verified.

#### Language and accuracy
- **Translation language:** English. Pinyin and definitions come from CC-CEDICT (CC BY-SA 4.0); examples and audio are by HSKStory [VERIFIED-DOCS].
- **Tone/pinyin** [VERIFIED-INSPECTED]:
  - Sentence pinyin applies 一/不 sandhi and neutral tones: "wǒ xiǎng xiū xi yí xià", "bú kè qi", "yì xiē", "yí ge", "péng you".
  - Headword pinyin is citation form (一下 yī xià, 不客气 bù kè qi, 一定 yī dìng, 不用 bù yòng). It is inconsistent: 一半 is shown as "yí bàn".
  - Pinyin is spaced per syllable, not per word.

#### Sample notes (verbatim, extracted from the v11/v9 .apkg files) [VERIFIED-INSPECTED]
- HSK1 | 一下 | yī xià | "(after a verb) a bit; a little …" | 我想休息一下，下午再学习。 | wǒ xiǎng xiū xi yí xià， xià wǔ zài xué xí。 | I want to rest for a bit and study again this afternoon. | word `hskstory-hsk1-002.mp3` | sentence `hskstory-hsk1-example-08dd25995eaf.mp3` | no image
- HSK1 | 不客气 | bù kè qi | you're welcome | 不客气，很高兴你喜欢我做的饭。 | bú kè qi， hěn gāo xìng nǐ xǐ huan wǒ zuò de fàn。 | You're welcome; I'm glad you like my cooking. | `hskstory-hsk1-019.mp3` / `hskstory-hsk1-example-2ef0a640f4d1.mp3`
- HSK1 | 没有 | méi yǒu | not have; there is not; have not | 我没有姐姐，有一个弟弟。 | wǒ méi yǒu jiě jie， yǒu yí ge dì di。 | I do not have an older sister; I have a younger brother. | `hskstory-hsk1-212.mp3` / `hskstory-hsk1-example-1c4c438f86e9.mp3`
- HSK3 | 不用 | bù yòng | need not | 明天学校放假，我们不用上课。 | míng tiān xué xiào fàng jià， wǒ men bú yòng shàng kè。 | School is on break tomorrow, so we don't need to attend class. | `hskstory-hsk3-012.mp3` / `hskstory-hsk3-example-f7ce9fab7be2.mp3`
- HSK2 | 上网 | shàng wǎng | to go online | 我喜欢上网买东西。 | wǒ xǐ huan shàng wǎng mǎi dōng xi。 | I like shopping online.

#### Price, licence, compatibility, reviews
- **Price/licence:** free [VERIFIED-DOCS]. No separate deck licence stated beyond CC-CEDICT attribution.
- **Compatibility:** "Anki Desktop, AnkiMobile and AnkiDroid", media bundled, works offline [VERIFIED-DOCS]. No add-ons needed.
  - INFERENCE: HTML5 audio playback depends on the client webview. AnkiMobile/AnkiDroid usually support it, but this is UNVERIFIED for this deck.
- **Known problems:**
  - One sentence per word.
  - Only a recognition card.
  - Example-audio field name is odd (stored in StoryTitle).
  - Inconsistent headword sandhi (see above).
- **Independent reviews:** one AnkiWeb review, "perfect!" (2026-11-03) [COMMUNITY]. No other reviews found.

#### Score: **72 / 100**
| Criterion | Score | Justification |
|---|---|---|
| Audio | 19/25 | Full-sentence clip on ~100% of notes (inspected); likely TTS; 1 clip/word; slowed playback by default |
| Examples | 13/20 | Short, everyday, level-matched; but only one per word, authorship/review process unknown |
| Level fit | 14/15 | Ideal for a beginner: 8–11-Hanzi sentences, tone colours, sandhi in sentence pinyin |
| Speaking | 9/15 | Useful daily chunks (你好, 不客气, 没事) but no production/shadowing card |
| Coverage | 9/10 | Exact 2025 list, all levels 1–9, per-level new words |
| Accuracy | 7/10 | Maintained (Oct 2026); minor pinyin-convention inconsistency |
| Extras | 1/5 | No images; one template; HTML audio hard to repurpose for audio-first |

Uncertainty: ±6, mostly the unknown voice source and naturalness.

### 4.2 "New HSK 3.0 Mandarin Chinese Sentence Deck" (GitHub: NewHSK3) — PRIMARY B

#### Identity, sources and size
- **Creator:** "tompat" (buymeacoffee.com/tompat), GitHub user NewHSK3. Repo created 2026-07-31, 1 commit, 6 stars [VERIFIED-DOCS].
- **URLs:** [AnkiWeb 258311532](https://ankiweb.net/shared/info/258311532) (HSK 1–4); [GitHub release v1.0](https://github.com/NewHSK3/new-hsk-3-anki-deck/releases/tag/v1.0) (HSK 5, 6, 7-8-9).
- **Version:** v1.0. AnkiWeb updated 2026-08-01. GitHub assets Last-Modified 2026-08-01: HSK 5 242.6 MB, HSK 6 309.2 MB, HSK 7-8-9 1,049.5 MB [VERIFIED-INSPECTED HTTP headers]. AnkiWeb package 235.9 MB, 18,000 notes, 5,969 audio files [VERIFIED-DOCS].
- **Author claims:** the full deck has about 11,000 words, 33,000 sentences and 99,000 cards; Simplified + Traditional, tone-marked pinyin, English [MARKETING/VERIFIED-DOCS].

#### Structure and templates (HSK 5 package)
I inspected the HSK 5 package via HTTP range requests: collection, media map and 30 audio files only [VERIFIED-INSPECTED].
- **Format:** `meta` (version 3), `collection.anki21b` (zstd, new schema) plus a stub `collection.anki2`, protobuf media map.
- **Subdecks:** New HSK 3.0::HSK 5::Listening / Reading / Writing, 4,800 cards each.
- **Note types:** three, one per card type ("13 Field Mandarin Listening HSK 5" etc.), so each sentence exists as 3 separate notes. Fields:
  - Focus Word Simplified, Focus Word Pinyin, Pinyin No Diacritic, Focus Word English
  - Mandarin Sentence Simplified, Mandarin Sentence Traditional, Mandarin Sentence Pinyin, English Sentence
  - … with Blanks ×3
  - Han (holds `[sound:<sentence>.mp3]`), Yun ("yes" on 2,400/4,800, probably the male-voice flag — INFERENCE).
- **Templates:**
  - **Listening:** front = `{{Han}}` audio only. Back = English, Simplified, Traditional, pinyin, replay.
  - **Reading:** front = Simplified + Traditional sentence with `{{type:…}}` input. Back adds English + pinyin.
  - **Writing:** English + blanked sentence + blanked pinyin, a "Focus word" reveal button and a hanzi-writer stroke-order script (`_hanzi-writer.min.js` in media). The author says it needs internet [VERIFIED-DOCS].

#### Audio
- **Sentence audio** [VERIFIED-INSPECTED]: 4,799 unique `[sound:]` files, all present in the media map. File names are the sentence text.
- **Sample of 30:** 3.38–6.30 s, median 5.22 s, about 3.1 Hanzi/s. MPEG-1 Layer III, 32 kHz, 64 kbps, TSSE=Lavf58.76.100.
- **AI label:** every sampled file has an ID3 `TXXX:aigc {"aigc": {"Label": "1", "ContentProducer": "HUABABSpeech7E01", "ProduceID": …}}` tag. This is a Chinese-style AIGC implicit label marking AI-generated speech.
- **Author's statements:** "generated using AI speech synthesis… roughly half male, half female… the male voice seems more likely… to deviate from standard pronunciation"; "I have not listened to every one" [VERIFIED-DOCS]. In a reply: "I have now added the voice from minimax… cost me about $150" [COMMUNITY/author].
- **Word audio:** none (only sentence audio) [VERIFIED-INSPECTED HSK 5].

#### Sentences and pinyin
- **Sentence source:** "created with extensive AI (ChatGPT extended thinking) assistance". Checked for formatting, duplicates and "obvious unnatural or incorrect output" [VERIFIED-DOCS]. Words outside the level occasionally appear [VERIFIED-DOCS].
- **Tone/pinyin** (HSK 5, 4,799 unique sentence-pinyin strings) [VERIFIED-INSPECTED]:
  - Sandhi is applied consistently: "bú shì" 59 vs 0 citation; "bú yào" 60 vs 1; "yí ge/yí gè" 99; "yì qǐ" 28 vs 0; "yí xià" 24 vs 0.
  - Neutral tones as expected: "péngyou" 20 vs 1 full tone; "wǒmen" 215; 讲究 "jiǎngjiu".
  - Pinyin is word-segmented with capitalisation. This matches the official 2025 conventions.
- **Translation:** English. Traditional is a script conversion only [VERIFIED-DOCS].

#### Sample notes (verbatim)
- HSK 5 [VERIFIED-INSPECTED] | 对比 | duìbǐ | to compare; comparison, contrast | 通过对比两份报告，我们发现数据差距很大。 | Tōngguò duìbǐ liǎng fèn bàogào, wǒmen fāxiàn shùjù chājù hěn dà. | By comparing the two reports, we found that the gap in the data was very large. | `[sound:通过对比两份报告，我们发现数据差距很大。.mp3]` | no image
- HSK 5 [VERIFIED-INSPECTED] | 毛笔 | máobǐ | writing brush | 他从小学习书法，对毛笔的选择很讲究。 | Tā cóng xiǎo xuéxí shūfǎ, duì máobǐ de xuǎnzé hěn jiǎngjiu. | He has studied calligraphy since childhood and is very particular about his choice of writing brush. | `[sound:他从小学习书法，对毛笔的选择很讲究。.mp3]` | Yun: yes
- HSK 5 [VERIFIED-INSPECTED] | 病情 | bìngqíng | illness condition | 经过治疗，他的病情已经明显好转。 | Jīngguò zhìliáo, tā de bìngqíng yǐjīng míngxiǎn hǎozhuǎn. | After treatment, his condition has clearly improved.
- HSK 1–4 [VERIFIED-DOCS, AnkiWeb sample] | 作业 | zuòyè | homework | 老师说明天要交作业。 | Lǎoshī shuō míngtiān yào jiāo zuòyè. | The teacher said the homework must be handed in tomorrow. Also 乘坐 "我们乘坐火车去北京。" and 举行 "会议已经按计划举行了。"

#### Price, licence, compatibility, reviews
- **Price/licence:** free. No licence file in the repo (1-file README). Derivative decks say sentence reuse needs the author's permission [VERIFIED-DOCS].
- **Compatibility:** needs an Anki version that reads `.anki21b` (modern Desktop/AnkiDroid/AnkiMobile — INFERENCE from the format). Writing cards need internet. The author tells AnkiDroid users to enable "Type answer into the card" for typing [VERIFIED-DOCS]. No add-ons needed.
- **Known problems:**
  - Possible AI mispronunciations; the author asks users to flag them [VERIFIED-DOCS].
  - Volume: 9 notes per word; full set about 99k cards.
  - Author: "probably best suited to learners who have already completed at least a small amount of beginner Mandarin study" [VERIFIED-DOCS].
  - No focus-word cue on Listening/Reading cards, by design [COMMUNITY author reply].
- **Independent reviews:** 8 thumbs-up, 8 positive reviews. Examples: "game changer… comprehension is king" (2026-09-05); a request to show the focus word (2026-08-15) [COMMUNITY] — [AnkiWeb](https://ankiweb.net/shared/info/258311532)

#### Score: **75 / 100**
| Criterion | Score | Justification |
|---|---|---|
| Audio | 21/25 | Every sentence voiced, true audio-first cards, two voices; but AI voice with an author-acknowledged error risk |
| Examples | 15/20 | 3 varied sentences/word; AI-written, not native-verified |
| Level fit | 10/15 | HSK 1–2 sentences are short, but the author warns about absolute beginners; huge card load |
| Speaking | 11/15 | Reading cards invite reading aloud / dictation into the type box; cloze recall cards |
| Coverage | 9/10 | Exact 2025 list, all levels |
| Accuracy | 7/10 | Consistent sandhi/neutral-tone pinyin; single v1.0 release; unreviewed AI audio |
| Extras | 2/5 | Traditional + stroke order; no images; 3 note types per sentence complicates editing |

Uncertainty: ±7, mostly unverified audio naturalness and no HSK 1–4 file inspection.

### 4.3 "🔥 New HSK 3.0: Ultimate Mandarin Chinese Vocabulary – HSK n" (fa9r) — SECONDARY / CONDITIONAL

#### Identity and versions
- **URLs:** HSK1 [1736976202](https://ankiweb.net/shared/info/1736976202), HSK2 [801432412](https://ankiweb.net/shared/info/801432412), HSK3 [1925338742](https://ankiweb.net/shared/info/1925338742), HSK4 [1436074812](https://ankiweb.net/shared/info/1436074812), HSK5 [1660936380](https://ankiweb.net/shared/info/1660936380), HSK6 [2093332568](https://ankiweb.net/shared/info/2093332568), HSK7-9 parts [1145295418](https://ankiweb.net/shared/info/1145295418) / [501450951](https://ankiweb.net/shared/info/501450951) / [739669936](https://ankiweb.net/shared/info/739669936).
- **Issue tracker:** [GitHub fa9r](https://github.com/fa9r/anki-chinese-new-hsk-3.0-ultimate). Created 2026-10-10, README + licence only, no releases [VERIFIED-INSPECTED clone].
- **Updated:** 2026-10-10/11.
- **Sizes** [VERIFIED-DOCS]:
  - HSK1: 34.4 MB, 300 notes, 565 audio, 258 images.
  - HSK2: 19.0 MB, 200 notes, 395 audio, 195 images.
  - HSK7 part 1: 181 MB, 1,867 notes, 3,729 audio, 1,862 images.

#### Fields, card and lineage
- **Fields** [VERIFIED-DOCS samples]: Hanzi, Pinyin, Part of Speech, Meaning, SentenceHanzi, SentencePinyin, SentenceMeaning, AudioHanzi, AudioSentence, Image.
- **Card:** Hanzi→English recognition only [VERIFIED-DOCS].
- **Lineage:** base from "Last HSK 3.0 2026" (itself built from hnsaw HSK 1–5 and the tompat sentences for 6–9). The examples and audio of 2,683 words were replaced with "HSK-JK" material [VERIFIED-DOCS].
  - Author reply: "All kudos for audio go to the creator of original 'HSK - JK' decks who put in the effort to manually record all these… The later decks in the series still use original deck audio" [COMMUNITY/author]. So HSK-JK human recordings cover the HSK 2.0 portion of words; other words keep Last-HSK audio of unstated origin.

#### Claimed changes
- **Data fixes** [VERIFIED-DOCS]:
  - 1,003 pinyin fixes (看 kān→kàn, 银行 yín xíng→yín háng, 了 liǎo→le).
  - 402 look-alike radical characters normalised (⼋→八).
  - Meanings checked with "OpenAI GPT 6 Luna" (a claim I did not verify).
- **Sandhi:** "changed the pinyin of 102 words from tone-sandhi to dictionary-form spelling (e.g. 一下 yíxià → yīxià)". This diverges from the official 2025 syllabus spelling (yíxià) [VERIFIED-DOCS vs VERIFIED-INSPECTED official].
- **Licence:** CC BY-NC-SA 4.0, except the sentences [VERIFIED-DOCS].

#### Samples and reviews
- **Samples** [VERIFIED-DOCS, AnkiWeb]:
  - 路上 | lùshang | 我在路上看见了老师。 | Wǒ zài lùshang kànjiàn le lǎoshī. | I saw the teacher on the road. | AudioHanzi + AudioSentence + Image
  - 白色 | báisè | 我喜欢白色的衣服。 | Wǒ xǐhuan báisè de yīfu.
  - 药店 | yàodiàn | 药店在学校旁边。
  - 外 | wài | 外面在下雨。 | Wàimian zài xiàyǔ.
- **Reviews:** 5 positive on HSK1, e.g. "For the ones obsesed with pronunciation and tones, the clear audios are awesome" (2026-10-16) [COMMUNITY].

#### Score: **67 / 100** (high uncertainty ±10; not inspected)
| Criterion | Score | Justification |
|---|---|---|
| Audio | 16/25 | Word + sentence audio claimed for all and part human-recorded, but the mix and coverage are unverified (565 audio for 300 notes at HSK1 suggests some sharing or gaps) |
| Examples | 13/20 | One sentence/word, partly hand-curated (JK) |
| Level fit | 11/15 | Images and simple sentences, but dictionary-form sandhi pinyin |
| Speaking | 7/15 | Recognition only |
| Coverage | 9/10 | Full 2025 list |
| Accuracy | 7/10 | Many documented fixes; new deck |
| Extras | 4/5 | Images on every card |

### 4.4 "Last HSK 3.0 2026 (From official list)" — not primary
- **URLs and size** [VERIFIED-DOCS]: [HSK1 1623336797](https://ankiweb.net/shared/info/1623336797), [HSK4 562028400](https://ankiweb.net/shared/info/562028400), [HSK6 395921696](https://ankiweb.net/shared/info/395921696). Updated 2026-07-17/19. The set is about 996 MB: 11,000 entries, 21,928 audio, 10,737 images.
- **Cards and audio** [VERIFIED-DOCS]: Recognition, Typing and Writing (English→handwritten). Audio: author "Replaced the vocabulary and sentence audio" (HSK1–5) and "Created vocabulary and sentence audio" (6–9). Engine not stated.
- **Known errors:** the HSK1 sample uses the Kangxi radical "⼈" (U+2F08) for 人 [VERIFIED-DOCS sample]. The derivative documents 402 such characters and 1,003 pinyin errors [VERIFIED-DOCS].
- **Reviews:** "by far the best set" (2026-10-13; that reviewer then made the Ultimate fork) [COMMUNITY].
- **Samples** [VERIFIED-DOCS]: 谁 shéi/shuí | 那个人是谁？ | Nàge rén shì shéi?; ⼈ rén | 这个人是我老师。; 这个 zhège | 这个很好吃。
- **Score: ~60** (audio 14, examples 12, level 10, speaking 9, coverage 9, accuracy 3, extras 5). Superseded by Ultimate on data quality, but keeps production cards. Uncertainty ±10.

### 4.5 hnsaw "NEW HSK 3.0 2026 (Hanzi, Eng, Sentence, Audio, Pic,) – 1" — not primary
- **Identity** [VERIFIED-DOCS]: [AnkiWeb 413677233](https://ankiweb.net/shared/info/413677233). Updated 2026-05-29, 57.8 MB, 301 notes, 590 audio, 272 images. Recognition / Typing / Writing cards; CC BY-NC-SA.
- **Author's caveats** [VERIFIED-DOCS]: "Some cards have audio while some don't because I used local Microsoft TTS… may sound a bit more robotic"; pictures "auto-sourced from Google using Python".
- **Sample** [VERIFIED-DOCS]: 男朋友 nánpéngyou | 他是我的男朋友。 | Tā shì wǒ de nánpéngyou.
- **Score: ~52.** Old-style TTS with incomplete coverage. Superseded by Last HSK / Ultimate, which reused it.

### 4.6 krmanik Anki-xiehanzi "New HSK 3.0 (2025) Mandarin with example sentences" / "(Separate Deck)" — not primary (no sentence audio)
- **Identity** [VERIFIED-DOCS]: [397871109](https://ankiweb.net/shared/info/397871109), [701666449](https://ankiweb.net/shared/info/701666449). 44,292 notes, 10,901 audio (word level), updated 2025-12-22/23.
- **Cards:** meaning, pinyin/zhuyin, audio + pinyin, stroke drawing. Example sentences are via a tatoeba link or text; the sample shows only word fields [VERIFIED-DOCS].
- **Audio:** the repo's 2025 word audio was replaced with "Yue Tan's voice" (native recordings from audio-cmn) on 2026-10-24 [VERIFIED-INSPECTED git log]. Whether the AnkiWeb decks (Dec 2025) contain that audio is UNVERIFIED.
- **Generator:** the author points users to a new web app generator (SvelteKit rewrite using the 2025 lists) [VERIFIED-DOCS, [forum](https://forums.ankiweb.net/t/working-on-new-version-of-anki-xiehanzi-web-based-chinese-words-deck-generator/70014)].
- **Score: ~45** (sentence audio 2/25). Good for word-level tones and writing; fails the sentence-audio rule.

### 4.7 RyanGibb/anki-hsk3 (build-it-yourself) — not primary
- **Contents:** 2025 list, 10,999 vocab + 1,200 writing + 2,038 grammar cards. Grammar cards show an **official chinesetest.cn example sentence and play its audio** [VERIFIED-DOCS] — [GitHub](https://github.com/RyanGibb/anki-hsk3)
- **Audio:** word recordings from Shtooka / Yue Tan audio-cmn (CC-BY-SA). Anything not covered is voiced by Azure `zh-CN-XiaoxiaoNeural` via `tts.py`, which needs the user's own AZURE_SPEECH_KEY [VERIFIED-INSPECTED repo source].
- **No release:** you must build a ~240 MB .apkg yourself (downloads ~1.2 GB Wiktionary + ~300 MB recordings) [VERIFIED-DOCS]. Last commit 2026-10-02.
- **Score: n/a** (not distributable). Interesting for grammar sentences with official examples, if someone builds it.

### 4.8 Legacy / 2021-list decks (mentioned for completeness; not primary for the 2026+ exam)
- **"HSK 1 - JK"** [VERIFIED-DOCS] — [132435921](https://ankiweb.net/shared/info/132435921)
  - HSK 2.0 level 1: 150 notes, 282 audio, 130 images; 2021-08-05; 115 up / 2 down.
  - Fields include Simplified/Traditional, Pinyin.1 / Pinyin.2, Audio, SentenceSimplified, SentenceSimplifiedCloze, SentencePinyin, SentenceMeaning, SentenceAudio, SentenceImage.
  - Sample: 医院 yīyuàn | 妈妈在医院工作。 | Māma zài yīyuàn gōngzuò. | `[sound:…]` ×2 + image.
  - Audio described as manually recorded (by the Ultimate author) [COMMUNITY]. Higher JK levels not located (Gap).
- **ChineseAudioFlashcards "Chinese HSK 1 – 150 Words, 300 Example Sentences, with Audio"** [VERIFIED-DOCS] — [1578796058](https://ankiweb.net/shared/info/1578796058)
  - HSK 2.0, 2016, 451 notes. "All sentences are written and read by native mandarin speakers" [MARKETING].
  - Sample "这个苹果一块钱。 / Zhège píngguǒ yīkuài qián." uses citation-tone 一 (yīkuài, not yí kuài).
  - HSK 2–5 sold separately; a 2026-05 review calls the paid set "organized extremely poorly" [COMMUNITY].
- **"Chinese HSK 1 – Simpl., Trad., Pinyin, Zhuyin, Audio, Images"** [VERIFIED-DOCS] — [1081958254](https://ankiweb.net/shared/info/1081958254)
  - HSK 2.0, 150 notes, 300 audio.
  - "Audio was recorded by my girlfriend (native Mandarin speaker)" [MARKETING].
  - One review reports misaligned sentence audio [COMMUNITY, via search snippet].
- **"Another HSK 3.0 vocabulary deck"** (2021 list) [VERIFIED-DOCS] — [549107549](https://ankiweb.net/shared/info/549107549)
  - Azure neural TTS word audio.
  - About 1/3 of words have tatoeba sentences, without pinyin or audio.
- **"Mandarin Chinese: New HSK 3.0 Vocabulary and Characters"** (2021 list; word audio only) — [1144807196](https://ankiweb.net/shared/info/1144807196)
- **Mega Mandarin HSK 3.0** (paid; 2021 list + HSK 2.0; native word audio per reviews; no sentence audio) — [2062516907](https://ankiweb.net/shared/info/2062516907)
- **hskcore.com** (HSK 2.0, 150 → 5,000 words; "Native Mandarin MP3 audio" per word; example sentences without stated audio) — [hskcore](https://hskcore.com/hsk-anki-decks/)
- **Bamboo HSK** (Gumroad, paid): page content not retrievable — [gumroad](https://bamboohsk.gumroad.com/l/TdXok) [UNVERIFIED]

### Inferences
- For this learner, weak on tones and listening but with Hanzi strength, the decisive features are (a) audio-first cards and (b) reliable sandhi-aware pinyin.
  - NewHSK3 is the only 2025-list deck with built-in audio-only sentence cards.
  - HSKStory is the gentlest entry and has exact 2025 HSK1–3 coverage.
  - Ultimate's switch to dictionary-form 一/不 pinyin is a minus for tone learners: written pinyin then disagrees with what the audio should say.
- Decks without verified full-sentence audio are excluded from primary use under the hard rule, even if well liked.
- Official or semi-official exports from Hack Chinese, Chinese Zero to Hero, HelloChinese, Dong Chinese or Pleco: I found no Anki export with sentence audio (not deeply searched; see Gaps).

### Gaps
- **Not inspected:** AnkiWeb downloads were blocked (HTTP 429 "Please log in to download more decks"), and the AnkiWeb search endpoint was also rate-limited. So:
  - Ultimate, Last HSK, hnsaw, HSK-JK and NewHSK3 HSK 1–4 were not inspected.
  - AnkiWeb-wide searches for Japanese-, Chinese- or Vietnamese-titled HSK decks were incomplete; web searches in JP, CN and VI found no such deck with sentence audio.
- HSK-JK levels 2–6 deck IDs not found.
- No independent (non-creator) evidence on whether HSKStory voices are human or TTS.
- No Reddit/Zhihu/note.com reviews of the 2025-list decks were found (they are 1–4 months old).
- Hack Chinese / Dong Chinese / Chinese Zero to Hero / Pleco Anki exports not verified (only briefly searched).

---

## Sources

Official / primary:
- HSK 考试大纲 (2025-11 发布, 2026-07 实施), CLEC PDF: https://hsk.cn-bj.ufileos.com/3.0/%E6%96%B0%E7%89%88HSK%E8%80%83%E8%AF%95%E5%A4%A7%E7%BA%B21219.pdf
- CTI "HSK 3.0 will be officially launched worldwide on December 13, 2026!": https://www.chinesetest.cn/news/51336883 (text via https://admin.chinesetest.cn/gonewcontent.do?id=51336883)
- CTI X post (same notice; ID decodes to 2026-09-09): https://x.com/HSKTestOfficial/status/2097633616931041329
- CTI 2027 test calendar: https://admin.chinesetest.cn/gonewcontent.do?id=51619013
- MOE / 中国教育报 2025-11-17 (HSK3.0 launched at 2025 World Chinese Language Conference): http://www.moe.gov.cn/jyb_xwfb/s5147/202511/t20251117_1420566.html
- ChinaNews 2025-12-19 (HSK3.0 global pilot 2026-01-31): https://www.chinanews.com.cn/edu/2025/12-19/10536380.shtml
- Beijing gov (EN) 2025-12-22: https://english.beijing.gov.cn/studyinginbeijing/news/202512/t20251222_4355931.html
- MOE 2021-03-29 GF0025-2021 release: http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202103/t20210329_523304.html ; PDF: http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202103/W020210329527301787356.pdf
- China Daily 2022-11-05 (first HSK 7–9 test on 26 Nov 2022): https://www.chinadaily.com.cn/a/202211/05/WS6365aa87a3105ca1f22742c8.html

Secondary:
- Wikipedia, Hanyu Shuiping Kaoshi: https://en.wikipedia.org/wiki/Hanyu_Shuiping_Kaoshi
- studycli, New HSK 3.0: https://studycli.org/hsk/the-new-hsk/

Data sets / repos:
- https://github.com/krmanik/HSK-3.0
- https://github.com/elkmovie/hsk30
- https://github.com/drkameleon/complete-hsk-vocabulary
- https://github.com/RyanGibb/anki-hsk3
- https://github.com/krmanik/Anki-xiehanzi
- https://forums.ankiweb.net/t/working-on-new-version-of-anki-xiehanzi-web-based-chinese-words-deck-generator/70014

Decks (AnkiWeb pages; metadata via `https://ankiweb.net/svc/shared/item-info?sharedId=<id>`):
- HSKStory:
  - https://hskstory.com/anki/hsk-1 ; https://hskstory.com/about
  - https://audio.hskstory.com/downloads/anki/hskstory-hsk1-anki-v11.apkg (also hsk2-v10, hsk3-v9, hsk4-v10, hsk5-v8, hsk7-9-v8)
  - https://ankiweb.net/shared/info/1703580298 ; https://ankiweb.net/shared/info/223368909 ; https://ankiweb.net/shared/info/1226554191 ; https://ankiweb.net/shared/info/2047844854 ; https://ankiweb.net/shared/info/735797420 ; https://ankiweb.net/shared/info/926470945
- NewHSK3 sentence deck: https://ankiweb.net/shared/info/258311532 ; https://github.com/NewHSK3/new-hsk-3-anki-deck ; https://github.com/NewHSK3/new-hsk-3-anki-deck/releases/tag/v1.0
- Ultimate: https://ankiweb.net/shared/info/1736976202 ; https://ankiweb.net/shared/info/801432412 ; https://ankiweb.net/shared/info/1925338742 ; https://ankiweb.net/shared/info/1436074812 ; https://ankiweb.net/shared/info/1660936380 ; https://ankiweb.net/shared/info/2093332568 ; https://ankiweb.net/shared/info/1145295418 ; https://ankiweb.net/shared/info/501450951 ; https://ankiweb.net/shared/info/739669936 ; https://github.com/fa9r/anki-chinese-new-hsk-3.0-ultimate
- Last HSK 3.0 2026: https://ankiweb.net/shared/info/1623336797 ; https://ankiweb.net/shared/info/562028400 ; https://ankiweb.net/shared/info/395921696
- hnsaw: https://ankiweb.net/shared/info/413677233
- krmanik: https://ankiweb.net/shared/info/397871109 ; https://ankiweb.net/shared/info/701666449 ; https://ankiweb.net/shared/info/239300382 ; https://ankiweb.net/shared/info/536858343 ; https://ankiweb.net/shared/info/1063372083 ; https://ankiweb.net/shared/info/1351435439
- 2021-list decks: https://ankiweb.net/shared/info/549107549 ; https://ankiweb.net/shared/info/1144807196 ; https://ankiweb.net/shared/info/2062516907 ; https://ankiweb.net/shared/info/640224122 ; https://ankiweb.net/shared/info/85606670
- Legacy HSK 2.0: https://ankiweb.net/shared/info/132435921 ; https://ankiweb.net/shared/info/1578796058 ; https://ankiweb.net/shared/info/1081958254 ; https://ankiweb.net/shared/info/1817307679 ; https://hskcore.com/hsk-anki-decks/ ; https://bamboohsk.gumroad.com/l/TdXok
- Language-specific search results (no JP/CN/VI HSK 3.0 Anki deck with sentence audio found): https://studycli.org/ja/chinese-tools/hsk-3-vocabulary/ ; https://studycli.org/zh-CN/chinese-tools/hsk-3-vocabulary/
