# Mehrere Benutzer am selben Arbeitsverzeichnis

!!! info "Konzept — Wie Herzog CAB Einträge speichert, wenn mehrere Rechner oder Benutzer gleichzeitig im selben Arbeitsverzeichnis arbeiten, und was Sie bei einer gleichzeitigen Änderung sehen"

Liegt das Arbeitsverzeichnis Ihrer Firma auf einem Netzlaufwerk (siehe
[Speicherort](../admin/storage-location.md)), arbeiten oft mehrere Kollegen
an verschiedenen Rechnern mit denselben Materialien, Maschinen, Aufträgen und
Designs. Damit dabei keine Änderung verloren geht, speichert Herzog CAB jeden
Eintrag **einzeln**, **gesperrt** und **mit Version**:

* **Einzeln** — beim Speichern ersetzt Herzog CAB nur den einen Eintrag, den
  Sie bearbeitet haben. Was ein Kollege zur selben Zeit an einem *anderen*
  Eintrag derselben Liste geändert hat, bleibt erhalten.
* **Gesperrt** — während des kurzen Schreibvorgangs sperrt Herzog CAB die
  Datei, damit zwei Rechner nicht gleichzeitig hineinschreiben.
* **Mit Version** — jeder Eintrag merkt sich, wann, von wem und an welchem
  Rechner er zuletzt gespeichert wurde. Hat ein anderer den **selben**
  Eintrag inzwischen geändert oder gelöscht, fragt Herzog CAB nach, statt
  dessen Änderung stillschweigend zu überschreiben.

!!! warning "Alle Rechner aktualisieren"
    Dieser Schutz wirkt nur, wenn **alle Rechner**, die auf das gemeinsame
    Arbeitsverzeichnis zugreifen, die neue Programmversion haben. Version
    2.1.0 und älter schreiben weiterhin ganze Listen zurück, beachten die
    Sperre nicht und können dabei Änderungen anderer Rechner verwerfen.
    Aktualisieren Sie deshalb alle Arbeitsplätze zur selben Zeit, siehe
    [Updates installieren](../setup/update.md).

## Welche Einträge geschützt sind

| Eintragsart | Beim Speichern | Beim Löschen |
|---|---|---|
| [Materialien](../master-data/materials.md), [Spulen](../master-data/bobbins.md), [Trommeln](../master-data/drums.md) | Versionsprüfung mit Rückfrage, **Als Kopie speichern** möglich | Rückfrage, wenn der Eintrag inzwischen geändert wurde |
| Eigene Maschinen: [Flechtmaschinen](../master-data/braiding-machines.md), [Spulmaschinen](../master-data/winding-machines.md), [Aufwickler](../master-data/take-up-machines.md), [Abwickler](../master-data/pay-off-machines.md), [Gatter](../master-data/creels.md) | Versionsprüfung mit Rückfrage (ohne Kopie) | ohne Rückfrage |
| [Flechtaufträge](../orders/braiding-order.md) und [Spulaufträge](../orders/winding-order.md) | Versionsprüfung mit Rückfrage, **Als Kopie speichern** möglich | ohne Rückfrage |
| [Kunden](../master-data/customers.md), [Farben](../master-data/colors.md), [Grundrisse](../master-data/floor-plans.md), Belegungen des [Hallenplaners](../hall-planner/index.md) | Versionsprüfung mit Rückfrage (ohne Kopie) | ohne Rückfrage |
| [Designs](../master-data/designs.md) | Versionsprüfung mit Rückfrage; statt einer Kopie bietet der Designer **Design unter neuem Namen speichern** an | ohne Rückfrage |
| [Druckvorlagen](../print-templates/manage.md) | gesperrt und einzeln gespeichert, aber **ohne** Versionsprüfung — wer zuletzt speichert, gewinnt | ohne Rückfrage |

Nicht dazu gehören Bilder, Dokumente und Vorschaubilder sowie Benutzer,
Rollen und Firmendaten (die liegen rechnerweit, siehe
[Speicherort](../admin/storage-location.md)). Ein **CSV-Import** von Kunden
oder Maschinen ersetzt vorhandene Einträge ohne Rückfrage.

Auch beim Löschen ohne Rückfrage geht nichts verloren: Die gelöschte Fassung
wird wie jede überschriebene Fassung aufbewahrt (siehe
[Alte Fassungen](#alte-fassungen)).

## Wenn ein anderer denselben Eintrag geändert hat

Speichern Sie einen Eintrag, den inzwischen jemand anderes gespeichert hat,
erscheint eine Rückfrage. Ihr Titel ist der Name des Bereichs (z. B.
*Materialien*, *Auftrag*, *Design*), der Text nennt, **wer** wann und an
welchem Rechner geändert hat, z. B.:

> Das Material "PA 6 schwarz" wurde inzwischen von Max Muster am Rechner
> PC-12 um 14:32 geändert.
>
> Die eigenen Änderungen sind noch nicht gespeichert.

Statt eines Namens steht dort *der Webapp*, wenn die Änderung aus
[Herzog CAB Web](../web/index.md) kam, *Webserver*, wenn ein Bediener den
Auftragsstatus über die mobile Ansicht des
[Webservers](../admin/settings/web-server.md) geändert hat, und *einem
anderen Benutzer*, wenn der Name nicht bekannt ist (z. B. bei einer
Änderung durch eine ältere Programmversion). Ältere Änderungen nennen das
Datum (*am 08.10.2026 um 14:32*).

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Rückfrage „Materialien“ mit dem Text „Das Material "…" wurde inzwischen von … am Rechner … um … geändert. Die eigenen Änderungen sind noch nicht gespeichert.“ und den Schaltflächen **Überschreiben**, **Als Kopie speichern**, **Neu laden** und **Abbrechen**.
    **So erzeugen:** Zwei Programmfenster auf zwei Rechnern (oder zwei Windows-Benutzern) mit demselben Arbeitsverzeichnis; in beiden dasselbe Material öffnen, in Fenster A ändern und speichern, danach in Fenster B ändern und **Speichern** klicken. Musterdaten, Musternamen.
    **Ziel-Datei:** `assets/screenshots/basics/mehrbenutzer-rueckfrage.png`

| Schaltfläche | Wirkung |
|---|---|
| **Überschreiben** | Speichert Ihre Fassung. Die Fassung des anderen bleibt in den [alten Fassungen](#alte-fassungen) erhalten. |
| **Als Kopie speichern** | Speichert Ihre Fassung als **neuen Eintrag** mit dem Zusatz „(Kopie)“ im Namen; der Eintrag des anderen bleibt unverändert. Das Formular zeigt danach die Kopie. Nur bei Materialien, Spulen, Trommeln, Aufträgen und Spulaufträgen — dort ist diese Schaltfläche vorgewählt. Im Designer öffnet sie **Design unter neuem Namen speichern** mit Ordner- und Namenswahl. |
| **Neu laden** | Verwirft Ihre Änderungen und zeigt die neue Fassung des anderen. Bei Maschinen, Kunden, Farben, Grundrissen und Belegungen ist diese Schaltfläche vorgewählt; die Maschinendialoge schließen sich dabei. |
| **Abbrechen** (oder ++esc++) | Es passiert nichts — Ihr Formular bleibt mit Ihren Änderungen offen, z. B. um sie sich zu notieren. |

**Wurde der Eintrag inzwischen gelöscht**, lautet der Text „… wurde
inzwischen von … gelöscht.“ Die Schaltflächen heißen dann **Wieder
anlegen** (legt den Eintrag mit Ihren Änderungen neu an) und **Verwerfen**
(verwirft Ihre Änderungen). Im Designer erscheint bei einem gelöschten
Design stattdessen die Meldung *„Design konnte nicht gespeichert werden“* —
speichern Sie es dann unter neuem Namen.

!!! tip "Keine Rückfrage ohne Grund"
    Ihre eigenen Speicherungen im selben Programmlauf lösen keine Rückfrage
    aus — auch nicht, wenn Sie aus einem Auftrag in den Designer wechseln
    und zurück. Öffnen oder wählen Sie aus dem Auftrag ein Design, ohne den
    Auftrag geändert zu haben, lädt Herzog CAB still die neueste Fassung.
    Arbeiten Sie im Designer mit mehreren Designfenstern, prüft jedes
    Fenster gegen die Fassung seines eigenen Designs.

## Wenn Sie einen inzwischen geänderten Eintrag löschen

Bei **Materialien, Spulen und Trommeln** fragt Herzog CAB nach, wenn der
Eintrag seit dem Öffnen von jemand anderem geändert wurde: „… wurde
inzwischen von … geändert. Trotzdem löschen?“ mit den Schaltflächen
**Trotzdem löschen** und **Abbrechen** (vorgewählt; lädt die Liste neu).
Ist der Eintrag schon gelöscht, gilt Ihr Löschen ohne Meldung als erledigt.

## Wenn die Datei gerade gesperrt ist

Speichert ein anderer Rechner im selben Augenblick in dieselbe Datei, wartet
Herzog CAB bis zu 15 Sekunden. Klappt es dann noch nicht, erscheint eine
Meldung mit **OK**, z. B.:

| Meldung | Bedeutung / Abhilfe |
|---|---|
| *„… wird gerade am Rechner … gespeichert. Bitte gleich noch einmal versuchen.“* bzw. *„… ist gerade gesperrt. Bitte gleich noch einmal versuchen.“* | Ein anderer Rechner schreibt gerade. Nach einem Moment erneut **Speichern** klicken — Ihre Eingaben bleiben im Formular. Eine liegengebliebene Sperre (z. B. nach einem Absturz) gilt nach 30 Sekunden als verwaist. |
| *„Keine Schreibrechte für ….“* | Ihr Windows-Benutzer darf im Arbeitsverzeichnis nicht schreiben — Rechte auf dem Netzlaufwerk prüfen lassen. |
| *„… ist nicht lesbar (…) und wird deshalb nicht überschrieben.“* / *„… hat ein unerwartetes Format und wird deshalb nicht überschrieben.“* | Die Datei ist beschädigt oder von einem anderen Programm geändert. Herzog CAB überschreibt sie zur Sicherheit nicht — wenden Sie sich an den [Support](../help/support.md). |

## Alte Fassungen

Bei jedem Speichern und Löschen legt Herzog CAB die bisherige Fassung des
Eintrags im Arbeitsverzeichnis im unsichtbaren Unterordner `.verlauf` ab.
Aufbewahrt werden je Eintrag **mindestens die letzten 20 Fassungen**; ältere
Fassungen werden entfernt, sobald sie älter als **90 Tage** sind.

In der Desktop-App gibt es noch keine Ansicht, um alte Fassungen anzusehen
oder zurückzuholen; im Notfall hilft der [Support](../help/support.md).
Arbeiten Sie mit dem [Cloud-Abgleich](../admin/settings/license.md), finden
Sie die Versionen und gelöschte Einträge in der Web-App unter
[Versionen und Papierkorb](../web/versions.md).

## Zusammenspiel mit Webserver und Web-App

* **Webserver:** Ändert ein Bediener in der mobilen Ansicht den
  Auftragsstatus, speichert der Webserver nur den Status — gesperrt und mit
  Version. Wer den Auftrag gleichzeitig im Programm offen hat, bekommt beim
  Speichern die Rückfrage, statt den alten Status zurückzuschreiben.
* **Cloud-Abgleich:** Herzog CAB lädt zuerst die eigenen Änderungen hoch und
  holt dann die Änderungen aus der Web-App. Hat das Programm denselben
  Eintrag geändert, gewinnt das Programm; die Fassung aus der Web-App
  bleibt in den Versionen der Web-App erhalten. Übernommene Änderungen aus
  der Web-App tragen den Absender *Webapp*; wer den Eintrag gerade im
  Programm offen hat, bekommt beim Speichern die Rückfrage.

## Verwandte Seiten

* [Speicherort](../admin/storage-location.md) — Arbeitsverzeichnis auf dem Netzlaufwerk
* [Einen weiteren Rechner einrichten](../tasks/add-workstation.md)
* [Lizenz und Cloud](../admin/settings/license.md) — Cloud-Abgleich mit der Web-App
* [Versionen und Papierkorb (Web-App)](../web/versions.md)
