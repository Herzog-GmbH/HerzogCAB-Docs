# Lizenz und Cloud

!!! abstract "Referenz — Tab „Lizenz" des Einstellungen-Dialogs: Lizenzstatus, Konto, Offline-Miete, Abmelden vom Rechner und der Cloud-Abgleich mit der Web-App."

## Wofür Sie diesen Bereich nutzen

Der Tab **Lizenz** (*Datei > Einstellungen*) zeigt, woher Herzog CAB seine
Lizenz bezieht, welches Konto und welcher Benutzer angemeldet sind, welche
Bausteine freigeschaltet sind, wie viele Plätze belegt sind und wie lange
die Miete noch gilt. Hier ziehen
Sie eine Offline-Miete, verlängern die Miete von Hand, melden den Rechner
vom Kundenkonto ab und schalten den automatischen Abgleich des
Arbeitsverzeichnisses mit der [Web-App](../../web/index.md) ein.

!!! info "Nur im Kontomodell"
    Der Tab erscheint, wenn Herzog CAB mit dem [Kundenkonto](../../setup/account.md)
    arbeitet. Bei Dongle- und CmAct-Installationen fehlt er — dort verwaltet
    das CodeMeter Kontrollzentrum die Lizenz.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Tab „Lizenz" mit den drei Karten „Lizenz – Kundenkonto
    (Lizenzserver)", „Konto" und „Cloud (app.herzog-cab.com)"; Konto, Benutzer,
    Edition, Bausteine, Miete und Plätze gefüllt, Cloud-Schalter aktiv.
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
| **Bausteine** | Die Bausteine dieses Rechners mit lesbaren Namen, zum Beispiel *Vollversion (Programm und Web)*. Ein Abo gilt für Programm und Web-App zusammen, als **ein** Kontingent; darum steht es als ein Eintrag da. |
| **Miete** | Normalerweise *Platz belegt, solange Herzog CAB läuft; beim Beenden wird er frei. Ohne Verbindung gültig bis &lt;Datum&gt; (noch n Tage).* Mit Offline-Miete: *Offline-Miete bis &lt;Datum&gt; (noch n Tage); danach braucht das Programm wieder Verbindung zum Lizenzserver.* Steht hier *keine gültige Bestätigung*, konnte die Miete zuletzt nicht verlängert werden. |
| **Plätze** | *n von m belegt (Programm und Herzog CAB Web zusammen)*. So viele Plätze des Abos sind gerade belegt, im Programm und im Browser. |
| Roter Hinweis | *Kein freier Platz für: &lt;Baustein&gt;. Bitte im Lizenzportal einen Platz freigeben oder anfragen.* Darunter steht, wer gerade arbeitet. Erscheint, wenn ein Baustein des Kontos für diesen Rechner keinen Platz mehr hatte. |

### Karte „Konto"

| Element | Wirkung |
|---|---|
| **Lizenzportal öffnen** | Öffnet [license.herzog-cab.com](https://license.herzog-cab.com) im Browser — dort verwalten Sie Benutzer, Rechner und Bausteine mit denselben Zugangsdaten. |
| **Ohne Internet:** *für n Tage* + **Offline-Miete ziehen** | Holt vorab eine Miete für **1 bis 30 Tage** (Standard 30). Danach läuft Herzog CAB so lange ohne Verbindung. Der Platz bleibt so lange belegt, auch wenn das Programm geschlossen ist. Die Erfolgsmeldung nennt die Zahl der Tage. Ohne Offline-Miete hält das Programm seinen Platz nur, solange es läuft, und arbeitet ohne Verbindung bis zu sieben Tage weiter. |
| **Miete jetzt verlängern** | Verlängert die Miete sofort von Hand, zum Beispiel kurz bevor Sie den Rechner für ein paar Tage vom Netz nehmen. |
| **Von diesem Rechner abmelden** | Meldet den Rechner vom Kundenkonto ab und gibt seine Plätze frei, nach der Rückfrage *Vom Kundenkonto abmelden?* Beim nächsten Start ist eine neue Anmeldung nötig. Sinnvoll vor einer Neuinstallation, einem Rechnerwechsel oder um eine Offline-Miete vorzeitig zu beenden. |

!!! tip "Alle Plätze belegt?"
    Ein Platz wird frei, sobald jemand Herzog CAB beendet oder sich in der
    Web-App abmeldet, spätestens 15 Minuten nach der letzten Aktivität. Wer
    gerade arbeitet, zeigt das [Lizenzportal](../../portal/licenses.md#wer-gerade-arbeitet).
    Ein Administrator kann dort auch einen Rechner freigeben oder unter
    [Abo und Bestellung](../../web/subscription.md) weitere Plätze
    bestellen. Die Meldungen im Einzelnen stehen unter
    [Lizenzprobleme](../../help/license-problems.md).

### Karte „Cloud (app.herzog-cab.com)"

Der **Cloud-Abgleich** bringt Ihr Arbeitsverzeichnis automatisch in den
Arbeitsbereich Ihres Kontos in der Web-App und holt — sofern
eingeschaltet — zurück, was dort geändert wurde.

| Element | Wirkung |
|---|---|
| **Arbeitsverzeichnis automatisch mit der Cloud abgleichen** | Schaltet den Abgleich ein oder aus; der Schalter gilt für das aktive Profil. Aktiv beobachtet Herzog CAB das Arbeitsverzeichnis und gleicht Änderungen kurz nach dem Speichern ab; zusätzlich läuft alle 15 Minuten ein Abgleich. |
| **Änderungen aus der Webapp ins Arbeitsverzeichnis übernehmen** | Nur bedienbar, wenn der Abgleich an ist; voreingestellt an. Holt nach jedem Hochladen, was in der Web-App angelegt, geändert oder gelöscht wurde (siehe unten). Aus: Der Abgleich läuft nur vom Desktop in die Web-App. |
| Hinweistext | Fasst zusammen, was in welche Richtung geht. Fehlt eine Voraussetzung, steht hier der Grund (siehe unten) mit dem Link **Lizenzportal öffnen**. |
| **In der Cloud:** | Welches Arbeitsverzeichnis das Konto in der Cloud hat: *Noch kein Arbeitsverzeichnis – der erste Abgleich legt es fest.*, *Dieses Arbeitsverzeichnis („…").* oder *„…" – ein anderes Arbeitsverzeichnis (Rechner …, seit …).* |
| **Stand** | *Aus.*, *Bereit, noch nicht abgeglichen.*, *Arbeitsverzeichnis wird gelesen …*, *Wird abgeglichen …*, *Zuletzt abgeglichen: &lt;Zeit&gt;* (mit der Zahl der Einträge und Dateien) oder *Fehler: …*. |
| **Jetzt abgleichen** | Stößt sofort einen Abgleich an. |
| **Stattdessen dieses Arbeitsverzeichnis verwenden …** | Nur sichtbar, wenn das Konto schon mit einem anderen Arbeitsverzeichnis abgleicht. Bindet die Cloud nach Rückfrage auf dieses Arbeitsverzeichnis um; was das andere hochgeladen hat, bleibt in der Web-App, und das andere gleicht danach nicht mehr ab. Umbinden dürfen nur Benutzer mit dem Recht *Arbeitsbereich verwalten*. |

**Voraussetzungen:** Das Konto braucht ein Abo, das die Web-App umfasst.
Das sind das Jahresabo und die Testversion. Eine Lizenz ohne Enddatum
(Lebenszeit) reicht nicht. Fehlt das Abo, bleibt der Schalter grau, und der
Hinweis lautet *„Dafür braucht das Konto den Baustein „Herzog CAB Web" (Abo).
Er lässt sich im Lizenzportal bestellen."* Außerdem muss der Rechner am
Kundenkonto angemeldet sein.

#### Was in welche Richtung geht

| Richtung | Was |
|---|---|
| Desktop → Web-App | Aufträge, Kunden, Farben, Materialien, Spulen, Trommeln, Maschinen, Designs samt Ordnern, Hallenpläne (Grundrisse und Belegungen) und Druckvorlagen, dazu die Dateien: Vorschaubilder, Medien, Maschinenbilder und -dokumente, Bilder des Hallenplaners und der Druckvorlagen. |
| Web-App → Desktop (Schalter *Änderungen aus der Webapp …* an) | Designs, Aufträge, Kunden, Farben, Materialien, Spulen, Maschinen und Hallenpläne; ab Version 2.1.0 auch Trommeln und Druckvorlagen. Außerdem Dateien, die in der Web-App hochgeladen wurden (Vorschauen, Bilder, Dokumente). |

!!! info "Wer hat recht? Der Desktop."
    Ein Abgleich lädt zuerst hoch und holt danach die Änderungen aus der
    Web-App. Haben beide Seiten denselben Eintrag geändert, gewinnt
    deshalb der Desktop. Löschungen wirken in beide Richtungen:

    * Löschen Sie im Desktop einen Eintrag, den der Abgleich kennt (weil er
      ihn hochgeladen oder aus der Web-App übernommen hat), entfernt der
      nächste Abgleich ihn auch in der Web-App. Einträge, die nur in der
      Web-App existieren und nie ins Arbeitsverzeichnis kamen, bleiben
      unberührt.
    * Löschen Sie in der Web-App einen Eintrag, löscht der Abgleich ihn
      auch im Arbeitsverzeichnis. Löscht man die angepasste Fassung einer
      Standard-Druckvorlage, gilt wieder die mitgelieferte. In der Web-App
      gelöschte **Dateien** bleiben im Arbeitsverzeichnis liegen.

!!! info "Ein Konto, ein Arbeitsverzeichnis"
    Die Web-App hat je Konto genau einen Arbeitsbereich. Der erste Abgleich
    bindet ihn an das Arbeitsverzeichnis, mit dem er läuft. Versucht ein
    anderes Arbeitsverzeichnis (z. B. ein anderes Profil) abzugleichen,
    meldet der Stand *Dieses Konto wird schon vom Arbeitsverzeichnis „…"
    abgeglichen (Rechner …, seit …). Ein Konto hat genau ein
    Arbeitsverzeichnis in der Cloud.* Mehrere Rechner, die dasselbe
    Arbeitsverzeichnis auf einem Netzlaufwerk nutzen, gleichen nacheinander
    ab.

!!! info "Was nicht abgeglichen wird"
    Einzelne Dateien über 25 MB (z. B. große Maschinenbilder oder
    3D-Modelle) werden übersprungen; der Stand nennt sie. Benutzer, Rollen
    und Profile gehören nicht zum Arbeitsverzeichnis — sie kommen in der
    Web-App aus dem Kundenkonto.

Als Alternative zum laufenden Abgleich gibt es den einmaligen
[ZIP-Import in der Web-App](../../web/import.md). Der Ablauf beider Wege
steht unter [Daten vom Desktop in die Web-App bringen](../../tasks/desktop-to-web.md).

## Verwandte Seiten

* [Kundenkonto und Einladung](../../setup/account.md) — Bausteine, Plätze, Rollen
* [Anmelden und Lizenz beziehen](../../setup/activate-license.md) — Rechner am Konto anmelden
* [Lizenzportal](../../portal/index.md) — Konto verwalten
* [Web-App](../../web/index.md) — Herzog CAB im Browser
* [Lizenzprobleme](../../help/license-problems.md)
