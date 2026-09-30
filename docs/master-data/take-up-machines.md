# Aufwickler

!!! abstract "Referenz — Aufwickler der Baureihen AW, AWS, AWST, AWSP, AWSA und AWH anlegen und pflegen: Trommelmaße, Traglast, Bauart, Haspel, Zubehör und Dokumente."

## Wofür Sie diesen Bereich nutzen

Unter *Stammdaten > Aufwickler* legen Sie die Aufwickler Ihres Werks an.
Ein Aufwickler steht hinter der Flechtmaschine und wickelt das fertige
Produkt auf eine Trommel oder eine Haspel. Seine Grenzen — welche Trommeln
er aufnimmt, wie schwer die bestückte Trommel sein darf, welche
Produktdurchmesser er verarbeitet — prüft Herzog CAB in der
[Trommel- und Aufwicklerwahl](../calculations/product/drum-take-up-selection.md)
und im [Flechtauftrag](../orders/braiding-order.md#tab-aufwicklung)
(Tab **Aufwicklung**). Im [Maschinenpark](../machine-park/index.md) haben
Aufwickler einen eigenen Filter.

!!! info "Neu ab Version 2.1.0"
    Aufwickler sind eine eigene Maschinenart. Die Liste ist aufgebaut wie
    bei den [Spulmaschinen](winding-machines.md); zum Anlegen und Bearbeiten
    öffnet sich ein eigener Dialog mit Trommelmaßen, Traglast und Bauart.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Die Aufwickler-Liste als Karten (Bild, Baureihe, „Trommel bis Ø … mm", Traglast und Verlegebreite) samt Werkzeugleiste.
    **So erzeugen:** Navigationspunkt *Stammdaten > Aufwickler* öffnen; einige Aufwickler der Baureihen AW, AWS und AWH (Demo-Daten „Musterbetrieb") anlegen, einen davon mit Haspel.
    **Ziel-Datei:** `assets/screenshots/master-data/aufwickler.png`

Oben liegt eine Werkzeugleiste, darunter die **Maschinenliste** als Karten.
Jede Karte zeigt Bild, Baureihe (ohne Baureihe *Aufwickler*) und die
wichtigsten Angaben:

* **Trommel bis Ø … mm** — der größte Trommeldurchmesser, bei einem
  Aufwickler mit Haspel stattdessen **Haspel … ccm**,
* **Traglast … kg** und **Verlegebreite … mm**, soweit hinterlegt.

### Werkzeugleiste

| Schaltfläche | Wirkung |
|---|---|
| **Maschine suchen** | Filtert die Liste. |
| **Neu** | Öffnet den Dialog *Neuen Aufwickler erstellen* (siehe unten). |
| **Bearbeiten** | Öffnet den gewählten Aufwickler im Dialog *Aufwickler bearbeiten*. |
| **Löschen** | Entfernt die gewählte(n) Maschine(n) mit Sicherheitsabfrage. |

Ein Doppelklick auf eine Karte öffnet den Aufwickler ebenfalls zum
Bearbeiten. Ein Rechtsklick öffnet ein Kontextmenü mit **Öffnen**,
**Bearbeiten**, **Duplizieren** und **Löschen**; die Kopie heißt
*„… (Kopie)"*.

!!! tip "Aufwickler aus dem Herzog-Katalog"
    Herzog-Aufwickler legen Sie am schnellsten über den
    [Herzog-Katalog](../catalog/index.md) an (Reiter **Aufwickler**): Technik
    und Bild kommen von dort, Sie tragen nur Gruppe, Seriennummer und Namen
    ein.

## Der Dialog „Neuen Aufwickler erstellen"

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Der Dialog *Neuen Aufwickler erstellen* mit den Abschnitten „Maschinendaten", „Maße und Grenzen" und „Bauart".
    **So erzeugen:** In *Stammdaten > Aufwickler* auf **Neu** klicken, Baureihe **AWS** wählen und die Maße mit Demo-Werten füllen; bis zum Abschnitt „Bauart" scrollen.
    **Ziel-Datei:** `assets/screenshots/master-data/aufwickler-neu-dialog.png`

Der Dialog ist von oben nach unten in Abschnitte gegliedert. Leere
Zahlenfelder zeigen einen Strich mit Einheit (z. B. *– mm*) und gelten als
nicht hinterlegt.

!!! tip "Unbekanntes leer lassen"
    Tragen Sie nur ein, was Sie wirklich wissen. Fehlt z. B. die
    **Traglast**, meldet die Trommel- und Aufwicklerwahl die Traglast als
    *nicht prüfbar* — statt eine Trommel vorzuschlagen, die den Aufwickler
    überlastet.

### Bild

* **Bild hochladen** – wählt ein Maschinenbild aus der
  [Medienbibliothek](media.md).
* **Bild aus Katalog übernehmen** – erscheint nur, solange der Aufwickler
  kein eigenes Bild hat und sein **Maschinentyp** einem Modell aus dem
  [Herzog-Katalog](../catalog/index.md) entspricht. Lädt das Katalogbild
  aus dem Internet (dafür ist eine Internetverbindung nötig).
* **Bild entfernen** – nimmt das Bild wieder weg.

Das Bild wird beim Speichern in den Arbeitsbereich kopiert und mit der
Maschine verknüpft.

### Maschinendaten

| Feld | Bedeutung |
|---|---|
| **Name** | Anzeigename der Maschine. Pflichtfeld. |
| **Baureihe** | Eine der Baureihen (siehe [unten](#die-baureihen)) oder *–*. Die Baureihe **AWH** setzt beim Wählen den Haken *Diese Maschine wickelt auf eine Haspel*. |
| **Maschinentyp** | Typbezeichnung, z. B. *AWS 2400*. Bleibt das Feld leer, wird die Baureihe als Maschinentyp gespeichert. Entspricht der Typ einem Katalogmodell, erscheinen dessen Zubehörvorschläge und das Katalogbild. |
| **Seriennummer** | Seriennummer der Maschine. |
| **Gruppe** | Frei vergebbare Gruppierung. |
| **Standort** | Halle/Werk/Abteilung. |
| **Baujahr** | Baujahr (oder *–*). |

### Maße und Grenzen

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Trommeldurchmesser (min–max)** | mm | Kleinster und größter Trommeldurchmesser, den der Aufwickler aufnimmt. |
| **Verlegebreite max.** | mm | Größte Verlegebreite; breitere Trommeln passen nicht. |
| **Traglast** | kg | Gesamtgewicht der bestückten Trommel: Trommel plus aufgewickeltes Produkt. |
| **Pinolendurchmesser** | mm | Durchmesser der Pinole. Er wird an die jeweilige Trommel angepasst und entscheidet nicht, ob eine Trommel passt. |
| **Geflechtdurchmesser (min–max)** | mm | Kleinster und größter Produktdurchmesser, den der Aufwickler verarbeitet (eine Nachkommastelle). |
| **Liniengeschwindigkeit (min–max)** | m/h | Geschwindigkeitsbereich des Aufwicklers. |

### Bauart

| Feld | Bedeutung |
|---|---|
| **Trommelhub** | *kein Hub*, *Handhubkurbel*, *elektrisch*, *hydraulisch* oder *motorischer Spindelantrieb* (oder *–*). |
| **Verlegung** | *Uhing*, *traversierende Trommel* oder *elektronische Parallelverlegung* (oder *–*). |
| **Zugregelung** | Ankreuzfelder *Flaschenzug*, *Tänzerarm*, *Servomotor*, *Drehmomentsteuerung* — mehrere zugleich möglich. |
| **Verlegeart** | Ankreuzfeld *traversierend*. |
| **Wickelspannung (min–max)** | Spannungsbereich in kg. |
| **Verlegeschritt (min–max)** | Kleinster und größter Verlegeschritt in mm. |
| **Steuerung** | *mechanisch*, *Display* oder *SPS mit Touchpanel* (oder *–*). |
| **Zähler** | Ankreuzfelder *Lagenzähler*, *Betriebsstundenzähler*, *Produktdatenverwaltung*. |

### Haspel statt Trommel

| Feld | Bedeutung |
|---|---|
| **Diese Maschine wickelt auf eine Haspel** | Ankreuzfeld für Aufwickler, die nicht auf eine wechselbare Trommel, sondern auf ihre eigene Haspel wickeln. Die Haspel gehört zum Aufwickler und wird nicht gewechselt. |
| **Haspelvolumen** | Aufnahmevolumen der Haspel in ccm. Nur bearbeitbar, wenn der Haken gesetzt ist. Begrenzt wird dann über das Haspelvolumen, nicht über den Trommeldurchmesser. |

### Zubehör

Das Zubehör des Aufwicklers zum Ankreuzen — wie bei den
[Flechtmaschinen](braiding-machines.md#zubehor): Vorschläge aus dem
Herzog-Katalog (sofern der Maschinentyp einem Katalogmodell entspricht)
und eigenes Zubehör über das Feld *Zubehör hinzufügen* mit **Hinzufügen**.
Gespeichert wird, was angekreuzt ist.

### Dokumente

Unterlagen zur Maschine mit den Spalten **Kategorie**, **Datei** und
**Beschreibung**. Beim Hinzufügen wählen Sie eine der Kategorien:

* Bedienungsanleitung
* Datenblatt
* Wartung
* Ersatzteile
* Sonstiges

Die Schaltflächen darunter sind **Dokument hinzufügen**, **Öffnen** und
**Dokument entfernen**.

### Speichern

Unten schließen Sie den Dialog mit **Aufwickler erstellen** ab oder
verwerfen ihn mit **Abbrechen**. Beim Bearbeiten heißt die Schaltfläche
**Speichern**.

Beim Speichern prüft der Dialog:

* Ohne Namen erscheint *Bitte einen Namen eingeben.*
* Ist bei einem der Bereiche (Trommeldurchmesser, Geflechtdurchmesser,
  Liniengeschwindigkeit, Wickelspannung, Verlegeschritt) der untere Wert
  größer als der obere, meldet der Dialog *„…: der untere Wert ist größer
  als der obere."* — ein verdrehter Bereich würde in der Trommel- und
  Aufwicklerwahl jeden Vorschlag verhindern.

## Die Baureihen

| Baureihe | Bezeichnung |
|---|---|
| **AW** | Aufwickler |
| **AWS** | Aufwickler mit Servoantrieb |
| **AWST** | Aufwickler mit traversierender Trommel |
| **AWSP** | Portalaufwickler |
| **AWSA** | Schwerlastaufwickler |
| **AWH** | Haspelaufwickler |

## Welche Angaben geprüft werden

Die [Trommel- und Aufwicklerwahl](../calculations/product/drum-take-up-selection.md)
und der Tab **Aufwicklung** im Flechtauftrag vergleichen Trommel und
Produkt mit diesen Angaben des Aufwicklers:

| Angabe des Aufwicklers | Wird verglichen mit |
|---|---|
| **Trommeldurchmesser (min–max)** | dem Außendurchmesser der Trommel |
| **Verlegebreite max.** | der Trommelbreite (sonst der Verlegeweite) der Trommel |
| **Geflechtdurchmesser (min–max)** | dem Produktdurchmesser |
| **Traglast** | dem Gewicht von Produkt und leerer Trommel |
| **Haspelvolumen** | bei Haspelaufwicklern: bestimmt, wie viel Produkt auf die Haspel passt |

Fehlt beim Aufwickler der größte Trommeldurchmesser, die Verlegebreite oder
die Traglast, lautet das Ergebnis *nicht prüfbar* statt *passt*. Die
übrigen Felder (z. B. Liniengeschwindigkeit, Wickelspannung, Pinole) sind
beschreibend.

## Verwandte Seiten

* [Trommeln](drums.md) – die Trommeln, auf die der Aufwickler wickelt
* [Trommel- und Aufwicklerwahl](../calculations/product/drum-take-up-selection.md) – passende Trommeln und Aufwickler finden
* [Flechtauftrag, Tab „Aufwicklung"](../orders/braiding-order.md#tab-aufwicklung) – Aufwickler und Trommel im Auftrag
* [Herzog-Katalog](../catalog/index.md) – Aufwickler von Herzog übernehmen
* [Abwickler](pay-off-machines.md) · [Gatter](creels.md) · [Spulmaschinen](winding-machines.md) · [Flechtmaschinen](braiding-machines.md)
* [Maschinenpark](../machine-park/index.md) – Betriebsübersicht aller Maschinen
