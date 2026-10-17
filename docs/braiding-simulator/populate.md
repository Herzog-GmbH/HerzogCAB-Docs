# Bestücken

!!! abstract "Referenz — Die Aufgabe „Bestücken“: Klöppel setzen und entfernen, Farben, Fachung und Nummern, Bestücken nach Muster, Garn und Bedeckung, Rohrfäden und Besetzungen speichern"

## Wofür Sie diesen Bereich nutzen

Bevor ein Programm laufen kann, braucht die Maschine Klöppel. Am
schnellsten wählen Sie oben eine **Konfiguration** von Herzog (*Voll*,
*Halb*, *Tandem* …) und passen sie an. Sie können die Maschine auch von
Hand oder nach einem Muster bestücken. Farben, Fachung und Garn bestimmen,
wie das Geflecht in der [3D-Vorschau](views.md) aussieht; zusammen
speichern Sie alles als **Besetzung**.

Klöppel setzen und entfernen gehört immer zur Besetzung, nie zum
Programm. Auch während der Aufnahme wird daraus kein Programmbefehl.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Aufgabe „Bestücken“ mit den Gruppen Klöppel (Bestücken nach Muster…, Farbe für neue Klöppel, Alle Klöppel auswählen, Alle Klöppel entfernen), Garn (Materialdurchmesser, Bedeckung) und Besetzung; darüber die Auswahlkarte eines Klöppels mit Fachung 3 und Einzelfarben.
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
| **Bestücken nach Muster…** | Verteilt die Klöppel regelmäßig auf die Bahnen der Maschine, siehe [unten](#bestucken-nach-muster). |
| **Farbe für neue Klöppel** | Knopf mit der aktuellen Setzfarbe. Ein Klick öffnet die Auswahl: **Automatisch (Farbrotation)** (jeder Klöppel bekommt eine eigene Farbe), **Standardfarben** aus der [Farbbibliothek](../master-data/colors.md), **Zuletzt verwendet** und **Eigene Farbe wählen…**. |
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
Besetzung an (dasselbe wie im Menü **⋯** neben **Besetzung**). Der Hinweis
darunter erinnert: *„Speichern“ oben schreibt Änderungen in die gewählte
Besetzung zurück.*

## Bestücken nach Muster { #bestucken-nach-muster }

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Dialog „Bestücken nach Muster“ mit Muster Voll, Farbe je Laufrichtung, zwei Farbknöpfen und der Ergebniszeile „✅ 32 Klöppel — 16 im, 16 gegen den Uhrzeigersinn. Läuft mit „…“ kollisionsfrei.“
    **So erzeugen:** Maschine mit Programm öffnen, Bestücken > Bestücken nach Muster….
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/bestuecken-muster.png`

Der Dialog verteilt die Klöppel regelmäßig auf die Bahnen der Maschine, so
wie die Weichen gerade stehen. Die bisherige Aufstellung wird ersetzt;
**Rückgängig** holt sie zurück.

| Feld | Bedeutung |
|---|---|
| **Muster** | **Voll** (jeder 2. Platz jeder Bahn, die Normalbesetzung), **Halb** (jeder 4. Platz jeder Bahn), **Tandem** (jedes 2. Rad voll besetzt), **Nur eine Laufrichtung** (nur die Bahnen einer Laufrichtung, jeder 2. Platz, zum Beispiel für eine Spirale) oder **So viele wie möglich** (die größte kollisionsfreie Besetzung, die sich finden lässt). |
| **Laufrichtung** | **Im Uhrzeigersinn** oder **Gegen den Uhrzeigersinn**; nur bei *Nur eine Laufrichtung*. |
| **Farbe je Laufrichtung** | Die Klöppel einer Laufrichtung bekommen die eine Farbe, die der anderen die zweite, wie im Flechtbild. Ohne Häkchen gilt die Farbe für neue Klöppel. |
| **Farben** | Die beiden Farben **im Uhrzeigersinn** (Standard rot) und **gegen den Uhrzeigersinn** (Standard gelb). |
| **Mit dem Zeitprogramm prüfen** | Nur mit gewähltem Programm: Nimmt nur eine Lage, die mit diesem Programm kollisionsfrei läuft. Gibt es mehrere gleichwertige Lagen, passt so nur die, zu der das Programm geschrieben ist. Bei *Tandem* und *So viele wie möglich* nicht verfügbar. |

Die Ergebniszeile rechnet bei jeder Änderung neu, zum Beispiel *✅ 32
Klöppel — 16 im, 16 gegen den Uhrzeigersinn. Läuft mit „…“
kollisionsfrei.* Geht das Muster nicht, steht dort ❌ mit dem Grund.
**Bestücken** setzt die Klöppel; die neue Aufstellung ist noch keine
gespeicherte Besetzung.

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
| **Nach Laufrichtung färben** | Die Klöppel im Uhrzeigersinn bekommen die eine, die gegen den Uhrzeigersinn die andere Farbe, dieselben wie beim Bestücken nach Muster. |

### Rohr { #rohr }

Die Karte nennt Rohrart und Kennung (zum Beispiel *Mitleitrohr Z3*), Lage
und Maße.

| Element | Wirkung |
|---|---|
| **Zettelfaden eingezogen** bzw. **Kern eingezogen** | Häkchen: Faden ist eingezogen. Ohne Häkchen ist er ausgezogen. |
| **Farbe…** | Farbe des Fadens (nur, wenn eingezogen). |
| **Kerndurchmesser** | Nur am Zentralrohr: Durchmesser des Kerns. Er bestimmt in der 3D-Vorschau den Geflechtsdurchmesser; das Geflecht legt sich auf ihn. **Bohrung ausfüllen** nimmt den Durchmesser der Bohrung. |

## Konfigurationen und eigene Besetzungen

* **Konfigurationen** liefert Herzog mit dem Modell. Sie enthalten nur
  Plätze und Klöppelnummern; Ihre Farben und Ihr Garn kommen dazu.
* Wählen Sie eine Konfiguration oder eine Besetzung von Herzog und ändern
  sie, speichert **Speichern** eine eigene Kopie *&lt;Name&gt; – eigene*:
  *Als eigene Besetzung „…“ gespeichert — „…“ von Herzog bleibt
  unverändert.*
* Besetzungen von Herzog lassen sich nicht löschen.

### Besetzung speichern { #besetzung-speichern }

**Als neue Besetzung speichern…** öffnet den Dialog **Besetzung
speichern**:

| Feld | Bedeutung |
|---|---|
| **Name der Besetzung** | Vorschlag *&lt;gewählte Besetzung&gt; – eigene* bzw. *Besetzung n*. Gibt es eine eigene Besetzung gleichen Namens, fragt das Programm, ob es sie überschreiben soll. |
| **Mit „…“ mitladen** | Nur, wenn ein eigenes Programm gewählt ist: Wer das Programm wählt, bekommt diese Besetzung gleich dazu. |

Die Besetzung wird sofort gespeichert (*Besetzung „…“ gespeichert (32
Klöppel).*). **Besetzung löschen…** im Menü **⋯** löscht eine eigene
Besetzung nach Rückfrage.

## In der Web-App

* **Bestücken nach Muster…** bietet nur die Muster und **Farbe je
  Laufrichtung** mit festen Farben; Laufrichtung, eigene Farben und **Mit
  dem Zeitprogramm prüfen** fehlen.
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
* [Färben und Texturieren im Designer](../designer/painting.md) —
  Fachungsfarben im Designer.
