# Der Simulator-Bildschirm

!!! abstract "Referenz — Der Arbeitsbildschirm des Flechtsimulators: Kopfzeile mit Besetzung und Programm, Maschinenansicht, Aufgaben-Leiste mit Auswahlkarte, Wiedergabe, Tasten und Maus"

## Wofür Sie diesen Bereich nutzen

Öffnen Sie auf der [Startseite](index.md#startseite) eine Maschine, sehen
Sie diesen Bildschirm. Hier bestücken Sie die Maschine, schreiben und
prüfen Programme und geben den Schaltplan aus. Die Seite beschreibt, was
in allen Aufgaben gleich ist; die Aufgaben selbst haben eigene Seiten.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Simulator-Bildschirm einer Rundflechtmaschine: Kopfzeile mit Besetzung und Programm, Maschinenansicht mit Klöppeln, rechts die Aufgaben-Leiste mit geöffneter Auswahlkarte einer Weiche, 3D-Vorschau, unten Wiedergabeleiste und Zeitachse; Nummern 1–6 an den Bereichen.
    **So erzeugen:** Kundenbuild mit Modell-Lizenz, Maschine mit Programm öffnen, eine Weiche anklicken, einige Schritte abspielen; Navigation eingeklappt.
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/bildschirm.png`

1. **Kopfzeile** — zurück zur Startseite, Name der Maschine, Besetzung,
   Programm, Meldungen, Ansicht, Kurzhilfe, Rückgängig, Speichern.
2. **Maschinenansicht** — die Maschine von oben mit Rädern, Weichen,
   Rohren und Klöppeln. Hier klicken Sie, um zu bestücken, zu schalten
   und auszuwählen.
3. **3D-Vorschau** — Geflecht, Schema oder Maschine in 3D, siehe
   [3D-Vorschau und Abzug](views.md).
4. **Auswahlkarte** — oben in der rechten Leiste, solange etwas ausgewählt
   ist.
5. **Aufgaben-Leiste** — die Reiter **Bestücken**, **Programm**,
   **Prüfen** und **Ausgeben**.
6. **Wiedergabeleiste und Zeitachse** — unten über die volle Breite.

## Kopfzeile

| Element | Wirkung |
|---|---|
| **← Flechtsimulator** | Zurück zur [Startseite](index.md#startseite). Bei ungespeicherten Änderungen fragt das Programm vorher nach. |
| Name der Maschine | Bei ungespeicherten Änderungen mit einem Stern. Der Kurzhinweis nennt die Zahl der Räder, Weichen und Klöppelplätze. |
| **Besetzung** | Liste der Besetzungen dieser Maschine. Die Wahl setzt die Besetzung sofort auf die Maschine und lädt ihr zuletzt benutztes Programm, siehe [unten](#besetzung-und-programm). |
| **⋯** neben Besetzung | **Als neue Besetzung speichern…**, **Besetzung umbenennen…** und **Besetzung löschen…**, siehe [unten](#besetzung-und-programm). |
| **Programm** | Die Zeitprogramme der gewählten Besetzung. Die Wahl lädt sofort. Beim nächsten Öffnen der Maschine sind Besetzung und Programm wieder gewählt. |
| **⋯** neben Programm | **Neues Programm…**, **Programm umbenennen…**, **Programm duplizieren**, **Anderer Besetzung zuordnen…** und **Programm löschen…**, siehe [unten](#besetzung-und-programm). |
| **⛔ n Fehler**, **⚠ n Hinweise** | Erscheinen, sobald es Meldungen gibt (rot bzw. orange). Der Kurzhinweis listet sie auf; ein Klick öffnet die Aufgabe [Prüfen](check.md). |
| **Ansicht** | Was die Maschinenansicht zeigt, siehe [unten](#ansicht). |
| **?** | Kurzhilfe mit Maus und Tasten, siehe [Tasten und Maus](#tasten-und-maus). |
| Rückgängig, Wiederholen | Mehrstufig (++ctrl+z++, ++ctrl+y++). Der Lauf steht danach wieder am Start. Während der Aufnahme gesperrt. |
| **Speichern** | Speichert Ihre eigenen Besetzungen und Programme (++ctrl+s++). Aktiv, sobald es Änderungen gibt und Sie das Recht *Flechtsimulator bearbeiten* haben. Siehe [Speichern](#speichern). |

### Besetzung und Programm { #besetzung-und-programm }

Jedes Programm gehört zu genau einer Besetzung. Die Liste **Programm**
zeigt deshalb nur die Programme der Besetzung, die oben gewählt ist.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Kopfzeile des Simulators mit gewählter Besetzung und geöffnetem Menü ⋯ neben „Programm“ (Neues Programm…, Programm umbenennen…, Programm duplizieren, Anderer Besetzung zuordnen…, Programm löschen…).
    **So erzeugen:** Kundenbuild mit Modell-Lizenz, Maschine mit zwei Besetzungen und mehreren Programmen öffnen, ⋯ neben „Programm“ klicken.
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/programm-menue.png`

* **Besetzung wechseln:** Die neue Besetzung kommt mit ihrem zuletzt
  benutzten Programm, bei einer Besetzung ohne Programm mit **— kein
  Programm —**. Ist die aktuelle Aufstellung nicht gespeichert, fragt das
  Programm vorher (*Besetzung wechseln*, **Verwerfen und laden**).
* **Programme ohne Besetzung:** Programme aus älteren Programmversionen,
  die noch keiner Besetzung gehören, stehen in der Liste **Programm** unter
  der Zwischenzeile *Ohne Besetzung:*. Wählen Sie eines, fragt das Programm
  einmal, zu welcher Besetzung es gehört (**Programm zuordnen**,
  **Zuordnen**). Gibt es noch keine Besetzung, speichern Sie zuerst eine.

Menü **⋯** neben **Besetzung**:

| Eintrag | Wirkung |
|---|---|
| **Als neue Besetzung speichern…** | Legt die aktuelle Aufstellung als neue Besetzung an, auf Wunsch mit einer Kopie des offenen Programms, siehe [Bestücken](populate.md#besetzung-speichern). |
| **Besetzung umbenennen…** | Neuer Name für die gewählte Besetzung. Einen Namen, den es schon gibt, lehnt das Programm ab (*Die Besetzung „…“ gibt es schon.*). |
| **Besetzung löschen…** | Löscht die gewählte Besetzung **samt ihren Programmen**. Die Rückfrage nennt die Programme, zum Beispiel *Besetzung „…“ samt 2 Programmen löschen?*. **Rückgängig** holt Besetzung und Programme zurück. |

Diese drei Einträge wirken sofort, ohne **Speichern**.

Menü **⋯** neben **Programm**:

| Eintrag | Wirkung |
|---|---|
| **Neues Programm…** | Legt ein neues Programm auf der gewählten Besetzung an (Name eingeben). Es übernimmt die aktuelle Startstellung von Weichen und Rädern. Ein neues Programm geht nur auf einer gespeicherten Besetzung: Ist die Aufstellung noch keine, fragt das Programm *Ein Programm gehört zu einer Besetzung. Die aktuelle Aufstellung ist noch keine gespeicherte Besetzung. Jetzt als Besetzung speichern?*; **Besetzung speichern…** öffnet den Dialog [Besetzung speichern](populate.md#besetzung-speichern). |
| **Programm umbenennen…** | Neuer Name für das gewählte Programm. |
| **Programm duplizieren** | Legt eine Kopie des Programms auf derselben Besetzung an (*… – Kopie*). |
| **Anderer Besetzung zuordnen…** | Das Programm gehört danach zu der Besetzung, die Sie im Dialog wählen (**Zuordnen**), und läuft mit deren Klöppeln. Der Simulator wechselt auf diese Besetzung. Prüfen Sie das Programm danach unter [Prüfen](check.md). Nur aktiv, wenn die Maschine mehr als eine Besetzung hat. |
| **Programm löschen…** | Löscht das gewählte Programm nach Rückfrage; endgültig ist es erst mit **Speichern**. |

Diese Programmänderungen speichern Sie mit **Speichern**. Die Einträge
beider Menüs brauchen das Recht *Flechtsimulator bearbeiten*. Dieselben
Befehle gibt es auch auf der [Startseite](index.md#startseite).

### Ansicht { #ansicht }

| Schalter | Zeigt | Standard |
|---|---|---|
| **Weichen mit Nummern** | Weichen und feste Bauteile mit ihrer W-Nummer, wie in der Zeitachse. Runde Symbole lassen sich schalten, eckige sind feste Bauteile. | an |
| **Laufrichtung** | Färbt jeden leeren Platz nach der Richtung, in die ein Klöppel dort um die Maschine liefe: die beiden Fadensysteme des Geflechts. Dazu Drehpfeile an den Naben, Richtungspfeile an den Klöppeln und unten links eine Legende (*im Uhrzeigersinn*, *gegen den Uhrzeigersinn*, *pendelt*, *bleibt am Rad*, *Sackgasse*). Fahren Sie mit der Maus über einen leeren Platz, zeigt die Ansicht dessen Bahn. | an |
| **Klöppelnummern** | Nummer jedes Klöppels und die Bezeichnung der Rohre. | aus |
| **Leere Plätze** | Leere Klöppelplätze. | an |
| **Einschnitte** | Die Einschnitte der Flügelräder. | an |
| **3D-Vorschau** | Blendet die [3D-Vorschau](views.md) ein oder aus. | an |
| **Maschine einpassen** | Zeigt die ganze Maschine (auch ++ctrl+0++ oder Doppelklick auf eine freie Stelle). | — |

Die Schalter merkt sich das Programm.

## Maschinenansicht

Die Maschine erscheint von oben, so wie sie in der Konstruktion liegt.
Neben den Klöppeln und Rädern sehen Sie:

* **Weichen** mit ihrer Nummer (*W12*); hängt eine Weiche an einem
  Stellhebel, steht der Hebel dahinter (*W12·H1*). Runde Symbole sind
  schaltbare Weichen, eckige feste Bauteile.
* **G1**, **G2** … an den Rädern einer Flügelradgruppe.
* ein **Lauf-Symbol** unter der Nabe von Rädern mit eigenem Antrieb
  (▶ läuft, ⏸ steht), siehe [Programm](program.md#rad).
* die **Radnummer** in der Nabe, wenn Sie mit der Maus darüberfahren oder
  das Rad ausgewählt ist.
* während der Aufnahme oben links ein rotes Band **Aufnahme läuft** mit
  Position und Zahl der aufgezeichneten Befehle.
* nach einer Kollision die markierte Stelle.

Was ein Klick bewirkt, hängt von der offenen Aufgabe ab, siehe
[Tasten und Maus](#tasten-und-maus).

## Aufgaben-Leiste und Auswahlkarte

Die rechte Leiste hat eine feste Breite. Unten liegen die vier Aufgaben:

| Reiter | Inhalt |
|---|---|
| [**Bestücken**](populate.md) | Klöppel setzen und färben; Garn und Rohrfäden. Ein Klick auf einen leeren Platz setzt einen Klöppel. |
| [**Programm**](program.md) | Weichen und Räder im Lauf, Drehzahl und Abzug. Ein Klick auf eine Weiche schaltet sie. |
| [**Prüfen**](check.md) | Fehler und Hinweise, Kollisionsprüfung über den ganzen Lauf. Ein roter bzw. oranger Punkt am Reiter zeigt Fehler bzw. Hinweise. |
| [**Ausgeben**](output.md) | Schaltplan für die Steuerung: drucken, als PDF oder CSV. |

Klicken Sie in der Maschine auf einen Klöppelplatz, eine Weiche, ein Rad
oder ein Rohr, erscheint darüber die **Auswahlkarte** mit dessen
Eigenschaften, zum Beispiel *Klöppel 7 ausgewählt* oder *Weiche W12
ausgewählt*. **✕** oder ++esc++ schließt sie, ebenso ein Klick ins Leere.

| Karte | Beschrieben unter |
|---|---|
| Klöppel, mehrere Klöppel, Rohr | [Bestücken](populate.md#auswahlkarte-kloppel) |
| Weiche, Stellhebel | [Programm](program.md#weiche) |
| Rad, Flügelradgruppe, Teilung | [Programm](program.md#rad) |

## Wiedergabeleiste { #wiedergabe }

Die Leiste über der Zeitachse steuert den Lauf der Simulation:

| Element | Wirkung |
|---|---|
| **Start** / **Pause** | Startet und hält an (++space++). Pause hält genau an der Stelle, auch mitten im Schritt. Nach einer Kollision startet die Wiedergabe nicht mehr, bis Sie zurückgehen. |
| Schritt zurück | Einen Schritt zurück, mitten im Schritt zuerst an den Schrittanfang (++arrow-left++). Geht auch nach einer Kollision. |
| Einzelschritt | Einen Schritt vor (++arrow-right++). |
| Zurücksetzen | Zurück an den Start. |
| **Aufnahme** | Schaltet die Aufnahme ein und aus, siehe [Programm](program.md#aufnahme). |
| Geschwindigkeit | **0,5**, **1** (Standard), **2** oder **4 Schritte/s**; dazu **Maschinentempo**, **Maschinentempo 1:4** und **Maschinentempo 1:10**: so schnell wie die echte Maschine bei der [Drehzahl](views.md#drehzahl) des Programms bzw. als Zeitlupe. Ohne Drehzahl im Programm läuft das Maschinentempo mit 1 Schritt/s. |
| **Gehe zu Schritt** | Schritt eingeben und ++enter++: Der Lauf wird vom Start bis dorthin durchgerechnet. Bei laufender Aufnahme wächst das Programm mit. |
| Schrittanzeige | *Schritt n* ohne Programm, *Programmschritt n/m* mit Programm, ab dem zweiten Durchlauf mit *· Zyklus n*. |
| **Zeitachse** | Blendet die [Zeitachse](program.md#zeitachse) aus und ein (nur mit Programm). Ausgeblendet bekommt die Maschine den Platz. |

Ganz unten zeigt eine Statuszeile links den Stand (zum Beispiel
*Programmschritt 3/48 · 32 Klöppel · Programm (Länge 48, wiederholt)*) und
die letzte Meldung, rechts den Zoom der Maschinenansicht.

## Speichern { #speichern }

**Speichern** schreibt eine geänderte Aufstellung in die gewählte
Besetzung und speichert die Programme. Ist keine Besetzung gewählt (zum
Beispiel nach **Alle Klöppel entfernen**), fragt das Programm nach einem
Namen (*Besetzung speichern*, **Name der Besetzung:**).

Verlassen Sie die Maschine mit ungespeicherten Änderungen (zurück, über
die Navigation oder beim Schließen des Programms), fragt das Programm
*Die Maschine „…“ hat ungespeicherte Änderungen. Vor dem Verlassen
speichern?* mit **Speichern**, **Verwerfen** und **Abbrechen**. Ohne das
Recht *Flechtsimulator bearbeiten* gibt es keine Rückfrage: Änderungen
gelten als ausprobiert und verfallen. Bearbeitet ein anderer Benutzer
gerade die Programme dieser Maschine, können Sie nur verwerfen oder
bleiben, siehe [Mehrere Benutzer](../basics/multi-user.md).

Ein Wechsel des Programms in der Kopfzeile fragt nicht nach: Ihre
Änderungen bleiben erhalten, bis Sie speichern oder verwerfen.

## Tasten und Maus { #tasten-und-maus }

### Maschinenansicht

| Aktion | Wirkung |
|---|---|
| Klick | **Bestücken:** Klöppel setzen (leerer Platz) bzw. auswählen. **Programm:** Weiche schalten. **Prüfen**, **Ausgeben:** auswählen. Während der Aufnahme schaltet ein Klick auf eine Weiche sie immer, gleich welche Aufgabe offen ist. |
| Rechtsklick | **Bestücken:** Klöppel entfernen. Sonst und während der Aufnahme: Weiche schalten. |
| ++ctrl++ + Klick, ++ctrl++ + Ziehen | Mehrere Klöppel wählen bzw. einen Rahmen um Klöppel ziehen. In **Programm**: Weichen zu einer Schaltgruppe sammeln. |
| ++ctrl+a++ | Alle Klöppel wählen. |
| ++esc++ | Auswahl aufheben. |
| Mausrad | Zoomen um den Mauszeiger. |
| Rechte oder mittlere Maustaste ziehen | Verschieben. |
| Doppelklick ins Leere, ++ctrl+0++ | Maschine einpassen. |

Liegen ein Klöppelplatz und eine Weiche übereinander, wählt der Klick den
Platz; die Weiche schalten Sie dann mit Rechtsklick.

### Tastatur

| Taste | Wirkung |
|---|---|
| ++space++ | Start und Pause (nicht in Eingabefeldern). |
| ++arrow-left++ / ++arrow-right++ | Schritt zurück / vor. Wirkt, wenn Sie vorher in die Maschinenansicht geklickt haben. |
| ++ctrl+a++ | Alle Klöppel wählen (Maschinenansicht hat den Fokus). |
| ++esc++ | Auswahl aufheben. |
| ++ctrl+z++ / ++ctrl+y++ | Rückgängig / Wiederholen. |
| ++ctrl+s++ | Speichern. |
| ++ctrl+0++ | Maschine einpassen. |

Die Kurzhilfe **?** fasst Maus und Tasten für Maschine, Wiedergabe,
Zeitachse und 3D-Vorschau zusammen.

## In der Web-App

Aufbau und Bedienung sind gleich. Abweichungen, Einzelheiten unter
[Flechtsimulator in der Web-App](../web/braiding-simulator.md):

* Ziehen mit der **linken** oder mittleren Maustaste verschiebt die
  Maschine; oben rechts liegen **Vergrößern**, **Verkleinern** und
  **Einpassen**.
* Im Menü **⋯** neben **Programm** heißen die Einträge **Umbenennen…** und
  **Duplizieren…**; beim Duplizieren fragt die Web-App nach dem Namen der
  Kopie.
* Die Geschwindigkeit hat zusätzlich **8 Schritte/s**.
* Am Smartphone steht alles untereinander, die Auswahlkarte kommt als
  Bogen von unten, und **langes Drücken** ersetzt den Rechtsklick.
* Die Rückfrage beim Verlassen heißt *Änderungen speichern?* mit
  **Speichern**, **Nicht speichern** und **Abbrechen**.

## Verwandte Seiten

* [Flechtsimulator](index.md) — Überblick und Startseite.
* [Bestücken](populate.md), [Programm](program.md), [Prüfen](check.md),
  [Ausgeben](output.md)
* [3D-Vorschau und Abzug](views.md)
