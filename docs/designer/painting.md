# Färben und Texturieren

!!! abstract "Referenz — Malmodus, Farbpalette, Benutzerfarben, Farbwähler, Fachungsfarben und Texturen: den Klöppeln und ihren Garnen Farben und Faser-Texturen zuweisen."

## Wofür Sie diesen Bereich nutzen

Das Muster eines Geflechts entsteht dadurch, **welcher Klöppel welche Farbe
führt**. Im Malmodus weisen Sie den Klöppelpositionen Farben und Faser-Texturen
zu — per Klick im Flechtbild oder in der Klöppeltabelle. Das Flechtbild
aktualisiert sich bei jeder Änderung sofort.

## Der Bildschirm im Überblick

![Geöffnete Farbpalette mit aktiver Farbe, Auswahl „Standardpalette“, Farbfeldern und Farbrad-Schaltfläche](../assets/screenshots/designer/designer-farbpalette.png)

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

### Fachungsfarben (Farbe je Garn)

Ab einer [Fachung](parameters.md#fachung) von 2 laufen auf einem Klöppel
mehrere Garne nebeneinander auf derselben Bahn. Jedes dieser Garne kann eine
**eigene Farbe** bekommen — z. B. ein schwarzer Klöppel mit einem roten
Kennfaden. Garn 1 ist immer die Klöppelfarbe selbst.

![Designer mit Rundgeflecht und Fachung 3: Garn-Wähler in der Werkzeugleiste mit geöffnetem Menü Garn 1 bis Garn 3](../assets/screenshots/designer/designer-fachungsfarben.png)

**Garn-Wähler (Werkzeugleiste).** Rechts neben den Schaltflächen für
Linkslauf und Rechtslauf erscheint ab Fachung 2 eine Schaltfläche mit
Balkensymbol, beschriftet **Alle Garne** bzw. **Garn N**. Ihr Menü bietet
**Alle Garne** und darunter **Garn 1** … **Garn n**. Er legt fest, welches
Garn ein Klick in die Klöppeltabelle oder ins Flechtbild färbt:

| Auswahl | Wirkung eines Klicks mit der aktiven Farbe |
|---|---|
| **Alle Garne** | färbt den ganzen Klöppel in einer Farbe; vorhandene Garnfarben dieses Klöppels werden dabei aufgehoben. |
| **Garn N** | färbt nur dieses eine Garn des getroffenen Klöppels. |

Verkleinern Sie die Fachung unter das gewählte Garn, springt der Wähler auf
**Alle Garne** zurück.

**Fachungsfarben eines Klöppels im Dialog.** Ein **Rechtsklick** auf eine
Zelle der Klöppeltabelle färbt nicht, sondern öffnet ein Menü:

| Menüeintrag | Wirkung |
|---|---|
| **Fachungsfarben…** | Öffnet den Dialog *Fachungsfarben – &lt;Klöppel&gt;* (z. B. „– L3“ oder „– Bahn 2, Klöppel 4“). Ausgegraut bei Fachung 1 (*„Fachungsfarben gibt es ab Fachung 2.“*). |
| **Alle Garne wie Garn 1** | Hebt die eigenen Garnfarben dieses Klöppels auf; alle Garne laufen wieder in der Klöppelfarbe. Nur aktiv, wenn der Klöppel eigene Garnfarben hat. |

![Dialog „Fachungsfarben – L3“ mit den Farbknöpfen für Garn 1 bis Garn 3 und „Alle wie Garn 1“](../assets/screenshots/designer/designer-fachungsfarben-dialog.png)

Im Dialog steht je Garn eine Zeile **Garn N** mit einem Farbknopf, der den
Farbcode bzw. den Farbwert zeigt. Ein Klick auf den Farbknopf bietet die
**Aktive Farbe**, die Farben der aktuellen **Palette** und **Eigene Farbe
wählen…** an. **Alle wie Garn 1** gibt allen Garnen die Farbe von Garn 1;
**Übernehmen** schreibt die Farben in den Klöppel, **Abbrechen** verwirft
sie. Eigene Farben gibt es für bis zu 12 Garne je Klöppel; weitere Garne
laufen in der Klöppelfarbe. Jede Änderung lässt sich mit **Zurück**
rückgängig machen.

**Wo die Garnfarben erscheinen:**

* **Klöppeltabelle** — senkrechte Streifen je Garn, Garn 1 links.
* **Flechtbild** — jedes Garn als eigener Streifen **längs zum Faden**, in
  allen Ansichten (Voll, Halb, Zylinder, Vierkant, Kante), im Linkslauf wie
  im Rechtslauf und auch mit eingeschalteten Texturen.
* **Besetzungsübersicht** — der Klöppelpunkt ist in Kreisstücke je Garn
  geteilt, siehe [Besetzung und Gangbahn-Animation](animation.md).
* **3D-Ansicht** — jedes Garn in seiner Farbe, siehe
  [Ansichten und 3D-Ansicht](view-3d.md).
* **Ausdruck und Auftrag** — die Klöppelliste zeigt je Garn einen Streifen
  und die Farbangaben je Garn durch „ / “ getrennt (z. B. „STD-RED /
  STD-BLU“), siehe [Speichern und Drucken](save-print.md); ebenso die
  Klöppel-Tabelle im [Flechtauftrag](../orders/braiding-order.md) und die
  Farbaufschlüsselung im [Spulauftrag](../orders/winding-order.md#farbaufschlusselung).

!!! info "Trennlinien der Fachung"
    Ab Fachung 2 trennen dünne Linien die Garne jedes Klöppels im Flechtbild
    — **immer**, auch wenn alle Garne dieselbe Farbe haben. So sehen Sie auf
    einen Blick, dass gefacht wird. Die Linien sind so fein wie die Kontur
    der Maschen; nur wenn alle Garne einer Masche dunkel sind, werden sie
    hell gezeichnet.

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
* [Besetzung und Gangbahn-Animation](animation.md) — die Farben in der laufenden Maschine
* [Geflechtsart und Parameter](parameters.md) — Fachung und Geflechtsart einstellen
* [Ein Design von Grund auf entwerfen](../tasks/design-from-scratch.md)
