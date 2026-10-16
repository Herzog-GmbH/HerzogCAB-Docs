# Ausgeben: Schaltplan

!!! abstract "Referenz — Die Aufgabe „Ausgeben“: den Schaltplan eines Zeitprogramms für die Steuerung der Flechtmaschine drucken, als PDF oder als CSV-Tabelle speichern"

## Wofür Sie diesen Bereich nutzen

Der **Schaltplan** übersetzt ein Zeitprogramm in das, was die Steuerung der
echten Maschine braucht: wann welche Weiche, welcher Stellhebel, welches
Rad und welcher Abzug schaltet, jeweils mit Schritt,
Flügelradumdrehung, Zeit ab Start und Abzugslänge. Sie geben ihn an die
Elektrik- bzw. Steuerungsabteilung weiter oder legen ihn zum Programm in
die Auftragsunterlagen.

!!! info "Nur in der Desktop-App"
    Den Schaltplan gibt es nur im Programm. In der Web-App zeigt die
    Aufgabe **Ausgeben** nur einen Hinweis darauf, siehe
    [Web-App](../web/braiding-simulator.md).

Grundlage sind die **Zustände** der Simulation, nicht die einzelnen
Befehle: Der Schaltplan zeigt, was sich an der Maschine tatsächlich
ändert. Ein Stellhebel erscheint als **eine** Schaltung, wenn alle seine
Weichen zusammen umgelegt werden.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Aufgabe „Ausgeben“ in der rechten Leiste: Überschrift Schaltplan, Programmname, Programmlänge, Schaltpunkte, Abzugsbereiche, Druckvorlage „Standard Schaltplan“, Knöpfe Drucken…, Als PDF speichern…, Als CSV speichern….
    **So erzeugen:** Kundenbuild mit Modell-Lizenz, Maschine öffnen, ein Programm mit Abzug wählen, rechts den Reiter „Ausgeben“ öffnen.
    **Ziel-Datei:** `assets/screenshots/braiding-simulator/ausgeben.png`

Die Aufgabe **Ausgeben** (*Schaltplan für die Steuerung: drucken, als PDF
oder CSV.*) zeigt oben eine Zusammenfassung des gewählten Programms,
darunter die Druckvorlage und die Knöpfe.

## Bedienelemente im Detail

### Zusammenfassung

Unter der Überschrift **Schaltplan** stehen der Name des Programms und:

| Zeile | Bedeutung |
|---|---|
| **Programmlänge** | Länge eines Durchlaufs in Schritten. |
| **Schaltpunkte** | Wie viele Schritte eine Schaltung enthalten. |
| **Abzugsbereiche** | Wie viele Abschnitte mit eigenem Abzug das Programm hat (nur, wenn es welche gibt). |
| **Stellhebel** | Wie viele Stellhebel die Maschine hat (nur, wenn es welche gibt). |

Darunter stehen gelb die [Hinweise](#hinweise). Ist kein Programm gewählt,
steht dort *Kein Zeitprogramm gewählt. Oben unter „Programm“ ein Programm
wählen oder anlegen.*, und die Knöpfe sind gesperrt.

### Druckvorlage

Auswahl der Vorlage mit der Verwendung **Flechtsimulator**. Vorn steht
immer **Standard Schaltplan**. Eigene Vorlagen gestalten Sie im
[Druck-Editor](../print-templates/index.md): Dort gibt es die Verwendung
**Flechtsimulator** mit der Elementgruppe **Flechtsimulator** (Elemente
**Programmdaten**, **Startzustand**, **Schaltfolge**, **Abzug**,
**Stellhebel** und **Schaltdiagramm**). Das Programm merkt sich die
zuletzt gewählte Vorlage.

### Knöpfe

| Knopf | Wirkung |
|---|---|
| **Drucken…** | Öffnet den Schaltplan mit der gewählten Vorlage in der Druckvorschau (Fenster *Schaltplan: &lt;Programm&gt;*). |
| **Als PDF speichern…** | Speichert den Schaltplan mit der gewählten Vorlage als PDF. |
| **Als CSV speichern…** (Bereich **Daten**) | Speichert Programmdaten, Startzustand, Schaltfolge, Abzug, Stellhebel und die Zustände aller Weichen und Räder je Schaltpunkt als Tabelle, zum Beispiel für Excel. |

Beim Speichern schlägt das Programm den Dateinamen *&lt;Maschine&gt; -
&lt;Programm&gt; - Schaltplan* vor und merkt sich den Ordner. Danach
erscheint *Gespeichert: &lt;Datei&gt;*.

Zum Ausgeben genügt das Recht *Flechtsimulator anzeigen*, siehe
[Rechte](licence.md#rechte).

## Inhalt des Schaltplans

Die Vorlage **Standard Schaltplan** ist A4 quer und hat drei Seiten.
Seite 1 trägt den Titel *Schaltplan: &lt;Programm&gt;* mit Datum, die
Maschine, Programmdaten und Startzustand nebeneinander und das
Schaltdiagramm; Seite 2 die Schaltfolge; Seite 3 Abzug und Stellhebel.

### Programmdaten

| Zeile | Inhalt |
|---|---|
| **Version** | Fassung des Programms. |
| **Programmlänge** | Schritte je Durchlauf. |
| **Flügelradumdrehungen je Durchlauf** | |
| **Ablauf** | *wiederholt sich* oder *einmalig*. |
| **Schritte je Flügelradumdrehung** | |
| **Flügelraddrehzahl** | U/min oder *nicht gesetzt*. |
| **Schrittdauer** | Sekunden je Schritt. |
| **Dauer je Durchlauf** | Minuten und Sekunden. |
| **Abzugslänge je Durchlauf** | mm. |
| **Besetzung**, **Klöppel** | Name der Besetzung und Zahl der Klöppel. |
| **Materialdurchmesser** | mm. |
| **Flechtwinkel gemessen zur** | *Querrichtung* oder *Geflechtsachse* (nur, wenn das Programm Abzugsbereiche hat), siehe [Flechtwinkel-Bezug](views.md#flechtwinkel-bezug). |

### Startzustand

Wie Stellhebel, Weichen, Räder (laufen, stehen, Drehrichtung), Teilungen
und Abzug beim Start stehen; Spalten **Bauteil**, **Zustand**,
**Einzelheiten**.

### Schaltfolge

Je Schaltung eine Zeile mit **Nr.**, **Schritt**, **Umdrehung**, **Zeit ab
Start**, **Länge ab Start**, **Bauteil**, **Schaltung** und
**Einzelheiten**. Beispiele:

| Bauteil | Schaltung |
|---|---|
| *Weiche W3* | *schließen*, *öffnen* |
| *Stellhebel 1* | *auf …* (Stellung) |
| *Alle Räder* | *anhalten* (Klöppel parken), *starten*, *umkehren* |
| *Abzug* | neuer Abzug mit seiner Vorgabe |

Am Ende steht *Programmende nach Schritt n — weiter mit Schritt 1* (das
Programm wiederholt sich) oder *— alle Stellungen bleiben so*. Danach
folgen gegebenenfalls die Schaltungen, die beim Wiederholen nötig sind.

### Abzug, Stellhebel, Schaltdiagramm

* **Abzug** — die Abzugsbereiche mit Schritt, Länge, Abzug, Abzug je
  Umdrehung, Schlaglänge, Flechtwinkel, PPI und Vorgabe.
* **Stellhebel** — welche Weichen zu welchem Stellhebel gehören und wie
  sie in Stellung 1 und 2 stehen.
* **Schaltdiagramm** — ein Weg-Schritt-Diagramm: je Zeile ein Bauteil,
  dessen Zustand sich ändert, waagerecht die Programmschritte.

### CSV-Tabelle

Die CSV-Datei (Trennzeichen Semikolon) enthält dieselben Blöcke wie der
Druck. Die Zahlen stehen ohne Einheit in der Zelle, damit Excel mit ihnen
rechnen kann. Zusätzlich gibt es den Block **Zustände je Schaltpunkt**:
eine Zeile je Schaltpunkt mit einer Spalte je Weiche (W1, W2 …), je Rad
(R1, R2 …) und dem Abzug in m/min. Legende: *Weichen 1 = geschlossen, 0 =
offen · Räder 1 = läuft, 0 = steht, -1 = läuft gegen die
Konstruktionsrichtung · gilt bis zur nächsten Zeile*. Diesen Block gibt es
nur in der CSV, nicht im Druck.

## Hinweise { #hinweise }

Der Schaltplan meldet, was an der Maschine nicht so umsetzbar ist oder
noch fehlt. Im Druck stehen die Hinweise vorn in der Schaltfolge.

| Hinweis | Bedeutung |
|---|---|
| *Flügelraddrehzahl fehlt: Zeiten und Abzugslängen sind unbekannt.* | In der Zeitachse eine [Drehzahl](views.md#drehzahl) setzen. |
| *Schlaglänge, Flechtwinkel und PPI kommen aus der 3D-Vorschau: für vollständige Werte die Geflechtsvorschau einschalten.* | Die 3D-Vorschau ist ausgeblendet; über **Ansicht > 3D-Vorschau** einschalten. |
| *Stellhebel n steht beim Start gemischt — an der Maschine nicht möglich.* | Die Weichen eines Stellhebels stehen beim Start unterschiedlich. |
| *Im Programm wird ein Stellhebel nur teilweise umgestellt — an der Maschine nicht möglich. Die Weichen stehen einzeln in der Schaltfolge.* | Das Programm schaltet nur einen Teil der Weichen eines Stellhebels. |
| *Beim Wiederholen stehen Weichen oder Räder anders als beim ersten Start — der zweite Durchlauf weicht vom ersten ab.* | Das Programm kommt am Ende nicht in seinen Startzustand zurück. Siehe [Prüfen](check.md). |

## Verwandte Seiten

* [Programm](program.md) — das Zeitprogramm, aus dem der Schaltplan
  entsteht.
* [3D-Vorschau und Abzug](views.md) — Abzug und Drehzahl.
* [Druck-Editor](../print-templates/index.md) — eigene Vorlagen mit der
  Verwendung **Flechtsimulator**.
