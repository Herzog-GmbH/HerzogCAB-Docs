# Umrechnung Geflechtsdichte

Mit der **Umrechnung Geflechtsdichte** wandeln Sie die Dichte eines Geflechts zwischen verschiedenen Bezugsmaßen um – zwischen der **Schlaglänge** und der Anzahl **Flechten** (Flechtungen) je Bezugslänge (10 mm, 25,4 mm bzw. 27 mm). So vergleichen Sie Angaben aus unterschiedlichen Quellen auf einen Blick, ohne von Hand umzurechnen.

Die Funktion arbeitet als Live-Umrechner: Sie geben einen Wert ein, wählen die Ausgangs- und die Zieleinheit, und das Ergebnis erscheint sofort.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Eingabe:** | je nach **Von:** | Der umzurechnende Zahlenwert (Schlaglänge oder Flechtendichte). Werte ≤ 0 ergeben kein Ergebnis. |
| **Von:** | – | Ausgangseinheit. Auswahl: *Schlaglänge*, *Flechten / 10 mm*, *Flechten / 25,4 mm*, *Flechten / 27 mm*. |
| **Zu:** | – | Zieleinheit. Gleiche Auswahl wie bei **Von:**. |
| **Geflechtstyp:** | – | *Rundgeflecht* oder *Litzengeflecht*. Nur sichtbar, wenn **Schlaglänge** auf genau einer Seite (Von oder Zu) steht. |
| **Klöppelanzahl:** | stk. | Anzahl der Klöppel der Maschine. Nur sichtbar, wenn **Schlaglänge** auf genau einer Seite steht. Wertebereich 0–20000. |

!!! note "Wann Geflechtstyp und Klöppelanzahl gebraucht werden"
    Die Zeilen **Geflechtstyp** und **Klöppelanzahl** erscheinen nur, wenn die **Schlaglänge** auf genau einer Seite der Umrechnung steht (also Schlaglänge ↔ Flechten). Nur dann geht die Maschine in die Berechnung ein. Rechnen Sie dagegen zwischen zwei Flechten-Einheiten um (z. B. *Flechten / 10 mm* nach *Flechten / 27 mm*), werden diese Angaben nicht benötigt und bleiben ausgeblendet.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Ergebnis** | je nach **Zu:** | Der in die Zieleinheit umgerechnete Wert (Schlaglänge bzw. Flechtendichte je Bezugslänge). |

Fehlt bei der Umrechnung Schlaglänge ↔ Flechten die **Klöppelanzahl** (Wert 0), kann nicht gerechnet werden und es wird kein Ergebnis (–) angezeigt.

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

* [Flechtwinkel](braid-angle.md)
* [Geflechtsdichte](lay-length.md)
