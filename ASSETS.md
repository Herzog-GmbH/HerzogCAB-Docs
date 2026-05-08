# Bilder fuer die Doku

Hier liegen Logos, Favicons und Screenshots fuer die Dokumentation.

## Struktur

```
assets/
├── logo.png                Logo fuer den Header (helles Theme)
├── logo-dark.png           Logo fuer dunkles Theme (optional)
├── favicon.png             Browser-Tab-Icon
└── screenshots/
    ├── installation/
    ├── erste-schritte/
    ├── stammdaten/
    └── ...
```

## Konventionen

- **Format:** PNG (Lossless), 1x oder 2x Aufloesung
- **Groesse:** Maximal 1600 px Breite (wird im Browser skaliert)
- **Dateinamen:** Kleinbuchstaben, Bindestriche, sprechend
  (z. B. `materialeditor-leer.png`, nicht `image001.png`)
- **Pfad in Markdown:** `![Beschreibung](../assets/screenshots/<kapitel>/<datei>.png)`

## Logos (aktueller Stand)

`logo.png` und `favicon.png` sind aktuell mit `Resources/logos/trans_logo.png`
aus der Hauptanwendung als Platzhalter befuellt.

Empfehlung fuer die finale Version (analog zur Webseite herzog-online.com):

* **Logo:** das offizielle Herzog-Wortmarken-Logo
  (`https://herzog-online.com/cms/wp-content/uploads/2020/06/HERZOG_440.png`).
  Einfach herunterladen und hier als `logo.png` ablegen, oder eine
  Variante mit dem Zusatz "CAB" fuer die Doku verwenden.
* **Favicon:** quadratisches PNG, mind. 32x32 px, am besten mit dem
  blau-gelben Akzent-Streifen aus dem Header.

## Brand-Farben (entsprechend Webseite)

| Token              | Hex      |
|--------------------|----------|
| Primary            | #00459a  |
| Primary dunkel     | #003470  |
| Primary hell       | #1a5db0  |
| Accent (Gelb)      | #ffb800  |
| Hintergrund dunkel | #0b1a33  |

Alle Farben sind in `css/herzog-brand.css` als CSS-Variablen
definiert und werden vom Material-Theme uebernommen.
