# Produktdurchmesser

Berechnet den Außendurchmesser des fertigen Geflechts aus den Garn- bzw. Materialeigenschaften, der Klöppelzahl, dem Flechtwinkel und dem Füllungsgrad. So lässt sich schon vor dem Flechten abschätzen, welchen Durchmesser ein geplantes Produkt erreicht – nützlich für Auslegung, Maschinenwahl und Angebotskalkulation.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Material:** | – | Optionale Auswahl eines Materials aus der [Materialdatenbank](../../master-data/materials.md). **Dichte** und **Feinheit** werden dann automatisch übernommen. |
| **Dichte:** | g/cm³ | Materialdichte (drei Nachkommastellen, max. 25). Muss größer als 0 sein. |
| **Feinheit:** | tex, dtex, den, Nr metrisch, Nr englisch | Feinheit (lineare Dichte) des Garns. Die Einheit wählen Sie im Auswahlfeld rechts daneben; intern wird der Wert nach tex umgerechnet. Mindestwert 1. |
| **Fachung:** | stk. | Anzahl der parallel geführten Fäden je Klöppel. Mindestwert 1. |
| **Klöppelanzahl:** | stk. | Anzahl der Klöppel der Flechtmaschine (max. 1500). Mindestwert 5. |
| **Flechtwinkel:** | ° | Winkel der Stränge zur Längsachse. Zulässig 5° bis 85°. |
| **Füllungsgrad:** | % | Wie dicht der theoretisch verfügbare Querschnitt mit Material gefüllt ist (1–100 %). Startwert 70 %. |

!!! tip "Material einmal pflegen, immer wieder nutzen"
    Wählen Sie oben ein Material aus der Datenbank, statt Dichte und Feinheit von Hand einzutippen. Das ist schneller und vermeidet Eingabefehler. Wie Sie Materialien anlegen, lesen Sie unter [Materialien](../../master-data/materials.md).

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Produktdurchmesser:** | mm | Berechneter Außendurchmesser des fertigen Geflechts (zwei Nachkommastellen). |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

!!! note "Vollständige Eingabe nötig"
    Es wird nur gerechnet, wenn Dichte, Feinheit, Fachung, Klöppelanzahl, Flechtwinkel und Füllungsgrad sinnvolle Werte (> 0 bzw. innerhalb der genannten Grenzen) enthalten. Fehlt ein Wert oder liegt er außerhalb des zulässigen Bereichs, wird das Feld rot markiert und es erscheint kein Ergebnis.

## Verwandte Berechnungen

* [Flechtwinkel](../braid-geometry/braid-angle.md)
* [Materialdurchmesser](../material/material-diameter.md)
* [Feinheit / Titer](../material/linear-density.md)
* [Produktgewicht](./rope-weight.md)
