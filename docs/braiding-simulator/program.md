# Programm

!!! abstract "Referenz — Die Aufgabe „Programm“: Weichen und Räder schalten, Startstellung, Aufnahme, Zeitachse, Teilung im Lauf, Flügelradgruppen, Drehzahl und Abzug"

## Wofür Sie diesen Bereich nutzen

Ein **Zeitprogramm** beschreibt, wie die Maschine läuft: die
**Startstellung** aller Weichen und Räder und die **Befehle**, die im Lauf
an bestimmten Schritten schalten. So entstehen Umschaltungen wie Rund ⇄
Litze, Verzwirnen oder Spirale. Sie schreiben ein Programm auf zwei Wegen:

* **Aufnehmen:** Aufnahme einschalten, laufen lassen, anhalten, Weiche
  klicken, weiter. Jeder Klick wird ein Befehl am aktuellen Schritt.
* **In der Zeitachse setzen:** In der Zeile einer Weiche oder eines Rades
  auf den Schritt klicken, an dem geschaltet werden soll.

Jedes Programm gehört zu genau einer Besetzung. Neue Programme legen Sie
oben in der Kopfzeile auf der gewählten Besetzung an (**⋯** neben
**Programm** > **Neues Programm…**) oder auf der
[Startseite](index.md#startseite) in der Karte der Besetzung mit **+ Neues
Programm**. Wie Programme und Besetzungen zusammenhängen, steht unter
[Besetzung und Programm](editor.md#besetzung-und-programm).

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Aufgabe „Programm“ mit den Gruppen Weichen und Räder sowie Drehzahl und Abzug; unten die Zeitachse mit den Zeilen Abzug, Drehzahl, Richtung, Weichen (aufgeklappt) und Räder; das rote Band „Aufnahme läuft“ in der Maschinenansicht.
    **So erzeugen:** Kundenbuild mit Modell-Lizenz, Maschine mit einem eigenen Umschaltprogramm öffnen, Reiter „Programm“, Aufnahme starten.
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/programm.png`

In der Aufgabe **Programm** schaltet ein **Klick auf eine Weiche** sie.
Ein Klick auf einen Klöppel oder ein Rad wählt es aus.

## Weichen schalten

Was ein Klick auf eine Weiche bewirkt, hängt davon ab, ob ein Programm
gewählt ist und ob die Aufnahme läuft. Kurz gesagt: ohne Aufnahme die
Startstellung, mit Aufnahme ab hier.

| Stand | Wirkung |
|---|---|
| **Programm gewählt, ohne Aufnahme** | Ändert die **Startstellung** des Programms, gleich an welchem Schritt der Lauf gerade steht. Die Weiche steht danach von Anfang an so: *W12 ist jetzt von Anfang an geschlossen — die Startstellung des Programms ist geändert.* |
| **Mit Aufnahme** | Wird ein Schaltbefehl ab dem aktuellen Schritt. |
| **Ohne Programm** | Am Start stellt der Klick die Weiche um; mitten im Lauf gilt er nur für diesen Lauf. |

Ändern Sie die Startstellung mitten im Lauf, rechnet der Simulator den
Lauf mit der neuen Startstellung bis zur alten Stelle neu. Ein Befehl in
Schritt 1 für dieselbe Weiche zieht mit. Schaltet das Programm die Weiche
später selbst, nennt die Meldung den Schritt: *Ab Schritt 20 schaltet das
Programm um.* Bis dorthin gilt die neue Startstellung.

Befehle in Schritt 1 zeigt die Maschine schon am Start: Weichen, Lauf und
Richtung der Räder stehen dort so, wie Schritt 1 sie schaltet.

* Hängt die Weiche an einem **Stellhebel**, stellt ein Klick alle Weichen
  des Hebels gemeinsam.
* **++ctrl++ + Klick** sammelt mehrere Weichen zu einer **Schaltgruppe**:
  Ein Klick auf eine von ihnen schaltet dann alle; ein Klick auf eine
  andere Weiche löst die Gruppe auf.
* Für Stellhebel und Schaltgruppen gilt dieselbe Regel wie für eine
  einzelne Weiche: ohne Aufnahme die Startstellung, mit Aufnahme ein Befehl
  ab hier.
* **Feste Bauteile** (X-Kreuzung, Y-Stück, Nutensteine) lassen sich nicht
  schalten; ein Klick wählt sie nur aus.

## Gruppe „Weichen und Räder“

Oben in der Gruppe fasst ein Hinweis die Klickregel zusammen: *Klick auf
eine Weiche schaltet sie, Strg+Klick sammelt mehrere zum gemeinsamen
Schalten. Ohne Aufnahme ändert das die Startstellung des Programms, also
von Anfang an. Mit laufender Aufnahme wird es ein Befehl ab dem aktuellen
Schritt. Für Start und Stopp der Räder gilt dasselbe.*

| Element | Wirkung |
|---|---|
| **Alle Räder umkehren** | Kehrt die Laufrichtung aller Räder um; alle Paare bleiben gegenläufig, der Flechtkreis läuft rückwärts weiter. Gruppierte Räder bleiben fest gekoppelt. Wirkt ab der nächsten Schrittgrenze: am Start als Startstellung, mitten im Lauf ohne Aufnahme nur für diesen Lauf, mit Aufnahme als Befehl. |
| **Startzustand übernehmen** | Speichert die aktuelle Stellung von Rädern und Weichen als Start des Programms (*Programmstart übernommen: … Räder, … Weichen · Besetzung: …*). Das Programm bleibt bei seiner Besetzung. Der Lauf steht danach am Start. |
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

**Anhalten** und **Starten** folgen derselben Regel wie ein Weichenklick:
Mit gewähltem Programm und ohne Aufnahme ändern sie die Startstellung des
Programms, gleich an welchem Schritt der Lauf steht (*Flügelradgruppe 1
(Räder …) steht jetzt von Anfang an — die Startstellung des Programms ist
geändert.*); ein Befehl in Schritt 1 zieht mit, ein späterer Befehl
für dasselbe Rad wird in der Meldung genannt. Mit Aufnahme werden sie ein
Befehl ab dem aktuellen Schritt. Ohne Programm wirken sie am Start als
Startstellung und mitten im Lauf nur für diesen Lauf.

**Umkehren** wirkt ab der nächsten Schrittgrenze: am Start als
Startstellung, mitten im Lauf ohne Aufnahme nur für diesen Lauf, mit
Aufnahme als Programmbefehl.

Unter der Nabe dieser Räder zeigt ein Lauf-Symbol, ob sie laufen (▶) oder
stehen (⏸); in der Aufgabe **Programm** startet bzw. hält ein Klick darauf
das Rad, mit derselben Wirkung wie die Knöpfe.

Läuft ein Rad gegen seine Grundrichtung, warnt die Karte: *Läuft im
Betrieb rückwärts, gegen die Grundrichtung.*

### Dreheinheit: Klöppelwechsel

An einer **Dreheinheit** tauscht **Klöppelwechsel auslösen** je einen
Klöppel zwischen den beiden Nachbarrädern; währenddessen steht die übrige
Maschine. Mit Aufnahme wird daraus ein Befehl im Programm, ohne Aufnahme
gilt der Wechsel nur für diesen Lauf. Geht der
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
Teil der Besetzung. Ohne Aufnahme ändert ein Klick auf eine Weiche oder
auf den Lauf eines Rades die Startstellung, siehe
[Weichen schalten](#weichen-schalten).

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

Wie **Richtung** und **Weichen** stehen auch **Abzug** und **Drehzahl**
über die ganze Breite der Zeitachse, auch hinter dem Programmende:

* Ohne **Programm wiederholen** gilt der letzte Bereich nach dem
  Programmende weiter.
* Mit **Programm wiederholen** kehren die Bereiche mit der Programmlänge
  wieder.
* Gleiche Bereiche nebeneinander verschmelzen zu einem Block.
* Hinter dem Programmende nennt der Kurzhinweis den Bereich, der dort
  gilt.

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
| **Zu Schritt n springen** | Setzt den Abspielkopf. |

Steht in einer Radzeile ein Befehl, den die Maschine nicht ausführen kann
(ein einzelnes Rad ohne eigenen Antrieb anhalten oder umkehren, aus einem
älteren Programm), ist die Zeile schraffiert und der Kurzhinweis sagt
*Nicht maschinentauglich: an der Maschine laufen alle Räder synchron.*
Mit **Einzelrad-Befehle von R… entfernen** im Rechtsklick-Menü löschen Sie
diese Befehle.

## In der Web-App

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
