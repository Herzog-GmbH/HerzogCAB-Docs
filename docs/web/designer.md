# Designs und Designer (Web-App)

!!! abstract "Referenz — Das Modul Designs der Web-App: Design-Bibliothek und der Designer mit Geometrie, Flechtbild, Farben, Klöppeltabelle, Besetzungsübersicht und 3D-Ansicht"

## Wofür Sie diesen Bereich nutzen

Unter **Designs** liegt die Design-Bibliothek Ihres Kontos; ein Klick auf
ein Design öffnet den **Designer**. Er beherrscht wie die Desktop-App alle
sechs Geflechtsarten (Rund, Litze, Quadrat, Spirale, Packung, Soutache) mit
ihren Bindungen, zeichnet dasselbe Flechtbild, zeigt die Besetzungsübersicht
mit Gangbahn-Animation und das echte 3D-Modell des Geflechts. Was die
einzelnen Parameter bedeuten, steht in der Referenz des Desktop-Designers
([Geflechtsart und Parameter](../designer/parameters.md)); hier geht es um
die Bedienung im Browser.

## Design-Bibliothek

![Design-Bibliothek der Web-App mit Vorschaubildern, Chips und Ordnerfilter.](../assets/screenshots/web/designs.png)

| Element | Bedeutung |
|---|---|
| **Neues Design** | Legt ein neues Design mit Standardwerten an und öffnet den Designer. |
| **Ordner** (Baum) | Am breiten Bildschirm links: **Alle Designs**, **Ohne Ordner** und Ihre Ordner mit der Zahl der Designs. Ein Ordner zeigt seine Unterordner und die Designs direkt darin. Auf schmalen Bildschirmen öffnet der Knopf mit dem Ordnernamen über der Liste den Baum. |
| Ordner-Aktionen | Mit dem Recht *Designer bearbeiten* neben dem Pfad des gewählten Ordners: **Neuer Ordner**, **Ordner umbenennen**, **Ordner kopieren** und **Ordner löschen**. Beim Löschen kommen die Designs darin in den übergeordneten Ordner. |
| **Suchen …** | Filtert nach dem Namen, im gewählten Ordner bzw. über alle Designs. |
| **Sortierung** | **Name**, **Zuletzt bearbeitet** oder **Geflechtsart**. In der Liste sortieren Sie auch über die Spaltenköpfe. |
| **Kacheln** / **Listenansicht** | Schmale Kacheln mit großer Vorschau oder eine Tabelle mit kleiner Vorschau, Geflechtsart, Klöppelzahl, Winkel, Ordner und Datum der letzten Änderung. Die Wahl bleibt in diesem Browser gespeichert. |
| Eintrag | Vorschaubild (*keine Vorschau*, solange das Design noch nie gespeichert wurde), Name, Geflechtsart, Klöppelzahl und Flechtwinkel. Ein Klick öffnet das Design. |
| Kästchen und Auswahlleiste | Mit dem Kästchen an einem Eintrag wählen Sie Designs aus. Die Leiste unten bietet dann **Verschieben nach …**, **Kopieren nach …**, **Umbenennen** (bei einem Design) und **Löschen**. Am Rechner lassen sich Designs auch auf einen Ordner im Baum ziehen. |
| **Löschen** | Entfernt das Design nach Sicherheitsabfrage. Es kommt in den [Papierkorb](versions.md#papierkorb) und lässt sich dort wiederherstellen. |

Designs aus der Desktop-App erscheinen hier nach dem
[Import](import.md) bzw. dem Cloud-Upload mit ihrem Ordner.

## Der Designer im Überblick

![Designer der Web-App: Geometrie links, Flechtbild und Besetzungsübersicht in der Mitte, Farben und Klöppeltabelle rechts.](../assets/screenshots/web/designer.png)

Am Desktop ist der Designer dreispaltig: **Geometrie** links, **Flechtbild**
mit **Besetzungsübersicht** in der Mitte, **Farben** und **Klöppeltabelle**
rechts. Auf Tablet und Smartphone liegt das Flechtbild oben in voller
Breite; darunter schalten die Reiter **Geometrie**, **Farben** und
**Übersicht** die Bereiche um.

### Kopfzeile und Werkzeugleiste

| Element | Wirkung |
|---|---|
| **Produktname** | Name des Designs (Kopfzeile). |
| **Speicherort** (Ordner-Knopf neben dem Namen) | Zeigt den Ordner des Designs in der Bibliothek oder *Ohne Ordner*. Ein Klick öffnet den Ordnerbaum zur Auswahl. |
| **Ansicht**: **Voll** bzw. **Flechtbild** / **Halb** / **Zylinder**, **Vierkant** bzw. **Kante** / **3D** | *Voll* klappt den vollen Umfang flach auf (Abwicklung); bei Litze, Spirale und Soutache heißt der Knopf *Flechtbild*. *Halb* (nur Rundgeflecht) zeigt die halbe Abwicklung, also die Vorderseite. *Zylinder* (Rund), *Vierkant* (Quadrat) bzw. *Kante* (Packung) projiziert die Abwicklung drehbar auf den Körper. *3D* zeigt das echte Modell aus den Klöppelbahnen (siehe unten). |
| Nach links / rechts drehen | Nur in der Projektion: dreht den Körper um 15° je Klick; Gedrückthalten dreht weiter. |
| **Klöppelnummern** | Blendet die Klöppelbezeichnungen im Flechtbild ein oder aus. |
| **Textur** | Füllt die Kacheln des Flechtbilds mit einer Fasertextur statt glatter Farbe. |
| **Garn** | Nur ab Fachung 2: welches Garn ein Klick färbt (siehe [Fachungsfarben](#fachungsfarben-farbe-je-garn)). |
| **Rückgängig** / **Wiederholen** | Färbeschritte zurücknehmen bzw. wiederherstellen. |
| **Alle Farben löschen** | Setzt alle Klöppel auf ungefärbt. |
| **Drucken** | Öffnet die [Druckseite](print.md) mit der Design-Vorlage. |
| **Versionen** (Symbol) | Frühere Fassungen des Designs ansehen und wiederherstellen, siehe [Versionen und Papierkorb](versions.md). Erscheint, sobald das Design gespeichert ist. |
| **Vergrößern** / **Verkleinern** / **Einpassen** | Zoom des Flechtbilds; zusätzlich Mausrad (am Touchscreen zwei Finger) und Ziehen mit gedrückter Maustaste. |
| **Speichern** / **Als neu speichern** | Speichert das Design bzw. legt eine Kopie unter neuem Namen an. Beim Speichern entsteht das Vorschaubild für die Bibliothek. Kommen Sie aus einem Auftrag, heißt der Knopf **Speichern & zurück** und verknüpft das Design mit dem Auftrag. |

### Geometrie

| Feld | Bedeutung |
|---|---|
| **Geflechtsart** | Rundgeflecht, Litzengeflecht, Quadratgeflecht, Spiralgeflecht, Packungsgeflecht, Soutachegeflecht. |
| **Bahn-Art** | Nur Packungsgeflecht: Familie (2-, 3-, 4-bahnig, rund). |
| **Besetzung** | Bindung: Normal, Halb, Tandem usw. — je nach Geflechtsart. |
| **Klöppelanzahl** | Auswahlliste mit den zulässigen Klöppelzahlen der gewählten Geflechtsart und Bindung. |
| **Flechtwinkel** | Schieberegler; wirkt auf das Flechtbild und live auf die 3D-Ansicht. |
| **Fachung** | Anzahl der Fäden (Garne) je Klöppel, 1 bis 12. Ab 2 kann jedes Garn eine eigene Farbe bekommen, siehe [Fachungsfarben](#fachungsfarben-farbe-je-garn). |
| **Seelenfäden** | Nur Soutache: Seelen durch die Radachsen. |
| **Material-Ø** / **Bedeckung %** | Materialdurchmesser und Bedeckung; die Bedeckung steuert in der 3D-Ansicht die gezeichnete Fadendicke. |

Die Bedeutung dieser Parameter je Geflechtsart erklärt
[Geflechtsart und Parameter](../designer/parameters.md).

### Farben und Klöppeltabelle

* **Farbe:** Die Farbpalette aus Ihren [Farben-Stammdaten](master-data.md)
  und **Eigene Farbe** (Farbwähler). Die aktive Farbe ist hervorgehoben.
* **Färben:** Klicken Sie auf eine Kachel im **Flechtbild** oder auf eine
  Zeile der **Klöppeltabelle** — der Klöppel (bei Rund- und Quadratgeflecht:
  Index und Laufseite) übernimmt die aktive Farbe. Mit gedrückter Maustaste
  färben Sie mehrere Zeilen der Tabelle in einem Zug. Beim Zeigen auf eine
  Kachel nennt eine Einblendung den Klöppel.
* **Klöppeltabelle** (Karte **Klöppel**): je Klöppel eine Zeile mit der
  Klöppelnummer auf seiner Farbe. Bei Rund- und Quadratgeflecht stehen
  **Klöppel Links** und **Klöppel Rechts** als eigene Spalten nebeneinander,
  bei Packung und Spirale eine Spalte je **Bahn**; ist die Karte schmal,
  stehen sie untereinander. Wo ein Klöppel auf der Maschine sitzt, zeigt die
  Besetzungsübersicht. Die Belegung erscheint später so im Auftrag und auf
  dem Druck.

### Fachungsfarben: Farbe je Garn

Bei einer **Fachung** ab 2 laufen auf jedem Klöppel mehrere Garne
nebeneinander. Jedes dieser Garne kann eine eigene Farbe bekommen, zum
Beispiel ein schwarzes und ein weißes Garn auf demselben Klöppel. Garn 1
trägt die Farbe des Klöppels; ohne eigene Farben laufen alle Garne in
dieser Farbe.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Designer mit Fachung 2 und geöffnetem Dialog „Fachungsfarben – L1": Garn 1 und Garn 2 mit ihren Farben, darunter die Farbauswahl mit aktiver Farbe und Palette; im Hintergrund die Klöppeltabelle mit gestreiften Zellen.
    **So erzeugen:** Web-App lokal (127.0.0.1:5173), Seite `/designs/<id>`, Fachung 2, Rechtsklick auf eine Zeile der Klöppeltabelle; automatisch per `python _tools/web_screenshots.py shots nur:fachungsfarben`
    **Ziel-Datei:** `assets/screenshots/web/fachungsfarben.png`
    <!-- web-bild ../assets/screenshots/web/fachungsfarben.png -->

Sie färben Garne auf zwei Wegen:

=== "Mit dem Garn-Wähler"

    1. Wählen Sie in der Werkzeugleiste unter **Garn** das Garn, zum
       Beispiel **Garn 2**. Die Auswahl erscheint nur bei Fachung ab 2 und
       mit dem Recht *Designer bearbeiten*.
    2. Wählen Sie die Farbe in der Palette.
    3. Klicken Sie auf Zeilen der Klöppeltabelle oder auf Kacheln im
       Flechtbild. Es ändert sich nur das gewählte Garn, die anderen Garne
       behalten ihre Farbe.

    Mit **Alle Garne** färbt ein Klick wieder den ganzen Klöppel: Alle
    Garne bekommen die neue Farbe.

=== "Mit dem Dialog „Fachungsfarben""

    1. Klicken Sie mit der rechten Maustaste auf eine Zeile der
       Klöppeltabelle. Am Tablet und Smartphone halten Sie den Finger
       länger auf die Zeile.
    2. Der Dialog **Fachungsfarben – &lt;Klöppel&gt;** listet die Garne
       (**Garn 1**, **Garn 2** …) mit ihrer Farbe. Tippen Sie das Garn an,
       das Sie ändern wollen.
    3. Wählen Sie darunter die Farbe: die **Aktive Farbe** ganz links, eine
       Farbe der Palette oder über **Eigene Farbe wählen…** eine beliebige.
    4. Klicken Sie auf **Übernehmen**.

    **Alle wie Garn 1** gibt allen Garnen die Farbe von Garn 1 zurück.
    **Abbrechen** schließt den Dialog ohne Änderung.

**Rückgängig** und **Wiederholen** nehmen auch Garnfarben zurück. So
erscheinen die Garnfarben:

| Stelle | Darstellung |
|---|---|
| Klöppeltabelle | Die Zelle ist längs gestreift, Garn 1 links. Beim Zeigen auf die Zeile nennt eine Einblendung die Farbe jedes Garns. |
| Flechtbild | Jede Kachel ist längs zum Faden in Streifen je Garn geteilt, in allen Ansichten und auch mit **Textur**. Dünne Trennlinien zeigen die Fachung immer an, auch wenn alle Garne gleich gefärbt sind. |
| Besetzungsübersicht | Der Klöppelpunkt ist in Kreisstücke je Garn geteilt. |
| 3D-Ansicht | Jedes Garn als eigener Faden in seiner Farbe. Eigene Farben gibt es für höchstens zwölf Garne. |
| Druck | Die Klöppelliste zeigt die Streifen und die Farbe je Garn, Flechtbild und Übersicht sind wie im Designer gefärbt. |

!!! info "Desktop-App"
    Die Garnfarben werden mit dem Design gespeichert. Die Desktop-App zeigt
    sie erst ab einer späteren Programmversion an.

### Besetzungsübersicht

Die Draufsicht der Maschine mit Flügelrädern und Klöppeln unter dem
Flechtbild — mit **Gangbahn-Animation** (**Anhalten**, **Zurück auf
Anfang**, **Tempo**). Läuft die Animation in der 3D-Ansicht, wächst das
Geflecht synchron mit. Details zur Übersicht:
[Besetzung und Gangbahn-Animation](../designer/animation.md).

### 3D-Ansicht

Die Ansicht **3D** zeigt das Geflecht als räumliches Modell — jeder Faden
als Rohr, über/unter aus der Kinematik der Besetzungsübersicht, in den
Klöppelfarben. Sie funktioniert für alle sechs Geflechtsarten (Mischdesigns
ausgenommen).

| Element | Wirkung |
|---|---|
| **Draufsicht** / **Seitenansicht** / **Flechtpunkt** | Drei feste Kameraansichten: Querschnitt, ganzes Geflecht von der Seite, Nahaufnahme der Entstehungsstelle. |
| **Schloss** | Gesperrt: Maus und Finger drehen nicht, das Mausrad zoomt. Offen: linke Maustaste dreht, rechte verschiebt, Doppelklick stellt die gewählte Ansicht wieder her. |
| **Material** | Glattes Filament, gedrehtes Garn, Draht oder eine einfache Light-Version. |
| **Darstellung** | Vorgabe der Geflechtsart, *Nur Abbindung (Schema)*, *Automatisch* oder *Wie die Maschine steht* — bestimmt, ob der Querschnitt aus den Gangbahnen oder idealisiert hergeleitet wird. |
| **Bedeckung** | Zeile *Bedeckung n % (Fadendicke m %)*: die Fadendicke folgt der Bedeckung des Designs. |

Farbänderungen übernimmt das 3D sofort; Klöppelzahl, Bindung und Winkel
bauen das Modell neu auf (bei großen Maschinen dauert das einen Moment,
*Geflecht wird aufgebaut …*). Der Browser braucht WebGL — fehlt es, meldet
die Ansicht *„Dieser Browser kann kein WebGL darstellen."*

!!! info "Unterschied zur Desktop-App"
    Die Web-App zeigt ein Design je Seite — den Zwei-Fenster-Vergleich der
    Desktop-App gibt es nicht. Mischdesigns aus Rund- und Litzenabschnitten
    zeigt die Web-App an; anlegen lassen sie sich nur in der Desktop-App.
    Dafür hat die Web-App schon die [Fachungsfarben](#fachungsfarben-farbe-je-garn)
    und den Dialog [Versionen](versions.md).

## Verwandte Seiten

* [Designer (Desktop-App)](../designer/index.md) — Referenz mit allen Details
* [Geflechtsart und Parameter](../designer/parameters.md)
* [3D-Ansicht (Desktop-App)](../designer/view-3d.md)
* [Ein Design entwerfen und drucken](../tasks/design-from-scratch.md)
* [Drucken (Web-App)](print.md)
* [Versionen und Papierkorb](versions.md)
