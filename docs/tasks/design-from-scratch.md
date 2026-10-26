# Ein Design entwerfen und drucken

!!! example "Anleitung — am Ende liegt ein fertig bemustertes Design in der Design-Bibliothek und als Ausdruck vor"

**Voraussetzungen:**

* Sie haben die Berechtigung, Designs anzulegen und zu speichern.
* Optional: eigene Farben in der [Farbdatenbank](../master-data/colors.md) —
  der Designer bringt aber auch ohne Vorarbeit eine Farbpalette mit.

```mermaid
flowchart LR
  A["Designer öffnen"] --> B["Geflechtsart & Parameter"]
  B --> C["Färben & Drehung"]
  C --> D["Besetzung & Animation prüfen"]
  D --> E["3D-Ansicht"]
  E --> F["Speichern"]
  F --> G["Drucken"]
```

## Schritt 1: Designer öffnen und neues Design anlegen

1. Öffnen Sie den Navigationspunkt **Designer** (Referenz:
   [Designer](../designer/index.md)).
2. Klicken Sie in der Werkzeugleiste auf **Neu** (++ctrl+n++). Ein
   leeres Design mit Standardwerten wird angelegt.

Ein bestehendes Design öffnen Sie stattdessen über **Laden** (++ctrl+o++) oder per
Doppelklick in der Liste „Zuletzt bearbeitet". Sie können zwei Design-Fenster
nebeneinander öffnen, um Varianten direkt zu vergleichen.

!!! tip "Geführte Tour"
    Beim ersten Besuch bietet der Designer eine
    [geführte Tour](../basics/guided-tour.md) an, die Schritt für Schritt
    durch das Anlegen eines Designs führt.

## Schritt 2: Geflechtsart und Parameter festlegen

Stellen Sie im linken Panel die Grunddaten des Designs ein: **Designname**,
**Geflechtsart** (Rundgeflecht, Litzengeflecht, Quadratgeflecht,
Spiralgeflecht, Packungsgeflecht oder Soutachegeflecht), **Geflechtsbindung**,
**Anzahl Klöppel**, **Flechtwinkel**
und **Fachung**. Jede Änderung baut das Flechtbild sofort neu auf.

Alle Parameter und ihre zulässigen Werte sind auf der Referenzseite
[Geflechtsart & Parameter](../designer/parameters.md) erklärt.

## Schritt 3: Färben und Drehung setzen

1. Aktivieren Sie das Werkzeug **Färben**.
2. Wählen Sie über **Farbpalette** eine Farbe (oder eine Farbe aus einer
   Bibliothek der [Farbdatenbank](../master-data/colors.md)).
3. Klicken Sie im Flechtbild oder in der Klöppeltabelle auf die Positionen,
   die diese Farbe erhalten sollen. Über den Seitenfilter färben Sie gezielt
   nur den Linkslauf oder nur den Rechtslauf.
4. Optional geben Sie Klöppeln eine Drehung: Klicken Sie auf **Drehung**,
   wählen Sie **S**, **Z** oder **Gerade** und bei Bedarf die **TPM**, und
   klicken Sie dann auf die Klöppel. Eine Farbe aus der Palette schaltet
   zurück aufs Färben.

Fehlgriffe machen Sie mit **Zurück** (++ctrl+z++) wieder rückgängig. Alle
Bedienelemente des Malmodus und der Drehung beschreibt die Referenzseite
[Färben & Drehung](../designer/painting.md).

## Schritt 4: Besetzung und Gangbahn-Animation prüfen

Die Besetzungsübersicht zeigt die Flügelräder der Maschine von oben mit den
zugewiesenen Farben je Klöppel:

1. Prüfen Sie, ob die Farben so auf den Klöppeln sitzen, wie Sie es
   geplant haben. Umfärben können Sie weiter im Flechtbild oder in der
   Klöppeltabelle; die Übersicht folgt sofort.
2. Starten Sie mit der Play-Schaltfläche die **Gangbahn-Animation**: Die
   Klöppel wandern über die Räder, und das Flechtbild baut sich synchron
   Lage für Lage auf. Das Tempo regeln Sie mit den
   Geschwindigkeits-Schaltflächen; ⏮ setzt Maschine und Aufbau auf den
   Anfang.

Details zu allen Schaltflächen: Referenzseite
[Besetzung & Gangbahn-Animation](../designer/animation.md).

## Schritt 5: 3D-Ansicht kontrollieren

Schalten Sie in der Werkzeugleiste mit dem Ansichts-Schalter **3D** die
3D-Ansicht ein (verfügbar für alle Geflechtsarten außer Mischdesigns). Sie
zeigt, wie sich das Muster am fertigen Geflechtstrang umlaufend fortsetzt.
Werkstoff und Form des Modells wählen Sie über die Schaltfläche
**Darstellung** — Referenz:
[Ansichten und 3D-Ansicht](../designer/view-3d.md).

## Schritt 6: Design in der Bibliothek speichern

1. Klicken Sie in der Kopfzeile des Design-Fensters auf **Speichern**.
2. Wählen Sie im Dialog den Zielordner der Design-Bibliothek (oder legen Sie
   direkt einen neuen Unterordner an) und vergeben Sie den Designnamen.

Eine Kopie unter neuem Namen erzeugen Sie mit **Speichern unter neuem
Namen**. Details: [Speichern & Drucken](../designer/save-print.md). Das
gespeicherte Design finden Sie anschließend in der
[Design-Bibliothek](../master-data/designs.md) unter *Stammdaten > Designs*.

## Schritt 7: Design drucken

1. Klicken Sie in der Kopfzeile des Design-Fensters auf **Drucken**.
2. Sind mehrere Druckvorlagen vorhanden, wählen Sie die gewünschte Vorlage
   aus; passend zur Klöppelzahl ist bereits eine Standardvorlage
   (**Standard Design** bzw. **Standard Design (hohe Klöppelzahl)**)
   vorausgewählt.
3. Prüfen Sie die Druckvorschau und starten Sie den Druck.

Details: [Speichern & Drucken](../designer/save-print.md); eigene Vorlagen
gestalten Sie im [Druck-Editor](../print-templates/index.md).

## Ergebnis

* Das Design liegt in der [Design-Bibliothek](../master-data/designs.md) und
  erscheint unter „Zuletzt geöffnet" auf der [Startseite](../basics/home.md).
* Der Ausdruck mit Flechtbild, 3D-Ansicht, Besetzungsübersicht und
  Besetzung ist fertig.
* Das Design kann jetzt im
  [Flechtauftrag](../orders/braiding-order.md) (Tab **Design**) verknüpft
  werden — siehe Ablauf
  [Vom Kundenauftrag zum Maschinenzettel](order-to-machine-sheet.md).

## Wenn etwas nicht klappt

* Der Ausdruck sieht falsch aus oder es passiert nichts →
  [Druckprobleme](../help/print-problems.md)
* Sie können keine weiteren Designs anlegen (Testversion) →
  [Testversion und Lizenz-Quoten](../basics/trial-quotas.md)
* Weitere Hilfe → [Hilfe-Übersicht](../help/index.md) und
  [Support kontaktieren](../help/support.md)
