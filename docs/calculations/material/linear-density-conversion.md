# Umrechnung Feinheit

Mit der **Umrechnung Feinheit** rechnen Sie einen Feinheitswert (lineare Dichte) live zwischen den gebräuchlichen Garn-Einheiten um – von **tex** nach **dtex**, **den**, **Nr_Metrisch** oder **Nr_Englisch** und in jeder beliebigen Richtung. Das ist praktisch, wenn ein Garn in einer Einheit angegeben ist, Sie aber für Auftrag, Datenblatt oder Berechnung eine andere Einheit benötigen.

## Eingabewerte

Die Seite ist als Live-Umrechner mit einer **Von/Zu**-Karte aufgebaut: Sie tragen den Wert ein, wählen die Ausgangs- und Zieleinheit, das Ergebnis erscheint sofort.

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Eingabe:** | je nach gewählter Einheit | Umzurechnender Feinheitswert. Es wird nur ein positiver Wert (> 0) umgerechnet. |
| **Von:** | tex, dtex, den, Nr_Metrisch, Nr_Englisch | Einheit, in der der eingegebene Wert vorliegt. Voreinstellung: **tex**. |
| **Zu:** | tex, dtex, den, Nr_Metrisch, Nr_Englisch | Einheit, in die umgerechnet werden soll. Voreinstellung: **dtex**. |

!!! note "Einheiten tauschen"
    Über den grünen Richtungs-Pfeil zwischen den beiden Feldern (Tooltip *„Einheiten tauschen"*) vertauschen Sie **Von** und **Zu** mit einem Klick und rechnen so direkt in die Gegenrichtung.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Ergebnis** | die unter **Zu:** gewählte Einheit | Der in die Zieleinheit umgerechnete Feinheitswert. Bei einer Eingabe ≤ 0 (oder einer ungültigen Umrechnung) wird **0** ausgegeben. |

## Berechnung

Herzog CAB rechnet den eingegebenen Feinheitswert intern zwischen den Einheiten **tex**, **dtex**, **den**, **Nr_Metrisch** und **Nr_Englisch** um. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

!!! note "Beide Richtungen"
    Der Umrechner arbeitet in beide Richtungen: Über die Auswahl von **Von** und **Zu** bzw. den Tausch-Pfeil können Sie jede der fünf Einheiten als Ausgangs- oder als Zieleinheit verwenden.

## Verwandte Berechnungen

* [Feinheit / Titer](./linear-density.md)
* [Materialdurchmesser](./material-diameter.md)
* [Materialien (Stammdaten)](../../master-data/materials.md)
