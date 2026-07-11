# Speichern und Drucken

!!! abstract "Referenz — Designs in der Design-Bibliothek speichern (mit Zielordner-Auswahl) und mit Druckvorlage und Vorschau drucken."

## Wofür Sie diesen Bereich nutzen

Über die Dokument-Kopfzeile jedes Design-Fensters legen Sie das Design in der
[Design-Bibliothek](../master-data/designs.md) ab — beim ersten Speichern
wählen Sie dabei Namen und Zielordner. **Drucken** erzeugt aus dem Design ein
Belegblatt für die Maschine: mit Druckvorlage, Vorschau und allen aktuellen
Design-, Farb- und Klöppeldaten.

## Speichern

### Speichern

Schaltfläche **Speichern** in der Dokument-Kopfzeile oder ++ctrl+s++:

* **Bestehendes Design** — wird direkt aktualisiert. Eine kurze
  Erfolgsmeldung bestätigt das Speichern mit Name, Klöppelzahl, Flechtwinkel
  und Fachung.
* **Neues Design** — vor dem ersten Speichern öffnet sich der Dialog
  **Design speichern** (siehe unten), in dem Sie Namen und Zielordner
  festlegen. Brechen Sie den Dialog ab, wird das Design **nicht** gespeichert
  (Meldung *„Nicht gespeichert (abgebrochen)"*).

Beim Speichern erzeugt die App automatisch ein Vorschaubild — es erscheint in
der Design-Bibliothek und in der Liste **Zuletzt bearbeitet oder gespeichert**
auf der [Designer-Startansicht](index.md).

### Dialog „Design speichern" (Zielordner-Auswahl)

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Der Dialog **Design speichern** mit Namensfeld, dem Ordnerbaum
    der Design-Bibliothek (inklusive Eintrag „Ohne Ordner" und Unterordnern),
    der Zeile „Neuer Ordner (unterhalb der Auswahl)…" mit **Anlegen** sowie den
    Schaltflächen **Abbrechen** und **Speichern**.
    **So erzeugen:** Neues Design anlegen, etwas färben, **Speichern** klicken.
    **Ziel-Datei:** `assets/screenshots/designer/designer-speichern-dialog.png`

| Element | Funktion |
|---|---|
| **Designname** | Editierbares Namensfeld, vorbelegt mit dem Namen aus dem Parameter-Panel. Änderungen hier werden ins Design übernommen. |
| **Speicherort** (Ordnerbaum) | Die Ordnerstruktur der Design-Bibliothek, inklusive aller Unterordner. Der Eintrag *Ohne Ordner* legt das Design auf der obersten Ebene ab. Ein **Doppelklick** auf einen Ordner übernimmt ihn direkt und schließt den Dialog. |
| **Neuer Ordner (unterhalb der Auswahl)…** + **Anlegen** | Legt einen neuen Unterordner direkt unter dem aktuell markierten Ordner an (auch mit ++enter++ im Eingabefeld). Der neue Ordner wird sofort vorausgewählt. |
| **Abbrechen** | Schließt den Dialog, ohne zu speichern. |
| **Speichern** | Speichert das Design mit dem eingegebenen Namen im markierten Ordner. |

### Speichern unter neuem Namen

Schaltfläche **Speichern unter neuem Namen** in der Dokument-Kopfzeile: erzeugt
eine **Kopie** des aktuellen Designs als neuen Eintrag in der
Design-Bibliothek. Es öffnet sich derselbe Dialog **Design speichern** — dort
vergeben Sie den neuen Namen und wählen den Zielordner. Das Original bleibt
unverändert; Sie arbeiten anschließend an der Kopie weiter.

### Ungespeicherte Änderungen

Verlassen Sie ein Design mit ungespeicherten Änderungen — durch **Ansicht
schließen** (✕), das Laden eines anderen Designs oder das Beenden der App —
fragt die App mit **Änderungen speichern?** nach:

* **Ja** — speichert wie oben beschrieben (bei neuen Designs mit
  Zielordner-Dialog).
* **Nein** — verwirft die Änderungen.

!!! info "Speichern erfordert Bearbeitungsrechte"
    Zum Speichern brauchen Sie die Designer-Bearbeitungsberechtigung (siehe
    [Rollen und Rechte](../admin/roles.md)). Ohne dieses Recht sind die
    Speichern-Schaltflächen deaktiviert; Änderungen an geöffneten Designs
    werden beim Verlassen mit einem Hinweis verworfen.

## Drucken

### Druck starten und Vorlage wählen

Schaltfläche **Drucken** in der Dokument-Kopfzeile oder ++ctrl+p++. Gedruckt
wird über [Druckvorlagen](../print-templates/index.md); der Ablauf hängt davon
ab, welche Design-Vorlagen vorhanden sind:

* **Genau eine Vorlage** — die Druckvorschau öffnet sich direkt.
* **Mehrere Vorlagen** — der Dialog **Druckvorlage wählen** listet die
  Vorlagennamen; die passende Standardvorlage ist vorausgewählt.
* **Keine Vorlage** — die App bietet an, stattdessen den einfachen
  **Standarddruck** zu verwenden.

Für Designs bringt Herzog CAB zwei Standardvorlagen mit, die automatisch
passend zur Klöppelzahl angeboten werden:

| Standardvorlage | Für Designs mit … |
|---|---|
| Kompakte Design-Vorlage (eine Seite) | bis **48 Klöppeln** |
| Große Design-Vorlage (zwei Seiten, mit großer Besetzungsübersicht) | ab **49 Klöppeln** |

Es wird immer nur die zur aktuellen Klöppelzahl passende Standardvorlage
angezeigt; Ihre selbst angelegten Vorlagen erscheinen unabhängig von der
Klöppelzahl immer in der Auswahl.

### Druckvorschau

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Druckvorschau-Fenster eines Designs (Standardvorlage): Seite mit
    Flechtbild, Besetzungsübersicht und Klöppeltabelle, Zoom-Leiste und
    Drucken-Schaltfläche.
    **So erzeugen:** Design mit Farben öffnen, **Drucken** klicken, Vorlage
    bestätigen.
    **Ziel-Datei:** `assets/screenshots/designer/designer-druckvorschau.png`

Die Druckvorschau zeigt alle Seiten der gewählten Vorlage, bereits befüllt mit
den aktuellen Design-, Farb- und Klöppeldaten. Im Vorschau-Fenster stehen
Zoom-Funktionen und die **Drucken**-Schaltfläche bereit, über die Sie den
Ausdruck an den Drucker senden.

## Verwandte Seiten

* [Design-Bibliothek](../master-data/designs.md) — gespeicherte Designs verwalten, umbenennen, verschieben
* [Druckvorlagen](../print-templates/index.md) — eigene Design-Vorlagen gestalten
* [Vorschau und Druck](../print-templates/preview-and-print.md) — Druckvorschau im Detail
* [Ein Design von Grund auf entwerfen](../tasks/design-from-scratch.md)
