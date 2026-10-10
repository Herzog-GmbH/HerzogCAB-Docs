"""Sprungmarken (Anker-IDs) der Ueberschriften: englische Seiten gegen die deutschen.

F1-Hilfe und Querverweise springen auf Abschnitte (#aufbau-des-hauptfensters).
Die IDs muessen deshalb in beiden Sprachen gleich sein. Eine englische
Ueberschrift behaelt die ID der deutschen ueber ein angehaengtes Attribut,
z. B. `## Profile tab { #tab-profil }` (auch `{#tab-profil}`). Ergibt der
englische Text zufaellig dieselbe ID, ist kein Attribut noetig.

Die IDs entstehen genau wie im Build: Das Skript laedt mkdocs.yml und rendert die
Seite mit denselben Markdown-Erweiterungen und toc-Einstellungen (inkl. slugify)
wie MkDocs selbst - jede Schreibweise des Attributs wird also verstanden.

Deutsche Seite -> Ueberschriften mit ID, fertig zum Uebernehmen in die .en.md:

    python _tools/anker.py docs/web/versions.md

Englische Seite(n) -> Abgleich mit der deutschen Seite daneben:

    python _tools/anker.py docs/web/versions.en.md
    python _tools/anker.py --alle            # alle *.en.md unter docs/ (so prueft die CI)
    python _tools/anker.py --alle --streng   # zusaetzlich: jede Ueberschrift ab ## mit { #id }

    Meldet fehlende und zusaetzliche IDs und abweichende Reihenfolge (ab Ebene 2).
    Rueckgabewert 1, wenn etwas nicht passt. Deutsche Seiten ohne .en.md werden
    nur als Hinweis gemeldet (dort zeigt /en/ die deutsche Ersatzseite).

Fehlende Attribute setzen (frueher _tools/anker_en.py):

    python _tools/anker.py --setzen [docs/…/seite.en.md]   # ohne Seite: alle

    Paart deutsche und englische Ueberschriften nach Reihenfolge und haengt an
    jede englische Ueberschrift, deren ID abweicht, `{ #<deutsche-id> }` an.
    Weicht die Folge der Ueberschriften-Ebenen ab, bleibt die Seite unveraendert.

Immer aus dem Repo-Wurzelordner aufrufen (mkdocs.yml muss dort liegen).
"""
from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

_md = None


def markdown_wie_mkdocs():
    """Markdown-Instanz mit Erweiterungen und Einstellungen aus mkdocs.yml."""
    global _md
    if _md is None:
        import markdown
        from mkdocs.config import load_config

        logging.getLogger("mkdocs").setLevel(logging.ERROR)
        cfg = load_config(config_file=str(ROOT / "mkdocs.yml"))
        _md = markdown.Markdown(extensions=cfg["markdown_extensions"],
                                extension_configs=cfg["mdx_configs"])
    return _md


def tooltips_fuer(pfad: Path) -> str:
    """Wie hooks/sprachen.py: Glossar-Tooltips je Sprache anhaengen (aendert keine IDs,
    haelt das Rendern aber identisch zum Build)."""
    name = "glossar-tooltips.en.md" if pfad.name.endswith(".en.md") else "glossar-tooltips.md"
    datei = ROOT / "includes" / name
    return "\n\n" + datei.read_text(encoding="utf-8") if datei.exists() else ""


def ueberschriften(pfad: Path) -> list[dict]:
    """Liste {level, id, name} in Dokumentreihenfolge."""
    from mkdocs.utils import meta

    text = pfad.read_text(encoding="utf-8-sig")
    text, _ = meta.get_data(text)
    md = markdown_wie_mkdocs()
    md.reset()
    md.convert(text + tooltips_fuer(pfad))

    flach = []

    def sammeln(tokens):
        for t in tokens:
            flach.append({"level": t["level"], "id": t["id"], "name": t["name"]})
            sammeln(t.get("children", []))

    sammeln(md.toc_tokens)
    return flach


_ZAUN = re.compile(r"^\s*(```|~~~)")
_ATX = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_ATTR = re.compile(r"\s*\{[^}]*#[\w-]+[^}]*\}\s*$")


def atx_zeilen(zeilen: list[str]) -> list[tuple[int, int, str]]:
    """(Zeilenindex, Ebene, Text) aller ATX-Ueberschriften ausserhalb von Codebloecken.

    Wie im Build: eingerueckte Zeilen (Admonitions, Tabs, Codebloecke) zaehlen
    nicht, Front Matter am Dateianfang auch nicht."""
    aus, im_zaun, start = [], False, 0
    if zeilen and zeilen[0].strip() == "---":
        for i in range(1, len(zeilen)):
            if zeilen[i].strip() in ("---", "..."):
                start = i + 1
                break
    for i in range(start, len(zeilen)):
        z = zeilen[i]
        if _ZAUN.match(z):
            im_zaun = not im_zaun
            continue
        if im_zaun or z[:1] in (" ", "\t"):
            continue
        m = _ATX.match(z)
        if m:
            aus.append((i, len(m.group(1)), m.group(2)))
    return aus


def deutsch_zu(en_pfad: Path) -> Path:
    return en_pfad.with_name(en_pfad.name[: -len(".en.md")] + ".md")


def rel(pfad: Path) -> str:
    return pfad.resolve().relative_to(ROOT).as_posix()


def zeigen(pfad: Path) -> int:
    for h in ueberschriften(pfad):
        print(f"{'#' * h['level']} {h['name']} {{ #{h['id']} }}")
    return 0


def vergleichen(en_pfad: Path, streng: bool = False) -> int:
    de_pfad = deutsch_zu(en_pfad)
    if not de_pfad.exists():
        print(f"{rel(en_pfad)}: keine deutsche Seite {de_pfad.name} gefunden")
        return 1
    de = [h["id"] for h in ueberschriften(de_pfad) if h["level"] >= 2]
    en = [h["id"] for h in ueberschriften(en_pfad) if h["level"] >= 2]
    probleme = []
    fehlen = [i for i in de if i not in en]
    zuviel = [i for i in en if i not in de]
    if fehlen:
        probleme.append("fehlen in .en.md: " + ", ".join(fehlen))
    if zuviel:
        probleme.append("nur in .en.md: " + ", ".join(zuviel))
    if not fehlen and not zuviel and de != en:
        probleme.append("Reihenfolge weicht ab")
    if streng:
        zeilen = en_pfad.read_text(encoding="utf-8-sig").splitlines()
        for nr, ebene, text in atx_zeilen(zeilen):
            if ebene >= 2 and not _ATTR.search(text):
                probleme.append(f"ohne {{ #id }}: Zeile {nr + 1}: {zeilen[nr].strip()}")
    if probleme:
        print(f"{rel(en_pfad)}: {len(probleme)} Problem(e)")
        for p in probleme:
            print("  - " + p)
        return 1
    print(f"{rel(en_pfad)}: OK ({len(en)} Anker wie {de_pfad.name})")
    return 0


def setzen(en_pfad: Path) -> str:
    """Haengt abweichenden englischen Ueberschriften die deutsche ID an.
    Rueckgabe: 'geaendert', 'ok' oder eine Fehlermeldung."""
    de_pfad = deutsch_zu(en_pfad)
    if not de_pfad.exists():
        return f"keine deutsche Seite {de_pfad.name}"
    roh = en_pfad.read_bytes().decode("utf-8")
    nl = "\r\n" if "\r\n" in roh else "\n"
    zeilen = roh.splitlines()
    zeilen_ende = roh.endswith(("\n", "\r"))
    de_h = [h for h in ueberschriften(de_pfad)]
    en_h = [h for h in ueberschriften(en_pfad)]
    en_atx = atx_zeilen(zeilen)
    if [h["level"] for h in de_h] != [h["level"] for h in en_h]:
        return f"Ueberschriften-Ebenen weichen ab (DE {len(de_h)} / EN {len(en_h)}) - von Hand angleichen"
    if [h["level"] for h in en_h] != [e for _, e, _ in en_atx]:
        return "Ueberschriften nicht alle als '# Text' geschrieben - von Hand angleichen"
    neu = False
    for d, e, (idx, ebene, text) in zip(de_h, en_h, en_atx):
        if ebene < 2 or d["id"] == e["id"]:
            continue
        basis = _ATTR.sub("", text)
        zeilen[idx] = f"{'#' * ebene} {basis} {{ #{d['id']} }}"
        neu = True
    if not neu:
        return "ok"
    en_pfad.write_bytes((nl.join(zeilen) + (nl if zeilen_ende else "")).encode("utf-8"))
    return "geaendert"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Anker-IDs der Ueberschriften: englische gegen deutsche Seiten")
    ap.add_argument("seite", nargs="?", type=Path, help="docs/…/seite.md oder seite.en.md")
    ap.add_argument("--alle", action="store_true", help="alle docs/**/*.en.md gegen die deutsche Seite pruefen")
    ap.add_argument("--streng", action="store_true", help="auch Ueberschriften ab ## ohne ausdrueckliches { #id } melden")
    ap.add_argument("--setzen", action="store_true", help="abweichende englische IDs per { #id } auf die deutschen setzen")
    args = ap.parse_args()

    if args.seite:
        pfad = args.seite if args.seite.is_absolute() else Path.cwd() / args.seite
        if not pfad.exists():
            ap.error(f"{args.seite} nicht gefunden")
    else:
        pfad = None

    if args.setzen:
        dateien = [pfad] if pfad else sorted(DOCS.rglob("*.en.md"))
        fehler = 0
        for p in dateien:
            if not p.name.endswith(".en.md"):
                ap.error("--setzen braucht eine .en.md")
            ergebnis = setzen(p)
            if ergebnis == "geaendert":
                print(f"{rel(p)}: deutsche Anker gesetzt")
            elif ergebnis != "ok":
                print(f"{rel(p)}: {ergebnis}")
                fehler = 1
        sys.exit(fehler)

    if args.alle:
        dateien = sorted(DOCS.rglob("*.en.md"))
        if not dateien:
            print("keine .en.md-Dateien gefunden")
        rc = max([vergleichen(p, args.streng) for p in dateien], default=0)
        ohne = sorted(rel(p) for p in DOCS.rglob("*.md")
                      if not p.name.endswith(".en.md") and not p.with_name(p.stem + ".en.md").exists())
        if ohne:
            print(f"Hinweis: {len(ohne)} deutsche Seite(n) ohne .en.md (unter /en/ erscheint die deutsche):")
            for o in ohne:
                print("  - " + o)
        print(f"{len(dateien)} englische Seiten geprueft: " + ("Abweichungen gefunden" if rc else "alle Anker wie im Deutschen"))
        sys.exit(rc)

    if not pfad:
        ap.error("Seite angeben, --alle oder --setzen")
    sys.exit(vergleichen(pfad, args.streng) if pfad.name.endswith(".en.md") else zeigen(pfad))


if __name__ == "__main__":
    main()
