# Produktlänge pro Trommel

!!! abstract "Referenz — Berechnung: aufwickelbare Produktlänge auf eine Trommel"

## Wofür

Diese Berechnung ermittelt, wie viel Produkt (Seil, Litze, Geflecht) auf
eine Trommel aufgewickelt werden kann. Aus der Trommelgeometrie und dem
Produktdurchmesser wird die gesamte aufgewickelte Länge in Metern bestimmt –
nützlich für die Planung von Trommelgrößen, Liefermengen und
Wickelaufträgen.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Außendurchmesser:** | mm | Durchmesser des fertig bewickelten Wickelpakets (äußere Lage). |
| **Kerndurchmesser:** | mm | Durchmesser des Trommelkerns, auf dem die erste Lage aufliegt. |
| **Wickellänge:** | mm | Nutzbare Breite der Trommel, über die das Produkt gewickelt wird. |
| **Produktdurchmesser:** | mm | Durchmesser eines einzelnen aufgewickelten Stranges (auf vier Nachkommastellen genau). |
| **Fachung:** | stk. | Anzahl der nebeneinander gemeinsam aufgewickelten Stränge. |

!!! note "Pflichtangaben"
    Alle fünf Felder müssen größer als null sein, die Fachung mindestens **1 stk.** Fehlende oder ungültige Eingaben werden rot markiert; ohne vollständige Werte bleibt das Ergebnis leer.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Produktlänge:** | m | Gesamte aufgewickelte Produktlänge, die unter den angegebenen Maßen auf die Trommel passt. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md).

Werden mehrere Stränge gleichzeitig nebeneinander aufgewickelt (Fachung > 1),
teilt sich die verfügbare Wickelbreite auf alle Stränge auf – die Länge pro
Strang sinkt entsprechend.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

- [Produktgewicht](rope-weight.md)
- [Materialdurchmesser über Material](../material/material-diameter.md)
- [Produktlänge](rope-length.md)
