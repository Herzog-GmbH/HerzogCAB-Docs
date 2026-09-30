# Lizenz und Cloud

!!! abstract "Referenz — Tab „Lizenz" des Einstellungen-Dialogs: Lizenzstatus, Konto, Offline-Miete, Abmelden vom Rechner und der Cloud-Upload in die Web-App."

## Wofür Sie diesen Bereich nutzen

Der Tab **Lizenz** (*Datei > Einstellungen*) zeigt, woher Herzog CAB seine
Lizenz bezieht, welches Konto und welcher Benutzer angemeldet sind, welche
Bausteine freigeschaltet sind und wie lange die Miete noch gilt. Hier ziehen
Sie eine Offline-Miete, verlängern die Miete von Hand, melden den Rechner
vom Kundenkonto ab und schalten den automatischen Upload des
Arbeitsverzeichnisses in die [Web-App](../../web/index.md) ein.

!!! info "Nur im Kontomodell"
    Der Tab erscheint, wenn Herzog CAB mit dem [Kundenkonto](../../setup/account.md)
    arbeitet. Bei Dongle- und CmAct-Installationen fehlt er — dort verwaltet
    das CodeMeter Kontrollzentrum die Lizenz.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Tab „Lizenz" mit den drei Karten „Lizenz – Kundenkonto
    (Lizenzserver)", „Konto" und „Cloud (app.herzog-cab.com)"; Konto, Benutzer,
    Edition, Bausteine und Miete gefüllt, Cloud-Schalter aktiv.
    **So erzeugen:** Kunden-Build mit Kontoanmeldung, *Datei > Einstellungen*,
    Tab **Lizenz**.
    **Ziel-Datei:** `assets/screenshots/settings/einstellungen-lizenz.png`

Der Tab besteht aus drei Karten: **Lizenz** (Status), **Konto** (Aktionen)
und **Cloud**.

## Bedienelemente im Detail

### Karte „Lizenz – …"

Der Kartentitel nennt die Quelle der Lizenz: **Kundenkonto (Lizenzserver)**,
**Dongle / CodeMeter-Container** oder *keine gültige Lizenz*.

| Zeile | Bedeutung |
|---|---|
| **Konto** | Name Ihres Kundenkontos (Firma). |
| **Angemeldet als** | Der Benutzer, der gerade im Programm angemeldet ist, mit seiner Rolle (z. B. *Administrator*). |
| **Edition** | Was diese Installation gerade ist: *Vollversion*, *Designer-Version* oder *Testversion* — abgeleitet aus den Bausteinen. |
| **Bausteine** | Alle Bausteine, für die dieser Rechner einen Platz hält, mit lesbaren Namen (z. B. *Vollversion*; Web-Bausteine des Kontos erscheinen zur Auskunft mit, belegen aber keinen Rechnerplatz). |
| **Miete** | *Regelmiete bis <Datum> (noch n Tage), verlängert sich automatisch* — oder *Offline-Miete bis <Datum> (noch n Tage); danach braucht das Programm wieder Verbindung zum Lizenzserver*. Steht hier *keine gültige Bestätigung*, konnte die Miete zuletzt nicht verlängert werden. |
| Roter Hinweis | *Kein freier Platz für: <Baustein>. Bitte im Lizenzportal einen Platz freigeben oder anfragen.* — erscheint, wenn ein Baustein des Kontos für diesen Rechner keinen Platz mehr hatte. |

### Karte „Konto"

| Element | Wirkung |
|---|---|
| **Lizenzportal öffnen** | Öffnet [license.herzog-cab.com](https://license.herzog-cab.com) im Browser — dort verwalten Sie Benutzer, Rechner und Bausteine mit denselben Zugangsdaten. |
| **Ohne Internet:** *für n Tage* + **Offline-Miete ziehen** | Holt vorab eine Miete für **1 bis 30 Tage** (Standard 30). Danach läuft Herzog CAB so lange ohne Verbindung; die Erfolgsmeldung nennt die Zahl der Tage. Ohne Offline-Miete gilt die Regelmiete, die sich beim Start und alle sechs Stunden von selbst verlängert und ohne Verbindung sieben Tage hält. |
| **Miete jetzt verlängern** | Verlängert die Regelmiete sofort von Hand — z. B. kurz bevor Sie den Rechner für ein paar Tage vom Netz nehmen. |
| **Von diesem Rechner abmelden** | Gibt alle Plätze dieses Rechners im Konto frei (mit Sicherheitsabfrage). Beim nächsten Start ist eine neue Anmeldung nötig. Sinnvoll vor einer Neuinstallation, einem Rechnerwechsel oder wenn ein anderer Rechner den Platz braucht. |

!!! tip "Kein freier Platz?"
    Ein Administrator gibt im [Lizenzportal](../../portal/licenses.md) einen
    Rechner frei, der den Platz nicht mehr braucht, oder
    [fragt weitere Plätze an](../../portal/requests.md). Beim nächsten Start
    holt sich Herzog CAB den Platz von selbst.

### Karte „Cloud (app.herzog-cab.com)"

Der **Cloud-Upload** bringt Ihr Arbeitsverzeichnis automatisch in den
Arbeitsbereich Ihres Kontos in der Web-App — Aufträge, Kunden, Maschinen,
Designs, Hallenpläne und Druckvorlagen samt zugehöriger Dateien.

| Element | Wirkung |
|---|---|
| **Arbeitsverzeichnis automatisch in die Cloud hochladen** | Schaltet den Upload ein oder aus. Aktiv beobachtet Herzog CAB das Arbeitsverzeichnis und lädt Änderungen wenige Sekunden nach dem Speichern hoch; zusätzlich läuft alle 15 Minuten ein vollständiger Abgleich. |
| Hinweistext | Erklärt die Richtung: *„… Nur in diese Richtung – der Desktop hat immer recht."* Fehlt die Voraussetzung, steht hier der Grund (siehe unten) mit einem Link ins Lizenzportal. |
| **Stand** | *Aus.*, *Bereit, noch nichts hochgeladen.*, *Arbeitsverzeichnis wird gelesen …*, *Wird hochgeladen …*, *Zuletzt hochgeladen: <Zeit>* oder *Fehler: …*. |
| **Jetzt hochladen** | Stößt sofort einen vollständigen Abgleich an. |

**Voraussetzungen:** Das Konto braucht den Baustein **Herzog CAB Web**
(Abo) — sonst bleibt der Schalter grau und der Hinweis lautet *„Dafür braucht
das Konto den Baustein „Herzog CAB Web" (Abo)."*. Außerdem muss der Rechner
am Kundenkonto angemeldet sein.

!!! info "Einbahnstraße: Desktop → Web-App"
    Der Upload ist bewusst **nur in eine Richtung** gebaut. Was Sie in der
    Web-App ändern, wird **nicht** in das Arbeitsverzeichnis der Desktop-App
    zurückgeschrieben — beim nächsten Abgleich gewinnt der Desktop und
    überschreibt gleiche Einträge in der Cloud. Löschen Sie etwas im
    Desktop, entfernt der Abgleich es auch in der Cloud, aber nur, wenn es
    zuvor vom Desktop hochgeladen wurde. Arbeiten Sie dauerhaft in beiden,
    legen Sie fest, welches System führend ist.

!!! info "Was nicht hochgeladen wird"
    Einzelne Dateien über 25 MB (z. B. große Maschinenbilder oder
    3D-Modelle) werden übersprungen; der Stand nennt sie. Benutzer, Rollen
    und Profile gehören nicht zum Arbeitsverzeichnis — sie kommen in der
    Web-App aus dem Kundenkonto.

Als Alternative zum laufenden Upload gibt es den einmaligen
[ZIP-Import in der Web-App](../../web/import.md). Der Ablauf beider Wege
steht unter [Daten vom Desktop in die Web-App bringen](../../tasks/desktop-to-web.md).

## Verwandte Seiten

* [Kundenkonto und Einladung](../../setup/account.md) — Bausteine, Plätze, Rollen
* [Anmelden und Lizenz beziehen](../../setup/activate-license.md) — Rechner am Konto anmelden
* [Lizenzportal](../../portal/index.md) — Konto verwalten
* [Web-App](../../web/index.md) — Herzog CAB im Browser
* [Lizenzprobleme](../../help/license-problems.md)
