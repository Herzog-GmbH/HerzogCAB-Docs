# Besetzung und Gangbahn-Animation

!!! abstract "Referenz — die Besetzungsübersicht: Flügelräder und Gangbahnen der Flechtmaschine von oben, mit Animation, Geschwindigkeitsregelung und Farbrotation."

## Wofür Sie diesen Bereich nutzen

Die **Besetzungsübersicht** unten im linken Panel zeigt die Flechtmaschine
schematisch von oben: die Flügelräder mit ihren Einschnitten und die darauf
sitzenden Klöppel in ihren aktuellen Farben. So sehen Sie, wie Ihre
Farbbelegung auf der realen Maschine aussieht. Mit der **Gangbahn-Animation**
setzen Sie das Bild in Bewegung: Die Flügelräder drehen sich, die Klöppel
laufen ihre Gangbahnen ab — und das Flechtbild baut sich synchron dazu Lage für
Lage auf.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Besetzungsübersicht eines Packungsgeflechts (3×3 Flügelräder)
    mit eingefärbten Klöppeln, den Animations-Schaltflächen (Play, langsamer,
    schneller) oben links und den beiden Farbrotations-Pfeilen darunter.
    **So erzeugen:** *Designer* öffnen, **Neu**, Geflechtsart
    **Packungsgeflecht** (12 Klöppel) wählen, einige Klöppel einfärben; nur die
    Besetzungsübersicht aufnehmen.
    **Ziel-Datei:** `assets/screenshots/designer/designer-besetzungsuebersicht.png`

## Bedienelemente im Detail

### Die Besetzungsübersicht je Geflechtsart

Die Anordnung der Flügelräder folgt der gewählten
[Geflechtsart](parameters.md):

| Geflechtsart | Darstellung |
|---|---|
| **Rundgeflecht** | Flügelräder im geschlossenen Ring um den Flechtkreis. |
| **Litzengeflecht** | Flügelräder in offener Reihe — an den beiden größeren Endrädern kehren die Klöppel um. |
| **Quadratgeflecht** | 4 Flügelräder im 2×2-Block, je 4 Einschnitte, zwei Gangbahnen. |
| **Packungsgeflecht** | Flügelräder im Raster: 3×3 (12 Klöppel, 3 Gangbahnen) oder 4×4 (36 Klöppel, 4 Gangbahnen). |

Jeder belegte Einschnitt trägt einen Punkt in der Farbe des zugehörigen
Klöppels. Färben Sie im Flechtbild oder in der Klöppeltabelle um, aktualisiert
sich die Übersicht sofort.

### Zoomen und Verschieben in der Übersicht

Die Übersicht hat eine eigene Ansichtssteuerung, unabhängig vom Zoom des
Flechtbilds:

| Aktion | Bedienung |
|---|---|
| Zoomen | **Mausrad** — gezoomt wird an der Mausposition. |
| Verschieben | **Rechte Maustaste** gedrückt halten und ziehen. |
| Ansicht einpassen | **Doppelklick** mit der linken Maustaste. |

### Gangbahn-Animation (Play/Pause)

Oben links in der Übersicht liegt die **Play-Schaltfläche** (*„Gangbahnen
animieren: Flügelräder drehen sich, Klöppel laufen ihre Bahn ab"*):

* **Play** startet die Animation: Die Flügelräder drehen sich gegensinnig, die
  Klöppel reiten in ihren Einschnitten mit und wechseln an den Übergabepunkten
  auf das Nachbarrad. Jede Geflechtsart hat dabei ihre eigene Bewegungslogik —
  vom umlaufenden Ring des Rundgeflechts über die Pendelbahn der Litze bis zu
  den verschlungenen Gangbahnen von Quadrat- und Packungsgeflecht.
* Erneutes Klicken (**Pause**) hält die Animation an; der aktuelle Stand bleibt
  stehen. Ein weiterer Klick setzt sie fort.
* Ändern Sie Parameter oder die Farbbelegung, wird die Animation zurückgesetzt
  und das vollständige Flechtbild wieder angezeigt.

!!! info "Wann die Animation verfügbar ist"
    Die Animation gibt es für alle vier Geflechtsarten. Bei einzelnen sehr
    kleinen Konfigurationen (z. B. Rundgeflecht mit sehr wenigen Klöppeln) ist
    keine kollisionsfreie Animation möglich — die Play-Schaltfläche wird dann
    nicht angeboten.

### Geschwindigkeit (0,25× bis 8×)

Neben der Play-Schaltfläche liegen zwei Tempo-Schaltflächen:

* **Animation langsamer** — halbiert die Geschwindigkeit (bis minimal 0,25×).
* **Animation schneller** — verdoppelt die Geschwindigkeit (bis maximal 8×).

Die Grundgeschwindigkeit ist bewusst gemächlich gewählt, damit Sie die
Übergaben der Klöppel zwischen den Rädern gut verfolgen können. Zum schnellen
Aufbau des kompletten Flechtbilds schalten Sie einfach ein paar Stufen hoch.

### Synchroner Lage-für-Lage-Aufbau des Flechtbilds

Während die Animation läuft, baut sich das Flechtbild in der Vorschau
**synchron Lage für Lage** auf: Mit jedem Animationsschritt erscheint die
nächste Lage von Maschen. So wird sichtbar, in welcher Reihenfolge die Fäden
tatsächlich verkreuzt werden und wie das Muster entsteht.

* Ist das Bild vollständig aufgebaut, bleibt es komplett stehen — die
  Animation der Räder läuft weiter.
* Beim **Pausieren** bleibt der aktuelle Aufbaustand sichtbar.
* Beim **Zurücksetzen** (z. B. durch eine Parameteränderung) erscheint sofort
  wieder das vollständige Flechtbild.

### Farbrotation (Pfeil-Schaltflächen)

Unter der Übersicht liegen zwei Pfeil-Schaltflächen (**Links drehen** /
**Rechts drehen**). Sie verschieben die komplette Farb- und Texturbelegung
aller Klöppel um jeweils eine Position entlang der Gangbahn — die Besetzung
selbst (welche Einschnitte belegt sind) ändert sich dabei nicht. Damit
simulieren Sie ein Weiterdrehen der Maschine und probieren Farbvarianten
durch, ohne jeden Klöppel einzeln umzufärben — praktisch für Spiral- und
Versatzmuster. Flechtbild, Klöppeltabelle und Übersicht wandern gemeinsam mit.

!!! info "Keine Farbrotation beim Packungsgeflecht"
    Beim **Packungsgeflecht** passt die Links-/Rechts-Rotation nicht zur
    Gangbahn-Struktur — die beiden Pfeil-Schaltflächen sind dort deaktiviert.

## Verwandte Seiten

* [Färben und Texturieren](painting.md) — die Farben, die hier rotiert und animiert werden
* [Geflechtart und Parameter](parameters.md) — Radanordnung und Klöppelzahl festlegen
* [3D-Ansicht](view-3d.md) — das fertige Muster am runden Strang betrachten
