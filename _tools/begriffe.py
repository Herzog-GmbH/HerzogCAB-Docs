"""Baut das Begriffswoerterbuch DE->EN aus den Programmuebersetzungen.

Quellen: app_en.ts (Desktop, Qt) und die Web-App-Uebersetzungen (en.json).
Ausgabe: _tools/begriffe_de_en.json  {deutscher Quelltext: englische Uebersetzung}
und      _tools/begriffe_handbuch.tsv  (nur Begriffe, die im Handbuch fett vorkommen)
Aufruf:  python _tools/begriffe.py <HerzogCAB-Repo> <Lizenzserver-Repo>
"""
import json, re, sys, collections, pathlib, html
import xml.etree.ElementTree as ET

app = pathlib.Path(sys.argv[1]); web = pathlib.Path(sys.argv[2])
root = pathlib.Path(__file__).resolve().parent.parent
paare = collections.defaultdict(collections.Counter)

t = ET.parse(app / "app_en.ts")
for m in t.iter("message"):
    s = m.findtext("source") or ""; tr = m.find("translation")
    if tr is None or (tr.get("type") in ("unfinished", "obsolete", "vanished")): continue
    e = "".join(tr.itertext()).strip()
    if s.strip() and e: paare[s.strip()][e] += 2   # Desktop zaehlt doppelt
for f in (web / "web/src/i18n/en.json", web / "web/src/i18n/web/en.json"):
    if f.exists():
        for s, e in json.load(open(f, encoding="utf-8")).items():
            if s.strip() and e: paare[s.strip()][e.strip()] += 1

woerter = {s: c.most_common(1)[0][0] for s, c in paare.items()}
json.dump(woerter, open(root / "_tools/begriffe_de_en.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0, sort_keys=True)

fett = collections.Counter()
for md in (root / "docs").rglob("*.md"):
    if ".en." in md.name: continue
    for b in re.findall(r"\*\*([^*\n]{2,80})\*\*", md.read_text(encoding="utf-8")):
        fett[b.strip().rstrip(":").strip()] += 1
nocolon = {k.rstrip(":").strip(): v for k, v in woerter.items()}
with open(root / "_tools/begriffe_handbuch.tsv", "w", encoding="utf-8") as o:
    o.write("deutsch\tenglisch\thaeufigkeit\n")
    for b, n in fett.most_common():
        e = nocolon.get(b) or nocolon.get(b + "…") or nocolon.get(b + "...")
        o.write(f"{b}\t{(e or '').rstrip(':').strip()}\t{n}\n")
print(len(woerter), "Paare;", len(fett), "fette Begriffe;", sum(1 for b in fett if nocolon.get(b)), "zugeordnet")
