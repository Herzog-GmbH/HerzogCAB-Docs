# Bekannte Einschränkungen

!!! info "Konzept — Grenzen von Herzog CAB, die keine Fehler sind, sondern so vorgesehen"

Diese Punkte sind kein Programmfehler, sondern bewusste oder
technisch bedingte Grenzen der aktuellen Version. Wenn Sie eines dieser
Verhalten beobachten, müssen Sie kein Support-Ticket eröffnen.

## Workspace auf einem Netzlaufwerk

Liegt das Arbeitsverzeichnis auf einem Netzlaufwerk und mehrere Arbeitsplätze
greifen darauf zu: Zwei Rechner können **nicht gleichzeitig denselben
Auftrag** bearbeiten. Die zuletzt gespeicherte Version überschreibt die
vorherige, ohne dass Herzog CAB warnt. Sprechen Sie sich im Team ab, wer
gerade welchen Auftrag bearbeitet.

## Druckvorschau bei sehr großen Vorlagen

Druckvorlagen mit sehr vielen Tabellenzeilen – etwa Klöppeltabellen großer
Maschinen – können den Aufbau der Druckvorschau spürbar verlangsamen. Das
ist unabhängig vom eigentlichen Drucken; nach dem einmaligen Aufbau reagiert
die Vorschau wieder normal.

## Testversion: feste Obergrenzen

In der Testversion sind Anzahl der Maschinen, Aufträge, Kunden, Designs,
Benutzer und Berechnungen je Berechnungsart begrenzt, und die Lizenz läuft
nach Ablauf der Testzeit endgültig aus. Details dazu finden Sie unter
[Testversion und Kontingente](../basics/trial-quotas.md).

## Verwandte Seiten

* [Lizenzprobleme](license-problems.md)
* [Druckprobleme](print-problems.md)
* [Testversion und Kontingente](../basics/trial-quotas.md)
