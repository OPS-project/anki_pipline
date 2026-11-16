# Card design for productive vocabulary, Anki/FSRS in late 2026, and sentence-audio/context pipelines (Mandarin, Japanese, English)

Research date: **2026-11-13**. Learner profile: a Vietnamese IT/DX engineer living in Japan.
- **Mandarin:** beginner, following an HSK-structured route. Strong Hanzi recognition via Japanese; weak tones and listening.
- **Japanese:** N2 moving to N1, aiming for speaking beyond N1.
- **English:** C1, aiming for C2 expressiveness.

**Coordinator priority update:** for Japanese and English, the main route is sentence cards mined from authentic native media (drama, film, TV, podcasts, talks, news, workplace talk), not exam or word-list decks. That workflow gets extra depth in Section 5B.

**Evidence labels used on every claim:**
- `[VERIFIED-DOCS]`: official documentation, release notes or a peer-reviewed paper. For papers, the citation was confirmed via Crossref/OpenAlex this session. Where the finding was also read from the abstract this session, it says "abstract read".
- `[COMMUNITY]`: user or forum reports.
- `[MARKETING]`: vendor claims.
- `[UNVERIFIED]`: not confirmed this session. This includes my own estimates and items from prior knowledge.
- `[LOCAL-TEST]`: something I ran on this machine on 2026-11-13. It counts as verified, but only for what was run.

---

## Top findings

1. **Anki has no tool that trains speaking fluency directly.** Retrieval practice and spacing are among the most robust findings in learning science (Karpicke & Roediger 2008; Cepeda et al. 2006/2008; Kim & Webb 2022 meta-analysis), so Anki builds accessible lexical knowledge. Deliberate flashcard learning can even produce automatic, "lexicalised" knowledge (Elgort 2011). Oral fluency, however, improves through *repeated speaking*: in de Jong & Perfetti 2011, gains were maintained only by learners who repeated their speeches. In Nation's four strands, Anki covers only "language-focused learning" `[VERIFIED-DOCS]`.
2. **Productive (L1/cue→L2) retrieval builds productive knowledge. Receptive retrieval mostly builds receptive meaning.**
   - Webb 2009: productive learning of word pairs gave larger gains in productive meaning, orthography, syntax and grammatical functions.
   - Laufer & Goldstein 2004: active recall is the hardest strength level.
   - Nakata 2016: recall formats beat recognition for productive orthographic knowledge.
   - Kang et al. 2013: retrieval practice beat imitation ("repeat after me") for foreign vocabulary.
   - **Upshot:** add production cards, but only for items you actually want to say `[VERIFIED-DOCS]`.
3. **Sentence context alone is not magic.** A single glossed sentence gave no measurable advantage over word pairs (Webb 2007). Translation learning gives more words, but weaker learners transfer worse to L2 contexts (Prince 1996).
   - The value of sentence cards for this learner lies in real-life audio, collocation, pragmatics, and the chance to practise production in context.
   - I found no rigorous head-to-head studies of cloze versus flashcards. Cloze is a reasonable design choice, not an evidence-proven winner `[VERIFIED-DOCS]` / `[UNVERIFIED]`.
4. **Shadowing improves bottom-up listening and phoneme perception, and with self-recording it improves comprehensibility and fluency, but not accentedness.**
   - Hamada 2016: listening gains were strongest for lower-proficiency learners.
   - Foote & McDonough 2017: 8 weeks, at least 4 sessions of at least 10 minutes per week, with self-recording.
   - **Upshot:** short (one-line) sentence-audio cards double as shadowing material, but run shadowing as a separate routine `[VERIFIED-DOCS]`.
5. **Mandarin tones:** high-variability perceptual training (many talkers) gave about a 21% gain in tone identification, which generalised and was retained after 6 months (Wang et al. 1999). Tone colour helps, but slightly less than pitch contours or tone numbers (Godfroid et al. 2017).
   - **Upshot:** use audio-first cards with Hanzi hidden on the front (this learner can read Hanzi through Japanese and would bypass the audio), with tone marks or numbers plus colour on the back `[VERIFIED-DOCS]`.
6. **Anki state as of 2026-11-13:**
   - **Desktop:** latest stable is 26.09.4 (2026-11-04), a security release. 26.11b1 (beta, 2026-11-12) adds `{{type:ci:}}`. FSRS is the scheduling engine (fsrs-rs 6.6.2 in 26.09). FSRS-6 (21 parameters, trainable forgetting-curve decay, new same-day-review formula) arrived in Anki 25.07.
   - **Mobile:** AnkiDroid 2.25.3 is the latest stable (2026-10-17; the 2.25 line matches Anki 26.05 features). AnkiMobile 26.10 was released 2026-11-03.
   - **FSRS defaults:** desired retention 90% by default, and the manual advises staying below 97%. Optimise about monthly. Help Me Decide simulator, health check, Easy Days (24.11) and load balancer (24.10/24.11) are all built in `[VERIFIED-DOCS]`.
7. **Mobile rule of thumb:** add-ons never run on AnkiDroid or AnkiMobile. Anything an add-on writes into fields at edit time syncs and works on mobile: audio files, furigana, pitch HTML, tone-coloured spans (colours also need the CSS in the template). Things rendered live by an add-on, such as HyperTTS realtime TTS, are desktop-only.
   - The built-in `{{tts}}` filter uses the device's OS voices on every platform, so it is a zero-cost fallback. Linux needs an add-on.
   - On iOS, prefer **mp3** audio. AnkiMobile has trouble with Opus, and iOS Lockdown Mode disables Opus and AVIF.
   - Sources: `[VERIFIED-DOCS]` (Anki manual, mpvacious, asbplayer and HyperTTS docs).
8. **TTS options for existing decks (late 2026):**
   - **HyperTTS** (free add-on, GPL) does batch audio for a whole deck.
     - Free services: GoogleTranslate, NaverPapago (which includes Japanese and English), Youdao (English), and the Windows/macOS system voices.
     - Premium services, with your own API key or the vocab.ai subscription: Azure, Google, Amazon, OpenAI, ElevenLabs, IBM Watson, Naver, and since v3.1.0 (2026-04-19) Gemini TTS.
     - The vocab.ai plan starts at **$5/month for 250K characters** `[MARKETING]`.
   - **edge-tts** (free, unofficial Python client for Microsoft Edge's online voices) **worked on 2026-11-13** in my local test (v7.3.1). Voices: 6 standard zh-CN voices, only 2 ja-JP voices (Nanami, Keita), and many en-US/en-GB voices. Custom SSML is not supported, so you cannot force a reading `[LOCAL-TEST]` / `[VERIFIED-DOCS]`.
   - **Azure** neural TTS does accept SSML `<phoneme>` overrides: pinyin with tone numbers for zh-CN, katakana with accent marks for ja-JP. That is the best repair path for polyphone (多音字) and pitch-accent errors `[VERIFIED-DOCS]`.
9. **Neural TTS error classes are well documented, but I found no error rates for Azure, Google or edge voices `[VERIFIED-DOCS]` / gap:**
   - Mandarin: Tone-3 sandhi chains and polyphones whose reading depends on the part of speech.
   - Japanese: kanji reading choice and pitch accent. Research says the text frontend lacks pitch-accent information.
   - Recommended QA: listen to 100% of sentences that contain flagged polyphone characters or readings, plus a 5–10% random sample `[UNVERIFIED — my recommendation]`.
10. **Native-audio sources (counts fetched 2026-11-13):**
    - **Tatoeba** has 850,274 English, 6,332 Japanese and 5,826 Mandarin sentences with audio. Text is CC BY 2.0 FR; audio licences vary per contributor, and some are NC or ND `[VERIFIED-DOCS]`.
    - **Immersion Kit** claims a database of about 500k anime sentences, Japanese only `[MARKETING]`.
    - **Recommended mining stack for Japanese and English:**
      - **asbplayer** (free, AGPL): Netflix, YouTube, other streaming sites, and local files. It produces an Anki card with the sentence, a sentence-audio clip and a screenshot, through AnkiConnect, with one-key "update last card" after Yomitan.
      - **mpvacious** for local files in mpv.
    - **Language Reactor Pro** (about $4.99/month per a competitor's site `[UNVERIFIED]`) exports CSV plus media. A forum moderator says only Netflix lines keep the original audio; YouTube lines get a "robot voice" `[COMMUNITY]`.
    - **Migaku**: price could not be verified. Community reports say cards created in Migaku Memory cannot later be exported to Anki `[COMMUNITY]`.

---

## 1. Research evidence: retrieval direction, context, cloze, audio-first, reverse cards, shadowing, spacing, and the limits of SRS for speaking

### Takeaway
- Use retrieval practice with FSRS spacing as the backbone.
- Add productive (cue→L2) cards selectively for items you want to say, because learning direction transfers mainly to the matching kind of knowledge.
- Make cards audio-rich and short.
- Anki cannot build speaking fluency by itself. Fluency needs repeated meaning-focused speaking (4/3/2 retelling, shadowing with self-recording, conversation), so treat Anki as roughly the language-focused quarter of Nation's four strands.

### Cited Findings

**Receptive vs productive retrieval and transfer**
- **Webb 2005** (SSLA 27(1)) `[VERIFIED-DOCS, abstract read]`:
  - **Design:** Japanese EFL learners met target words either in three glossed sentences (reading) or in a sentence-production task (writing).
  - **With equal time on task,** reading was superior.
  - **When time depended on completion** (writing took longer), writing was more effective. The author argues that the second condition represents authentic learning, which favours productive tasks.
  - **Measures:** 5 aspects of word knowledge, each tested receptively and productively (10 tests per word).
  - Sources: [Webb 2005, doi:10.1017/S0272263105050023](https://doi.org/10.1017/S0272263105050023); [Cambridge Core](https://www.cambridge.org/core/product/DDF362AE7B13D1949B1CD591DA2F3414).
- **Webb 2009** (RELC Journal 40(3)) `[VERIFIED-DOCS, abstract-level summary via search]`:
  - **Productive learning of word pairs** gave larger gains in receptive and productive orthography, and in productive knowledge of meaning, syntax and grammatical functions.
  - **Receptive learning** gave larger gains in receptive meaning.
  - **Author's suggestion:** if only one method is used, productive learning may be more effective.
  - Source: [Webb 2009, doi:10.1177/0033688209343854](https://doi.org/10.1177/0033688209343854).
- **Laufer & Goldstein 2004** (Language Learning 54(3)) `[VERIFIED-DOCS, abstract read]`:
  - **Hierarchy of difficulty** (435 ESL learners), confirmed at all frequency levels: passive recognition (easiest) < active recognition < passive recall < active recall (hardest).
  - **Passive recall** (L2→meaning, recall) was the best predictor of classroom language performance.
  - Source: [doi:10.1111/j.0023-8333.2004.00260.x](https://doi.org/10.1111/j.0023-8333.2004.00260.x).
- **Nakata 2016** (IRAL 54(3)) `[VERIFIED-DOCS, abstract read]`:
  - **Design:** recognition, recall, hybrid and productive-recall-only formats compared; 64 learners, 60 Swahili–English pairs, flashcard software.
  - **Findings:** recall formats beat recognition for productive knowledge of orthography. Recognition is preferable when spelling knowledge is not needed.
  - Source: [doi:10.1515/iral-2015-0022](https://doi.org/10.1515/iral-2015-0022).
- **Nakata 2011** (CALL 24(1)) reviewed flashcard software against paired-associate learning principles `[VERIFIED-DOCS: citation only; content not re-read this session]`. Source: [doi:10.1080/09588221.2010.520675](https://doi.org/10.1080/09588221.2010.520675).
- **Nakata & Webb 2016** (SSLA, "Does studying vocabulary in smaller sets increase learning?") and **Nakata 2017** (SSLA, within-session repeated retrieval) exist `[VERIFIED-DOCS: citations only; findings not re-read this session]`. Sources: [doi:10.1017/S0272263115000236](https://doi.org/10.1017/S0272263115000236); [doi:10.1017/S0272263116000280](https://doi.org/10.1017/S0272263116000280).
- **Kang, Gollan & Pashler 2013** (Psychonomic Bulletin & Review 20, 1259–1265), "Don't just repeat after me: Retrieval practice is better than imitation for foreign vocabulary learning" `[VERIFIED-DOCS: citation and title; details from a slide summary]`. A slide summary says the retrieval condition used an L1 cue and recall, by writing rather than speaking `[COMMUNITY]`. Sources: [doi:10.3758/s13423-013-0450-z](https://doi.org/10.3758/s13423-013-0450-z); [slides](https://fr.slideshare.net/alandon429/kang-2013-presentation).
- **Schneider, Healy & Bourne 2002** (JML 46), "What is learned under difficult conditions is hard to forget: contextual interference effects in foreign vocabulary acquisition, retention, and transfer" `[VERIFIED-DOCS: citation only; the claim that harder L1→L2 practice is more durable is UNVERIFIED this session]`. Source: [doi:10.1006/jmla.2001.2813](https://doi.org/10.1006/jmla.2001.2813).
- **Barcroft 2006** (Second Language Research 22(4)) `[VERIFIED-DOCS, abstract read]`: copying new words while viewing word–picture pairs *reduced* productive learning compared with not writing. The author's explanation is that forced output without access to meaning exhausts the resources needed to encode new word forms. Source: [doi:10.1191/0267658306sr276oa](https://doi.org/10.1191/0267658306sr276oa).
- Schmitt's reviews (e.g., "Instructed second language vocabulary learning," LTR 2008) are standard syntheses `[UNVERIFIED: not fetched this session]`.

**Words in sentences vs isolation; cloze**
- **Webb 2007** (LTR 11(1)) `[VERIFIED-DOCS, abstract read]`:
  - Prior research had found little evidence that context helps; decontextualised tasks tend to be equally or more effective for meaning and form.
  - In this study, words learned in a single glossed sentence and as word pairs showed **no significant difference** across 10 measures, including grammatical functions and associations.
  - Source: [doi:10.1177/1362168806072463](https://doi.org/10.1177/1362168806072463).
- **Prince 1996** (MLJ 80(4)) `[VERIFIED-DOCS, abstract read]`: translation learning was superior in *quantity*, but weaker learners were unable to transfer that knowledge into L2 contexts. Source: [doi:10.1111/j.1540-4781.1996.tb05468.x](https://doi.org/10.1111/j.1540-4781.1996.tb05468.x).
- **Elgort 2011** (Language Learning 61(2)) `[VERIFIED-DOCS: citation via Crossref; findings via the full-text PDF snippet and secondary summaries]`: deliberate, decontextualised learning of pseudowords with word lists and flashcards produced priming effects. Deliberate learning drove both representational and functional (lexicalised) knowledge. Sources: [doi:10.1111/j.1467-9922.2010.00613.x](https://doi.org/10.1111/j.1467-9922.2010.00613.x); [PDF](https://www.lextutor.ca/freq/lists_download/elgort_2011.pdf).
- **Cloze vs flashcards:** I found no clean, replicated head-to-head study. Hits were a UWO thesis (sentence production vs flashcards, massed vs spaced; fill-in vs flashcards), a Haifa "second-hand cloze" study whose results I could not see, and vendor blogs (Clozemaster, Migaku) claiming cloze superiority `[MARKETING]`. Sources: [UWO thesis](https://ir.lib.uwo.ca/etd/8600/); [Haifa](https://cris.haifa.ac.il/en/publications/facilitating-long-term-retention-of-vocabulary-the-second-hand-cl/); [Clozemaster blog](https://www.clozemaster.com/blog/?p=7651).
- **Involvement Load Hypothesis** (Laufer & Hulstijn 2001, Applied Linguistics 22(1)): tasks that involve need, search and evaluation (e.g., gap-filling) promote retention more than passive exposure. This is the usual theoretical rationale for cloze/fill-in `[VERIFIED-DOCS: citation; summary from prior knowledge]`. Source: [doi:10.1093/applin/22.1.1](https://doi.org/10.1093/applin/22.1.1).

**Listening-first and tone training (Mandarin)**
- **Wang, Spence, Jongman & Sereno 1999** (JASA 106) `[VERIFIED-DOCS, abstract read]`:
  - **Training:** 8 sessions over 2 weeks of high-variability tone identification training, using natural words from several native talkers.
  - **Results:** about 21% improvement; generalisation to new stimuli (+18%) and to new talkers (+25%); retained after 6 months (+21%).
  - Source: [doi:10.1121/1.428217](https://doi.org/10.1121/1.428217).
- **Godfroid, Lin & Ryu 2017** (Language Learning 67(4)) `[VERIFIED-DOCS: summary via search]`: multimodal training (number, pitch contour, colour, colour+number, colour+contour) helped tone perception. There was a "small, practical advantage for pitch contours and numbers over color coding." Source: [doi:10.1111/lang.12246](https://doi.org/10.1111/lang.12246).

**Shadowing**
- **Hamada 2016** (LTR 20(1); Crossref lists online-first 2015) `[VERIFIED-DOCS, abstract read]`: 43 Japanese EFL learners; phoneme perception improved in both low- and intermediate-proficiency groups, but only low-proficiency learners improved on listening comprehension questions. The recommendation is to use shadowing for bottom-up listening. Source: [doi:10.1177/1362168815597504](https://doi.org/10.1177/1362168815597504).
- **Hamada 2019** (RELC Journal) review `[VERIFIED-DOCS, abstract read]`: beginners should start with "shadowing for listening" and move on to "shadowing for speaking." Source: [doi:10.1177/0033688218771380](https://doi.org/10.1177/0033688218771380).
- **Foote & McDonough 2017** (J. Second Language Pronunciation 3(1)) `[VERIFIED-DOCS, abstract read]`: 16 learners shadowed short dialogues on iPods for 8 weeks, at least 4 times a week for at least 10 minutes, recording themselves. They improved significantly on all speaking measures except accentedness (comprehensibility and fluency improved). Source: [doi:10.1075/jslp.3.1.02foo](https://doi.org/10.1075/jslp.3.1.02foo).
- Kadota's work (e.g., *Shadowing as a Practice in Second Language Acquisition*, Routledge 2019) is the main theoretical source `[UNVERIFIED: not fetched this session]`.

**Testing effect and spacing**
- **Karpicke & Roediger 2008** (Science 319), "The critical importance of retrieval for learning" `[VERIFIED-DOCS: citation]`. Repeated retrieval, not repeated study, drove delayed recall of foreign word pairs `[prior knowledge of the paper; details not re-read]`. Source: [doi:10.1126/science.1152408](https://doi.org/10.1126/science.1152408).
- **Cepeda et al. 2006** (Psych. Bulletin, distributed-practice meta-analysis) and **Cepeda et al. 2008** (Psych. Science, "temporal ridgeline": the optimal gap grows with the retention interval) `[VERIFIED-DOCS: citations; summaries from prior knowledge]`. Sources: [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354); [doi:10.1111/j.1467-9280.2008.02209.x](https://doi.org/10.1111/j.1467-9280.2008.02209.x).
- **Kim & Webb 2022** (Language Learning) L2 spacing meta-analysis `[VERIFIED-DOCS, abstract read]`: 98 effect sizes from 48 experiments (N = 3,411).
  - Spacing had a medium-to-large effect.
  - Longer spacing beat shorter spacing on delayed posttests.
  - **Equal and expanding spacing were statistically equivalent.**
  - Source: [doi:10.1111/lang.12479](https://doi.org/10.1111/lang.12479).
- **Seibert Hanson & Brown 2019/2020** (CALL), a study of Anki itself `[VERIFIED-DOCS, abstract read]`: 62 beginning Spanish learners. Days spent studying with Anki predicted end-of-semester performance after controlling for baseline ability and motivation, but students were reluctant to use it and reported low enjoyment. Source: [doi:10.1080/09588221.2018.1552975](https://doi.org/10.1080/09588221.2018.1552975).

**Limits of SRS for speaking fluency**
- **Nation 2007, "The Four Strands"** `[VERIFIED-DOCS: citation; content from prior knowledge]`: a balanced course has four roughly equal strands: meaning-focused input, meaning-focused output, language-focused learning, and fluency development. Flashcards belong to language-focused learning. Source: [doi:10.2167/illt039.0](https://doi.org/10.2167/illt039.0).
- **Swain's Output Hypothesis** (1985, in Gass & Madden, *Input in Second Language Acquisition*): pushed output drives noticing, hypothesis testing and metalinguistic reflection, which needs real communicative output and feedback `[UNVERIFIED: no DOI; from prior knowledge]`.
- **de Jong & Perfetti 2011** (Language Learning 61(2)) `[VERIFIED-DOCS, abstract read]`: in 4/3/2-minute speech training, fluency improved for all during training but was **maintained only by students who repeated the same speech**. The authors interpret this as proceduralisation. Source: [doi:10.1111/j.1467-9922.2010.00620.x](https://doi.org/10.1111/j.1467-9922.2010.00620.x).
- **Snellings, van Gelderen & de Glopper 2002** (Language Learning), "Lexical retrieval: An aspect of fluent second-language production that can be enhanced" `[VERIFIED-DOCS: citation and title; detailed results not re-read]`. The title states that lexical retrieval speed is trainable; follow-up work concerns written production. Source: [doi:10.1111/1467-9922.00202](https://doi.org/10.1111/1467-9922.00202).
- **Minimum information principle:** "Effective learning: Twenty rules of formulating knowledge" (Wozniak, SuperMemo) is the classic practitioner source for keeping cards atomic `[UNVERIFIED: not fetched this session; widely cited practitioner guidance]`.

### Inferences (card-type recommendations derived from the evidence)

**What Anki can do:**
- Durable form–meaning links (Karpicke & Roediger; Kim & Webb).
- Faster lexical access (Elgort; Snellings).
- Tone and phoneme perception through audio-first cards (Wang 1999; Hamada 2016).
- Productive recall of chosen expressions (Webb 2009; Nakata 2016).

**What Anki cannot do:**
- Proceduralised fluency from repeated speaking (de Jong & Perfetti).
- Pushed output with feedback (Swain).
- Turn-taking and pragmatics in real time.
- Accent change: even shadowing did not change accentedness (Foote & McDonough).

**Card types per language:**
- **Audio-first recognition (all three languages; most important for Mandarin):**
  - **Front:** sentence audio only, plus optionally a screenshot. No text.
  - **Task:** understand it, and for Mandarin, say the tones of the target word.
  - **Back:** transcript (Hanzi + pinyin with tone marks or numbers + colour), meaning, and audio replay.
  - **Mandarin:** hide Hanzi on the front, because Japanese-literate learners can otherwise read through it. Use 2–3 different TTS voices or native speakers across notes to mimic high-variability training.
- **Sentence or cloze cards on a single chunk:**
  - Cloze one collocation or expression only, not several gaps.
  - Play the full-sentence audio on the back, with the option of also playing it on the front for an "audio-assisted cloze."
  - The evidence for cloze is theoretical (involvement load), not head-to-head.
- **Expression-to-context recall (productive; for Japanese N1+ and English C2):**
  - **Front:** a situation or paraphrase prompt, e.g., an English or Japanese gloss: "politely decline the proposal while leaving room for later."
  - **Task:** *say* the target expression or sentence aloud.
  - **Back:** the native sentence with audio, so you can compare.
  - This is productive recall, the hardest level (Laufer & Goldstein). Webb 2009 and Nakata 2016 predict gains in productive knowledge.
  - Limit it to a curated subset (e.g., tag `produce`) to control workload.
- **Reverse cards (L1→L2):**
  - **Value:** productive knowledge (Webb 2009).
  - **Cost:** each one adds a full card and they are harder; generating them for every note roughly doubles reviews `[UNVERIFIED estimate]`.
  - For Mandarin, a reverse card should mean "meaning/picture → say the word with tones, then check the audio," not "type the Hanzi," unless handwriting is a goal.
- **Type-in answers:** useful for recalling spelling (English collocations, Japanese kana). Do not use them as copying drills for brand-new words (Barcroft 2006).
- **Shadowing-friendly cards:** one subtitle line or 2–8 s of audio, transcript hidden on the front, replay button. Do the shadowing in a separate daily session rather than inside reviews, because reviews optimise retrieval, not imitation (Kang et al.). `[UNVERIFIED: design recommendation]`
- **Long sentences:**
  - Keep the card's *task* atomic: one target chunk.
  - Keep the long sentence as context on the back, or trim the clip to the clause containing the target.
  - FSRS assigns one memory state per card. If a card bundles several unknowns, a lapse on any of them resets the whole card `[UNVERIFIED reasoning, consistent with the minimum information principle]`.

### Gaps
- No rigorous, replicated studies directly compare cloze cards with word cards, or audio-front with text-front SRS cards, for advanced learners.
- I found no study of Anki/FSRS specifically for *speaking* outcomes.
- The Kang et al. 2013 detailed results, the Schneider et al. 2002 direction-of-learning results, and the Snellings 2002 effect sizes were not re-read this session.

---

## 2. Anki / FSRS / mobile status (as of 2026-11-13)

### Takeaway
- **Use:** Anki desktop 26.09.4, AnkiDroid 2.25.3, AnkiMobile 26.10.
- **FSRS is mature:** FSRS-6 since 25.07, fsrs-rs 6.6.2 in 26.09.
- **Recommended setup:**
  - Desired retention 0.90 (try 0.85–0.88 for large mined decks if workload bites; check with Help Me Decide).
  - Same-day learning steps such as 10m or 30m.
  - Optimise each preset monthly with the health check on.
  - Separate presets per language.
  - Easy Days, load balancer and sibling burying all on.

### Cited Findings

**Desktop versions**
- **26.09.4** = "Latest" stable (04 Nov 2026), security fixes only. **26.11b1** = pre-release (12 Nov 2026), which:
  - adds the `{{type:ci:}}` case-insensitive answer filter,
  - fixes FSRS with the load balancer, easy days and the simulator,
  - fixes macOS 13/14 audio.
  - `[VERIFIED-DOCS]` [GitHub releases](https://github.com/ankitects/anki/releases).
- **26.09** (14 Sep 2026) `[VERIFIED-DOCS]` [release 26.09](https://github.com/ankitects/anki/releases/tag/26.09):
  - "Update FSRS to 6.6.2".
  - Memory state recomputed when a card changes deck.
  - Legacy `anki.importing` and `anki.exporting` removed, with temporary AnkiConnect wrappers. This matters for older add-ons.
- **26.08** updated to fsrs-rs 6.6.1 `[VERIFIED-DOCS via mirror]` [newreleases 26.08](https://newreleases.io/project/github/ankitects/anki/release/26.08).
- **26.05** `[VERIFIED-DOCS]` [release 26.05](https://github.com/ankitects/anki/releases/tag/26.05):
  - "Improve sibling dispersal in the load balancer, including across presets".
  - "Don't reschedule suspended cards".
  - Three clicks required to unlock FSRS parameter editing.
  - Reworked "Help Me Decide" efficiency graph.
  - WindowsRT TTS player re-enabled on Windows 11.
- **25.07** `[VERIFIED-DOCS via mirror]` [newreleases 25.07](https://newreleases.io/project/github/ankitects/anki/release/25.07):
  - "FSRS-6 brings further algorithm improvements".
  - Evaluate button replaced by an optional health check.
  - Load balance and easy days supported when rescheduling and in the simulator.
- **24.10/24.11** `[VERIFIED-DOCS via mirrors]` [24.11 notes](https://newreleases.io/project/github/ankitects/anki/release/24.11); [24.10beta1](https://newreleases.io/project/github/ankitects/anki/release/24.10beta1):
  - **Load balancer**, introduced in the 24.10 betas: within the fuzz range, it picks days with fewer reviews.
  - **Native Easy Days** in 24.11.
  - **FSRS-5**, which adds same-day-review parameters.
- **FSRS-6 algorithm** `[VERIFIED-DOCS]` [FSRS wiki — The Algorithm](https://github.com/open-spaced-repetition/awesome-fsrs/wiki/The-Algorithm):
  - 21 parameters.
  - Forgetting-curve decay is trainable (w20). R(S,S) = 90% by definition.
  - The stability-after-same-day-review formula changed: "S increases faster when it's small and slower when it's large".
  - There is no FSRS-7 on the wiki.

**Manual guidance (deck options)** `[VERIFIED-DOCS]` [Anki manual — Deck Options](https://docs.ankiweb.net/deck-options.html):
- **Enabling FSRS:**
  - The toggle is global.
  - Supported clients: Anki 23.10+, AnkiMobile 23.10+, AnkiWeb, AnkiDroid 2.17+.
- **Desired retention:**
  - "The default is 90%, which offers a good balance of retention and workload." Higher values raise workload quickly; "above 97% the workload can be overwhelming".
- **Optimiser:**
  - Optimising "once every month is sufficient". "Optimize All Presets" runs it for every preset.
  - Separate presets are suggested for decks of very different difficulty.
  - Do not hand-edit or copy parameters.
  - The health check flags "less than a few hundred" reviews as too few. Do not use Hard for forgotten answers ("it is a passing grade").
- **Learning steps with FSRS:**
  - Keep them under 1 day; "10m or 30m are good"; "23h is not recommended"; keep them minimal.
  - An empty field lets FSRS handle short-term scheduling (experimental).
- **Workload and other options:**
  - **Help Me Decide (experimental):** simulates workload at different retention levels using your own memory states.
  - **Reschedule cards on change:** not recommended when first switching from SM-2.
  - **Workload rule of thumb:** 20 new cards/day ≈ "roughly about 200 cards/day" of reviews. Stop adding new cards while a backlog is overdue.
  - **Bury siblings:** new, review and interday-learning burying options exist.

**Known issue:** a forum report says the Help Me Decide simulator failed silently when a preset had fewer than 21 parameters after upgrading from 25.09 to 26.05 `[COMMUNITY]` [forum](https://forums.ankiweb.net/t/bug-fsrs-desired-retention-simulator-expects-21-parameters-but-decks-support-less-than-that-leading-to-silent-failure/70285).

**AnkiDroid**
- **Latest stable:** 2.25.3 (17 Oct 2026). 2.26.0 alphas are running, with alpha13 on 10 Nov 2026 `[VERIFIED-DOCS]` [GitHub releases](https://github.com/ankidroid/Anki-Android/releases).
- **2.25 changelog** (28 Sep 2026) `[VERIFIED-DOCS]` [AnkiDroid 2.25 changelog](https://forums.ankiweb.net/t/ankidroid-2-25-changelog/71237):
  - Includes "Anki 26.05 features", among them "FSRS: faster calculations and better spacing of siblings."
  - "TTS: Support all installed engines."
  - "New Study Screen: Card templates can record audio" (useful for production and shadowing self-checks).
  - Security change: the JavaScript API now blocks calls that read or modify other cards. This can be unblocked in advanced settings.

**AnkiMobile**
- **26.10** (announced 3 Nov 2026, phased rollout): Browse redesign, deck-list counts, sync conflict dialog that matches desktop, VoiceOver improvements. No FSRS or template changes are listed `[VERIFIED-DOCS]` [AnkiMobile 26.10 forum post](https://forums.ankiweb.net/t/ankimobile-26-10-is-out/74202).
- AnkiMobile has had built-in FSRS support since 23.10/23.12 `[VERIFIED-DOCS]` (manual lists 23.10+).

**Template features and mobile caveats** `[VERIFIED-DOCS]` [Anki manual — Field replacements](https://docs.ankiweb.net/templates/fields.html):
- **`{{tts}}`:**
  - Syntax: `{{tts zh_CN:Field}}`, with `voices=` and `speed=0.8` options; speed works only on some platforms.
  - `{{tts-voices:}}` lists the available voices.
  - Uses OS voices on Windows, macOS and iOS; Linux needs an add-on.
- **Type-in:** `{{type:Field}}`, `{{type:nc:}}`, `{{type:ci:}}` and `{{type:cloze:Text}}`.
  - One comparison per card.
  - The box does not appear on AnkiWeb or in preview.
  - AnkiMobile lacks the `typeMissed` class.
- **Other filters:** `{{hint:Field}}` cannot hide audio. `{{furigana:}}`, `{{kana:}}` and `{{kanji:}}` use `漢字[かんじ]` ruby syntax.
- **Media in templates:**
  - Field media references inside templates (`[sound:{{Field}}]`) do not work; put `[sound:...]` in the field itself.
  - `{{FrontSide}}` does not replay front audio on the back.
  - Static template files need a `_` prefix.
- Note: `{{type:ci:}}` appears in the manual, but the GitHub notes list it as new in 26.11b1. On stable 26.09.4 it may not exist yet `[VERIFIED-DOCS; possible doc/version mismatch]`.

**Add-ons and mobile**
- **Desktop only:** HyperTTS's own page says realtime audio generation works only on Anki desktop, while audio generated into the collection plays in AnkiMobile and AnkiDroid `[VERIFIED-DOCS]` [vocab.ai/hypertts](https://vocab.ai/hypertts). Chinese Support V4 says it "works with Anki for desktop, not mobile" `[VERIFIED-DOCS]` [Chinese Support V4](https://shigeyukey.github.io/shige-addons-wiki/chinese-support-v4.html).
- **Audio formats on iOS:**
  - mpvacious docs: AnkiMobile has trouble with Opus; set `opus_container` to `m4a` or `webm`, or use mp3. Lockdown Mode disables Opus and AVIF `[VERIFIED-DOCS]` [mpvacious](https://github.com/Ajatt-Tools/mpvacious).
  - asbplayer docs: "Re-encode audio as mp3"; "In general there's no reason to turn this setting off, especially for users who want to review their cards on iOS" `[VERIFIED-DOCS]` [asbplayer settings](https://docs.asbplayer.dev/docs/reference/settings).

### Inferences — recommended FSRS configuration for this learner `[UNVERIFIED: my synthesis of the docs above]`
- **Presets:** three presets (ZH-HSK, JA-mined, EN-mined), because the manual suggests separate presets for decks of very different difficulty. Turn FSRS on globally. Optimise each preset monthly once it has a few hundred reviews, with "Check health when optimizing" on.
- **Desired retention:**
  - Mandarin core: 0.90.
  - Japanese and English mined decks: start at 0.90; if daily load exceeds your time budget, drop to 0.85–0.88 after checking Help Me Decide.
  - Do not go above 0.95.
- **Learning steps:** `10m 30m` or a single `15m`; relearning `10m`. Keep them minimal.
- **Rating:** press Again when you forget or cannot produce the item. Hard means "recalled with effort," not failure. This matters most for production cards, where a partially correct answer is tempting to grade Hard.
- **Daily limits:** new cards/day across all three languages of roughly 20–30 total (e.g., ZH 10, JA 10, EN 5–10). The manual's 20 new → about 200 reviews/day rule implies about 250–300 reviews/day at 25–30 new.
- **Scheduling helpers:** Easy Days set to "Reduced" on your busiest weekdays. Load balancer is built in (no toggle needed in recent versions `[UNVERIFIED]`).
- **Burying:** bury new, review and interday siblings on, so the listening card and production card of the same note do not appear on the same day.
- **Keep clients current:** desktop ≥ 26.05, AnkiDroid ≥ 2.25, AnkiMobile ≥ 26.x, so FSRS-6 parameters and sibling dispersal behave the same everywhere.

### Gaps
- I could not open the official AnkiMobile changelog page (docs.ankimobile.net/changes.html returned 404). AnkiMobile version facts come from the forum announcement.
- AnkiDroid release pages list no backend version string. The "26.05 features" mapping comes from the changelog post.
- I did not find whether 26.11 (final) changes FSRS defaults.

---

## 3. Note types, templates and add-ons per language (with mobile compatibility)

### Takeaway
- **Japanese:** use **Lapis** (lightweight; has audio/sentence/click card modes) filled by Yomitan, plus AJT Japanese for furigana and pitch stored in fields. Everything renders on mobile because it lives in fields.
- **Mandarin:** Chinese Support Redux is archived. Use **Chinese Support 3** (Gustaf-C, beta, Anki 23.10+) or **Chinese Support V4** (Shige, fixed for Anki 25.07+) on desktop to fill pinyin, tone colours, audio and Tatoeba examples into fields, then review anywhere with an audio-first template.
- **Generic:** built-in Cloze with type-in, `{{hint}}`, `{{tts}}` fallback, and recording your own voice.

### Cited Findings

**Japanese**
- **Lapis** (GPL-3.0) `[VERIFIED-DOCS]` [Lapis GitHub](https://github.com/donkuri/lapis):
  - **Fields:** Expression, ExpressionFurigana, ExpressionReading, ExpressionAudio, PitchPosition, PitchCategories, Sentence, SentenceFurigana, SentenceAudio, MainDefinition, Glossary, Hint, Picture, Frequency, FreqSort, MiscInfo.
  - **Card modes (one `Is...Card` flag per note):** default vocab card, `IsWordAndSentenceCard`, `IsClickCard` (click the word to reveal the sentence), `IsSentenceCard`, and `IsAudioCard` (plays sentence audio with the word hidden; falls back to word audio).
  - **Compatibility:** needs Anki 23.10+. Uses no custom handlebars, so it works with any Yomitan dictionary.
  - **Mobile:** designed to avoid the heavy JS that lagged on mobile with JPMN (jp-mining-note). The page mentions mobile font and position settings but does not name AnkiDroid or AnkiMobile explicitly.
  - **Optional companions:** AJT Japanese, NHK accent dictionary, backfill-anki-yomitan.
- **AJT Japanese** (AnkiWeb code 1344485230) `[VERIFIED-DOCS]` [AJT Japanese GitHub](https://github.com/Ajatt-Tools/Japanese):
  - Furigana via MeCab on field blur, in bulk from the Browser, and for notes added through AnkiConnect.
  - Pitch accent lookup from NHK and Kanjium data (~337,552 entries), written into fields.
  - The page does not state the supported Anki version or mobile behaviour. Output is stored in fields, so it should sync to mobile `[UNVERIFIED inference]`.
- **jp-mining-note (JPMN):** the Lapis README describes it as a JS-heavy predecessor that lagged on mobile `[COMMUNITY via Lapis README]`. I did not verify its 2026 maintenance status.

**Mandarin**
- **Chinese Support Redux:** archived and read-only since 30 Nov 2023 `[VERIFIED-DOCS]` ([search summary of the jdlorimer repo](https://github.com/jdlorimer/chinese-support-redux)). An undated forum comment calls it broken `[COMMUNITY]`.
- **Chinese Support 3** (maintainer Gustaf-C; "still in beta"; "Anki 23.10-compatible"; v0.18.0 fixed a crash on 25.02+) `[VERIFIED-DOCS]` [Chinese Support 3 README](https://github.com/Gustaf-C/anki-chinese-support-3):
  - Fills translation (EN, DE or FR), Pinyin or Jyutping, Mandarin audio (Google or Baidu), traditional and simplified forms, Bopomofo, rubies, frequency, and Tatoeba example pairs.
  - Converts numbered pinyin to tone marks.
  - Tone colours apply to characters, romanisation and Bopomofo, and require template CSS.
  - Provides "Chinese (Basic)" and "Chinese (Advanced)" note types.
- **Chinese Support V4** (AnkiWeb 1240761427) `[VERIFIED-DOCS]` [Shige wiki](https://shigeyukey.github.io/shige-addons-wiki/chinese-support-v4.html): "a fixed version for Anki25.07+" of CS3, with the same features, including Tatoeba sentences in a "Usage"/"Examples" field. It "works with Anki for desktop, not mobile" (the add-on itself; the generated fields still sync).
- **Tone colour plus number or contour:** see Godfroid et al. 2017 in Section 1. Showing tone marks or numbers *and* colour is better supported than colour alone `[VERIFIED-DOCS]`.

**Generic, built into Anki** `[VERIFIED-DOCS]` [manual](https://docs.ankiweb.net/templates/fields.html)
- `{{cloze:Text}}` with `{{type:cloze:Text}}`, and the cloze-only TTS form `{{tts en_US:cloze-only:Text}}`.
- `{{hint:Field}}` for tap-to-reveal hints, e.g., pinyin or a translation.
- Replaying front audio on the back means including the audio field explicitly on the back.
- AnkiDroid 2.25 templates can record audio `[VERIFIED-DOCS]` (changelog above).
- Desktop "Record own voice" / "Replay own voice" shortcuts exist `[UNVERIFIED: from prior knowledge of the manual; not fetched this session]`.
- **Slowed audio:** `{{tts ... speed=0.8}}` works only for TTS and only on some platforms. I found no official per-clip playback-speed control in the 2026 release notes `[VERIFIED-DOCS: absence in notes]`. Practical workaround: generate a second, slower TTS file (edge-tts `--rate=-20%`, or a HyperTTS voice setting) into a `SentenceAudioSlow` field `[LOCAL-TEST: edge-tts rate option works]`.

### Inferences — template patterns `[UNVERIFIED: illustrative, not tested in Anki]`
- **Mandarin audio-first card** (one card type on the CS3 or a custom note):
  - **Front:** `{{SentenceAudio}}`. If the audio field is empty, fall back to `[anki:tts lang=zh_CN]{{Sentence}}[/anki:tts]`, with the text itself hidden. Optionally add `{{hint:Pinyin}}`.
  - **Back:** coloured Hanzi, pinyin with tone marks, meaning, `{{SentenceAudio}}` again, and `{{WordAudio}}`.
  - **Second card ("produce"):** meaning or English/Vietnamese prompt on the front, then say it aloud and compare with the audio on the back. Generate it only when a `Produce` field is non-empty, using a `{{#Produce}}...{{/Produce}}` conditional front, so you choose which notes get production cards.
- **Japanese and English mined sentence (Lapis or similar):**
  - Default to `IsAudioCard` for the listening-first workflow.
  - Use `IsClickCard` or `IsSentenceCard` when the sentence is long.
  - For production, add your own card type to a cloned Lapis note: prompt = `Hint` or English gloss plus the screenshot; answer = sentence with audio. Lapis's selector model is one card type per note, so a separate production card needs a modified note type.
- **Atomic cloze:** `{{c1::to keep someone in the loop}}` only. Put the rest of the sentence in plain text and the full audio on the back. Avoid c1/c2/c3 on one long sentence; each cloze becomes a separate card, which multiplies workload.

### Gaps
- Exact 2026 versions and last-update dates of Lapis, AJT Japanese and Chinese Support 3/V4 were not shown on the pages fetched.
- I did not verify whether CS3/V4 tone-colour spans render correctly on AnkiMobile; it depends on the template CSS.

---

## 4. TTS and native-audio sources, with quality notes

### Takeaway
- **Zero-cost route:**
  - Free HyperTTS services (GoogleTranslate, NaverPapago for Japanese and English, Windows/macOS voices).
  - edge-tts outside Anki (works as of 2026-11-13).
  - Built-in `{{tts}}` as a fallback.
- **Quality-and-control route:** Azure neural voices via HyperTTS with your own key (0.5M characters/month free tier per multiple secondary sources). Only Azure, among the options here, lets you fix readings with SSML phonemes.
- **QA is mandatory** for Mandarin polyphones and sandhi and for Japanese readings and pitch.
- **Native audio for Japanese and English mostly means mining your own media** (Section 5B). Tatoeba native audio is plentiful for English but scarce for Japanese and Mandarin.

### Cited Findings

**HyperTTS**
- **Licence and free services:** free add-on, GPL `[VERIFIED-DOCS]` [vocab.ai/hypertts](https://vocab.ai/hypertts). Free services `[VERIFIED-DOCS]` [vocab.ai free services](https://www.vocab.ai/tips/free-services):
  - GoogleTranslate.
  - NaverPapago (Korean, Japanese, Thai, English, Spanish).
  - Youdao (English UK/US).
  - Dictionary sources (Oxford, Cambridge, …).
  - Local Windows, macOS and ESpeakNg engines.
  - After a Pro trial you must "Remove API Key" before enabling the free services.
- **Premium services:** Collins, Forvo, Google Cloud TTS, Microsoft Azure, IBM Watson, Naver, Amazon, OpenAI and ElevenLabs ("20+ services," "1000's of voices") `[VERIFIED-DOCS/MARKETING]`. Gemini TTS was added in v3.1.0 (19 Apr 2026), models `gemini-3.1-flash-tts-preview` etc. Batch requests retry up to 3 times `[VERIFIED-DOCS]` [Gemini TTS update](https://www.vocab.ai/updates/gemini-tts).
- **Batch mode:** audio for a whole deck or a selection, presets per note type and deck, preview, text processing `[VERIFIED-DOCS]` [vocab.ai/hypertts](https://vocab.ai/hypertts).
- **Price:** "plans start at $5/month for 250K characters," described as enough for about 3,000–6,000 notes/month. The trial lasts one week with 50,000 characters `[MARKETING]` [vocab.ai signup](https://www.vocab.ai/signup); [character credit tip](https://www.vocab.ai/tips/fix-insufficient-character-credit-error); [trial](https://www.vocab.ai/trial).
- **Community services:** HyperTTS supports community-provided service extensions and custom or self-hosted services, per forum and vocab.ai pages. Whether an edge-tts extension exists was not verified `[UNVERIFIED]` [extensions page](https://www.vocab.ai/tips/hypertts-extensions-community-services); [forum](https://forums.ankiweb.net/t/hypertts-and-custom-services-self-hosted-or-cloud-ai-tts-models/69213).
- **AwesomeTTS:** HyperTTS was announced as its "spiritual successor" `[COMMUNITY]` [forum](https://forums.ankiweb.net/t/hypertts-spirtual-successor-to-awesometts/17143). I did not verify AwesomeTTS's 2026 status. A 2026 blog claims to cover it, but that is not authoritative `[UNVERIFIED]`.

**edge-tts** `[VERIFIED-DOCS]` [GitHub rany2/edge-tts](https://github.com/rany2/edge-tts)
- Unofficial Python module and CLI for Microsoft Edge's online TTS.
- Options: `--voice`, `--rate=-50%`, `--pitch=-50Hz`, `--volume`, `--write-media`, `--write-subtitles`.
- "Custom SSML support was removed"; only a single voice and prosody tag are allowed.
- The repo contains a GPL-3.0 licence file.
- **Local test on 2026-11-13** `[LOCAL-TEST]`:
  - `pip install edge-tts` in an isolated venv installed **v7.3.1**.
  - `--list-voices` succeeded.
  - zh-CN voices: Xiaoxiao, Xiaoyi, Yunjian, Yunxi, Yunxia, Yunyang, plus the dialect voices liaoning-Xiaobei and shaanxi-Xiaoni.
  - ja-JP voices: only Keita and Nanami.
  - en-GB: Libby, Maisie, Ryan, Sonia, Thomas. en-US: about 22 voices, including Multilingual ones.
  - Generated three test MP3s: zh "我们一起去银行，行不行？" (polyphone 行 háng/xíng), ja "橋の端で箸を落としました。" at `--rate=-20%` (pitch-accent minimal set), and en.
  - I could not listen to them, so **pronunciation correctness is untested**.
  - Files: `C:\Users\trinh-v\AppData\Local\Temp\claude\ad1c1fd31c67307a\43f64388-07fc-4045-ac80-4a54f3550946\scratchpad\scripts\card-design\out\` (zh_test.mp3, ja_test.mp3, en_test.mp3); voice list in `...\card-design\voices.txt`.
- **Terms of use:** edge-tts uses an undocumented Microsoft endpoint, so its availability and terms are a grey area. It could break without notice `[UNVERIFIED]`.

**Cloud pricing (unstable; verify on the live pages)**
- **Azure F0:** 0.5M neural TTS characters per month free (Microsoft Learn Q&A and other sources) `[COMMUNITY]` [MS Learn Q&A](https://learn.microsoft.com/en-us/answers/questions/1654938/text-to-speech-s0-standard-tier-0-5-million-charac). Paid neural is about $15 or $16 per 1M characters per secondary aggregators. The live Azure page did not render a price `[UNVERIFIED]` [Azure pricing page](https://azure.microsoft.com/en-us/pricing/details/speech/); [costbench](https://costbench.com/software/ai-voice-tools/microsoft-speech/).
- **Google Cloud TTS:** the pricing page could not be read this session (content truncated) — **gap** [Google pricing](https://cloud.google.com/text-to-speech/pricing).

**Repairing readings with Azure SSML** `[VERIFIED-DOCS]` [Azure phonetic sets](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-ssml-phonetic-sets)
- **zh-CN:** `alphabet="sapi"` (not `pinyin`), pinyin syllables with tone numbers 1–5, e.g., `<phoneme alphabet="sapi" ph="ni 3 hao 3">你好</phoneme>`. Neutral tone = 5; erhua is a separate `r`, e.g., `yi 2 hui r 4`.
- **ja-JP:** a kana-based phone set; `sapi` uses katakana with accent marks, e.g., `<phoneme alphabet="sapi" ph="ゴ'ウセ">合成</phoneme>`. IPA is also possible. The page does not fully define the accent symbols.
- Whether HyperTTS passes raw SSML through to Azure was **not verified** `[UNVERIFIED]`.

**Quality evidence: Mandarin**
- A probe of Tacotron-2 Mandarin TTS found surface tonal coarticulation handled well, but **Tone-3 sandhi applied inconsistently on novel sentences**. Errors were concentrated in long, syntactically complex input and trisyllabic words, and mostly came from tone changes at the wrong syntactic boundary `[VERIFIED-DOCS: older (2019) model generation]` [arXiv 1912.10915](https://arxiv.org/pdf/1912.10915).
- Polyphone disambiguation depends on part-of-speech tagging; inaccurate tagging produces wrong readings `[VERIFIED-DOCS]` [arXiv 1911.04111](https://ar5iv.arxiv.org/html/1911.04111).
- A 2026 evaluation framework (TTS-PRISM) still lists polyphone failures and tone-sandhi errors as diagnostic categories `[VERIFIED-DOCS]` [arXiv 2604.22225](https://arxiv.org/html/2604.22225).
- A vendor blog says modern models handle most sandhi but are inconsistent on chains of three or more third tones `[MARKETING]` [okmiku blog](https://okmiku.com/blog/mandarin-tts-tones-practical-guide).

**Quality evidence: Japanese**
- A NICT ICASSP 2025 preprint notes that a katakana reading is unambiguous but carries no pitch-accent information, and proposes accent labels as input `[VERIFIED-DOCS]` [NICT preprint](https://ast-astrec.nict.go.jp/release/preprints/preprint_icassp_2025_ogura.pdf).
- UtterTune (2025) says errors in end-to-end models with implicit G2P and accent estimation are hard to fix by hand `[VERIFIED-DOCS]` [arXiv 2508.09767](https://arxiv.org/html/2508.09767v1).
- A 2026 paper builds a *pitch-accent-focused* quality-assessment model trained on synthetic speech with accent errors, which shows accent errors remain an active problem `[VERIFIED-DOCS: title-level]` [HF papers 2606.20137](https://huggingface.co/papers/2606.20137.md).

**Quality evidence: English**
- I found no specific 2026 evaluation of en-US/en-GB neural prosody for learner material. General experience is that English neural voices are the most mature of the three `[UNVERIFIED]`.

**Native-audio sources**
- **Tatoeba** (stats page fetched 2026-11-13) `[VERIFIED-DOCS]` [Tatoeba stats](https://tatoeba.org/en/stats/sentences_by_language); [Tatoeba terms](https://tatoeba.org/en/terms_of_use):

  | Language | Sentences | With audio |
  |---|---|---|
  | English (eng) | 2,049,506 | 850,274 |
  | Japanese (jpn) | 249,264 | 6,332 |
  | Mandarin (cmn) | 89,403 | 5,826 |
  | Vietnamese (vie) | 33,343 | (not in the audio list) |
  | Total (all languages) | 13,670,712 | — |

  Licensing: sentence text is CC BY 2.0 FR. Audio licences vary per contributor; BY is the minimum, and some audio has non-commercial or no-derivatives conditions.
- **Immersion Kit:** the homepage claims a "500k Anime sentence database" with audio and pictures, plus "Read Aloud Stories" `[MARKETING]` [immersionkit.com](https://www.immersionkit.com/). Its Patreon says examples can be saved or downloaded as Anki cards `[MARKETING]` [Patreon](https://www.patreon.com/immersionkit/about?l=ru-RU). Tofugu's database entry describes 400k+ sentences with screenshot and audio `[COMMUNITY]` [Tofugu](https://tofugu.com/japanese-learning-resources-database/immersion-kit). Japanese only; mostly anime.
- **Language Reactor, asbplayer, mpvacious, subs2srs, Migaku:** see Section 5B.
- **YouGlish** (no export), **Forvo** (word-level), **Glossika** (no export): not verified this session `[UNVERIFIED]`. HyperTTS lists Forvo as a service, which is word pronunciation `[VERIFIED-DOCS]`.

### Inferences
- **Cost for this learner `[UNVERIFIED estimate]`:**
  - 3,000 zh + 3,000 ja sentences at about 25 characters each ≈ 150k characters.
  - 3,000 English sentences at about 80 characters ≈ 240k characters.
  - In total that fits inside one month of Azure F0 (0.5M) or two months of the $5 HyperTTS plan. Effective cost: $0–10.
- **Best quality-to-effort split per language `[UNVERIFIED]`:**
  - **Mandarin:** Azure, or edge-tts (same Microsoft voice family) for bulk; Azure SSML to fix flagged polyphones.
  - **Japanese:** native mined audio first. TTS only for sentences without audio, with pitch QA against the AJT pitch field or OJAD/NHK.
  - **English:** TTS is the most acceptable, but mined native audio is preferred for C2 prosody and register.
- **Mandarin voices:** use 2–3 different voices across the deck to mimic Wang et al.'s high-variability training.

### Gaps
- No published error rates for Azure, Google, edge, OpenAI, ElevenLabs or Gemini voices on 多音字, sandhi or Japanese pitch.
- Google Cloud TTS 2026 price table and the official Azure 2026 neural rate were not obtained.
- I did not confirm whether HyperTTS supports edge-tts or SSML passthrough.

---

## 5. Minimal extension workflows

### 5A. Adding sentence audio and context to an existing deck (no rebuilding)

#### Takeaway
- Use one or both of two paths to add audio to an existing deck:
  - **(1) HyperTTS batch inside Anki desktop:** about 30–60 minutes of setup plus generation time, $0–5.
  - **(2) edge-tts or Azure script plus AnkiConnect/CSV re-import:** free, more control, more technical.
- Then run QA on flagged sentences.
- Context comes from the sentences you already have, plus optional Tatoeba examples (CS3/V4 can fill them for Mandarin).
- Add production cards only to a tagged subset.

#### Cited Findings
- HyperTTS batch-generates audio for a deck or selection, with presets per note type and deck, preview and text processing. Generated audio plays on AnkiMobile and AnkiDroid `[VERIFIED-DOCS]` [vocab.ai/hypertts](https://vocab.ai/hypertts); [HyperTTS adding audio](https://vocab.ai/tips/hypertts-adding-audio); [getting started](https://vocab.ai/tutorials/hypertts-getting-started).
- edge-tts CLI options, including `--rate` for a slow version `[VERIFIED-DOCS]` [edge-tts](https://github.com/rany2/edge-tts); `[LOCAL-TEST]` working on 2026-11-13.
- Azure SSML phoneme syntax for repairs `[VERIFIED-DOCS]` [Azure phonetic sets](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-ssml-phonetic-sets).
- Chinese Support 3/V4 can fill Tatoeba example pairs into a "Usage"/"Examples" field `[VERIFIED-DOCS]` [CS3](https://github.com/Gustaf-C/anki-chinese-support-3); [V4](https://shigeyukey.github.io/shige-addons-wiki/chinese-support-v4.html).
- Media references must live in fields (`[sound:file.mp3]`), not be built in templates from field values `[VERIFIED-DOCS]` [manual](https://docs.ankiweb.net/templates/fields.html).

#### Inferences — recommended steps `[UNVERIFIED: procedure synthesised from the docs; exact menu labels may differ]`

**Path 1: HyperTTS (recommended default)**
1. **Back up.** File → Create Backup / export `.colpkg`.
2. **Add fields.** In Manage Note Types, add `SentenceAudio` (and optionally `SentenceAudioSlow`, `Produce`) to the existing note type.
3. **Install HyperTTS.** In Services Configuration, either enable the free services (Windows voices, GoogleTranslate, NaverPapago for ja/en) or paste an Azure key. A free F0 Speech resource is created in the Azure portal.
4. **Configure the batch.** In the Browser, select the notes. Choose HyperTTS → Add Audio (Collection/batch), source = `Sentence`, target = `SentenceAudio`.
   - Text processing: strip HTML/furigana brackets, e.g., a regex that removes `[...]` ruby readings for Japanese and pinyin for Mandarin, so the TTS reads only the sentence.
5. **Preview** 10–20 sentences, choose the voice, save as a preset per deck, then run. HyperTTS retries transient errors.
6. **Template edit.** Put `{{SentenceAudio}}` on the front of a new "Listening" card type, and on the back of the existing card.
7. **Sync,** then spot-check on the phone (audio plays offline because the mp3 files are in the media folder).

**Path 2: edge-tts or Azure script (free, scriptable)**
1. Export notes as plain text with the note ID or GUID, or use AnkiConnect `findNotes`/`notesInfo`.
2. For each note, run `edge-tts --voice zh-CN-XiaoxiaoNeural --text "<sentence>" --write-media zh_<noteid>.mp3`. Optionally make a slow version with `--rate=-25%`. Rotate voices across notes.
3. Push the result back with AnkiConnect `storeMediaFile` + `updateNoteFields`, setting `SentenceAudio = [sound:zh_<noteid>.mp3]`. Or copy the files into `collection.media` and re-import a CSV that updates existing notes by GUID.
4. AnkiConnect method names are from prior knowledge and were not re-checked `[UNVERIFIED]`.

**QA protocol (tone, polyphone, pitch) `[UNVERIFIED: recommended procedure]`**
- **Mandarin:**
  - Regex-flag sentences that contain high-risk polyphones: 行 长 了 得 还 重 觉 便 为 地 着 都 和 乐 数 好 少 种 差 只 调 发 干 处 当 看 教 空 假 背 薄 倒.
  - Also flag runs of two or more third-tone syllables and 一/不.
  - Listen to 100% of flagged sentences and 5–10% of the rest.
  - Fix with Azure SSML `<phoneme alphabet="sapi" ph="...">`, or replace the character with an unambiguous homophone *in the TTS input only*, keeping the display text unchanged. HyperTTS's text-processing rules are one place to do this.
  - Note that pinyin auto-filled by CS3 can also be wrong for polyphones, so treat a mismatch between pinyin and audio as a flag.
- **Japanese:**
  - Flag numerals and counters, names, 今日/一日/上手/方/生/後/日本 and other kanji with several readings, and sentences without furigana.
  - Compare the target word's pitch in the audio with AJT's NHK/Kanjium pitch field.
  - Fix with Azure `sapi` katakana and accent, or by writing the word in kana in the TTS input.
- **English:** check stress on noun/verb pairs (record, present), abbreviations, numbers, and dates.
- **Time budget:** about 1–2 s per sentence of generation time for cloud TTS; listening to 300 flagged sentences takes about 30–45 minutes `[UNVERIFIED estimate]`.

**Context and production without rebuilding `[UNVERIFIED: recommended]`**
- Add a `Produce` field. Fill it (e.g., with an English or Vietnamese cue) only for the 10–20% of notes you want in active use. A conditional card type then generates production cards only for those notes.

#### Gaps
- Exact HyperTTS 2026 menu names and its batch throughput/rate limits per service were not documented on the pages fetched.
- I did not test end-to-end AnkiConnect writes (no Anki instance in this environment).

### 5B. Sentence mining from authentic native media (priority route for Japanese and English)

#### Takeaway
- **Core stack:** asbplayer (browser: Netflix, YouTube and most streaming sites, plus local video files) or mpvacious (mpv, local files), with Yomitan for one-click card creation and AnkiConnect on Anki desktop.
- **What a card gets:** sentence text, a sentence-audio clip, a screenshot, source and URL, written into your note type (e.g., Lapis). The cards then sync as ordinary notes to AnkiDroid and AnkiMobile.
- **Settings that matter:**
  - Make asbplayer re-encode audio as mp3 for iOS.
  - In mpvacious, avoid raw Opus or use an m4a/webm container.
- **Card length:** one subtitle line, a padded short clip, cloze or highlight a single chunk, and an audio-first front.
- **Language Reactor:** easiest for Netflix, but Pro-only export, and YouTube lines get a robot voice per its forum.
- **Migaku:** a paid, closed ecosystem; community reports say its own SRS cards can't be exported to Anki afterwards.
- **subs2srs:** legacy batch tool that turns whole episodes into thousands of cards, which this learner does not want.
- Mandarin stays on the HSK-structured deck plus the audio pipeline (5A).

#### Cited Findings

**asbplayer** (free; AGPL-3.0, some parts MIT) `[VERIFIED-DOCS]` [GitHub](https://github.com/killergerbah/asbplayer); [mining in depth](https://docs.asbplayer.dev/docs/guides/mining-in-depth); [settings](https://docs.asbplayer.dev/docs/reference/settings); [one-click mining](https://docs.asbplayer.dev/docs/guides/one-click-mining); [common issues](https://docs.asbplayer.dev/docs/common-issues)
- **Sources:**
  - Subtitles are auto-detected on Netflix and YouTube.
  - A generic detection works on "about 85%" of other streaming services.
  - You can drag your own subtitle files onto streaming video or onto the asbplayer website for local files.
  - A Firefox-for-Android build is mentioned.
- **Card fields:**
  - Sentence ("All subtitles at the mined timestamp").
  - Audio, recorded from the video.
  - Image (screenshot).
  - Source (file or video name and timestamp), URL, Definition, Word, Subtitle Track 1–3, custom fields, and tags.
- **Audio settings:**
  - "Audio padding start/end" (ms).
  - "Re-encode audio as mp3": "In general there's no reason to turn this setting off, especially for users who want to review their cards on iOS."
  - On streaming sites, audio is recorded in real time and "Re-record" captures a new range. For local files the clip updates automatically when the range slider changes.
- **Image settings:** max width/height, trim black bars, screenshot delay, and "Animated WebP" for streaming in the extension (not available in Firefox; the tab must stay visible).
- **Workflow:**
  - `Ctrl+Shift+X` opens the export dialog, which has a time-range slider. The Sentence field follows the range unless you have edited it.
  - The Export, Update last card and Open in Anki buttons are in the dialog.
  - Dialog-less flow: create the card with Yomitan, then press `Ctrl+Shift+U` to "update last card" with asbplayer's sentence, audio and screenshot. `Ctrl+Shift+V` takes a manual screenshot.
  - The "Always use subtitle text for sentence field" option is useful with Yomitan.
  - Most setups need "two or three" user inputs.
  - Keep Anki's Browser closed while using "update last card," which is a known AnkiConnect issue.

**mpvacious** (mpv user script; mpv ≥ 0.41.0; AnkiConnect) `[VERIFIED-DOCS]` [mpvacious](https://github.com/Ajatt-Tools/mpvacious)
- **Keys:**
  - `Ctrl+n` exports the visible subtitle as a card ("works best when subtitles are well-timed and the sentence fits in one line").
  - The advanced menu `a` sets start and end times for multi-line sentences.
  - `Ctrl+m` appends media to the last note; `Ctrl+Shift+m` overwrites it.
- **Fields:** sentence, audio, image, a secondary-subtitle field (e.g., an English or Vietnamese translation track), and Forvo pronunciations.
- **Formats:** Opus is the recommended audio format; mp3 is the option for older mobile devices. AnkiMobile has trouble with Opus, so set `opus_container` to `m4a` or `webm`. AVIF/WebP images are recommended, with jpg for older devices. Lockdown Mode disables Opus and AVIF.

**Language Reactor** (Netflix, YouTube and others)
- **Export:**
  - Formats: Print, Excel, Anki, CSV, JSON.
  - Tick "Include Media" to get audio and images in a zip.
  - Import with the template from AnkiWeb (shared ID 1580143799, "LLNTemplate," tab separator).
  - Copy the `media` folder into `collection.media`.
  - Disable "Only new items since last export" if items are missing.
  - `[COMMUNITY: official-forum guide, Apr 2024, replies to Sep 2025]` [How to Export](https://forum.languagelearningwithnetflix.com/t/how-to-export-guide/19596).
  - The official help page describes "Include media" bundling CSV plus image and audio in a zip. Saved items come as phrases, words with context, or words without context; on Anki cards the context shows with the target word removed `[VERIFIED-DOCS via search snippet]` [LR help: export](https://languagereactor.com/help/export).
- **Audio caveat:** a moderator replied (13 Jul 2025) "Only the lines from Netflix will have the original audio," while YouTube lines use a "Roboter voice" `[COMMUNITY]` [forum](https://forum.languagelearningwithnetflix.com/t/language-reactor-pro-features/31894).
- **Price and Pro requirement:** Pro is about $4.99/month per Trancy (a competitor), and stork.ai says Anki export is Pro-only. The official pricing page did not render `[UNVERIFIED]` [Trancy comparison](https://www.trancy.org/blog/language-reactor-pro-vs-trancy-2026-which-is-better-for-language-learners-31f9d225200580a48aa8c5f28602a2b3); [stork.ai](https://www.stork.ai/en/language-reactor).

**Immersion Kit:** Japanese anime sentences with audio and screenshots, downloadable as Anki cards. An API is used by third-party tools such as the "JPDB Immersion Kit Examples" extension `[MARKETING/COMMUNITY]` [immersionkit.com](https://www.immersionkit.com/); [Chrome extension](https://chromewebstore.google.com/detail/jpdb-immersion-kit-exampl/knedmjcggobmokkephmaggbgakjjckbf). Exact export format not verified.

**subs2srs and alternatives**
- subs2srs (SourceForge) creates import files for Anki from video plus subtitles, using ffmpeg `[VERIFIED-DOCS]` [subs2srs](https://subs2srs.sourceforge.net/).
- Alternatives `[VERIFIED-DOCS: project pages via search]` [GitHub topic subs2srs](https://github.com/topics/subs2srs); [movies2anki](https://relatedrepos.com/gh/kelciour/movies2anki); [subs2cia](https://relatedrepos.com/gh/dxing97/subs2cia); [yt2srs](https://github.com/kamui-fin/yt2srs):
  - **movies2anki:** Anki add-on with video, picture and audio-only templates.
  - **substudy:** CLI tool.
  - **yt2srs:** YouTube; can merge subtitle fragments into sentences. Its authors note auto-generated subtitles give poor results.
  - **subs2cia:** condensed audio, last updated about June 2025.

**Migaku**
- The official pricing page did not render. Third-party prices conflict: $9.99/month or $79.99/year with a 14-day trial; one site says $99/month (likely wrong) `[UNVERIFIED]` [itechguides](https://www.itechguides.com/products/migaku/).
- The Migaku homepage lists Japanese, Mandarin, English, Vietnamese and others, plus a browser extension, iOS/Android apps and Migaku Memory `[VERIFIED-DOCS]` [migaku.com](https://migaku.com/pricing).
- Community posts say you can send cards to Anki *instead of* Migaku Memory, but cards made in Migaku Memory can't be exported to Anki later `[COMMUNITY]` [Migaku community](https://migaku.com/community).

**Time per card:** I found no published timing data `[gap]`. The docs only say "two or three" inputs per card for dialog-less mining `[VERIFIED-DOCS]`. A Reddit user describes the sequence: hold a key for the Yomitan popup, click +, then Ctrl+Shift+U `[COMMUNITY]` [r/languagelearning](https://redlib.hbubli.cc/r/languagelearning/comments/1l0ipdz/sentence_mining_useful_or_not/mvdt5fl).

**Newer automation tools:** SubMiner auto-fills sentence, audio, image and translation into new cards `[COMMUNITY/docs]` [SubMiner](https://subminer-docs.pages.dev/anki-integration). Anki Miner (last pushed May 2026) does automated Japanese mining from local subtitles `[VERIFIED-DOCS: project page]` [Anki Miner](https://pypi.org/project/anki-miner/2.4.3/).

**Vietnamese-language guide:** a community asbplayer mining guide for Netflix and YouTube also exists in Vietnamese `[COMMUNITY]` [Notion guide](https://soyuz18.notion.site/Sentence-mining-from-Netflix-and-YouTube-with-asbplayer-83a03590cd8349ba81ca10340645b565).

#### Inferences — recommended low-effort mining workflow `[UNVERIFIED: synthesis; timings are my estimates]`

**One-time setup (about 1–2 hours)**
1. Anki desktop with AnkiConnect, plus the Lapis note type (Japanese) or a simple English mining note with Sentence, SentenceAudio, Picture, Target, Definition, Hint/Gloss, Source and Produce fields.
2. Yomitan with Japanese dictionaries (JMdict and a monolingual dictionary for N1+, pitch and frequency) and English dictionaries, mapped to the note fields. Yomitan's English support is not verified this session `[UNVERIFIED]`.
3. **asbplayer extension:**
   - Map the Sentence, Audio, Image, Source and URL fields.
   - Turn "Re-encode audio as mp3" **ON**.
   - Audio padding about 100–250 ms start and 300–500 ms end (my suggestion).
   - Max image width about 640 px, to keep media small for phone sync.
   - Use the dialog-less "update last card" (Yomitan postMineAction = 2).
4. **mpvacious** for local video and downloaded podcasts or talks: set audio to mp3, or Opus in an m4a container, and images to jpg/webp, for AnkiMobile safety.
5. **Podcasts, talks, interviews and news without subtitles:** generate subtitles first with a local speech-to-text model, then load the media and subtitles into asbplayer (local file) or mpv. ASR timing and errors need a glance `[UNVERIFIED approach]`.
6. **Workplace talk:** only mine recordings you are permitted to keep (meetings require consent). An alternative is to write down phrases heard at work and generate TTS or find native examples later.

**Per-card loop (estimates `[UNVERIFIED]`)**
- **Dialog-less** (Yomitan click → Ctrl+Shift+U): about 10–30 s per card.
- **With the export dialog** (adjust the range slider, trim to one clause, write a short Hint/Gloss): about 45–90 s.
- **Production cards:** writing a good cue for the `Produce` field adds about 30–60 s, so do it only for selected cards.
- **Pacing:** batch decisions while watching, mining at most 5–10 cards per episode, keeping each session's mining to about 10–15 minutes.

**What appears on the phone**
- **asbplayer, mpvacious, Language Reactor and Immersion Kit** all produce ordinary notes, with `[sound:...]` audio and `<img>` in fields. These play on AnkiDroid and AnkiMobile if the formats are mobile-safe:
  - mp3 audio is safest.
  - Opus is problematic on iOS.
  - AVIF fails under Lockdown Mode.
  - Animated WebP support on mobile is **unverified**.
- **Lapis** card modes render on mobile because they are template HTML/CSS, not add-on code. The furigana and pitch fields come from AJT or Yomitan at creation time.

**Keeping cards short (long-sentence workflow)**
- **Clip length:**
  - Prefer one subtitle line, about 2–8 s of audio including padding.
  - If the line is longer than about 10 s or holds several clauses, use asbplayer's range slider or mpvacious's `a` menu to trim to the clause containing the target.
  - Keep the full line's text on the back (MiscInfo/Source field) if you want context.
- **One target per card:**
  - Highlight or cloze a single chunk: a collocation, set phrase, keigo formula, discourse marker, or idiom.
  - Do not make multiple clozes from one long line, because each becomes a card and a lapse on any piece fails the card.
- **Listening-first front:**
  - Audio (and screenshot) only. Task: understand the line, and catch the target chunk.
  - Back: transcript with the target highlighted, gloss or definition, and the audio again.
  - Lapis `IsAudioCard` does this out of the box. Use `IsClickCard` when the sentence is long and you need the text revealed in parts.
- **Production layer:**
  - For about 10–20% of cards (expressions you want to *say*), a second card shows the situation/gloss and screenshot. You say the line, then compare with the native audio. On AnkiDroid 2.25, you can record yourself inside the template.
  - Grade honestly (Again if you could not produce the chunk).
- **Shadowing reuse:** tag the best 2–8 s clips `shadow`. In a separate daily 10-minute session (Foote & McDonough), run a filtered deck of that tag: listen, shadow 3–5 times, record, and compare.

**Mandarin (beginner):** stay HSK-structured. Use Path 1/2 TTS audio (multiple voices) on HSK sentences, plus Tatoeba cmn audio where available (about 5.8k sentences). Postpone native-media mining until about HSK 4 `[UNVERIFIED recommendation]`.

#### Gaps
- No measured seconds-per-card benchmarks.
- I could not confirm Language Reactor's official 2026 price, or whether export is Pro-only, from an official page.
- Migaku's 2026 price was not verified.
- Immersion Kit's export format and any 2026 non-anime coverage were not confirmed.
- Animated WebP playback on AnkiMobile and AnkiDroid was not verified.
- Yomitan's English-dictionary support and its 2026 version were not checked.

---

## 6. External speaking practice that must complement Anki

### Takeaway
- For C2/beyond-N1 speaking, pair Anki with weekly practice in four forms:
  - **(a)** Repeated-speech fluency tasks: 4/3/2 retelling of the same content, which de Jong & Perfetti found to have lasting effects.
  - **(b)** Shadowing with self-recording, about 4 sessions of at least 10 minutes per week (Foote & McDonough).
  - **(c)** Pushed output with feedback from tutors or colleagues (Swain).
  - **(d)** Meaning-focused output across Nation's strands.
- AI conversation partners can add low-cost volume, but I found no 2026 efficacy studies for them.

### Cited Findings
- de Jong & Perfetti 2011: fluency gains were maintained only when the same speech was repeated at 4, 3 and 2 minutes; the authors interpret this as proceduralisation `[VERIFIED-DOCS, abstract read]` [doi](https://doi.org/10.1111/j.1467-9922.2010.00620.x).
- Foote & McDonough 2017: shadowing with self-recording improved comprehensibility and fluency, but not accentedness `[VERIFIED-DOCS, abstract read]` [doi](https://doi.org/10.1075/jslp.3.1.02foo).
- Hamada 2019: progress from shadowing for listening to shadowing for speaking `[VERIFIED-DOCS, abstract read]` [doi](https://doi.org/10.1177/0033688218771380).
- Nation 2007: four strands, with fluency development and meaning-focused output each about a quarter of learning time `[VERIFIED-DOCS: citation; content from prior knowledge]` [doi](https://doi.org/10.2167/illt039.0).
- Kang et al. 2013: retrieval beats imitation. Shadowing alone is not a substitute for recalling and producing expressions yourself `[VERIFIED-DOCS: title-level]` [doi](https://doi.org/10.3758/s13423-013-0450-z).

### Inferences — weekly routine `[UNVERIFIED: recommendation]`
- **Japanese (N1+ speaking):**
  - 2 × 30–60 min tutor sessions per week (e.g., an italki-style platform) focused on workplace and DX topics: explaining a system, negotiating a schedule, keigo in meetings. Bring the week's `Produce` cards as targets.
  - Daily: 10 min shadowing of mined clips, plus one 4/3/2 retelling of a mined scene or work topic, recorded and compared.
- **English (C2 expressiveness):**
  - Weekly 4/3/2 talks on the same topic.
  - Paraphrase drills: retell a mined talk clip in your own words, then compare with the original phrasing and add the gaps as cloze/production cards.
  - Occasional tutor sessions for feedback on register and precision.
- **Mandarin (beginner):**
  - 2–3 × 30 min tutor sessions per week for tone feedback.
  - Daily minimal-pair and tone listening from audio-first cards.
  - Shadowing of HSK dialogues, starting slow (`--rate=-20%` TTS) and then at normal speed.
- **AI conversation partners:** voice-mode LLM tutors give unlimited pushed-output volume and instant reformulations. Correction quality, especially for Mandarin tones and Japanese pitch, is unverified. Use them for volume, and humans for pronunciation feedback.

### Gaps
- I did not research current tutoring platform prices, or efficacy studies of AI speaking partners for 2025–2026.

---

## Full source list (accessed 2026-11-13)

**Anki / FSRS / mobile**
- Anki releases (26.11b1, 26.09.4, …): https://github.com/ankitects/anki/releases
- Anki 26.09: https://github.com/ankitects/anki/releases/tag/26.09
- Anki 26.05: https://github.com/ankitects/anki/releases/tag/26.05
- Anki 26.08 (mirror): https://newreleases.io/project/github/ankitects/anki/release/26.08
- Anki 25.07 (mirror): https://newreleases.io/project/github/ankitects/anki/release/25.07
- Anki 24.11 (mirror): https://newreleases.io/project/github/ankitects/anki/release/24.11
- Anki 24.10beta1 (mirror): https://newreleases.io/project/github/ankitects/anki/release/24.10beta1
- Anki manual, Deck Options: https://docs.ankiweb.net/deck-options.html
- Anki manual, Field replacements (tts, type, hint, furigana): https://docs.ankiweb.net/templates/fields.html
- FSRS algorithm wiki: https://github.com/open-spaced-repetition/awesome-fsrs/wiki/The-Algorithm
- Help Me Decide simulator bug report: https://forums.ankiweb.net/t/bug-fsrs-desired-retention-simulator-expects-21-parameters-but-decks-support-less-than-that-leading-to-silent-failure/70285
- AnkiDroid releases: https://github.com/ankidroid/Anki-Android/releases
- AnkiDroid 2.25 changelog: https://forums.ankiweb.net/t/ankidroid-2-25-changelog/71237
- AnkiMobile 26.10 announcement: https://forums.ankiweb.net/t/ankimobile-26-10-is-out/74202

**Note types and add-ons**
- Lapis: https://github.com/donkuri/lapis
- AJT Japanese: https://github.com/Ajatt-Tools/Japanese (AnkiWeb 1344485230)
- Chinese Support 3: https://github.com/Gustaf-C/anki-chinese-support-3
- Chinese Support V4: https://shigeyukey.github.io/shige-addons-wiki/chinese-support-v4.html (AnkiWeb 1240761427)
- Chinese Support Redux (archived): https://github.com/jdlorimer/chinese-support-redux

**TTS**
- HyperTTS: https://vocab.ai/hypertts ; free services: https://www.vocab.ai/tips/free-services ; Gemini TTS update: https://www.vocab.ai/updates/gemini-tts ; signup/pricing: https://www.vocab.ai/signup ; trial: https://www.vocab.ai/trial ; character credit: https://www.vocab.ai/tips/fix-insufficient-character-credit-error ; code: https://github.com/Vocab-Apps/anki-hyper-tts
- HyperTTS as AwesomeTTS successor (forum): https://forums.ankiweb.net/t/hypertts-spirtual-successor-to-awesometts/17143
- edge-tts: https://github.com/rany2/edge-tts
- Azure SSML phonetic sets: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-ssml-phonetic-sets
- Azure F0 Q&A: https://learn.microsoft.com/en-us/answers/questions/1654938/text-to-speech-s0-standard-tier-0-5-million-charac ; Azure pricing: https://azure.microsoft.com/en-us/pricing/details/speech/ ; costbench: https://costbench.com/software/ai-voice-tools/microsoft-speech/
- Google TTS pricing (not readable this session): https://cloud.google.com/text-to-speech/pricing
- Mandarin TTS tone probe: https://arxiv.org/pdf/1912.10915 ; Mandarin front-end (polyphones): https://ar5iv.arxiv.org/html/1911.04111 ; TTS-PRISM: https://arxiv.org/html/2604.22225 ; okmiku blog: https://okmiku.com/blog/mandarin-tts-tones-practical-guide
- Japanese accent TTS: https://ast-astrec.nict.go.jp/release/preprints/preprint_icassp_2025_ogura.pdf ; https://arxiv.org/html/2508.09767v1 ; https://huggingface.co/papers/2606.20137.md

**Native audio and mining**
- Tatoeba stats: https://tatoeba.org/en/stats/sentences_by_language ; terms: https://tatoeba.org/en/terms_of_use
- Immersion Kit: https://www.immersionkit.com/ ; Patreon: https://www.patreon.com/immersionkit/about?l=ru-RU ; Tofugu entry: https://tofugu.com/japanese-learning-resources-database/immersion-kit
- asbplayer: https://github.com/killergerbah/asbplayer ; https://docs.asbplayer.dev/docs/guides/mining-in-depth ; https://docs.asbplayer.dev/docs/reference/settings ; https://docs.asbplayer.dev/docs/guides/one-click-mining ; https://docs.asbplayer.dev/docs/common-issues
- mpvacious: https://github.com/Ajatt-Tools/mpvacious
- Language Reactor: https://languagereactor.com/help/export ; export guide: https://forum.languagelearningwithnetflix.com/t/how-to-export-guide/19596 ; Pro thread: https://forum.languagelearningwithnetflix.com/t/language-reactor-pro-features/31894 ; Trancy comparison: https://www.trancy.org/blog/language-reactor-pro-vs-trancy-2026-which-is-better-for-language-learners-31f9d225200580a48aa8c5f28602a2b3 ; stork.ai: https://www.stork.ai/en/language-reactor
- subs2srs: https://subs2srs.sourceforge.net/ ; GitHub topic: https://github.com/topics/subs2srs ; yt2srs: https://github.com/kamui-fin/yt2srs ; movies2anki: https://relatedrepos.com/gh/kelciour/movies2anki ; subs2cia: https://relatedrepos.com/gh/dxing97/subs2cia
- Migaku: https://migaku.com/pricing ; community: https://migaku.com/community ; itechguides: https://www.itechguides.com/products/migaku/
- SubMiner: https://subminer-docs.pages.dev/anki-integration ; Anki Miner: https://pypi.org/project/anki-miner/2.4.3/
- Reddit mining sequence: https://redlib.hbubli.cc/r/languagelearning/comments/1l0ipdz/sentence_mining_useful_or_not/mvdt5fl
- Vietnamese asbplayer guide: https://soyuz18.notion.site/Sentence-mining-from-Netflix-and-YouTube-with-asbplayer-83a03590cd8349ba81ca10340645b565

**Research papers (DOIs verified via Crossref on 2026-11-13)**
- Webb 2005, SSLA: https://doi.org/10.1017/S0272263105050023
- Webb 2007, LTR: https://doi.org/10.1177/1362168806072463
- Webb 2009, RELC Journal: https://doi.org/10.1177/0033688209343854
- Laufer & Goldstein 2004, Language Learning: https://doi.org/10.1111/j.0023-8333.2004.00260.x
- Laufer & Hulstijn 2001, Applied Linguistics: https://doi.org/10.1093/applin/22.1.1
- Nakata 2011, CALL: https://doi.org/10.1080/09588221.2010.520675
- Nakata 2016, IRAL: https://doi.org/10.1515/iral-2015-0022
- Nakata & Webb 2016 (smaller sets), SSLA: https://doi.org/10.1017/S0272263115000236
- Nakata 2017 (repeated retrieval), SSLA: https://doi.org/10.1017/S0272263116000280
- Kang, Gollan & Pashler 2013, PB&R: https://doi.org/10.3758/s13423-013-0450-z
- Schneider, Healy & Bourne 2002, JML: https://doi.org/10.1006/jmla.2001.2813
- Barcroft 2006, SLR: https://doi.org/10.1191/0267658306sr276oa
- Prince 1996, MLJ: https://doi.org/10.1111/j.1540-4781.1996.tb05468.x
- Elgort 2011, Language Learning: https://doi.org/10.1111/j.1467-9922.2010.00613.x
- Wang, Spence, Jongman & Sereno 1999, JASA: https://doi.org/10.1121/1.428217
- Godfroid, Lin & Ryu 2017, Language Learning: https://doi.org/10.1111/lang.12246
- Hamada 2016, LTR: https://doi.org/10.1177/1362168815597504
- Hamada 2019, RELC Journal: https://doi.org/10.1177/0033688218771380
- Foote & McDonough 2017, JSLP: https://doi.org/10.1075/jslp.3.1.02foo
- Karpicke & Roediger 2008, Science: https://doi.org/10.1126/science.1152408
- Cepeda et al. 2006, Psych. Bulletin: https://doi.org/10.1037/0033-2909.132.3.354
- Cepeda et al. 2008, Psych. Science: https://doi.org/10.1111/j.1467-9280.2008.02209.x
- Kim & Webb 2022, Language Learning: https://doi.org/10.1111/lang.12479
- Seibert Hanson & Brown 2019/2020, CALL: https://doi.org/10.1080/09588221.2018.1552975
- de Jong & Perfetti 2011, Language Learning: https://doi.org/10.1111/j.1467-9922.2010.00620.x
- Snellings, van Gelderen & de Glopper 2002, Language Learning: https://doi.org/10.1111/1467-9922.00202
- Nation 2007, ILLT: https://doi.org/10.2167/illt039.0
- Swain 1985 (book chapter in *Input in Second Language Acquisition*, Gass & Madden, eds.; no DOI; not re-verified)
- Cloze evidence search hits: https://ir.lib.uwo.ca/etd/8600/ ; https://cris.haifa.ac.il/en/publications/facilitating-long-term-retention-of-vocabulary-the-second-hand-cl/ ; vendor: https://www.clozemaster.com/blog/?p=7651
