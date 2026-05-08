# Herzog CAB - Anwenderhandbuch (Quelle)

Dies ist das Quell-Repository fuer das Anwenderhandbuch von **Herzog CAB**.
Die fertige Doku wird automatisch auf GitHub Pages veroeffentlicht.

> **Live:** https://herzog-gmbh.github.io/HerzogCAB-Docs/

## Schnellstart fuer Autoren

```cmd
REM 1) Python 3.11+ installiert? Falls nein: https://www.python.org/downloads/
python --version

REM 2) Virtuelles Environment + Abhaengigkeiten
cd docs-site
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

REM 3) Lokaler Vorschau-Server (Live-Reload bei Aenderungen)
mkdocs serve

REM   -> oeffne http://127.0.0.1:8000 im Browser
```

## Projektstruktur

```
docs-site/
├── mkdocs.yml              # zentrale Konfiguration & Navigation
├── requirements.txt        # Python-Abhaengigkeiten
├── docs/                   # >>> Hier wird der Inhalt geschrieben <<<
│   ├── index.md            # Startseite
│   ├── assets/             # Logos, Bilder, Downloads
│   ├── installation/       # Kapitel "Installation"
│   ├── getting-started/     # Kapitel "Erste Schritte"
│   ├── master-data/         # ...
│   └── ...
└── .github/
    └── workflows/
        └── docs.yml        # Automatischer Build & Deploy
```

## Inhalt schreiben

* Jede Seite ist eine Markdown-Datei (`.md`) unter `docs/`.
* Die Reihenfolge in der Sidebar wird in `mkdocs.yml` unter `nav:` festgelegt.
* Bilder/Screenshots gehoeren nach `docs/assets/screenshots/<kapitel>/...`
  und werden mit `![Beschreibung](../assets/screenshots/...)` eingebunden.

## Konventionen

* **Sprachebene:** Endkunde, der Herzog CAB im Werk bedient.
  Keine Code-Begriffe (z. B. `QSettings`, `JSON`) im Fliesstext.
* **Formatierung:** Buttons in **fett** (z. B. **Speichern**), Menuepfade
  mit `>` (z. B. *Datei > Einstellungen*).
* **Hinweise:** Nutze die Admonition-Bloecke fuer Warnungen, Tipps und Hinweise:

  ```markdown
  !!! tip "Tipp"
      Wenn der Workspace auf einem Netzlaufwerk liegt, ...

  !!! warning "Achtung"
      Beim Verschieben des Workspaces muessen alle Benutzer sich neu anmelden.

  !!! info "Hinweis"
      Diese Funktion steht erst ab Version 1.3 zur Verfuegung.
  ```

## Veroeffentlichung

Push nach `main` -> GitHub Actions baut die Site -> Deploy auf `gh-pages`.
Manuell ist nichts zu tun.

## Kontakt

Bei Fragen zur Doku: e.siemering@herzog-online.com
