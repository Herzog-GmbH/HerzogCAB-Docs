"""Tauscht Screenshot-Platzhalter gegen Bilder, sobald die Bilddatei existiert.

Gilt fuer deutsche UND englische Seiten (die englischen enthalten die
Platzhalter woertlich deutsch). Bildunterschrift aus _tools/bildtexte.tsv
(Spalten: ziel, deutsch, englisch); fehlt dort ein Eintrag, nimmt das Skript
den ersten Satzteil des Motivs (deutsch) und meldet die Datei.
Englische Bilder liegen als <name>.en.png neben dem deutschen und werden von
der englischen Fassung automatisch genommen; der Verweis bleibt <name>.png.

Aufruf: python _tools/bilder_einsetzen.py [--trocken]
"""
import os
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PH = re.compile(
    r'^!!! warning "📷 Screenshot fehlt"\n'
    r"    \*\*Motiv:\*\* (?P<motiv>.*?)\n"
    r"    \*\*So erzeugen:\*\* .*?\n"
    r"    \*\*Ziel-Datei:\*\* `(?P<ziel>assets/[^`]+)`\n"
    r"(?:    <!-- web-bild [^\n]* -->\n)?",
    re.M | re.S,
)

texte = {}
tsv = ROOT / "_tools/bildtexte.tsv"
if tsv.exists():
    for z in tsv.read_text(encoding="utf-8").splitlines()[1:]:
        t = z.split("\t")
        if len(t) >= 3:
            texte[t[0].strip()] = (t[1].strip(), t[2].strip())

trocken = "--trocken" in sys.argv
ohne_text, eingesetzt = set(), 0
for md in sorted(DOCS.rglob("*.md")):
    en = md.name.endswith(".en.md")
    s = md.read_text(encoding="utf-8")

    def ersatz(m):
        global eingesetzt
        ziel = m.group("ziel")
        if not (DOCS / ziel).exists():
            return m.group(0)
        de_t, en_t = texte.get(ziel, ("", ""))
        if not de_t:
            ohne_text.add(ziel)
            de_t = re.split(r"[:;,—(]", m.group("motiv"))[0].strip(" .“„\"")
        cap = (en_t or de_t) if en else de_t
        rel = os.path.relpath(DOCS / ziel, md.parent).replace("\\", "/")
        eingesetzt += 1
        return f"![{cap}]({rel})\n"

    neu = PH.sub(ersatz, s)
    if neu != s and not trocken:
        md.write_text(neu, encoding="utf-8", newline="\n")
print(f"{eingesetzt} Platzhalter durch Bilder ersetzt")
for z in sorted(ohne_text):
    print("OHNE BILDTEXT", z)
