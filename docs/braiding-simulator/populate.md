# Bestücken

!!! abstract "Referenz — Die Aufgabe „Bestücken“: Klöppel setzen und entfernen, Farben, Fachung und Nummern, Garn und Bedeckung, Rohrfäden und Besetzungen speichern"

## Wofür Sie diesen Bereich nutzen

Bevor ein Programm laufen kann, braucht die Maschine Klöppel. Das
Maschinenmodell kommt leer: Sie setzen die Klöppel selbst oder wählen oben
eine gespeicherte **Besetzung** und passen sie an. Farben, Fachung und
Garn bestimmen, wie das Geflecht in der [3D-Vorschau](views.md) aussieht;
zusammen speichern Sie alles als **Besetzung**. Auf einer Besetzung legen
Sie danach Ihre Programme an.

Klöppel setzen und entfernen gehört immer zur Besetzung, nie zum
Programm. Auch während der Aufnahme wird daraus kein Programmbefehl.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Aufgabe „Bestücken“ mit den Gruppen Klöppel (Farbe für neue Klöppel, Alle Klöppel auswählen, Alle Klöppel entfernen), Garn (Materialdurchmesser, Bedeckung) und Besetzung; darüber die Auswahlkarte eines Klöppels mit Fachung 3 und Einzelfarben.
    **So erzeugen:** Kundenbuild mit Modell-Lizenz, Maschine öffnen, Reiter „Bestücken“, einen Klöppel anklicken und Fachung auf 3 stellen.
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/bestuecken.png`

In der Aufgabe **Bestücken** gilt in der Maschinenansicht:

* **Klick auf einen leeren Platz** setzt einen Klöppel in der Farbe für
  neue Klöppel.
* **Klick auf einen Klöppel** wählt ihn aus; die
  [Auswahlkarte](#auswahlkarte-kloppel) zeigt seine Eigenschaften.
* **Rechtsklick auf einen Klöppel** entfernt ihn.
* **++ctrl++ + Klick** bzw. **++ctrl++ + Ziehen** wählt mehrere Klöppel,
  **++ctrl+a++** alle.
* **Klick auf ein leeres Rohr** zieht den Faden ein, siehe
  [Rohrfäden](#rohrfaden).

Setzen Sie mitten im Lauf einen Klöppel, stellt der Simulator ihn in der
Startaufstellung dorthin, von wo er genau zu dieser Stelle läuft. Geht das
ohne Kollision nicht, meldet er *Hier lässt sich bei … kein Klöppel
einsetzen*; setzen Sie ihn dann am Start oder auf einen anderen Platz.

## Bedienelemente im Detail

### Gruppe „Klöppel“

| Element | Wirkung |
|---|---|
| **Farbe für neue Klöppel** | Knopf mit der aktuellen Setzfarbe. Ein Klick öffnet die Auswahl: **Standardfarben** aus der [Farbbibliothek](../master-data/colors.md), **Zuletzt verwendet** und **Eigene Farbe wählen…**. Neue Klöppel bekommen immer die gewählte Farbe; Standard ist Blau. Klöppel ohne eigene Farbe aus älteren Besetzungen behalten ihre automatisch verteilten Farben. |
| **Alle Klöppel auswählen** | Wählt alle Klöppel, um Fachung, Anordnung oder Farbe gemeinsam zu ändern (in der Maschine auch ++ctrl+a++). |
| **Alle Klöppel entfernen** | Nimmt nach Rückfrage alle Klöppel von der Maschine. Eine gespeicherte Besetzung bleibt erhalten; die Liste **Besetzung** zeigt danach keine Besetzung mehr an. |

### Gruppe „Garn“ { #garn }

| Feld | Bedeutung |
|---|---|
| **Materialdurchmesser** | Durchmesser **eines** Garns in mm (wie in der [Berechnung](../calculations/material/material-diameter.md)), 0,05 bis 50 mm. Bei einer Fachung ist das Band eines Klöppels so viele Garne breit. Der Wert gibt der 3D-Vorschau den Maßstab: Ohne Kern zieht sich das Geflecht bis zur eingestellten Bedeckung zusammen, und sein Durchmesser folgt aus dem Garn. Mit Kern ergibt sich aus Kern und Garn, wie dicht die Fäden den Kern bedecken. Es ist derselbe Wert wie im [Abzug](views.md#abzug). **✕** löscht den Wert der Besetzung; dann gilt der Wert eines älteren Programms bzw. die Vorgabe dieses PCs. |
| **Bedeckung** | Wie dicht das Material das Geflecht bedeckt, gerechnet wie in der Berechnung [Bedeckung](../calculations/tubular-braid/tube-cover.md) (bei der Litze der Füllungsgrad), 30 bis 100 % in Schritten von 5. 100 % heißt dicht zusammengezogen wie auf der Maschine. Weniger lässt das Geflecht bei gleichem Material weiter; Durchmesser, Schlaglänge und Abzug folgen daraus. |

Materialdurchmesser und Bedeckung gehören zur **Besetzung** wie Farbe und
Fachung und werden mit ihr gespeichert. Das Programm bleibt unverändert;
nur bei einem eigenen Programm mit Abzug rechnet der Simulator die m/min
neu.

Die Bedeckung lässt sich nur **ohne Kern** einstellen:

* **Mit Kern** ergibt sie sich aus Kern, Garn und Flechtwinkel; das Feld
  zeigt sie nur an.
* **Spirale** und kompakte Querschnitte wie die **Packung** sind immer
  voll; das Feld steht auf 100 % und ist gesperrt.

Kann die Vorschau bei einem sehr flachen Winkel so wenig Bedeckung nicht
zeichnen, meldet sie *Bei …° kann die Vorschau so wenig Bedeckung nicht
zeichnen: eingestellt sind … %, das Bild zeigt … %. Der Abzug rechnet mit
… %.*

### Rohrfäden { #rohrfaden }

Hat die Maschine Rohre, steht in der Gruppe **Garn** der Hinweis *Rohre:
ein Klick auf ein Rohr zieht den Faden ein; Farbe und Kerndurchmesser
stehen dann oben in der Karte.*

| Rohr | Faden |
|---|---|
| **Mitleitrohr** (in der Radmitte) | Zettelfaden |
| **Zettelfadenrohr** (zwischen Rädern) | Zettelfaden |
| **Zentralrohr** (Maschinenmitte) | Kern |

Ein Klick auf ein leeres Rohr zieht den Faden ein (*Mitleitrohr Z3:
Zettelfaden eingezogen.*). Ein Klick auf ein Rohr mit Faden wählt es nur
aus. Ausziehen, Farbe und Kerndurchmesser stellen Sie in der
[Auswahlkarte](#rohr) ein. Die Rohrfäden gehören zur Besetzung.

### Gruppe „Besetzung“

**Als neue Besetzung speichern…** legt die aktuelle Aufstellung als neue
Besetzung an (dasselbe wie im Menü **⋯** neben **Besetzung**), siehe
[Besetzung speichern](#besetzung-speichern). Der Hinweis darunter
erinnert: *„Speichern“ oben schreibt Änderungen in die gewählte Besetzung
zurück.*

## Auswahlkarte: Klöppel und Rohr { #auswahlkarte-kloppel }

### Ein Klöppel

Die Karte heißt *Klöppel n ausgewählt* bzw. bei einem leeren Platz *Rad n
· Platz m ausgewählt* und zeigt *Besetzt mit Klöppel n · 2 Garne.* oder
*Leer.*

| Feld | Bedeutung |
|---|---|
| **Fachung** | Anzahl parallel geführter Garne auf diesem Klöppel, 1 bis 12. |
| **Anordnung** | **Kompakt gepackt** hält den Gesamtfaden annähernd rund. **Flach nebeneinander** legt alle Garne nebeneinander und macht den Gesamtfaden breiter und dünner. |
| **Einzelfarben** | Knopf *1 Farbe…* bzw. *n Farben…*: öffnet **Einzelfarben der Fachung** mit einer Farbe je Garn. Auch die Farbe eines Klöppels mit Fachung 1 ändern Sie hier. |
| **Nummer** | Die Klöppelnummer. Neue Klöppel bekommen automatisch die kleinste freie Nummer (*Automatisch vergeben*); Sie können sie überschreiben. Trägt ein anderer Klöppel die Nummer schon, bietet das Programm an, die Nummern zu tauschen (**Nummern tauschen**). Jede Nummer gibt es nur einmal. |
| **Klöppel entfernen** / **Klöppel setzen** | Entfernt den Klöppel bzw. setzt einen auf den leeren Platz. |

### Mehrere Klöppel

Bei *n Klöppel ausgewählt* gelten Änderungen sofort für die ganze Auswahl.
Unterschiedliche Ausgangswerte zeigt die Karte als *— unterschiedlich —*.

| Element | Wirkung |
|---|---|
| **Fachung**, **Anordnung** | Für alle ausgewählten Klöppel. |
| **Farbe…** | Eine Farbe für alle ausgewählten Klöppel, bei Fachung für alle Garne. |
| **Nach Laufrichtung färben** | Die Klöppel im Uhrzeigersinn bekommen die eine, die gegen den Uhrzeigersinn die andere Farbe, standardmäßig Rot und Gelb. |

### Rohr { #rohr }

Die Karte nennt Rohrart und Kennung (zum Beispiel *Mitleitrohr Z3*), Lage
und Maße.

| Element | Wirkung |
|---|---|
| **Zettelfaden eingezogen** bzw. **Kern eingezogen** | Häkchen: Faden ist eingezogen. Ohne Häkchen ist er ausgezogen. |
| **Farbe…** | Farbe des Fadens (nur, wenn eingezogen). |
| **Kerndurchmesser** | Nur am Zentralrohr: Durchmesser des Kerns. Er bestimmt in der 3D-Vorschau den Geflechtsdurchmesser; das Geflecht legt sich auf ihn. **Bohrung ausfüllen** nimmt den Durchmesser der Bohrung. |

## Besetzungen speichern

Jede Besetzung ist Ihre eigene: Sie entsteht auf der leeren Maschine oder
als Kopie einer anderen Besetzung. Eine Maschine kann beliebig viele
Besetzungen haben, und zu jeder gehören ihre Programme.

* **Speichern** in der Kopfzeile schreibt geänderte Klöppel, Farben und
  Garn in die gewählte Besetzung zurück. Ist keine Besetzung gewählt (zum
  Beispiel nach **Alle Klöppel entfernen**), fragt das Programm nach einem
  Namen.
* **Als neue Besetzung speichern…** legt eine weitere Besetzung an.
* Umbenennen und Löschen stehen im Menü **⋯** neben **Besetzung**, siehe
  [Der Simulator-Bildschirm](editor.md#besetzung-und-programm).

### Besetzung speichern { #besetzung-speichern }

**Als neue Besetzung speichern…** öffnet den Dialog **Besetzung
speichern**:

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Dialog „Besetzung speichern“ mit dem Feld „Name der Besetzung“ (Vorschlag „Rund 2“) und dem gesetzten Haken „Programm „…“ als Kopie mitnehmen“.
    **So erzeugen:** Kundenbuild mit Modell-Lizenz, Maschine mit einer Besetzung und einem ihrer Programme öffnen, Reiter „Bestücken“, „Als neue Besetzung speichern…“ klicken.
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/besetzung-speichern.png`

| Feld | Bedeutung |
|---|---|
| **Name der Besetzung** | Vorschlag: der Name der gewählten Besetzung mit einer Zahl dahinter, zum Beispiel *Rund 2*, ohne gewählte Besetzung *Besetzung n*. Gibt es eine Besetzung gleichen Namens, fragt das Programm, ob es sie mit der aktuellen Aufstellung überschreiben soll. |
| **Programm „…“ als Kopie mitnehmen** | Nur, wenn ein Programm gewählt ist; vorbelegt an. Die neue Besetzung bekommt eine Kopie des offenen Programms. Das Programm selbst bleibt bei seiner Besetzung. |

**Speichern** legt die Besetzung sofort an (*Besetzung „…“ gespeichert (32
Klöppel).*, mit Programmkopie zusätzlich *Mit Kopie von „…“.*). Danach ist
die neue Besetzung gewählt, mit der Programmkopie oder ohne Programm.

## In der Web-App

* Die **Bedeckung** lässt sich nicht einstellen. Der
  **Materialdurchmesser** gilt je Browser für alle Maschinen und wird nicht
  mit der Besetzung gespeichert.
* **Rohrfäden** lassen sich nicht per Klick einziehen; sie kommen nur aus
  einer gespeicherten Besetzung.
* Klöppel setzen und entfernen geht nur, solange der Lauf steht.
* **Farbe für neue Klöppel** bietet zusätzlich die Wahl der **Palette**,
  **Alle Klöppel färben** und **Farbdatenbank öffnen**. In der Karte eines
  Klöppels stellen Sie die Fachung mit − und + ein.

Einzelheiten: [Flechtsimulator in der Web-App](../web/braiding-simulator.md).

## Verwandte Seiten

* [Der Simulator-Bildschirm](editor.md)
* [Programm](program.md) — Weichen schalten und Programme aufnehmen.
* [3D-Vorschau und Abzug](views.md) — wie Farben, Fachung und Garn im
  Geflecht aussehen.
* [Färben und Drehung im Designer](../designer/painting.md) —
  Fachungsfarben im Designer.
