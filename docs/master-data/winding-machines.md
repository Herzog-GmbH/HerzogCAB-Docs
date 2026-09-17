# Spulmaschinen

!!! abstract "Referenz — Spulmaschinen der Baureihen SP, SPA und HLM anlegen und pflegen: Stammdaten, Wickeltechnik, Abmessungen und Dokumente."

## Wofür Sie diesen Bereich nutzen

Unter *Stammdaten > Spulmaschinen* legen Sie die Spulmaschinen Ihres Werks an.
Anders als Flechtmaschinen haben Spulmaschinen keine Klöppel oder Geflechtsart,
sondern eine **Wickeltechnik** (Spulstellen, Drehzahl, Verlegung usw.). Die
Stammdaten werden in [Spulaufträgen](../orders/winding-order.md), in den
[Spulerei-Berechnungen](../calculations/winding/index.md), im
[Maschinenpark](../machine-park/index.md) und im
[Hallenplaner](../hall-planner/index.md) herangezogen.

!!! info "Neu ab Version 1.4.5"
    Die Spulmaschinen-Stammdaten sind Teil der Spulmaschinen-Integration. Die
    Liste ist genauso aufgebaut wie bei den [Flechtmaschinen](braiding-machines.md);
    zum Anlegen und Bearbeiten öffnet sich jedoch ein eigener Dialog mit
    spulspezifischen Feldern.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Die Spulmaschinen-Liste als Karten (mit Baureihe, Spulstellen,
    Spulen-Durchmesser und Drehzahl) samt Werkzeugleiste.
    **So erzeugen:** Navigationspunkt **Spulmaschinen** öffnen, einige
    Beispiel-Spulmaschinen der Baureihen SP/SPA/HLM (Demo-Daten „Musterbetrieb")
    anlegen.
    **Ziel-Datei:** `assets/screenshots/master-data/spulmaschinen.png`

Oben liegt eine Werkzeugleiste, darunter die **Maschinenliste** als Karten. Jede
Karte zeigt Bild, Baureihe und die wichtigsten Angaben: **Spulstellen**,
**Spulen-Ø** (maximaler Spulendurchmesser) und **UpM** (maximale Drehzahl).

### Werkzeugleiste

| Schaltfläche | Wirkung |
|---|---|
| **Suche** | Filtert die Liste. |
| **Neu** | Öffnet den Dialog *Neue Spulmaschine erstellen* (siehe unten). |
| **Bearbeiten** | Öffnet die gewählte Maschine zum Ändern. |
| **Löschen** | Entfernt die gewählte(n) Maschine(n) mit Sicherheitsabfrage. |

Ein Rechtsklick auf eine Karte öffnet ein Kontextmenü mit **Öffnen**,
**Bearbeiten**, **Duplizieren** und **Löschen**.

## Der Dialog „Neue Spulmaschine erstellen"

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Der Dialog *Neue Spulmaschine erstellen* mit Baureihenauswahl und
    dem Abschnitt „Wickeltechnik".
    **So erzeugen:** In **Spulmaschinen** auf **Neu** klicken; als Baureihe
    einmal SPA (zeigt den Abschnitt „Automatischer Spulenwechsel") und einmal HLM
    (zeigt „Litzenschlag") wählen.
    **Ziel-Datei:** `assets/screenshots/master-data/spulmaschine-neu-dialog.png`

Der Dialog ist von oben nach unten in Abschnitte gegliedert.

### Bild

* **Bild hochladen** – wählt ein Maschinenbild aus der
  [Medienbibliothek](media.md).
* **Bild entfernen** – nimmt das Bild wieder weg.

### Maschinendaten

| Feld | Bedeutung |
|---|---|
| **Name** | Anzeigename der Maschine. Pflichtfeld. |
| **Baureihe** | **SP**, **SPA** oder **HLM** (Pflichtfeld). Die Baureihe steuert, welche Zusatz­abschnitte erscheinen (siehe unten). |
| **Maschinentyp** | Typbezeichnung (z. B. „SP 280 Eltra Servo"). |
| **Seriennummer** | Seriennummer der Maschine. |
| **Gruppe** | Frei vergebbare Gruppierung. |
| **Standort** | Halle/Werk/Abteilung. |
| **Baujahr** | Baujahr (oder *Nicht gesetzt*). |

### Wickeltechnik

Diese Angaben gelten für alle Baureihen.

| Feld | Bedeutung |
|---|---|
| **Spulstellen** | Anzahl der Spulstellen (1–64). |
| **Spulendurchmesser (min–max)** | Kleinster und größter aufnehmbarer Spulendurchmesser in mm. |
| **Spullänge (min–max)** | Kleinste und größte Spullänge in mm. |
| **Drehzahl (min–max)** | Drehzahlbereich in UpM (Umdrehungen pro Minute). |
| **Verlegung** | Verlegesystem: *UHING-Rollringgetriebe (mechanisch)*, *Eltra-Servo (elektronisch)* oder *Kreuzspindel*. |
| **Wickelart** | *Parallelwicklung*, *Kreuzwicklung* oder *Präzisionswicklung*. |
| **Geschwindigkeitsführung** | Zwei Ankreuzfelder: *Konstante Spindeldrehzahl* und/oder *Konstante Fadengeschwindigkeit*. |
| **Fadenspannung** | Art der Fadenspannung: *Keine*, *Tellerbremse*, *Fadenspannungsüberwachung* oder *Winding Feeder (elektronisch geregelt)*. |
| **Steuerung** | *Mechanisch* oder *SPS mit Touchpanel*. |
| **Antrieb** | *Standardmotor* oder *Servomotor mit Absolutwertgeber*. |
| **Verlegeschritt (min–max)** | Kleinster und größter Verlegeschritt in mm. |
| **Verlegebreite max.** | Maximale Verlegebreite in mm. |
| **Spulengewicht max.** | Höchstgewicht einer vollen Spule in kg. |
| **Einrichtzeit je Auftrag** | Rüstzeit in Minuten, die einmal je Spulauftrag anfällt. Vorbelegung für die Spulzeit-Hochrechnung im [Spulauftrag](../orders/winding-order.md#spulmaschinen-verteiltabelle); dort je Auftrag übersteuerbar. |
| **Bestückungszeit je Spule** | Zeit in Minuten für den Spulenwechsel je Spule — bei vollautomatischem Spulenwechsel die Wechselzeit des Automaten. Ebenfalls Vorbelegung für den Spulauftrag. |
| **Zähler** | Ankreuzfelder *Meterzähler*, *Lagenzähler*, *Betriebsstundenzähler*, *Produktdatenbank*. |
| **Überwachung** | Ankreuzfelder *Fadenbruchüberwachung*, *Knotenüberwachung*, *Leerlaufüberwachung*. |
| **Materialien** | Ankreuzfelder für verarbeitbare Materialien: *Garn*, *Draht*, *Kohlefaser*, *Litze*, *Geflecht*. |
| **Passende Spulen** | Mehrfachauswahl aus der [Spulendatenbank](bobbins.md). |

### Automatischer Spulenwechsel (SPA)

Dieser Abschnitt erscheint nur, wenn als Baureihe **SPA** gewählt ist.

| Feld | Bedeutung |
|---|---|
| **Spulenwechsel** | Ankreuzfelder *Automatischer Spulenwechsel*, *Leerspulenmagazin*, *Vollspulenablage*. |
| **Fadenhandling** | Ankreuzfelder *Fadenschneider*, *Fadenfänger*. |

### Litzenschlag (HLM)

Dieser Abschnitt erscheint nur, wenn als Baureihe **HLM** gewählt ist.

| Feld | Bedeutung |
|---|---|
| **Schlaglänge (min–max)** | Kleinste und größte Schlaglänge in mm. |
| **Litzendurchmesser (min–max)** | Kleinster und größter Litzendurchmesser in mm. |
| **Schlagrichtung** | *S-Schlag*, *Z-Schlag* oder *S- und Z-Schlag*. |

### Abmessungen

Länge, Breite und Höhe in cm. **Länge und Breite** bestimmen die Grundfläche der
Maschine im [Hallenplaner](../hall-planner/index.md).

### Dokumente

Wie bei den Flechtmaschinen können Sie Unterlagen ablegen (Spalten
**Kategorie**, **Datei**, **Beschreibung**). Beim Hinzufügen wählen Sie eine der
Kategorien:

* Bedienungsanleitung
* Datenblatt
* Wartung
* Ersatzteile
* Sonstiges

Die Schaltflächen darunter sind **Dokument hinzufügen**, **Öffnen** und
**Dokument entfernen**.

### Speichern

Unten schließen Sie den Dialog mit **Maschine erstellen** ab oder verwerfen ihn
mit **Abbrechen**. Beim Bearbeiten heißt die Schaltfläche **Speichern**. Name
und Baureihe müssen ausgefüllt sein.

## Die Baureihen

| Baureihe | Bezeichnung |
|---|---|
| **SP** | Halbautomatische Spulmaschine |
| **SPA** | Vollautomatische Spulmaschine (mit automatischem Spulenwechsel) |
| **HLM** | Litzenschlagmaschine |

## Verwandte Seiten

* [Spulauftrag](../orders/winding-order.md) – Spulmaschine einem Auftrag zuordnen
* [Spulerei-Berechnungen](../calculations/winding/index.md) – Spulzeit,
  Fadengeschwindigkeit, Spulenkapazität u. a.
* [Spulen](bobbins.md) – Spulenformate zuordnen
* [Flechtmaschinen](braiding-machines.md) – Stammdaten der Flechtmaschinen
* [Maschinenpark](../machine-park/index.md) – Betriebsübersicht aller Maschinen
