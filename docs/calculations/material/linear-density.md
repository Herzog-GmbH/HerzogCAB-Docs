# Feinheit / Titer

!!! abstract "Referenz — Berechnung: benötigte Garnfeinheit für ein gewünschtes Geflecht"

## Wofür

Diese Berechnung ermittelt die **Feinheit (Titer) eines Einzelfadens**, die
nötig ist, um ein Geflecht mit den gewünschten geometrischen Eigenschaften zu
erzeugen. Aus Produktdurchmesser, Flechtwinkel, Klöppelanzahl, Füllungsgrad
und Materialdichte wird die lineare Dichte je Träger berechnet – praktisch,
um vor der Produktion das passende Garn bzw. den passenden Draht auszuwählen.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Material:** | – | Optionale Auswahl eines Materials aus den [Stammdaten](../../master-data/materials.md). Übernimmt die hinterlegte **Dichte** automatisch in das Feld *Dichte*. |
| **Dichte:** | g/cm³ | Materialdichte (bis 3 Nachkommastellen, max. 25). Muss größer als 0 sein. |
| **Feinheit:** | tex, dtex, den, Nr_metrisch, Nr_englisch | Auswahl der Einheit, in der das Ergebnis ausgegeben wird. Die Ergebnis-Einheit folgt automatisch dieser Auswahl. |
| **Flechtwinkel:** | ° | Flechtwinkel des Produkts (max. 85°). Muss mindestens 5° betragen. |
| **Produktdurchmesser:** | mm | Außendurchmesser des fertigen Geflechts. Muss größer als 0 sein. |
| **Klöppelanzahl:** | stk. | Anzahl der Klöppel/Träger (max. 1500). Muss mindestens 8 betragen. |
| **Füllungsgrad:** | % | Gewünschter Bedeckungs-/Füllungsgrad der Oberfläche (max. 100 %, Startwert 70 %). Muss mindestens 1 % betragen. |

!!! tip "Material aus den Stammdaten übernehmen"
    Wählen Sie oben ein Material aus, wird die **Dichte** automatisch eingetragen. So vermeiden Sie Tippfehler und arbeiten immer mit denselben gepflegten Werten.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Feinheit:** | folgt der Auswahl *Feinheit* (tex, dtex, den, Nr_metrisch, Nr_englisch) | Berechnete Feinheit (Titer) je Einzelfaden/Träger, auf 2 Nachkommastellen. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md).

Diese Berechnung läuft nur in eine Richtung – aus den Eingaben wird die
Feinheit ermittelt; einzelne Eingabefelder werden nicht rückwärts aus dem
Ergebnis berechnet. Es wird nur gerechnet, wenn Dichte, Füllungsgrad,
Klöppelanzahl, Flechtwinkel und Produktdurchmesser positiv ausgefüllt sind.
Fehlt ein Wert, bleibt das Ergebnisfeld leer. Werte außerhalb der genannten
Grenzen (z. B. Klöppelanzahl unter 8 oder Flechtwinkel unter 5°) werden rot
markiert.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

- [Feinheit umrechnen](linear-density-conversion.md)
- [Materialdurchmesser über Material](material-diameter.md)
- [Materialdurchmesser über Produkt](material-diameter-product.md)
- [Flechtwinkel](../product/braid-angle.md)
- [Produktgewicht](../product/rope-weight.md)
