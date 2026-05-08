# Maschinen

Im Maschinen-Modul pflegen Sie die Flechtmaschinen Ihres Werks. Pro
Maschine speichert Herzog CAB technische Daten, optional Dokumente
(Datenblaetter, Betriebsanleitungen) und einen QR-Code fuer die
Verwendung an der Maschine selbst.

> :material-image-area: *Screenshot: Maschinen-Uebersicht (My Machines)*

## Eigenschaften einer Maschine

> :material-alert-circle-outline: **TODO** *Felder anhand des Editors validieren.*

| Feld                | Beschreibung                                                |
|---------------------|-------------------------------------------------------------|
| Bezeichnung         | Eindeutiger Name (z. B. "Halle 2 - HM48")                   |
| Hersteller          | z. B. Herzog GmbH                                            |
| Modell              | Modellbezeichnung                                            |
| Anzahl Klueppel     | Zahl der Spulentraeger                                       |
| Fluegelteilkreis    | in mm                                                        |
| Hoechstdrehzahl     | in U/min                                                     |
| Bemerkung           | Frei-Text                                                    |

## Maschinenpark

Die Liste **Maschinen-Park** zeigt alle erfassten Maschinen. Klicken Sie
einen Eintrag an, um Details und Berechnungen fuer diese Maschine zu
oeffnen.

## Dokumente pro Maschine

Pro Maschine koennen Sie Dokumente ablegen (z. B. PDFs mit Betriebs-
anleitung, Wartungsplaene). Die Dateien werden im Workspace unter

```
<Workspace>\Machines\<MaschinenID>\documents\
```

abgelegt.

> :material-image-area: *Screenshot: Maschinen-Detailseite mit Dokumenten*
