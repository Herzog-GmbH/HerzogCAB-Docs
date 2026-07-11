# 3D-Ansicht

!!! abstract "Referenz — die 3D-Rundansicht des Designers: das Flechtbild als runder Geflechtstrang statt als flacher Ausschnitt."

## Wofür Sie diesen Bereich nutzen

Das normale Flechtbild zeigt das Geflecht als flach „aufgeschnittenen"
Ausschnitt. Die **3D-Ansicht** projiziert dasselbe Bild auf einen Zylinder: Sie
sehen, wie sich das Muster am fertigen runden Geflechtstrang **umlaufend
fortsetzt** — so beurteilen Sie Spiralen, Ringe und Übergänge realistischer,
bevor das Design auf die Maschine geht. Zusammen mit der
[Texturdarstellung](painting.md) entsteht ein guter Eindruck des fertigen
Produkts.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Vorschau-Bereich des Designers mit eingeschalteter 3D-Ansicht:
    ein eingefärbtes Rundgeflecht als zylindrischer Strang, daneben die
    aktivierte **3D**-Schaltfläche in der Werkzeugleiste.
    **So erzeugen:** *Designer* öffnen, Rundgeflecht mit farbigem Muster
    anlegen, in der Werkzeugleiste **3D** aktivieren.
    **Ziel-Datei:** `assets/screenshots/designer/designer-3d-ansicht.png`

## Bedienelemente im Detail

### Schaltfläche „3D" (Werkzeugleiste)

Die Schaltfläche **3D** schaltet zwischen der flachen 2D-Darstellung und der
zylindrischen 3D-Rundansicht um:

* **Einschalten:** Klick auf **3D** — das Flechtbild wird als runder Strang
  gezeichnet. Die dem Betrachter abgewandte Rückseite des Zylinders wird dabei
  ausgeblendet.
* **Ausschalten:** erneuter Klick — zurück zur flachen Ansicht.

Farben, Texturen und alle laufenden Änderungen bleiben in beiden Ansichten
identisch; Zoomen und Verschieben funktionieren [wie gewohnt](index.md).

### Verfügbarkeit je Geflechtsart

| Geflechtsart | 3D-Ansicht |
|---|---|
| **Rundgeflecht** | verfügbar |
| **Quadratgeflecht** | verfügbar |
| **Litzengeflecht** | nicht verfügbar (flaches Geflecht) |
| **Packungsgeflecht** | nicht verfügbar |

Bei Litzen- und Packungsgeflecht ist die Schaltfläche **3D** deaktiviert.
Wechseln Sie bei eingeschalteter 3D-Ansicht zu einer dieser Geflechtsarten,
schaltet der Designer automatisch auf die 2D-Darstellung zurück.

<!-- TODO(Verifikation): Ist das Färben per Klick auch in der 3D-Ansicht möglich? Im Code wahrscheinlich ja (gleiche Klick-Logik), aber nicht am laufenden Programm geprüft. -->

## Verwandte Seiten

* [Designer-Überblick](index.md) — Zoomen und Verschieben der Vorschau
* [Färben und Texturieren](painting.md) — Texturdarstellung für den realistischen Eindruck
* [Geflechtart und Parameter](parameters.md) — Geflechtsart wählen
