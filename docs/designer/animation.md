# Besetzung und Gangbahn-Animation

!!! abstract "Referenz — die Besetzungsübersicht: Flügelräder und Gangbahnen der Flechtmaschine von oben, mit Animation und Geschwindigkeitsregelung."

## Wofür Sie diesen Bereich nutzen

Die **Besetzungsübersicht** unten im linken Panel zeigt die Flechtmaschine
schematisch von oben: die Flügelräder mit ihren Einschnitten und die darauf
sitzenden Klöppel in ihren aktuellen Farben. So sehen Sie, wie Ihre
Farbbelegung auf der realen Maschine aussieht. Mit der **Gangbahn-Animation**
setzen Sie das Bild in Bewegung: Die Flügelräder drehen sich, die Klöppel
laufen ihre Gangbahnen ab — und das Flechtbild baut sich synchron dazu Lage für
Lage auf.

## Der Bildschirm im Überblick

![Besetzungsübersicht eines Packungsgeflechts mit neun Flügelrädern, eingefärbten Klöppeln und den Animations-Schaltflächen](../assets/screenshots/designer/designer-besetzungsuebersicht.png)

## Bedienelemente im Detail

### Die Besetzungsübersicht je Geflechtsart

Die Anordnung der Flügelräder folgt der gewählten
[Geflechtsart](parameters.md):

| Geflechtsart | Darstellung |
|---|---|
| **Rundgeflecht** | Flügelräder im geschlossenen Ring um den Flechtkreis. |
| **Litzengeflecht** | Flügelräder in offener Reihe — an den beiden größeren Endrädern kehren die Klöppel um. |
| **Quadratgeflecht** | 4 Flügelräder im 2×2-Block, je 4 Einschnitte, zwei Gangbahnen. |
| **Spiralgeflecht** | 4 kleine Flügelräder, die innen an einem festen Außenkranz abrollen; alle drehen gleichsinnig. |
| **Packungsgeflecht** | Flügelräder im Raster: 3×3 (12 Klöppel, 3 Gangbahnen) oder 4×4 (36 Klöppel, 4 Gangbahnen). |
| **Soutachegeflecht** | Genau 2 Flügelräder mit einer Achter-Bahn. |

Jeder belegte Einschnitt trägt einen Punkt in der Farbe des zugehörigen
Klöppels. Hat ein Klöppel [Fachungsfarben](painting.md#fachungsfarben-farbe-je-garn),
ist sein Punkt in Kreisstücke je Garn geteilt. Färben Sie im Flechtbild oder
in der Klöppeltabelle um, aktualisiert sich die Übersicht sofort.

### Zoomen und Verschieben in der Übersicht

Die Übersicht hat eine eigene Ansichtssteuerung, unabhängig vom Zoom des
Flechtbilds:

| Aktion | Bedienung |
|---|---|
| Zoomen | **Mausrad** — gezoomt wird an der Mausposition. |
| Verschieben | **Rechte Maustaste** gedrückt halten und ziehen. |
| Ansicht einpassen | **Doppelklick** mit der linken Maustaste. |

### Schaltflächen der Übersicht

Oben links in der Übersicht liegen die Schaltflächen der Animation, von
links nach rechts:

| Schaltfläche | Kurzhinweis | Wirkung |
|---|---|---|
| ⏮ | *Maschine und Geflechtsaufbau auf den Anfang setzen* | Setzt Maschine und Aufbau auf den Anfang, siehe [unten](#auf-den-anfang-setzen). |
| ▶ / ⏸ | *Gangbahnen animieren: Flügelräder drehen sich, Klöppel laufen ihre Bahn ab* | Startet bzw. hält die Animation an. |
| ⏪ | *Animation langsamer* | Halbiert die Geschwindigkeit. |
| ⏩ | *Animation schneller* | Verdoppelt die Geschwindigkeit. |

Die Schaltfläche oben rechts (*Maschinenübersicht vergrößert anzeigen*)
öffnet die Übersicht in einem großen Fenster **Maschinenübersicht**.

### Gangbahn-Animation (Play/Pause)

* **Play** startet die Animation: Die Flügelräder drehen sich gegensinnig, die
  Klöppel reiten in ihren Einschnitten mit und wechseln an den Übergabepunkten
  auf das Nachbarrad. Jede Geflechtsart hat dabei ihre eigene Bewegungslogik —
  vom umlaufenden Ring des Rundgeflechts über die Pendelbahn der Litze bis zu
  den verschlungenen Gangbahnen von Quadrat- und Packungsgeflecht, der
  Achter-Bahn der Soutache und den abrollenden Rädern der Spirale.
* Erneutes Klicken (**Pause**) hält die Animation an; der aktuelle Stand bleibt
  stehen. Ein weiterer Klick setzt sie fort.
* Ändern Sie Parameter oder die Farbbelegung, wird die Animation zurückgesetzt
  und das vollständige Flechtbild wieder angezeigt.

!!! info "Wann die Animation verfügbar ist"
    Die Animation gibt es für alle sechs Geflechtsarten. Bei einzelnen sehr
    kleinen Konfigurationen (z. B. Rundgeflecht mit sehr wenigen Klöppeln) ist
    keine kollisionsfreie Animation möglich — die Schaltflächen der Animation
    werden dann nicht angeboten.

### Auf den Anfang setzen (⏮) { #auf-den-anfang-setzen }

Die Schaltfläche ⏮ links neben Play setzt die Klöppel auf ihre
Startposition und leert den lagenweisen Aufbau im Flechtbild und in der
[3D-Ansicht](view-3d.md):

* Läuft die Animation, baut sich das Geflecht sofort von vorn neu auf.
* Steht die Animation, bleibt der Anfang stehen, bis Sie **Play** drücken.

Die Klöppelbezeichnungen bleiben dabei an ihren Klöppeln.

### Geschwindigkeit (0,25× bis 16×)

Rechts neben der Play-Schaltfläche liegen zwei Tempo-Schaltflächen:

* **Animation langsamer** — halbiert die Geschwindigkeit (bis minimal 0,25×).
* **Animation schneller** — verdoppelt die Geschwindigkeit (bis maximal 16×).

Mit niedriger Geschwindigkeit verfolgen Sie die Übergaben der Klöppel
zwischen den Rädern, mit hoher bauen Sie das komplette Flechtbild schnell
auf. Die Startgeschwindigkeit legen Sie unter
[Einstellungen > Design](../admin/settings/legacy-import.md) fest; die
Tempo-Schaltflächen schreiben den zuletzt genutzten Wert dorthin zurück.

### Synchroner Lage-für-Lage-Aufbau des Flechtbilds

Während die Animation läuft, baut sich das Flechtbild in der Vorschau
**synchron Lage für Lage** auf: Mit jedem Animationsschritt erscheint die
nächste Lage von Maschen. So wird sichtbar, in welcher Reihenfolge die Fäden
tatsächlich verkreuzt werden und wie das Muster entsteht.

* Ist das Bild vollständig aufgebaut, bleibt es komplett stehen — die
  Animation der Räder läuft weiter.
* Beim **Pausieren** bleibt der aktuelle Aufbaustand sichtbar.
* Mit **⏮** beginnt der Aufbau von vorn.
* Beim **Zurücksetzen** (z. B. durch eine Parameteränderung) erscheint sofort
  wieder das vollständige Flechtbild.

In der [3D-Ansicht](view-3d.md) wächst das Geflecht genauso synchron mit.

## Verwandte Seiten

* [Färben und Drehung](painting.md) — die Farben, die hier animiert werden
* [Geflechtsart und Parameter](parameters.md) — Radanordnung und Klöppelzahl festlegen
* [3D-Ansicht](view-3d.md) — das fertige Muster am runden Strang betrachten
