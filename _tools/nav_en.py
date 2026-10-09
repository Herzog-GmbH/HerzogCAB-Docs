"""Schreibt die englischen Navigationstitel aus _tools/nav_en.txt in mkdocs.yml.

Ersetzt den Block zwischen den Markern  # nav_en:start  und  # nav_en:end
im i18n-Plugin. Meldet deutsche Navigationstitel ohne englische Entsprechung.
Aufruf: python _tools/nav_en.py
"""
import re, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
yml = root / "mkdocs.yml"
s = yml.read_text(encoding="utf-8")
paare = []
for z in (root / "_tools/nav_en.txt").read_text(encoding="utf-8").splitlines():
    if z.strip() and not z.startswith("#") and "=" in z:
        de, en = z.split("=", 1)
        paare.append((de.strip(), en.strip()))

nav = s[s.index("\nnav:"):]
titel = {t.strip() for t in re.findall(r"^\s*- ([^:\n]+):", nav, re.M)}
fehlt = sorted(titel - {d for d, _ in paare})
if fehlt:
    print("Ohne englischen Titel:", fehlt)


def q(x):
    return '"' + x.replace("\\", "\\\\").replace('"', '\\"') + '"'


block = "".join(f"            {q(d)}: {q(e)}\n" for d, e in paare if d in titel)
s = re.sub(r"(# nav_en:start\n).*?(\s*# nav_en:end)", lambda m: m.group(1) + block.rstrip("\n") + m.group(2), s, flags=re.S)
yml.write_text(s, encoding="utf-8")
print(len(paare), "Titel geschrieben")
