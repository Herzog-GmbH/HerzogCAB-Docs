# Spulen für einen Flechtauftrag planen

!!! example "Anleitung — am Ende existiert ein gedruckter Spulauftrag mit berechneten Sollwerten, verknüpft mit dem zugehörigen Flechtauftrag"

**Voraussetzungen:**

* Ein gespeicherter [Flechtauftrag](../orders/braiding-order.md) — falls noch
  keiner existiert, folgen Sie zuerst dem Ablauf
  [Vom Kundenauftrag zum Maschinenzettel](order-to-machine-sheet.md).
* [Spulmaschinen](../master-data/winding-machines.md),
  [Spulen (Spulenformate)](../master-data/bobbins.md) und
  [Materialien](../master-data/materials.md) sind in den Stammdaten gepflegt.
* Sie haben die Berechtigung, Aufträge anzulegen.

```mermaid
flowchart LR
  A["Stammdaten prüfen"] --> B["Spulauftrag aus Flechtauftrag erstellen"]
  B --> C["Sollwerte berechnen"]
  C --> D["Speichern"]
  D --> E["Drucken"]
```

## Schritt 1: Spulmaschinen-Stammdaten prüfen

Öffnen Sie *Stammdaten > Spulmaschinen* und prüfen Sie, ob die Spulmaschine,
mit der gespult werden soll, mit ihren Wickeltechnik-Angaben erfasst ist.
Falls nicht, legen Sie sie über **Neu** an — alle Felder erklärt die
Referenzseite [Spulmaschinen](../master-data/winding-machines.md).

Prüfen Sie bei der Gelegenheit auch die
[Spulenformate](../master-data/bobbins.md) (Abmessungen der Spulen) und das
[Material](../master-data/materials.md) — beide werden in den
Spulerei-Berechnungen als Auswahl angeboten.

## Schritt 2: Spulauftrag aus dem Flechtauftrag erstellen

1. Öffnen Sie den Navigationspunkt **Aufträge** (Referenz:
   [Auftragsübersicht](../orders/index.md)).
2. Markieren Sie den Flechtauftrag, für den gespult werden soll.
3. Klicken Sie auf **Spulauftrag erstellen**. Der
   [Spulauftrag-Editor](../orders/winding-order.md) öffnet sich; der neue
   Spulauftrag ist bereits mit dem Flechtauftrag verknüpft, und Sie können
   Sollwerte wie Zielspulenzahl und Länge pro Spule aus dem Flechtauftrag
   übernehmen.
4. Arbeiten Sie die Tabs durch (**Auftrag**, **Kunde**, **Maschine**,
   **Material und Spule**, **Spulerei**) und wählen Sie dabei die
   Spulmaschine aus Schritt 1. Alle Felder — einschließlich der
   Farbaufschlüsselung, die aus der Klöppelbelegung des verknüpften Designs
   vorgeschlagen wird, und der Wickeltechnik-Angaben — erklärt die
   Referenzseite [Spulauftrag-Editor](../orders/winding-order.md).

!!! tip "Spulauftrag ohne Flechtauftrag"
    Einen freien Spulauftrag ohne Verknüpfung legen Sie über
    **Neuer Auftrag** → **Neuer Spulauftrag** an. Die Verknüpfung lässt sich
    im Editor auch nachträglich setzen oder lösen.

## Schritt 3: Sollwerte berechnen

Im Tab **Spulerei** des Spulauftrags sitzen **Rechner-Symbole** direkt an
den Sollwert-Feldern:

* An **Länge pro Spule**: öffnet die Berechnung
  [Spulenkapazität](../calculations/winding/bobbin-capacity.md) — das
  Ergebnis wird als Länge pro Spule übernommen.
* An **Gesamtlänge**: öffnet die Berechnung
  [Spulzeit](../calculations/winding/winding-time.md), mit der Sie die Dauer
  des Spulpostens abschätzen.

Für die weitergehende Planung stehen im Kapitel
[Berechnungen > Spulerei](../calculations/winding/index.md) weitere Rechner
bereit, unter anderem:

* [Materialbedarf](../calculations/winding/material-demand.md) — Gesamtlänge
  und -gewicht inklusive Reserve
* [Spulen aus Liefergebinde](../calculations/winding/from-supplier-spool.md)
  — wie viele Spulen ein Liefergebinde ergibt
* [Anzahl Spulmaschinen](../calculations/winding/number-of-winders.md) — wie
  viele Flechtmaschinen eine Spulmaschine versorgen kann
* [Fadenspannung](../calculations/winding/yarn-tension.md) und
  [Fadengeschwindigkeit](../calculations/winding/line-speed.md) — Richtwerte
  für die Wickeltechnik

Der gemeinsame Aufbau aller Berechnungsseiten ist unter
[So sind Berechnungsseiten aufgebaut](../basics/calc-page-anatomy.md)
beschrieben.

## Schritt 4: Speichern

Klicken Sie auf **Spulauftrag speichern**. Der Spulauftrag erscheint in der
[Auftragsübersicht](../orders/index.md) — dort können Sie die Liste über den
Auftragsart-Filter gezielt auf Spulaufträge einschränken; beim verknüpften
Flechtauftrag wird der Spulauftrag als Verknüpfung angezeigt.

## Schritt 5: Drucken

1. Klicken Sie im Spulauftrag auf **Drucken**.
2. Wählen Sie bei mehreren Vorlagen die gewünschte aus (für Spulaufträge ist
   die Vorlage *Standard Spulauftrag* vorausgewählt).
3. Prüfen Sie die Druckvorschau und starten Sie den Druck.

Der Ausdruck enthält die Spulerei-Sollwerte und die Farbaufschlüsselung für
die Spulerei. Details: [Auftrag drucken](../orders/print.md); eigene Vorlagen:
[Druck-Editor](../print-templates/index.md).

## Ergebnis

* Der Spulauftrag ist gespeichert, mit dem Flechtauftrag verknüpft und
  enthält berechnete Sollwerte (Zielspulenzahl, Länge pro Spule,
  Gesamtlänge).
* Der Begleitschein für die Spulerei ist gedruckt.
* Ist im Spulauftrag eine Spulmaschine gewählt, erscheint er im
  [Maschinenpark](../machine-park/index.md) bei dieser Maschine.

## Wenn etwas nicht klappt

* Der Ausdruck sieht falsch aus oder es passiert nichts →
  [Druckprobleme](../help/print-problems.md)
* Sie können keine weiteren Aufträge anlegen (Testversion) →
  [Testversion und Lizenz-Quoten](../basics/trial-quotas.md)
* Die Spulmaschine fehlt in der Auswahl → Stammdaten prüfen, siehe
  [Spulmaschinen](../master-data/winding-machines.md)
* Weitere Hilfe → [Hilfe-Übersicht](../help/index.md) und
  [Support kontaktieren](../help/support.md)
