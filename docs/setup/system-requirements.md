# Systemvoraussetzungen

!!! abstract "Referenz — Welche Betriebssysteme, Hardware, Browser und Berechtigungen Herzog CAB benötigt"

## Desktop-App

### Betriebssystem

| Anforderung           | Empfehlung                              |
|-----------------------|-----------------------------------------|
| Betriebssystem        | Windows 10 (64-bit) oder Windows 11; macOS auf Anfrage |
| Architektur           | x64 (Windows)                            |

Die aktuelle Version von Herzog CAB ist auf Windows 10 und 11 getestet.
Sie läuft nur unter 64-Bit-Windows. Ältere Windows-Versionen werden nicht
unterstützt. Für Version 2 gibt es kein fertiges Installationspaket für
macOS. Brauchen Sie Herzog CAB auf einem Mac, fragen Sie beim Vertrieb
nach.

### Hardware

| Komponente            | Mindestens             | Empfohlen                   |
|-----------------------|------------------------|-----------------------------|
| Prozessor             | Dual-Core 2 GHz        | Quad-Core 2,5 GHz oder mehr |
| Arbeitsspeicher       | 4 GB                   | 8 GB                        |
| Freier Festplattenplatz | 500 MB              | 2 GB (Auftragsdaten)        |
| Bildschirmauflösung  | 1280 x 720             | 1920 x 1080 oder höher     |
| Grafik                | OpenGL-fähige Grafik   | Dedizierte Grafikkarte für die 3D-Ansichten (Designer, Hallenplaner) |

### Lizenz

Für den Betrieb von Herzog CAB benötigen Sie eine gültige Lizenz. Seit
Version 2.0 gibt es zwei Wege:

| Lizenzweg | Voraussetzung auf dem Rechner |
|---|---|
| **Kundenkonto** (Regelfall) | Internetverbindung zum Lizenzserver `license.herzog-cab.com` (HTTPS, Port 443) — mindestens beim ersten Start und danach spätestens alle sieben Tage. Keine zusätzliche Software. |
| **CodeMeter** (Bestandskunden mit CmDongle oder CmAct-Lizenz) | Die [Wibu CodeMeter Runtime](codemeter.md) und der Dongle bzw. die aktivierte Software-Lizenz. |

Mehr dazu unter [Kundenkonto und Einladung](account.md) und
[Anmelden und Lizenz beziehen](activate-license.md).

### Berechtigungen

Für die Installation benötigen Sie **Administratorrechte** auf dem
Zielrechner. Die tägliche Nutzung des Programms erfordert keine
Administratorrechte.

### Internet

Eine dauerhafte Internetverbindung ist nicht zwingend erforderlich. Sie wird
benötigt für:

- die **Anmeldung am Kundenkonto** und die stille Verlängerung der
  Lizenz-Miete (beim Kontomodell; ohne Verbindung läuft das Programm bis zu
  sieben Tage, mit Offline-Miete bis zu 30 Tage weiter)
- den **Cloud-Upload** des Arbeitsverzeichnisses in die Web-App, falls
  eingeschaltet (siehe [Lizenz und Cloud](../admin/settings/license.md))
- Updates über das **Herzog CAB Maintenance**-Tool
- die Anmeldung mit **Microsoft Entra ID** (nur bei Dongle-Installationen
  mit eingerichteter Microsoft-Anmeldung)
- Senden von Feedback aus dem Programm

!!! tip "Proxy und Firewall"
    Herzog CAB nutzt die Proxy-Einstellungen von Windows. Muss die Firmen-
    Firewall Ziele freigeben, sind das `license.herzog-cab.com` (Lizenz) und
    `app.herzog-cab.com` (Cloud-Upload und Web-App), jeweils HTTPS.

### Drucker

Falls Sie Berechnungen oder Aufträge ausdrucken möchten, sollte ein
Drucker installiert und unter Windows als Standarddrucker eingerichtet
sein. Ein PDF-Drucker (z. B. *Microsoft Print to PDF*) reicht aus.

## Web-App

Die [Web-App](../web/index.md) unter
[app.herzog-cab.com](https://app.herzog-cab.com) braucht keine Installation.

| Anforderung | Empfehlung |
|---|---|
| Browser | Aktuelle Version von Microsoft Edge, Google Chrome, Firefox oder Safari (jeweils die letzten zwei Hauptversionen). |
| Bildschirm | Ab 1280 px Breite für die volle Oberfläche mit Seitenleiste; ab 768 px (Tablet) angepasstes Layout; am Smartphone eine Leiste mit den wichtigsten Zielen. |
| 3D-Ansichten | Browser mit WebGL 2 (Standard in allen genannten Browsern); für große Geflechte und Hallen ist eine dedizierte Grafikkarte von Vorteil. |
| Internet | Dauerhafte Verbindung — die Web-App arbeitet direkt auf dem Server. |
| Drucken | Über den Druckdialog des Browsers oder als PDF-Datei. |

Ein Platz ist eine **Person, die gerade arbeitet**. Programm und Web-App
teilen sich die Plätze des Abos. Wer beides zugleich nutzt, belegt zwei
Plätze. Wie viele Plätze Ihr Konto hat, sehen Sie im
[Lizenzportal](../portal/licenses.md) und unter
[Abo und Bestellung](../web/subscription.md).

## Nächster Schritt

Klären Sie als Nächstes, welches [Einsatz-Szenario](topology.md) zu Ihrem
Werk passt — das entscheidet mit, wo Ihr Arbeitsverzeichnis liegt und ob
Sie neben der Desktop-App auch die Web-App einsetzen.
