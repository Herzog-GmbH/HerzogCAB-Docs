# Oberfläche im Überblick

!!! info "Konzept — Aufbau des Hauptfensters und seiner festen Bereiche"

Nach der Anmeldung startet Herzog CAB mit der [Startseite (Home)](home.md).
Von dort erreichen Sie alle Bereiche über die Navigation links. Diese Seite
erklärt, wie das Hauptfenster aufgebaut ist und welche Bereiche in jedem
Modul gleich bleiben.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Hauptfenster mit eingeklappter Navigation (schmale Symbolleiste links), Titelzeile „Home“ oben links im Inhalt und der Startseite in voller Breite; Menüleiste *Datei · Ansicht · Hilfe*.
    **So erzeugen:** Kunden-Build, Fenster ca. 1600 px breit, Pfeil oben in der Navigation klicken, Maus aus dem Navigationsbereich nehmen, *Home* anzeigen. Ersetzt das bisherige Bild `getting-started/oberflaeche-home.png`.
    **Ziel-Datei:** `assets/screenshots/basics/hauptfenster.png`

## Aufbau des Hauptfensters

Das Hauptfenster lässt sich bis auf **960 × 600 Pixel** verkleinern. Ist es
schmaler als 1500 Pixel, klappt die Navigation von selbst ein (siehe unten),
damit der Inhalt genug Platz behält.

### Menüleiste (oben)

| Menü | Einträge |
|---|---|
| *Datei* | **Einstellungen** (öffnet den [Einstellungen-Dialog](../admin/settings/index.md)), **Drucken…** (++ctrl+p++, druckt die aktuelle Seite über eine [Druckvorlage](../print-templates/index.md)), **Beenden** |
| *Ansicht* | **Navigation** — klappt die Navigation links aus oder ein, wie der Pfeil in ihrer Kopfzeile |
| *Hilfe* | **Handbuch** (++f1++, öffnet die passende Seite dieses Handbuchs im Browser, siehe unten), **Geführte Touren...** (Auswahldialog der [geführten Touren](guided-tour.md)), **Updates** (Update-Prüfung, siehe [Updates installieren](../setup/update.md)), **Feedback und Neuigkeiten**, **Über Herzog CAB** (Programm- und Versionsinformationen), **Über Qt** |

!!! info "Kein Menü „Über“ mehr"
    Bis Version 2.1.0 standen Updates, Feedback und die beiden Über-Dialoge
    in einem eigenen Menü *Über*. Sie liegen jetzt gesammelt im Menü *Hilfe*.

### Navigation (links)

Der seitliche Navigationsbereich führt zu allen Modulen. In der Kopfzeile
steht der Programmname **Herzog CAB**, daneben ein **Pfeil-Symbol**, mit dem
Sie die Navigation ein- und ausklappen:

* **Ausgeklappt** zeigt die Navigation den vollständigen Baum mit allen
  Einträgen und Gruppen. Sie belegt einen festen Streifen am linken Rand,
  der Inhalt rückt daneben.
* **Eingeklappt** bleibt eine schmale Symbolleiste stehen. Jedes Symbol
  steht für einen Hauptbereich (der Name erscheint als Kurzhinweis, wenn Sie
  mit der Maus darüber verweilen). Ein Klick auf ein Symbol öffnet die Seite
  direkt; bei Bereichen mit Unterpunkten klappt ein kleines Menü neben dem
  Symbol auf. Ganz unten liegen ein rundes **Benutzer-Symbol** (öffnet
  [Mein Profil](../admin/my-profile.md)) und ein **Zahnrad-Symbol** (öffnet
  die [Einstellungen](../admin/settings/index.md)).
* **Kurz aufklappen per Maus:** Bleibt der Mauszeiger einen Augenblick über
  der eingeklappten Leiste, klappt die vollständige Navigation auf und
  **schwebt über dem Inhalt** — die Seite daneben verschiebt sich dabei
  nicht. Sobald die Maus die Navigation verlässt, klappt sie wieder ein.

**Automatisch einklappen bei schmalem Fenster:** Unter 1500 Pixel
Fensterbreite klappt Herzog CAB die Navigation selbst ein; ziehen Sie das
Fenster wieder breiter, klappt sie zurück auf. Klappen Sie die Navigation im
schmalen Fenster selbst mit dem Pfeil auf, bleibt sie offen, bis das Fenster
wieder breit genug war. Gemerkt wird nur Ihre eigene Wahl über den Pfeil,
nicht das automatische Einklappen.

Alle Einträge, ihre Reihenfolge und die aufklappbaren Gruppen sind auf der
Seite [Navigieren in der App](navigation.md) im Detail beschrieben. Dort
lesen Sie auch, wie Sie Einträge als [Favoriten](favorites.md) anpinnen.

### Hauptbereich (Mitte)

Zeigt den Inhalt der gewählten Seite — z. B. eine Stammdaten-Liste, eine
[Berechnung](calc-page-anatomy.md) oder den
[Auftrags-Editor](../orders/braiding-order.md). Jede Seite beginnt oben links
mit einer schlichten **Titelzeile** in normaler Schreibweise (z. B.
„Flechtwinkel“), ohne eigene Kopfkarte. Kurze Erklärsätze zu Karten und
Formularen erscheinen als Kurzhinweis, wenn Sie mit der Maus auf die
Kartenüberschrift zeigen.

Reicht die Fensterbreite nicht für alle Bereiche einer Seite, stapeln sich
die Karten untereinander und die Seite lässt sich scrollen; abgeschnitten
wird nichts.

### Verlaufs-Leiste (rechts, nur bei Berechnungen)

Auf den Seiten unter **Berechnungen** — der Berechnungs-Übersicht, ihren
Gruppen und allen Rechnern — lässt sich am rechten Fensterrand über das
Pfeil-Symbol (**Historie öffnen**) die Leiste **Historie** ein- und
ausklappen. Sie listet die in dieser Sitzung durchgeführten Berechnungen mit
Ergebnis und Uhrzeit; ein Klick lädt die Berechnung mit allen damaligen
Eingabewerten erneut. Auf allen anderen Seiten (Aufträge, Stammdaten,
Designer, Katalog …) gibt es die Leiste nicht. Details unter
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

* ++f1++ (oder *Hilfe > Handbuch*) öffnet die **passende Seite dieses
  Handbuchs** im Standardbrowser. Maßgeblich ist die Seite oder der Dialog,
  in dem gerade der Fokus steht, sonst die geöffnete Seite. Gibt es zu
  einer Stelle keine eigene Handbuchseite, öffnet sich die Startseite des
  Handbuchs. Das funktioniert auch in Dialogen. Unter macOS erreichen Sie
  dasselbe mit ++cmd+question++ bzw. ++fn+f1++.
* ++shift+f1++ startet die [geführte Tour](guided-tour.md) des Bereichs,
  in dem Sie sich gerade befinden; steht der Fokus in der Navigation,
  startet die Navigations-Tour.

Eine Übersicht aller Tastenkürzel finden Sie unter
[Tastenkürzel](../appendix/keyboard-shortcuts.md).

## Verwandte Seiten

* [Navigieren in der App](navigation.md)
* [Startseite (Home)](home.md)
* [Verlauf der Berechnungen](history.md)
* [Geführte Touren](guided-tour.md)
