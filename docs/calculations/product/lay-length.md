# Geflechtsdichte (Schlaglänge)

Die **Geflechtsdichte** beschreibt, wie dicht ein Geflecht erscheint. Diese Berechnung ermittelt aus Geflechtsmaß und Flechtwinkel die **Schlaglänge** – also den axialen Vorschub für eine volle Umdrehung eines Strangs um das Produkt – und kann das Ergebnis wahlweise direkt in gängige Dichte-Einheiten (Flechten je Längeneinheit) umrechnen.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Geflechtsart** | – | Auswahl zwischen **Rundgeflecht** und **Litzengeflecht**. Bestimmt die verwendete Formel. Bei *Rundgeflecht* ist das Maßfeld der Geflechtsdurchmesser, bei *Litzengeflecht* die Geflechtsbreite. |
| **Geflechtsdurchmesser** / **Geflechtsbreite** | mm | Maß des Geflechts. Die Beschriftung wechselt je nach Geflechtsart: *Geflechtsdurchmesser* bei Rundgeflecht, *Geflechtsbreite* bei Litzengeflecht. |
| **Flechtwinkel** | ° | Winkel, unter dem die Stränge zur Produktachse verlaufen (0–90°). |
| **Ergebnis-Einheit** | – | In welcher Einheit das Ergebnis ausgegeben wird: **Schlaglänge [mm]**, **Flechten / 10 mm**, **Flechten / Zoll** oder **Flechten / franz. Zoll**. |
| **Klöppelanzahl** | stk. | Anzahl der Klöppel. **Nur erforderlich**, wenn als Ergebnis-Einheit eine *Flechten / …*-Variante gewählt ist; bei *Schlaglänge [mm]* wird das Feld ausgeblendet. |

!!! note "Pflichtfelder"
    Für die Berechnung müssen **Geflechtsdurchmesser/-breite** und **Flechtwinkel** größer als 0 sein. Bei den *Flechten / …*-Einheiten ist zusätzlich eine **Klöppelanzahl** von mindestens 1 erforderlich.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Schlaglänge** | mm | Bei Ergebnis-Einheit *Schlaglänge [mm]*: axialer Vorschub pro voller Umdrehung. |
| **Flechten / 10 mm** | – | Anzahl der Flechten (Kreuzungspunkte je Klöppel) auf 10 mm Länge. |
| **Flechten / Zoll** | – | Anzahl der Flechten auf einen Zoll (25,4 mm). |
| **Flechten / franz. Zoll** | – | Anzahl der Flechten auf einen französischen Zoll (27 mm). |

Die Ergebnisbeschriftung und -einheit passen sich automatisch der gewählten **Ergebnis-Einheit** an.

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

!!! tip "Gleiche Eingaben, vier Sichtweisen"
    Über die **Ergebnis-Einheit** erhalten Sie aus denselben Eingaben entweder die reine Schlaglänge oder die in der Praxis übliche Flechtdichte (Flechten je 10 mm, Zoll oder französischem Zoll) – ohne die Werte neu eingeben zu müssen.

## Verwandte Berechnungen

* [Flechtwinkel](braid-angle.md)
* [Flechtdichte](picks-density.md)
