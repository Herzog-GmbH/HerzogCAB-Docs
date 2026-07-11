# Spulzeit

!!! abstract "Referenz — Berechnung: Dauer für eine Spule und für einen ganzen Spulposten"

## Wofür

Diese Berechnung ermittelt, wie lange das Bespulen einer einzelnen Spule
dauert und wie lange ein ganzer Posten mit mehreren gleichartigen Spulen
braucht. Sie hilft bei der Zeitplanung in der Spulerei — etwa um
abzuschätzen, wann ein Spulauftrag fertig ist, oder um die Auslastung einer
Spulmaschine über eine Schicht einzuschätzen.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Länge auf Spule:** | m | Materiallänge, die auf eine Spule aufgespult wird. Muss größer als 0 sein. |
| **Spulgeschwindigkeit:** | m/min | Geschwindigkeit, mit der die Spulmaschine das Material aufspult. Muss größer als 0 sein. |
| **Anzahl Spulen:** | stk. | Anzahl der Spulen im Posten (mindestens 1, Startwert 1). |
| **Spulenwechselzeit:** | min | Optionale Zeit für Spulenwechsel und Rüsten zwischen zwei Spulen. Bleibt das Feld leer bzw. auf 0, rechnet Herzog CAB ohne Wechselzeit. |

!!! note "Pflichtfelder"
    Länge auf Spule und Spulgeschwindigkeit müssen größer als 0 sein, die
    Anzahl Spulen mindestens 1. Fehlt einer dieser Werte, bleiben die
    Ergebnisfelder leer.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Spulzeit pro Spule:** | min | Hauptergebnis: reine Spulzeit einer Spule (ohne Wechselzeit), auf zwei Nachkommastellen. |
| **Gesamtzeit:** | h | Zeit für den kompletten Posten inkl. Spulenwechsel, auf zwei Nachkommastellen. |
| **Spulen pro Stunde:** | stk. | Durchsatz der Spulmaschine bei laufendem Wechsel, auf eine Nachkommastelle. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten (Eingabe-Karte,
Ergebnis-Kacheln, Schaltflächen **Berechnen**/**Löschen**, Verlauf) steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md) —
hier nur die Besonderheiten dieser Seite.

Die **Spulenwechselzeit** ist optional: Lassen Sie das Feld leer oder auf 0,
rechnet Herzog CAB die Gesamtzeit und den Durchsatz ohne
Rüst-/Wechselanteil, allein aus Spulzeit und Anzahl Spulen.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

* [Fadengeschwindigkeit](line-speed.md)
* [Spulenkapazität](bobbin-capacity.md)
* [Anzahl Spulmaschinen](number-of-winders.md)
* [Materialbedarf](material-demand.md)
