# Medienbibliothek (Web-App)

!!! abstract "Referenz — Die Seite „Medienbibliothek" im Benutzermenü der Web-App: hochgeladene Bilder und Dokumente des Kontos"

## Wofür Sie diesen Bereich nutzen

Die Medienbibliothek sammelt alle Dateien des Arbeitsbereichs, die nicht
selbst Daten sind: Maschinenbilder und Box-Ansichten, Dokumente an
Maschinen, Grundrissbilder des Hallenplaners, das Firmenlogo und Bilder
für Druckvorlagen. Was Sie auf einer Maschinenseite oder im Hallenplaner
hochladen, landet automatisch hier; umgekehrt können Sie Dateien vorab
hochladen und dann an den passenden Stellen auswählen. Die Bibliothek
entspricht [Medien](../master-data/media.md) in der Desktop-App.

Sie öffnen die Seite über *Benutzermenü > Medienbibliothek*.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Medienbibliothek der Web-App mit Suchfeld, Artfilter und Dateiliste.
    **So erzeugen:** Web-App lokal (127.0.0.1:5173), Seite `/medien`; automatisch per `python _tools/web_screenshots.py shots nur:medien`
    **Ziel-Datei:** `assets/screenshots/web/medien.png`
    <!-- web-bild ../assets/screenshots/web/medien.png -->

| Element | Bedeutung |
|---|---|
| **Hochladen** | Wählt eine oder mehrere Dateien aus; alternativ ziehen Sie Dateien auf die Liste. |
| Suchfeld | Filtert nach dem Dateinamen. |
| Filter **Alle** / **Bilder** / **PDF** / **Sonstige** | Filtert nach Dateiart; die Trefferzahl steht daneben (*n von m Dateien*). |
| Liste | Name mit Vorschau, **Typ**, **Größe**, **Hochgeladen** (Datum) und Gruppe (z. B. Maschinen, Grundrisse). |
| **Öffnen** | Zeigt die Datei in einem neuen Tab. |
| **Löschen** | Entfernt die Datei nach Sicherheitsabfrage — auch dort, wo sie verwendet wird. |

Zum Hochladen und Löschen brauchen Sie das Recht der jeweiligen Gruppe
(z. B. **Stammdaten bearbeiten** für Maschinenbilder). Gleiche Dateien
werden beim Hochladen nur einmal gespeichert.

## Verwandte Seiten

* [Medien (Desktop-App)](../master-data/media.md)
* [Maschinen (Web-App)](machines.md) — Bilder und Dokumente an Maschinen
* [Hallenplaner (Web-App)](hall-planner.md) — Grundrissbilder
* [Firma (Web-App)](company.md) — Firmenlogo
