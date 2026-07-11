# Fadengeschwindigkeit

!!! abstract "Referenz — Berechnung: Umrechnung zwischen Spindeldrehzahl und Fadengeschwindigkeit"

## Wofür

Diese Berechnung rechnet zwischen der Spindeldrehzahl einer Spulmaschine und
der tatsächlichen Fadengeschwindigkeit am Wickelkörper um. Weil sich der
Wickeldurchmesser während des Spulens laufend ändert, gehört zu jeder
Drehzahl eine andere Fadengeschwindigkeit — praktisch, um die Spulmaschine
auf eine gewünschte Fadenspannung einzustellen oder umgekehrt die passende
Drehzahl für einen bestimmten Wickeldurchmesser zu ermitteln.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Berechnung:** | – | Richtung der Umrechnung: *Fadengeschwindigkeit aus Drehzahl* oder *Drehzahl aus Fadengeschwindigkeit*. Steuert, welche der beiden folgenden Eingaben angezeigt wird. |
| **Spindeldrehzahl:** | rpm | Nur bei Richtung *Fadengeschwindigkeit aus Drehzahl* sichtbar. Drehzahl der Spulspindel (mindestens 1, max. 100.000 rpm). |
| **Fadengeschwindigkeit:** | m/min | Nur bei Richtung *Drehzahl aus Fadengeschwindigkeit* sichtbar. Gewünschte Geschwindigkeit des Fadens am Wickelkörper. Muss größer als 0 sein. |
| **Wickeldurchmesser:** | mm | Aktueller Durchmesser des Wickelkörpers (leere Spule bis volle Spule). Muss größer als 0 sein (max. 5000 mm). |

!!! note "Pflichtfelder"
    Der Wickeldurchmesser muss immer größer als 0 sein. Je nach gewählter
    Richtung muss zusätzlich die Spindeldrehzahl mindestens 1 rpm bzw. die
    Fadengeschwindigkeit größer als 0 sein.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Fadengeschwindigkeit:** | m/min | Nur bei Richtung *Fadengeschwindigkeit aus Drehzahl* sichtbar. Berechnete Fadengeschwindigkeit, auf zwei Nachkommastellen. |
| **Spindeldrehzahl:** | rpm | Nur bei Richtung *Drehzahl aus Fadengeschwindigkeit* sichtbar. Berechnete Drehzahl, ganzzahlig. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten (Eingabe-Karte,
Ergebnis-Kacheln, Schaltflächen **Berechnen**/**Löschen**, Verlauf) steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md) —
hier nur die Besonderheiten dieser Seite.

Die Auswahl unter **Berechnung:** blendet jeweils nur das passende
Eingabefeld und die passende Ergebnis-Kachel ein: Bei *Fadengeschwindigkeit
aus Drehzahl* geben Sie die Spindeldrehzahl vor und erhalten die
Fadengeschwindigkeit; bei *Drehzahl aus Fadengeschwindigkeit* ist es
umgekehrt. Der Wickeldurchmesser wird in beiden Richtungen benötigt.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

* [Spulzeit](winding-time.md)
* [Fadenspannung](yarn-tension.md)
* [Spulenkapazität](bobbin-capacity.md)
