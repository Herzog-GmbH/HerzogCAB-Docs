# Ansichten und 3D-Ansicht

!!! abstract "Referenz — die Ansichts-Schalter des Designers: volle und halbe Abwicklung, die drehbaren Projektionen Zylinder, Vierkant und Kante sowie das echte 3D-Modell des Geflechts."

## Wofür Sie diesen Bereich nutzen

Das normale Flechtbild zeigt das Geflecht als flach „aufgeschnittenen"
Ausschnitt. Für die Beurteilung eines Musters am fertigen Produkt bietet der
Designer weitere Ansichten: die **Projektionen** legen die Abwicklung drehbar
auf einen Zylinder oder Vierkant, das echte **3D-Modell** baut das Geflecht
Faden für Faden aus den Klöppelbahnen der Besetzungsübersicht auf — mit
Kreuzungen, Material und Bedeckung, frei drehbar. So
beurteilen Sie Spiralen, Ringe, Übergänge und Kanten realistisch, bevor das
Design auf die Maschine geht.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Vorschau-Bereich des Designers in der 3D-Ansicht: ein
    zweifarbiges Rundgeflecht als räumliches Modell, darüber die
    Ansichtsleiste (Draufsicht / Seitenansicht / Flechtpunkt + Schloss),
    darunter die Reglerzeile Material / Darstellung / Ausrichtung; in der
    Werkzeugleiste ist **3D** aktiv.
    **So erzeugen:** *Designer* öffnen, Rundgeflecht 24 Klöppel, Linkslauf
    rot und Rechtslauf blau färben, in der Werkzeugleiste **3D** wählen,
    Ansicht *Seitenansicht*.
    **Ziel-Datei:** `assets/screenshots/designer/designer-3d-ansicht.png`

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Dieselbe Vorschau in der Ansicht **Zylinder** (Projektion),
    leicht gedreht, mit den Drehpfeilen.
    **So erzeugen:** wie oben, Ansicht **Zylinder** wählen und einmal drehen.
    **Ziel-Datei:** `assets/screenshots/designer/designer-zylinder-ansicht.png`

## Bedienelemente im Detail

### Ansichts-Schalter in der Werkzeugleiste

Die Schalter sind eine Gruppe — genau einer ist aktiv. Welche erscheinen,
hängt von der Geflechtsart ab:

| Geflechtsart | Schalter |
|---|---|
| **Rundgeflecht** | **Voll** · **Halb** · **Zylinder** · **3D** |
| **Quadratgeflecht** | **Voll** · **Vierkant** · **3D** |
| **Packungsgeflecht** | **Voll** · **Kante** · **3D** |
| **Litzen-**, **Spiral-**, **Soutachegeflecht** | **Voll** · **3D** |

| Schalter | Bedeutung |
|---|---|
| **Voll** | Die komplette Abwicklung des Umfangs als flaches Flechtbild — die Standardansicht, in der Sie färben. |
| **Halb** | Nur die vordere Hälfte der Abwicklung (Rundgeflecht). |
| **Zylinder** / **Vierkant** / **Kante** | Die Abwicklung auf den Zylinder (Rund) bzw. den Vierkant (Quadrat, Packung) projiziert. Die Rückseite ist ausgeblendet; mit den Drehpfeilen an der Vorschau-Karte drehen Sie den Körper schrittweise. Bei Vierkant und Kante entstehen die Kanten durch Licht und Schattierung, nicht durch Linien. |
| **3D** | Das echte räumliche Modell des Geflechts aus den Klöppelbahnen der Besetzungsübersicht — für alle sechs Geflechtsarten. Mischdesigns aus Rund- und Litzenabschnitten haben kein 3D-Modell; die Ansicht zeigt dann einen Hinweis. |

Farben, Fachung und alle laufenden Änderungen bleiben in allen Ansichten
identisch. Färben per Klick gehört ins flache Flechtbild; in der 3D-Ansicht
färben Sie über die Klöppeltabelle oder die Palette — das Modell folgt
sofort. Die gewählte Ansicht (samt Drehwinkel)
merkt sich der Designer je Geflechtsart, wenn die Einstellung
*Zuletzt genutzte Ansicht merken* aktiv ist
([Einstellungen > Design](../admin/settings/legacy-import.md)).

### Die 3D-Ansicht bedienen

Oben im Bild liegt die **Ansichtsleiste**:

| Element | Wirkung |
|---|---|
| **Draufsicht** | Blick auf den Querschnitt, so orientiert wie die Maschine in der Besetzungsübersicht. |
| **Seitenansicht** | Das ganze Geflecht von der Seite — das Flechtbild. |
| **Flechtpunkt** | Nahaufnahme der Stelle, an der das Geflecht gerade entsteht; die Kamera folgt der Gangbahn-Animation. |
| **Schloss** | Gesperrt: Maus und Finger drehen das Geflecht nicht, das Mausrad zoomt weiterhin. Offen: linke Maustaste dreht, rechte verschiebt, Doppelklick stellt die gewählte Ansicht wieder her. |
| **Hineinzoomen** / **Herauszoomen** (Vorschau-Karte) | Wirken auch in der 3D-Ansicht; ebenso das Mausrad. |

Unter dem Bild liegt die **Reglerzeile**:

| Regler | Optionen | Bedeutung |
|---|---|---|
| **Material** | *Glattes Filament*, *Gedrehtes Garn*, *Draht*, *Light-Version (einfach)* | Faserstruktur, Rauheit und Glanz der Fäden. Die Klöppelfarben bleiben in allen Materialien erhalten; die Light-Version ist für schwache Grafikkarten. |
| **Darstellung** | *Vorgabe der Geflechtsart*, *Nur Abbindung (Schema)*, *Automatisch*, *Wie die Maschine steht*, *Korrektur: immer rund*, *Korrektur: immer Litze* | Wie der Querschnitt hergeleitet wird: *Nur Abbindung* zeigt Fadenfolge und Kreuzungen auf dem normierten Querschnitt (ohne Radpositionen und Radgrößen); *Automatisch* und *Wie die Maschine steht* leiten ihn aus den Gangbahnen ab. Die Vorgabe je Geflechtsart ist Abbindung für Rund, Spirale und Soutache, gerade gezogen für Litze, Maschinenform für Quadrat und Packung. |
| **Ausrichtung** | *Oben → unten*, *Unten → oben* | Dreht nur die 3D-Anzeige des Geflechts — je nachdem, ob Sie die Maschine von oben oder von unten betrachten möchten. |

Die **Bedeckung** aus der [Maßzeile](parameters.md#mazeile-in-der-vorschau)
bestimmt die gezeichnete Fadendicke; der **Flechtwinkel** wirkt live. Läuft
die [Gangbahn-Animation](animation.md), wächst das 3D-Geflecht synchron mit
— *Zurück auf Anfang* zeigt wieder das ganze Geflecht. Diese Einstellungen
gelten für den Designer insgesamt, nicht je Design.

!!! info "Grenzen der 3D-Ansicht"
    * Färben per Klick, Klöppelnummern und Texturen gibt es nur im flachen
      Flechtbild.
    * Bei Quadrat- und Packungsgeflecht zeigt das Modell die Gangbahnen der
      Klöppel; der gepackte Vierkant-Querschnitt des fertigen Produkts
      entsteht erst auf der Maschine.
    * Große Maschinen (ab etwa 100 Klöppeln) brauchen nach einer Änderung von
      Klöppelzahl oder Bindung einen Moment für den Neuaufbau; Farbwechsel
      sind sofort sichtbar.
    * Die Ansicht braucht eine OpenGL-fähige Grafik (siehe
      [Systemvoraussetzungen](../setup/system-requirements.md)).

## Verwandte Seiten

* [Designer-Überblick](index.md) — Zoomen und Verschieben der Vorschau
* [Geflechtsart und Parameter](parameters.md) — Geflechtsart wählen, Maßzeile
* [Färben und Texturieren](painting.md) — Texturdarstellung im flachen Flechtbild
* [Besetzung und Gangbahn-Animation](animation.md) — die Kinematik hinter dem 3D-Modell
* [Design (Einstellungen)](../admin/settings/legacy-import.md) — Ansicht merken
