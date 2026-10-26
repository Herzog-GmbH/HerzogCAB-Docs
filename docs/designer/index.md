# Designer

!!! abstract "Referenz — der Design-Editor: Flechtdesigns entwerfen, einfärben, animieren, vergleichen, speichern und drucken."

## Wofür Sie diesen Bereich nutzen

Im **Designer** entwerfen Sie Flechtdesigns: Sie wählen die Geflechtsart und die
Geflechtsbindung, legen Klöppelzahl, Flechtwinkel und Fachung fest und färben
dann die einzelnen Klöppel ein. Das Flechtbild entsteht dabei live — so sehen Sie
sofort, welches Muster (Spirale, Ring, Karo …) aus Ihrer Farbbelegung wird.
Fertige Designs speichern Sie in der [Designbibliothek](../master-data/designs.md),
verwenden sie in [Flechtaufträgen](../orders/braiding-order.md) und drucken sie
als Maschinenbelegblatt.

## In diesem Kapitel

<div class="grid cards" markdown>

- :material-tune: **Geflechtsart und Parameter**

    ---

    Rund-, Litzen-, Quadrat-, Spiral-, Packungs- und Soutachegeflecht;
    Bindung, Klöppelzahl, Flechtwinkel, Fachung, Material-Ø und Bedeckung.

    [:octicons-arrow-right-24: Geflechtsart und Parameter](parameters.md)

- :material-palette: **Färben und Drehung**

    ---

    Malmodus, Farbbibliothek, Benutzerfarben, Farbwähler, Fachungsfarben,
    Drehung je Klöppel und Seitenfilter.

    [:octicons-arrow-right-24: Färben und Drehung](painting.md)

- :material-play-circle-outline: **Besetzung und Gangbahn-Animation**

    ---

    Die Maschinen-Draufsicht mit Flügelrädern und den animierten
    Gangbahnen.

    [:octicons-arrow-right-24: Besetzung und Animation](animation.md)

- :material-rotate-3d: **Ansichten und 3D-Ansicht**

    ---

    Volle und halbe Abwicklung, die drehbaren Projektionen Zylinder und
    Vierkant, das echte 3D-Modell des Geflechts und das Fenster Darstellung.

    [:octicons-arrow-right-24: Ansichten und 3D-Ansicht](view-3d.md)

- :material-content-save-outline: **Speichern und Drucken**

    ---

    Speichern mit Zielordner-Auswahl, Speichern unter neuem Namen, Drucken mit
    Vorlagenauswahl und Vorschau.

    [:octicons-arrow-right-24: Speichern und Drucken](save-print.md)

</div>

## Der Bildschirm im Überblick

### Startansicht (noch kein Design geöffnet)

Solange kein Design geöffnet ist, zeigt der Designer eine Startansicht mit
Kurzanleitung und Ihren zuletzt verwendeten Designs:

![Designer-Startansicht mit Kurzanleitung links und der Liste „Zuletzt bearbeitet oder gespeichert" rechts.](../assets/screenshots/design/designer-start.png)

* **Ein Design öffnen** (links) — die beiden Wege zum Start: **Design
  erstellen** (++ctrl+n++) legt ein neues, leeres Design an, **Design laden**
  (++ctrl+o++) öffnet ein gespeichertes.
* **Zuletzt bearbeitet oder gespeichert** (rechts) — Ihre fünf zuletzt
  geänderten Designs, jeweils mit Vorschaubild, Namen, Ordner und dem
  Zeitstempel der letzten Bearbeitung bzw. Speicherung. Ein **Klick**
  öffnet das Design direkt. Passt seine Klöppelzahl nicht zu Geflechtsart
  und Bindung, fragt der Designer nach (*„…“ hat n Klöppel. Für diese
  Geflechtsart und Bindung sind nur m Klöppel möglich …*) und bietet
  **Mit m Klöppeln öffnen** an; das gespeicherte Design ändert sich erst,
  wenn Sie speichern.

Solange kein Design geöffnet ist, ist die Werkzeugleiste gesperrt; nur
**Neu** und **Laden** sind bedienbar.

### Bearbeitungsansicht

Sobald ein Design geöffnet ist, erscheint die Bearbeitungsansicht. Sie besteht
aus fünf Bereichen:

![Designer mit Rundgeflecht: Werkzeugleiste, links Parameter und Besetzungsübersicht, Mitte Klöppeltabelle, rechts Flechtbild](../assets/screenshots/designer/designer-bearbeitungsansicht.png)

| Bereich | Inhalt |
|---|---|
| **Werkzeugleiste** (oben) | Modus-Umschalter, Seitenfilter, Rückgängig/Wiederherstellen, Ansichts-Schalter, **Darstellung**, **Farbpalette** und der Pinsel **Drehung**. |
| **Dokument-Kopfzeile** (je Design-Fenster) | Zusammenfassung des Designs und die Aktionen **Drucken**, **Speichern**, **Speichern unter neuem Namen**, **Ansicht schließen**. |
| **Parameter-Panel** (links) | Designname, [Geflechtsart und Parameter](parameters.md) mit [Material-Ø, Bedeckung und Geflechts-Ø](parameters.md#material-bedeckung-geflechts) unter **Fachung** sowie darunter die [Besetzungsübersicht](animation.md). |
| **Klöppeltabelle** (Mitte) | Alle Klöppelpositionen mit ihrer aktuellen Farbe — hier können Sie auch direkt färben. |
| **Vorschau** (rechts) | Das Flechtbild, das aus der aktuellen Farbbelegung entsteht, mit eigenen Zoom-Schaltflächen; in der 3D-Ansicht das räumliche Modell. |

## Bedienelemente im Detail

### Werkzeugleiste

| Schaltfläche | Funktion |
|---|---|
| **Neu** (++ctrl+n++) | Öffnet ein neues Designfenster mit den Vorgaben aus [Einstellungen > Design](../admin/settings/legacy-import.md) (Standard: Rundgeflecht, 16 Klöppel, 45°, Normale Besetzung 1-1). Ist bereits ein Design geöffnet, entsteht ein zweites Fenster daneben (siehe unten). |
| **Laden** (++ctrl+o++) | Wechselt in die [Designbibliothek](../master-data/designs.md), wo Sie ein gespeichertes Design auswählen und öffnen. |
| **Färben** | Malmodus: Klicks im Flechtbild oder in der Klöppeltabelle färben Klöppel mit der aktiven Farbe ein — siehe [Färben und Drehung](painting.md). Ist der Pinsel **Drehung** gewählt, schaltet **Färben** zurück aufs Färben. |
| **Bewegen** | Verschiebemodus: mit gedrückter linker Maustaste verschieben Sie die Ansicht, ohne zu färben. |
| **Linkslauf** / **Rechtslauf** | Seitenfilter für Farbe und Drehung: legt fest, welche Laufrichtung ein Klick trifft. Nur bei Rund- und Quadratgeflecht sichtbar (zwei Läufe). |
| **Alle Garne** / **Garn N** | Garn-Wähler, nur ab Fachung 2: legt fest, welches Garn eines Klöppels ein Klick färbt — siehe [Fachungsfarben](painting.md#fachungsfarben-farbe-je-garn). |
| **Zurück** (++ctrl+z++) / **Vor** (++ctrl+y++) | Macht den letzten Schritt (Farbe oder Drehung) rückgängig bzw. stellt ihn wieder her. |
| **Voll** bzw. **Flechtbild** / **Halb** / **Zylinder** bzw. **Vierkant** / **3D** | Die Ansichts-Schalter: flache Abwicklung, halbe Abwicklung, drehbare Projektion und das echte 3D-Modell — welche erscheinen, hängt von der Geflechtsart ab, siehe [Ansichten und 3D-Ansicht](view-3d.md). |
| **Darstellung** | Öffnet das Fenster **Darstellung**: **Fadenstruktur** und **Labels** für die Zeichenansichten, **Werkstoff**, **Einfache Darstellung**, **Form** und **Ausrichtung** für die 3D-Ansicht. Gilt für alle Designfenster — siehe [Fenster „Darstellung“](view-3d.md#fenster-darstellung). |
| **Farbpalette** | Öffnet die Farbpalette mit aktiver Farbe, Bibliotheksfarben und Benutzerfarben — siehe [Färben und Drehung](painting.md). |
| **Drehung** | Pinsel für die Drehung der Garne: S, Z oder gerade, auf Wunsch mit TPM. Die Schaltfläche trägt die gewählte Drehung im Namen, z. B. **Drehung S 120** — siehe [Drehung](painting.md#drehung-s-z-oder-gerade). |

### Dokument-Kopfzeile

Jedes Design-Fenster hat eine eigene Kopfzeile:

* **Zusammenfassung** (links) — Designname und die wichtigsten Einstellungen in
  einer Zeile, z. B. Geflechtsart, Bindung, Klöppelzahl, Flechtwinkel und
  Fachung. Bei Quadrat- und Packungsgeflecht stehen zusätzlich die
  Flügelrad-Anordnung und (beim Packungsgeflecht) die Zahl der Gangbahnen dabei.
* **Drucken** — startet den [Druck mit Vorlagenauswahl](save-print.md).
* **Speichern** / **Speichern unter neuem Namen** — legt das Design in der
  [Designbibliothek](../master-data/designs.md) ab, siehe
  [Speichern und Drucken](save-print.md).
* **Ansicht schließen** (✕) — schließt dieses Design-Fenster. Bei
  ungespeicherten Änderungen fragt die App vorher nach — oder speichert
  automatisch, wenn das unter [Einstellungen > Design](../admin/settings/legacy-import.md)
  so eingestellt ist.

### Zwei Designs nebeneinander vergleichen

Der Designer kann **zwei Design-Fenster gleichzeitig** anzeigen — praktisch, um
zwei Farbvarianten direkt zu vergleichen:

1. Öffnen Sie das erste Design.
2. Klicken Sie auf **Neu** — ein zweites, leeres Designfenster erscheint daneben
   und ist aktiv.
3. Klicken Sie auf **Laden** und wählen Sie das zweite Design — es wird in das
   aktive Fenster geladen.

Das **aktive Fenster** erkennen Sie an der Hervorhebung; ein Klick in ein
Fenster aktiviert es. Werkzeugleiste und Parameter-Panel wirken immer auf das
aktive Fenster. Mehr als zwei Fenster sind bewusst nicht möglich — beim Versuch
erscheint der Hinweis *„Es können maximal zwei Designs gleichzeitig geöffnet
sein"*. Schließen Sie dann zuerst eines über das ✕ in dessen Kopfzeile.

### Zoomen und Verschieben

| Aktion | Bedienung |
|---|---|
| Zoomen | **Mausrad** über dem Flechtbild — gezoomt wird an der Mausposition. |
| Zoomen (Schaltflächen) | **Hineinzoomen** / **Herauszoomen** oben rechts an der Vorschau-Karte. |
| Ansicht einpassen | **Ansicht einpassen** (Vollbild-Symbol) an der Vorschau-Karte — das Flechtbild wird wieder komplett eingepasst. Bei **Zylinder** und **Vierkant** führt es auf den Startausschnitt zurück, in dem der Körper die Vorschau füllt. |
| Verschieben | **Rechte Maustaste** gedrückt halten und ziehen — funktioniert jederzeit, auch im Malmodus. |
| Verschieben (Modus) | Werkzeug **Bewegen** wählen und mit der **linken Maustaste** ziehen. In **Zylinder** und **Vierkant** dreht die linke Maustaste auch hier den Körper; verschieben Sie dort mit der rechten Maustaste. |
| Drehen (**Zylinder**, **Vierkant**) | **Linke Maustaste** gedrückt halten und waagerecht ziehen — siehe [Zylinder und Vierkant drehen](view-3d.md#zylinder-und-vierkant-drehen). |

Die [Besetzungsübersicht](animation.md) hat eine eigene, unabhängige
Zoom-und-Verschieben-Bedienung.

### Geführte Tour

Für den Einstieg bietet der Designer eine eingebaute [geführte Tour](../basics/guided-tour.md):
Sie startet in der Startansicht, legt auf Wunsch ein neues Design an und erklärt
anschließend Schritt für Schritt alle Werkzeuge und Bereiche der
Bearbeitungsansicht.

## Verwandte Seiten

* [Ein Design von Grund auf entwerfen](../tasks/design-from-scratch.md) — der Workflow von leerem Design bis zum Druck
* [Designbibliothek](../master-data/designs.md) — gespeicherte Designs verwalten
* [Farben (Stammdaten)](../master-data/colors.md) — Farbpaletten für den Designer pflegen
* [Flechtauftrag](../orders/braiding-order.md) — Designs im Auftrag verwenden
* [Design (Einstellungen)](../admin/settings/legacy-import.md) — Vorgaben, Ansicht, Animation, Speichern
* [Designs und Designer in der Web-App](../web/designer.md)
