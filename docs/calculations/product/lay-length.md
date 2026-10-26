# Geflechtsdichte (Schlaglänge)

!!! abstract "Referenz — Berechnung: Schlaglänge bzw. Flechtdichte aus Geflechtsmaß und Flechtwinkel oder Schlaglängenfaktor"

## Wofür

Die **Geflechtsdichte** beschreibt, wie dicht ein Geflecht erscheint. Diese
Berechnung ermittelt aus Geflechtsmaß und Flechtwinkel die **Schlaglänge** –
also den axialen Vorschub für eine volle Umdrehung eines Strangs um das
Produkt – und kann das Ergebnis wahlweise direkt in gängige Dichte-Einheiten
(Flechten je Längeneinheit) umrechnen. Statt des Flechtwinkels können Sie
auch den **Schlaglängenfaktor** vorgeben, wie er bei Seilen üblich ist.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Geflechtsart** | – | Auswahl zwischen **Rundgeflecht** und **Litzengeflecht**. Bestimmt die verwendete Formel. Bei *Rundgeflecht* ist das Maßfeld der Geflechtsdurchmesser, bei *Litzengeflecht* die Geflechtsbreite. |
| **Geflechtsdurchmesser** / **Geflechtsbreite** | mm | Maß des Geflechts. Die Beschriftung wechselt je nach Geflechtsart: *Geflechtsdurchmesser* bei Rundgeflecht, *Geflechtsbreite* bei Litzengeflecht. |
| **Eingabe über** | – | **Flechtwinkel** oder **Schlaglängenfaktor**: Welchen der beiden Werte Sie vorgeben. Der jeweils andere erscheint im Ergebnis. Aufträge und Verlauf von vor Version 2.1.2 öffnen mit *Flechtwinkel*. |
| **Flechtwinkel** | ° | Nur bei *Eingabe über Flechtwinkel*. Winkel der Stränge im eingestellten [Bezug](../../admin/settings/appearance.md#flechtwinkel) (0–90°). |
| **Schlaglängenfaktor** | – | Nur bei *Eingabe über Schlaglängenfaktor*. Verhältnis von Schlaglänge zu Geflechtsdurchmesser, bei Litzengeflecht zur Geflechtsbreite. Bei Seilen sind Werte von 7 bis 12 üblich. |
| **Ergebnis-Einheit** | – | In welcher Einheit das Ergebnis ausgegeben wird: **Schlaglänge [mm]**, **Flechten / 10 mm**, **Flechten / Zoll** oder **Flechten / franz. Zoll**. |
| **Klöppelanzahl** | stk. | Anzahl der Klöppel. **Nur erforderlich**, wenn als Ergebnis-Einheit eine *Flechten / …*-Variante gewählt ist; bei *Schlaglänge [mm]* wird das Feld ausgeblendet. |

!!! note "Pflichtfelder"
    Für die Berechnung müssen **Geflechtsdurchmesser/-breite** und, je nach **Eingabe über**, **Flechtwinkel** oder **Schlaglängenfaktor** größer als 0 sein. Bei den *Flechten / …*-Einheiten ist zusätzlich eine **Klöppelanzahl** von mindestens 1 erforderlich.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Schlaglänge** | mm | Bei Ergebnis-Einheit *Schlaglänge [mm]*: axialer Vorschub pro voller Umdrehung. |
| **Flechten / 10 mm** | – | Anzahl der Flechten (Kreuzungspunkte je Klöppel) auf 10 mm Länge. |
| **Flechten / Zoll** | – | Anzahl der Flechten auf einen Zoll (25,4 mm). |
| **Flechten / franz. Zoll** | – | Anzahl der Flechten auf einen französischen Zoll (27 mm). |
| **Schlaglängenfaktor** | – | Bei *Eingabe über Flechtwinkel*: der Faktor, der zu Maß und Winkel gehört. |
| **Flechtwinkel** | ° | Bei *Eingabe über Schlaglängenfaktor*: der Winkel, der zu Maß und Faktor gehört. |

Die Ergebnisbeschriftung und -einheit passen sich automatisch der gewählten **Ergebnis-Einheit** an.

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md).

Über die **Ergebnis-Einheit** erhalten Sie aus denselben Eingaben entweder
die reine Schlaglänge oder die in der Praxis übliche Flechtdichte (Flechten
je 10 mm, Zoll oder französischem Zoll) – ohne die Werte neu eingeben zu
müssen.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

- [Flechtwinkel](braid-angle.md)
- [Umrechnung Geflechtsdichte](picks-density.md)
