# Färben und Texturieren

!!! abstract "Referenz — Malmodus, Farbpalette, Benutzerfarben, Farbwähler und Texturen: den Klöppeln Farben und Faser-Texturen zuweisen."

## Wofür Sie diesen Bereich nutzen

Das Muster eines Geflechts entsteht dadurch, **welcher Klöppel welche Farbe
führt**. Im Malmodus weisen Sie den Klöppelpositionen Farben und Faser-Texturen
zu — per Klick im Flechtbild oder in der Klöppeltabelle. Das Flechtbild
aktualisiert sich bei jeder Änderung sofort.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Werkzeugleiste des Designers mit geöffneter Farbpalette: großes
    Aktive-Farbe-Quadrat, Paletten-Auswahlliste, Bibliotheksfarben,
    Benutzerfarben-Reihe und Farbrad-Schaltfläche; daneben die Texturpalette
    mit großer Vorschau.
    **So erzeugen:** *Designer* öffnen, **Neu** klicken, Fenster breit ziehen,
    damit die Gruppen **Farbe** und **Texturen** in der Werkzeugleiste sichtbar
    sind.
    **Ziel-Datei:** `assets/screenshots/designer/designer-farbpalette.png`

## Bedienelemente im Detail

### Färben und Bewegen (Modus-Umschalter)

* **Färben** — der Malmodus (Standard): Klicks im Flechtbild oder in der
  Klöppeltabelle färben die getroffene Klöppelposition mit der aktiven Farbe.
  Im Flechtbild wird die Position unter dem Mauszeiger hervorgehoben, damit Sie
  sehen, was ein Klick treffen würde.
* **Bewegen** — der Verschiebemodus: die linke Maustaste verschiebt die
  Ansicht, es wird nichts gefärbt. (Verschieben per **rechter Maustaste**
  funktioniert in beiden Modi.)

### Seitenfilter Linkslauf / Rechtslauf

Rund- und Quadratgeflecht haben zwei Läufe. Die Schaltflächen **Linkslauf** und
**Rechtslauf** legen fest, welchen Lauf ein Klick einfärbt — es ist immer genau
eine der beiden aktiv. Bei Litzen- und Packungsgeflecht gibt es diese Auswahl
nicht; die Schaltflächen sind dann ausgeblendet.

### Aktive Farbe

Das große Quadrat links in der Gruppe **Farbe** zeigt die aktuell aktive Farbe —
mit ihr wird gefärbt. Ein Klick auf das Quadrat öffnet den Farbwähler-Dialog
(**Farbe wählen**) zur freien Farbwahl.

### Farbbibliothek (Paletten-Auswahl)

Die Auswahlliste über den Farbfeldern listet alle Farbpaletten aus der
zentralen Farbdatenbank ([Stammdaten > Farben](../master-data/colors.md)):

* **Standardpalette** — immer verfügbar; enthält zehn Programmfarben und
  darunter die zehn Benutzerfarben-Plätze (siehe unten).
* **Eigene Paletten** — alle Farben der gewählten Palette erscheinen als
  Farbfelder in Zehnerreihen. Bei sehr vielen Farben wird die Liste scrollbar;
  eine kleine Angabe darunter nennt die Gesamtzahl der Farben.

Jedes Farbfeld zeigt beim Überfahren den Farbnamen und den Farbwert an. Ein
Klick macht die Farbe zur aktiven Farbe — Farben aus der Bibliothek behalten
dabei ihre Zuordnung (Name, Pantone-/RAL-Referenz), die auch in der
Klöppeltabelle und auf Ausdrucken erscheint.

Die Schaltfläche neben der Auswahlliste (**Farbdatenbank öffnen**) springt
direkt zu *Stammdaten > Farben*, wo Sie Paletten und Farben pflegen.

### Benutzerfarben (10 Plätze)

In der Standardpalette stehen zehn frei belegbare Plätze (gestrichelt
umrandet) bereit:

| Aktion | Wirkung |
|---|---|
| Klick auf einen **leeren** Platz | Öffnet den Farbwähler (**Benutzerfarbe anlegen**) und belegt den Platz mit der gewählten Farbe. |
| Klick auf einen **belegten** Platz | Macht die gespeicherte Farbe zur aktiven Farbe. |
| **Rechtsklick** auf einen Platz | Öffnet den Farbwähler, um den Platz neu zu belegen. |

Benutzerfarben bleiben dauerhaft gespeichert und stehen beim nächsten Start
wieder zur Verfügung.

### Farbwähler (Farbrad)

Die Farbrad-Schaltfläche rechts neben der Palette öffnet den
Farbwähler-Dialog für Farben außerhalb der Bibliothek. Die gewählte Farbe wird
zur aktiven Farbe; ist die Standardpalette aktiv, wird sie zusätzlich auf dem
ersten freien Benutzerfarben-Platz abgelegt.

### Färben im Flechtbild

Klicken Sie im Malmodus auf eine Masche im Flechtbild — die zugehörige
Klöppelposition erhält die aktive Farbe (bzw. die aktive Textur). Bei Rund- und
Quadratgeflecht bestimmt der Seitenfilter, ob der Linkslauf oder der Rechtslauf
gefärbt wird.

### Färben in der Klöppeltabelle

Die Klöppeltabelle in der Mitte listet alle Klöppelpositionen mit ihrer
aktuellen Farbe:

* **Rund- und Quadratgeflecht:** zwei Spalten **Klöppel Links** und **Klöppel
  Rechts**.
* **Litzengeflecht:** eine Spalte **Klöppel**.
* **Packungsgeflecht:** eine Spalte je Gangbahn (**Bahn 1**, **Bahn 2**, …).

Ein Klick auf eine Zelle färbt genau diese Position.

!!! tip "Schnell viele Klöppel färben"
    Halten Sie die Maustaste gedrückt und ziehen Sie über die Zellen der
    Klöppeltabelle — alle überstrichenen Positionen erhalten die aktive Farbe.

### Texturen

* **Textur** (Werkzeugleiste) — schaltet die Texturdarstellung im Flechtbild
  ein oder aus (Standard: ein). Ausgeschaltet werden die Maschen als glatte
  Farbflächen gezeichnet.
* **Texturpalette** (Gruppe **Texturen** bzw. Schaltfläche **Muster**) — links
  eine große Vorschau der aktiven Textur, daneben die verfügbaren
  Faser-Texturen zur Auswahl. Ein Klick wählt die Textur und schaltet auf
  Texturdarstellung um.

Die angebotenen Texturen passen zur eingestellten
[Fachung](parameters.md) (Fadenzahl je Klöppel) und werden farblich passend zur
aktiven Farbe eingefärbt dargestellt.

!!! info "Schmale Fenster: Paletten als Popup"
    Reicht die Fensterbreite nicht aus, klappen die Gruppen **Farbe** und
    **Texturen** zu den Schaltflächen **Farbpalette** und **Muster** zusammen.
    Ein Klick öffnet die jeweilige Palette als Popup mit identischem Inhalt.

### Zurück und Vor (Rückgängig / Wiederherstellen)

**Zurück** (++ctrl+z++) macht den letzten Färbeschritt rückgängig, **Vor**
(++ctrl+y++) stellt rückgängig gemachte Schritte wieder her. Der Verlauf
umfasst alle Farb- und Texturzuweisungen seit dem Öffnen des Designs.

## Verwandte Seiten

* [Farben (Stammdaten)](../master-data/colors.md) — Paletten und Farben mit Pantone-/RAL-Referenz pflegen
* [Besetzung und Gangbahn-Animation](animation.md) — Farbbelegung entlang der Gangbahn rotieren
* [Geflechtsart und Parameter](parameters.md) — Fachung und Geflechtsart einstellen
* [Ein Design von Grund auf entwerfen](../tasks/design-from-scratch.md)
