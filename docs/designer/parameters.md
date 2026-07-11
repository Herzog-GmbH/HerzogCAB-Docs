# Geflechtsart und Parameter

!!! abstract "Referenz — das Parameter-Panel des Designers: Geflechtsart, Geflechtsbindung, Klöppelzahl, Flechtwinkel und Fachung."

## Wofür Sie diesen Bereich nutzen

Im linken Panel des Designers legen Sie die Grundeinstellungen eines Designs
fest: **welches Geflecht** entsteht (Geflechtsart und Bindung) und **mit welcher
Maschinen-Konfiguration** (Klöppelzahl, Flechtwinkel, Fachung). Jede Änderung
baut das Flechtbild, die Klöppeltabelle und die
[Besetzungsübersicht](animation.md) sofort neu auf — Sie sehen also unmittelbar,
welche Auswahl zu welcher Darstellung führt.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Das Parameter-Panel links im Designer mit Designname, den vier
    Geflechtsarten (Rundgeflecht, Litzengeflecht, Quadratgeflecht,
    Packungsgeflecht), den drei Bindungen sowie den Feldern Anzahl Klöppel,
    Flechtwinkel und Fachung.
    **So erzeugen:** *Designer* öffnen, **Neu** klicken; nur das linke Panel
    (oberer Teil bis einschließlich „Fachung") aufnehmen.
    **Ziel-Datei:** `assets/screenshots/designer/designer-parameter-panel.png`

## Bedienelemente im Detail

### Designname

Freitextfeld für die Bezeichnung des Designs (Platzhalter *„Designname
eingeben"*). Der Name erscheint in der Dokument-Kopfzeile, in der
[Design-Bibliothek](../master-data/designs.md) und auf Ausdrucken. Sie können
ihn auch später noch im [Speichern-Dialog](save-print.md) anpassen.

### Geflechtsart

Vier Auswahlfelder bestimmen den Geflechttyp. Die Auswahl steuert, wie das
Flechtbild aufgebaut wird, welche Klöppelzahlen zulässig sind und wie die
Besetzungsübersicht aussieht:

| Geflechtsart | Beschreibung |
|---|---|
| **Rundgeflecht** | Rundes Geflecht mit zwei gegenläufigen Läufen (Linkslauf und Rechtslauf). Das Flechtbild zeigt den umlaufenden Geflechtstrang als flachen Ausschnitt; die [3D-Ansicht](view-3d.md) zeigt ihn rund. |
| **Litzengeflecht** | Flaches Geflecht (Litze) mit einer offenen Gangbahn — die Klöppel pendeln zwischen den beiden Endrädern hin und her. |
| **Quadratgeflecht** | Quadratischer Geflechtquerschnitt auf einer 8er-Maschine mit 4 Flügelrädern (2×2-Anordnung) à 4 Einschnitten und zwei Gangbahnen. |
| **Packungsgeflecht** | Packungs-Flechtmaschine mit Flügelrädern im Raster: **3×3** Flügelräder à 4 Einschnitte (12 Klöppel, 3 Gangbahnen) oder **4×4** Flügelräder à 9 Einschnitten (36 Klöppel, 4 Gangbahnen) — je nachdem, welche Klöppelzahl Sie wählen. |

!!! info "Wechsel der Geflechtsart passt die Klöppelzahl an"
    Beim Umschalten der Geflechtsart (oder der Bindung) springt das Feld
    **Anzahl Klöppel** automatisch auf den nächsten zulässigen Wert der neuen
    Auswahl (siehe Tabelle unten).

### Geflechtsbindung

Drei Auswahlfelder legen die Bindung — also die Besetzungsregel der Maschine —
fest:

| Bindung | Bedeutung |
|---|---|
| **Halbe Besetzung 1-3** | Einflechtige Bindung 1-3: nur jede zweite mögliche Position ist besetzt. |
| **Tandem Besetzung 2-2** | Einflechtige Tandem-Bindung 2-2: die Klöppel laufen paarweise hintereinander. |
| **Normale Besetzung 1-1** | Zweiflechtige Bindung 1-1: die Standardbesetzung. |

!!! info "Packungsgeflecht: Bindung ist fest vorgegeben"
    Beim **Packungsgeflecht** ist konstruktionsbedingt nur die **Normale
    Besetzung 1-1** möglich. Die beiden anderen Bindungen sind dann gesperrt,
    die Auswahl springt automatisch auf 1-1.

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
| Quadratgeflecht | Normale / Tandem Besetzung | fest 8 |
| Quadratgeflecht | Halbe Besetzung 1-3 | fest 4 |
| Packungsgeflecht | Normale Besetzung 1-1 (fest) | 12 (3×3) oder 36 (4×4) |

!!! info "Obergrenzen gelten nur für den Designer"
    Die Obergrenzen der Tabelle sind Darstellungsgrenzen des Designers — sehr
    große Klöppelzahlen wären grafisch nicht mehr sinnvoll darstellbar. In den
    [Berechnungen](../calculations/index.md) können Sie auch mit höheren
    Klöppelzahlen rechnen.

### Flechtwinkel

Zahlenfeld für den Flechtwinkel des Produkts in Grad: **20° bis 80°** in
1°-Schritten, Standardwert **45°**. Der Winkel verändert die Steigung des
Musters im Flechtbild. Der aktuelle Wert steht auch in der Dokument-Kopfzeile.

### Fachung

Zahlenfeld für die Anzahl der Fäden je Klöppelposition (**1 bis 100**). Die
Fachung wird im Flechtbild dargestellt; zum Einfärben und Texturieren der
Fäden siehe [Färben und Texturieren](painting.md).

## Verwandte Seiten

* [Färben und Texturieren](painting.md) — die Klöppel des eingestellten Geflechts einfärben
* [Besetzung und Gangbahn-Animation](animation.md) — wie die gewählte Konfiguration auf der Maschine aussieht
* [Speichern und Drucken](save-print.md) — das fertige Design ablegen
* [Flechtauftrag](../orders/braiding-order.md) — Geflechtsart, Bindung und Klöppelzahl im Auftrag
