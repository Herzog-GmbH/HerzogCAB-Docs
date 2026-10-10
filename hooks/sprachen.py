"""MkDocs-Hooks fuer die zweisprachige Fassung (Deutsch = Standard, Englisch unter /en/).

Eingebunden ueber `hooks:` in mkdocs.yml. Ergaenzt das Plugin mkdocs-static-i18n
um vier Dinge, die es selbst nicht kann:

1. Glossar-Tooltips je Sprache
   Haengt an jede Seite die Abkuerzungsliste ihrer Inhaltssprache an:
   includes/glossar-tooltips.md (deutsch) bzw. includes/glossar-tooltips.en.md
   (Seiten aus *.en.md). Ersetzt das fruehere `auto_append` von
   pymdownx.snippets, das fuer alle Seiten dieselbe (deutsche) Datei angehaengt
   hat. Eine deutsche Ersatzseite unter /en/ (falls eine .en.md fehlt) behaelt
   die deutschen Tooltips, weil ihr Text deutsch ist.

2. Titel "Auf dieser Seite" je Sprache
   Material liest den Titel des Inhaltsverzeichnisses aus `toc.title`
   (markdown_extensions). Das Plugin darf markdown_extensions nicht je Sprache
   ueberschreiben, deshalb setzt der Hook ihn fuer jedes Sprach-Build.

3. Suchindex je Sprache und 404-Seite je Sprache
   Das Plugin sammelt die Suchtreffer aller Sprachen in EINEM Index
   (/search/search_index.json). Der Hook teilt ihn nach dem letzten Build auf:
     /search/search_index.json     nur deutsche Seiten, lunr-Sprache de
     /en/search/search_index.json  alle Seiten unter /en/, lunr-Sprache en
   Die englischen Seiten laden ihren Index ueber overrides/main.html.
   Ausserdem bekommt jede Sprache ihre eigene 404.html (sonst ueberschreibt das
   englische Build die deutsche); ihr Sprachumschalter fuehrt auf die
   Startseiten (sonst auf die zuletzt gebaute Seite).

4. Hinweis auf fehlende Uebersetzungen
   Zeigt eine Sprache eine Seite der Standardsprache an (Ersatzseite, weil die
   .en.md fehlt), meldet der Hook die Seiten am Ende des Builds (Info, kein
   Abbruch - eine neue deutsche Seite darf vor ihrer Uebersetzung live gehen).
"""
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

from mkdocs.plugins import event_priority, get_plugin_logger

log = get_plugin_logger("sprachen")

ROOT = Path(__file__).resolve().parent.parent
TOOLTIPS = {
    "de": ROOT / "includes" / "glossar-tooltips.md",
    "en": ROOT / "includes" / "glossar-tooltips.en.md",
}
# Sprachen ohne Eintrag behalten den Wert aus mkdocs.yml (deutsch).
TOC_TITEL = {"en": "On this page"}

_toc_original: dict[int, str | None] = {}
_seite_404: dict[str, str] = {}
_ersatzseiten: dict[str, list[str]] = {}


def _i18n(config):
    return config.plugins.get("i18n")


def _sprache(config) -> str:
    plugin = _i18n(config)
    if plugin is None:
        return "de"
    return plugin.current_language or plugin.default_language or "de"


@event_priority(-110)  # nach i18n (-100), das current_language setzt
def on_config(config):
    toc = config.mdx_configs.get("toc")
    if toc is not None:
        _toc_original.setdefault(id(config), toc.get("title"))
        toc["title"] = TOC_TITEL.get(_sprache(config), _toc_original[id(config)])
    return config


def on_page_markdown(markdown, page, config, files):
    sprache = getattr(page.file, "locale", None) or "de"
    aktuell = _sprache(config)
    if sprache != aktuell:
        _ersatzseiten.setdefault(aktuell, []).append(page.file.src_uri)
    datei = TOOLTIPS.get(sprache, TOOLTIPS["de"])
    if datei.exists():
        markdown = markdown + "\n\n" + datei.read_text(encoding="utf-8")
    return markdown


def on_template_context(context, template_name, config):
    # Das Plugin biegt die Links des Sprachumschalters je Seite auf die passende
    # Seite der anderen Sprache um (als Attribut config.extra.alternate, das das
    # Template vor dem Eintrag config.extra["alternate"] liest). Die englische
    # 404-Seite erbte so die Links der zuletzt gebauten deutschen Seite.
    # Auf der 404-Seite fuehrt der Umschalter deshalb auf die Startseiten.
    if template_name == "404.html":
        plugin = _i18n(config)
        if plugin is not None and plugin.extra_alternate:
            config.extra["alternate"] = deepcopy(plugin.extra_alternate)
            config.extra.alternate = deepcopy(plugin.extra_alternate)
    return context


def on_post_template(output_content, template_name, config):
    if template_name == "404.html":
        _seite_404[_sprache(config)] = output_content
    return output_content


@event_priority(-200)  # nach i18n (-100), das am Ende den gemeinsamen Index schreibt
def on_post_build(config):
    plugin = _i18n(config)
    if plugin is None or plugin.building:
        # inneres Build einer weiteren Sprache - aufgeteilt wird erst ganz am Ende
        return
    site = Path(config.site_dir)
    standard = plugin.default_language
    weitere = [s for s in plugin.build_languages if s != standard]

    # fehlende Uebersetzungen melden
    for sprache, seiten in sorted(_ersatzseiten.items()):
        log.info(f"'{sprache}': {len(seiten)} Seite(n) ohne Uebersetzung (Ersatzseite): "
                 + ", ".join(sorted(seiten)))
    _ersatzseiten.clear()

    # 404.html je Sprache
    for sprache, inhalt in _seite_404.items():
        ziel = site / "404.html" if sprache == standard else site / sprache / "404.html"
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ziel.write_text(inhalt, encoding="utf-8")
    _seite_404.clear()

    # Suchindex je Sprache
    pfad = site / "search" / "search_index.json"
    if not weitere or not pfad.exists():
        return
    daten = json.loads(pfad.read_text(encoding="utf-8"))
    docs: dict[str, list] = {s: [] for s in [standard, *weitere]}
    for eintrag in daten.get("docs", []):
        ort = eintrag.get("location", "")
        for sprache in weitere:
            if ort == sprache or ort.startswith(sprache + "/"):
                docs[sprache].append(dict(eintrag, location=ort[len(sprache) + 1:]))
                break
        else:
            docs[standard].append(eintrag)
    for sprache, liste in docs.items():
        ziel = pfad if sprache == standard else site / sprache / "search" / "search_index.json"
        ziel.parent.mkdir(parents=True, exist_ok=True)
        inhalt = {"config": dict(daten.get("config", {}), lang=[sprache]), "docs": liste}
        # Format wie das Search-Plugin von Material (kompakt, ASCII-maskiert)
        ziel.write_text(json.dumps(inhalt, separators=(",", ":"), default=str), encoding="utf-8")
        log.info(f"Suchindex '{sprache}': {len(liste)} Eintraege -> {ziel.relative_to(site).as_posix()}")
