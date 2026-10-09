#!/usr/bin/env python3
"""Erzeugt SCREENSHOTS-DESKTOP.md aus den Screenshot-Platzhaltern des Handbuchs.

Sammelt alle Bloecke

    !!! warning "📷 Screenshot fehlt"
        **Motiv:** ...
        **So erzeugen:** ...
        **Ziel-Datei:** `assets/screenshots/<kapitel>/<name>.png`

unter docs/ ein (auch eingerueckte, z. B. in Content-Tabs, und mehrzeilige
Feldwerte) und schreibt sie gruppiert nach Tab und Bereich der Navigation
(Reihenfolge wie in mkdocs.yml) in SCREENSHOTS-DESKTOP.md.

Nicht in die Liste kommen Web-App- und Portal-Bilder (Seiten unter docs/web/
und docs/portal/, Ziel unter assets/screenshots/web|portal/ oder Zeile
`<!-- web-bild ... -->`). Die entstehen per _tools/web_screenshots.py.

Zusaetzlich listet die Datei alle Desktop-Bestandsbilder, die eine Seite
einbindet, mit dem Datum ihres letzten Commits.

Der Abschnitt zwischen den Markierungen <!-- veraltet:start --> und
<!-- veraltet:end --> wird von Hand gepflegt und beim Neuerzeugen aus der
bestehenden Datei uebernommen.

Aufruf (im Repo-Root):
    python _tools/screenshot_liste.py            # SCREENSHOTS-DESKTOP.md neu schreiben
    python _tools/screenshot_liste.py --pruefen  # nur pruefen, Exit 1 bei fehlenden Feldern
                                                 # oder doppelten Ziel-Dateien
"""

from __future__ import annotations

import datetime
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
AUSGABE = ROOT / "SCREENSHOTS-DESKTOP.md"
MKDOCS = ROOT / "mkdocs.yml"

KOPF_RE = re.compile(r'^(?P<einzug>[ \t]*)!!! warning "📷 Screenshot fehlt"\s*$')
FELD_RE = re.compile(
    r"\*\*(?P<name>Motiv|So erzeugen|Ziel-Datei):\*\*\s*(?P<wert>.*?)"
    r"(?=\*\*(?:Motiv|So erzeugen|Ziel-Datei):\*\*|$)",
    re.S,
)
BILD_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<pfad>[^)\s]*assets/screenshots/[^)\s]+)\)")
WEB_ORDNER = ("web/", "portal/")
DESKTOP_TAB = "Desktop-App"
# Bilder fremder Programme (CodeMeter, Wibu, Installer): vom UI-Review nicht betroffen
FREMD_ORDNER = ("assets/screenshots/codemeter/", "assets/screenshots/installer/",
                "assets/screenshots/activate-license/")

VERALTET_START = "<!-- veraltet:start -->"
VERALTET_ENDE = "<!-- veraltet:end -->"
VERALTET_VORGABE = """## Zusätzlich zu ersetzen: veraltete Bestandsbilder

| Datei | Warum | Was drauf sein soll |
|---|---|---|
"""


# ---------------------------------------------------------------------------
# Navigation aus mkdocs.yml: Seite -> (Tab, Bereich, laufende Nummer)
# ---------------------------------------------------------------------------
class _Lader(yaml.SafeLoader):
    """SafeLoader, der die !!python/name-Tags von mkdocs.yml einfach ignoriert."""


_Lader.add_multi_constructor("tag:yaml.org,2002:python/", lambda lader, suffix, knoten: None)


def navigation() -> dict[str, tuple[str, str, int]]:
    daten = yaml.load(MKDOCS.read_text(encoding="utf-8"), Loader=_Lader)
    ordnung: dict[str, tuple[str, str, int]] = {}
    zaehler = 0

    def seiten(eintrag):
        """Alle Seitenpfade unterhalb eines Nav-Eintrags in Reihenfolge."""
        if isinstance(eintrag, str):
            yield eintrag
        elif isinstance(eintrag, list):
            for e in eintrag:
                yield from seiten(e)
        elif isinstance(eintrag, dict):
            for wert in eintrag.values():
                yield from seiten(wert)

    for oben in daten.get("nav", []):
        if isinstance(oben, str):
            tab, inhalt = "Start", [oben]
        else:
            (tab, inhalt), = oben.items()
        if isinstance(inhalt, str):
            inhalt = [inhalt]
        for eintrag in inhalt:
            # Bereich = Unterabschnitt mit eigener Seitenliste; im Tab
            # „Desktop-App" ist jeder Eintrag ein Programmbereich. Einzelne
            # Seiten der übrigen Tabs laufen unter dem Tab selbst.
            if isinstance(eintrag, dict):
                (bereich, unter), = eintrag.items()
                if not isinstance(unter, list) and tab != DESKTOP_TAB:
                    bereich = tab
            else:
                bereich, unter = tab, eintrag
            for seite in seiten(unter):
                if seite not in ordnung:
                    zaehler += 1
                    ordnung[seite] = (tab, bereich, zaehler)
    return ordnung


# ---------------------------------------------------------------------------
# Platzhalter einsammeln
# ---------------------------------------------------------------------------
@dataclass
class Platzhalter:
    seite: str
    zeile: int
    motiv: str = ""
    erzeugen: str = ""
    ziel: str = ""
    web: bool = False
    fehler: list[str] = field(default_factory=list)


def _einzug(zeile: str) -> int:
    return len(zeile) - len(zeile.lstrip(" \t"))


def platzhalter_der_seite(md: Path) -> list[Platzhalter]:
    rel = md.relative_to(DOCS).as_posix()
    zeilen = md.read_text(encoding="utf-8").splitlines()
    gefunden: list[Platzhalter] = []
    i = 0
    while i < len(zeilen):
        kopf = KOPF_RE.match(zeilen[i])
        if not kopf:
            i += 1
            continue
        basis = _einzug(zeilen[i])
        p = Platzhalter(seite=rel, zeile=i + 1)
        inhalt: list[str] = []
        j = i + 1
        while j < len(zeilen):
            z = zeilen[j]
            if not z.strip() or _einzug(z) <= basis:
                break
            if "<!-- web-bild" in z:
                p.web = True
            else:
                inhalt.append(z.strip())
            j += 1
        text = " ".join(inhalt)
        for m in FELD_RE.finditer(text):
            wert = " ".join(m.group("wert").split())
            if m.group("name") == "Motiv":
                p.motiv = wert
            elif m.group("name") == "So erzeugen":
                p.erzeugen = wert
            else:
                p.ziel = wert.strip("` ")
        for name, wert in (("Motiv", p.motiv), ("So erzeugen", p.erzeugen), ("Ziel-Datei", p.ziel)):
            if not wert:
                p.fehler.append(f"Feld „{name}“ fehlt")
        if rel.startswith(WEB_ORDNER) or any(
            p.ziel.startswith(f"assets/screenshots/{o}") for o in WEB_ORDNER
        ):
            p.web = True
        gefunden.append(p)
        i = j
    return gefunden


# ---------------------------------------------------------------------------
# Bestandsbilder (Desktop) einsammeln
# ---------------------------------------------------------------------------
def git_datum(pfad: Path) -> str:
    try:
        aus = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(pfad.relative_to(ROOT))],
            cwd=ROOT, capture_output=True, text=True, check=False,
        ).stdout.strip()
    except OSError:
        aus = ""
    if not aus:
        return "–"
    j, m, t = aus.split("-")
    return f"{t}.{m}.{j}"


def bestandsbilder(md_dateien: list[Path]) -> dict[str, dict]:
    bilder: dict[str, dict] = {}
    for md in md_dateien:
        rel = md.relative_to(DOCS).as_posix()
        if rel.startswith(WEB_ORDNER):
            continue
        for m in BILD_RE.finditer(md.read_text(encoding="utf-8")):
            ziel = (md.parent / m.group("pfad")).resolve()
            try:
                ziel_rel = ziel.relative_to(DOCS).as_posix()
            except ValueError:
                continue
            if any(ziel_rel.startswith(f"assets/screenshots/{o}") for o in WEB_ORDNER):
                continue
            eintrag = bilder.setdefault(ziel_rel, {"seiten": [], "alt": m.group("alt"), "pfad": ziel})
            if rel not in eintrag["seiten"]:
                eintrag["seiten"].append(rel)
    return bilder


# ---------------------------------------------------------------------------
# Ausgabe
# ---------------------------------------------------------------------------
def zelle(text: str) -> str:
    return text.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;") if text else "–"


def zelle_md(text: str) -> str:
    """Wie zelle(), laesst aber bereits maskierte Markdown-Texte (Backticks, &lt;) stehen."""
    return text.replace("|", "\\|") if text else "–"


def kuerzen(text: str, laenge: int = 110) -> str:
    text = " ".join(text.split())
    return text if len(text) <= laenge else text[: laenge - 1].rstrip() + "…"


def veraltet_abschnitt() -> str:
    if AUSGABE.exists():
        alt = AUSGABE.read_text(encoding="utf-8")
        a, e = alt.find(VERALTET_START), alt.find(VERALTET_ENDE)
        if a >= 0 and e > a:
            return alt[a + len(VERALTET_START): e].strip("\n") + "\n"
    return VERALTET_VORGABE


def erzeugen(liste: list[Platzhalter], nav: dict, bilder: dict[str, dict]) -> str:
    heute = datetime.date.today().strftime("%d.%m.%Y")
    seiten = sorted({p.seite for p in liste})
    gruppen: dict[tuple[str, str], list[Platzhalter]] = {}
    for p in liste:
        tab, bereich, _ = nav.get(p.seite, ("Ohne Navigation", "Ohne Navigation", 10**6))
        gruppen.setdefault((tab, bereich), []).append(p)

    def gruppen_rang(schluessel):
        tab, bereich = schluessel
        return min(nav.get(p.seite, ("", "", 10**6))[2] for p in gruppen[schluessel])

    out: list[str] = []
    w = out.append
    w("# Screenshots Desktop-App — Liste für Eike")
    w("")
    w(f"Stand: {heute}. Insgesamt **{len(liste)}** Platzhalter auf {len(seiten)} Seiten.")
    w("")
    w("> Diese Datei erzeugt `python _tools/screenshot_liste.py` aus allen Blöcken "
      "`!!! warning \"📷 Screenshot fehlt\"` unter `docs/`. Nicht von Hand bearbeiten — "
      "Ausnahme ist der markierte Abschnitt „veraltete Bestandsbilder“, den das Skript übernimmt.")
    w("")
    w("Jeder Platzhalter steht im Handbuch mit **Motiv**, **So erzeugen** und **Ziel-Datei** "
      "(Suche nach „Screenshot fehlt“). Bild unter `docs/<Ziel-Datei>` ablegen und den Platzhalter durch "
      "`![<Bildunterschrift>](<relativer Pfad>)` ersetzen, danach dieses Skript erneut laufen lassen.")
    w("")
    w("## Aufnahme-Regeln")
    w("")
    w("* **Helles Theme**, Fensterbreite **ca. 1600 px**, Windows-Skalierung 100 %.")
    w("* **Navigation eingeklappt:** vorher den **Pfeil oben in der Navigation** klicken. Der Inhalt bekommt "
      "dann die ganze Breite. Die eingeklappte Navigation klappt beim Überfahren mit der Maus wieder auf — "
      "Mauszeiger vor der Aufnahme aus dem linken Rand nehmen. (Erst unter 1500 px Fensterbreite klappt "
      "sie von selbst ein; bei 1600 px also von Hand.)")
    w("* **Musterdaten** „Musterbetrieb“ — keine echten Kunden-, Preis- oder Personendaten, keine echten "
      "Tenant-/Client-IDs, keine echten E-Mail-Adressen.")
    w("* **Kunden-Build** mit Kontoanmeldung (`CONFIG+=customer CONFIG+=account`), soweit beim Bild "
      "nicht anders angegeben (Dongle-Bilder: Build mit CodeMeter). Kein interner Build — der zeigt "
      "Einträge, die Kunden nicht haben.")
    w("* Aufnahme per Fensteraufnahme ohne Mauszeiger; Annotationen nach STYLEGUIDE.md "
      "(blaue Nummernkreise `#00459a`, gelber Fokus-Rahmen `#ffb800`).")
    w("* **Web-App- und Portal-Bilder** gehören nicht in diese Liste. Sie entstehen per "
      "`_tools/web_screenshots.py` aus der lokalen Testumgebung.")
    w("")
    w(VERALTET_START)
    w(veraltet_abschnitt().rstrip("\n"))
    w(VERALTET_ENDE)
    w("")

    nummer = 0
    for schluessel in sorted(gruppen, key=gruppen_rang):
        tab, bereich = schluessel
        eintraege = sorted(gruppen[schluessel],
                           key=lambda p: (nav.get(p.seite, ("", "", 10**6))[2], p.zeile))
        titel = tab if bereich == tab else f"{tab} › {bereich}"
        anzahl = len(eintraege)
        w(f"## {titel} — {anzahl} {'Bild' if anzahl == 1 else 'Bilder'}")
        w("")
        w("| # | Seite | Motiv | So erzeugen | Ziel-Datei |")
        w("|---|---|---|---|---|")
        for p in eintraege:
            nummer += 1
            ziel = f"`{p.ziel}`" if p.ziel else "–"
            w(f"| {nummer} | `{p.seite}` | {zelle_md(p.motiv)} | {zelle_md(p.erzeugen)} | {ziel} |")
        w("")

    eigene = {z: b for z, b in bilder.items() if not z.startswith(FREMD_ORDNER)}
    fremde = {z: b for z, b in bilder.items() if z.startswith(FREMD_ORDNER)}

    def bildtabelle(auswahl: dict[str, dict]) -> None:
        w("| Datei | eingebunden auf | Bildunterschrift | Stand |")
        w("|---|---|---|---|")
        for ziel in sorted(auswahl):
            b = auswahl[ziel]
            stand = git_datum(b["pfad"]) if b["pfad"].exists() else "**Datei fehlt**"
            seiten_txt = ", ".join(f"`{s}`" for s in b["seiten"])
            w(f"| `{ziel}` | {seiten_txt} | {zelle(kuerzen(b['alt']))} | {stand} |")
        w("")

    w(f"## Alle Desktop-Bestandsbilder — {len(eigene)} Dateien neu aufnehmen")
    w("")
    w("Alle Bilder der Herzog-CAB-Oberfläche stammen von **vor dem UI-Review (02.10.2026)** und der neuen "
      "Startseite (Entwurf 2, 08.10.2026): Seitenkopf als Karte, alte Knopfgrößen und -farben, Navigation "
      "ausgeklappt, Menü „Über“. Sie sollten nach denselben Aufnahme-Regeln neu entstehen; die Datei "
      "behält ihren Namen. Spalte „Stand“ = letzter Commit der Bilddatei. Bilder, für die schon ein "
      "Platzhalter mit derselben Ziel-Datei oben steht, sind hier mit aufgeführt.")
    w("")
    bildtabelle(eigene)
    if fremde:
        w(f"## Bilder fremder Programme — {len(fremde)} Dateien, nicht betroffen")
        w("")
        w("CodeMeter-, Wibu- und Installer-Bilder zeigen keine Herzog-CAB-Oberfläche; das UI-Review betrifft "
          "sie nicht. Neu aufnehmen nur, wenn sich das jeweilige Programm ändert.")
        w("")
        bildtabelle(fremde)
    return "\n".join(out)


def main(argv: list[str]) -> int:
    pruefen = "--pruefen" in argv
    md_dateien = sorted(DOCS.rglob("*.md"))
    alle: list[Platzhalter] = []
    for md in md_dateien:
        alle.extend(platzhalter_der_seite(md))
    desktop = [p for p in alle if not p.web]

    probleme = []
    for p in desktop:
        for f in p.fehler:
            probleme.append(f"{p.seite}:{p.zeile}: {f}")
    ziele: dict[str, str] = {}
    for p in desktop:
        if p.ziel and p.ziel in ziele:
            probleme.append(f"{p.seite}:{p.zeile}: Ziel-Datei {p.ziel} auch in {ziele[p.ziel]}")
        elif p.ziel:
            ziele[p.ziel] = f"{p.seite}:{p.zeile}"

    print(f"{len(alle)} Platzhalter gefunden, davon {len(alle) - len(desktop)} Web/Portal, "
          f"{len(desktop)} Desktop auf {len({p.seite for p in desktop})} Seiten.")
    for z in probleme:
        print("  ! " + z)
    if pruefen:
        return 1 if probleme else 0

    text = erzeugen(desktop, navigation(), bestandsbilder(md_dateien))
    with open(AUSGABE, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(text)
    print(f"geschrieben: {AUSGABE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
