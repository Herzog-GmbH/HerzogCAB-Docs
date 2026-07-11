# Designs

!!! abstract "Referenz — die Design-Bibliothek: gespeicherte Flechtdesigns in Ordnern verwalten, öffnen, umbenennen, verschieben und löschen."

## Wofür Sie diesen Bereich nutzen

**Designs** ist Ihre Design-Bibliothek – eine Ablage aller gespeicherten
Flechtmuster, aufgebaut wie ein Datei-Explorer mit Ordnern und einer
Tabellenübersicht. Hier **verwalten** Sie Designs: Sie ordnen sie in Ordner ein,
benennen sie um, verschieben oder löschen sie und öffnen ein Design zum
Bearbeiten.

!!! info "Bibliothek verwalten hier – zeichnen im Designer"
    Auf dieser Seite wird **nichts gezeichnet**. Das eigentliche Entwerfen –
    Geflechtsart wählen, Muster malen, Animation ansehen – geschieht im
    [Designer](../designer/index.md). Diese Seite ist die *Bibliothek*, der
    Designer ist das *Zeichenwerkzeug*. Ein Doppelklick auf ein Design öffnet es
    im Designer.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Die Design-Bibliothek mit Ordnerbaum links, Design-Tabelle rechts
    (mit Thumbnails) und der Werkzeugleiste darüber.
    **So erzeugen:** Navigationspunkt **Designs** öffnen, einen Ordner mit
    mehreren Beispiel-Designs auswählen (Demo-Daten „Musterbetrieb").
    **Ziel-Datei:** `assets/screenshots/master-data/designs-bibliothek.png`

Die Seite besteht aus drei Bereichen:

* **Werkzeugleiste** (oben) – Navigation, Suche und die Aktionen (Ordner/Design
  anlegen, Zwischenablage, Umbenennen, Löschen).
* **Ordnerbaum** (links) – die Ordnerstruktur Ihrer Designs. Ein Klick öffnet
  einen Ordner.
* **Design-Tabelle** (rechts) – alle Designs des gewählten Ordners als Tabelle
  mit Vorschaubild.

## Bedienelemente im Detail

### Navigation

In der Werkzeugleiste finden Sie – wie in einem Datei-Explorer – die
Navigationsschaltflächen:

| Schaltfläche | Wirkung |
|---|---|
| **Zurück** | Zum zuvor besuchten Ordner zurück. |
| **Vor** | Wieder vorwärts (nach „Zurück"). |
| **Eine Ebene höher** | In den übergeordneten Ordner wechseln. |
| **Aktualisieren** | Die Ansicht neu einlesen. |

### Suche

Das Suchfeld filtert die Designs. Passt der Suchbegriff, wechselt die Ansicht in
einen flachen Ergebnismodus, der Treffer aus allen Ordnern zeigt.

### Aktionen der Werkzeugleiste

| Schaltfläche | Wirkung |
|---|---|
| **Neuer Ordner** | Legt einen Ordner im aktuellen Pfad an. |
| **Neues Design** | Erstellt ein neues Design im aktuellen Ordner und öffnet es zum Bearbeiten. |
| **Ausschneiden** | Das gewählte Element (Ordner oder Design) für einen Verschiebe-Vorgang merken. |
| **Kopieren** | Das gewählte Element für einen Kopier-Vorgang merken. |
| **Einfügen** | Das ausgeschnittene bzw. kopierte Element in den aktuellen Ordner einfügen. |
| **Umbenennen** | Das gewählte Element umbenennen. |
| **Löschen** | Das gewählte Element löschen (mit Sicherheitsabfrage). |

Ausschneiden/Kopieren und Einfügen bilden zusammen die **Zwischenablage**: Erst
markieren Sie ein Design oder einen Ordner mit **Ausschneiden** (verschieben)
oder **Kopieren** (duplizieren), dann wechseln Sie in den Zielordner und wählen
**Einfügen**.

### Ordnerbaum (links)

Der Ordnerbaum zeigt Ihre Ordnerstruktur. Ein Einfachklick öffnet den Ordner;
dessen Designs erscheinen rechts. Über das **Kontextmenü** (rechte Maustaste auf
einen Ordner) erreichen Sie dieselben Aktionen wie in der Werkzeugleiste –
*Neues Design anlegen…*, *Neuer Ordner…*, *Umbenennen…*, *Ausschneiden*,
*Kopieren*, *Einfügen* und *Löschen…*.

### Design-Tabelle (rechts)

Die Tabelle listet alle Designs des aktuellen Ordners. Sie können sie durch
Klick auf eine Spaltenüberschrift sortieren.

| Spalte | Inhalt |
|---|---|
| **Design** | Vorschaubild (Thumbnail) des Musters. |
| **Produktname** | Name des Designs. |
| **Geflechtsart** | Rundgeflecht, Litzengeflecht, Quadratgeflecht oder Packungsgeflecht. |
| **Bindung** | Besetzung/Bindung (z. B. Normale Besetzung, Tandem, Halbe Besetzung). |
| **Klöppel** | Anzahl der Klöppel. |
| **Winkel** | Flechtwinkel. |
| **Fachung** | Anzahl der zusammengefassten Fäden je Klöppel. |
| **Erstellt** | Erstellungsdatum. |
| **Geändert** | Datum der letzten Änderung. |

Ein **Doppelklick** auf eine Zeile öffnet das Design im
[Designer](../designer/index.md). Das **Kontextmenü** eines Designs bietet
*Umbenennen…*, *Ausschneiden*, *Kopieren* und *Löschen…*.

## Verwandte Seiten

* [Designer](../designer/index.md) – Designs entwerfen und bemustern
* [Design-Parameter](../designer/parameters.md) – Geflechtsart, Besetzung,
  Flechtwinkel und Fachung im Detail
* [Ein Design von Grund auf erstellen](../tasks/design-from-scratch.md) –
  Schritt-für-Schritt-Ablauf
* [Farben](colors.md) – Farbpalette für die Bemusterung
