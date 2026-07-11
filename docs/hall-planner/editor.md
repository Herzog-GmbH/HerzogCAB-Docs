# Hallenplaner-Editor

!!! abstract "Referenz — der Zeichen- und Bestückungs-Editor des Hallenplaners: Hallengeometrie zeichnen und Maschinen platzieren"

## Wofür Sie diesen Bereich nutzen

Der Editor ist die Arbeitsfläche des Hallenplaners. Er arbeitet in zwei Modi
mit derselben Oberfläche:

* **Geometrie-Modus** (Titel *Hallenlayout bearbeiten*) — Sie zeichnen die
  Halle selbst: Wände, Funktionsflächen und Bauelemente wie Türen und Tore.
  Einstieg: *Stammdaten > Grundrisse* > **Bearbeiten**.
* **Bestückungs-Modus** (Titel *Hallenplaner*) — Sie platzieren Maschinen auf
  einem fertigen Grundriss und richten sie aus. Einstieg:
  *Hallenplaner* > **Bestücken**. Die Hallengeometrie ist in diesem Modus
  gesperrt; welcher Grundriss bestückt wird, zeigt die Kopfzeile an
  (*Grundriss: …*).

Alle Objekte liegen maßstäblich auf der Zeichenfläche — Positionen und Maße
werden millimetergenau geführt und in der gewählten Einheit (Meter oder
Millimeter) angezeigt.

=== "Geometrie"

    !!! warning "📷 Screenshot fehlt"
        **Motiv:** Editor im Geometrie-Modus — links die Werkzeugleiste mit den Gruppen WERKZEUGE, WÄNDE, FLÄCHEN, OBJEKTE; Mitte ein Grundriss mit Wänden und einer farbigen Fläche; rechts das Eigenschaften-Panel (Reiter Layout)
        **So erzeugen:** *Stammdaten > Grundrisse* > Grundriss wählen > **Bearbeiten**; ein paar Wände und eine Produktionsfläche zeichnen
        **Ziel-Datei:** `assets/screenshots/hall-planner/editor-geometrie.png`

=== "Bestückung"

    !!! warning "📷 Screenshot fehlt"
        **Motiv:** Editor im Bestückungs-Modus — links WERKZEUGE + KATALOG mit Maschinenliste; über der Zeichenfläche die Auswahl-Toolbar (Bearbeiten · Ausrichten · Verteilen · Aneinanderreihen); mehrere platzierte Maschinen, davon zwei markiert; rechts das Eigenschaften-Panel mit Maschinen-Eigenschaften
        **So erzeugen:** *Hallenplaner* > Grundriss und Belegung wählen > **Bestücken**; zwei Maschinen markieren (Rahmen aufziehen)
        **Ziel-Datei:** `assets/screenshots/hall-planner/editor-bestueckung.png`

## Der Bildschirm im Überblick

| Bereich | Inhalt |
|---|---|
| **Kopf-Werkzeugleiste** (oben) | Zurück zur Übersicht, Layout-Auswahl, **Neu**, **Speichern**, ⋯-Menü, Ansicht-Schalter (Raster, Einrasten, 2D/3D). |
| **Werkzeugleiste** (links) | Werkzeuge zum Auswählen, Zeichnen und — im Bestückungs-Modus — der Maschinen-**Katalog**. |
| **Zeichenfläche** (Mitte) | Der maßstäbliche Plan; im Bestückungs-Modus darüber die Auswahl-Toolbar. |
| **Eigenschaften-Panel** (rechts) | Reiter **Auswahl** und **Layout** — Eigenschaften des markierten Objekts bzw. Einstellungen des gesamten Layouts. |
| **Statusleiste** (unten) | Cursor-Koordinaten, Messwert, aktives Werkzeug, Raster/Winkel, Auswahlanzahl und Zoom-Steuerung. |

## Bedienelemente im Detail

### Kopf-Werkzeugleiste

* **‹ Übersicht** — zurück zur Übersichtsseite (Grundrisse bzw. Hallenplaner).
  Bei ungespeicherten Änderungen fragt die App: *Das Layout „…" hat
  ungespeicherte Änderungen. Jetzt speichern?*
* ***Grundriss: …*** (nur Bestückungs-Modus) — zeigt, zu welchem Grundriss
  die bearbeitete Belegung gehört.
* **Auswahlliste** — wechselt im Geometrie-Modus zwischen den Grundrissen, im
  Bestückungs-Modus zwischen den Belegungen.
* **Neu** — legt im Geometrie-Modus einen neuen Grundriss an, im
  Bestückungs-Modus eine neue Belegung (bei mehreren Grundrissen fragt die App,
  für welchen Grundriss).
* **Speichern** — speichert das aktuelle Layout.
* **⋯** (Weitere Layout-Aktionen) — Menü mit **Umbenennen…**,
  **Duplizieren…** und **Löschen…** für den aktuellen Grundriss bzw. die
  aktuelle Belegung.
* **Ansicht:**
    * **Raster** — blendet das Zeichenraster ein/aus.
    * **Einrasten** — schaltet das Einrasten am Raster ein/aus.
    * **2D | 3D** — wechselt zwischen der Zeichenansicht und der
      [3D-Hallenansicht](view-3d.md) (öffnet ein eigenes Fenster).

### Linke Werkzeugleiste

Es ist immer genau **ein** Werkzeug aktiv. Die Gruppe **WERKZEUGE** ist in
beiden Modi vorhanden:

| Werkzeug | Funktion |
|---|---|
| **Auswählen** | Objekte anklicken, verschieben und markieren (Standard). Ein aufgezogener Rahmen markiert mehrere Maschinen. |
| **Verschieben** | Hand-Werkzeug: die Ansicht mit gedrückter Maustaste verschieben. |
| **Messen** | Zwei Punkte anklicken — die gemessene Länge erscheint unten in der Statusleiste. |

=== "Geometrie"

    Zusätzlich stehen im Geometrie-Modus drei Zeichengruppen bereit:

    **WÄNDE**

    * **Außenwand** — Außenwände als Klick-Kette zeichnen: nacheinander
      klicken, um einen Wandzug zu setzen; Rechtsklick oder ++esc++ beendet
      das Zeichnen.
    * **Innenwand** — Raumtrenner, gleiche Bedienung. Innenwände erhalten in
      der 3D-Ansicht beidseitig die Innen-Textur.

    **FLÄCHEN** — farbige Funktionsbereiche. Eckpunkte nacheinander anklicken;
    ein Klick auf den ersten Punkt (oder ++enter++) schließt die Fläche.
    Verfügbare Typen:

    * **Produktionsfläche**
    * **Transportweg**
    * **Lagerfläche**
    * **Wartung / Rüstplatz**
    * **Büro / Sozial**
    * **Qualitätskontrolle**
    * **Sonstige**

    **OBJEKTE** — Bauelemente:

    * **Tür**, **Tor**, **Fenster**, **Banner / Logo** — auf eine Wand
      klicken; das Element sitzt in der Wand und lässt sich anschließend an
      ihr entlang verschieben.
    * **Treppe** — auf eine freie Stelle klicken, um sie frei zu platzieren.

=== "Bestückung"

    Im Bestückungs-Modus ersetzt der **KATALOG** die Zeichengruppen:

    * **Maschine suchen…** — durchsucht Name, Typ, Seriennummer und Standort.
    * **Typ-Filter** — schränkt die Liste auf einen Maschinentyp ein
      (*Alle Typen* = kein Filter).
    * **Maschinenliste** — alle Maschinen aus den Stammdaten; enthält Ihr
      Park Flecht- **und** Spulmaschinen, ist die Liste entsprechend in die
      Abschnitte *Flechtmaschinen* und *Spulmaschinen* gegliedert. Jeder
      Eintrag zeigt Name, Typ, Seriennummer und die Stellmaße
      (L × B × H in Metern); fehlen die Maße, warnt der Eintrag mit
      *Maße fehlen*.
    * **Platzieren:** Maschine mit der Maus **auf die Zeichenfläche ziehen**
      — oder per **Doppelklick** in die Mitte der Ansicht setzen.
    * **Zähler** — zeigt, wie viele Maschinen der Filter durchlässt.

### Zeichenfläche

* **Zoomen** — Mausrad (an der Cursorposition) oder die Zoom-Schaltflächen in
  der Statusleiste.
* **Ansicht verschieben** — mit gedrückter **mittlerer Maustaste** oder mit
  dem Hand-Werkzeug **Verschieben**.
* **Markieren** — Klick auf ein Objekt; im Bestückungs-Modus zieht ein
  Rahmen mehrere Maschinen in die Auswahl.
* **Kontextmenüs** — die rechte Maustaste öffnet objektabhängige Menüs
  (siehe unten).
* Platzierte Maschinen zeigen — je nach Anzeige-Einstellung — ihre
  Beschriftung und eine kleine **Status-Ampel** mit dem aktuellen
  Auftragsstatus aus den [Aufträgen](../orders/index.md) (gleiche Farblogik
  wie im [Maschinenpark](../machine-park/index.md)).

**Tastenkürzel:**

| Taste | Wirkung |
|---|---|
| ++esc++ | Zeichnen abbrechen bzw. Auswahl aufheben |
| ++enter++ | Flächenzug schließen (beim Flächen-Zeichnen) |
| ++delete++ / ++backspace++ | markierte Objekte entfernen |
| ++ctrl+c++ / ++ctrl+v++ | markierte Maschinen kopieren und leicht versetzt einfügen |

### Auswahl-Toolbar (nur Bestückungs-Modus)

Oberhalb der Zeichenfläche liegt eine Leiste mit vier Funktionsblöcken. Die
Blöcke werden je nach Größe der Auswahl aktiv; ein ausgegrauter Block nennt im
Tooltip den Grund (z. B. *Mindestens zwei Maschinen auswählen*).

| Block | Ab | Schaltflächen |
|---|---|---|
| **Bearbeiten** | 1 Maschine | **90° links**, **90° rechts** (jede markierte Maschine drehen), **Duplizieren**, **Entfernen** (aus dem Layout) |
| **Ausrichten** | 2 Maschinen | **Links**, **H-Mitte**, **Rechts**, **Oben**, **V-Mitte**, **Unten** |
| **Verteilen** | 3 Maschinen | **Horizontal**, **Vertikal** — gleichmäßige Abstände |
| **Aneinanderreihen** | 2 Maschinen | **Horizontal**, **Vertikal** — lückenlos aneinanderlegen |

### Kontextmenüs (rechte Maustaste)

* **Maschine** (Bestückungs-Modus): **Ausrichten**-Untermenü (bei mehreren
  markierten Maschinen zusätzlich Verteilen und Aneinanderlegen), **90° nach
  links** / **90° nach rechts**, **Vorderseite** (Unten / Rechts / Oben /
  Links), **Duplizieren**, **Aus Layout entfernen**.
* **Wand** (Geometrie-Modus): **Wände verbinden** (zwei markierte Wände zu
  einer Ecke zusammenführen), **Als Innenwand/Außenwand markieren**,
  **Innen/Außen tauschen**, **Wand entfernen**.
* **Bauelement** (Geometrie-Modus): bei Türen **Anschlag spiegeln
  (links/rechts)** und **Aufschlag spiegeln (innen/außen)**; bei Türen und
  Toren **Tür/Tor öffnen** bzw. **schließen**; bei frei platzierbaren
  Elementen **90° drehen**; außerdem **Duplizieren** und **Element
  entfernen**.

### Eigenschaften-Panel (rechts)

Das Panel hat zwei Reiter: **Auswahl** (Eigenschaften des markierten Objekts)
und **Layout** (Einstellungen des gesamten Layouts). Ohne Auswahl zeigt der
Auswahl-Reiter den Hinweis, ein Objekt anzuklicken.

#### Reiter „Layout"

Karte **Allgemein**:

| Feld | Bedeutung |
|---|---|
| **Beschreibung** | Freitext zum Layout (optional). |
| **Einheit** | Anzeige-Einheit aller Maße: **Meter** oder **Millimeter**. |
| **Rastergröße** | Weite des Zeichenrasters in mm. |
| **Objektfang** | Beim Zeichnen an vorhandenen Objekten ausrichten. |
| **Winkelfang** | Wände/Kanten auf feste Winkelschritte einrasten; die Schrittweite (°) stellen Sie daneben ein. |

Karte **Grundriss** — hinterlegt ein Bild (Foto oder Plan) als maßstäbliche
Zeichenunterlage:

| Element | Bedeutung | Sichtbar in |
|---|---|---|
| **Bild laden…** | Grundriss-Bild über die [Medienbibliothek](../master-data/media.md) wählen; sehr große Bilder werden beim Import automatisch verkleinert. | Geometrie |
| **Ausrichtung** | Drehung des Bildes in Grad, mit Schnelltasten **−90°** / **+90°** — so richten Sie einen schief gescannten Plan am Raster aus. | Geometrie |
| **Maßstab setzen** | Kalibrierung: Sie klicken zwei Punkte einer bekannten Strecke auf dem Bild an und geben deren **tatsächliche Länge in Metern** ein — danach stimmen alle Maße. | Geometrie |
| **Entfernen** | Löst das Bild vom Layout; Wände und Maschinen bleiben erhalten. | Geometrie |
| **Grundrissbild anzeigen** | Blendet die Unterlage ein/aus. | Geometrie + Bestückung |
| **Transparenz** | Regler für die Deckkraft der Unterlage. | Geometrie + Bestückung |

!!! tip "Erst ausrichten, dann kalibrieren"
    Nach dem Laden empfiehlt die App die Reihenfolge: zuerst das Bild über
    **Ausrichtung** am Raster ausrichten, danach über **Maßstab setzen** die
    echte Länge festlegen.

Aufklappbare Karte **Wand-Textur (3D)** (nur Geometrie-Modus) — Texturen für
die [3D-Hallenansicht](view-3d.md):

* **Innen…** — Textur für die Innenseite der Wände laden.
* **Außen…** — optionale Textur für die Außenseite (leer = wie innen).
* **Kachelgröße** — Kachelmaß der Textur in mm.
* **Textur entfernen** — entfernt die hinterlegten Texturen.

#### Reiter „Auswahl" — Maschine

| Gruppe | Felder |
|---|---|
| **Maschine** | Name, Identnummer, Typ und **Maße (L × B × H)** aus den Stammdaten (schreibgeschützt) sowie der aktuelle Auftragsstatus. Fehlen die Maße, zeigt das Panel *Keine Maße hinterlegt (Ersatzgröße 2,0 × 1,0 × 1,5 m)*. |
| **Platzierung** | **Position X**, **Position Y**, **Rotation** (°), **Vorderseite** (Unten / Rechts / Oben / Links — bestimmt, welche Seite als Bedienseite gilt). |
| **Anzeige** | **Beschriftung** (Name + Seriennummer · Nur Name · Nur Seriennummer · Nur Maschinentyp · Nicht anzeigen), **Eigener Text** (überschreibt die Auswahl), **Statusampel anzeigen**. |
| Aktionen | **Duplizieren**, **Entfernen** — *Entfernen löscht nur die Platzierung im Layout, nicht die Maschine aus den Stammdaten.* |

#### Reiter „Auswahl" — Wand

* **Maße:** Länge und Winkel (schreibgeschützt), **Dicke** in mm.
* **Typ & Optionen:** **Innenwand (beidseitig innen)**,
  **Innen-/Außenseite tauschen** (welche Wandseite in der 3D-Ansicht die
  Außen-Textur erhält).
* **Position** (aufklappbar): **Start X/Y** und **Ende X/Y** — für exakte
  Koordinaten; alternativ ziehen Sie die Endpunkt-Anfasser direkt auf der
  Zeichenfläche.
* **Wand entfernen**.

#### Reiter „Auswahl" — Bereich (Fläche)

* **Typ** — der Flächentyp (siehe Liste oben), nachträglich änderbar.
* **Bezeichnung** — eigener Name (leer = Typname).
* **Fläche** — berechnete Größe des Bereichs (schreibgeschützt).
* **Bereich entfernen**.

#### Reiter „Auswahl" — Bauelement

Angezeigt werden nur die zum Elementtyp passenden Felder:

| Feld | Gilt für | Bedeutung |
|---|---|---|
| **Typ** | alle | Elementtyp (schreibgeschützt). |
| **Breite** | alle | Elementbreite in mm. |
| **Position an Wand** | Tür, Tor, Fenster, Banner | Lage entlang der Wand in Prozent. |
| **Türtyp** | Tür | Stahltür mit Sichtfenster · Füllungstür (Holz) · Glastür. |
| **Anschlag** | Tür | Links / Rechts. |
| **Aufschlag** | Tür | Innen / Außen. |
| **Offen darstellen** | Tür, Tor | Zeigt das Element geöffnet. |
| **Wandseite** | Banner | Innenseite / Außenseite. |
| **Banner-Bild** | Banner | **Bild/Logo laden…** — Bild für die Darstellung (auch in 3D). |
| **Stufen** | Treppe | Anzahl der Stufen. |
| **Rotation** | Treppe | Drehung in Grad. |
| **Bezeichnung** | alle | Eigener Text (optional). |

Dazu die Schaltfläche **Element entfernen**.

### Statusleiste

* **X / Y** — die Cursorposition in der gewählten Einheit.
* **Länge …** — Live-Länge beim Messen und Zeichnen.
* **Werkzeug · Raster · Winkel · Auswahl** — aktives Werkzeug, Rasterweite,
  Winkelfang-Schrittweite und Anzahl markierter Objekte.
* **− / Zoomwert / +** und **Einpassen** — Zoom-Steuerung; **Einpassen**
  bringt den gesamten Inhalt ins Bild.

## Speichern und Rechte

Änderungen werden erst mit **Speichern** übernommen; beim Verlassen, beim
Wechsel des Layouts und beim Beenden fragt die App nach ungespeicherten
Änderungen. Das Bearbeiten von Grundrissen erfordert das
Stammdaten-Bearbeitungsrecht, das Bestücken das Hallenplaner-Bearbeitungsrecht
(siehe [Rollen](../admin/roles.md)).

## Verwandte Seiten

* [Hallenplaner-Übersicht](index.md) — Grundrisse, Belegungen und
  Ist-Belegung verwalten.
* [3D-Hallenansicht](view-3d.md) — das Ergebnis dreidimensional betrachten.
* [Grundrisse (Stammdaten)](../master-data/floor-plans.md) — Grundrisse
  anlegen, umbenennen, duplizieren, löschen.
* [Medien](../master-data/media.md) — Bildquellen für Grundriss-Unterlage,
  Texturen und Banner.
* [Eine Halle aufbauen](../tasks/build-hall.md) — der komplette Ablauf als
  Anleitung.
