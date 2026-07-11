# Editor-Aufbau

!!! abstract "Referenz — Aufbau des Druck-Editors: Element-Palette, Seiten-Canvas, Eigenschaften"

Der Druck-Editor besteht aus drei Bereichen: der **Element-Palette** (links),
der **Seiten-Canvas** (Mitte) und den **Eigenschaften / Seiteneinstellungen**
(rechts).

![Aufbau des Druck-Editors mit den drei Bereichen.](../assets/screenshots/print-templates/druck-editor.png)

## Element-Palette (links)

Die Palette enthält alle Bausteine, die Sie auf die Seite ziehen können –
gegliedert in sechs Gruppen (Datentabellen, Datentabellen Flechterei,
Datentabellen Spulerei, Grafische Elemente, Firmenelemente, Freie Elemente).
Jedes Element ist im Detail unter [Elemente und Platzhalter](elements.md)
beschrieben.

Über das Auswahlfeld **Filter** grenzen Sie ein, welche Elemente in der Liste
erscheinen:

| Auswahl | Zeigt |
|---|---|
| **Aktuelle Vorlage** | Nur Elemente, die zur **Verwendung** der aktuell geöffneten Vorlage passen (z. B. bei einer Auftrags-Vorlage keine Eingabe-/Ergebnistabelle), plus die immer verfügbaren Firmen- und Freien Elemente. Voreinstellung. |
| **Alle anzeigen** | Blendet den Filter aus – alle Elemente aus allen Bereichen sind sichtbar. |
| **Berechnung / Design / Auftrag** | Zeigt gezielt nur die Elemente einer bestimmten Verwendung, unabhängig von der geöffneten Vorlage. |

Ein Element ziehen Sie per Drag-and-drop auf die Seiten-Canvas.

## Seiten-Canvas (Mitte)

Die Canvas zeigt die Seite originalgetreu. Elemente platzieren Sie per
Drag-and-drop, verschieben und skalieren sie direkt auf der Seite. Über die
Zoomregler oben (**−**, **+**, Prozentanzeige, **Einpassen**) passen Sie die
Darstellungsgröße an, ohne das Layout zu verändern.

Ein bereits platziertes Element bearbeiten Sie per Doppelklick – welcher
Dialog sich dabei öffnet, hängt vom Elementtyp ab und ist unter
[Elemente und Platzhalter](elements.md) beschrieben.

## Eigenschaften und Seiteneinstellungen (rechts)

Oben zeigt **Ausgewählt: …** den Namen des aktuell markierten Elements
(„Ausgewählt: −“, wenn nichts ausgewählt ist). Je nach Elementtyp folgen
darunter dessen Eigenschaften, z. B. Zeilen/Spalten bei Tabellen oder Inhalt,
Format und Textfarbe bei Textfeld und Datum/Zeit.

Darunter stellen Sie die Seiteneinstellungen der gesamten Vorlage ein:

| Einstellung | Bedeutung |
|---|---|
| **Papierformat** | A4 oder A3. |
| **Ausrichtung** | Hochformat oder Querformat. |
| **Verwendung** | Für welche Art Druck die Vorlage gilt: Berechnung, Design oder Auftrag. Bestimmt, in welchem Auswahldialog die Vorlage später auftaucht, und filtert die Element-Palette (siehe oben). |
| **Seiten** | Anzahl der Seiten der Vorlage. |
| **Seitenrand (mm)** | Randabstand der Seite. |

Darunter verwalten Sie die Seiten der Vorlage mit **Seite hinzufügen** und
**Seite entfernen** sowie die Vorlage selbst (**Speichern**, **Neue Vorlage**,
**Vorlage löschen**) – siehe [Vorlagen verwalten](manage.md).

!!! warning "Berechtigung erforderlich"
    Zum Bearbeiten und Speichern von Druckvorlagen benötigen Sie die
    Berechtigung **Druckvorlagen bearbeiten**. Ohne diese Berechtigung öffnet
    sich der Editor schreibgeschützt: Sie können Vorlagen ansehen, aber keine
    Änderungen speichern. Mehr zu Berechtigungen unter
    [Rollen](../admin/roles.md).

## Verwandte Seiten

* [Elemente und Platzhalter](elements.md) – alle Bausteine der Element-Palette im Detail
* [Vorlagen verwalten](manage.md) – Vorlagen anlegen, wählen, löschen
* [Vorschau und Druck](preview-and-print.md) – Seitenformat, Vorschau, Ausgabe
* [Eine Druckvorlage erstellen](../tasks/create-print-template.md) – Schritt-für-Schritt-Anleitung
* [Aufträge → Drucken](../orders/print.md) – wo Auftrags-Vorlagen zum Einsatz kommen
* [Designer → Speichern und Drucken](../designer/save-print.md) – wo Design-Vorlagen zum Einsatz kommen
