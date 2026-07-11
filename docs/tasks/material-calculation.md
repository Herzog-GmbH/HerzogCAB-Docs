# Material richtig kalkulieren

!!! example "Anleitung — am Ende kennen Sie für Ihr Produkt das passende Material, die Materiallänge je Spule sowie Produktlänge und Produktgewicht"

**Voraussetzungen:**

* Die Materialien sind mit **Dichte** und **Titer** in den
  [Material-Stammdaten](../master-data/materials.md) erfasst — die
  Material-Auswahllisten der Berechnungen füllen sich daraus und übernehmen
  Dichte und Feinheit automatisch.
* Die [Spulenformate](../master-data/bobbins.md) sind mit ihren Abmessungen
  gepflegt.
* Sie kennen den gemeinsamen Aufbau der Berechnungsseiten —
  siehe [So sind Berechnungsseiten aufgebaut](../basics/calc-page-anatomy.md).

```mermaid
flowchart LR
  A["Stammdaten pflegen"] --> B["Feinheit bestimmen"]
  B --> C["Materialdurchmesser & Fachung"]
  C --> D["Materiallänge auf Spule"]
  D --> E["Produktlänge & -gewicht"]
```

Die Schritte bauen aufeinander auf — Sie können aber jederzeit auch nur eine
einzelne Berechnung aus der Kette nutzen. Alle Rechner erreichen Sie über die
Kachel-Übersicht [Berechnungen](../calculations/index.md) oder über die
Navigationsleiste links.

## Schritt 1: Material-Stammdaten pflegen

Prüfen Sie unter *Stammdaten > Materialien*, ob das Material mit Name, Dichte
und Titer angelegt ist; falls nicht, legen Sie es über **Neues Material** an
(Referenz: [Materialien](../master-data/materials.md)). Der Pflegeaufwand
lohnt sich: In allen folgenden Berechnungen genügt dann die Auswahl des
Materials aus der Auswahlliste.

## Schritt 2: Feinheit bestimmen und umrechnen

* Mit der Berechnung
  [Feinheit](../calculations/material/linear-density.md) ermitteln Sie,
  welche Garnstärke für das gewünschte Geflecht benötigt wird.
* Liegen Lieferantenangaben in einer anderen Einheit vor (tex, dtex, den,
  Nr. metrisch, Nr. englisch), nutzen Sie den Live-Umrechner
  [Umrechnung Feinheit](../calculations/material/linear-density-conversion.md).

## Schritt 3: Materialdurchmesser und Fachung ermitteln

Je nachdem, was Sie kennen:

* Sie kennen das **Material** (Feinheit, Dichte) und wollen dessen
  Durchmesser wissen →
  [Materialdurchmesser über Material](../calculations/material/material-diameter.md).
* Sie kennen das **fertige Produkt** (Durchmesser, Klöppelzahl, Flechtwinkel)
  und suchen das passende Garn → 
  [Materialdurchmesser über Produkt](../calculations/material/material-diameter-product.md)
  — diese Berechnung schlägt zusätzlich ein passendes Material aus Ihrer
  Materialdatenbank vor.
* Sie wollen wissen, mit **wie vielen Fäden je Klöppel** das gewählte
  Material eingesetzt werden muss →
  [Fachung über Produkt](../calculations/material/required-ply.md).

## Schritt 4: Materiallänge auf der Spule berechnen

* [Spulvolumen](../calculations/material/bobbin-volume.md) liefert das
  Fassungsvolumen einer Spule aus ihren Abmessungen (bei gepflegten
  [Spulen-Stammdaten](../master-data/bobbins.md) ist es dort bereits
  hinterlegt).
* [Materiallänge auf Spule](../calculations/material/material-length.md)
  berechnet, wie viele Meter Ihres Materials auf die gewählte Spule passen.

## Schritt 5: Produktlänge und Produktgewicht berechnen

* [Produktlänge](../calculations/product/rope-length.md) — wie viele Meter
  fertiges Produkt ein Spulensatz ergibt.
* [Produktgewicht](../calculations/product/rope-weight.md) — das Gewicht des
  gefertigten Geflechtabschnitts.
* Für die Aufwicklung:
  [Produktlänge pro Trommel](../calculations/product/rope-length-on-drum.md).

## Ergebnis

* Sie haben eine durchgängige Kalkulationskette vom Rohmaterial bis zum
  fertigen Produkt.
* Jede abgeschlossene Berechnung liegt im
  [Verlauf](../basics/history.md) und lässt sich von dort mit den damaligen
  Eingaben erneut laden.
* Die Ergebnisse können Sie über [Druckvorlagen](../print-templates/index.md)
  ausgeben und im [Flechtauftrag](../orders/braiding-order.md) verwenden —
  viele dieser Berechnungen sind dort direkt an den Feldern verlinkt.

## Wenn etwas nicht klappt

* Ein Feld ist rot umrandet → die Eingabe fehlt oder ist ungültig; Details
  zur Eingabeprüfung unter
  [So sind Berechnungsseiten aufgebaut](../basics/calc-page-anatomy.md)
* Das Material erscheint nicht in der Auswahlliste → Stammdaten prüfen, siehe
  [Materialien](../master-data/materials.md)
* Das Berechnungs-Kontingent der Testversion ist aufgebraucht →
  [Testversion und Lizenz-Quoten](../basics/trial-quotas.md)
* Weitere Hilfe → [Hilfe-Übersicht](../help/index.md) und
  [Support kontaktieren](../help/support.md)
