# Kiểm cập nhật bản v1 -> v2 (Hán Việt) trên collection Anki tạm: tiến độ học phải giữ nguyên.
import sys, os, shutil, re, json, hashlib
sys.stdout.reconfigure(encoding="utf-8")
SCR = "C:/Users/trinh-v/AppData/Local/Temp/claude/ad1c1fd31c67307a/43f64388-07fc-4045-ac80-4a54f3550946/scratchpad"
sys.path.insert(0, SCR + "/pylib_anki")
from anki.collection import Collection, ImportAnkiPackageRequest, ImportAnkiPackageOptions
from anki.scheduler.v3 import CardAnswer
B = "C:/Users/trinh-v/Desktop/04_Personal/Anki Search/chung/build/zh/"
T = SCR + "/work/anki-update-test"; shutil.rmtree(T, ignore_errors=True); os.makedirs(T)
col = Collection(T + "/collection.anki2")
def imp(path):
    r = col.import_anki_package(ImportAnkiPackageRequest(package_path=path, options=ImportAnkiPackageOptions(with_scheduling=False, with_deck_configs=False)))
    return len(r.log.new), len(r.log.updated), len(r.log.duplicate), len(r.log.conflicting)
print("import v1 (new, updated, dup, conflict):", imp(B + "Tieng_Trung_HSK_nghe_cau.apkg"))
try: col.set_config("fsrs", True)
except Exception as e: print("fsrs config:", e)
did = col.decks.id_for_name("Tiếng Trung HSK"); col.decks.select(did)
answered = []
ratings = [CardAnswer.GOOD, CardAnswer.AGAIN, CardAnswer.HARD, CardAnswer.EASY]
for i in range(50):
    q = col.sched.get_queued_cards(fetch_limit=1)
    if not q.cards: break
    qc = q.cards[0]; card = col.get_card(qc.card.id); card.start_timer()
    ans = col.sched.build_answer(card=card, states=qc.states, rating=ratings[i % 4])
    col.sched.answer_card(ans); answered.append(card.id)
def snap():
    rev = col.db.all("select id, cid, ease, ivl, lastIvl, factor, type from revlog order by id")
    cards = {cid: col.db.first("select due, ivl, type, queue, reps, lapses, data from cards where id=?", cid) for cid in answered}
    return hashlib.sha256(json.dumps(rev).encode()).hexdigest(), len(rev), cards
before = snap()
n_notes, n_cards = col.note_count(), col.card_count()
print("answered", len(answered), "revlog", before[1], "notes", n_notes, "cards", n_cards)
print("import v2 (new, updated, dup, conflict):", imp(B + "Tieng_Trung_HSK_nghe_cau_v2_hanviet.apkg"))
after = snap()
print("notes/cards unchanged:", (col.note_count(), col.card_count()) == (n_notes, n_cards), col.note_count(), col.card_count())
print("revlog unchanged:", before[0] == after[0], after[1])
diff = [cid for cid in answered if before[2][cid] != after[2][cid]]
print("answered cards with changed scheduling:", len(diff))
if diff: print("  e.g.", before[2][diff[0]], "->", after[2][diff[0]])
m = col.models.by_name("Câu nghe v1")
print("notetypes:", [x.name for x in col.models.all_names_and_ids()])
print("template has notes-hv:", "notes-hv" in m["tmpls"][0]["afmt"], "| css has .hv-line:", ".hv-line" in m["css"])
nids = col.find_notes('"note:Câu nghe v1"')
empty = sum(1 for nid in nids if not col.get_note(nid)["Notes"].strip())
print("notes with empty Notes field:", empty, "/", len(nids))
strip = lambda h: re.sub(r"\s+", " ", re.sub(r"<style.*?</style>|<[^>]+>", " ", h, flags=re.S)).strip()
for q, label in (('"NoteKey:zh:hskstory-hsk4:1792758600632"', None), ('Notes:*khác*dùng*', "khac_dung"), ('Notes:*từ*Việt*đọc*', "char_note"), ("tag:hanviet::needs_review", "needs_review")):
    ids = col.find_cards(q) if label else []
    if not ids: continue
    c = col.get_card(ids[0]); a = strip(c.answer())
    i = a.find("Hán Việt") if "Hán Việt" in a else 0
    print(f"--- [{label}]", strip(c.note()["TargetWords"])[:40]); print("   ", a[max(0, a.find(strip(c.note()['TargetWords'])[:4])):][:330])
print("needs_review tag count:", len(col.find_notes("tag:hanviet::needs_review")))
col.close()
