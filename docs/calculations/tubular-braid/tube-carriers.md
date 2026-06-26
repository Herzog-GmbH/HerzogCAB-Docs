# Hohlgeflecht – Anzahl Klöppel

Diese Berechnung ermittelt für ein Hohlgeflecht (Schlauchgeflecht) die benötigte **Anzahl Klöppel** aus Geflechtsdurchmesser, Flechtwinkel, Materialbreite und gewünschter Bedeckung. So legen Sie schon bei der Auftragsvorbereitung fest, mit wie vielen Klöppeln eine Flechtmaschine bestückt werden muss, um die geforderte Geometrie und Deckung zu erreichen.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Garnart** | – | Auswahl zwischen *Multifil* und *Monofil*. Bei *Monofil* entfällt der Faktor Breite/Ø (intern = 1), und das Breitenfeld heißt **Materialdurchmesser**. |
| **Geflechtsdurchmesser** | mm | Außendurchmesser des fertigen Hohlgeflechts. |
| **Flechtwinkel** | ° | Winkel der Fäden zur Geflechtsachse. Zulässig größer 0° und kleiner 90° (Vorgabe 45°). |
| **Materialbreite** bzw. **Materialdurchmesser** | mm | Bei *Multifil* die abgeflachte Breite des Garns, bei *Monofil* der Materialdurchmesser. |
| **Faktor Breite/Ø** | – | Verhältnis Breite zu Durchmesser des Garns (1,0 – 3,0; Vorgabe 1,25). Nur bei *Multifil* sichtbar; bei *Monofil* fest 1,0. |
| **Fachung** | stk. | Anzahl der parallel laufenden Fäden je Klöppel (Vorgabe 1). |
| **Bedeckung** | % | Gewünschter Bedeckungsgrad der Geflechtsoberfläche (Vorgabe 70 %). |

!!! note "Anzeigefeld Materialdurchmesser"
    Bei *Multifil* zeigt das Feld **Materialdurchmesser** den aus Materialbreite
    und Faktor Breite/Ø abgeleiteten Materialdurchmesser an. Es
    ist ein reines Anzeigefeld und kann nicht bearbeitet werden. Bei *Monofil*
    wird es ausgeblendet, da Breite und Durchmesser hier identisch sind.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Anzahl Klöppel** | stk. | Erforderliche Klöppelzahl, **aufgerundet auf das nächste Vielfache von 4**. |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

Das Ergebnis wird zum Schluss auf das nächste **Vielfache von 4** aufgerundet (z. B. wird aus 18 → 20). Ergibt sich kein sinnvoller positiver Wert, bleibt das Feld leer.

!!! note "Bedeckung 100 %"
    Eine Bedeckung von genau 100 % ist rechnerisch nicht lösbar und wird
    intern auf 99,9999 % begrenzt, damit ein Ergebnis ausgegeben werden kann.

!!! tip "Vielfaches von 4"
    Klöppel laufen in Vierergruppen (gleich viele links- und rechtsgängige
    Träger). Deshalb rundet die Software immer auf das nächste Vielfache von 4
    auf – die ausgegebene Zahl ist direkt maschinentauglich.

Die Berechnung ist **nicht umkehrbar**: Die Anzahl Klöppel ist stets das Ergebnis, alle übrigen Felder sind Eingaben. Sobald eine Pflichtangabe fehlt oder unzulässig ist (Durchmesser ≤ 0, Winkel außerhalb 0–90°, Fachung ≤ 0, Bedeckung ≤ 0 oder wirksamer Materialdurchmesser ≤ 0), bleibt das Ergebnis leer.

## Verwandte Berechnungen

* [Hohlgeflecht – Durchmesser](./tube-diameter.md)
* [Materialdurchmesser](../material/material-diameter.md)
* [Feinheit / Titer](../material/linear-density.md)
