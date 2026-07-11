# Oberfläche im Überblick

!!! info "Konzept — Aufbau des Hauptfensters und seiner festen Bereiche"

Nach der Anmeldung startet Herzog CAB mit der [Startseite (Home)](home.md).
Von dort erreichen Sie alle Bereiche über die Navigation links. Diese Seite
erklärt, wie das Hauptfenster aufgebaut ist und welche Bereiche in jedem
Modul gleich bleiben.

![Startseite mit Navigation (links), Begrüßung, Auftrags-Kennzahlen und letzten Aktivitäten.](../assets/screenshots/getting-started/oberflaeche-home.png)

## Aufbau des Hauptfensters

### Menüleiste (oben)

| Menü | Einträge |
|---|---|
| *Datei* | **Einstellungen** (öffnet den [Einstellungen-Dialog](../admin/settings/index.md)), **Drucken…** (++ctrl+p++, druckt die aktuelle Seite über eine [Druckvorlage](../print-templates/index.md)), **Beenden** |
| *Ansicht* | **Navigation** — blendet den Navigationsbereich links ein oder aus |
| *Über* | **Über Qt**, **Über Herzog CAB** (Programm- und Versionsinformationen), **Feedback und Neuigkeiten**, **Updates** (Update-Prüfung, siehe [Updates installieren](../setup/update.md)) |
| *Hilfe* | **Geführte Touren…** — öffnet den Auswahldialog der [geführten Touren](guided-tour.md) |

### Navigation (links)

Der seitliche Navigationsbereich führt zu allen Modulen. In der Kopfzeile
steht der Programmname **Herzog CAB**, daneben ein **Pfeil-Symbol**, mit dem
Sie die Navigation einklappen:

* **Ausgeklappt** zeigt die Navigation den vollständigen Baum mit allen
  Einträgen und Gruppen.
* **Eingeklappt** bleibt eine schmale Symbolleiste stehen. Jedes Symbol
  steht für einen Hauptbereich (der Name erscheint als Kurzhinweis, wenn Sie
  mit der Maus darüber verweilen). Ein Klick auf ein Symbol öffnet die Seite
  direkt; bei Bereichen mit Unterpunkten klappt ein kleines Menü neben dem
  Symbol auf. Ganz unten liegen ein rundes **Benutzer-Symbol** (öffnet
  [Mein Profil](../admin/my-profile.md)) und ein **Zahnrad-Symbol** (öffnet
  die [Einstellungen](../admin/settings/index.md)).

Alle Einträge, ihre Reihenfolge und die aufklappbaren Gruppen sind auf der
Seite [Navigieren in der App](navigation.md) im Detail beschrieben. Dort
lesen Sie auch, wie Sie Einträge als [Favoriten](favorites.md) anpinnen.

### Hauptbereich (Mitte)

Zeigt den Inhalt der gewählten Seite — z. B. eine Stammdaten-Liste, eine
[Berechnung](calc-page-anatomy.md) oder den
[Auftrags-Editor](../orders/braiding-order.md).

### Verlaufs-Leiste (rechts)

Am rechten Fensterrand lässt sich über das Pfeil-Symbol (**Historie öffnen**)
die Leiste **Historie** ein- und ausklappen. Sie listet die in dieser Sitzung
durchgeführten Berechnungen mit Ergebnis und Uhrzeit; ein Klick lädt die
Berechnung mit allen damaligen Eingabewerten erneut. Details unter
[Verlauf der Berechnungen](history.md).

### Profil-Leiste (unten links)

Unten in der Navigation zeigt die Profil-Leiste das **Profilbild**, den
**Anzeigenamen** und die **Rolle** des angemeldeten Benutzers. Ein Klick
darauf öffnet den Dialog **Mein Profil** (Anzeigename, E-Mail und eigenes
Passwort ändern, **Abmelden**) — siehe [Mein Profil](../admin/my-profile.md).

### Statuszeile (ganz unten)

Am unteren Fensterrand zeigt eine schmale Statuszeile den Programmzustand
(im Normalbetrieb „Bereit").

## Meldungen im Programm

Hinweise und Bestätigungen erscheinen als kurze **Einblendung** („Toast"),
z. B. „Auftrag gespeichert" oder die Warnung „Bitte die Eingaben
überprüfen!" bei einer unvollständigen Berechnung. Die Einblendungen
verschwinden nach wenigen Sekunden von selbst und blockieren die Bedienung
nicht.

## Hilfe zur aktuellen Seite

Mit ++f1++ starten Sie die [geführte Tour](guided-tour.md) des Bereichs, in
dem Sie sich gerade befinden; steht der Fokus in der Navigation, startet die
Navigations-Tour. Eine Übersicht aller Tastenkürzel finden Sie unter
[Tastenkürzel](../appendix/keyboard-shortcuts.md).

## Verwandte Seiten

* [Navigieren in der App](navigation.md)
* [Startseite (Home)](home.md)
* [Verlauf der Berechnungen](history.md)
* [Geführte Touren](guided-tour.md)
