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

## Cloud-Upload nur in eine Richtung

Der Cloud-Upload der Desktop-App bringt das Arbeitsverzeichnis in die
Web-App, aber nicht zurück: Änderungen aus der Web-App überschreibt der
nächste Upload. Das ist Absicht — der Desktop ist führend. Wer die Web-App
führend nutzen will, schaltet den Upload aus und holt den Stand per ZIP —
siehe [Daten vom Desktop in die Web-App bringen](../tasks/desktop-to-web.md).

## Web-App: nicht enthaltene Funktionen

Die Web-App enthält keinen Druckvorlagen-Editor, keine Mischdesigns und Texturen im Designer, keinen Zwei-Fenster-Vergleich,
keinen Verlauf und keine Favoriten sowie nicht den Rechner *Flechtwinkel
über Abzug*. Im Hallenplaner fehlen Kontextmenüs, *Wände verbinden*, die
automatische Flächenerkennung und Wandtexturen. Einzelne Dateien über 25 MB
werden vom Cloud-Upload übersprungen. Die vollständige Gegenüberstellung
steht unter [Web-App](../web/index.md).

## Web-Testphase: 25 Einträge je Art

In der Testphase der Web-App sind je Datenart (Aufträge, Designs, Maschinen,
Kunden …) höchstens 25 Einträge möglich — auch beim ZIP-Import. Details unter
[Testphase und Registrierung](../web/trial.md).

## Verwandte Seiten

* [Lizenzprobleme](license-problems.md)
* [Druckprobleme](print-problems.md)
* [Testversion und Kontingente](../basics/trial-quotas.md)
* [Desktop-App oder Web-App?](../basics/platforms.md)
