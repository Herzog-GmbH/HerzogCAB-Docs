# Wechselräder Gummibandkette

Diese Berechnung ermittelt die passende Wechselrad-Kombination für die Gummibandkette des Abzugs. Aus der gewünschten Dehnung, dem Durchmesser der Abzugsscheibe und der Übersetzung berechnet die Software die beiden Zähnezahlen, mit denen Sie die Maschine bestücken – so erreichen Sie im Flechtbetrieb die gewünschte Verlegelänge bzw. den geplanten Vorschub.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Bandkettentype:** | – | Auswahl der eingesetzten Bandkette: *Kleine Bandkette K70* oder *Große Bandkette*. Die Auswahl legt die festen Kettenkennwerte fest. |
| **Dehnung:** | % | Gewünschte Dehnung. Darf 0 sein; Maximalwert 1500 %. |
| **Durchmesser Abzugsscheibe:** | mm | Durchmesser der Abzugsscheibe. Pflichtfeld, muss größer als 0 sein. |
| **Übersetzung Abzugsscheibe-Bandkette:** | – | Übersetzungsverhältnis zwischen Abzugsscheibe und Bandkette. Pflichtfeld, muss größer als 0 sein; Maximalwert 1500. |

!!! note "Pflichtfelder"
    **Durchmesser Abzugsscheibe** und **Übersetzung Abzugsscheibe-Bandkette** müssen beide größer als 0 sein, da durch diese Werte geteilt wird. Fehlt einer der beiden Werte, wird das Feld rot markiert und es erfolgt keine Berechnung. Die **Dehnung** darf dagegen 0 betragen.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Zähnezahl Wechselrad 1:** | stk. | Zähnezahl des ersten Wechselrads (ganzzahlig). |
| **Zähnezahl Wechselrad 2:** | stk. | Zähnezahl des zweiten Wechselrads (ganzzahlig). |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

!!! note "Gültiger Bereich der Wechselräder"
    Wechselrad 1 muss innerhalb des für die gewählte Bandkettentype zulässigen Bereichs liegen (kleine Bandkette: 20 … 50, große Bandkette: 20 … 63). Liegt das berechnete Ergebnis außerhalb, werden die Ergebnisse geleert und es erscheint der Hinweis: *„Nicht möglich, bitte eine andere Ausprägung wählen!"* Wählen Sie in diesem Fall eine andere Ausprägung – etwa eine andere Übersetzung, einen anderen Scheibendurchmesser oder eine andere Bandkettentype.

!!! tip "Stellschrauben bei „Nicht möglich"
    Größere Dehnung, größere Übersetzung oder kleinerer Scheibendurchmesser verringern Wechselrad 1; die jeweils umgekehrte Änderung vergrößert es. So lässt sich das Ergebnis gezielt in den zulässigen Bereich bringen.

## Verwandte Berechnungen

- [Wechselräder Gummibandkette](./change-gears.md)
- [Produktionsgeschwindigkeit](./production-speed.md)
- [Laufzeit Spulensatz](./run-time-bobbin-set.md)
