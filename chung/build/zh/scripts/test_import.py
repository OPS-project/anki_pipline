import sys, os, shutil, re
sys.stdout.reconfigure(encoding="utf-8")
SCR = "C:/Users/trinh-v/AppData/Local/Temp/claude/ad1c1fd31c67307a/43f64388-07fc-4045-ac80-4a54f3550946/scratchpad"
sys.path.insert(0, SCR + "/pylib_anki")
from anki.collection import Collection, ImportAnkiPackageRequest, ImportAnkiPackageOptions
T = SCR + "/work/anki-test"; shutil.rmtree(T, ignore_errors=True); os.makedirs(T)
col = Collection(T + "/collection.anki2")
B = "C:/Users/trinh-v/Desktop/04_Personal/Anki Search/chung/build/zh/"
for f in ("00_Phat_am_thanh_dieu_helq.apkg", "Tieng_Trung_HSK_nghe_cau.apkg"):
    r = col.import_anki_package(ImportAnkiPackageRequest(package_path=B + f, options=ImportAnkiPackageOptions(with_scheduling=False, with_deck_configs=False)))
    print(f, "new notes:", len(r.log.new), "dup:", len(r.log.duplicate), "conflict:", len(r.log.conflicting))
names = sorted(d.name for d in col.decks.all_names_and_ids())
print("decks", len(names)); [print("  ", n) for n in names[:12]]; print("   ...", names[-1])
print("cards total", col.card_count())
did = col.decks.id_for_name("Tiếng Trung HSK::HSK1::Phần 01 (từ 1–100)")
cid = col.find_cards(f"did:{did}")[0]
c = col.get_card(cid)
strip = lambda h: re.sub(r"\s+", " ", re.sub(r"<style.*?</style>|<[^>]+>", " ", h, flags=re.S)).strip()
print("Q:", strip(c.question())); print("A:", strip(c.answer())[:400])
print("Q sounds:", [a.filename for a in c.question_av_tags()]); print("A sounds:", [a.filename for a in c.answer_av_tags()])
# media check
mc = col.media.check(); print("media missing:", len(mc.missing), "unused:", len(mc.unused))
col.close()
