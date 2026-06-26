# Anzahl Spulmaschinen

Diese Berechnung ermittelt, wie viele Spulmaschinen nötig sind, um eine Flechtmaschine kontinuierlich mit gefüllten Spulen zu versorgen. Sie verbindet die Geflechtkennzahlen (Flechtwinkel, Leistung, Maschinenlaufzeit) mit der Spulleistung der Spulmaschinen und zeigt so das Verhältnis von Flecht- zu Spulmaschinen im Schichtbetrieb.

## Eingabewerte

Die Eingaben sind in drei Bereiche gegliedert: **Flechtmaschine**, **Spulmaschine** und **Produktdaten**.

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Anzahl Schichten:** (Flechtmaschine) | – | Anzahl der Schichten im Flechtbetrieb (Auswahl 1, 2 oder 3). |
| **Anzahl Klöppel:** | stk. | Anzahl der Klöppel der Flechtmaschine (mindestens 1). |
| **Anzahl Köpfe:** | stk. | Anzahl der Flechtköpfe (mindestens 1). |
| **Flügelrad-Drehzahl:** | rpm | Drehzahl der Flügelräder (Hörnerräder) der Flechtmaschine. |
| **Anzahl Schichten:** (Spulmaschine) | – | Anzahl der Schichten im Spulbetrieb (Auswahl 1, 2 oder 3). |
| **Spulmaschinentyp:** | – | Auswahl **Halbautomat** oder **Vollautomat**. Standard: Vollautomat. |
| **Spulgeschwindigkeit:** | m/min | Geschwindigkeit, mit der die Spulmaschine das Material aufspult. |
| **Länge auf Spule:** | m | Materiallänge, die auf eine Spule gewickelt wird. |
| **Spindeln pro Spulmaschine:** | stk. | Anzahl der Spindeln (parallel bespulte Plätze) je Spulmaschine (mindestens 1). |
| **Schlaglänge:** | mm | Schlaglänge des Geflechts. |
| **Geflechtsdurchmesser:** | mm | Durchmesser des Geflechts. |

!!! note "Pflichtfelder"
    Spulgeschwindigkeit, Länge auf Spule, Schlaglänge und Geflechtsdurchmesser müssen größer als 0 sein; Anzahl Klöppel, Anzahl Köpfe und Spindeln pro Spulmaschine mindestens 1, die Flügelrad-Drehzahl größer als 0. Sind nicht alle Werte gesetzt, bleiben die Ergebnisse leer.

## Ergebnis

Hauptergebnis ist **Flechtmaschinen / Spulmaschine**; die übrigen Werte werden als Kennzahl-Kacheln ausgegeben.

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Flechtmaschinen / Spulmaschine:** | stk. | Hauptergebnis: Verhältnis von Flecht- zu Spulmaschinen (aufgerundet). |
| **Anzahl Spulen:** | stk. | Berechnete Anzahl benötigter Spulen (aufgerundet). |
| **Maschinenlaufzeit:** | h | Laufzeit der Flechtmaschine für die berechnete Geflechtlänge. |
| **Leistung:** | m/h | Flechtleistung (produzierte Geflechtlänge pro Stunde). |
| **Spulzeit:** | min | Zeit zum Bespulen einer Spule. |
| **Flechtwinkel:** | ° | Aus Schlaglänge und Geflechtsdurchmesser berechneter Flechtwinkel. |
| **Länge Geflecht:** | m | Aus Länge auf Spule und Flechtwinkel berechnete Geflechtlänge. |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

* [Materiallänge auf Spule](./material-length.md)
* [Spulvolumen](./bobbin-volume.md)
* [Flechtwinkel](../braid-geometry/braid-angle.md)
* [Schlaglänge](../braid-geometry/lay-length.md)
* [Produktionsgeschwindigkeit](../machine/production-speed.md)
* [Laufzeit eines Spulensatzes](../machine/run-time-bobbin-set.md)
