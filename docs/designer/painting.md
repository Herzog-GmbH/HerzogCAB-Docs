# Färben und Drehung

!!! abstract "Referenz — Malmodus, Farbpalette, Benutzerfarben, Farbwähler, Fachungsfarben und der Pinsel Drehung: den Klöppeln und ihren Garnen Farben und eine Drehung zuweisen."

## Wofür Sie diesen Bereich nutzen

Das Muster eines Geflechts entsteht dadurch, **welcher Klöppel welche Farbe
führt**. Im Malmodus weisen Sie den Klöppelpositionen Farben zu — per Klick
im Flechtbild oder in der Klöppeltabelle. Mit dem Pinsel **Drehung** legen
Sie außerdem fest, ob die Garne eines Klöppels S-gedreht, Z-gedreht oder
gerade sind. Das Flechtbild aktualisiert sich bei jeder Änderung sofort.

## Der Bildschirm im Überblick

![Geöffnete Farbpalette mit aktiver Farbe, Auswahl „Standardpalette“, Farbfeldern und Farbrad-Schaltfläche](../assets/screenshots/designer/designer-farbpalette.png)

Die Schaltfläche **Farbpalette** in der Werkzeugleiste öffnet die
Farbpalette, die Schaltfläche **Drehung** rechts daneben das Fenster
**Drehung**. Beide Fenster öffnen sich unter ihrer Schaltfläche und
schließen sich beim Klick daneben oder mit ++esc++.

## Bedienelemente im Detail

### Färben und Bewegen (Modus-Umschalter)

* **Färben** — der Malmodus (Standard): Klicks im Flechtbild oder in der
  Klöppeltabelle färben die getroffene Klöppelposition mit der aktiven Farbe.
  Im Flechtbild wird die Position unter dem Mauszeiger hervorgehoben, damit Sie
  sehen, was ein Klick treffen würde. Ist der Pinsel **Drehung** gewählt,
  schaltet ein Klick auf **Färben** zurück aufs Färben.
* **Bewegen** — der Verschiebemodus: die linke Maustaste verschiebt die
  Ansicht, es wird nichts gefärbt. (Verschieben per **rechter Maustaste**
  funktioniert in beiden Modi.) In den Ansichten **Zylinder** und
  **Vierkant** dreht die linke Maustaste auch hier den Körper, siehe
  [Ansichten und 3D-Ansicht](view-3d.md).

### Seitenfilter Linkslauf / Rechtslauf

Rund- und Quadratgeflecht haben zwei Läufe. Die Schaltflächen **Linkslauf** und
**Rechtslauf** legen fest, welchen Lauf ein Klick einfärbt bzw. mit einer
Drehung versieht — es ist immer genau eine der beiden aktiv. Bei Litzen- und
Packungsgeflecht gibt es diese Auswahl nicht; die Schaltflächen sind dann
ausgeblendet.

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
Klöppeltabelle und auf Ausdrucken erscheint. Ist der Pinsel **Drehung**
gewählt, schaltet ein Klick auf eine Farbe zurück aufs Färben.

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
Klöppelposition erhält die aktive Farbe. Bei Rund- und Quadratgeflecht
bestimmt der Seitenfilter, ob der Linkslauf oder der Rechtslauf gefärbt wird.
In den Ansichten **Zylinder** und **Vierkant** färbt ein kurzer Klick;
Ziehen mit gedrückter Maustaste dreht dort den Körper.

### Färben in der Klöppeltabelle

Die Klöppeltabelle in der Mitte listet alle Klöppelpositionen mit ihrer
aktuellen Farbe:

* **Rund- und Quadratgeflecht:** zwei Spalten **Klöppel Links** und **Klöppel
  Rechts**.
* **Litzengeflecht:** eine Spalte **Klöppel**.
* **Packungsgeflecht:** eine Spalte je Gangbahn (**Bahn 1**, **Bahn 2**, …).

Ein Klick auf eine Zelle färbt genau diese Position. Hat ein Klöppel eine
Drehung, steht sie hinter der Nummer, siehe [Drehung](#drehung-s-z-oder-gerade).

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
**Alle Garne** zurück. Solange der Pinsel **Drehung** gewählt ist, ist der
Garn-Wähler gesperrt: Die Drehung gilt immer für alle Garne eines Klöppels.

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
  allen Zeichenansichten (Voll, Halb, Zylinder, Vierkant, Flechtbild), im
  Linkslauf wie im Rechtslauf und auch mit eingeschalteter Fadenstruktur.
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

### Drehung (S, Z oder gerade)

Mit dem Pinsel **Drehung** geben Sie jedem Klöppel die Drehung seiner Garne:
**S**, **Z** oder **Gerade** (ungedreht), auf Wunsch mit der Zahl der
Drehungen je Meter. Die Drehung gilt für alle Garne auf der Spule eines
Klöppels, nicht je Garn der Fachung.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Geöffnetes Fenster „Drehung“ unter der Schaltfläche **Drehung** mit den Knöpfen S, Z und Gerade, dem Feld TPM und dem Hinweistext; im Hintergrund die Klöppeltabelle mit Einträgen wie „3  S 120“.
    **So erzeugen:** Designer, Rundgeflecht mit einigen gedrehten Klöppeln, Schaltfläche **Drehung** rechts neben **Farbpalette** anklicken, S wählen, TPM 120 eintragen.
    **Ziel-Datei:** `assets/screenshots/designer/designer-drehung.png`

**Schaltfläche Drehung (Werkzeugleiste).** Sie liegt rechts neben
**Farbpalette** und trägt die gewählte Drehung im Namen, z. B. **Drehung S
120**. Ein Klick wählt den Pinsel, schaltet aus **Bewegen** in den Malmodus
und öffnet das Fenster **Drehung**:

| Element | Bedeutung |
|---|---|
| **S** | S-Drehung: die Fasern laufen bei senkrechtem Faden wie „\“. |
| **Z** | Z-Drehung: die Fasern laufen bei senkrechtem Faden wie „/“. |
| **Gerade** | Ungedrehte Fäden. |
| **TPM** | Drehungen je Meter, freiwillig, 0 bis 9999 in Zehnerschritten; „–“ bedeutet keine Angabe. Mit dem [Material-Ø](parameters.md#material-bedeckung-geflechts) bestimmt die TPM die Neigung der Drehungsstriche. Bei **Gerade** gesperrt. |

**Drehung setzen.** Klicken Sie auf einen Klöppel in der Klöppeltabelle oder
eine Masche im Flechtbild — der Klöppel erhält die gewählte Drehung samt
TPM. Der [Seitenfilter](#seitenfilter-linkslauf-rechtslauf) wirkt wie beim
Färben, und auch das Ziehen mit gedrückter Maustaste über die Klöppeltabelle
funktioniert. Eine Schaltfläche, die alle Klöppel auf einmal setzt, gibt es
nicht. Eine Farbe aus der Palette oder ein Klick auf **Färben** schaltet
zurück aufs Färben.

**Wo die Drehung erscheint:**

* **Klöppeltabelle** — hinter der Nummer, z. B. „3  S 120“ (Klöppel 3,
  S-Drehung, 120 TPM). Der Kurzhinweis schreibt sie aus (*Drehung S, 120
  TPM*). Gerade Klöppel zeigen nur die Nummer.
* **Flechtbild** — mit eingeschalteter **Fadenstruktur** zeichnet jede Masche
  die Garne der Fachung mit Faserglanz, gedrehte Garne mit Drehungsstrichen
  (S „\“, Z „/“). Die Neigung der Striche folgt aus TPM und Material-Ø; ohne
  TPM oder ohne Material-Ø gilt 30°, insgesamt bleibt sie zwischen 3° und
  75°. Die Fadenstruktur schalten Sie im Fenster
  [Darstellung](view-3d.md#fenster-darstellung) ein und aus.
* **3D-Ansicht** — mit dem Werkstoff **Garn** erscheinen gerade Garne glatt,
  S- und Z-Garne gedreht. **Draht** und **Seil** zeigen keine Drehung.
* **Ausdruck** — die Besetzungstabelle nennt die Drehung hinter der
  Klöppelnummer, siehe [Elemente und Platzhalter](../print-templates/elements.md#besetzung).

Die Drehung wird mit dem Design gespeichert und gilt für alle Geflechtsarten,
auch im Mischdesign. **Zurück** und **Vor** nehmen sie mit zurück bzw.
stellen sie wieder her.

!!! warning "Ältere Programmversionen verlieren die Drehung"
    Herzog CAB vor Version 2.1.2 kennt die Drehung nicht. Speichert ein
    solcher Rechner ein Design, geht die Drehung verloren. Arbeiten mehrere
    Rechner mit demselben Arbeitsverzeichnis, aktualisieren Sie alle.

### Zurück und Vor (Rückgängig / Wiederherstellen)

**Zurück** (++ctrl+z++) macht den letzten Schritt rückgängig, **Vor**
(++ctrl+y++) stellt rückgängig gemachte Schritte wieder her. Der Verlauf
umfasst alle Farb- und Drehungszuweisungen seit dem Öffnen des Designs.

## Verwandte Seiten

* [Farben (Stammdaten)](../master-data/colors.md) — Paletten und Farben mit Pantone-/RAL-Referenz pflegen
* [Besetzung und Gangbahn-Animation](animation.md) — die Farben in der laufenden Maschine
* [Ansichten und 3D-Ansicht](view-3d.md) — Fenster Darstellung mit Fadenstruktur und Werkstoff
* [Geflechtsart und Parameter](parameters.md) — Fachung, Material-Ø und Geflechtsart einstellen
* [Ein Design von Grund auf entwerfen](../tasks/design-from-scratch.md)
