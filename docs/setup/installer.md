# Herzog CAB installieren

!!! example "Anleitung — Herzog CAB über den Einrichtungsassistenten installiert"

!!! info "Voraussetzung nur bei Dongle-Lizenzen"
    Bestandskunden mit **CmDongle** oder **CmAct-Lizenz** installieren zuerst
    die [CodeMeter-Runtime](codemeter.md), sonst meldet das Programm beim
    ersten Start eine fehlende Lizenz-Komponente. Beim
    [Kundenkonto](account.md) entfällt dieser Schritt.

## Woher bekommen Sie den Installer?

| Bezugsquelle                       | Wann?                                                                 |
|------------------------------------|-----------------------------------------------------------------------|
| **Lizenzportal → Herunterladen** | **Empfohlen** für alle mit Kundenkonto. Melden Sie sich unter [license.herzog-cab.com](https://license.herzog-cab.com) an und klicken Sie auf **Herunterladen** — die Seite zeigt die neueste Version mit Veröffentlichungsdatum, den Neuerungen und je einem Installer für Windows (`Herzog_CAB_Installer_<Version>.exe`) und macOS (`.dmg`). Siehe [Herunterladen](../portal/download.md). |
| **Download vom Herzog-Feedback-Repo** | Ohne Kundenkonto. Öffnen Sie [github.com/Herzog-GmbH/HerzogCAB-Feedback](https://github.com/Herzog-GmbH/HerzogCAB-Feedback) und laden Sie unter *Releases* den aktuellen Installer herunter. Die Produktseite [cab.herzog-online.com](https://cab.herzog-online.com) verlinkt dieselben Dateien. |
| **Mitgelieferter USB-Stick**       | Nur wenn Sie einen **CmDongle** bestellt haben — auf dem mitgelieferten Software-USB-Stick liegt der Installer mit dabei. Praktisch, wenn der Rechner kein Internet hat. |

!!! info "Ein Installer für alle Editionen"
    Seit Version 2.0 gibt es **einen** Installer. Ob Vollversion,
    Designer-Edition oder Testversion läuft, entscheidet die Lizenz —
    die Bausteine im Kundenkonto bzw. der Feature Code des Dongles.

Doppelklicken Sie die heruntergeladene oder vom USB-Stick gestartete
Datei und bestätigen Sie die Windows-Abfrage nach Administratorrechten
mit **Ja**.

---

## Setup-Assistent durchlaufen

Der Einrichtungsassistent führt Sie in sieben Schritten durch die
Installation. Die linke Seitenleiste zeigt jederzeit, wo Sie sich
befinden.

### Schritt 1 - Willkommen

![Willkommen zum Herzog CAB-Einrichtungsassistenten.](../assets/screenshots/installer/1-willkommen.png)

Klicken Sie auf **Weiter**.

### Schritt 2 - Installationsordner

![Installationsordner mit Vorgabe C:\\Program Files\\Herzog\\HerzogCAB.](../assets/screenshots/installer/2-installationsordner.png)

Standardmäßig wird Herzog CAB nach

```
C:\Program Files\Herzog\HerzogCAB
```

installiert. Sie können über **Durchsuchen** einen anderen Ordner
wählen — wir empfehlen aber, die Vorgabe zu belassen, sofern kein
besonderer Grund dagegen spricht.

Klicken Sie auf **Weiter**.

### Schritt 3 - Komponenten auswählen

![Komponentenauswahl mit Herzog Cab Main Component.](../assets/screenshots/installer/3-komponenten.png)

Aktuell gibt es nur eine Komponente: **Herzog Cab Main Component**
(die Hauptanwendung, ca. 82 MB). Lassen Sie das Häkchen gesetzt und
klicken Sie auf **Weiter**.

### Schritt 4 - Lizenzabkommen

![Lizenzabkommen mit Häkchen 'Ich akzeptiere die Lizenzvereinbarung'.](../assets/screenshots/installer/4-lizenzabkommen.png)

Lesen Sie das *License Agreement* der Herzog GmbH, setzen Sie das
Häkchen bei **Ich akzeptiere die Lizenzvereinbarung** und klicken Sie
auf **Weiter**.

### Schritt 5 - Verknüpfungen im Startmenü

![Auswahl des Startmenü-Ordners mit Vorgabe 'Herzog'.](../assets/screenshots/installer/5-startmenue.png)

Der Installer legt eine Verknüpfung im Windows-Startmenü an. Vorgegeben
ist der Ordner-Name **Herzog**. Sie können einen anderen Namen tippen
oder einen vorhandenen Ordner aus der Liste auswählen.

Klicken Sie auf **Weiter**.

### Schritt 6 - Bereit zum Installieren

![Bereit zum Installieren - Bestätigungsseite vor dem Start.](../assets/screenshots/installer/6-bereit.png)

Der Assistent fasst zusammen, was passieren wird (Festplattenbedarf,
Zielordner). Klicken Sie auf **Installieren**.

Der Vorgang dauert je nach Rechner eine bis zwei Minuten. Während der
Installation sehen Sie einen Fortschrittsbalken.

### Schritt 7 - Abschließen

![Den Herzog CAB-Assistent abschließen.](../assets/screenshots/installer/7-abschliessen.png)

Klicken Sie auf **Abschließen**. Herzog CAB ist jetzt installiert und
über das Startmenü unter *Herzog > Herzog CAB* erreichbar.

---

## Nächster Schritt

Starten Sie Herzog CAB und [melden Sie den Rechner am Kundenkonto
an](activate-license.md). Bestandskunden mit Dongle stecken vorher den
CmDongle ein bzw. aktivieren ihre CmAct-Lizenz — ebenfalls auf dieser Seite
beschrieben.
