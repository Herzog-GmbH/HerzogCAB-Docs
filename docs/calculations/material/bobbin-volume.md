# Spulvolumen

Berechnet das Wickelvolumen einer Spule aus ihrer Geometrie. Das Ergebnis hilft im Flecht-Alltag abzuschätzen, wie viel Material auf eine Spule passt und ob die gewählte Spule für ein Garn ausreicht.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Außendurchmesser** | mm | Maximaler Durchmesser der vollen Spule (über dem aufgewickelten Material). |
| **Kerndurchmesser** | mm | Durchmesser des Spulenkerns (Wickelkörper ohne Material). |
| **Wickellänge** | mm | Länge der nutzbaren Wickelfläche zwischen den Flanschen. |

!!! note "Alle Eingaben in Millimeter"
    Außendurchmesser, Kerndurchmesser und Wickellänge werden in Millimetern erfasst. Alle drei Werte müssen größer als 0 sein.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Spule-Volumen** | ccm (cm³) | Volumen des Wickelraums, also der Hohlraum zwischen Kern und Außendurchmesser über die Wickellänge. Anzeige mit zwei Nachkommastellen. |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

* [Feinheit / Titer](../material/linear-density.md)
* [Materialdurchmesser](../material/material-diameter.md)
* [Produktgewicht](../product/rope-weight.md)
