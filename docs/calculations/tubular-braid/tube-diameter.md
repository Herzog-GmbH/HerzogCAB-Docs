# Hohlgeflecht – Durchmesser

Diese Berechnung ermittelt den **Geflechtsdurchmesser** eines Hohlgeflechts (Schlauch- bzw. Rundgeflecht) aus Flechtwinkel, Material, Klöppelanzahl, Fachung und gewünschter Bedeckung. So lässt sich vorab abschätzen, welchen Durchmesser ein Geflecht mit einer geplanten Konfiguration annimmt.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Garnart:** | – | Umschalter **Multifil** / **Monofil**. Multifil (z. B. Garn) legt sich flach ab und wird über den Faktor Breite/Ø beschrieben; Monofil (Draht, rund) hat Durchmesser = Breite. |
| **Flechtwinkel:** | ° | Flechtwinkel des Geflechts. Zulässig größer 0 und kleiner 90; Standard 45. |
| **Materialbreite:** *(Multifil)* bzw. **Materialdurchmesser:** *(Monofil)* | mm | Bei Multifil die abgelegte Breite des Materials, bei Monofil direkt der Materialdurchmesser. Das Label wechselt je nach Garnart. |
| **Faktor Breite/Ø:** | – | Nur bei **Multifil** sichtbar. Verhältnis von Materialbreite zu Materialdurchmesser (Bereich 1,0 bis 3,0; Standard 1,25). Bei Monofil fest 1,0 und ausgeblendet. |
| **Klöppelanzahl:** | stk. | Anzahl der Klöppel (Fäden) im Geflecht. Muss größer 0 sein. |
| **Fachung:** | stk. | Anzahl der je Klöppel zusammengefassten Fäden. Standard 1; muss größer 0 sein. |
| **Bedeckung:** | % | Gewünschte Bedeckung der Geflechtsoberfläche (0 bis 100 %; Standard 70 %). |

!!! note "Materialdurchmesser als Info-Zeile"
    Bei Multifil zeigt eine zusätzliche, schreibgeschützte Zeile **Materialdurchmesser:** den aus Materialbreite und Faktor abgeleiteten Durchmesser an. Bei Monofil entfällt diese Zeile, da Durchmesser und Breite identisch sind.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Geflechtsdurchmesser** | mm | Berechneter (Außen-)Durchmesser des Hohlgeflechts für die eingegebene Konfiguration. |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

!!! note "Pflichteingaben"
    Ein Ergebnis wird nur ausgegeben, wenn Flechtwinkel (zwischen 0 und 90°), Fachung, Bedeckung, Klöppelanzahl und der Materialdurchmesser jeweils größer 0 sind. Fehlende oder ungültige Werte werden im Feld rot markiert.

!!! tip "Wirkung der Bedeckung"
    Eine höhere Bedeckung führt bei sonst gleichen Werten zu einem kleineren Geflechtsdurchmesser. Über den Flechtwinkel und die Klöppelanzahl steuern Sie zusätzlich, wie dicht und wie groß das Geflecht ausfällt.

## Verwandte Berechnungen

* [Hohlgeflecht – Bedeckung](./tube-cover.md)
* [Flechtwinkel](../braid-geometry/braid-angle.md)
* [Materialdurchmesser](../material/material-diameter.md)
