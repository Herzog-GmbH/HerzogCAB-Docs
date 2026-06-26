# Produktgewicht

Berechnet das Gesamtgewicht eines geflochtenen Produkts (Seil, Litze, Schlauch) aus der Materialfeinheit, der Klöppelanzahl, dem Flechtwinkel und der Produktlänge. So lässt sich vor der Produktion abschätzen, wie viel Material ein Auftrag benötigt und wie schwer das fertige Produkt wird.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Feinheit** | tex, dtex, den, Nr_metrisch, Nr_englisch | Lineare Dichte des verwendeten Garns/Fadens. Die Einheit wählen Sie im Auswahlfeld rechts daneben (Standard: tex). Für die Berechnung wird der Wert intern nach tex umgerechnet. |
| **Klöppelanzahl** | stk. | Anzahl der mitflechtenden Klöppel (= Anzahl der Einzelfäden im Geflecht). |
| **Flechtwinkel** | ° | Winkel, unter dem die Fäden zur Produktachse verlaufen. |
| **Produktlänge** | m | Länge des fertigen Produkts, für das das Gewicht berechnet wird. |

!!! note "Gültige Eingabebereiche"
    Die Eingaben werden vor der Berechnung geprüft. Es gelten: Klöppelanzahl ≥ 8, Flechtwinkel ≥ 4°, Feinheit ≥ 1 und Produktlänge > 0. Wird eine Grenze unterschritten, markiert das Programm das betroffene Feld rot und rechnet nicht.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Produktgewicht** | kg | Gesamtgewicht des Produkts über die angegebene Produktlänge. |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

!!! tip "Flechtwinkel beeinflusst das Gewicht spürbar"
    Je flacher der Flechtwinkel (kleinerer Wert), desto höher das Produktgewicht. Achten Sie daher auf einen realistischen, zur Maschine passenden Flechtwinkel.

## Verwandte Berechnungen

* [Feinheit / Titer](../material/linear-density.md)
* [Materialdurchmesser](../material/material-diameter.md)
* [Materialien](../../master-data/materials.md) – Feinheit (Titer) je Material zentral pflegen und in die Berechnung übernehmen.
