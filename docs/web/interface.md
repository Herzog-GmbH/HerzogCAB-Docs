# Oberfläche der Web-App

!!! info "Konzept — Wie die Web-App aufgebaut ist: Seitenleiste, Kopfzeile, Reiter, Benutzermenü, Listen und Dialoge, Bedienung am Tablet und Smartphone"

## Der Rahmen

![Rahmen der Web-App: Seitenleiste links mit einem Eintrag je Modul, Kopfzeile mit Firma, Sprache und Benutzermenü, Inhalt rechts.](../assets/screenshots/web/oberflaeche.png)

| Bereich | Inhalt |
|---|---|
| **Seitenleiste** (links) | Ein Eintrag je Modul (siehe [unten](#eintrage-der-seitenleiste)), jeweils nur mit dem passenden Recht. Unten Ihr Name, das Konto und das **Abmelden**-Symbol. Die Leiste beantwortet nur die Frage „in welchem Modul bin ich" — Unterseiten und Aktionen liegen in der Seite selbst. |
| **Kopfzeile** (oben) | Links der Name des Kontos mit Kennzeichen (z. B. *intern*, die Edition oder *Testphase: noch n Tage*), rechts die **Sprachauswahl** und das **Benutzermenü**. |
| **Inhalt** | Die aktuelle Seite mit **Seitentitel**, Aktionen rechts daneben (z. B. **Neuer Flechtauftrag**) und darunter **Reitern** für Unterseiten (z. B. *Materialien*, *Spulen*, *Trommeln*, *Farben*, *Kunden* unter Stammdaten oder die Maschinenarten im Herzog-Katalog). |

### Einträge der Seitenleiste

Von oben nach unten, jeweils nur mit dem genannten Recht
([Rollen](roles.md)):

| Eintrag | Sichtbar mit | Seite |
|---|---|---|
| **Startseite** | immer | [Startseite](start.md) |
| **Aufträge** | *Aufträge anzeigen* | [Aufträge](orders.md) |
| **Hallenansicht** | *Aufträge anzeigen* und *Stammdaten anzeigen* | Aufträge je Maschine mit ihrem Status |
| **Berechnungen** | *Berechnungen ausführen* | [Berechnungen](calculations.md) |
| **Designs** | *Designer anzeigen* | [Designs und Designer](designer.md) |
| **Maschinen** | *Stammdaten anzeigen* | [Maschinen](machines.md) |
| **Katalog** | *Stammdaten anzeigen* | [Herzog-Katalog](catalog.md) |
| **Stammdaten** | Recht auf mindestens einen Stammdaten-Reiter | [Stammdaten](master-data.md) |
| **Hallenplaner** | *Hallenplaner anzeigen* | [Hallenplaner](hall-planner.md) |
| **Druck Editor** | *Druckvorlagen anzeigen* | [Druck Editor](print-editor.md) |
| **Parameter Explorer** | *Parameter Explorer öffnen* und *Aufträge anzeigen* | Parameter der Aufträge |

Welche Einträge Sie sehen, richtet sich außerdem nach dem Baustein: Mit
*Herzog CAB Designer* fehlen Aufträge, Hallenansicht, Berechnungen,
Maschinen, Katalog, Hallenplaner und Parameter Explorer; unter Stammdaten
bleiben Farben und Kunden.

## Benutzermenü

Ein Klick auf Ihre Initialen bzw. Ihren Namen rechts oben öffnet das
Benutzermenü:

| Eintrag | Ziel |
|---|---|
| **Konto** (Auswahl) | Nur für Mitarbeiter von Herzog mit mehreren internen Konten: wechselt das Konto. |
| **Sprache** | Am Smartphone hier statt in der Kopfzeile. |
| **Einstellungen** | [Sprache, Benutzer, Passwort-Hinweis](settings.md). |
| **Konto und Benutzer** | [Edition, Bausteine, Plätze, Benutzer und Rollen](account.md). |
| **Abo und Bestellung** | [Freischaltungen, Testphase, Jahresabo bestellen oder Anfrage](subscription.md). |
| **Firma** | [Firmendaten und Logo für Druckvorlagen](company.md). |
| **Medienbibliothek** | [Hochgeladene Bilder und Dokumente](media.md). |
| **Papierkorb** | [Gelöschte Einträge ansehen und wiederherstellen](versions.md#papierkorb). |
| **Rollen** | [Rollen und Rechte](roles.md) — nur mit den Rechten *Rollen verwalten* bzw. *Benutzer verwalten*. |
| **Import aus dem Desktop** | [ZIP-Import und -Export des Arbeitsbereichs](import.md) — nur mit dem Recht *Workspace-Einstellungen*. |
| **Abmelden** | Beendet die Sitzung. |

## Listen, Karten und Formulare

* **Listen** haben oben ein **Suchfeld** und **Filter**; die Trefferzahl
  steht daneben (*n von m …*). Auf schmalen Bildschirmen werden Tabellen zu
  **Karten**.
* **Neu…**-Schaltflächen stehen rechts neben dem Seitentitel; **Öffnen**
  bzw. ein Klick auf die Zeile führt in den Editor.
* **Speichern** sitzt oben rechts im Editor. Nach dem Speichern erscheint
  kurz eine Bestätigung (*Gespeichert.*) am unteren Rand; Fehler erscheinen
  als rote Hinweisbox.
* **Sicherheitsabfragen** (z. B. beim Löschen) öffnen sich als Dialog — am
  Smartphone als Bogen von unten. Gelöschte Aufträge, Designs, Maschinen,
  Stammdaten, Hallenpläne und Druckvorlagen landen im
  [Papierkorb](versions.md#papierkorb).
* **Versionen:** Editoren haben einen Knopf **Versionen** mit den früheren
  Fassungen des Eintrags, siehe [Versionen und Papierkorb](versions.md).
* **Versionskonflikt:** Hat jemand anderes einen Eintrag gespeichert,
  während Sie ihn offen hatten (z. B. die Desktop-App über den
  Cloud-Abgleich), meldet die Web-App beim Speichern *„Der Eintrag wurde
  inzwischen von jemand anderem geändert. Bitte neu laden."* — laden Sie die
  Seite neu und tragen Sie Ihre Änderung erneut ein. Was der andere
  gespeichert hat, sehen Sie danach unter **Versionen**. Meist verhindert
  das schon die [Bearbeitungssperre](#bearbeitungssperre).

## Bearbeitungssperre

Öffnen Sie einen Eintrag zum Bearbeiten, sperrt die Web-App ihn für alle
anderen: für Kollegen in der Web-App und, wenn die Desktop-App mit dem
[Cloud-Abgleich](../admin/settings/license.md) arbeitet, auch für die
Rechner am Arbeitsverzeichnis. Wer denselben Eintrag öffnet, sieht ihn nur
zum Lesen, bis Sie fertig sind. Den Grundgedanken und die Seite der
Desktop-App beschreibt
[Mehrere Benutzer am selben Arbeitsverzeichnis](../basics/multi-user.md#die-bearbeitungssperre).

Gesperrt wird beim Öffnen: Flecht- und Spulaufträge, Designs im
[Designer](designer.md) (kommen Sie aus einem Auftrag, auch der Auftrag),
[Maschinen](machines.md), im [Hallenplaner](hall-planner.md) der Grundriss
und die gewählte Belegung, die Vorlage im [Druck Editor](print-editor.md),
der Eintrag im Bearbeitungsdialog der [Stammdaten](master-data.md) und das
Programm im [Flechtsimulator](braiding-simulator.md). Neue, noch nicht gespeicherte Einträge und
Einträge, die Sie nur ansehen dürfen, sperrt die Web-App nicht.

### Das Schloss

Was gerade ein **anderer** bearbeitet, trägt in Listen und Karten ein
kleines graues Schloss: in den Aufträgen, den Designs, den Maschinen, den
Hallenplänen, den Stammdaten, der Hallenansicht, der Vorlagenauswahl des
Druck Editors und im Flechtsimulator. Zeigen Sie darauf, nennt der Tooltip
*In Bearbeitung* und darunter Name, Ort und Beginn, z. B.
*Max Muster · PC-12 · seit 14:32*. Als Ort steht der Rechnername, wenn
jemand in der Desktop-App bearbeitet, sonst *Webapp*. Die Listen sehen alle
30 Sekunden nach; ein Schloss erscheint oder verschwindet deshalb mit kurzer
Verzögerung.

### Der Hinweis im Editor

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Auftrag in der Web-App mit dem Hinweis „In Bearbeitung – nur lesen“ neben **Versionen**, den Knöpfen **Erneut versuchen** und **Sperre aufheben** und dem Tooltip am Schloss.
    **So erzeugen:** Denselben Auftrag in zwei Browsern (zwei Benutzer desselben Kontos, einer mit dem Recht *Sperren aufheben*) öffnen; im zweiten Browser mit der Maus auf das Schloss zeigen. Musterkonto, 1440 × 900 px.
    **Ziel-Datei:** `assets/screenshots/web/sperre-hinweis.png`
    <!-- web-bild ../assets/screenshots/web/sperre-hinweis.png -->

Bearbeitet ein anderer den Eintrag, steht oben im Editor neben
**Versionen** ein Hinweis, und alle Felder sind nur lesbar:

| Hinweis | Bedeutung | Knöpfe |
|---|---|---|
| *In Bearbeitung – nur lesen* | Ein anderer bearbeitet den Eintrag; wer, steht im Tooltip am Schloss. | **Erneut versuchen** fragt sofort nach; ist er noch nicht frei, meldet die Web-App *Der Eintrag ist noch in Bearbeitung.* **Sperre aufheben** nur mit dem Recht *Sperren aufheben*. |
| *Jetzt frei – neu laden* | Der andere ist fertig. Holt inzwischen ein Dritter den Eintrag, steht wieder *In Bearbeitung – nur lesen* da. | **Neu laden** lädt die Seite mit der aktuellen Fassung, danach bearbeiten Sie. |
| *Inzwischen in Bearbeitung – nur lesen* | Sie hatten den Eintrag, jetzt bearbeitet ihn ein anderer. | **Neu laden** |
| *Ihre Bearbeitung wurde beendet – nur lesen. Ungespeichertes lässt sich nicht mehr speichern.* | Jemand mit dem Recht *Sperren aufheben* hat Ihre Sperre aufgehoben. | **Neu laden** |
| *Wegen Inaktivität freigegeben – zum Weiterarbeiten neu laden* | 30 Minuten ohne Eingabe und ohne ungespeicherte Änderungen: Die Web-App hat den Eintrag freigegeben. | **Neu laden** |
| *Keine Verbindung zum Server – nur lesen* | Die Web-App erreicht den Server nicht und kann die Sperre nicht holen. | **Erneut versuchen** |

Speichern, Löschen oder Wiederherstellen eines Eintrags, den gerade ein
anderer bearbeitet, lehnt der Server mit *Dieser Eintrag ist gerade in
Bearbeitung.* ab.

### Wann der Eintrag wieder frei ist

* Sie schließen den Tab, laden die Seite neu oder wechseln in der Web-App
  auf eine andere Seite. Wechseln Sie gleich weiter in einen Editor desselben
  Eintrags (z. B. vom Designer zurück in den Auftrag), bleibt die Sperre
  ohne Lücke bestehen.
* 30 Minuten ohne Eingabe, wenn nichts Ungespeichertes daran hängt.
* Der Tab meldet sich jede Minute beim Server. Kommt drei Minuten lang
  nichts, etwa weil der Rechner schläft oder das Netz weg ist, ist der
  Eintrag frei.

Jeder Browser-Tab bearbeitet für sich: Öffnen Sie denselben Eintrag in einem
zweiten Tab oder zusätzlich in der Desktop-App, sehen Sie ihn dort nur zum
Lesen.

### Sperre aufheben

Mit dem Recht **Sperren aufheben** (Gruppe *Administration*, von Haus aus
nur in der Rolle *Administrator*, siehe [Rollen](roles.md)) beenden Sie
eine fremde Sperre: **Sperre aufheben** im Hinweis klicken und die
Rückfrage *Sperre aufheben?* bestätigen. Sie nennt den Bearbeiter, z. B.
*In Bearbeitung von Max Muster an PC-12, seit 14:32. Wer die Sperre
aufhebt, beendet diese Bearbeitung: Ungespeichertes lässt sich dort danach
nicht mehr speichern.* Die Seite lädt neu, und Sie bearbeiten den Eintrag.
Das Aufheben wird protokolliert. Hat inzwischen ein anderer den Eintrag
übernommen, meldet die Web-App *Inzwischen bearbeitet jemand anderes den
Eintrag.*

### Status aus der Halle

Den Auftragsstatus in der **Hallenansicht** können Sie auch dann setzen,
wenn jemand den Auftrag gerade bearbeitet. Wer den Auftrag offen hat,
übernimmt den neuen Status beim Speichern: *Der Status wurde inzwischen in
der Halle auf „In Produktion“ gesetzt und übernommen.* Hatte er den Status
selbst geändert, gilt seiner: *Gespeichert. Der Status aus der Halle („In
Produktion“) wurde durch Ihren ersetzt.*

## Tablet und Smartphone

Die Web-App passt sich der Bildschirmbreite an:

* **Ab 768 px (Tablet):** Seitenleiste und Kopfzeile wie am Desktop, Listen
  je nach Platz als Karten.
* **Smartphone:** Die Seitenleiste wird zur **Schublade**, die Sie über das
  Menü-Symbol links oben öffnen. Am unteren Rand liegt eine **Tab-Leiste**
  mit **Start**, **Aufträge**, **Rechner**, **Designs** und **Mehr** (öffnet
  die Schublade). In den Zeichenflächen (Designer, Hallenplaner) zoomen Sie
  mit zwei Fingern.

!!! tip "Als App auf dem Startbildschirm"
    Die meisten Browser bieten an, die Seite *zum Startbildschirm hinzuzufügen*.
    Dann startet die Web-App wie eine App — ohne Adressleiste.

## Verwandte Seiten

* [Anmelden und Konto wählen](login.md)
* [Startseite](start.md)
* [Versionen und Papierkorb](versions.md)
* [Mehrere Benutzer am selben Arbeitsverzeichnis](../basics/multi-user.md) — Bearbeitungssperre in der Desktop-App
* [Rollen](roles.md) — Recht *Sperren aufheben*
* [Oberfläche im Überblick (Desktop-App)](../basics/interface.md) — zum Vergleich
