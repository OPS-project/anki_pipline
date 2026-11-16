import sys, zipfile, sqlite3, json, re, collections
sys.stdout.reconfigure(encoding="utf-8")
p = sys.argv[1]; work = sys.argv[2]
z = zipfile.ZipFile(p); names = set(z.namelist())
open(work + "/out.sqlite", "wb").write(z.read("collection.anki2"))
db = sqlite3.connect(work + "/out.sqlite")
mm = json.loads(z.read("media")); files = set(mm.values())
decks = json.loads(db.execute("select decks from col").fetchone()[0])
did2name = {int(k): v["name"] for k, v in decks.items()}
cnt = collections.Counter(did2name[d] for (d,) in db.execute("select did from cards"))
print("notes", db.execute("select count(*) from notes").fetchone()[0], "cards", sum(cnt.values()), "decks", len(cnt), "media", len(files))
for k in sorted(cnt)[:5] + sorted(cnt)[-3:]: print("  ", k, cnt[k])
missing = 0; refs = 0
for (flds,) in db.execute("select flds from notes"):
    for s in re.findall(r"\[sound:([^\]]+)\]", flds):
        refs += 1; missing += s not in files
print("sound refs", refs, "missing", missing)
guids = [g for (g,) in db.execute("select guid from notes")]; print("dup guids", len(guids) - len(set(guids)))
bad_tone = 0
for (flds,) in db.execute("select flds from notes"):
    pin = flds.split("\x1f")[3]
    if "tone-" not in pin: bad_tone += 1
print("notes without colored pinyin", bad_tone)
for nid, flds in db.execute("select id, flds from notes where id in (select min(id) from notes) or flds like '%hsk5:%' limit 2"):
    f = flds.split("\x1f"); print("---", f[0]); print(" S:", f[1]); print(" P:", f[3][:300]); print(" EN:", f[8]); print(" T:", f[13][:200]); print(" A:", f[4], f[25])
