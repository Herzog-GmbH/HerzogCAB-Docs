# Legacy-Designimport

!!! abstract "Referenz — Tab „Design" des Einstellungen-Dialogs: Designdateien aus alten Herzog-CAB-Versionen übernehmen."

## Wofür Sie diesen Bereich nutzen

Der Tab **Design** (*Datei > Einstellungen*) enthält die Karte
**Legacy-Designimport**. Damit übernehmen Sie Designdateien aus dem **alten
Herzog-CAB-Format** (als einzelne JSON-Dateien gespeicherte Designs, z. B.
aus früheren Programmversionen oder aus dem alten GFL-Bestand exportiert) in
die Design-Bibliothek des aktuellen Arbeitsbereichs.

!!! warning "Berechtigung erforderlich"
    Der Import erfordert das Recht **Workspace-Einstellungen**.

## Bedienelemente im Detail

| Element | Beschreibung |
|---|---|
| **Import** — **JSON importieren...** | Öffnet die Dateiauswahl *Legacy-JSON-Dateien auswählen* (Filter *JSON (\*.json)*). Es können **mehrere Dateien auf einmal** ausgewählt werden. |

## So läuft der Import ab

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
* [Designer](../../designer/index.md) — importierte Designs weiterbearbeiten
* [Stammdaten: Designs](../../master-data/designs.md) — die Design-Bibliothek
