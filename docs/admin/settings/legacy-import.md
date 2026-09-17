# Design: Designer-Vorgaben und Legacy-Designimport

!!! abstract "Referenz — Tab „Design" des Einstellungen-Dialogs: Startwerte für neue Designs, Ansicht, Animation und Speichern im Designer sowie der Import von Designdateien aus alten Herzog-CAB-Versionen."

## Wofür Sie diesen Bereich nutzen

Der Tab **Design** (*Datei > Einstellungen*) bündelt alles, was das
Verhalten des [Designers](../../designer/index.md) programmweit steuert —
mit welchen Werten ein neues Design startet, ob sich der Designer die
letzte Ansicht merkt, wie schnell die Gangbahn-Animation läuft und was beim
Schließen eines ungespeicherten Designs passiert. Ganz unten liegt die Karte
**Legacy-Designimport** für Altdaten.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Tab „Design" des Einstellungen-Dialogs mit den Karten
    „Vorgaben für neue Designs", „Vorschau & Ansicht", „Animation",
    „Speichern" und „Legacy-Designimport".
    **So erzeugen:** *Datei > Einstellungen*, Tab **Design**, Dialog so hoch
    ziehen, dass alle fünf Karten sichtbar sind.
    **Ziel-Datei:** `assets/screenshots/settings/einstellungen-design.png`

## Bedienelemente im Detail

### Vorgaben für neue Designs

Startwerte für jedes neu angelegte Design (**Neu** im Designer). Bestehende
Designs bleiben unverändert.

| Einstellung | Bedeutung | Werte / Standard |
|---|---|---|
| **Geflechtsart** | Geflechtsart, mit der ein neues Design startet. | Rundgeflecht (Standard), Litze (flach), Quadratgeflecht, Spiralgeflecht, Packungsgeflecht, Soutachegeflecht |
| **Klöppelzahl** | Klöppelzahl des neuen Designs. Die zulässigen Werte richten sich nach der gewählten Geflechtsart — beim Tippen springt das Feld auf die nächste erlaubte Zahl. | Standard 16 |
| **Flechtwinkel** | Start-Flechtwinkel. | 20–80 °, Standard 45 ° |
| **Bedeckung** | Start-Bedeckung. | 0–100 %, Standard 70 % |

### Vorschau & Ansicht

| Einstellung | Wirkung |
|---|---|
| **Zuletzt genutzte Ansicht merken** | Ist die Option aktiv (Standard), merkt sich der Designer je Geflechtsart die zuletzt gewählte Ansicht (Voll, Halb, Zylinder/Vierkant/Kante samt Drehwinkel oder 3D) und stellt sie beim nächsten Start wieder her. Ohne die Option startet jede Geflechtsart in der vollen Abwicklung; die gemerkten Werte bleiben erhalten. |
| **Maßzeile in der Vorschau anzeigen (Material-Ø, Bedeckung, Geflechts-Ø)** | Blendet die Maßzeile in der Titelleiste der Vorschau ein oder aus (Standard: ein). Die Änderung wirkt beim nächsten Neuzeichnen, z. B. beim Wechsel des Design-Fensters. |

### Animation

Gilt für die [Gangbahn-Animation](../../designer/animation.md) in der
Besetzungsübersicht.

| Einstellung | Wirkung |
|---|---|
| **Geschwindigkeit** | Abspielgeschwindigkeit als Faktor (0,25 × bis 16 ×, Standard 8 ×). Die Tempo-Schaltflächen im Designer schreiben den zuletzt genutzten Wert hierher zurück. |
| **Animation automatisch starten** | Startet die Animation beim Öffnen eines Designs von selbst (Standard: aus). |

### Speichern

| Einstellung | Wirkung |
|---|---|
| **Ungespeicherte Änderungen** | Verhalten beim Schließen eines Designs mit ungespeicherten Änderungen: **Nachfragen** (Standard) zeigt die Sicherheitsabfrage; **Automatisch speichern** speichert ohne Rückfrage — nur bei noch nie gespeicherten Designs wird der Zielordner erfragt. |

### Legacy-Designimport

Mit dieser Karte übernehmen Sie Designdateien aus dem **alten
Herzog-CAB-Format** (als einzelne JSON-Dateien gespeicherte Designs, z. B.
aus früheren Programmversionen oder aus dem alten GFL-Bestand exportiert) in
die Design-Bibliothek des aktuellen Arbeitsbereichs.

!!! warning "Berechtigung erforderlich"
    Der Import erfordert das Recht **Workspace-Einstellungen**.

| Element | Beschreibung |
|---|---|
| **Import** — **JSON importieren...** | Öffnet die Dateiauswahl *Legacy-JSON-Dateien auswählen* (Filter *JSON (\*.json)*). Es können **mehrere Dateien auf einmal** ausgewählt werden. |

So läuft der Import ab:

1. *Datei > Einstellungen*, Tab **Design** öffnen.
2. Auf **JSON importieren...** klicken und eine oder mehrere Altdateien
   auswählen.
3. Herzog CAB prüft jede Datei und legt die gültigen Designs als Produkte im
   Ordner **Products/Import** des aktiven Arbeitsbereichs ab — Sie finden sie
   anschließend in der Design-Bibliothek im Ordner *Import*.
4. Zum Abschluss meldet der Dialog *Altdaten-Import* das Ergebnis, z. B.
   *„3 Datei(en) erfolgreich importiert."* Nicht lesbare oder ungültige
   Dateien werden namentlich unter *Fehlgeschlagen:* aufgeführt.

!!! tip "Nach dem Import prüfen"
    Öffnen Sie die importierten Designs einmal im
    [Designer](../../designer/index.md) und kontrollieren Sie Besetzung und
    Farben — Altdaten können unvollständige Angaben enthalten; fehlende
    Namen erscheinen als *Altdaten-Import*.

## Verwandte Seiten

* [Einstellungen (Dialog)](index.md) — Überblick über alle Tabs
* [Designer](../../designer/index.md) — wo die Vorgaben wirken
* [Geflechtsart und Parameter](../../designer/parameters.md) — zulässige Klöppelzahlen je Geflechtsart
* [Stammdaten: Designs](../../master-data/designs.md) — die Design-Bibliothek
