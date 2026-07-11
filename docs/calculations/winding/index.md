# Spulerei

Die **Spulerei** bereitet das Material für die Flechterei vor: Garn, Draht
oder Litze wird von einem Liefergebinde auf Spulen umgespult, die anschließend
in die Klöppel der Flechtmaschine eingesetzt werden. Die neun Berechnungen
dieser Gruppe unterstützen genau diesen Schritt — von der Spulzeit über die
Spulenkapazität bis zum Materialbedarf für einen ganzen Spulposten.

## Die Spulerei-Berechnungen

<div class="grid cards" markdown>

- :material-timer-outline: **Spulzeit**

    ---

    Dauer für eine einzelne Spule und für einen ganzen Posten Spulen.

    [:octicons-arrow-right-24: Öffnen](winding-time.md)

- :material-speedometer: **Fadengeschwindigkeit**

    ---

    Umrechnung zwischen Spindeldrehzahl und Fadengeschwindigkeit über den Wickeldurchmesser.

    [:octicons-arrow-right-24: Öffnen](line-speed.md)

- :material-tune-vertical: **Fadenspannung**

    ---

    Sinnvolle Spannung beim Bespulen, abgeleitet aus Feinheit und Spannungsfaktor.

    [:octicons-arrow-right-24: Öffnen](yarn-tension.md)

- :material-database-outline: **Spulenkapazität**

    ---

    Wie viele Meter Material eine gewählte Spule fasst.

    [:octicons-arrow-right-24: Öffnen](bobbin-capacity.md)

- :material-weight-kilogram: **Spulengewicht**

    ---

    Netto- und Bruttogewicht einer bespulten Spule.

    [:octicons-arrow-right-24: Öffnen](bobbin-weight.md)

- :material-package-variant-closed: **Materialbedarf**

    ---

    Gesamter Materialbedarf für einen Spulposten inklusive Verschnitt/Reserve.

    [:octicons-arrow-right-24: Öffnen](material-demand.md)

- :material-swap-horizontal: **Spulen aus Liefergebinde**

    ---

    Wie viele Spulen sich aus einem Liefergebinde bespulen lassen.

    [:octicons-arrow-right-24: Öffnen](from-supplier-spool.md)

- :material-ruler: **Restlänge über Gewicht**

    ---

    Restliche Materiallänge einer angebrochenen Spule, zurückgerechnet aus dem Gewicht.

    [:octicons-arrow-right-24: Öffnen](residual-length.md)

- :material-counter: **Anzahl Spulmaschinen**

    ---

    Wie viele Flechtmaschinen eine Spulmaschine im Schichtbetrieb versorgen kann.

    [:octicons-arrow-right-24: Öffnen](number-of-winders.md)

</div>

## Gemeinsamer Aufbau

Alle Spulerei-Berechnungen folgen demselben Baukasten wie die übrigen
Berechnungen in Herzog CAB: Eingabe-Karte, Ergebnis-Kacheln, Schaltflächen
**Berechnen**/**Löschen** sowie eine Verlaufs-Seitenleiste. Der gemeinsame
Aufbau ist unter
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md)
erklärt.

Sie erreichen die Spulerei-Berechnungen über die eigene Kachel-Übersicht
**Spulerei** sowie über die Navigationsgruppe *Berechnungen > Spulerei* in
der linken Navigationsleiste.

## Verwandte Bereiche

* [Spulmaschinen](../../master-data/winding-machines.md) — Stammdaten der
  Spulmaschinen (Baureihen SP, SPA, HLM)
* [Spulen](../../master-data/bobbins.md) — Spulenformate mit ihren
  Abmessungen
* [Spulauftrag](../../orders/winding-order.md) — eigene Auftragsart für die
  Spulerei
* [Berechnungen](../index.md) — Übersicht aller Berechnungsgruppen
