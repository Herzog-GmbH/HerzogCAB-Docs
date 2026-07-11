# Eine Produktionshalle aufbauen

!!! example "Anleitung — am Ende haben Sie ein maßstäbliches Abbild Ihrer Halle mit platzierten Maschinen, einer aktiven Ist-Belegung und einer 3D-Kontrollansicht"

**Voraussetzungen:**

* Die Maschinen sind mit ihren Abmessungen in den Stammdaten erfasst
  ([Flechtmaschinen](../master-data/braiding-machines.md),
  [Spulmaschinen](../master-data/winding-machines.md)) — die Kachelgrößen im
  Plan basieren auf diesen Maßen.
* Sie haben die Berechtigung, Grundrisse und Belegungen zu bearbeiten.
* Optional: ein eingescannter Hallenplan als Bilddatei, den Sie als
  Zeichen-Unterlage hinterlegen möchten.

```mermaid
flowchart LR
  A["Grundriss anlegen"] --> B["Geometrie zeichnen"]
  B --> C["Belegung anlegen"]
  C --> D["Maschinen bestücken"]
  D --> E["3D-Kontrolle"]
```

## Schritt 1: Grundriss anlegen

1. Öffnen Sie *Stammdaten > Grundrisse* (Referenz:
   [Grundrisse](../master-data/floor-plans.md)).
2. Klicken Sie auf **+ Neuer Grundriss** und vergeben Sie einen Namen.

## Schritt 2: Hallengeometrie zeichnen

1. Markieren Sie den neuen Grundriss und klicken Sie auf **Bearbeiten** — der
   [Hallenplaner-Editor](../hall-planner/editor.md) öffnet sich im
   Geometrie-Modus.
2. Zeichnen Sie mit den Wand-Werkzeugen zuerst die **Außenwände**, dann die
   **Innenwände**.
3. Legen Sie mit den Flächen-Werkzeugen Funktionsbereiche an (z. B.
   Produktion, Verkehrsweg, Lager).
4. Setzen Sie Bauelemente wie Türen, Tore, Fenster oder Treppen.
5. Speichern Sie den Grundriss.

Alle Werkzeuge, das Eigenschaften-Panel sowie Raster- und Fang-Einstellungen
erklärt die Referenzseite
[Editor — Geometrie & Bestückung](../hall-planner/editor.md).

!!! tip "Vorhandenen Hallenplan als Unterlage nutzen"
    Sie können ein Grundriss-Bild als Hintergrund laden und über zwei
    Referenzpunkte maßstäblich kalibrieren — dann zeichnen Sie die Wände
    einfach nach. Wie das geht, steht auf der
    [Editor-Referenzseite](../hall-planner/editor.md).

## Schritt 3: Belegung anlegen

1. Öffnen Sie den Navigationspunkt **Hallenplaner** (Referenz:
   [Grundriss-/Belegungs-Übersicht](../hall-planner/index.md)).
2. Wählen Sie links Ihren Grundriss aus.
3. Legen Sie in der Belegungsleiste über **+** eine neue Belegung an und
   benennen Sie sie (z. B. „Planung 2026").

Eine *Belegung* ist ein Bestückungs-Szenario: Derselbe Grundriss kann mehrere
Belegungen haben (Ist-Zustand, Umbau-Varianten), zwischen denen Sie wechseln.

## Schritt 4: Maschinen bestücken

1. Klicken Sie auf **Bestücken** — der Editor öffnet sich im
   Bestückungs-Modus.
2. Ziehen Sie Maschinen aus dem Maschinenkatalog (links, mit Suche und
   Typ-Filter) auf die Zeichenfläche.
3. Ordnen Sie die Maschinen an: verschieben, in 90°-Schritten drehen,
   duplizieren. Bei mehreren markierten Maschinen helfen die Funktionen
   **Ausrichten**, **Verteilen** und **Aneinanderreihen** in der
   Auswahl-Werkzeugleiste.
4. Speichern Sie die Belegung.

Alle Platzierungs-Werkzeuge, Kontextmenüs und das Eigenschaften-Panel sind
auf der Referenzseite
[Editor — Geometrie & Bestückung](../hall-planner/editor.md) beschrieben.

## Schritt 5: Ist-Belegung festlegen

Die **erste** Belegung eines Grundrisses wird automatisch zur Ist-Belegung —
dieser Schritt ist also nur nötig, wenn Sie mehrere Belegungen angelegt haben.
Zurück in der [Belegungs-Übersicht](../hall-planner/index.md) markieren Sie
die gewünschte Belegung über ihr Kontextmenü mit **Als Ist-Belegung setzen**.
Die Ist-Belegung ist das Szenario, das den tatsächlichen Hallenzustand
abbildet; die Status-Ampeln der Maschinen zeigen darin den aktuellen
Auftragsstatus aus den [Aufträgen](../orders/index.md).

## Schritt 6: 3D-Kontrolle

Wechseln Sie im Editor in die **3D-Ansicht** (Referenz:
[3D-Hallenansicht](../hall-planner/view-3d.md)):

* Drehen, schwenken und zoomen Sie mit der Maus durch die Halle.
* Senken Sie die Wände bei Bedarf ab, damit der Blick ins Halleninnere frei
  bleibt.
* Prüfen Sie Stellflächen, Wege und Abstände; die Leuchtkugeln über den
  Maschinen zeigen den Auftragsstatus.

## Ergebnis

* Der Grundriss mit Wänden, Flächen und Bauelementen liegt in den
  [Stammdaten](../master-data/floor-plans.md).
* Mindestens eine Belegung mit platzierten Maschinen ist gespeichert und als
  Ist-Belegung markiert.
* Die [3D-Hallenansicht](../hall-planner/view-3d.md) zeigt Ihre Halle
  maßstäblich mit Maschinen und Status.

## Wenn etwas nicht klappt

* Maschinen erscheinen nicht im Katalog → Stammdaten prüfen
  ([Flechtmaschinen](../master-data/braiding-machines.md),
  [Spulmaschinen](../master-data/winding-machines.md))
* Kacheln haben die falsche Größe → Abmessungen in den Maschinen-Stammdaten
  ergänzen
* Schaltflächen sind ausgegraut → Berechtigung fehlt, siehe
  [Rollen und Berechtigungen](../admin/roles.md)
* Weitere Hilfe → [Hilfe-Übersicht](../help/index.md) und
  [Support kontaktieren](../help/support.md)
