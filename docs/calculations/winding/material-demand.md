# Materialbedarf

!!! abstract "Referenz — Berechnung: Gesamter Materialbedarf für einen Spulposten"

## Wofür

Diese Berechnung ermittelt den gesamten Materialbedarf für einen Spulposten
aus mehreren gleich langen Spulen, inklusive eines Verschnitt- oder
Reservezuschlags. Ist zusätzlich eine Feinheit angegeben, wird daraus auch
gleich das Gesamtgewicht berechnet — praktisch für die Materialbestellung
vor einem größeren Spulauftrag.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Anzahl Spulen:** | stk. | Anzahl der Spulen im Posten. Muss mindestens 1 sein. |
| **Länge pro Spule:** | m | Materiallänge je Spule. Muss größer als 0 sein. |
| **Verschnitt/Reserve:** | % | Optionaler prozentualer Zuschlag für Verschnitt, Anspulverluste oder Reserve, bis zu einer Nachkommastelle. Bleibt das Feld auf 0, wird ohne Zuschlag gerechnet. |
| **Material:** | – | Optionale Auswahl eines Materials aus den [Stammdaten](../../master-data/materials.md); nur für das Gesamtgewicht relevant. Übernimmt die hinterlegte Feinheit automatisch. |
| **Feinheit:** | tex, dtex, den, Nr_metrisch, Nr_englisch | Optional, nur fürs Gesamtgewicht. Feinheit des Materials mit Einheiten-Auswahl daneben. |
| **Fachung:** | stk. | Anzahl der gemeinsam gespulten Einzelfäden (mindestens 1, Startwert 1). Nur relevant, wenn eine Feinheit angegeben ist. |

!!! note "Pflichtfelder"
    Anzahl Spulen (mindestens 1) und Länge pro Spule (größer als 0) sind
    Pflicht. Material und Feinheit sind optional — ohne Feinheit bleibt nur
    das Gesamtgewicht leer, Gesamtlänge und Reserve werden trotzdem
    berechnet.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Gesamtlänge (inkl. Reserve):** | m | Hauptergebnis: Summe aus allen Spulen zuzüglich Verschnitt/Reserve, ganzzahlig. |
| **Gesamtgewicht:** | kg | Nur sichtbar, wenn eine Feinheit angegeben ist. Gewicht der Gesamtlänge, auf zwei Nachkommastellen. |
| **davon Reserve:** | m | Anteil der Gesamtlänge, der auf den Verschnitt-/Reservezuschlag entfällt, ganzzahlig. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten (Eingabe-Karte,
Ergebnis-Kacheln, Schaltflächen **Berechnen**/**Löschen**, Verlauf) steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md) —
hier nur die Besonderheiten dieser Seite.

**Material** und **Feinheit** sind bewusst optional: Ohne Angabe liefert die
Berechnung nur die Gesamtlänge und die Reservemenge; mit Feinheit kommt das
Gesamtgewicht hinzu.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

* [Spulen aus Liefergebinde](from-supplier-spool.md)
* [Spulengewicht](bobbin-weight.md)
* [Spulzeit](winding-time.md)
