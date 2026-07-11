# Spulengewicht

!!! abstract "Referenz — Berechnung: Netto- und Bruttogewicht einer bespulten Spule"

## Wofür

Diese Berechnung liefert das Netto- und das Bruttogewicht einer bespulten
Spule aus Feinheit, Fachung und Wickellänge. Das Bruttogewicht (inklusive
Spulenkörper) ist z. B. für den Transport, die Lagerlogistik oder eine
Wiegekontrolle beim Wareneingang nützlich.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Material:** | – | Optionale Auswahl eines Materials aus den [Stammdaten](../../master-data/materials.md). Übernimmt die hinterlegte Feinheit automatisch. |
| **Feinheit:** | tex, dtex, den, Nr_metrisch, Nr_englisch | Feinheit des Materials mit Einheiten-Auswahl daneben. Muss mindestens 1 tex entsprechen. |
| **Fachung:** | stk. | Anzahl der gemeinsam gespulten Einzelfäden (mindestens 1, Startwert 1). |
| **Länge auf Spule:** | m | Materiallänge, die auf der Spule aufgewickelt ist. Muss größer als 0 sein. |
| **Leergewicht Spule:** | g | Optionales Gewicht der leeren Spule (Hülse/Trommel ohne Material), bis zu einer Nachkommastelle. Bleibt das Feld leer bzw. auf 0, wird nur das Nettogewicht ausgegeben. |

!!! note "Pflichtfelder"
    Länge auf Spule und Feinheit müssen größer als 0 sein (Feinheit
    mindestens 1 tex), Fachung mindestens 1. Fehlt einer dieser Werte,
    bleiben die Ergebnisfelder leer.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Nettogewicht Material:** | kg | Hauptergebnis: reines Materialgewicht ohne Spulenkörper, auf drei Nachkommastellen. |
| **Bruttogewicht (mit Spule):** | kg | Gesamtgewicht der bespulten Spule einschließlich Spulenkörper, auf drei Nachkommastellen. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten (Eingabe-Karte,
Ergebnis-Kacheln, Schaltflächen **Berechnen**/**Löschen**, Verlauf) steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md) —
hier nur die Besonderheiten dieser Seite.

Das **Leergewicht Spule** ist optional: Lassen Sie es leer bzw. auf 0,
entspricht das Bruttogewicht dem Nettogewicht.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

* [Restlänge über Gewicht](residual-length.md)
* [Materialbedarf](material-demand.md)
* [Spulenkapazität](bobbin-capacity.md)
* [Fadenspannung](yarn-tension.md)
