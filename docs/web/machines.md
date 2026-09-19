# Maschinen (Web-App)

!!! abstract "Referenz — Das Modul Maschinen der Web-App: Maschinenpark mit Karten- und Listenansicht, Maschinenseite und Herzog-Katalog"

## Wofür Sie diesen Bereich nutzen

Unter **Maschinen** pflegen Sie die Flecht- und Spulmaschinen Ihres Werks —
die Stammdaten, mit denen Aufträge, Designer und Hallenplaner arbeiten. Zwei
Reiter: **Park** (Ihre eigenen Maschinen) und **Katalog** (die Herzog-Modelle
als Vorlage). Die Bedeutung der Maschinendaten steht in der Referenz der
Desktop-App ([Flechtmaschinen](../master-data/braiding-machines.md),
[Spulmaschinen](../master-data/winding-machines.md),
[Maschinenpark](../machine-park/index.md)); hier geht es um die Bedienung
im Browser.

## Reiter „Park"

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Maschinenpark der Web-App in der Kartenansicht mit Filterleiste.
    **So erzeugen:** Web-App lokal (127.0.0.1:5173), Seite `/maschinen`; automatisch per `python _tools/web_screenshots.py shots nur:maschinen`
    **Ziel-Datei:** `assets/screenshots/web/maschinen.png`
    <!-- web-bild ../assets/screenshots/web/maschinen.png -->

| Element | Bedeutung |
|---|---|
| **Neue Flechtmaschine** / **Neue Spulmaschine** | Öffnen die Maschinenseite für eine neue Maschine. |
| **Suchen** | Filtert nach Name, Typ, Seriennummer, Gruppe oder Standort. |
| **Ansicht**: **Karten** / **Liste** | Karten mit Bild und Kennwerten oder eine Tabelle. |
| Filter | **Maschinenart** (Flecht-/Spulmaschinen), **Kategorie**, **Status**, **Gruppe**, **Geflechtsart**, **Standort**; die Trefferzahl steht daneben (*n von m Maschinen*). |
| **Sortierung** | Reihenfolge der Liste. |
| Karte / Zeile | Name, Typ, Kategorie, Standort, Status, Kennwerte (Köpfe, Klöppel, Drehzahl bzw. Spulstellen und UpM) und die Zahl der laufenden **Aufträge**. Ein Klick öffnet die Maschinenseite. |

## Maschinenseite

Die Maschinenseite ist in vier Reiter gegliedert; **Speichern** sitzt oben
rechts, **← Zurück zum Maschinenpark** führt zur Liste. Zum Ändern brauchen
Sie das Recht *Stammdaten bearbeiten* — sonst ist die Seite nur lesbar und
nennt das fehlende Recht.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Maschinenseite der Web-App, Reiter „Allgemein".
    **So erzeugen:** Web-App lokal (127.0.0.1:5173), Seite `/maschinen/<id>`; automatisch per `python _tools/web_screenshots.py shots nur:maschine`
    **Ziel-Datei:** `assets/screenshots/web/maschine.png`
    <!-- web-bild ../assets/screenshots/web/maschine.png -->

| Reiter | Inhalt |
|---|---|
| **Allgemein** | Bild (**Bild hochladen** / **Bild entfernen**), **Modell (Herzog-Katalog)** — ein Katalogmodell belegt Typ, Kategorie, Geflechtsart, Köpfe, Klöppel, Stich, Drehzahl und Bindungen vor —, Maschinendaten (**Name**, **Baureihe**, **Kategorie**, **Maschinentyp**, **Seriennummer**, **Gruppe**, **Standort**, **Baujahr**, **Status**) und die laufenden Aufträge dieser Maschine. |
| **Technik** | Flechtmaschine: **Geflechtsart**, **Einschnitte Endflügelrad**, **Max. Klöppel pro Kopf**, **Köpfe**, **Stich**, **Klöppelart**, **Drehzahl**, **Ölmenge**, **Klöppel gesamt**, **Bindungen**, **Passende Spulen**, **Abmessungen** (Länge, Breite, Höhe — mit **Maße berechnen** überschlägig aus Köpfen, Klöppeln und Stich), Aufwicklung, Abzugsoption und Zubehör. Spulmaschine: **Wickeltechnik** (Spulstellen, Spulendurchmesser, Spullänge, Drehzahl, Verlegung, Wickelart, Geschwindigkeitsführung, Fadenspannung, Steuerung, Antrieb, Verlegeschritt, Verlegebreite, Spulengewicht, **Einrichtzeit je Auftrag**, **Bestückungszeit je Spule**), Zähler, Überwachung, Materialien, automatischer Spulenwechsel (SPA), Fadenhandling, Litzenschlag (HLM). |
| **Bilder & 3D** | **Box-Ansichten**: bis zu fünf Bilder (Vorderseite, Rückansicht, links, rechts, Draufsicht) für die Ersatz-Box in der 3D-Halle; **3D-Modell** (OBJ) nur für interne Konten, **Massstab**, **Drehung X/Y/Z**, **Ausrichtung vorne**. |
| **Dokumente & Notizen** | **Beschreibung**, **Dokumente** (Bedienungsanleitungen, Datenblätter, Abzugstabellen … über **Dokument hinzufügen**, mit **Öffnen** und **Dokument entfernen**) und **Notizen**. |

Bilder und Dokumente landen in der [Medienbibliothek](media.md) des Kontos.
**Löschen** entfernt die Maschine samt Bild, Dokumenten und 3D-Modell — mit
Sicherheitsabfrage.

!!! tip "Spulzeit-Vorbelegung"
    **Einrichtzeit je Auftrag** und **Bestückungszeit je Spule** einer
    Spulmaschine sind die Vorgaben für die Spulzeit-Hochrechnung im
    [Spulauftrag](orders.md); dort lassen sie sich je Auftrag übersteuern.

## Reiter „Katalog"

Der Herzog-Katalog zeigt die aktuellen Maschinenmodelle mit Bild,
**Maschinentyp**, **Kategorie**, **Klöppel gesamt**, **Drehzahl**, **Spule**,
**Bindungen**, **Spezifikationen**, **Zubehör** und **Abzugsoptionen**.
**Suchen** und der Filter **Kategorie** grenzen die Liste ein.

| Schaltfläche | Wirkung |
|---|---|
| **Produktseite** | Öffnet die Produktseite auf herzog-online.com. |
| **Als eigene Maschine anlegen** | Legt eine neue Maschine im Park an, vorbelegt mit den Katalogdaten — Sie ergänzen Seriennummer, Standort und Ihre Einstellungen. |

## Verwandte Seiten

* [Maschinenpark (Desktop-App)](../machine-park/index.md)
* [Flechtmaschinen (Stammdaten)](../master-data/braiding-machines.md) · [Spulmaschinen (Stammdaten)](../master-data/winding-machines.md)
* [Hallenplaner (Web-App)](hall-planner.md) — Maschinen in der Halle platzieren
* [Medienbibliothek (Web-App)](media.md)
