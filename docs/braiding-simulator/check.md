# Prüfen

!!! abstract "Referenz — Die Aufgabe „Prüfen“: Fehler und Hinweise, Kollisionsprüfung über den ganzen Lauf, Grundlauf ohne Programm, Rapport und Abbindung"

## Wofür Sie diesen Bereich nutzen

Bevor ein Programm an die Maschine geht, muss feststehen, dass die
Klöppel **dauerhaft kollisionsfrei** laufen und das Geflecht so abbindet
wie gewollt. Die Aufgabe **Prüfen** sammelt alle Fehler und Hinweise und
rechnet auf Knopfdruck den ganzen Lauf durch, bis die Maschine wieder im
Startzustand steht (Rapport). Erst dann ist bewiesen, dass sich das
Programm beliebig oft wiederholen lässt.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Aufgabe „Prüfen“ mit der Gruppe Meldungen (ein Hinweis mit „Stelle anzeigen“) und der Gruppe Kollisionsprüfung nach „Aktuelle Aufstellung prüfen“: „✅ Kollisionsfrei — Rapport nach … Schritten“, Farbbild, Abbindung je Abschnitt; in der Kopfzeile der Chip „⚠ 1 Hinweis“.
    **So erzeugen:** Kundenbuild mit Modell-Lizenz, Maschine mit Umschaltprogramm öffnen, Reiter „Prüfen“, „Aktuelle Aufstellung prüfen“ klicken.
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/pruefen.png`

Ein Punkt am Reiter **Prüfen** zeigt, ob es etwas zu beachten gibt: rot
bei Fehlern, orange bei Hinweisen. Dieselben Meldungen zählen die Chips
**⛔ n Fehler** und **⚠ n Hinweise** in der Kopfzeile; ein Klick auf einen
Chip öffnet diese Aufgabe. In der Aufgabe **Prüfen** wählt ein Klick in
der Maschine aus, ein Rechtsklick schaltet eine Weiche.

## Gruppe „Meldungen“

Die Liste zeigt zuerst die **Fehler** (⛔, rot), dann die **Hinweise** (⚠,
orange); ohne Meldungen steht dort *Keine Fehler und Hinweise.*

| Knopf an einer Meldung | Wirkung |
|---|---|
| **Stelle anzeigen** | Wählt die betroffenen Räder aus, zoomt die Maschine auf sie und springt bei einer Kollision an den Anfang des Schritts. |
| **Zum Schritt springen** | Nur bei Kollisionen: setzt den Lauf an diesen Schritt. |

Typische Meldungen:

| Meldung | Art | Bedeutung |
|---|---|---|
| *Kollision bei Programmschritt …: Rad … und Rad … blockieren sich.* | Fehler | Zwei Klöppel treffen an der Übergabe zwischen diesen Rädern aufeinander. Die Wiedergabe hält an, die Räder sind markiert. |
| *Sackgasse bei …: Auf Rad … läuft ein Klöppel gegen den diagonalen Nutenstein …* | Fehler | Ein Klöppel läuft gegen das Ende einer diagonalen Nut. |
| *Kein Übergang funktionsfähig — dieses Maschinenmodell lässt sich so nicht simulieren.* | Fehler | Das Modell passt nicht; wenden Sie sich an Herzog. |
| Hinweise zur 3D-Vorschau | Hinweis | Zum Beispiel, dass ein Kern nur im Schlauchbetrieb gezeigt wird oder dass die Vorschau eine Bedeckung nicht zeichnen kann. |
| Hinweise zum Aufbau und zum Programm | Hinweis | Zum Beispiel Befehle, die der Simulator ignoriert, oder ein [verfallener Teilungswechsel](program.md#teilung-im-lauf) mit Schritt und Rad. |

## Gruppe „Kollisionsprüfung“

| Element | Wirkung |
|---|---|
| **Aktuelle Aufstellung prüfen** | Setzt den Lauf an den Start und rechnet ihn in einem Zug durch: Kollisionen, Rapport, Farbbild, ob jeder Klöppel auf seinen Platz zurückkehrt, und die Abbindung je Abschnitt. |
| **Grundlauf ohne Programm** | Häkchen: Prüft die Besetzung nur mit der Startstellung der Weichen und Räder, ohne die Befehle des Zeitprogramms. So sehen Sie, ob die Besetzung an sich läuft, bevor Sie Umschaltungen hinzufügen. |

Nach jeder Änderung an Programm, Aufstellung oder Startstellung steht
dort *Programm oder Aufstellung geändert — bitte erneut prüfen.*

### Das Ergebnis lesen

Das Ergebnis beginnt mit *Prüfung ab Startaufstellung:* (bzw. *…,
Grundlauf ohne Programm:*). Danach:

| Zeile | Bedeutung |
|---|---|
| *✅ Kollisionsfrei — Rapport nach n Schritten (m Klöppel)* | Der Lauf kehrt nach n Schritten in den Startzustand zurück, ohne dass sich Klöppel treffen. Das Programm läuft dauerhaft kollisionsfrei. |
| *❌ Kollision bei Schritt n: Rad a ↔ Rad b* | An dieser Übergabe treffen sich Klöppel. |
| *❌ Sackgasse bei Schritt n: …* | Ein Klöppel läuft gegen das Ende einer diagonalen Nut. |
| *Keine Kollision in n Schritten, Rapport nicht erreicht.* | Bis zur Prüfgrenze gab es keine Kollision, aber der Startzustand kam nicht wieder. Die Kollisionsfreiheit ist damit nicht bewiesen. |
| *Prüfung nicht möglich.* | Zum Beispiel ohne Klöppel. |

Darunter stehen, soweit zutreffend:

* **Rückkehr der Klöppel und des Farbbilds**, zum Beispiel *Jeder Klöppel
  steht danach wieder auf seinem Startplatz.*, *Das Farbbild steht nach n
  Schritten wieder wie am Start.* oder *⚠ Das Farbbild kehrt in n Schritten
  nicht zum Start zurück.* *Klöppel gleicher Farbe tauschen dauerhaft die
  Plätze* heißt: Das Bild stimmt, aber nicht jeder Klöppel kommt auf
  seinen eigenen Platz zurück.
* Bei Programmen mit Umschaltung: *Nach einem Durchlauf steht das Farbbild
  wie im Grundlauf ohne Umschaltung.* bzw. *⚠ … verschoben — die
  Umschaltung kehrt nicht sauber zurück.*
* **Rapport länger als das Programm:** *Belegung und Farbbild stehen schon
  nach jedem Durchlauf wieder wie am Start; erst nach n Schritten stehen
  auch die Räder wieder in ihrer Startdrehung.* Dazu ein Vorschlag *Mit
  Länge … ist Rapport = Programmlänge.*; ein Klick auf **Länge …** setzt
  die Programmlänge und prüft neu.
* **Abbindung:** je Abschnitt (*Schritt a–b:*) die Art des Geflechts,
  zum Beispiel *Geflecht, jeder Faden kreuzt 4 andere.*, *Flachgeflecht, …*,
  *Verzwirnen — kein Klöppel wechselt das Rad.*, *Spirale — alle Klöppel
  laufen in einer Richtung, die Fäden binden nicht ab.* oder *Stillstand.*
  *⚠ Klöppel n bindet hier nicht ab.* weist auf einen Klöppel hin, der in
  diesem Abschnitt nicht mitflicht.
* **Abzug beim Verzwirnen:** *ℹ Beim Verzwirnen in Schritt a–b läuft der
  Abzug weiter.* Mit **Abzug dort auf 0 setzen** stellt der Simulator den
  Abzug in diesem Bereich auf 0.

## Was der Simulator nicht zulässt

Der Simulator prüft auch, ob ein Programm an der echten Maschine
ausführbar ist. Alle Flügelräder laufen synchron; einzeln anhalten oder
umkehren lassen sich nur Flügelradgruppen und Switch-out-Räder. Versuchen
Sie es an einem anderen Rad, meldet die Statuszeile *Rad … hat keinen
eigenen Antrieb und läuft synchron mit allen Rädern.* Stammen solche
Befehle aus einem älteren Programm, zeigt die
[Zeitachse](program.md#zeitachse) die Zeile schraffiert als *nicht
maschinentauglich*; entfernen Sie die Befehle mit Rechtsklick.

## Typischer Ablauf

1. Besetzung wählen, **Grundlauf ohne Programm** einschalten,
   **Aktuelle Aufstellung prüfen**: Die Besetzung muss kollisionsfrei
   laufen.
2. Häkchen wegnehmen, Programm wählen und erneut prüfen.
3. Bei ❌: **Zum Schritt springen**, in der Maschine nachsehen, Befehl in
   der [Zeitachse](program.md#zeitachse) verschieben oder ändern.
4. Bei *Rapport nicht erreicht* oder einem Rapport, der viel länger ist
   als das Programm: den Vorschlag **Länge …** übernehmen.
5. Wenn alles ✅ ist: **Speichern** und den [Schaltplan](output.md)
   ausgeben.

## In der Web-App

* Die Kollisionsprüfung läuft nach jeder Änderung von selbst; einen Knopf
  **Aktuelle Aufstellung prüfen** gibt es nicht.
* Sie zeigt Kollision bzw. Sackgasse, Rapport und Klöppelzahl, dazu *Alle
  Befehle lassen sich an der Maschine ausführen.* oder die Befunde, zum
  Beispiel *Schritt …: Rad … hält an oder startet allein — an der Maschine
  laufen alle Räder synchron.* oder einen verfallenden Teilungswechsel.
  Farbbild, Rückkehr der Klöppel und Abbindung je Abschnitt zeigt sie
  nicht.
* An einem Befund entfernt **Befehl entfernen** den betroffenen Befehl.
* Hat Herzog zum Modell Notizen hinterlegt, stehen sie unter **Notizen**.

Einzelheiten: [Flechtsimulator in der Web-App](../web/braiding-simulator.md).

## Verwandte Seiten

* [Programm](program.md)
* [Bestücken](populate.md)
* [Ausgeben](output.md) — die Hinweise des Schaltplans.
