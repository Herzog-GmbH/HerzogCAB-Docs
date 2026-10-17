# Bekannte Einschränkungen

!!! info "Konzept — Grenzen von Herzog CAB, die keine Fehler sind, sondern so vorgesehen"

Diese Punkte sind kein Programmfehler, sondern bewusste oder
technisch bedingte Grenzen der aktuellen Version. Wenn Sie eines dieser
Verhalten beobachten, müssen Sie kein Support-Ticket eröffnen.

## Workspace auf einem Netzlaufwerk

Liegt das Arbeitsverzeichnis auf einem Netzlaufwerk und mehrere Arbeitsplätze
greifen darauf zu, kann **immer nur einer** einen Eintrag bearbeiten: Wer
denselben Auftrag, dasselbe Design oder denselben Stammdateneintrag öffnet,
während ein Kollege ihn bearbeitet, sieht ihn nur zum Lesen (Schloss, Band
*In Bearbeitung – nur lesen*), bis der Kollege fertig ist. Das ist gewollt,
siehe [Die Bearbeitungssperre](../basics/multi-user.md#die-bearbeitungssperre).
Bleibt ein Eintrag gesperrt, weil der Kollege nicht erreichbar ist, kann ein
Administrator die Sperre aufheben. Rechner mit Version 2.1.0 oder älter am
selben Arbeitsverzeichnis kennen die Sperre nicht und können Änderungen
anderer überschreiben; aktualisieren Sie deshalb alle Rechner gleichzeitig.

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

## Cloud-Abgleich: der Desktop hat Vorrang

Der Cloud-Abgleich der Desktop-App gleicht in beide Richtungen ab, aber
nicht gleichberechtigt: Er lädt zuerst hoch und holt danach die Änderungen
aus der Web-App. Haben beide Seiten denselben Eintrag geändert, gewinnt der
Desktop. Die Fassung aus der Web-App ist dann nicht weg: Sie steht in der
Web-App unter [Versionen](../web/versions.md) und lässt sich dort
wiederherstellen. Weitere Grenzen:

* In der Web-App gelöschte Dateien (Bilder, Dokumente) bleiben im
  Arbeitsverzeichnis liegen.
* Ein Konto gleicht mit genau einem Arbeitsverzeichnis ab; ein zweites
  Profil lässt sich nur durch Umbinden anschließen.
* Einzelne Dateien über 25 MB werden übersprungen.

Wer nur vom Desktop in die Web-App abgleichen will, schaltet
*Änderungen aus der Webapp ins Arbeitsverzeichnis übernehmen* aus — siehe
[Lizenz und Cloud](../admin/settings/license.md) und
[Daten vom Desktop in die Web-App bringen](../tasks/desktop-to-web.md).

## Web-App: nicht enthaltene Funktionen

Mischdesigns zeigt der Designer der Web-App nur an, anlegen lassen sie sich
dort nicht; einen Zwei-Fenster-Vergleich gibt es nicht. Im Hallenplaner fehlen Kontextmenüs, *Wände
verbinden*, die automatische Flächenerkennung und Wandtexturen. Die
vollständige Gegenüberstellung steht unter [Web-App](../web/index.md).

## Web-Testphase: begrenzte Mengen

In der Testphase der Web-App sind höchstens 2 Designs, 2 Maschinen,
4 Aufträge und 3 Kunden möglich, dazu so viele Benutzer, wie die
Testversion Plätze hat, und 100 Berechnungen je Berechnungsart. Das gilt auch beim ZIP-Import. Details unter
[Testphase und Registrierung](../web/trial.md).

## Verwandte Seiten

* [Lizenzprobleme](license-problems.md)
* [Druckprobleme](print-problems.md)
* [Testversion und Kontingente](../basics/trial-quotas.md)
* [Desktop-App oder Web-App?](../basics/platforms.md)
