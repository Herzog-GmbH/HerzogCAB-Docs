# Hohlgeflecht – Bedeckung

Diese Berechnung ermittelt die **Bedeckung** eines Hohlgeflechts – also wie
vollständig die Oberfläche des Schlauchs/Rohrs vom Geflecht bedeckt ist (in
Prozent). So prüfen Sie, ob eine Konstellation aus Material, Klöppelzahl und
Flechtwinkel die gewünschte Dichte erreicht.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Garnart** | – | **Multifil** oder **Monofil**. Bestimmt, ob mit Materialbreite oder Materialdurchmesser gerechnet wird. |
| **Geflechtsdurchmesser** | mm | Durchmesser des Hohlgeflechts. |
| **Flechtwinkel** | ° | Flechtwinkel (kleiner 90°, Vorgabe 45). |
| **Materialbreite** / **Materialdurchmesser** | mm | Bei *Multifil* die Materialbreite, bei *Monofil* der Materialdurchmesser. |
| **Faktor Breite/Ø** | – | Verhältnis Breite zu Durchmesser (1–3, Vorgabe 1,25; nur bei *Multifil*). |
| **Klöppelanzahl** | Stück | Anzahl der Klöppel. |
| **Fachung** | Stück | Anzahl der Fäden je Klöppel (Vorgabe 1). |

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Bedeckung** | % | Bedeckungsgrad des Geflechts (1 Nachkommastelle). Werte über 100 % werden als „Bedeckung > 100 %" gekennzeichnet. |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

* [Anzahl Klöppel](tube-carriers.md)
* [Durchmesser](tube-diameter.md)
* [Materialbreite](yarn-width.md)
