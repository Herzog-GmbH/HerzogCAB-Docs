# Ein Flechtprogramm erstellen

!!! example "Anleitung — am Ende liegt für eine Maschine ein geprüftes Zeitprogramm mit Besetzung vor, und der Schaltplan ist ausgedruckt oder als PDF gespeichert"

**Voraussetzungen:**

* Ihnen ist im Lizenzportal eine Modell-Lizenz für die Maschine
  zugewiesen, und Ihre Rolle hat *Flechtsimulator anzeigen* und
  *Flechtsimulator bearbeiten*, siehe [Lizenz und Rechte](../braiding-simulator/licence.md).
* Für den Schaltplan: die Desktop-App. Schritte 1 bis 6 gehen auch in der
  [Web-App](../web/braiding-simulator.md).

```mermaid
flowchart LR
  A["Maschine öffnen"] --> B["Besetzung anlegen"]
  B --> C["Besetzung prüfen"]
  C --> D["Programm anlegen<br>und aufnehmen"]
  D --> E["Abzug und Drehzahl"]
  E --> F["Prüfen"]
  F --> G["Speichern"]
  G --> H["Schaltplan ausgeben"]
  F -. Kollision .-> D
```

## Schritt 1: Maschine öffnen

1. Klicken Sie in der Navigation auf **Flechtsimulator** (Referenz:
   [Startseite](../braiding-simulator/index.md#startseite)).
2. Wählen Sie links die Maschine.
3. Klicken Sie rechts unter dem Abschnitt **Besetzungen und Programme**
   auf **Neue Besetzung**.

Die leere Maschine erscheint im
[Simulator-Bildschirm](../braiding-simulator/editor.md), die Aufgabe
**Bestücken** ist offen.

!!! tip "Tipp"
    Hat die Maschine schon eine passende Besetzung, klicken Sie in deren
    Karte auf **Öffnen**, passen die Besetzung in Schritt 2 an und
    speichern Änderungen mit **Speichern** statt mit **Als neue Besetzung
    speichern…**.

## Schritt 2: Besetzung anlegen

1. In der Aufgabe **Bestücken**
   ([Referenz](../braiding-simulator/populate.md)) setzen Sie mit einem
   Klick auf einen leeren Platz einen Klöppel.
2. Färben Sie die Klöppel: Klöppel anklicken und in der Auswahlkarte
   **Einzelfarben** wählen, oder mehrere mit ++ctrl++ + Klick wählen und
   **Farbe…** bzw. **Nach Laufrichtung färben**.
3. Stellen Sie bei Bedarf **Fachung** und **Anordnung** ein.
4. Tragen Sie unter **Garn** den **Materialdurchmesser** ein; erst dann
   rechnet die Vorschau in Millimetern.
5. Ziehen Sie bei Maschinen mit Rohren Zettelfäden oder einen Kern per
   Klick auf das Rohr ein.
6. Wählen Sie **Als neue Besetzung speichern…** und vergeben Sie einen
   Namen.

## Schritt 3: Besetzung prüfen

1. Ist oben unter **Programm** ein Programm gewählt, wählen Sie dort
   **— kein Programm —**. Ohne Programm prüft der Simulator die Besetzung
   mit der Startstellung der Weichen und Räder.
2. Öffnen Sie die Aufgabe **Prüfen** ([Referenz](../braiding-simulator/check.md))
   und klicken Sie auf **Aktuelle Aufstellung prüfen**.
3. Das Ergebnis muss *✅ Kollisionsfrei — Rapport nach … Schritten* sein.

Läuft schon die Besetzung nicht kollisionsfrei, passen Sie sie an, bevor
Sie ein Programm schreiben.

## Schritt 4: Programm anlegen und aufnehmen

1. Wählen Sie oben **⋯** neben **Programm** > **Neues Programm…** und
   vergeben Sie einen Namen. Das Programm gehört zur gewählten Besetzung
   und übernimmt die aktuelle Weichenstellung als Start.
2. Öffnen Sie die Aufgabe **Programm**
   ([Referenz](../braiding-simulator/program.md)).
3. Soll eine Weiche von Anfang an anders stehen, klicken Sie sie ohne
   Aufnahme an. Das ändert die Startstellung des Programms.
4. Klicken Sie in der Wiedergabeleiste auf **Aufnahme** und dann auf
   **Start**.
5. Drücken Sie an der Stelle, an der umgeschaltet werden soll, **Pause**
   (oder geben Sie den Schritt unter **Gehe zu Schritt** ein).
6. Klicken Sie die Weichen, die schalten sollen; bei einem Stellhebel
   genügt eine Weiche.
7. Lassen Sie weiterlaufen und schalten Sie später zurück. Klicken Sie am
   Ende auf **Aufnahme stoppen**.

Feinarbeit erledigen Sie in der [Zeitachse](../braiding-simulator/program.md#zeitachse):
Befehle verschieben, Schritte einfügen oder löschen. Befehle aus einem
anderen Programm dieser Maschine übernehmen Sie mit **Abschnitt
kopieren…** im Rechtsklick-Menü der Zeitachse.

## Schritt 5: Abzug und Drehzahl einstellen

1. Klicken Sie in der Zeitachse in der Zeile **Drehzahl** auf Schritt 1
   und tragen Sie die Flügelraddrehzahl ein.
2. Klicken Sie in der Zeile **Abzug** auf Schritt 1, wählen Sie die
   **Größe**, die Sie vorgeben wollen (zum Beispiel **Flechtwinkel**), und
   tragen Sie den **Wert** ein.
3. Braucht ein Abschnitt einen anderen Abzug, klicken Sie dort in die
   Zeile **Abzug** oder ziehen Sie über den Bereich.

Referenz: [Abzug](../braiding-simulator/views.md#abzug) und
[Drehzahl](../braiding-simulator/views.md#drehzahl). In der
[3D-Vorschau](../braiding-simulator/views.md) sehen Sie das Geflecht mit
diesen Werten.

## Schritt 6: Prüfen und speichern

1. Klicken Sie in **Prüfen** auf **Aktuelle Aufstellung prüfen**. Geprüft
   wird mit dem Programm, das oben unter **Programm** gewählt ist.
2. Bei ❌ springen Sie mit **Zum Schritt springen** zur Kollision und
   korrigieren den Befehl in der Zeitachse; dann erneut prüfen.
3. Ist der Rapport viel länger als das Programm, übernehmen Sie den
   Vorschlag **Länge …**.
4. Klicken Sie auf **Speichern** (++ctrl+s++).

## Schritt 7: Schaltplan ausgeben

1. Öffnen Sie die Aufgabe **Ausgeben** ([Referenz](../braiding-simulator/output.md)).
2. Prüfen Sie die orangefarbenen Hinweise; fehlt zum Beispiel die Drehzahl, sind
   Zeiten und Abzugslängen unbekannt.
3. Klicken Sie auf **Drucken…** oder **Als PDF speichern…**. Für die
   Weiterverarbeitung in Excel wählen Sie **Als CSV speichern…**.

## Ergebnis

* Auf der Startseite steht Ihre Besetzung als Karte unter **Besetzungen
  und Programme**, das Programm eingerückt darunter.
* Die Prüfung zeigt *✅ Kollisionsfrei — Rapport nach … Schritten*.
* Der Schaltplan liegt als Ausdruck, PDF oder CSV vor.

## Wenn etwas nicht klappt

* Die Maschine fehlt oder öffnet nicht: [Lizenz und Rechte](../braiding-simulator/licence.md#wenn-eine-lizenz-wegfallt).
* **Speichern** bleibt grau: Ihre Rolle braucht *Flechtsimulator
  bearbeiten*, oder ein Kollege bearbeitet gerade dieselbe Maschine.
* **Neues Programm…** fragt nach einer Besetzung: Ein Programm gehört
  immer zu einer gespeicherten Besetzung. Speichern Sie zuerst die
  Aufstellung (Schritt 2), siehe
  [Besetzung und Programm](../braiding-simulator/editor.md#besetzung-und-programm).
* Ein Teilungswechsel wirkt nicht: siehe
  [Teilung im Lauf](../braiding-simulator/program.md#teilung-im-lauf).
