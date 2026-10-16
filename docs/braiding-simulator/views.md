# 3D-Vorschau und Abzug

!!! abstract "Referenz — Die 3D-Vorschau des Flechtsimulators mit Geflecht, Schema und Maschine sowie die Dialoge für Abzug und Drehzahl"

## Wofür Sie diesen Bereich nutzen

Rechts neben der Maschinenansicht zeigt die **3D-Vorschau**, was aus der
Besetzung und dem Programm wird: das entstehende **Geflecht**, das
**Schema** der Abbindung oder die bestückte **Maschine** mit Fäden,
Flechtpunkt und Abzugsscheibe. Die Vorschau läuft mit der Simulation mit.
Über **Abzug** und **Drehzahl** legen Sie fest, mit welchem Flechtwinkel,
welcher Schlaglänge und welcher Geschwindigkeit das Programm flicht; diese
Werte stehen im Zeitprogramm und kommen in den
[Schaltplan](output.md).

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Flechtsimulator mit bestückter Maschine links und der 3D-Vorschau rechts im Modus „Geflecht“, Seitenansicht, darunter die Infozeilen; das Zahnrad-Fenster „3D-Vorschau“ ist geöffnet.
    **So erzeugen:** Kundenbuild mit Modell-Lizenz, Flechtsimulator > Maschine öffnen > Konfiguration von Herzog laden, einige Schritte abspielen, Zahnrad oben an der 3D-Vorschau klicken.
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/vorschau-geflecht.png`

Oben an der 3D-Vorschau liegen von links nach rechts:

1. der Umschalter **Geflecht** | **Schema** | **Maschine**,
2. das Info-Symbol **ⓘ** (nur Kurzhinweis zur Bedienung mit der Maus),
3. das **Zahnrad** mit den Einstellungen der 3D-Vorschau,
4. **✕** zum Ausblenden.

Im Bild selbst stehen oben die festen Ansichten, unter dem Bild ein bis
zwei Infozeilen. Den Platz zwischen Maschine und 3D-Vorschau verteilen Sie
mit dem Teiler dazwischen (*Ziehen: Platz zwischen Maschine und
3D-Vorschau verteilen*).

## Bedienelemente im Detail

### Geflecht, Schema, Maschine

| Modus | Zeigt |
|---|---|
| **Geflecht** | *Das entstehende Geflecht in 3D.* Die Klöppelfarben, die Fachung und der [Materialdurchmesser](populate.md#garn) bestimmen das Bild. Das ist der Standard. |
| **Schema** | *Nur die Abbindung: Fadenfolge und Über- und Unterkreuzungen, ohne Radpositionen und Radgrößen.* Hilfreich, um die Bindung zu prüfen, wenn das Geflecht im Bild sehr dicht oder flach ist. |
| **Maschine** | *Die bestückte Maschine in 3D: Klöppel, Fäden zum Flechtpunkt, das Geflecht bis zur Abzugsscheibe.* Siehe [Ansicht „Maschine“](#ansicht-maschine). |

Die Wahl merkt sich das Programm. **✕** blendet die Vorschau aus (*zurück
über „Ansicht“*); wieder ein schalten Sie sie im Menü **Ansicht** der
Kopfzeile mit **3D-Vorschau**.

### Feste Ansichten und Schloss

Im Modus **Geflecht** und **Schema** stehen oben im Bild drei feste
Ansichten:

| Ansicht | Zeigt |
|---|---|
| **Draufsicht** | Blick auf den Querschnitt, so orientiert wie die Maschine in der Zeichnung. |
| **Seitenansicht** | Das ganze Geflecht von der Seite, also das Flechtbild. Das ist der Standard. |
| **Flechtpunkt** | Nahaufnahme der Stelle, an der das Geflecht gerade entsteht. Die Kamera folgt der Simulation; am besten mit **Geflecht während der Simulation aufbauen**. |

Rechts daneben liegt das **Schloss**. Gesperrt (Standard) dreht die Maus
das Geflecht nicht; das Mausrad zoomt trotzdem. Ziehen Sie gesperrt,
erscheint kurz *Ansicht gesperrt — zum Drehen das Schloss öffnen*. Offen
gilt:

| Aktion | Bedienung |
|---|---|
| Drehen | Linke Maustaste ziehen |
| Verschieben | Rechte Maustaste ziehen |
| Zoomen | Mausrad |
| Gewählte Ansicht wiederherstellen | Doppelklick |

### Anzeigen im leeren Bild

| Anzeige | Bedeutung |
|---|---|
| *Keine Maschine geladen* | Es ist noch keine Maschine geöffnet. |
| *Keine Klöppel gesetzt — Besetzung wählen, dann entsteht hier das Geflecht.* | Die Maschine ist leer. Wählen Sie oben eine **Besetzung** oder [bestücken](populate.md) Sie die Maschine. |
| *Start drücken — das Geflecht wird mit der Simulation aufgebaut.* | **Geflecht während der Simulation aufbauen** ist an; das Geflecht wächst ab **Start**. |
| *⛔ Kollision bei Schritt n — das Geflecht endet hier* | Zwei Klöppel treffen aufeinander. Das Geflecht wird nur bis zu diesem Schritt gezeichnet. Wie Sie Kollisionen finden, steht unter [Prüfen](check.md). |
| *⛔ Sackgasse bei Schritt n — das Geflecht endet hier* | Ein Klöppel kommt nicht weiter, zum Beispiel an einer falsch gestellten Weiche. |

### Einstellungen der 3D-Vorschau (Zahnrad)

Das Zahnrad öffnet das Fenster **3D-Vorschau**:

| Einstellung | Wirkung |
|---|---|
| **Flechtwinkel** | Regler für die Steigung der Fäden im Bild (Standard 45°), angezeigt im [gewählten Bezug](#flechtwinkel-bezug). Hat das Programm einen [Abzug](#abzug), ist der Regler gesperrt: *Der Flechtwinkel kommt aus dem Abzug im Zeitprogramm (Zeile „Abzug" der Zeitachse).* |
| **Material** | **Glattes Filament**, **Gedrehtes Garn** (Standard), **Draht** oder **Einfache Darstellung**. Bestimmt nur Faserstruktur, Rauheit und Glanz. Die einfache Darstellung ist schneller und hilft bei schwacher Grafik. Die Klöppelfarben bleiben in allen Modi erhalten. |
| **Querschnitt wie die Radanordnung** | Zeigt den Querschnitt genau wie die Radanordnung der Maschine, ohne Umrechnung: die Ansicht für die Fehlersuche. Aus (Standard) zeigt das Geflecht, wie es die Maschine verlässt; Litzen-Betrieb und mehrere Flechtkreise erkennt die Vorschau dann selbst. Der Schalter wird nicht gespeichert. |
| **Geparkte Fäden bündig abschneiden** | Nur sichtbar, wenn das Programm Klöppel auf einem Switch-out-Rad parkt. Aus (Standard): Die Fäden der geparkten Klöppel stehen außen am Geflecht und laufen wieder hinein, wenn der Klöppel zurückkommt, so wie beim Flechten. Ein: Diese Strecke ist bündig abgeschnitten, so wie am fertigen Geflecht. |
| **Geflecht während der Simulation aufbauen** | Ein: Das Geflecht wächst ab **Start** mit der Klöppelbewegung. Aus: Das vollständige Geflecht ist sofort sichtbar. |
| **3D-Ausrichtung** | **Oben → unten** oder **Unten → oben**. Dreht nur die Anzeige; Simulation, Abzug und Flechtrichtung bleiben unverändert. |
| **Zettelfäden** | Nur bei Maschinen mit Rohren: Dicke der Zettelfäden im Bild, 20 bis 250 %. |

Den Materialdurchmesser und die Bedeckung stellen Sie nicht hier ein,
sondern unter [Bestücken > Garn](populate.md#garn): Sie gehören zur
Besetzung.

### Infozeilen unter dem Bild

Die erste Zeile beginnt mit **Gezeigt:** und sagt, wie die Vorschau das
Geflecht aufbaut, zum Beispiel:

* *Rundgeflecht*, *Litze, flach gezogen* oder *2 Rundgeflechte
  nebeneinander*,
* *2 Flechtkreise aufeinandergelegt* oder *2 Flechtkreise so weit
  auseinander wie in der Maschine*,
* *dünner, solange Klöppel geparkt sind (12 statt 16 Klöppel)*,
* *nichts umgerechnet* bei **Querschnitt wie die Radanordnung**,
* *Flechtwinkel wirksam …° statt …° (das Geflecht wird länger, damit die
  Bänder Platz haben)* oder *mehr Garn passt nicht mehr, das Bild bleibt
  stehen*, wenn das Material im eingestellten Winkel nicht mehr
  nebeneinander passt.

Im Modus **Schema** steht dort *Gezeigt: Abbindungsschema, ohne
Radpositionen und Radgrößen.*

Die zweite Zeile nennt das Maß, sobald es einen Maßstab gibt (einen
[Materialdurchmesser](populate.md#garn) oder einen eingezogenen Kern):
*Geflecht Ø … mm* oder *Litze … mm breit*, gegebenenfalls *über Kern Ø
… mm*, *· Bedeckung … %* und die Breite des Bandes eines Klöppels. Die
Schlaglänge steht nicht hier, sondern in der
[Zusammenfassung des Abzugs](program.md#drehzahl-und-abzug) und an der
Abzugsscheibe in der Ansicht **Maschine**.

## Ansicht „Maschine“ { #ansicht-maschine }

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Ansicht „Maschine“ der 3D-Vorschau: bestückte Maschine mit Spulen in Garnfarben, Fäden zum Flechtpunkt, Geflecht bis zur Abzugsscheibe; Beschriftungen Abzug, Schlaglänge, U/min, Flechtwinkel.
    **So erzeugen:** Wie oben, Umschalter auf „Maschine“, feste Ansicht „Gesamt“, Programm mit Abzug und Drehzahl abspielen.
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/vorschau-maschine.png`

Die Ansicht zeigt die bestückte Maschine schematisch, so wie sie das
Geflecht produziert: Klöppel mit Spulen in den Garnfarben auf der
Gangplatte, die Fäden zum Flechtpunkt, das Geflecht bis zur
Abzugsscheibe und ein Stück darüber hinaus. Räder und Scheibe laufen mit
der Simulation. Das Gestell ist eine typische Bauform (Tisch, Portal,
liegend, Gehäuse des Variationsflechters), kein Abbild Ihrer Maschine.
Aufwickler zeigt die Ansicht nicht.

| Feste Ansicht | Zeigt |
|---|---|
| **Gesamt** | Die ganze Maschine: Klöppel, Flechtpunkt, Geflecht und Abzug. |
| **Flechtpunkt** | Nahaufnahme des Flechtpunkts: hier laufen die Fäden zusammen und das Geflecht entsteht. |
| **Abzug** | Die Abzugsscheibe mit dem Geflecht. |

Linke Maustaste ziehen dreht, rechte verschiebt, das Mausrad zoomt zum
Mauszeiger, ein Doppelklick stellt die gewählte Ansicht wieder her. Ein
Schloss gibt es hier nicht.

Im Bild stehen an der Scheibe der Abzug in m/min und die Schlaglänge, am
Antrieb die Drehzahl (oder *Drehzahl fehlt*), am Flechtpunkt der
Flechtwinkel und am Geflecht Durchmesser bzw. Breite und Bedeckung.

* **Klick auf die Abzugsscheibe** öffnet den [Abzug](#abzug) für den
  Bereich am Abspielkopf.
* **Klick auf den Antrieb** öffnet die [Drehzahl](#drehzahl).

Ohne Programm meldet ein Klick *Abzug und Drehzahl stehen im Zeitprogramm.
Ohne Programm zeigt das Bild den Flechtwinkel der Vorschau.*

## Abzug { #abzug }

Der Abzug bestimmt, wie schnell das Geflecht von der Maschine gezogen wird,
und damit Flechtwinkel, Schlaglänge und PPI. Er gehört zum Zeitprogramm
und gilt ab einem Schritt bis zum nächsten Abzugswechsel. An dieser Stelle
springt er um; eine Rampe gibt es nicht.

So öffnen Sie den Dialog:

* in der Zeitachse ein Klick in die Zeile **Abzug** (ab diesem Schritt)
  oder Ziehen über einen Bereich (nur für diesen Bereich), siehe
  [Programm](program.md#abzug-und-drehzahl-in-der-zeitachse),
* in der Aufgabe **Programm** mit **Abzug ändern…** (ab dem Schritt am
  Abspielkopf),
* in der Ansicht **Maschine** mit einem Klick auf die Abzugsscheibe.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Dialog „Abzug ab Schritt 1“ mit Vorgabe Flechtwinkel, Wert 30°, Flügelraddrehzahl, Materialdurchmesser und der Ergebnistabelle.
    **So erzeugen:** Programm wählen, in der Zeitachse in die Zeile „Abzug“ bei Schritt 1 klicken.
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/abzug-dialog.png`

Der Titel lautet *Abzug ab Schritt n* oder, für einen gezogenen Bereich,
*Abzug für Schritt n bis m*. Darunter: *Eine Größe vorgeben, die anderen
folgen daraus.*

| Bereich | Feld | Bedeutung |
|---|---|---|
| **Vorgabe** | **Größe** | Welche Größe Sie vorgeben: **Abzug [m/min]**, **Schlaglänge [mm]**, **Flechtwinkel [°]** oder **PPI [1/Zoll]**. Wechseln Sie die Größe, rechnet der Dialog denselben Abzug in die neue Größe um. |
| | **Wert** | Der Wert der gewählten Größe. Den Flechtwinkel zeigt der Dialog im [gewählten Bezug](#flechtwinkel-bezug). |
| | **Flügelraddrehzahl** | Nur Anzeige: die Drehzahl an diesem Schritt oder *nicht gesetzt*. Sie stellen sie in der Zeile **Drehzahl** ein; ändert sie sich, läuft der Abzug mit. |
| **Für das ganze Programm** | **Materialdurchmesser** | Durchmesser **eines** Garns in mm. Er gibt der Vorschau den Maßstab. Der Wert gehört zur Besetzung, siehe [Bestücken > Garn](populate.md#garn). |
| **Ergibt** | Tabelle | Abzug (m/min), **Abzug je Flügelradumdrehung** (mm), Schlaglänge (mm), Flechtwinkel, PPI, **Geflechtsdurchmesser** (bei der Litze **Geflechtsbreite**) und **Bedeckung**. Die vorgegebene Größe steht fett. Durchmesser und Bedeckung sind immer Ergebnis. |

Orangefarbene Hinweise im Dialog:

| Hinweis | Was zu tun ist |
|---|---|
| *Materialdurchmesser fehlt: Abzug, Schlaglänge und PPI lassen sich nicht in den Flechtwinkel umrechnen.* | Materialdurchmesser eintragen. |
| *Flügelraddrehzahl fehlt: der Abzug in m/min ist unbekannt.* | In der Zeile **Drehzahl** eine Drehzahl setzen. |
| *Der Klöppelumlauf ist in diesem Bereich nicht bestimmbar: Schlaglänge und PPI fehlen.* | Im Bereich laufen die Klöppel nicht vollständig um (zum Beispiel beim Umschalten); nur Abzug und Winkel sind bestimmbar. |
| *Bei diesem Winkel passt das Material nicht auf den Kern: die Bedeckung läge über 100 %.* | Winkel ändern oder dünneres Material wählen. |
| *Die Schlaglänge ist kürzer, als das Material nebeneinander Platz braucht: so dicht lässt sich nicht flechten.* | Längere Schlaglänge bzw. kleineren Flechtwinkel vorgeben. |

**Übernehmen** setzt den Abzugswechsel, **Abbrechen** verwirft.
**Abzugswechsel entfernen** erscheint, wenn an diesem Schritt schon ein
Wechsel steht. Hatte das Programm noch keinen Abzug, beginnt der Dialog
mit der Größe *Flechtwinkel* und dem Winkel der Vorschau. Nach einem
gezogenen Bereich gilt wieder der Abzug davor.

## Drehzahl { #drehzahl }

Die **Flügelraddrehzahl** in U/min gibt dem Programm seine Zeit: Aus ihr
folgen die Dauer, der Abzug in m/min und das **Maschinentempo** der
Wiedergabe. Sie öffnen den Dialog über die Zeile **Drehzahl** der
Zeitachse, mit **Drehzahl ändern…** in der Aufgabe **Programm** oder mit
einem Klick auf den Antrieb in der Ansicht **Maschine**.

Der Titel lautet *Startdrehzahl des Programms* (Schritt 1), *Drehzahl ab
Schritt n* oder *Drehzahl für Schritt n bis m*. Der Hinweis erklärt:
*Alle Flügelräder laufen synchron mit dieser Drehzahl. Der Abzug läuft
mit: Schlaglänge und Flechtwinkel bleiben, es ändern sich nur der Abzug in
m/min und die Zeit.*

| Feld | Bedeutung |
|---|---|
| **Drehzahl** | 0 bis 2000 U/min; 0 heißt *nicht gesetzt*. |
| **Drehzahlwechsel entfernen** | Entfernt den Wechsel an diesem Schritt (nicht bei Schritt 1). |

## Flechtwinkel-Bezug { #flechtwinkel-bezug }

Der Simulator zeigt den Flechtwinkel in dem Bezug, den Sie unter
*Einstellungen > Allgemein > Flechtwinkel* gewählt haben:
**Zur Querrichtung (Herzog)** oder **Zur Geflechtsachse (Fachliteratur)**,
siehe [Flechtwinkel-Einstellung](../admin/settings/appearance.md#flechtwinkel).
Das gilt für den Regler im Zahnrad-Fenster (bei Bezug zur Geflechtsachse
läuft er umgekehrt), den Abzug-Dialog, die Zeitachse, die Zusammenfassung,
die Infozeilen und die Beschriftung in der Ansicht **Maschine**.

Die Beschriftungen nennen den Bezug nicht. Zeigen Sie mit der Maus auf
einen Winkel, nennt der Kurzhinweis beide Werte, zum Beispiel *30,0° zur
Querrichtung (Herzog) = 60,0° zur Geflechtsachse (Fachliteratur)*. Der
[Schaltplan](output.md) nennt den Bezug in der Zeile **Flechtwinkel
gemessen zur**. Gespeichert wird immer gleich; ein Wechsel des Bezugs
ändert kein Programm.

## Startwerte in den Einstellungen

Im Programm gibt es unter *Einstellungen* den Reiter **Flechtsimulator**
mit persönlichen Startwerten:

| Bereich | Einstellung | Wirkung |
|---|---|---|
| **Wiedergabe** | **Geflecht während der Simulation aufbauen** | Startwert für den gleichnamigen Schalter im Zahnrad-Fenster. |
| | **Standardgeschwindigkeit** | Tempo, mit dem die Wiedergabe startet (0,5 bis 4 Schritte/s). |
| **3D-Vorschau** | **3D-Ausrichtung** | Startwert für **Oben → unten** bzw. **Unten → oben**. |

## In der Web-App

Die 3D-Vorschau ist gleich aufgebaut. Abweichungen:

* Ein Knopf **Vollbild** vergrößert die Vorschau.
* In der Ansicht **Maschine** gibt es das Schloss nur auf Touch-Geräten.
* Ist der Flechtwinkel-Regler gesperrt, zeigt er den Winkel des längsten
  Abzugsbereichs.
* Der Reiter **Flechtsimulator** in den Einstellungen fehlt; Ausrichtung
  und Aufbau stellen Sie im Zahnrad ein, der Browser merkt sie sich.
* Am Smartphone ist die Vorschau zunächst gesperrt, damit ein Finger die
  Seite rollt.

Einzelheiten: [Flechtsimulator in der Web-App](../web/braiding-simulator.md).

## Verwandte Seiten

* [Bestücken](populate.md) — Materialdurchmesser und Bedeckung.
* [Programm](program.md) — Zeilen **Abzug** und **Drehzahl** der
  Zeitachse.
* [Ausgeben](output.md) — Abzugsbereiche im Schaltplan.
* [Flechtwinkel](../calculations/product/braid-angle.md) und
  [Flechtwinkel über Abzug](../calculations/product/braid-angle-takeup.md)
  — dieselben Größen als Berechnung.
