# Spulvolumen

!!! abstract "Referenz — Berechnung: Wickelvolumen einer Spule aus ihrer Geometrie"

## Wofür

Berechnet das Wickelvolumen einer Spule aus ihrer Geometrie. Das Ergebnis
hilft im Flecht-Alltag abzuschätzen, wie viel Material auf eine Spule passt
und ob die gewählte Spule für ein Garn ausreicht.

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

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md). Diese
Seite hat darüber hinaus keine Besonderheiten – drei Maße, ein Ergebnis.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

- [Materiallänge auf Spule](material-length.md)
- [Feinheit / Titer](linear-density.md)
- [Materialdurchmesser über Material](material-diameter.md)
- [Produktgewicht](../product/rope-weight.md)
