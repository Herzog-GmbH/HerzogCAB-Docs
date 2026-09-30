# Screenshots Desktop-App — Liste für Elke

Stand: 19.09.2026, Handbuch 2.0. Insgesamt **43** Platzhalter auf 29 Seiten.


Jeder Platzhalter steht im Handbuch als Admonition `!!! warning "📷 Screenshot fehlt"` (Suche nach „Screenshot fehlt") mit
**Motiv**, **So erzeugen** und **Ziel-Datei**. Bild unter `docs/<Ziel-Datei>` ablegen und den Platzhalter durch
`![<Bildunterschrift>](<relativer Pfad>)` ersetzen — Beispiele stehen auf jeder Seite (bestehende Bilder).

**Aufnahme-Regeln (STYLEGUIDE.md):** helles Theme, ~1600 px Fensterbreite, 100 % Skalierung, Demodaten „Musterbetrieb"
(keine echten Kunden/Preise), Kunden-Build mit Kontoanmeldung (`CONFIG+=customer account`), soweit nicht anders angegeben.
Die Web-App- und Portal-Screenshots (Ordner `web/`, `portal/`) entstehen per `_tools/web_screenshots.py` aus der lokalen
Testumgebung und stehen deshalb NICHT in dieser Liste (Suche nach „web_screenshots.py" zeigt die offenen).

## Zusätzlich zu ersetzen: veraltete Bestandsbilder

| Datei | Warum | Was drauf sein soll |
|---|---|---|
| `assets/screenshots/orders/auftraege-uebersicht.png` | vor Spulaufträgen aufgenommen | Auftragsübersicht mit Flecht- **und** Spulaufträgen, Filter Auftragsart sichtbar |
| `assets/screenshots/master-data/maschinenpark.png` | vor Spulmaschinen aufgenommen | Maschinenpark mit Flecht- und Spulmaschinen, Typ-Gruppierung und Auftrags-Badges |
| `assets/screenshots/users/benutzer.png` | zeigt weder LDAP-Button noch Kontomodell | wird durch `admin/benutzer-konto.png` (Kontomodell) und `admin/benutzer.png` (Dongle) ersetzt, siehe unten |
| `assets/screenshots/getting-started/oberflaeche-home.png` | Home ohne Spulerei | Home-Seite mit Flecht- und Spulaufträgen in den Status-Kacheln |
| `assets/screenshots/settings/einstellungen-allgemein.png` | ohne Karte „Produktionsplanung" | Tab Allgemein inkl. Produktionsplanung |
| `assets/screenshots/design/designer-canvas.png` | alte Werkzeugleiste (3D-Knopf) | Bearbeitungsansicht mit Voll/Halb/Zylinder/3D — kann durch `designer/designer-bearbeitungsansicht.png` ersetzt werden |


## Loslegen (setup/) — 9 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 1 | `setup/activate-license.md` | Dialog „Herzog CAB – Anmeldung am Kundenkonto" mit Erklärtext, den Feldern **E-Mail-Adresse** und **Passwort** sowie den Schaltflächen **Anmelden** und **Beenden**. | Kunden-Build auf einem Rechner ohne `license.json` starten (oder vorher unter *Einstellungen > Lizenz* **Von diesem Rechner abmelden** wählen). | `assets/screenshots/setup/konto-anmeldung-geraet.png` |
| 2 | `setup/activate-license.md` | CodeMeter-Tray-Icon im Windows-Infobereich vor und nach dem Einstecken des Dongles (Farbwechsel grau → blau). | Dongle abgezogen fotografieren, dann einstecken und nach ein paar Sekunden erneut fotografieren. | `assets/screenshots/activate-license/tray-icon-farbwechsel.png` |
| 3 | `setup/activate-license.md` | CodeMeter Kontrollzentrum mit erkanntem CmDongle, Firmencode 6001037 und Artikel 88805 in der Lizenzliste. | Dongle einstecken, CodeMeter Kontrollzentrum öffnen, Lizenzliste zeigen. | `assets/screenshots/activate-license/kontrollzentrum-dongle-erkannt.png` |
| 4 | `setup/activate-license.md` | CodeMeter Kontrollzentrum direkt nach dem Doppelklick auf den `.WibuCmLif`-Container — Eintrag „Herzog GmbH", Status „Aktivierung ungültig". | `.WibuCmLif`-Datei doppelklicken, Kontrollzentrum fotografieren. | `assets/screenshots/activate-license/kontrollzentrum-leerer-container.png` |
| 5 | `setup/activate-license.md` | CmFAS-Assistent mit ausgewählter Option „Lizenzanforderung erzeugen". | Im CodeMeter Kontrollzentrum **Lizenz aktivieren** anklicken, ersten Assistenten-Schritt fotografieren. | `assets/screenshots/activate-license/cmfas-lizenzanforderung-erzeugen.png` |
| 6 | `setup/first-run.md` | Dialog „Benutzerverwaltung einrichten" mit den Feldern Firma, Login-Name, Anzeigename, E-Mail, Passwort, Passwort bestätigen. | Herzog CAB auf einem Rechner ohne bestehende Benutzerverwaltung starten (leerer `%ProgramData%\Herzog GmbH\Herzog Cab`). | `assets/screenshots/setup/erstadmin-einrichten.png` |
| 7 | `setup/uninstall.md` | Maintenance-Tool-Assistent im Schritt „Alle Komponenten entfernen". | Maintenance-Tool über *Herzog > Herzog CAB Maintenance* öffnen und den Deinstallations-Schritt fotografieren. | `assets/screenshots/setup/maintenance-tool-entfernen.png` |
| 8 | `setup/update.md` | Dialog „Update verfügbar" mit Versionsangabe, Was-ist-neu-Liste und den drei Schaltflächen. | *Hilfe > Updates* anklicken, wenn eine neuere Version veröffentlicht ist. | `assets/screenshots/setup/update-dialog.png` |
| 9 | `setup/update.md` | Maintenance-Tool-Assistent im Schritt „Komponenten aktualisieren". | Maintenance-Tool über *Herzog > Herzog CAB Maintenance* öffnen und den Update-Schritt fotografieren. | `assets/screenshots/setup/maintenance-tool-update.png` |

## Grundlagen (basics/) — 1 Bild

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 10 | `basics/guided-tour.md` | Dialog „Geführte Touren" mit den zehn Themenkarten und den Start-Schaltflächen | *Hilfe > Geführte Touren…* öffnen, Dialog unverändert aufnehmen | `assets/screenshots/basics/gefuehrte-touren-dialog.png` |

## Aufträge (orders/) — 5 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 11 | `orders/braiding-order.md` | Tab „Produktion" mit den beiden Abschnitten „Produktionswerte" (links) und „Hochrechnung auf die Auftragslänge" (rechts), inklusive gefüllter berechneter Felder | Flechtauftrag mit Auftragslänge, Maschine, Material, Spule und ausgeführter Laufzeit-Berechnung öffnen; Tab *Produktion* wählen | `assets/screenshots/orders/auftrag-tab-produktion.png` |
| 12 | `orders/braiding-order.md` | Tab „Design" mit verknüpftem Design: Feld „Verknüpftes Design" mit den drei Schaltflächen, Vorschau-Miniatur mit Design-Infos und geöffneter Unter-Tab „Klöppel-Tabelle" mit farbigen Zellen | Flechtauftrag mit verknüpftem mehrfarbigem Design öffnen; Tab *Design*, Unter-Tab *Klöppel-Tabelle* wählen | `assets/screenshots/orders/auftrag-tab-design.png` |
| 13 | `orders/index.md` | Auftragsübersicht mit Suchfeld, den vier Filtern (Auftragsart, Status, Zeitraum, Sortierung), zeitlich gruppierten Auftragskarten (Flecht- und Spulauftrag gemischt, mit Auftragsart-Chips und Verknüpfungszeile) und der Aktionsleiste unten inkl. **Spulauftrag erstellen** | Navigationspunkt *Aufträge* öffnen; Workspace „Musterbetrieb" mit mindestens einem Flechtauftrag samt verknüpftem Spulauftrag; einen Flechtauftrag anwählen, damit alle Schaltflächen aktiv sind | `assets/screenshots/orders/auftraege-uebersicht.png` |
| 14 | `orders/print.md` | Dialog „Druckvorlage wählen" mit Auswahlliste (Standardvorlage vorgewählt, eine eigene Vorlage zusätzlich sichtbar) | Im Flechtauftrag-Editor **Drucken** klicken; vorher unter *Druck Editor* eine eigene Auftragsvorlage anlegen, damit der Dialog erscheint | `assets/screenshots/orders/auftrag-druckvorlage-waehlen.png` |
| 15 | `orders/winding-order.md` | Spulauftrag-Editor mit Kopfzeile (**Zur Auftragsübersicht**, **Drucken**, **Spulauftrag speichern**) und den drei Karten „Auftrag", „Spulerei — was wird gespult?" und „Maschinen und Zeitplan" auf einer Scroll-Seite; verknüpfter Flechtauftrag, gefüllte Farbaufschlüsselung und zwei Spulmaschinen in der Verteiltabelle | In der Auftragsübersicht einen Flechtauftrag mit Design anwählen und **Spulauftrag erstellen** klicken; zwei Spulmaschinen hinzufügen, **Spulen gleichmäßig verteilen** | `assets/screenshots/orders/spulauftrag-editor.png` |

## Maschinenpark — 1 Bild

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 16 | `machine-park/index.md` | Maschinenpark-Übersicht (Kartenansicht) mit der aktuellen Filterzeile inklusive Filter **Maschinenart** und einem gemischten Park aus Flecht- und Spulmaschinen | *Maschinenpark* öffnen; Datenbestand mit mindestens einer Spulmaschine, damit der Filter „Maschinenart" relevant ist; Kartenansicht aktiv | `assets/screenshots/machine-park/maschinenpark.png` |

## Hallenplaner — 3 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 17 | `hall-planner/editor.md` | Editor im Geometrie-Modus — links die Werkzeugleiste mit den Gruppen WERKZEUGE, WÄNDE, FLÄCHEN, OBJEKTE; Mitte ein Grundriss mit Wänden und einer farbigen Fläche; rechts das Eigenschaften-Panel (Reiter Layout) **So erzeugen:** *Stammdaten > Grundrisse* > Grundriss wählen > **Bearbeiten**; ein paar Wände und eine Produktionsfläche zeichnen **Ziel-Datei:** `assets/screenshots/hall-planner/editor-geometrie.png` | *Stammdaten > Grundrisse* > Grundriss wählen > **Bearbeiten**; ein paar Wände und eine Produktionsfläche zeichnen **Ziel-Datei:** `assets/screenshots/hall-planner/editor-geometrie.png` | `assets/screenshots/hall-planner/editor-geometrie.png` |
| 18 | `hall-planner/editor.md` | Editor im Bestückungs-Modus — links WERKZEUGE + KATALOG mit Maschinenliste; über der Zeichenfläche die Auswahl-Toolbar (Bearbeiten · Ausrichten · Verteilen · Aneinanderreihen); mehrere platzierte Maschinen, davon zwei markiert; rechts das Eigenschaften-Panel mit Maschinen-Eigenschaften **So erzeugen:** *Hallenplaner* > Grundriss und Belegung wählen > **Bestücken**; zwei Maschinen markieren (Rahmen aufziehen) **Ziel-Datei:** `assets/screenshots/hall-planner/editor-bestueckung.png` | *Hallenplaner* > Grundriss und Belegung wählen > **Bestücken**; zwei Maschinen markieren (Rahmen aufziehen) **Ziel-Datei:** `assets/screenshots/hall-planner/editor-bestueckung.png` | `assets/screenshots/hall-planner/editor-bestueckung.png` |
| 19 | `hall-planner/view-3d.md` | 3D-Hallenansicht mit Wänden, mehreren Maschinen und mindestens einer farbigen Status-Leuchtkugel; oben die dunkle Werkzeugleiste (Kamera zurücksetzen, Wände Voll/Aus/Stufen, Kugeln-Regler, Puls) | Bestückte Belegung im Editor öffnen > Ansicht-Schalter **3D**; Kamera leicht schräg von oben ausrichten | `assets/screenshots/hall-planner/3d-hallenansicht.png` |

## Designer — 8 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 20 | `designer/animation.md` | Besetzungsübersicht eines Packungsgeflechts (3×3 Flügelräder) mit eingefärbten Klöppeln, den Animations-Schaltflächen (Play, langsamer, schneller) oben links und den beiden Farbrotations-Pfeilen darunter. | *Designer* öffnen, **Neu**, Geflechtsart | `assets/screenshots/designer/designer-besetzungsuebersicht.png` |
| 21 | `designer/index.md` | Designer-Bearbeitungsansicht mit geöffnetem Rundgeflecht-Design: Werkzeugleiste oben (mit den Ansichts-Schaltern Voll/Halb/Zylinder/3D), Dokument-Kopfzeile, links Parameter-Panel mit den Auswahllisten Geflechtsart und Geflechtsbindung und der Besetzungsübersicht, Mitte Klöppeltabelle, rechts Flechtbild-Vorschau mit Maßzeile. | *Designer* öffnen, **Neu** klicken, Fenster breit ziehen (Farb- und Texturpalette sichtbar in der Werkzeugleiste), einige Klöppel einfärben. | `assets/screenshots/designer/designer-bearbeitungsansicht.png` |
| 22 | `designer/painting.md` | Werkzeugleiste des Designers mit geöffneter Farbpalette: großes Aktive-Farbe-Quadrat, Paletten-Auswahlliste, Bibliotheksfarben, Benutzerfarben-Reihe und Farbrad-Schaltfläche; daneben die Texturpalette mit großer Vorschau. | *Designer* öffnen, **Neu** klicken, Fenster breit ziehen, damit die Gruppen **Farbe** und **Texturen** in der Werkzeugleiste sichtbar sind. | `assets/screenshots/designer/designer-farbpalette.png` |
| 23 | `designer/parameters.md` | Das Parameter-Panel links im Designer mit Designname, den Auswahllisten **Geflechtsart** (aufgeklappt, alle sechs Einträge sichtbar) und **Geflechtsbindung** sowie den Feldern Anzahl Klöppel, Flechtwinkel und Fachung. | *Designer* öffnen, **Neu** klicken; die Liste Geflechtsart aufklappen; nur das linke Panel (oberer Teil bis einschließlich „Fachung") aufnehmen. | `assets/screenshots/designer/designer-parameter-panel.png` |
| 24 | `designer/save-print.md` | Der Dialog **Design speichern** mit Namensfeld, dem Ordnerbaum der Design-Bibliothek (inklusive Eintrag „Ohne Ordner" und Unterordnern), der Zeile „Neuer Ordner (unterhalb der Auswahl)…" mit **Anlegen** sowie den Schaltflächen **Abbrechen** und **Speichern**. | Neues Design anlegen, etwas färben, **Speichern** klicken. | `assets/screenshots/designer/designer-speichern-dialog.png` |
| 25 | `designer/save-print.md` | Druckvorschau-Fenster eines Designs (Standardvorlage): Seite mit Flechtbild, Besetzungsübersicht und Klöppeltabelle, Zoom-Leiste und Drucken-Schaltfläche. | Design mit Farben öffnen, **Drucken** klicken, Vorlage bestätigen. | `assets/screenshots/designer/designer-druckvorschau.png` |
| 26 | `designer/view-3d.md` | Vorschau-Bereich des Designers in der 3D-Ansicht: ein zweifarbiges Rundgeflecht als räumliches Modell, darüber die Ansichtsleiste (Draufsicht / Seitenansicht / Flechtpunkt + Schloss), darunter die Reglerzeile Material / Darstellung / Ausrichtung; in der Werkzeugleiste ist **3D** aktiv. | *Designer* öffnen, Rundgeflecht 24 Klöppel, Linkslauf rot und Rechtslauf blau färben, in der Werkzeugleiste **3D** wählen, Ansicht *Seitenansicht*. | `assets/screenshots/designer/designer-3d-ansicht.png` |
| 27 | `designer/view-3d.md` | Dieselbe Vorschau in der Ansicht **Zylinder** (Projektion), leicht gedreht, mit den Drehpfeilen. | wie oben, Ansicht **Zylinder** wählen und einmal drehen. | `assets/screenshots/designer/designer-zylinder-ansicht.png` |

## Stammdaten — 4 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 28 | `master-data/braiding-machines.md` | Der Dialog *Neue Maschine erstellen* mit Bild, dem Formular „Maschinendaten" und dem Abschnitt „Dokumente". | In **Flechtmaschinen** auf **Neu** klicken und den Dialog mit Demo-Daten „Musterbetrieb" ausfüllen. | `assets/screenshots/master-data/flechtmaschine-neu-dialog.png` |
| 29 | `master-data/designs.md` | Die Design-Bibliothek mit Ordnerbaum links, Design-Tabelle rechts (mit Thumbnails) und der Werkzeugleiste darüber. | Navigationspunkt **Designs** öffnen, einen Ordner mit mehreren Beispiel-Designs auswählen (Demo-Daten „Musterbetrieb"). | `assets/screenshots/master-data/designs-bibliothek.png` |
| 30 | `master-data/winding-machines.md` | Die Spulmaschinen-Liste als Karten (mit Baureihe, Spulstellen, Spulen-Durchmesser und Drehzahl) samt Werkzeugleiste. | Navigationspunkt **Spulmaschinen** öffnen, einige Beispiel-Spulmaschinen der Baureihen SP/SPA/HLM (Demo-Daten „Musterbetrieb") anlegen. | `assets/screenshots/master-data/spulmaschinen.png` |
| 31 | `master-data/winding-machines.md` | Der Dialog *Neue Spulmaschine erstellen* mit Baureihenauswahl und dem Abschnitt „Wickeltechnik". | In **Spulmaschinen** auf **Neu** klicken; als Baureihe einmal SPA (zeigt den Abschnitt „Automatischer Spulenwechsel") und einmal HLM (zeigt „Litzenschlag") wählen. | `assets/screenshots/master-data/spulmaschine-neu-dialog.png` |

## Druck-Editor — 2 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 32 | `print-templates/elements.md` | Der Bearbeitungsdialog einer Datentabelle (z. B. „Auftrag“) mit der Zeilen-Werkzeugleiste links und dem Feldvorlagen-Picker rechts. | Druck-Editor öffnen, eine Datentabelle wie „Auftrag“ auf die Seite ziehen, per Doppelklick öffnen. | `assets/screenshots/print-templates/tabelle-bearbeiten.png` |
| 33 | `print-templates/elements.md` | Der Feldvorlagen-Picker (Suche, Bereich-Auswahl, Liste, Schaltfläche „Feld einfügen“) im geöffneten Zustand mit ein paar Suchtreffern. | Bearbeitungsdialog einer Datentabelle öffnen, im Suchfeld einen Begriff eintippen (z. B. „Durchmesser“). | `assets/screenshots/print-templates/feldvorlagen-picker.png` |

## Verwaltung (admin/) — 10 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 34 | `admin/authentication.md` | Bildschirm „Authentifizierung", Reiter „Microsoft Entra ID" mit Konfigurationsfeldern und der Tabelle „Entra-Gruppe → Rolle" | *Systemverwaltung > Authentifizierung* öffnen (Reiter Microsoft Entra ID aktiv); Beispieldaten ohne echte Tenant-/Client-IDs verwenden | `assets/screenshots/admin/authentifizierung-entra.png` |
| 35 | `admin/authentication.md` | Bildschirm „Authentifizierung", Reiter „LDAP / Active Directory" mit allen Verbindungsfeldern und der Schaltfläche „Verbindung prüfen" | *Systemverwaltung > Authentifizierung* öffnen, Reiter „LDAP / Active Directory" wählen; Beispieldaten (example.local) verwenden | `assets/screenshots/admin/authentifizierung-ldap.png` |
| 36 | `admin/login.md` | Anmeldefenster „Herzog CAB – Anmelden" im Kontomodell: Hinweistext, Zeile „Konto: <Firma>", Felder E-Mail-Adresse und Passwort, Schaltflächen Anmelden und Beenden. | Kunden-Build auf einem am Konto angemeldeten Rechner ein zweites Mal starten. | `assets/screenshots/admin/anmelden-konto.png` |
| 37 | `admin/login.md` | Anmeldefenster „Herzog CAB – Anmelden" mit Logo, Feldern Login/Passwort und der Schaltfläche „Mit Microsoft anmelden" | Herzog CAB mit Dongle starten (Entra-Anmeldung muss unter *Systemverwaltung > Authentifizierung* aktiviert sein, sonst fehlt die Microsoft-Schaltfläche) | `assets/screenshots/admin/anmelden.png` |
| 38 | `admin/my-profile.md` | Dialog „Mein Profil", Reiter „Profil" mit Profilbild, Anzeigename und E-Mail | unten links in der Navigation auf die eigene Benutzerkarte klicken | `assets/screenshots/admin/mein-profil.png` |
| 39 | `admin/settings/legacy-import.md` | Tab „Design" des Einstellungen-Dialogs mit den Karten „Vorgaben für neue Designs", „Vorschau & Ansicht", „Animation", „Speichern" und „Legacy-Designimport". | *Datei > Einstellungen*, Tab **Design**, Dialog so hoch ziehen, dass alle fünf Karten sichtbar sind. | `assets/screenshots/settings/einstellungen-design.png` |
| 40 | `admin/settings/license.md` | Tab „Lizenz" mit den drei Karten „Lizenz – Kundenkonto (Lizenzserver)", „Konto" und „Cloud (app.herzog-cab.com)"; Konto, Benutzer, Edition, Bausteine und Miete gefüllt, Cloud-Schalter aktiv. | Kunden-Build mit Kontoanmeldung, *Datei > Einstellungen*, Tab **Lizenz**. | `assets/screenshots/settings/einstellungen-lizenz.png` |
| 41 | `admin/storage-location.md` | Bildschirm „Speicherort" mit Badge NETZWERK/LOKAL, Pfad der zentralen Benutzerdaten und Abschnitt „Arbeitsbereich (aktives Profil)" | *Systemverwaltung > Speicherort* öffnen | `assets/screenshots/admin/speicherort.png` |
| 42 | `admin/users.md` | Benutzerverwaltung im Kontomodell — Benutzerliste links mit dem Hinweistext „Benutzer, Passwörter und Rollen kommen aus dem Kundenkonto …" und den Schaltflächen „Vom Kundenkonto aktualisieren" und „Lizenzportal öffnen", Benutzer-Editor rechts mit ausgegrauten Stammdatenfeldern und der Infozeile „Kontobenutzer (Lizenzserver)" | Kunden-Build mit Kontoanmeldung, *Systemverwaltung > Benutzer* öffnen, einen Benutzer auswählen | `assets/screenshots/admin/benutzer-konto.png` |
| 43 | `admin/users.md` | Benutzerverwaltung bei Dongle-Installation — Benutzerliste links (mit den Schaltflächen „Neuer Benutzer", „Aus Entra importieren", „Aus LDAP importieren"), Benutzer-Editor rechts | Build mit Dongle, *Systemverwaltung > Benutzer* öffnen, einen Benutzer auswählen | `assets/screenshots/admin/benutzer.png` |

## Nachtrag Handbuch 2.1.0 (30.09.2026) — 11 Bilder

Neue Platzhalter auf den 2.1.0-Seiten (Kunden-Build 2.1.0 mit Kontoanmeldung, Vollversion). Außerdem veraltet:
`assets/screenshots/orders/auftrag-editor-kunde.png` zeigt neun Tabs — seit 2.1.0 hat der Flechtauftrag zehn (neuer Tab „Aufwicklung").

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| N1 | `master-data/take-up-machines.md` | Aufwickler-Liste als Karten (Bild, Baureihe, „Trommel bis Ø … mm", Traglast, Verlegebreite) samt Werkzeugleiste. | *Stammdaten > Aufwickler*; einige Aufwickler AW, AWS, AWH anlegen, einer mit Haspel. | `assets/screenshots/master-data/aufwickler.png` |
| N2 | `master-data/take-up-machines.md` | Dialog „Neuen Aufwickler erstellen" mit „Maschinendaten", „Maße und Grenzen", „Bauart". | **Neu**, Baureihe AWS, Demo-Maße, bis „Bauart" scrollen. | `assets/screenshots/master-data/aufwickler-neu-dialog.png` |
| N3 | `master-data/pay-off-machines.md` | Abwickler-Liste als Karten samt Werkzeugleiste. | *Stammdaten > Abwickler*; einige Abwickler AB, ABS anlegen. | `assets/screenshots/master-data/abwickler.png` |
| N4 | `master-data/pay-off-machines.md` | Dialog „Neuen Abwickler erstellen" mit „Maße und Grenzen" und „Bauart". | **Neu**, Baureihe ABS, Demo-Maße. | `assets/screenshots/master-data/abwickler-neu-dialog.png` |
| N5 | `master-data/creels.md` | Gatter-Liste als Karten samt Werkzeugleiste. | *Stammdaten > Gatter*; einige Gatter GU, GR anlegen. | `assets/screenshots/master-data/gatter.png` |
| N6 | `master-data/creels.md` | Dialog „Neues Gatter erstellen" mit „Ablaufstellen und Spulen" und „Bauart". | **Neu**, Baureihe GU, Ablaufstellen 8, davon aktiv 4. | `assets/screenshots/master-data/gatter-neu-dialog.png` |
| N7 | `master-data/drums.md` | Seite „Trommeln": Trommeldatenbank links, „Trommel bearbeiten" rechts inkl. „Trommelaufnahme". | Trommeln über **Aus Herzog-Katalog …** übernehmen, eine auswählen. | `assets/screenshots/master-data/trommeln.png` |
| N8 | `catalog/index.md` | Herzog-Katalog, Kachelansicht, Reiter Flechtmaschinen, mit Suche, Baureihe, Kacheln/Liste. | Navigationspunkt **Katalog**, Bilder laden lassen. | `assets/screenshots/catalog/katalog.png` |
| N9 | `catalog/index.md` | Detailfenster einer Flechtmaschine (z. B. KB 1/12-80) mit Kennzahlen, Technischen Daten, Zubehör, „Abzug und Aufnahme". | „KB 1/12-80" suchen, Kachel anklicken. | `assets/screenshots/catalog/katalog-details.png` |
| N10 | `catalog/index.md` | Unterer Teil des Detailfensters: „Als eigene Maschine anlegen" mit Besetzung, Maschinengruppe, Seriennummer, Name, Spulen-Haken; **Zu Flechtmaschinen hinzufügen**. | Flechtmaschine mit mehreren Besetzungen, Arbeitsverzeichnis ohne passende Spule, ans Ende scrollen. | `assets/screenshots/catalog/katalog-anlegen.png` |
| N11 | `orders/braiding-order.md` | Tab „Aufwicklung" mit Aufwickler, Trommel, Seele, **Vorschlag berechnen** und grüner Prüfzeile. | Flechtauftrag mit Auftragslänge, Produkt-Ø und Produktgewicht; **Vorschlag berechnen**. | `assets/screenshots/orders/auftrag-tab-aufwicklung.png` |
