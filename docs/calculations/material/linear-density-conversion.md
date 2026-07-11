# Umrechnung Feinheit

!!! abstract "Referenz — Berechnung: Feinheitswert live zwischen Garn-Einheiten umrechnen"

## Wofür

Mit der **Umrechnung Feinheit** rechnen Sie einen Feinheitswert (lineare
Dichte) live zwischen den gebräuchlichen Garn-Einheiten um – von **tex**
nach **dtex**, **den**, **Nr_Metrisch** oder **Nr_Englisch** und in jeder
beliebigen Richtung. Das ist praktisch, wenn ein Garn in einer Einheit
angegeben ist, Sie aber für Auftrag, Datenblatt oder Berechnung eine andere
Einheit benötigen.

## Eingabewerte

Die Seite ist als Live-Umrechner mit einer **Von/Zu**-Karte aufgebaut: Sie
tragen den Wert ein, wählen die Ausgangs- und Zieleinheit, das Ergebnis
erscheint sofort.

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Eingabe:** | je nach gewählter Einheit | Umzurechnender Feinheitswert. Es wird nur ein positiver Wert (> 0) umgerechnet. |
| **Von:** | tex, dtex, den, Nr_Metrisch, Nr_Englisch | Einheit, in der der eingegebene Wert vorliegt. Voreinstellung: **tex**. |
| **Zu:** | tex, dtex, den, Nr_Metrisch, Nr_Englisch | Einheit, in die umgerechnet werden soll. Voreinstellung: **dtex**. |

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Ergebnis** | die unter **Zu:** gewählte Einheit | Der in die Zieleinheit umgerechnete Feinheitswert. Bei einer Eingabe ≤ 0 (oder einer ungültigen Umrechnung) wird **0** ausgegeben. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md). Diese
Seite ist ein **Live-Umrechner**: Es gibt keine Schaltfläche **Berechnen**,
das Ergebnis aktualisiert sich bei jeder Eingabe sofort. Live-Umrechner legen
bewusst keinen Eintrag in der Verlaufs-Leiste an.

Über den grünen Richtungs-Pfeil zwischen den beiden Feldern (Tooltip
*„Einheiten tauschen"*) vertauschen Sie **Von** und **Zu** mit einem Klick und
rechnen so direkt in die Gegenrichtung.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

- [Feinheit / Titer](linear-density.md)
- [Materialdurchmesser über Material](material-diameter.md)
- [Materialien (Stammdaten)](../../master-data/materials.md)
