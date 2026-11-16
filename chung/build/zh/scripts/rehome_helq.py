# Copy helq apkg, renaming its decks under "Tiếng Trung HSK::00 Phát âm & thanh điệu (helq)". Source untouched.
import sys, zipfile, sqlite3, json, os, collections, shutil
sys.stdout.reconfigure(encoding="utf-8")
PROJ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../.."))
SRC = PROJ + "/chung/raw/helq-mandarin-ear-training/deck.apkg"
OUT = PROJ + "/chung/build/zh/00_Phat_am_thanh_dieu_helq.apkg"
WORK = sys.argv[1]; os.makedirs(WORK, exist_ok=True)
NEW = "Tiếng Trung HSK::00 Phát âm & thanh điệu (helq)"
def rename(n):
    if n == "Chinese::Pinyin" or n == "Chinese": return NEW
    if n.startswith("Chinese::Pinyin::"): return NEW + "::" + n[len("Chinese::Pinyin::"):]
    return n
zin = zipfile.ZipFile(SRC)
patched = {}
for c in ("collection.anki21", "collection.anki2"):
    p = f"{WORK}/{c}"; open(p, "wb").write(zin.read(c))
    db = sqlite3.connect(p)
    decks = json.loads(db.execute("select decks from col").fetchone()[0])
    cnt = collections.Counter(d for (d,) in db.execute("select did from cards"))
    # merge 'Chinese' and 'Chinese::Pinyin' (both map to NEW): move cards of 'Chinese' into 'Chinese::Pinyin'
    by_name = {v["name"]: int(k) for k, v in decks.items()}
    if "Chinese" in by_name and "Chinese::Pinyin" in by_name:
        db.execute("update cards set did=? where did=?", (by_name["Chinese::Pinyin"], by_name["Chinese"]))
        db.execute("update cards set odid=? where odid=?", (by_name["Chinese::Pinyin"], by_name["Chinese"]))
        del decks[str(by_name["Chinese"])]
    for k, v in decks.items():
        v["name"] = rename(v["name"])
    db.execute("update col set decks=?", (json.dumps(decks, ensure_ascii=False),))
    db.commit()
    print(c, {decks[str(k)]["name"] if str(k) in decks else k: n for k, n in cnt.items()})
    db.close(); patched[c] = p
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_STORED) as zout:
    for info in zin.infolist():
        if info.filename in patched:
            zout.write(patched[info.filename], info.filename)
        else:
            with zin.open(info) as src, zout.open(info.filename, "w") as dst: shutil.copyfileobj(src, dst, 1 << 20)
print("->", OUT, os.path.getsize(OUT))
