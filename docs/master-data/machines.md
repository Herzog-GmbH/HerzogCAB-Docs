# Maschinen

Im Maschinen-Modul pflegen Sie die Flechtmaschinen Ihres Werks. Pro
Maschine speichert Herzog CAB technische Daten, optional Dokumente
(Datenblätter, Betriebsanleitungen) und einen QR-Code für die
Verwendung an der Maschine selbst.

> :material-image-area: *Screenshot: Maschinen-Übersicht (My Machines)*

## Eigenschaften einer Maschine

> :material-alert-circle-outline: **TODO** *Felder anhand des Editors validieren.*

| Feld                | Beschreibung                                                |
|---------------------|-------------------------------------------------------------|
| Bezeichnung         | Eindeutiger Name (z. B. "Halle 2 - HM48")                   |
| Hersteller          | z. B. Herzog GmbH                                            |
| Modell              | Modellbezeichnung                                            |
| Anzahl Klüppel     | Zahl der Spulenträger                                       |
| Flügelteilkreis    | in mm                                                        |
| Höchstdrehzahl     | in U/min                                                     |
| Bemerkung           | Frei-Text                                                    |

## Maschinenpark

Die Liste **Maschinen-Park** zeigt alle erfassten Maschinen. Klicken Sie
einen Eintrag an, um Details und Berechnungen für diese Maschine zu
öffnen.

## Dokumente pro Maschine

Pro Maschine können Sie Dokumente ablegen (z. B. PDFs mit Betriebs-
anleitung, Wartungspläne). Die Dateien werden im Workspace unter

```
<Workspace>\Machines\<MaschinenID>\documents\
```

abgelegt.

> :material-image-area: *Screenshot: Maschinen-Detailseite mit Dokumenten*
