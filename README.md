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

Sechs Top-Tabs, drei Inhaltsebenen. Verbindliche Schreibregeln: **[STYLEGUIDE.md](STYLEGUIDE.md)**.

```
mkdocs.yml               # Konfiguration & Navigation (6 Tabs)
STYLEGUIDE.md            # Schreibregeln, Seiten-Schablonen, Screenshot-Konventionen
f1-mapping.json          # KANONISCH: App-Nav-Key -> Handbuch-Pfad (F1-Hilfe)
F1-MAPPING.md            # Erlaeuterung + Pflege-Regeln zum Mapping
includes/                # zentrale Glossar-Tooltips (auto_append auf allen Seiten)
docs/
├── index.md             # Startseite (Karten-Hub)
├── setup/               # TAB Loslegen: Installation, Lizenz, Update, Deinstallation
├── basics/              # TAB Grundlagen: Bedienkonzepte (Oberflaeche, Navigation,
│                        #   Home, Favoriten, Verlauf, Berechnungsseiten-Aufbau ...)
├── orders/  machine-park/  hall-planner/  designer/  calculations/
│   master-data/  print-templates/  parameter-overview/
│                        # TAB Funktionen: Referenz A-Z = F1-Zielseiten,
│                        #   Reihenfolge wie die Programm-Navigation
├── tasks/               # TAB Aufgaben & Ablaeufe: End-to-End-Workflows
├── admin/               # TAB Verwaltung: Benutzer, Rollen, Authentifizierung,
│                        #   Profile, Speicherort, Firma, Einstellungen
├── help/  appendix/     # TAB Hilfe: Problembehebung + Anhang
└── assets/              # Logos, CSS, Screenshots (je Kapitel ein Unterordner)
```

**Drei Ebenen, eine Regel:** Grundlagen werden verlinkt, Referenz beschreibt
jedes Feld genau einmal, Workflows (tasks/) verlinken auf beides und erklaeren
selbst keine Felder.

## Inhalt schreiben

* Alle Regeln, Schablonen und der Screenshot-Platzhalter-Standard stehen in
  **[STYLEGUIDE.md](STYLEGUIDE.md)** - vor dem Schreiben lesen.
* Die Reihenfolge in der Navigation wird in `mkdocs.yml` unter `nav:` festgelegt.
* **Keine Berechnungsformeln** - Berechnungsseiten beschreiben nur Bedienung
  (Policy; Standardsatz siehe Styleguide).
* Beim Verschieben/Umbenennen von Seiten: `f1-mapping.json` anpassen UND
  Redirect in `mkdocs.yml` ergaenzen (alte Links/Lesezeichen).
* Offene Screenshot-Stellen findet man mit der Suche nach `Screenshot fehlt`.

## Veroeffentlichung

Push nach `main` -> GitHub Actions baut die Site (inkl. F1-Mapping-Validierung)
-> Deploy auf GitHub Pages. Manuell ist nichts zu tun.

**Achtung:** Jeder Push auf `main` geht LIVE. Groessere Umbauten auf einem
Branch vorbereiten und erst nach Sichtpruefung mergen.

## Kontakt

Bei Fragen zur Doku: e.siemering@herzog-online.com
