# Flechtsimulator (Web-App)

!!! abstract "Referenz — Der Flechtsimulator im Browser: Aufruf, Startseite, Bedienung am PC und am Smartphone und alle Unterschiede zur Desktop-App"

## Wofür Sie diesen Bereich nutzen

Der Flechtsimulator der Web-App arbeitet mit denselben Maschinenmodellen,
Besetzungen und Programmen wie die Desktop-App: Was Sie im Browser
speichern, öffnet das Programm und umgekehrt. Aufbau und Bedienung sind
gleich, mit der Aufgaben-Leiste **Bestücken**, **Programm**, **Prüfen**
und **Ausgeben**. Die Felder und Knöpfe sind in der Referenz der
Desktop-App beschrieben ([Flechtsimulator](../braiding-simulator/index.md));
diese Seite nennt nur, was im Browser anders ist.

## Aufrufen

Der Eintrag **Flechtsimulator** steht in der Seitenleiste nach der
Parameter-Übersicht (Adresse `/flechtsimulator`). Am Smartphone öffnen Sie
ihn über **Menü** (☰) oder **Mehr**. Sie sehen ihn, wenn Ihr Konto die
Vollversion im Abo und mindestens eine gültige Modell-Lizenz hat und Ihre
Rolle das Recht *Flechtsimulator anzeigen* enthält, siehe
[Lizenz und Rechte](../braiding-simulator/licence.md). Läuft die letzte
gültige Modell-Lizenz des Kontos ab, verschwindet der Eintrag.

## Startseite

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Startseite des Flechtsimulators in der Web-App: links die Maschinen, rechts die gewählte Maschine mit Vorschau, Konfigurationen von Herzog, Meine Besetzungen, Meine Programme und den Knöpfen Neue Besetzung, Neues Programm, Öffnen.
    **So erzeugen:** Web-App lokal (127.0.0.1:5173), Seite `/flechtsimulator` mit einem Kundenkonto mit zugewiesener Modell-Lizenz; noch nicht im Skript `_tools/web_screenshots.py` (Name `flechtsimulator` ergänzen).
    **Ziel-Datei:** `assets/screenshots/web/flechtsimulator.png`
    <!-- web-bild ../assets/screenshots/web/flechtsimulator.png -->

Die Startseite entspricht der [Startseite der Desktop-App](../braiding-simulator/index.md#startseite).
Im Browser kommt hinzu:

* Unter dem Titel steht die Zahl der Maschinen; ab sieben Maschinen gibt
  es ein Suchfeld (Name, Katalogtyp, Ihre eigenen Maschinen).
* Ab 1024 px Breite stehen Liste und Details nebeneinander, darunter
  untereinander. Am Smartphone springt die Seite nach der Wahl zu den
  Details.
* Neben **Neue Besetzung** und **Neues Programm** gibt es den Knopf
  **Öffnen** für die gewählte Maschine.
* Die Liste lädt alle fünf Minuten und beim Zurückkehren ins Fenster neu;
  eine neue Zuweisung im Lizenzportal kommt so ohne Neuladen an.
* Ist Ihnen kein Modell zugewiesen, steht dort *Ihnen ist kein
  Maschinenmodell zugewiesen. Ihr Administrator weist Modell-Lizenzen im
  Lizenzportal zu.* Administratoren springen mit **Im Lizenzportal
  zuweisen** direkt zur Seite [Maschinenmodelle zuweisen](../portal/models.md).
* Den Hinweis *Neue Fassung von Herzog* merkt sich jeder Browser selbst.

Ihre eigenen Besetzungen und Programme gehören der Firma: Alle Benutzer
mit *Flechtsimulator anzeigen* können sie lesen; speichern kann, wem eine
gültige Lizenz dieses Modells zugewiesen ist und wer *Flechtsimulator
bearbeiten* darf.

## Der Simulator im Browser

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Flechtsimulator der Web-App am breiten Bildschirm: Kopf mit Besetzung und Programm, Maschine mit 3D-Vorschau daneben, rechts Auswahlkarte und Aufgaben-Leiste, unten Wiedergabeleiste und Zeitachse.
    **So erzeugen:** Web-App lokal (127.0.0.1:5173), Seite `/flechtsimulator/<id>` mit einem Programm, eine Weiche anklicken; noch nicht im Skript (Name `flechtsimulator-editor` ergänzen).
    **Ziel-Datei:** `assets/screenshots/web/flechtsimulator-editor.png`
    <!-- web-bild ../assets/screenshots/web/flechtsimulator-editor.png -->

Der Bildschirm ist aufgebaut wie in der Desktop-App
([Der Simulator-Bildschirm](../braiding-simulator/editor.md)). Die 3D-Vorschau
steht neben der Maschine, sobald genug Platz ist, sonst unter der
Zeitachse.

### Nur in der Web-App

| Funktion | Beschreibung |
|---|---|
| **Befehle (n)** | Aufklappbare Liste aller Befehle des Programms in der Aufgabe **Programm**. Je Befehl ändern Sie den **Schritt** (der Befehl wandert dorthin), springen mit **Zum Schritt springen** oder entfernen ihn mit **Befehl entfernen**. Befehle, die die Maschine nicht ausführen kann, stehen orange. |
| **Länge** | Die Programmlänge steht in der Aufgabe **Programm** (leer = so lang wie die Befehle). |
| **Umbenennen…**, **Duplizieren…** | Zusätzlich im Menü **⋯** neben **Programm**. Ein Programm von Herzog wird beim Umbenennen zur eigenen Kopie. |
| **Fadenspur (abgewickelt)** | In der Aufgabe **Ausgeben**: **Fadenspur berechnen** zeigt den Weg jedes Klöppels um das Geflecht, abgewickelt (Umfang waagerecht, Zeit nach unten, Rapport gestrichelt). |
| **8 Schritte/s** | Zusätzliche Geschwindigkeit der Wiedergabe. |
| **Vollbild** | Knopf in der 3D-Vorschau. |
| Prüfung läuft von selbst | Die Kollisionsprüfung rechnet nach jeder Änderung neu; einen Knopf **Aktuelle Aufstellung prüfen** gibt es nicht. |
| **Notizen** | In **Prüfen**, wenn Herzog zum Modell Notizen hinterlegt hat. |
| Farben | **Farbe für neue Klöppel** mit Auswahl der **Palette**, **Alle Klöppel färben** und **Farbdatenbank öffnen**. |

### Noch nicht in der Web-App

| Funktion der Desktop-App | Im Browser |
|---|---|
| [Schaltplan](../braiding-simulator/output.md) drucken, als PDF und CSV | **Ausgeben** zeigt nur: *Den Schaltplan für die Steuerung (Drucken, PDF, CSV) gibt es bisher nur in Herzog CAB am PC.* |
| [Bestücken nach Muster](../braiding-simulator/populate.md#bestucken-nach-muster) mit Wahl der Laufrichtung, eigenen Farben und **Mit dem Zeitprogramm prüfen** | Nur die Muster selbst und **Farbe je Laufrichtung** mit festen Farben. |
| **Bedeckung** | Nicht einstellbar; angezeigt wird sie in Infozeile, Abzug und Maschine 3D. |
| **Materialdurchmesser** je Besetzung | Gilt je Browser für alle Maschinen und wird nicht mit der Besetzung gespeichert. Ein Materialdurchmesser aus einem Programm der Desktop-App geht im Abzug vor. |
| [Rohrfäden](../braiding-simulator/populate.md#rohrfaden) per Klick einziehen | Rohrfäden kommen nur aus einer gespeicherten Besetzung. |
| [Betriebsart einfügen](../braiding-simulator/program.md#betriebsart-einfugen) | Fehlt. |
| Ansicht **Laufrichtung** färbt leere Plätze | Nur Drehpfeile und Richtungspfeile. |
| Zeitachse: Rechtsklick-Menü (Schritte einfügen/löschen, Abschnitt verschieben/kopieren), Zeilen markieren, Befehl durch Ziehen verschieben | Fehlt. Befehle verschieben Sie über die Befehlsliste. Ziehen in einer Zeile legt den Zustand über den Bereich. |
| Prüfung mit Farbbild, Rückkehr der Klöppel und Abbindung je Abschnitt | Nur Kollision, Rapport und Klöppelzahl, dazu *Alle Befehle lassen sich an der Maschine ausführen.* oder die Befunde. |
| Klöppel mitten im Lauf setzen | Nur im Stand: *Klick auf einen Platz setzt oder entfernt einen Klöppel (nur im Stand).* |

### Weitere Unterschiede

* **Maus:** Ziehen mit der **linken** oder mittleren Taste verschiebt die
  Maschine. Oben rechts gibt es Knöpfe **Vergrößern**, **Verkleinern**
  und **Einpassen**.
* **Zeitachse:** Stellhebel haben eine eigene Zeile, die Räder stehen in
  einer Zeile **Alle Räder**, dazu je Flügelradgruppe, Switch-out-Rad,
  Dreheinheit und Teilung eine Zeile. Nach einer Änderung bleibt die
  Wiedergabe am aktuellen Schritt.
* **Aufnahme:** Während der Aufnahme spielt das Programm ohne
  Wiederholung; beim Stoppen wächst die Programmlänge bis zum erreichten
  Schritt.
* **Anhalten und Umkehren** von Flügelradgruppen und Switch-out-Rädern
  kennt ohne Aufnahme keine Variante *nur für diesen Lauf*, wie es sie für
  Weichen gibt.
* **Rückgängig** wirkt auf Programmänderungen, nicht auf einzelnes Setzen
  oder Färben von Klöppeln.
* **Ohne *Flechtsimulator bearbeiten*** fehlen Aufnahme, **Startzustand
  übernehmen**, **Drehzahl ändern…**, **Abzug ändern…** und **Als neue
  Besetzung speichern…**; Klöppel setzen und färben geht zum Ausprobieren.
* Die Ansicht-Schalter, die Aufgabe, das Tempo und die Einstellungen der
  3D-Vorschau merkt sich jeder Browser.

## Am Tablet und Smartphone

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Flechtsimulator am Smartphone (390 px breit): Maschine oben, darunter Wiedergabe und Zeitachse, die Auswahlkarte einer Weiche als Bogen am unteren Rand.
    **So erzeugen:** Web-App lokal (127.0.0.1:5173), Seite `/flechtsimulator/<id>` bei 390 px Breite, Weiche antippen; noch nicht im Skript (Name `flechtsimulator-handy` ergänzen).
    **Ziel-Datei:** `assets/screenshots/web/flechtsimulator-handy.png`
    <!-- web-bild ../assets/screenshots/web/flechtsimulator-handy.png -->

Unter 1024 px Breite steht alles untereinander: Kopf, Maschine,
Wiedergabeleiste, Zeitachse, Aufgaben, 3D-Vorschau.

| Geste | Wirkung |
|---|---|
| Antippen | Wie ein Klick, je nach Aufgabe. |
| **Lange drücken** | Wie ein Rechtsklick: in **Bestücken** Klöppel entfernen, sonst Weiche schalten. |
| Ein Finger senkrecht | Rollt die Seite; waagerecht verschiebt er die Maschine. |
| Zwei Finger | Zoomen. |

* Die **Auswahlkarte** erscheint als Bogen am unteren Rand; die Maschine
  bleibt darüber sichtbar.
* Mehrere Klöppel wählen Sie mit **Alle Klöppel auswählen**; Strg+Klick
  und Rahmen gibt es nur mit Maus und Tastatur.
* In der 3D-Vorschau ist die Ansicht zunächst **gesperrt**, damit ein
  Finger die Seite rollt. Tippen auf das Schloss gibt das Drehen frei; in
  der Ansicht **Maschine** gibt es das Schloss nur auf Touch-Geräten.
* Die Chips **⛔ Fehler** und **⚠ Hinweise** rollen zur Aufgabe **Prüfen**.

## Speichern, Bearbeitungssperre, Entzug

* **Speichern** (++ctrl+s++) schreibt Ihre Besetzungen und Programme auf
  den Server (*Maschine gespeichert.*). Verlassen Sie die Seite mit
  Ungespeichertem, fragt die Web-App *Änderungen speichern?* mit
  **Speichern**, **Nicht speichern** und **Abbrechen**; beim Schließen des
  Tabs warnt der Browser.
* Hat ein Kollege dieselbe Maschine offen, erscheint *In Bearbeitung – nur
  lesen* mit **Erneut versuchen**; wird sie frei, *Jetzt frei – neu laden*.
  Siehe [Mehrere Benutzer](../basics/multi-user.md).
* Wird Ihnen das Modell entzogen oder läuft die Lizenz ab, hält die
  Wiedergabe an, siehe [Lizenz und Rechte](../braiding-simulator/licence.md#wenn-eine-lizenz-wegfallt).

## Verwandte Seiten

* [Flechtsimulator](../braiding-simulator/index.md) — Referenz mit allen
  Feldern.
* [Ein Flechtprogramm erstellen](../tasks/create-braiding-program.md)
* [Maschinenmodelle zuweisen](../portal/models.md)
* [Einstellungen](settings.md#flechtwinkel) — Flechtwinkel-Bezug, gilt auch
  im Simulator.
