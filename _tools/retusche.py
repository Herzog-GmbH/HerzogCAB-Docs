"""Ersetzt Texte in Screenshots (Testkonto-Namen -> Musterdaten).

Die Desktop-Bilder entstehen mit einem internen Testkonto; dessen Name,
E-Mail-Adresse und Kontoname werden hier durch die Musterdaten ersetzt.
Jede Regel: Bild, Rechteck (x0, y0, x1, y1), neuer Text, Schrift, Groesse.
Hintergrund = haeufigste Randfarbe des Rechtecks, Schriftfarbe = dunkelste
(bzw. bei dunklem Grund hellste) Farbe darin. Der Text wird links und
vertikal mittig gesetzt.

Aufruf: python _tools/retusche.py <regeldatei.json>
Regeldatei: [{"bild": "...png", "box": [x0,y0,x1,y1], "text": "...",
              "schrift": "segoeui|seguisb|segoeuib", "groesse": 14,
              "farbe": "#rrggbb" (optional), "grund": "#rrggbb" | "verlauf" (optional),
              "ausrichtung": "links|mitte", "einzug": px (optional)}]
"""
import json
import sys
import collections
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent / "docs" / "assets" / "screenshots"
FONTS = {k: f"C:/Windows/Fonts/{k}.ttf" for k in ("segoeui", "seguisb", "segoeuib")}


def farbe(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def anwenden(regel):
    p = ROOT / regel["bild"]
    im = Image.open(p).convert("RGB")
    x0, y0, x1, y1 = regel["box"]
    px = im.load()
    rand = [px[x, y0] for x in range(x0, x1)] + [px[x, y1 - 1] for x in range(x0, x1)]
    verlauf = regel.get("grund") == "verlauf"   # Hintergrund spaltenweise aus der Zeile ueber dem Rechteck
    if verlauf:
        grund = px[x0, y0 - 1]
    else:
        grund = farbe(regel["grund"]) if "grund" in regel else collections.Counter(rand).most_common(1)[0][0]
    innen = [px[x, y] for x in range(x0, x1) for y in range(y0, y1)]
    hell = sum(grund) > 380
    if "farbe" in regel:
        schrift_farbe = farbe(regel["farbe"])
    else:
        schrift_farbe = min(innen, key=sum) if hell else max(innen, key=sum)
    d = ImageDraw.Draw(im)
    if verlauf:
        for x in range(x0, x1):
            d.line((x, y0, x, y1 - 1), fill=px[x, y0 - 1])
    else:
        d.rectangle((x0, y0, x1 - 1, y1 - 1), fill=grund)
    f = ImageFont.truetype(FONTS[regel.get("schrift", "segoeui")], regel.get("groesse", 14))
    l, t, r, b = d.textbbox((0, 0), regel["text"], font=f)
    y = y0 + ((y1 - y0) - (b - t)) / 2 - t
    x = x0 + regel.get("einzug", 0) if regel.get("ausrichtung", "links") == "links" else x0 + ((x1 - x0) - (r - l)) / 2 - l
    d.text((x, y), regel["text"], font=f, fill=schrift_farbe)
    im.save(p)
    return p.name


regeln = json.load(open(sys.argv[1], encoding="utf-8"))
for r in regeln:
    print("retuschiert", anwenden(r), r["text"])
