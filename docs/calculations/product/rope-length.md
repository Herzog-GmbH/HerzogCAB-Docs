# Produktlänge

Berechnet, wie viel fertiges Geflecht (Länge in Meter) sich aus dem auf den Spulen vorrätigen Material ergibt. So lässt sich vor dem Flechten abschätzen, welche Produktlänge eine Spulenbestückung liefert, ohne dass die Maschine leerlaufen muss.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Spule-Volumen:** | cm³ | Materialvolumen pro Spule (Garn-/Drahtvorrat einer Spule). |
| **Klöppelanzahl:** | stk. | Anzahl der mitlaufenden Klöppel (Spulen) auf der Maschine. Muss mindestens 8 betragen. |
| **Produktdurchmesser:** | mm | Durchmesser des fertigen Geflechts. |

!!! note "Gültige Eingaben"
    Damit gerechnet wird, müssen **Spule-Volumen** und **Produktdurchmesser** größer als 0 sein und die **Klöppelanzahl** mindestens 8 betragen. Ungültige Felder werden rot markiert.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Produktlänge:** | m | Aus dem gesamten Spulenvorrat erzielbare Geflechtlänge (zwei Nachkommastellen). |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

!!! note "Einheiten beachten"
    Das Volumen geht in cm³, der Produktdurchmesser in mm ein; das Ergebnis wird in Meter ausgegeben.

Die Berechnung läuft nur in eine Richtung: Die **Produktlänge** wird stets aus den drei Eingabewerten ermittelt. Ein Rückrechnen eines leeren Eingabefelds aus der Produktlänge ist nicht vorgesehen.

## Verwandte Berechnungen

* [Produktgewicht](./rope-weight.md)
* [Produktdurchmesser](./product-diameter.md)
* [Produktlänge pro Trommel](./rope-length-on-drum.md)
* [Spulen-Volumen](../bobbins/bobbin-volume.md)
