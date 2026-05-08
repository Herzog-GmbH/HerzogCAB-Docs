# Lizenz aktivieren

Herzog CAB nutzt **Wibu CodeMeter** als Lizenzsystem. Ohne gueltige Lizenz
laesst sich die Anwendung nicht starten.

## Lizenztypen

| Typ            | Artikel  | Umfang                                              |
|----------------|----------|-----------------------------------------------------|
| Vollversion    | 88805    | Alle Funktionen, unbefristet                        |
| Demoversion    | 88806    | Eingeschraenkter Umfang, zeitlich begrenzt          |

Die Lizenz kann auf zwei Arten bereitgestellt werden:

1. **Lokal** - direkt auf dem Rechner als CmActLicense oder ueber einen
   USB-Dongle (CmDongle).
2. **Netzwerk** - ueber einen Wibu-Lizenzserver im Firmennetz.

## Variante A - Lokale Lizenz aktivieren

Sie haben von Herzog GmbH eine **Ticketnummer** erhalten? Dann gehen Sie
so vor:

1. Oeffnen Sie das **CodeMeter Control Center** (Start-Menue > *CodeMeter*).
   Falls es nicht installiert ist, installieren Sie zuerst die
   *CodeMeter User Runtime* von [https://www.wibu.com/de/support/anwendersoftware.html](https://www.wibu.com/de/support/anwendersoftware.html).
2. Klicken Sie auf **Lizenz aktualisieren** > **Weiter**.
3. Waehlen Sie **Lizenzbezug** und klicken Sie auf **Weiter**.
4. Geben Sie die Ticketnummer ein und folgen Sie dem Assistenten.

> :material-image-area: *Screenshot: CodeMeter Control Center*

## Variante B - Netzwerklizenz nutzen

Wenn Ihre Firma einen Wibu-Lizenzserver betreibt, ist meist keine weitere
Konfiguration noetig - Herzog CAB findet den Server automatisch im
Netzwerk. Funktioniert das nicht:

1. Oeffnen Sie das **CodeMeter WebAdmin** (Start-Menue > *CodeMeter* >
   *CodeMeter Control Center* > Schaltflaeche **WebAdmin**).
2. Wechseln Sie nach *Einstellungen > Server-Suchliste* und tragen Sie
   die IP oder den Hostnamen Ihres Lizenzservers ein.

## Lizenzpruefung durch Herzog CAB

Beim Start prueft Herzog CAB, ob eine gueltige Lizenz vorhanden ist:

| Status                      | Verhalten                                       |
|-----------------------------|-------------------------------------------------|
| Lizenz vorhanden, gueltig   | Programm startet normal.                        |
| Demolizenz, gueltig         | Programm startet mit Hinweis auf Restdauer.     |
| Lizenz abgelaufen           | Hinweis-Dialog, Programm startet nicht.         |
| Keine Lizenz gefunden       | Hinweis-Dialog, Programm startet nicht.         |

Wenn die Lizenzpruefung fehlschlaegt, lesen Sie
[Lizenzprobleme](../help/license-problems.md).

## Naechster Schritt

[Erster Programmstart](first-start.md)
