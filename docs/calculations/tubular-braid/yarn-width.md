# Hohlgeflecht – Materialbreite

Die Berechnung schätzt, wie breit ein Garn (Multifil) bzw. wie groß ein Monofil/Draht sein muss, damit das Hohlgeflecht bei vorgegebenem Durchmesser, Flechtwinkel und Klöppelzahl die gewünschte **Bedeckung** erreicht. So lässt sich vor dem Flechten beurteilen, ob ein verfügbares Material zur gewünschten Mantel-Schicht passt.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Garnart** | – | Auswahl zwischen **Multifil** und **Monofil**. Bei Monofil wird der Faktor Breite/Ø ausgeblendet (intern = 1), und das Ergebnis ist der Materialdurchmesser statt der Materialbreite. |
| **Geflechtsdurchmesser** | mm | Außendurchmesser des Hohlgeflechts. |
| **Flechtwinkel** | ° | Winkel der Fäden zur Geflechtsachse (0–89°, Vorgabe 45°). |
| **Klöppelanzahl** | stk. | Anzahl der Klöppel der Flechtmaschine. |
| **Fachung** | stk. | Anzahl der parallel je Klöppel laufenden Garne (Vorgabe 1). Das Ergebnis wird auf die Breite **pro Garn** heruntergerechnet. |
| **Bedeckung** | % | Gewünschter Bedeckungsgrad der Geflechtsoberfläche (0–100 %, Vorgabe 70 %). 100 % wird intern als 99,9999 % gerechnet. |
| **Faktor Breite/Ø** | – | Verhältnis von Garnbreite zu Garndurchmesser (1,00–3,00, Vorgabe 1,25). Nur bei Multifil sichtbar; bei Monofil = 1. Dient zur Umrechnung der Breite in den Durchmesser. |

!!! note "Pflichtfelder"
    Geflechtsdurchmesser, Flechtwinkel (0 < α < 90°), Klöppelanzahl, Fachung und Bedeckung müssen größer als 0 sein. Fehlt einer dieser Werte, bleibt das Ergebnis leer.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Materialbreite (Multifil)** | mm | Benötigte Garnbreite pro Garn für die gewünschte Bedeckung. Bei Garnart **Monofil** trägt dieselbe Kachel die Bezeichnung **Materialdurchmesser**. |
| **Materialdurchmesser** | mm | Aus der Breite abgeleiteter Durchmesser. Nur bei Multifil als zusätzliche Kachel sichtbar; bei Monofil entspricht er der Hauptkennzahl. |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

!!! tip "Faktor Breite/Ø richtig wählen"
    Bei Multifil-Garnen ist die abgeplattete Breite typischerweise größer als der runde Durchmesser. Der Faktor Breite/Ø (Vorgabe 1,25) bildet dieses Verhältnis ab. Passen Sie ihn an Ihr tatsächliches Garn an, wenn der abgeleitete Materialdurchmesser realistischer werden soll.

!!! note "Bedeckung 100 %"
    Eine vollständige Bedeckung lässt sich rechnerisch nicht exakt darstellen; der Wert wird daher intern auf 99,9999 % begrenzt.

## Verwandte Berechnungen

* [Materialdurchmesser](../material/material-diameter.md)
* [Feinheit / Titer](../material/linear-density.md)
