# Programm

!!! abstract "Referenz — Die Aufgabe „Programm“: Weichen und Räder schalten, Aufnahme, Zeitachse, Teilung im Lauf, Flügelradgruppen, Betriebsart einfügen, Drehzahl und Abzug"

## Wofür Sie diesen Bereich nutzen

Ein **Zeitprogramm** beschreibt, wie die Maschine läuft: die
**Startstellung** aller Weichen und Räder und die **Befehle**, die im Lauf
an bestimmten Schritten schalten. So entstehen Umschaltungen wie Rund ⇄
Litze, Verzwirnen oder Spirale. Sie schreiben ein Programm auf zwei Wegen:

* **Aufnehmen:** Aufnahme einschalten, laufen lassen, anhalten, Weiche
  klicken, weiter. Jeder Klick wird ein Befehl am aktuellen Schritt.
* **In der Zeitachse setzen:** In der Zeile einer Weiche oder eines Rades
  auf den Schritt klicken, an dem geschaltet werden soll.

Neue Programme legen Sie oben in der Kopfzeile an (**⋯** neben
**Programm** > **Neues Programm…**) oder auf der
[Startseite](index.md#startseite) mit **Neues Programm**.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Aufgabe „Programm“ mit den Gruppen Weichen und Räder sowie Drehzahl und Abzug; unten die Zeitachse mit den Zeilen Abzug, Drehzahl, Richtung, Weichen (aufgeklappt) und Räder; das rote Band „Aufnahme läuft“ in der Maschinenansicht.
    **So erzeugen:** Kundenbuild mit Modell-Lizenz, Maschine mit einem Programm von Herzog (Umschaltung) öffnen, Reiter „Programm“, Aufnahme starten.
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/programm.png`

In der Aufgabe **Programm** schaltet ein **Klick auf eine Weiche** sie.
Ein Klick auf einen Klöppel oder ein Rad wählt es aus.

## Weichen schalten

Was ein Klick auf eine Weiche bewirkt, hängt davon ab, wo der Lauf steht:

| Stand | Wirkung |
|---|---|
| **Am Start** | Ändert die **Startstellung** des Programms. |
| **Mitten im Lauf, ohne Aufnahme** | Gilt nur für diesen Lauf: *W12 nur für diesen Lauf umgestellt — die Startstellung bleibt. Ins Programm kommt der Befehl mit der Aufnahme.* |
| **Mit Aufnahme** | Wird ein Schaltbefehl am aktuellen Schritt. |

* Hängt die Weiche an einem **Stellhebel**, stellt ein Klick alle Weichen
  des Hebels gemeinsam.
* **++ctrl++ + Klick** sammelt mehrere Weichen zu einer **Schaltgruppe**:
  Ein Klick auf eine von ihnen schaltet dann alle; ein Klick auf eine
  andere Weiche löst die Gruppe auf.
* **Feste Bauteile** (X-Kreuzung, Y-Stück, Nutensteine) lassen sich nicht
  schalten; ein Klick wählt sie nur aus.

## Gruppe „Weichen und Räder“

| Element | Wirkung |
|---|---|
| **Alle Räder umkehren** | Kehrt die Laufrichtung aller Räder um; alle Paare bleiben gegenläufig, der Flechtkreis läuft rückwärts weiter. Gruppierte Räder bleiben fest gekoppelt. Wirkt ab der nächsten Schrittgrenze, wie ein Weichenklick am Start, im Lauf oder mit Aufnahme. |
| **Betriebsart einfügen…** | Übernimmt eine Umschaltung wie Verzwirnen, Spirale oder Flach aus einem Programm dieser Maschine an den aktuellen Schritt, siehe [unten](#betriebsart-einfugen). |
| **Startzustand übernehmen** | Speichert die aktuelle Stellung von Rädern und Weichen als Start des Programms; die gewählte Besetzung wird mit dem Programm verknüpft (*Programmstart übernommen: … Räder, … Weichen · Besetzung: …*). Der Lauf steht danach am Start. |
| **Programm wiederholen** | Häkchen (Standard an): Die Befehle wiederholen sich mit der Programmlänge als Periode, typisch für Flechtmuster. Ohne Häkchen läuft das Programm einmal durch, danach bleiben alle Stellungen. |

Ohne gewähltes Programm sind die programmbezogenen Knöpfe gesperrt.

## Gruppe „Drehzahl und Abzug“ { #drehzahl-und-abzug }

Die Zusammenfassung zeigt den Abzugsbereich am Abspielkopf: **Abzug**,
Schritte, Flechtwinkel, Schlaglänge, PPI, Abzug in m/min, Drehzahl in
U/min, Geflechtsdurchmesser bzw. -breite und Bedeckung; die vorgegebene
Größe steht fett. Ohne Abzug steht dort *Abzug gleichmäßig — der Winkel
kommt aus der Vorschau. In der Zeile „Abzug“ festlegen.*

| Knopf | Wirkung |
|---|---|
| **Drehzahl ändern…** | Drehzahl der Flügelräder ab dem Schritt am Abspielkopf, siehe [Drehzahl](views.md#drehzahl). |
| **Abzug ändern…** | Abzug ab dem Schritt am Abspielkopf, siehe [Abzug](views.md#abzug). |

Einen Bereich ziehen Sie in der Zeile **Drehzahl** bzw. **Abzug** der
Zeitachse auf. Wechselt in einem Abzugsbereich die Betriebsart (zum
Beispiel von Rund auf Litze), warnt die Zusammenfassung: *Ab Schritt …
wechselt die Betriebsart. Für dieselbe Vorgabe braucht dieser Teil einen
eigenen Abzug, die Maschine fährt aber einen je Abzugswechsel: dort einen
Abzugswechsel setzen.*

## Auswahlkarte: Weiche { #weiche }

Klicken Sie in **Bestücken**, **Prüfen** oder **Ausgeben** auf eine
Weiche, zeigt die Karte *Weiche W12 ausgewählt*. (In **Programm** schaltet
der Klick die Weiche, statt sie auszuwählen.)

* **Stellung:** *geschlossen* (die Bahnen kreuzen sich, Klöppel gehen auf
  das andere Flügelrad über) oder *offen* (die Bahnen laufen aneinander
  vorbei, jeder Klöppel bleibt auf seinem Rad). Weicht sie von der
  Grundstellung ab, steht das dabei.
* **Weiche öffnen** bzw. **Weiche schließen** schaltet sie, in jeder
  Aufgabe, mit derselben Wirkung wie ein Klick.
* Eine Weiche *Ohne Funktion (gleichlaufende oder unsynchrone Räder).*
  lässt sich nicht schalten.

Hängt die Weiche an einem **Stellhebel**, zeigt die Karte darunter den
Hebel mit seinen Weichen und der Stellung (*Stellung 1*, *Stellung 2* oder
*gemischt (einzeln verstellt)*). **Hebel auf „…“ stellen** stellt alle
Weichen des Hebels gemeinsam um, mit Aufnahme als Programmbefehle.

Feste Bauteile zeigen nur ihre Beschreibung:

| Bauteil | Wirkung |
|---|---|
| **X-Kreuzung** | Die Bahnen kreuzen sich, es wird immer in beide Richtungen übergeben. |
| **Y-Stück** | Zwei Zuläufe, ein Ablauf. |
| **Nutenstein Halbkreise** | Jede Bahn läuft an der anderen vorbei, keine Übergabe. Üblich an Litzenrädern. |
| **Nutenstein diagonal** | Nur eine diagonale Nut (/ statt X). Läuft ein Klöppel gegen ihr Ende, entsteht eine Sackgasse. |

## Auswahlkarte: Rad { #rad }

Die Karte *Rad n ausgewählt* zeigt, wie das Rad angetrieben wird, und nur
die Knöpfe, die die echte Maschine an diesem Rad kann.

### Flügelradgruppe und Switch-out-Rad

Normale Räder laufen synchron mit allen anderen (*Nicht gruppiert. Im
Betrieb läuft es synchron mit allen Rädern.*); für sie gibt es keine
Knöpfe. Einen eigenen Antrieb haben:

* eine **Flügelradgruppe** (an den Rädern steht *G1*, *G2* …): Start,
  Stopp und Richtungswechsel wirken immer auf die ganze Gruppe,
* ein **Switch-out-Rad**: Es lässt sich anhalten, damit seine Klöppel
  parken.

| Knopf | Wirkung |
|---|---|
| **Flügelradgruppe anhalten** / **Flügelradgruppe starten** | Hält die ganze Gruppe an bzw. startet sie; steht sie, parken ihre Klöppel. |
| **Flügelradgruppe umkehren** | Kehrt nur diese Gruppe um; innerhalb der Gruppe bleiben Nachbarn gegenläufig. |
| **Switch-out anhalten** / **Switch-out starten** | Hält das Switch-out-Rad an bzw. startet es; steht es, parken seine Klöppel. |
| **Switch-out umkehren** | Kehrt nur dieses Rad um. |

Alle wirken ab der nächsten Schrittgrenze: am Start als Startstellung,
mitten im Lauf nur für diesen Lauf, mit Aufnahme als Programmbefehl.
Unter der Nabe dieser Räder zeigt ein Lauf-Symbol, ob sie laufen (▶) oder
stehen (⏸); in der Aufgabe **Programm** startet bzw. hält ein Klick darauf
das Rad.

Läuft ein Rad gegen seine Grundrichtung, warnt die Karte: *Läuft im
Betrieb rückwärts, gegen die Grundrichtung.*

### Dreheinheit: Klöppelwechsel

An einer **Dreheinheit** tauscht **Klöppelwechsel auslösen** je einen
Klöppel zwischen den beiden Nachbarrädern; währenddessen steht die übrige
Maschine. Mit Aufnahme wird daraus ein Befehl im Programm. Geht der
Wechsel gerade nicht, nennt die Karte den Grund und den *nächsten
möglichen Schritt* mit dem Link **dorthin springen**.

### Teilung im Lauf { #teilung-im-lauf }

Manche Räder haben mehrere Teilungen, zum Beispiel ein Randrad mit 7
Einschnitten, das als 5er- oder 3er-Rad arbeiten kann. Für sie zeigt die
Karte die Auswahl **Teilung im Lauf** mit *5er-Teilung*, *3er-Teilung*
usw.:

| Stand | Wirkung |
|---|---|
| Am Start | Die gewählte Teilung wird Startstellung des Programms: *Rad 3 arbeitet in diesem Programm mit 5er-Teilung.* |
| Mit Aufnahme | Das Rad wechselt ab dem aktuellen Schritt: *Rad 3 arbeitet ab Schritt 12 mit 3er-Teilung — im Programm aufgezeichnet.* |
| Mitten im Lauf ohne Aufnahme | Nur für diesen Lauf. |

Gewechselt wird an der Schrittgrenze. Das Rad wird dabei einzeln
angesteuert und dreht in die nächste Lage der neuen Teilung; die Klöppel
bleiben in ihren Einschnitten.

!!! warning "Wann ein Teilungswechsel verfällt"
    Sitzt beim Wechsel ein Klöppel in einem Einschnitt, den die neue
    Teilung nicht benutzt, **verfällt der Wechsel**: Das Rad bleibt bei
    seiner Teilung, und ein Hinweis unter [Prüfen](check.md) nennt Schritt
    und Rad. Der Klöppel käme sonst zur falschen Zeit an den
    Übergabepunkt. Setzen Sie den Wechsel auf einen Schritt, an dem kein
    Klöppel in einem solchen Einschnitt steht.

Ohne Programm ist die Auswahl gesperrt: *Die Teilung wird im Zeitprogramm
gespeichert. Ohne Programm arbeitet das Rad mit der größten.*

## Aufnahme { #aufnahme }

**Aufnahme** in der [Wiedergabeleiste](editor.md#wiedergabe) schaltet die
Aufnahme ein. Aufgezeichnet werden als Befehl am aktuellen Schritt:
Weichenklicks (auch über Stellhebel), **Alle Räder umkehren**, Anhalten,
Starten und Umkehren von Flügelradgruppen und Switch-out-Rädern,
Klöppelwechsel und Teilungswechsel. Klöppel setzen und entfernen bleibt
Teil der Besetzung.

* Während der Aufnahme steht oben links in der Maschine ein rotes Band
  **Aufnahme läuft** mit Position und Zahl der Befehle, und der Knopf heißt
  **Aufnahme stoppen**.
* Ein Klick auf eine Weiche schaltet sie immer, gleich welche Aufgabe
  rechts offen ist; auch der Rechtsklick schaltet.
* Läuft der Lauf oder springen Sie mit **Gehe zu Schritt** über das Ende
  hinaus, wird das Programm länger.
* Rückgängig und Wiederholen sind gesperrt.
* Ist noch kein Programm angelegt, fragt der Simulator, ob er eines
  anlegen soll (**Programm anlegen**).

Beim Stoppen meldet er, wie viele Befehle aufgezeichnet wurden.

So nehmen Sie eine Umschaltung auf:

1. Programm wählen oder anlegen, Lauf an den Start setzen.
2. **Aufnahme** einschalten und **Start** drücken.
3. Am gewünschten Schritt **Pause** drücken (oder mit **Gehe zu Schritt**
   hinspringen).
4. Die Weichen klicken, die umschalten sollen.
5. Weiterlaufen lassen, bei Bedarf zurückschalten, am Ende **Aufnahme
   stoppen**.
6. In der Aufgabe [Prüfen](check.md) kontrollieren, dann **Speichern**.

## Zeitachse { #zeitachse }

Die Zeitachse unten zeigt das gewählte Programm als Zeilen über den
Schritten. Sie ist nur mit Programm sichtbar; mit dem Knopf **Zeitachse**
rechts in der Wiedergabeleiste blenden Sie sie aus und ein. Die Höhe
ändern Sie am Trenner zwischen Maschine und Wiedergabeleiste.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Zeitachse eines Umschaltprogramms mit den Zeilen Abzug (zwei farbige Bereiche), Drehzahl, Richtung, Weichen mit W-Zeilen (Blöcke und Schaltpunkte), Räder mit einer Flügelradgruppe und einer Teilungszeile; geöffnetes Rechtsklick-Menü.
    **So erzeugen:** Maschine mit Programm öffnen (z. B. Variationsflechter mit Teilungswechsel), „Alle Zeilen“ aus, Rechtsklick in eine W-Zeile.
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/zeitachse.png`

### Kopf der Zeitachse

| Element | Wirkung |
|---|---|
| *Zeitachse — &lt;Programm&gt;* | Titel. |
| Zoom − / + | Stufen 50 bis 300 %. |
| **Gesamtes Programm** | Passt das ganze Programm in die Breite (Standard). |
| **Länge** − / + | Programmlänge in Schritten (1 bis 999). Verlängern schafft Platz für weitere Befehle; kürzer als der letzte Befehl geht nicht. |
| **Alle Zeilen** | Standard: nur Zeilen mit Befehlen oder abweichendem Startzustand. Mit Häkchen auch die übrigen, um in frischen Zeilen Befehle zu setzen. **Neues Programm…** schaltet es ein. |

### Zeilen

| Zeile | Zeigt |
|---|---|
| Schrittzeile (oben) | Schrittnummern ab 1 und den roten Abspielkopf. Klick oder Ziehen springt. |
| **Abzug** | Die Abzugsbereiche als farbige Blöcke mit Wert, Farbe je Vorgabe (Abzug blau, Schlaglänge türkis, Flechtwinkel orange, PPI violett). Schraffiert, wo die Betriebsart wechselt. Ohne Abzug: *gleichmäßig (Winkel aus der Vorschau)*. |
| **Drehzahl** | Die Drehzahl in U/min je Bereich oder *nicht gesetzt*. |
| **Richtung** | Laufrichtung **aller** Räder: Block vorwärts, Winkel rückwärts, Dreieck an einer Umkehr. |
| **Weichen** (aufklappbar) | Darunter je Weiche **W12**: Block = geschlossen, dünne Linie = offen, Kreis = Schaltbefehl. Die Gruppenzeile zeigt als Balken, wie viele Weichen geschlossen sind. |
| **Räder** (aufklappbar) | Darunter je Flügelradgruppe **Gruppe 1**, je Switch-out-Rad und Dreheinheit **R5** (Block läuft, Linie steht, Winkel rückwärts, Raute = Klöppelwechsel) und je Rad mit mehreren Teilungen **R5 Teilung** mit Blöcken *5er*, *3er*. |

### Maus

| Aktion | Wirkung |
|---|---|
| Klick in eine W-Zeile | Schaltbefehl setzen (die Weiche schaltet ab hier um) bzw. vorhandenen entfernen. |
| Klick in die Zeile **Weichen** | Alle Weichen ab hier umschalten. |
| Klick in **Richtung** | Alle Räder ab hier umkehren bzw. Umkehr entfernen. |
| Klick in eine Gruppen- oder Switch-out-Zeile | Lauf/Stopp ab hier; mit ++ctrl++ Drehrichtung ab hier umkehren. |
| Klick in eine Dreheinheit-Zeile | Klöppelwechsel setzen bzw. entfernen. |
| Klick in eine Teilungszeile | Ab hier die andere Teilung; auf einer Marke den Wechsel entfernen. |
| Klick in **Abzug** bzw. **Drehzahl** | Öffnet den Dialog ab diesem Schritt, siehe [Abzug](views.md#abzug) und [Drehzahl](views.md#drehzahl). |
| Ziehen in einer Zeile | Legt den Zustand nur über den gezogenen Bereich; danach gilt wieder der alte. In **Abzug** und **Drehzahl** öffnet sich der Dialog für den Bereich. |
| Ziehen, das auf einem Befehl beginnt | Verschiebt den Befehl. |
| Klick in die Beschriftung | Markiert die Zeile; mit ++ctrl++ weitere, mit ++shift++ einen Bereich (nur Zeilen derselben Art). Ziehen in einer markierten Zeile schaltet alle markierten gemeinsam. |

Ein Doppelklick in einer Zeile nimmt den eben gesetzten Befehl nicht
wieder weg. Das Mausrad rollt die Zeitachse.

### Abzug und Drehzahl in der Zeitachse { #abzug-und-drehzahl-in-der-zeitachse }

Ein Klick in **Abzug** oder **Drehzahl** setzt einen neuen Wert **ab
diesem Schritt**; er gilt bis zum nächsten Wechsel. Ziehen setzt ihn
**nur für den Bereich**; danach gilt wieder der Wert davor. Die Dialoge
sind unter [3D-Vorschau und Abzug](views.md#abzug) beschrieben.

### Rechtsklick-Menü

Je nach Zeile oben ein passender Befehl, zum Beispiel *W12 bei Schritt 20
umschalten*, *Alle Räder bei Schritt 20 umkehren*, *Bei Schritt 20
anhalten* oder *Ab Schritt 20 mit 3er-Teilung*. Darunter immer:

| Eintrag | Wirkung |
|---|---|
| **Schritte einfügen…** | Fügt vor einem Schritt leere Schritte ein (Standard 4); was danach kommt, rückt nach hinten. In den neuen Schritten gilt der Zustand davor weiter. |
| **Schritte löschen…** | Löscht Schritte; was dort geschaltet wurde, gilt danach weiter, spätere Befehle rücken nach vorn. |
| **Abschnitt verschieben…** | Verschiebt die Befehle eines Schrittbereichs um eine Zahl von Schritten (positiv später, negativ früher), auf Wunsch **Nur markierte Zeilen**. |
| **Abschnitt kopieren…** | Kopiert die Befehle eines Abschnitts an eine andere Stelle, auch aus einem anderen Programm dieser Maschine (**Aus Programm**). |
| **Betriebsart einfügen…** | Wie in der Gruppe „Weichen und Räder“, siehe [unten](#betriebsart-einfugen). |
| **Zu Schritt n springen** | Setzt den Abspielkopf. |

Steht in einer Radzeile ein Befehl, den die Maschine nicht ausführen kann
(ein einzelnes Rad ohne eigenen Antrieb anhalten oder umkehren, aus einem
älteren Programm), ist die Zeile schraffiert und der Kurzhinweis sagt
*Nicht maschinentauglich: an der Maschine laufen alle Räder synchron.*
Mit **Einzelrad-Befehle von R… entfernen** im Rechtsklick-Menü löschen Sie
diese Befehle.

## Betriebsart einfügen { #betriebsart-einfugen }

Eine **Umschaltung** ist ein Abschnitt eines Programms, in dem Weichen vom
Programmstart abweichen und danach zurückschalten, zum Beispiel ins
Verzwirnen und zurück. **Betriebsart einfügen…** übernimmt eine solche
Umschaltung aus einem beliebigen Programm dieser Maschine, zum Beispiel aus
einem Programm von Herzog, in Ihr Programm.

| Feld | Bedeutung |
|---|---|
| **Umschaltung** | Die gefundenen Umschaltungen: Programm · Schritte · geschaltete Weichen. |
| **Beginnt bei Schritt** | Wo die Umschaltung beginnt (vorbelegt: aktueller Schritt). |
| **Dauer** | Schritte vom ersten Befehl des Hinwegs bis zum ersten des Rückwegs. |
| **Platz schaffen** | Schritte einfügen, damit das übrige Programm erhalten bleibt und nach hinten rückt. Ohne Häkchen überschreibt die Umschaltung, was dort steht. |
| **Abzug mitnehmen** | Nur, wenn der Abschnitt Abzugswechsel enthält: übernimmt sie mit; beim Verzwirnen steht der Abzug zum Beispiel auf 0. |

Der Dialog prüft sofort, ob der Lauf kollisionsfrei bleibt und jeder
Klöppel nach der Rückkehr dort steht, wo er ohne Umschaltung stünde:
*✅ Kollisionsfrei — nach der Rückkehr steht jeder Klöppel wie ohne
Umschaltung.*, *⚠ Kollisionsfrei, aber das Farbbild ist danach
verschoben.* oder *❌ Kollision bei Schritt …*. Darunter schlägt er
*Passende Startschritte* und *Passende Dauern* vor. **Einfügen** setzt die
Umschaltung ein. Die Funktion braucht das Recht *Flechtsimulator
bearbeiten*.

Findet der Simulator in den Programmen dieser Maschine keine Umschaltung,
sagt er das; legen Sie dann zuerst eine an oder nutzen Sie ein Programm
von Herzog.

## In der Web-App

* **Betriebsart einfügen** gibt es nicht.
* Die Zeitachse hat kein Rechtsklick-Menü und keine Zeilenmarkierung;
  Ziehen legt einen Zustand über den Bereich, verschiebt aber keinen
  Befehl. Befehle verschieben, anspringen und entfernen Sie in der Liste
  **Befehle (n)** der Aufgabe **Programm**; dort steht auch die **Länge**
  des Programms.
* Die Zeilen sind etwas anders geordnet: eine Zeile je Stellhebel, eine
  Zeile **Alle Räder**, dazu je Flügelradgruppe, Switch-out-Rad,
  Dreheinheit und Teilung eine Zeile.
* Während der Aufnahme spielt das Programm ohne Wiederholung; beim
  Stoppen wächst die Länge bis zum erreichten Schritt.

Einzelheiten: [Flechtsimulator in der Web-App](../web/braiding-simulator.md).

## Verwandte Seiten

* [Prüfen](check.md) — kontrollieren, ob das Programm kollisionsfrei läuft.
* [3D-Vorschau und Abzug](views.md) — Abzug und Drehzahl.
* [Ausgeben](output.md) — das Programm als Schaltplan.
* [Mehrere Flechtköpfe](multiple-heads.md)
