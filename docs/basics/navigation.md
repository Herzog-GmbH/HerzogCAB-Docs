# Navigieren in der App

!!! info "Konzept — Der Navigationsbaum links: alle Einträge, Gruppen und Bedienregeln"

Die Navigation am linken Fensterrand ist der zentrale Weg zu allen Modulen
von Herzog CAB. Diese Seite zeigt den vollständigen Baum und erklärt, wie
Sie ihn bedienen.

## Der Navigationsbaum

```
Home
Favoriten                        (erscheint nur, wenn Favoriten angepinnt sind)
Aufträge
Maschinenpark
Hallenplaner
Designer
Berechnungen
  ├─ Material
  │    ├─ Feinheit
  │    ├─ Umrechnung Feinheit
  │    ├─ Materialdurchmesser über Material
  │    ├─ Materialdurchmesser über Produkt
  │    ├─ Fachung über Produkt
  │    ├─ Materiallänge auf Spule
  │    └─ Spulvolumen
  ├─ Produkt
  │    ├─ Flechtwinkel
  │    ├─ Geflechtsdichte
  │    ├─ Produktlänge
  │    ├─ Produktlänge pro Trommel
  │    ├─ Produktgewicht
  │    ├─ Produktdurchmesser
  │    ├─ Kern-Mantel-Produkt
  │    ├─ Umrechnung Geflechtsdichte
  │    └─ Hohlgeflecht
  │         ├─ Anzahl Klöppel
  │         ├─ Durchmesser
  │         ├─ Materialbreite
  │         └─ Bedeckung
  ├─ Produktion
  │    ├─ Produktionsgeschwindigkeit
  │    ├─ Maschinen Dimensionierung
  │    ├─ Maschinenlaufzeit pro Spule-Satz
  │    └─ Wechselräder Gummibandkette
  └─ Spulerei
       ├─ Spulzeit
       ├─ Fadengeschwindigkeit
       ├─ Fadenspannung
       ├─ Spulenkapazität
       ├─ Spulengewicht
       ├─ Materialbedarf
       ├─ Spulen aus Liefergebinde
       ├─ Restlänge über Gewicht
       └─ Anzahl Spulmaschinen
Stammdaten
  ├─ Designs
  ├─ Farben
  ├─ Flechtmaschinen
  ├─ Grundrisse
  ├─ Kunden
  ├─ Materialien
  ├─ Medien
  ├─ Spulen
  └─ Spulmaschinen
Druck Editor
Parameter Explorer
Systemverwaltung                 (nur mit Verwaltungsrechten sichtbar)
  ├─ Benutzer
  ├─ Rollen
  ├─ Profile
  ├─ Speicherort
  ├─ Firma
  └─ Authentifizierung
```

Die Zielseiten der Einträge finden Sie im Handbuch unter
[Aufträge](../orders/index.md), [Maschinenpark](../machine-park/index.md),
[Hallenplaner](../hall-planner/index.md), [Designer](../designer/index.md),
[Berechnungen](../calculations/index.md),
[Stammdaten](../master-data/index.md),
[Druck-Editor](../print-templates/index.md),
[Parameter-Übersicht](../parameter-overview/index.md) und
[Verwaltung](../admin/index.md).

## So bedienen Sie den Baum

* **Ein Klick genügt.** Ein Klick auf einen Eintrag öffnet die zugehörige
  Seite; ein Klick auf eine Gruppe klappt sie auf bzw. zu. Zusätzlich können
  Sie zum Auf-/Zuklappen den kleinen **Pfeil (Chevron)** vor dem
  Gruppennamen anklicken.
* **Gruppen mit eigener Übersichtsseite.** Die Gruppen **Berechnungen**
  (samt Untergruppen *Material*, *Produkt*, *Hohlgeflecht*, *Produktion*,
  *Spulerei*) und **Stammdaten** öffnen beim Anklicken zusätzlich eine
  Kachel-Übersicht ihres Bereichs.
* **Favoriten anpinnen.** Per **Rechtsklick** auf einen Eintrag pinnen Sie
  ihn unter *Favoriten* ganz oben an — Details unter
  [Favoriten](favorites.md).
* **Navigation einklappen.** Über das Pfeil-Symbol in der Kopfzeile der
  Navigation verkleinern Sie sie zu einer Symbolleiste; über
  *Ansicht > Navigation* blenden Sie sie komplett aus und wieder ein.
  Der Aufbau ist unter [Oberfläche im Überblick](interface.md) beschrieben.

!!! info "Sie sehen weniger Einträge?"
    Die Navigation zeigt nur Bereiche, für die Ihre
    [Rolle](../admin/roles.md) die nötige Berechtigung hat. Fehlt z. B. das
    Recht „Stammdaten ansehen", verschwindet die gesamte Gruppe
    *Stammdaten*. Die **Systemverwaltung** erscheint nur für Benutzer mit
    mindestens einem Verwaltungsrecht — und darin auch nur die Unterpunkte,
    die das eigene Rechte-Set abdeckt.

!!! tip "Gleiche Namen, verschiedene Seiten"
    Drei Paare werden leicht verwechselt:
    **Maschinenpark** zeigt den Betriebszustand aller Maschinen, während
    *Stammdaten > Flechtmaschinen* bzw. *Spulmaschinen* die Maschinendaten
    selbst verwalten. **Designer** ist das Zeichenwerkzeug, *Stammdaten >
    Designs* die Bibliothek aller gespeicherten Designs. **Hallenplaner**
    bestückt Grundrisse mit Maschinen, *Stammdaten > Grundrisse* bearbeitet
    die Gebäudegeometrie.

## Eingaben bleiben in der Sitzung erhalten

Innerhalb einer Sitzung merkt sich Herzog CAB Ihre Eingaben in den
Berechnungen. Sie können auf eine andere Seite wechseln und die Berechnung
später mit allen Werten wieder öffnen. Nach einem Programmneustart sind die
Werte zurückgesetzt. Frühere Berechnungen laden Sie über den
[Verlauf](history.md) erneut.

## Hilfe zur aktuellen Seite

Mit ++f1++ starten Sie die [geführte Tour](guided-tour.md) zur Seite, auf
der Sie sich gerade befinden. Eine vollständige Liste der Tastenkürzel
finden Sie unter [Tastenkürzel](../appendix/keyboard-shortcuts.md).

## Verwandte Seiten

* [Oberfläche im Überblick](interface.md)
* [Favoriten](favorites.md)
* [Startseite (Home)](home.md)
* [Rollen und Berechtigungen](../admin/roles.md)
