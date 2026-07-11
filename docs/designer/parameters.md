# Produkt-Design

Ein Design beschreibt das fertige **Produkt** – also das konkrete Geflecht mit
seiner Klöppelzahl, Besetzung und Farbfolge. Über die Einstellungen im Designer
legen Sie fest, welches Produkt entsteht, und verknüpfen das Design anschließend
mit einem Auftrag.

![Designer mit Geflechtart, Besetzung und Klöppel-Parametern.](../assets/screenshots/design/designer-canvas.png)

## Produkt-Parameter

| Parameter | Bedeutung |
|---|---|
| **Geflechtart** | **Rundgeflecht** oder **Litzengeflecht**. |
| **Geflechtsbindung / Besetzung** | Bindungsart und Rapport (z. B. Normale Besetzung 1-1, Tandem 2-2, Halbe Besetzung 1-3). |
| **Anzahl Klöppel** | Anzahl der Klöppel – bestimmt zusammen mit der Besetzung das Muster. |
| **Flechtwinkel** | Flechtwinkel des Produkts in Grad. |
| **Fachung** | Anzahl der Fäden je Klöppel. |

Diese Parameter müssen zur gewählten [Flechtmaschine](../master-data/machines.md)
passen; der Designer berücksichtigt deren zulässige Klöppelzahlen und Bindungen.

## 3D-Vorschau

Über **3D** in der Werkzeugleiste blenden Sie eine räumliche Vorschau des
Rundgeflechts ein. Zusammen mit der Textur-Ansicht erhalten Sie so einen
realistischen Eindruck des fertigen Produkts.

## Design im Auftrag verwenden

Ein gespeichertes Design verknüpfen Sie im [Auftrag](../orders/create.md) im
Tab **Design**. Maschine, Klöppelzahl und Besetzung werden dabei mit dem Auftrag
abgeglichen, sodass Produktdaten und Design zusammenpassen.

!!! info "Design, Auftrag und Maschine greifen ineinander"
    Geflechtart, Besetzung und Klöppelzahl tauchen sowohl im Design als auch im
    Auftrag (Tab *Maschine* und *Produkt*) auf. Halten Sie sie konsistent –
    Herzog CAB unterstützt Sie dabei mit passenden Voreinstellungen und
    Plausibilitätsregeln.
