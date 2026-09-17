# Stammdaten (Web-App)

!!! abstract "Referenz — Das Modul Stammdaten der Web-App: Materialien, Spulen, Farben und Kunden als Reiter mit Liste und Formular"

## Wofür Sie diesen Bereich nutzen

Unter **Stammdaten** pflegen Sie die Grunddaten, auf die Aufträge, Rechner
und Designer zugreifen. Vier Reiter: **Materialien**, **Spulen**, **Farben**,
**Kunden**. Maschinen haben ihr eigenes Modul ([Maschinen](machines.md)),
Grundrisse liegen im [Hallenplaner](hall-planner.md), Bilder und Dokumente in
der [Medienbibliothek](media.md), Designs unter [Designs](designer.md).

Die Bedeutung der Felder entspricht der Desktop-App — siehe
[Materialien](../master-data/materials.md), [Spulen](../master-data/bobbins.md),
[Farben](../master-data/colors.md) und [Kunden](../master-data/customers.md).

## Der Bildschirm im Überblick

![Stammdaten der Web-App, Reiter „Materialien" mit Liste und Suchfeld.](../assets/screenshots/web/stammdaten.png)

Jeder Reiter hat denselben Aufbau:

| Element | Bedeutung |
|---|---|
| **Neu** | Öffnet das leere Formular für einen neuen Eintrag. |
| **Suchen …** | Filtert die Liste live; die Trefferzahl steht daneben (*n Einträge*). |
| Liste | Tabelle mit den wichtigsten Spalten, am Smartphone Karten mit Titel, Unterzeile und zwei Kennwerten. |
| **Bearbeiten** / **Löschen** | Öffnet das Formular bzw. entfernt den Eintrag nach Sicherheitsabfrage (*Das lässt sich nicht rückgängig machen.*). |
| Formular | Öffnet sich als Dialog (**Speichern** / **Abbrechen**); Pflichtfelder sind markiert. Ein Eintrag, den gerade jemand anderes geändert hat, lässt sich erst nach dem Neuladen speichern. |

## Die Reiter im Detail

### Materialien

| Feld | Bedeutung |
|---|---|
| **Name** (Pflicht) | Bezeichnung des Materials. |
| **Hersteller / Marke** | Freitext. |
| **Dichte** (Pflicht) | in g/cm³, drei Nachkommastellen. |
| **Feinheit** und **Einheit der Feinheit** | Titer in tex, dtex, den, Nm oder Ne. |
| **Notiz** | Freitext. |

### Spulen

| Feld | Bedeutung |
|---|---|
| **Name** | Leer lassen: die Anzeige entsteht aus den Maßen. |
| **Aussendurchmesser**, **Kerndurchmesser**, **Wicklungslänge** (Pflicht) | in mm. |
| **Flügelrad-Durchmesser** | in mm. |
| **Volumen** | in cm³; wird aus den Maßen berechnet, wenn leer. |
| **Maschinentypen** | Mehrfachauswahl, für welche Maschinenarten die Spule passt (Rund-, Flach-, Quadrat-, Spiral-, Packungs-, Soutacheflechtmaschine, Spulmaschine). |

### Farben

| Feld | Bedeutung |
|---|---|
| **Name** (Pflicht), **Code** | Bezeichnung und Kennung. |
| **Farbwert** (Pflicht) | Farbwähler. |
| **Palette**, **Pantone**, **Referenzsystem** | Zuordnung zu Palette und Referenzsystem. |
| **Notizen** | Freitext. |

Die Farben stehen im [Designer](designer.md) als Palette zur Verfügung.

### Kunden

| Feld | Bedeutung |
|---|---|
| **Kundennummer**, **Firma** (Pflicht), **Name**, **Ansprechpartner** | Grunddaten. |
| **Strasse**, **PLZ**, **Ort**, **Land** | Anschrift. |
| **Telefon**, **Mobil**, **E-Mail**, **Website** | Kontakt. |
| **Privatkunde** | Kennzeichen. |
| **Notizen** | Freitext. |

## Verwandte Seiten

* [Stammdaten (Desktop-App)](../master-data/index.md)
* [Maschinen (Web-App)](machines.md) · [Medienbibliothek (Web-App)](media.md)
* [Import aus dem Desktop](import.md) — Stammdaten aus der Desktop-App übernehmen
