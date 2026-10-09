"""Gibt den Ueberschriften der englischen Seiten die Anker der deutschen.

Links zwischen Seiten zeigen auf deutsche Anker (#aufbau-des-hauptfensters).
Damit sie in der englischen Fassung genauso treffen, bekommt jede englische
Ueberschrift (ab ##) das Attribut { #<deutscher-anker> } — gepaart wird nach
Reihenfolge. Weicht die Zahl der Ueberschriften ab, meldet das Skript die
Seite und laesst sie unveraendert.

Aufruf: python _tools/anker_en.py [--pruefen]
"""
import re
import sys
import pathlib
from markdown.extensions.toc import slugify

root = pathlib.Path(__file__).resolve().parent.parent / "docs"
H = re.compile(r"^(#{2,6})\s+(.*?)\s*$")
ATTR = re.compile(r"\s*\{[^}]*#[\w-]+[^}]*\}\s*$")


def ueberschriften(zeilen):
    """(Zeilennummer, Ebene, Text) aller Ueberschriften ausserhalb von Codebloecken."""
    aus, im_code = [], False
    for i, z in enumerate(zeilen):
        if z.lstrip().startswith(("```", "~~~")):
            im_code = not im_code
            continue
        if im_code or z.startswith("    "):
            continue
        m = H.match(z)
        if m:
            aus.append((i, len(m.group(1)), m.group(2)))
    return aus


def anker(text, gesehen):
    m = re.search(r"\{[^}]*#([\w-]+)", text)
    if m:
        a = m.group(1)
    else:
        a = slugify(re.sub(r"<[^>]+>|:[\w-]+:", "", text).replace("**", "").replace("`", ""), "-")
    if a in gesehen:
        gesehen[a] += 1
        a = f"{a}_{gesehen[a]}"
    else:
        gesehen[a] = 0
    return a


pruefen = "--pruefen" in sys.argv
abweichend = []
geaendert = 0
for en in sorted(root.rglob("*.en.md")):
    de = en.with_name(en.name[:-6] + ".md")
    if not de.exists():
        continue
    dz = de.read_text(encoding="utf-8").splitlines()
    ez = en.read_text(encoding="utf-8").splitlines()
    dh, eh = ueberschriften(dz), ueberschriften(ez)
    if [l for _, l, _ in dh] != [l for _, l, _ in eh]:
        abweichend.append(f"{en.relative_to(root)}: DE {len(dh)} / EN {len(eh)} Ueberschriften")
        continue
    gd, ge = {}, {}
    neu = False
    for (_, _, dt), (ei, el, et) in zip(dh, eh):
        a_de = anker(dt, gd)
        a_en = anker(et, ge)
        if a_de == a_en or ATTR.search(et):
            continue
        ez[ei] = f"{'#' * el} {et} {{ #{a_de} }}"
        neu = True
    if neu and not pruefen:
        en.write_text("\n".join(ez) + "\n", encoding="utf-8")
        geaendert += 1
print(f"{geaendert} englische Seiten mit deutschen Ankern versehen")
for a in abweichend:
    print("ABWEICHUNG", a)
