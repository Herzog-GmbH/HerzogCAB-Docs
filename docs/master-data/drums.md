# Trommeln

!!! abstract "Referenz — Trommeln (Maße, Spulvolumen, Leergewicht, Aufnahme) einmal anlegen und in Berechnungen und Aufträgen wiederverwenden."

## Wofür Sie diesen Bereich nutzen

Unter *Stammdaten > Trommeln* pflegen Sie die Trommeln, auf die Ihre
Aufwickler das fertige Produkt wickeln. Die Datenbank führt Bauarten, keine
einzelnen Trommeln: Eine Trommel mit denselben Maßen legen Sie einmal an,
egal wie viele davon im Werk sind. Die Trommeln werden in diesen Bereichen
ausgewählt:

* [Produktlänge pro Trommel](../calculations/product/rope-length-on-drum.md),
* [Trommel- und Aufwicklerwahl](../calculations/product/drum-take-up-selection.md),
* im [Flechtauftrag](../orders/braiding-order.md#tab-aufwicklung), Tab
  **Aufwicklung**.

!!! info "Neu ab Version 2.1.0 — Arbeitsverzeichnisse starten ohne Trommeln"
    Neue Arbeitsverzeichnisse enthalten keine mitgelieferten Trommeln mehr.
    Die Trommeln und Haspeln von Herzog übernehmen Sie mit
    **Aus Herzog-Katalog …**; eigene Trommeln legen Sie daneben an — genau
    wie bei den [Spulen](bobbins.md). Vorhandene Arbeitsverzeichnisse
    bleiben unverändert.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Die Seite *Trommeln*: links die Trommeldatenbank mit Suche, Filter „Materialart" und Trommel-Karten, rechts „Trommel bearbeiten" mit allen Maßfeldern und dem Abschnitt „Trommelaufnahme".
    **So erzeugen:** *Stammdaten > Trommeln* öffnen, einige Trommeln über **Aus Herzog-Katalog …** übernehmen und eine davon auswählen.
    **Ziel-Datei:** `assets/screenshots/master-data/trommeln.png`

Die Seite ist aufgebaut wie der [Spulen-Editor](bobbins.md):

* **Trommeldatenbank** (links) – Suche, Filter **Materialart**, die Liste
  der Trommeln als Karten und darunter die Schaltflächen zum Anlegen.
* **Trommel bearbeiten** (rechts) – die Eigenschaften der gewählten
  Trommel.

## Bedienelemente im Detail

### Suche und Filter

* **Suche** – filtert nach Bezeichnung, Artikelnummer, Durchmesser oder
  Volumen.
* **Materialart** – schränkt die Liste auf *Holz*, *Stahl*, *Kunststoff*
  oder *Sonstiges* ein (Standard: *Alle Materialarten*).

Über der Liste steht, wie viele Trommeln gezeigt werden (*„12 Trommeln"*
bzw. *„3 von 12 Trommeln"*). Ist die Datenbank leer, steht dort
*Noch keine Trommeln. Übernehmen Sie sie mit "Aus Herzog-Katalog …".*

### Die Trommel-Karten

Jede Karte zeigt:

* die **Bezeichnung** — ohne Bezeichnung die Maßzeile,
* die Maßzeile *Ø Außendurchmesser / Ø Kerndurchmesser / Verlegeweite /
  Spulvolumen*,
* Artikelnummer, Materialart und das Leergewicht (*„… kg leer"*) — fehlt
  es, steht dort *Leergewicht fehlt*.

### Neue Trommel und Aus Herzog-Katalog …

| Schaltfläche | Wirkung |
|---|---|
| **Neue Trommel** | Leert das Formular rechts für eine neue Trommel. Die Schaltfläche **Speichern** heißt dann **Trommel anlegen**. |
| **Aus Herzog-Katalog …** | Öffnet den [Herzog-Katalog](../catalog/index.md) im Reiter **Trommeln**. Dort übernehmen Sie Herzog-Trommeln mit ihren Maßen per **Zu Trommeln hinzufügen**. Nicht in Herzog CAB Designer. |

!!! note "Was aus dem Katalog kommt"
    Übernommene Trommeln bringen Bezeichnung, Materialart, Maße und
    Spulvolumen mit. Das Feld **Artikelnummer** bleibt leer — es ist für
    Ihre eigene Nummer gedacht. Das **Leergewicht** tragen Sie selbst nach;
    ohne Leergewicht meldet die Trommel- und Aufwicklerwahl die Traglast
    als *nicht prüfbar*. Haspeln aus dem Katalog lassen sich nicht
    übernehmen.

### Felder einer Trommel

| Feld | Einheit | Beschreibung |
|---|---|---|
| **Bezeichnung** | – | Freier Name, z. B. *Holztrommel 420 x 250*. Leer = die Maßzeile dient als Name. |
| **Artikelnummer** | – | Frei, Ihre eigene Nummer. |
| **Materialart** | – | *Holz*, *Stahl*, *Kunststoff*, *Sonstiges* oder *— keine Angabe —*. |
| **Außendurchmesser [mm]** | mm | Durchmesser über die Flansche. Pflichtfeld. |
| **Wickeldurchmesser [mm]** | mm | Durchmesser, bis zu dem tatsächlich gewickelt wird. Leer lassen, wenn bis zur Flanschkante gewickelt wird — dann gilt der Außendurchmesser. |
| **Kerndurchmesser [mm]** | mm | Durchmesser des Trommelkerns. Pflichtfeld; muss kleiner sein als der Wickeldurchmesser. |
| **Verlegeweite [mm]** | mm | Bewickelbare Breite zwischen den Flanschen. |
| **Trommelbreite [mm]** | mm | Breite über alles. Leer lassen, wenn sie der Verlegeweite entspricht. |
| **Spulvolumen [ccm]** | ccm | Aufnahmevolumen der Trommel. Wird aus den Maßen hergeleitet (siehe unten) und bleibt überschreibbar. |
| **Leergewicht [kg]** | kg | Gewicht der leeren Trommel. Zählt zur Traglast des Aufwicklers. |

Verlegeweite und Trommelbreite vertreten sich gegenseitig: Ist nur eines der
beiden Felder gefüllt, gilt es für beide.

!!! tip "Spulvolumen automatisch herleiten"
    Solange Sie das Feld **Spulvolumen [ccm]** nicht selbst ändern, rechnet
    Herzog CAB es bei jeder Maßänderung neu — aus dem Wickeldurchmesser
    (sonst dem Außendurchmesser), dem Kerndurchmesser und der Verlegeweite
    (sonst der Trommelbreite). Haben Sie das Volumen von Hand eingetragen,
    etwa den Wert aus einem Datenblatt, bleibt es stehen. Die
    Rechen-Schaltfläche am Feld schaltet die Herleitung wieder ein.

### Abschnitt „Trommelaufnahme"

Optionale Maße der Aufnahme am Aufwickler:

| Feld | Einheit | Beschreibung |
|---|---|---|
| **Pinolenbohrung [mm]** | mm | Durchmesser der Bohrung für die Pinole. |
| **Mitnahme-Pin [mm]** | mm | Durchmesser des Mitnahme-Pins. |
| **Abstand Mitte zu Pin [mm]** | mm | Abstand von der Trommelmitte zum Mitnahme-Pin. |

### Speichern und Löschen

* **Speichern** (bzw. **Trommel anlegen**) – sichert die Trommel. Fehlen
  Außendurchmesser, Kerndurchmesser oder Verlegeweite (bzw.
  Trommelbreite), erscheint *Außendurchmesser, Kerndurchmesser und
  Verlegeweite werden gebraucht.*; ist der Kern nicht kleiner als der
  Wickeldurchmesser, erscheint *Der Kerndurchmesser muss kleiner sein als
  der Wickeldurchmesser.*
* **Löschen** – entfernt die gewählte Trommel nach der Rückfrage
  *Soll die Trommel "…" gelöscht werden?*

!!! warning "Berechtigung erforderlich"
    Zum Anlegen, Ändern und Löschen brauchen Sie das Recht **Stammdaten
    bearbeiten**. Ohne dieses Recht sehen Sie alle Werte, können sie aber
    nicht ändern; Suche und Filter bleiben bedienbar.

## Verwandte Seiten

* [Aufwickler](take-up-machines.md) – welche Trommeln ein Aufwickler aufnimmt
* [Trommel- und Aufwicklerwahl](../calculations/product/drum-take-up-selection.md) – passende Trommel vorschlagen lassen
* [Produktlänge pro Trommel](../calculations/product/rope-length-on-drum.md) – Länge auf einer Trommel
* [Herzog-Katalog](../catalog/index.md) – Trommeln von Herzog übernehmen
* [Spulen](bobbins.md) – gleich aufgebaute Stammdaten für Klöppelspulen
