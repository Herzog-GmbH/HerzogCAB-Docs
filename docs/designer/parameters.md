# Geflechtsart und Parameter

!!! abstract "Referenz — das Parameter-Panel des Designers: Geflechtsart, Geflechtsbindung, Bahn-Art, Klöppelzahl, Flechtwinkel, Fachung, Seelen sowie die Maßzeile mit Material-Ø, Bedeckung und Geflechts-Ø."

## Wofür Sie diesen Bereich nutzen

Im linken Panel des Designers legen Sie die Grundeinstellungen eines Designs
fest: **welches Geflecht** entsteht (Geflechtsart und Bindung) und **mit welcher
Maschinen-Konfiguration** (Klöppelzahl, Flechtwinkel, Fachung). Jede Änderung
baut das Flechtbild, die Klöppeltabelle und die
[Besetzungsübersicht](animation.md) sofort neu auf — Sie sehen also unmittelbar,
welche Auswahl zu welcher Darstellung führt. Der Designer beherrscht **sechs
Geflechtsarten**; jedes Flechtbild ist aus der Kinematik der jeweiligen
Maschine hergeleitet.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Das Parameter-Panel links im Designer mit Designname, den
    Auswahllisten **Geflechtsart** (aufgeklappt, alle sechs Einträge sichtbar)
    und **Geflechtsbindung** sowie den Feldern Anzahl Klöppel, Flechtwinkel
    und Fachung.
    **So erzeugen:** *Designer* öffnen, **Neu** klicken; die Liste
    Geflechtsart aufklappen; nur das linke Panel (oberer Teil bis
    einschließlich „Fachung") aufnehmen.
    **Ziel-Datei:** `assets/screenshots/designer/designer-parameter-panel.png`

Die Karte ist kompakt und **scrollbar** — auf kleinen Bildschirmen rollen
Sie im Panel, um die unteren Felder zu erreichen.

## Bedienelemente im Detail

### Designname

Freitextfeld für die Bezeichnung des Designs (Platzhalter *„Designname
eingeben"*). Der Name erscheint in der Dokument-Kopfzeile, in der
[Design-Bibliothek](../master-data/designs.md) und auf Ausdrucken. Sie können
ihn auch später noch im [Speichern-Dialog](save-print.md) anpassen.

### Geflechtsart

Die Auswahlliste **Geflechtsart** bestimmt den Geflechttyp. Die Auswahl
steuert, wie das Flechtbild aufgebaut wird, welche Bindungen und Klöppelzahlen
zulässig sind und wie die Besetzungsübersicht aussieht. Beim Zeigen auf
einen Eintrag erklärt ein Hinweis die Maschinenbauart.

| Geflechtsart | Beschreibung |
|---|---|
| **Rundgeflecht** | Rundes Geflecht mit zwei gegenläufigen Läufen (Linkslauf und Rechtslauf) auf einem Ring von Flügelrädern. Das Flechtbild zeigt den umlaufenden Geflechtstrang als flachen Ausschnitt; die Ansichten *Zylinder* und *3D* zeigen ihn rund (siehe [3D-Ansicht](view-3d.md)). |
| **Litzengeflecht** | Flaches Geflecht (Litze) mit einer offenen Gangbahn — die Klöppel pendeln zwischen den beiden größeren Endrädern hin und her. |
| **Quadratgeflecht** | Quadratischer Geflechtquerschnitt: 4 Flügelräder mit 4 bis 18 Einschnitten tragen 8 bis 36 Klöppel auf zwei Gangbahnen. Ansichten *Voll*, *Vierkant* (drehbar) und *3D*. |
| **Spiralgeflecht** | Spiralflechter mit 4 Flügelrädern im festen Außenkranz: 12 Klöppel (3 Einschnitte je Rad, 3 Gangbahnen) oder 20 Klöppel (5 Einschnitte, 5 Gangbahnen); Besetzung 1 voll / 1 leer. |
| **Packungsgeflecht** | Packungsflechter mit Flügelrädern im Raster. Über **Bahn-Art** wählen Sie die Familie — **2-bahnig**, **3-bahnig**, **4-bahnig** oder **rund** —, über **Klöppel** die Größe. Ansichten *Voll*, *Kante* (drehbar) und *3D*. |
| **Soutachegeflecht** | Zwei Flügelräder mit je so vielen Einschnitten wie Klöppeln auf einer Achter-Bahn: 3, 5, 7, 9 oder 11 Klöppel (immer ungerade), Besetzung 1 voll / 1 leer — wahlweise mit **zwei Seelen** durch die Flügelrad-Achsen. |

!!! info "Wechsel der Geflechtsart passt die Klöppelzahl an"
    Beim Umschalten der Geflechtsart (oder der Bindung) springt das Feld
    **Anzahl Klöppel** automatisch auf den nächstliegenden zulässigen Wert
    der neuen Auswahl (siehe Tabelle unten). Die Werkzeugleiste blendet die
    passenden Ansichts-Schalter ein.

### Geflechtsbindung

Die Auswahlliste **Geflechtsbindung** legt die Besetzungsregel der Maschine
fest:

| Bindung | Bedeutung |
|---|---|
| **Normale Besetzung 1-1** | Zweiflechtige Bindung 1-1: die Standardbesetzung. |
| **Halbe Besetzung 1-3** | Einflechtige Bindung 1-3: nur jede zweite mögliche Position ist besetzt. |
| **Tandem Besetzung 2-2** | Einflechtige Tandem-Bindung 2-2: die Klöppel laufen paarweise hintereinander. |

!!! info "Feste Bindungen"
    **Packungs-**, **Spiral-** und **Soutachegeflecht** haben eine
    konstruktionsbedingt feste Besetzung — die Liste **Geflechtsbindung** ist
    dann ausgeblendet. Beim **Quadratgeflecht** gibt es die Tandem-Besetzung
    nur für 8, 16, 24 und 32 Klöppel. Ist das Design aus einem
    [Flechtauftrag](../orders/braiding-order.md) heraus geöffnet, gibt der
    Auftrag Geflechtsart und Bindung vor — die Felder sind dann gesperrt.

### Bahn-Art und Klöppel (nur Packungsgeflecht)

| Feld | Bedeutung |
|---|---|
| **Bahn-Art** | Familie des Packungsflechters: **2-bahnig**, **3-bahnig**, **4-bahnig** oder **rund**. Die Art legt Aufbau und Gangbahnen fest. |
| **Klöppel** | Klöppelzahl der gewählten Art. Größen, die der Designer noch nicht abbilden kann, stehen ausgegraut mit dem Zusatz *(in Vorbereitung)* in der Liste. |

| Bahn-Art | Klöppelzahlen |
|---|---|
| 2-bahnig | 8, 12, 16, 24 |
| 3-bahnig | 12 (3×3 Räder à 4 Einschnitte), 18 (3×3 à 6), 20 (Mischräder, PA3 1/20-280) — 24 in Vorbereitung |
| 4-bahnig | 24 (4×4 à 6), 32 (4×4 à 8), 36 (Mischräder, PA4 1/36-400), 52 (Mischräder, PA4 1/52-320) |
| rund | 12, 16, 24, 32 |

### Anzahl Klöppel

Zahlenfeld mit Stufenauswahl: Die Pfeile springen direkt zum nächsten
**zulässigen** Wert — welche Werte das sind, hängt von Geflechtsart und Bindung
ab:

| Geflechtsart | Bindung | Zulässige Klöppelzahlen |
|---|---|---|
| Rundgeflecht | Normale Besetzung 1-1 | 12 bis 144 in 4er-Schritten |
| Rundgeflecht | Tandem Besetzung 2-2 | 12 bis 144 in 4er-Schritten |
| Rundgeflecht | Halbe Besetzung 1-3 | 6 bis 72 in 2er-Schritten |
| Litzengeflecht | Normale Besetzung 1-1 | 9 bis 145 in 4er-Schritten |
| Litzengeflecht | Tandem Besetzung 2-2 | 10 bis 50 in 4er-Schritten |
| Litzengeflecht | Halbe Besetzung 1-3 | 5 bis 73 in 2er-Schritten |
| Quadratgeflecht | Normale Besetzung 1-1 | 8, 12, 16, 20, 24, 28, 32, 36 |
| Quadratgeflecht | Tandem Besetzung 2-2 | 8, 16, 24, 32 |
| Quadratgeflecht | Halbe Besetzung 1-3 | 4, 6, 8, 10, 12, 14, 16, 18 |
| Spiralgeflecht | fest | 12 oder 20 |
| Packungsgeflecht | fest | je Bahn-Art, siehe oben |
| Soutachegeflecht | fest | 3, 5, 7, 9, 11 |

!!! info "Obergrenzen gelten nur für den Designer"
    Die Obergrenzen der Tabelle sind Darstellungsgrenzen des Designers — sehr
    große Klöppelzahlen wären grafisch nicht mehr sinnvoll darstellbar. In den
    [Berechnungen](../calculations/index.md) können Sie auch mit höheren
    Klöppelzahlen rechnen.

### Flechtwinkel

Zahlenfeld für den Flechtwinkel des Produkts in Grad: **20° bis 80°** in
1°-Schritten, Standardwert **45°** (änderbar unter
[Einstellungen > Design](../admin/settings/legacy-import.md)). Der Winkel
verändert die Steigung des Musters im Flechtbild und wirkt live auf die
[3D-Ansicht](view-3d.md). Der aktuelle Wert steht auch in der
Dokument-Kopfzeile.

### Fachung

Zahlenfeld für die Anzahl der Fäden je Klöppelposition (**1 bis 100**). Die
Fachung wird im Flechtbild dargestellt; zum Einfärben und Texturieren der
Fäden siehe [Färben und Texturieren](painting.md).

### Seelen einlegen (2 Kerne) — nur Soutachegeflecht

Ankreuzfeld: Zwei Seelenfäden (Kerneinlagen) laufen durch die Achsen der
beiden Flügelräder und werden umflochten — die klassische Soutache-Kordel
mit zwei Wülsten. Ausschalten für seelenlose Geflechte. Die Seelen erscheinen
in der [3D-Ansicht](view-3d.md) als Kerne.

## Maßzeile in der Vorschau

Oben in der Vorschau-Karte steht eine **Maßzeile** (abschaltbar unter
[Einstellungen > Design](../admin/settings/legacy-import.md)):

| Feld | Bedeutung |
|---|---|
| **Material-Ø** | Durchmesser des einzelnen Fadens (Garn/Draht) in mm, 0,00–100,00. Leer (*–*) = keine Angabe; der Geflechtsdurchmesser bleibt dann leer. |
| **Bedeckung** (bei Litze: **Füllung**) | Bedeckungsgrad des Geflechts in Prozent, Standard **70 %** (änderbar in den Einstellungen). Steuert in der 3D-Ansicht die gezeichnete Fadendicke. |
| **Geflechts-Ø** (bei Litze: **Produktbreite**) | Anzeige: der berechnete Geflechtsdurchmesser aus Klöppelzahl, Flechtwinkel, Fachung, Materialdurchmesser und Bedeckung — dieselbe Berechnung wie die Seite [Durchmesser](../calculations/tubular-braid/tube-diameter.md). Nur Anzeige; die Zeichnung bleibt maßstabslos. |

## Verwandte Seiten

* [Färben und Texturieren](painting.md) — die Klöppel des eingestellten Geflechts einfärben
* [Besetzung und Gangbahn-Animation](animation.md) — wie die gewählte Konfiguration auf der Maschine aussieht
* [3D-Ansicht](view-3d.md) — Projektionen und echtes 3D-Modell
* [Speichern und Drucken](save-print.md) — das fertige Design ablegen
* [Flechtauftrag](../orders/braiding-order.md) — Geflechtsart, Bindung und Klöppelzahl im Auftrag
* [Design (Einstellungen)](../admin/settings/legacy-import.md) — Vorgaben für neue Designs
