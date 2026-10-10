# Herzog CAB - Anwenderhandbuch (Quelle)

Dies ist das Quell-Repository fuer das Anwenderhandbuch von **Herzog CAB**.
Die fertige Doku wird automatisch auf GitHub Pages veroeffentlicht.

> **Live:** https://cab.herzog-online.com/handbuch/

## Schnellstart fuer Autoren

```cmd
REM 1) Python 3.11+ installiert? Falls nein: https://www.python.org/downloads/
python --version

REM 2) Virtuelles Environment + Abhaengigkeiten
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

REM 3) Lokaler Vorschau-Server (mkdocs.exe-Shim ist kaputt -> immer python -m mkdocs)
python -m mkdocs serve -a 127.0.0.1:8800

REM   -> oeffne http://127.0.0.1:8800 im Browser
```

## Struktur (seit Neuaufbau 07/2026)

Sieben Top-Tabs, drei Inhaltsebenen. Verbindliche Schreibregeln: **[STYLEGUIDE.md](STYLEGUIDE.md)**.

```
mkdocs.yml               # Konfiguration & Navigation (7 Tabs)
STYLEGUIDE.md            # Schreibregeln, Seiten-Schablonen, Screenshot-Konventionen
f1-mapping.json          # KANONISCH: App-Nav-Key -> Handbuch-Pfad (F1-Hilfe)
F1-MAPPING.md            # Erlaeuterung + Pflege-Regeln zum Mapping
TERMINOLOGIE.md          # Fachwoerter Deutsch <-> Englisch (verbindlich fuer beide Sprachen)
includes/                # Glossar-Tooltips je Sprache (glossar-tooltips.md / .en.md)
hooks/sprachen.py        # Zweisprachigkeit: Tooltips, "Auf dieser Seite", Suchindex und 404 je Sprache
overrides/main.html      # Theme-Erweiterung: englische Seiten suchen im englischen Index
docs/
├── index.md             # Startseite (Karten-Hub); index.en.md = englische Fassung
│                        #   (jede Seite: <seite>.md deutsch, <seite>.en.md englisch,
│                        #   Bilder: <bild>.png deutsch, <bild>.en.png englisch)
├── setup/               # TAB Loslegen: Kundenkonto, Installation, Anmeldung/Lizenz,
│                        #   CodeMeter (Dongle), Update, Deinstallation
├── basics/              # TAB Grundlagen: Bedienkonzepte (Oberflaeche, Navigation,
│                        #   Home, Favoriten, Verlauf, Berechnungsseiten-Aufbau,
│                        #   Desktop-App oder Web-App?)
├── orders/  machine-park/  hall-planner/  designer/  calculations/
│   master-data/  print-templates/  parameter-overview/
│                        # TAB Desktop-App: Referenz A-Z = F1-Zielseiten,
│                        #   Reihenfolge wie die Programm-Navigation
├── web/                 # TAB Web-App (app.herzog-cab.com): je Modul eine Seite,
│                        #   Felder werden NICHT wiederholt, sondern auf die
│                        #   Desktop-Referenz verlinkt
├── tasks/               # TAB Aufgaben & Ablaeufe: End-to-End-Workflows
├── portal/              # TAB Verwaltung, Gruppe Kundenkonto: Lizenzportal
│                        #   (license.herzog-cab.com)
├── admin/               # TAB Verwaltung: Benutzer, Rollen, Authentifizierung,
│                        #   Profile, Speicherort, Firma, Einstellungen (inkl. Lizenz/Cloud)
├── help/  appendix/     # TAB Hilfe: Problembehebung + Anhang
└── assets/              # Logos, CSS, Screenshots (je Kapitel ein Unterordner;
                         #   web/ und portal/ werden per _tools/web_screenshots.py erzeugt)
```

**Drei Ebenen, eine Regel:** Grundlagen werden verlinkt, Referenz beschreibt
jedes Feld genau einmal, Workflows (tasks/) verlinken auf beides und erklaeren
selbst keine Felder.

**Zwei Sprachen (seit 10/2026):** Deutsch ist Standard und bleibt unter
`/handbuch/...`, Englisch liegt unter `/handbuch/en/...` (Plugin
mkdocs-static-i18n). Eine englische Seite ist `<seite>.en.md` neben der
deutschen, ein englisches Bild `<bild>.en.png` neben dem deutschen; Links und
Bildpfade in der `.en.md` bleiben wie im Deutschen. Fehlt eine `.en.md`, zeigt
`/en/` die deutsche Seite (der Build meldet das). Fachwoerter: `TERMINOLOGIE.md`.

* **Sprungmarken:** Ueberschriften der `.en.md` behalten die ID der deutschen
  (`## Profile tab { #tab-profil }`), sonst springen F1 und Querverweise ins
  Leere. `python _tools/anker.py --setzen` haengt fehlende IDs an,
  `python _tools/anker.py --alle` prueft alle Seiten (so auch die CI).
* **Navigation englisch:** `_tools/nav_en.txt` pflegen, dann
  `python _tools/nav_en.py` (schreibt `nav_translations` in `mkdocs.yml`).
* Englische Screenshot-Platzhalter: `📷 Screenshot missing` mit **Subject**,
  **How to create**, **Target file** (Ziel-Datei wie im Deutschen).

## Inhalt schreiben

* Alle Regeln, Schablonen und der Screenshot-Platzhalter-Standard stehen in
  **[STYLEGUIDE.md](STYLEGUIDE.md)** - vor dem Schreiben lesen.
* Die Reihenfolge in der Navigation wird in `mkdocs.yml` unter `nav:` festgelegt.
* **Keine Berechnungsformeln** - Berechnungsseiten beschreiben nur Bedienung
  (Policy; Standardsatz siehe Styleguide).
* Beim Verschieben/Umbenennen von Seiten: `f1-mapping.json` anpassen UND
  Redirect in `mkdocs.yml` ergaenzen (alte Links/Lesezeichen).
* Offene Screenshot-Stellen findet man mit der Suche nach `Screenshot fehlt`;
  die gesammelte Liste fuer die Desktop-App steht in
  **[SCREENSHOTS-DESKTOP.md](SCREENSHOTS-DESKTOP.md)** und wird mit
  `python _tools/screenshot_liste.py` neu erzeugt (`--pruefen` meldet nur
  fehlende Felder und doppelte Ziel-Dateien).
* Web-App- und Portal-Screenshots entstehen reproduzierbar mit
  `_tools/web_screenshots.py` (Playwright, lokale Testumgebung) - siehe
  Kopf des Skripts.

## Veroeffentlichung

Push nach `main` -> GitHub Actions baut die Site (inkl. F1-Mapping-Validierung)
-> Deploy auf GitHub Pages. Manuell ist nichts zu tun.

**Achtung:** Jeder Push auf `main` geht LIVE. Groessere Umbauten auf einem
Branch vorbereiten und erst nach Sichtpruefung mergen.

## Kontakt

Bei Fragen zur Doku: e.siemering@herzog-online.com
