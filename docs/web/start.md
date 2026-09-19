# Startseite

!!! abstract "Referenz — Die Startseite der Web-App: Kennzahlen des Arbeitsbereichs und Schnellzugriff auf alle Module"

## Wofür Sie diesen Bereich nutzen

Die Startseite begrüßt Sie nach der Anmeldung (*Willkommen, <Name>*) und
zeigt auf einen Blick, wie viel im Arbeitsbereich Ihres Kontos liegt. Von
hier springen Sie in jedes Modul. Sie erreichen die Startseite jederzeit
über **Startseite** in der Seitenleiste, das Herzog-Logo oder **Start** in
der unteren Leiste am Smartphone.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Startseite der Web-App mit den vier Kennzahlen und den Schnellzugriff-Kacheln.
    **So erzeugen:** Web-App lokal (127.0.0.1:5173), Seite `/`; automatisch per `python _tools/web_screenshots.py shots nur:startseite`
    **Ziel-Datei:** `assets/screenshots/web/startseite.png`
    <!-- web-bild ../assets/screenshots/web/startseite.png -->

### Überblick (Kennzahlen)

Vier Kacheln mit der Anzahl der Einträge im Arbeitsbereich — ein Klick
öffnet das jeweilige Modul:

| Kennzahl | Zählt | Ziel |
|---|---|---|
| **Aufträge** | Flecht- und Spulaufträge | [Aufträge](orders.md) |
| **Designs** | gespeicherte Designs | [Designs](designer.md) |
| **Maschinen** | eigene Flecht- und Spulmaschinen | [Maschinen](machines.md) |
| **Kunden** | Kunden in den Stammdaten | [Stammdaten › Kunden](master-data.md) |

Kacheln, für die Ihnen das Recht fehlt, werden nicht angezeigt; mit dem
Baustein *Web Designer* fehlt die Kachel **Aufträge**.

### Schnellzugriff

Kacheln mit kurzer Beschreibung für alle Module — **Aufträge**
(*Flecht- und Spulaufträge*), **Berechnungen** (*32 Rechner in 5 Gruppen*),
**Designer**, **Maschinenpark**, **Hallenplaner**, **Stammdaten** — sowie,
je nach Recht, **Import aus dem Desktop** und **Konto und Benutzer**.

!!! info "Unterschied zur Desktop-App"
    Die Startseite der Desktop-App zeigt zusätzlich Favoriten, den Verlauf
    der Berechnungen, eine Testversions-Kachel und die Update-Karte
    (siehe [Startseite (Home)](../basics/home.md)). In der Web-App gibt es
    keinen Verlauf; Updates entfallen, weil die Web-App immer aktuell ist.

## Verwandte Seiten

* [Oberfläche der Web-App](interface.md)
* [Aufträge](orders.md) · [Berechnungen](calculations.md) · [Designs und Designer](designer.md) · [Maschinen](machines.md) · [Stammdaten](master-data.md) · [Hallenplaner](hall-planner.md)
