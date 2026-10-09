# Screenshots Desktop-App — Liste für Eike

Stand: 09.10.2026. Insgesamt **66** Platzhalter auf 39 Seiten.

> Diese Datei erzeugt `python _tools/screenshot_liste.py` aus allen Blöcken `!!! warning "📷 Screenshot fehlt"` unter `docs/`. Nicht von Hand bearbeiten — Ausnahme ist der markierte Abschnitt „veraltete Bestandsbilder“, den das Skript übernimmt.

Jeder Platzhalter steht im Handbuch mit **Motiv**, **So erzeugen** und **Ziel-Datei** (Suche nach „Screenshot fehlt“). Bild unter `docs/<Ziel-Datei>` ablegen und den Platzhalter durch `![<Bildunterschrift>](<relativer Pfad>)` ersetzen, danach dieses Skript erneut laufen lassen.

## Aufnahme-Regeln

* **Helles Theme**, Fensterbreite **ca. 1600 px**, Windows-Skalierung 100 %.
* **Navigation eingeklappt:** vorher den **Pfeil oben in der Navigation** klicken. Der Inhalt bekommt dann die ganze Breite. Die eingeklappte Navigation klappt beim Überfahren mit der Maus wieder auf — Mauszeiger vor der Aufnahme aus dem linken Rand nehmen. (Erst unter 1500 px Fensterbreite klappt sie von selbst ein; bei 1600 px also von Hand.)
* **Musterdaten** „Musterbetrieb“ — keine echten Kunden-, Preis- oder Personendaten, keine echten Tenant-/Client-IDs, keine echten E-Mail-Adressen.
* **Kunden-Build** mit Kontoanmeldung (`CONFIG+=customer CONFIG+=account`), soweit beim Bild nicht anders angegeben (Dongle-Bilder: Build mit CodeMeter). Kein interner Build — der zeigt Einträge, die Kunden nicht haben.
* Aufnahme per Fensteraufnahme ohne Mauszeiger; Annotationen nach STYLEGUIDE.md (blaue Nummernkreise `#00459a`, gelber Fokus-Rahmen `#ffb800`).
* **Web-App- und Portal-Bilder** gehören nicht in diese Liste. Sie entstehen per `_tools/web_screenshots.py` aus der lokalen Testumgebung.

<!-- veraltet:start -->
## Zusätzlich zu ersetzen: veraltete Bestandsbilder mit besonderem Hinweis

Von Hand gepflegt; `_tools/screenshot_liste.py` übernimmt diesen Abschnitt unverändert.

| Datei | Warum | Was drauf sein soll |
|---|---|---|
| `assets/screenshots/orders/auftraege-uebersicht.png` | vor Spulaufträgen aufgenommen | Auftragsübersicht mit Flecht- **und** Spulaufträgen, Filter Auftragsart sichtbar |
| `assets/screenshots/master-data/maschinenpark.png` | vor Spulmaschinen aufgenommen | Maschinenpark mit Flecht- und Spulmaschinen, Typ-Gruppierung und Auftrags-Badges |
| `assets/screenshots/orders/auftrag-editor-kunde.png` | zeigt neun Tabs und den alten Seitenkopf | Flechtauftrag mit zehn Tabs (inkl. „Aufwicklung“) und einzeiliger Kopfzeile — Platzhalter in `orders/braiding-order.md` |
| `assets/screenshots/settings/einstellungen-allgemein.png` | ohne Karten „Produktionsplanung“ und „Flechtwinkel“, alte Kopfkarte, Knöpfe „Sichern/Abbruch“ | Tab Allgemein mit allen Karten, „Speichern/Abbrechen“ rechts — Platzhalter in `admin/settings/appearance.md` |
| `assets/screenshots/settings/webserver.png` | alter Aufbau (Status oben), Passwort „optional“ | Tab Webserver Netzwerk → Zugangsschutz → Live-Status — Platzhalter in `admin/settings/web-server.md` |
| `assets/screenshots/calculations/beispiel-feinheit.png`, `…/berechnungen-uebersicht.png` | Seitenkopf als Karte, alte Knopffarbe | Titelzeile links, Knöpfe in Herzogblau |
| `assets/screenshots/design/designer-canvas.png` | alte Werkzeugleiste (3D-Knopf); **nicht mehr eingebunden** | ersetzt durch `designer/designer-bearbeitungsansicht.png` (Platzhalter in `designer/index.md`) — Datei kann weg |
| `assets/screenshots/getting-started/oberflaeche-home.png` | alte Startseite (bis 2.1.0); **nicht mehr eingebunden** | ersetzt durch `basics/hauptfenster.png` und `basics/startseite.png` (Platzhalter in `basics/interface.md`, `basics/home.md`) — Datei kann weg |
| `assets/screenshots/settings/speicherorte.png` | Tab „Speicherorte“ gibt es nicht mehr; **nicht mehr eingebunden** | entfällt — Datei kann weg |
| `assets/screenshots/users/benutzer.png` | zeigt weder LDAP-Button noch Kontomodell; **nicht mehr eingebunden** | ersetzt durch `admin/benutzer-konto.png` (Kontomodell) und `admin/benutzer.png` (Dongle) — Datei kann weg |
<!-- veraltet:end -->

## Loslegen — 10 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 1 | `setup/activate-license.md` | Dialog „Herzog CAB – Anmeldung am Kundenkonto“ mit blauem Kopfband (Zopf rechts), Erklärtext, den Feldern **E-Mail-Adresse** und **Passwort** (Beschriftung über dem Feld), dem Häkchen **Angemeldet bleiben**, dem Link **Passwort vergessen?** sowie den Schaltflächen **Anmelden** und **Beenden**. | Kunden-Build auf einem Rechner ohne `license.json` starten (oder vorher unter *Einstellungen > Lizenz* **Von diesem Rechner abmelden** wählen). | `assets/screenshots/setup/konto-anmeldung-geraet.png` |
| 2 | `setup/activate-license.md` | CodeMeter-Tray-Icon im Windows-Infobereich vor und nach dem Einstecken des Dongles (Farbwechsel grau → blau). | Dongle abgezogen fotografieren, dann einstecken und nach ein paar Sekunden erneut fotografieren. | `assets/screenshots/activate-license/tray-icon-farbwechsel.png` |
| 3 | `setup/activate-license.md` | CodeMeter Kontrollzentrum mit erkanntem CmDongle, Firmencode 6001037 und Artikel 88805 in der Lizenzliste. | Dongle einstecken, CodeMeter Kontrollzentrum öffnen, Lizenzliste zeigen. | `assets/screenshots/activate-license/kontrollzentrum-dongle-erkannt.png` |
| 4 | `setup/activate-license.md` | CodeMeter Kontrollzentrum direkt nach dem Doppelklick auf den `.WibuCmLif`-Container — Eintrag „Herzog GmbH", Status „Aktivierung ungültig". | `.WibuCmLif`-Datei doppelklicken, Kontrollzentrum fotografieren. | `assets/screenshots/activate-license/kontrollzentrum-leerer-container.png` |
| 5 | `setup/activate-license.md` | CmFAS-Assistent mit ausgewählter Option „Lizenzanforderung erzeugen". | Im CodeMeter Kontrollzentrum **Lizenz aktivieren** anklicken, ersten Assistenten-Schritt fotografieren. | `assets/screenshots/activate-license/cmfas-lizenzanforderung-erzeugen.png` |
| 6 | `setup/first-run.md` | Dialog „Arbeitsverzeichnis einrichten" mit dem Ordner der Firma, grünem Haken „erreichbar" und der Schaltfläche **Verbinden** | Auf einem zweiten Rechner mit einem Konto, das schon einen Speicherort hat, zum ersten Mal anmelden | `assets/screenshots/setup/arbeitsverzeichnis-verbinden.png` |
| 7 | `setup/first-run.md` | Dialog „Benutzerverwaltung einrichten" mit den Feldern Firma, Login-Name, Anzeigename, E-Mail, Passwort, Passwort bestätigen. | Herzog CAB auf einem Rechner ohne bestehende Benutzerverwaltung starten (leerer `%ProgramData%\Herzog GmbH\Herzog Cab`). | `assets/screenshots/setup/erstadmin-einrichten.png` |
| 8 | `setup/update.md` | Dialog „Update verfügbar" mit Versionsangabe, Was-ist-neu-Liste und den drei Schaltflächen. | *Hilfe > Updates* anklicken, wenn eine neuere Version veröffentlicht ist. | `assets/screenshots/setup/update-dialog.png` |
| 9 | `setup/update.md` | Maintenance-Tool-Assistent im Schritt „Komponenten aktualisieren". | Maintenance-Tool über *Herzog > Herzog CAB Maintenance* öffnen und den Update-Schritt fotografieren. | `assets/screenshots/setup/maintenance-tool-update.png` |
| 10 | `setup/uninstall.md` | Maintenance-Tool-Assistent im Schritt „Alle Komponenten entfernen". | Maintenance-Tool über *Herzog > Herzog CAB Maintenance* öffnen und den Deinstallations-Schritt fotografieren. | `assets/screenshots/setup/maintenance-tool-entfernen.png` |

## Grundlagen — 5 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 11 | `basics/interface.md` | Hauptfenster mit eingeklappter Navigation (schmale Symbolleiste links), Titelzeile „Home“ oben links im Inhalt und der Startseite in voller Breite; Menüleiste *Datei · Ansicht · Hilfe*. | Kunden-Build, Fenster ca. 1600 px breit, Pfeil oben in der Navigation klicken, Maus aus dem Navigationsbereich nehmen, *Home* anzeigen. Ersetzt das bisherige Bild `getting-started/oberflaeche-home.png`. | `assets/screenshots/basics/hauptfenster.png` |
| 12 | `basics/home.md` | Startseite in drei Spalten: oben Begrüßung mit Schnellaktionen; links die Karte „Produktion“ als Tabelle mit den Reitern Überfällig/Diese Woche/Demnächst; Mitte „Aufträge“ mit vier Zählern und darunter „Favoriten“-Kacheln; rechts „Zuletzt geöffnet“ mit Symbolen je Berechnung und darunter „Workspace-Status“. | Kunden-Build, Musterbetrieb mit Aufträgen in allen Status und Produktionsdaten in den nächsten 14 Tagen, zwei Favoriten angepinnt, einige Berechnungen gerechnet; Navigation eingeklappt, Fenster so breit wie möglich (die dritte Spalte erscheint erst ab ca. 2000 px Inhaltsbreite — sonst zweispaltig aufnehmen). | `assets/screenshots/basics/startseite.png` |
| 13 | `basics/home.md` | Startseite zweispaltig: „Aufträge“ mit den Zählern über die ganze Breite, links „Produktion“, rechts „Favoriten“ und „Zuletzt geöffnet“, unten „Workspace-Status“. | wie oben, Fenster ca. 1600 px, Navigation eingeklappt. | `assets/screenshots/basics/startseite-zweispaltig.png` |
| 14 | `basics/guided-tour.md` | Dialog „Geführte Touren“ mit den zehn Themenkarten (darunter „Auftragseditor“) und der runden Start-Schaltfläche ▶ unten rechts in jeder Karte | *Hilfe > Geführte Touren…* öffnen, Dialog unverändert aufnehmen | `assets/screenshots/basics/gefuehrte-touren-dialog.png` |
| 15 | `basics/multi-user.md` | Rückfrage „Materialien“ mit dem Text „Das Material "…" wurde inzwischen von … am Rechner … um … geändert. Die eigenen Änderungen sind noch nicht gespeichert.“ und den Schaltflächen **Überschreiben**, **Als Kopie speichern**, **Neu laden** und **Abbrechen**. | Zwei Programmfenster auf zwei Rechnern (oder zwei Windows-Benutzern) mit demselben Arbeitsverzeichnis; in beiden dasselbe Material öffnen, in Fenster A ändern und speichern, danach in Fenster B ändern und **Speichern** klicken. Musterdaten, Musternamen. | `assets/screenshots/basics/mehrbenutzer-rueckfrage.png` |

## Desktop-App › Aufträge — 7 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 16 | `orders/index.md` | Auftragsübersicht mit Suchfeld, den vier Filtern (Auftragsart, Status, Zeitraum, Sortierung), zeitlich gruppierten Auftragskarten (Flecht- und Spulauftrag gemischt, mit Auftragsart-Chips und Verknüpfungszeile) und der Aktionsleiste unten inkl. **Spulauftrag erstellen** | Navigationspunkt *Aufträge* öffnen; Workspace „Musterbetrieb" mit mindestens einem Flechtauftrag samt verknüpftem Spulauftrag; einen Flechtauftrag anwählen, damit alle Schaltflächen aktiv sind | `assets/screenshots/orders/auftraege-uebersicht.png` |
| 17 | `orders/braiding-order.md` | Flechtauftrag-Editor mit der einzeiligen Kopfzeile (links Pfeil **Zur Auftragsliste** und Titel „Auftrag“, rechts **Drucken** und **Auftrag speichern**), darunter die Leiste mit allen zehn Tabs inkl. „Aufwicklung“, Tab „Kunde“ geöffnet; Navigation eingeklappt. | Kunden-Build, Auftragsübersicht, Musterauftrag öffnen. Ersetzt das bisherige Bild `orders/auftrag-editor-kunde.png` (alter Seitenkopf, neun Tabs). | `assets/screenshots/orders/auftrag-editor-kunde.png` |
| 18 | `orders/braiding-order.md` | Tab „Produktion" mit den beiden Abschnitten „Produktionswerte" (links) und „Hochrechnung auf die Auftragslänge" (rechts), inklusive gefüllter berechneter Felder | Flechtauftrag mit Auftragslänge, Maschine, Material, Spule und ausgeführter Laufzeit-Berechnung öffnen; Tab *Produktion* wählen | `assets/screenshots/orders/auftrag-tab-produktion.png` |
| 19 | `orders/braiding-order.md` | Tab „Aufwicklung" mit gewähltem Aufwickler und gewählter Trommel, links die Abschnitte „Aufwickler und Trommel" und „Seele (Kern-Mantel-Seil)" mit der Schaltfläche **Vorschlag berechnen**, rechts „Aufteilung der Auftragslänge" mit grüner Prüfzeile. | Flechtauftrag mit Auftragslänge, Produktdurchmesser und Produktgewicht öffnen (mindestens ein Aufwickler und eine Trommel in den Stammdaten), Tab *Aufwicklung* wählen und **Vorschlag berechnen** klicken. | `assets/screenshots/orders/auftrag-tab-aufwicklung.png` |
| 20 | `orders/braiding-order.md` | Tab „Design" mit verknüpftem Design: Feld „Verknüpftes Design" mit den drei Schaltflächen, Vorschau-Miniatur mit Design-Infos und geöffneter Unter-Tab „Klöppel-Tabelle" mit farbigen Zellen | Flechtauftrag mit verknüpftem mehrfarbigem Design öffnen; Tab *Design*, Unter-Tab *Klöppel-Tabelle* wählen | `assets/screenshots/orders/auftrag-tab-design.png` |
| 21 | `orders/winding-order.md` | Spulauftrag-Editor mit Kopfzeile (**Zur Auftragsübersicht**, **Drucken**, **Spulauftrag speichern**) und den drei Karten „Auftrag", „Spulerei — was wird gespult?" und „Maschinen und Zeitplan" auf einer Scroll-Seite; verknüpfter Flechtauftrag, gefüllte Farbaufschlüsselung und zwei Spulmaschinen in der Verteiltabelle | In der Auftragsübersicht einen Flechtauftrag mit Design anwählen und **Spulauftrag erstellen** klicken; zwei Spulmaschinen hinzufügen, **Spulen gleichmäßig verteilen** | `assets/screenshots/orders/spulauftrag-editor.png` |
| 22 | `orders/print.md` | Dialog „Druckvorlage wählen" mit Auswahlliste (Standardvorlage vorgewählt, eine eigene Vorlage zusätzlich sichtbar) | Im Flechtauftrag-Editor **Drucken** klicken; vorher unter *Druck Editor* eine eigene Auftragsvorlage anlegen, damit der Dialog erscheint | `assets/screenshots/orders/auftrag-druckvorlage-waehlen.png` |

## Desktop-App › Maschinenpark — 1 Bild

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 23 | `machine-park/index.md` | Maschinenpark-Übersicht (Kartenansicht) mit der aktuellen Filterzeile inklusive Filter **Maschinenart** und einem gemischten Park aus Flecht- und Spulmaschinen | *Maschinenpark* öffnen; Datenbestand mit mindestens einer Spulmaschine, damit der Filter „Maschinenart" relevant ist; Kartenansicht aktiv | `assets/screenshots/machine-park/maschinenpark.png` |

## Desktop-App › Herzog-Katalog — 3 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 24 | `catalog/index.md` | Der Herzog-Katalog in der Kachelansicht, Reiter *Flechtmaschinen*, mit Reiterleiste, Suchfeld, Baureihenfilter, Umschalter Kacheln/Liste und Trefferzahl. | Navigationspunkt **Katalog** öffnen, Reiter *Flechtmaschinen* wählen, Ansicht **Kacheln**; warten, bis die Bilder geladen sind. | `assets/screenshots/catalog/katalog.png` |
| 25 | `catalog/index.md` | Das Detailfenster einer Flechtmaschine (z. B. Feindrahtflechtmaschine KB 1/12-80): Bild, Kennzahlen, Technische Daten, Im Lieferumfang, darunter Zubehör zum Ankreuzen und „Abzug und Aufnahme" mit Auswahlkreisen. | Im Katalog Reiter *Flechtmaschinen*, „KB 1/12-80" suchen und die Kachel anklicken. | `assets/screenshots/catalog/katalog-details.png` |
| 26 | `catalog/index.md` | Der untere Teil des Detailfensters: Abschnitt „Als eigene Maschine anlegen" mit Besetzung (drei Felder nebeneinander), Maschinengruppe, Seriennummer, „Name in Flechtmaschinen" und dem Haken „… in die Spulen übernehmen"; unten **Abbrechen** und **Zu Flechtmaschinen hinzufügen**. | Detailfenster einer Flechtmaschine mit mehreren Besetzungen öffnen (Arbeitsverzeichnis ohne passende Spule), zwei Zubehörteile ankreuzen und ans Ende scrollen. | `assets/screenshots/catalog/katalog-anlegen.png` |

## Desktop-App › Hallenplaner — 3 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 27 | `hall-planner/editor.md` | Editor im Geometrie-Modus — links die Werkzeugleiste mit den Gruppen WERKZEUGE, WÄNDE, FLÄCHEN, OBJEKTE; Mitte ein Grundriss mit Wänden und einer farbigen Fläche; rechts das Eigenschaften-Panel (Reiter Layout) | *Stammdaten > Grundrisse* > Grundriss wählen > **Bearbeiten**; ein paar Wände und eine Produktionsfläche zeichnen | `assets/screenshots/hall-planner/editor-geometrie.png` |
| 28 | `hall-planner/editor.md` | Editor im Bestückungs-Modus — links WERKZEUGE + KATALOG mit Maschinenliste; über der Zeichenfläche die Auswahl-Toolbar (Bearbeiten · Ausrichten · Verteilen · Aneinanderreihen); mehrere platzierte Maschinen, davon zwei markiert; rechts das Eigenschaften-Panel mit Maschinen-Eigenschaften | *Hallenplaner* > Grundriss und Belegung wählen > **Bestücken**; zwei Maschinen markieren (Rahmen aufziehen) | `assets/screenshots/hall-planner/editor-bestueckung.png` |
| 29 | `hall-planner/view-3d.md` | 3D-Hallenansicht mit Wänden, mehreren Maschinen und mindestens einer farbigen Status-Leuchtkugel; oben die dunkle Werkzeugleiste (Kamera zurücksetzen, Wände Voll/Aus/Stufen, Kugeln-Regler, Puls) | Bestückte Belegung im Editor öffnen > Ansicht-Schalter **3D**; Kamera leicht schräg von oben ausrichten | `assets/screenshots/hall-planner/3d-hallenansicht.png` |

## Desktop-App › Designer — 10 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 30 | `designer/index.md` | Designer-Bearbeitungsansicht mit geöffnetem Rundgeflecht-Design: Werkzeugleiste oben (mit den Ansichts-Schaltern Voll/Halb/Zylinder/3D), Dokument-Kopfzeile, links Parameter-Panel mit den Auswahllisten Geflechtsart und Geflechtsbindung und der Besetzungsübersicht, Mitte Klöppeltabelle, rechts Flechtbild-Vorschau mit Maßzeile. | *Designer* öffnen, **Neu** klicken, Fenster breit ziehen (Farb- und Texturpalette sichtbar in der Werkzeugleiste), einige Klöppel einfärben. | `assets/screenshots/designer/designer-bearbeitungsansicht.png` |
| 31 | `designer/parameters.md` | Das Parameter-Panel links im Designer mit Designname, den Auswahllisten **Geflechtsart** (aufgeklappt, alle sechs Einträge sichtbar) und **Geflechtsbindung** sowie den Feldern Anzahl Klöppel, Flechtwinkel und Fachung. | *Designer* öffnen, **Neu** klicken; die Liste Geflechtsart aufklappen; nur das linke Panel (oberer Teil bis einschließlich „Fachung") aufnehmen. | `assets/screenshots/designer/designer-parameter-panel.png` |
| 32 | `designer/painting.md` | Werkzeugleiste des Designers mit geöffneter Farbpalette: großes Aktive-Farbe-Quadrat, Paletten-Auswahlliste, Bibliotheksfarben, Benutzerfarben-Reihe und Farbrad-Schaltfläche; daneben die Texturpalette mit großer Vorschau. | *Designer* öffnen, **Neu** klicken, Fenster breit ziehen, damit die Gruppen **Farbe** und **Texturen** in der Werkzeugleiste sichtbar sind. | `assets/screenshots/designer/designer-farbpalette.png` |
| 33 | `designer/painting.md` | Designer mit Rundgeflecht, Fachung 3: in der Werkzeugleiste neben „L“/„R“ der Garn-Wähler mit geöffnetem Menü (Alle Garne, Garn 1 … Garn 3); die Klöppeltabelle zeigt senkrechte Farbstreifen je Garn, das Flechtbild Streifen längs zum Faden mit dünnen Trennlinien. | *Designer*, **Neu**, Rundgeflecht 16 Klöppel, Fachung 3; einige Klöppel schwarz färben, über den Garn-Wähler „Garn 2“ wählen und diese Klöppel rot färben; Menü des Garn-Wählers aufklappen. | `assets/screenshots/designer/designer-fachungsfarben.png` |
| 34 | `designer/painting.md` | Dialog „Fachungsfarben – L3“ mit Hinweistext, Karte „Garne“ mit drei Zeilen „Garn 1 … Garn 3“ und Farbknöpfen (einer aufgeklappt mit Aktive Farbe, Palette, Eigene Farbe wählen…), unten **Alle wie Garn 1**, **Übernehmen** und **Abbrechen**. | wie oben, Rechtsklick auf einen Klöppel in der Klöppeltabelle > **Fachungsfarben…**, Farbknopf von Garn 2 anklicken. | `assets/screenshots/designer/designer-fachungsfarben-dialog.png` |
| 35 | `designer/animation.md` | Besetzungsübersicht eines Packungsgeflechts (3×3 Flügelräder) mit eingefärbten Klöppeln, den Animations-Schaltflächen (Play, langsamer, schneller) oben links und den beiden Farbrotations-Pfeilen darunter. | *Designer* öffnen, **Neu**, Geflechtsart **Packungsgeflecht** (12 Klöppel) wählen, einige Klöppel einfärben; nur die Besetzungsübersicht aufnehmen. | `assets/screenshots/designer/designer-besetzungsuebersicht.png` |
| 36 | `designer/view-3d.md` | Vorschau-Bereich des Designers in der 3D-Ansicht: ein zweifarbiges Rundgeflecht als räumliches Modell, darüber die Ansichtsleiste (Draufsicht / Seitenansicht / Flechtpunkt + Schloss), darunter die Reglerzeile Material / Darstellung / Ausrichtung; in der Werkzeugleiste ist **3D** aktiv. | *Designer* öffnen, Rundgeflecht 24 Klöppel, Linkslauf rot und Rechtslauf blau färben, in der Werkzeugleiste **3D** wählen, Ansicht *Seitenansicht*. | `assets/screenshots/designer/designer-3d-ansicht.png` |
| 37 | `designer/view-3d.md` | Dieselbe Vorschau in der Ansicht **Zylinder** (Projektion), leicht gedreht, mit den Drehpfeilen. | wie oben, Ansicht **Zylinder** wählen und einmal drehen. | `assets/screenshots/designer/designer-zylinder-ansicht.png` |
| 38 | `designer/save-print.md` | Der Dialog **Design speichern** mit Namensfeld, dem Ordnerbaum der Design-Bibliothek (inklusive Eintrag „Ohne Ordner" und Unterordnern), der Zeile „Neuer Ordner (unterhalb der Auswahl)…" mit **Anlegen** sowie den Schaltflächen **Abbrechen** und **Speichern**. | Neues Design anlegen, etwas färben, **Speichern** klicken. | `assets/screenshots/designer/designer-speichern-dialog.png` |
| 39 | `designer/save-print.md` | Druckvorschau-Fenster eines Designs (Standardvorlage): Seite mit Flechtbild, Besetzungsübersicht und Klöppeltabelle, Zoom-Leiste und Drucken-Schaltfläche. | Design mit Farben öffnen, **Drucken** klicken, Vorlage bestätigen. | `assets/screenshots/designer/designer-druckvorschau.png` |

## Desktop-App › Stammdaten — 11 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 40 | `master-data/designs.md` | Die Design-Bibliothek mit Ordnerbaum links, Design-Tabelle rechts (mit Thumbnails) und der Werkzeugleiste darüber. | Navigationspunkt **Designs** öffnen, einen Ordner mit mehreren Beispiel-Designs auswählen (Demo-Daten „Musterbetrieb"). | `assets/screenshots/master-data/designs-bibliothek.png` |
| 41 | `master-data/braiding-machines.md` | Der Dialog *Neue Maschine erstellen* mit Bild, dem Formular „Maschinendaten" und dem Abschnitt „Dokumente". | In **Flechtmaschinen** auf **Neu** klicken und den Dialog mit Demo-Daten „Musterbetrieb" ausfüllen. | `assets/screenshots/master-data/flechtmaschine-neu-dialog.png` |
| 42 | `master-data/winding-machines.md` | Die Spulmaschinen-Liste als Karten (mit Baureihe, Spulstellen, Spulen-Durchmesser und Drehzahl) samt Werkzeugleiste. | Navigationspunkt **Spulmaschinen** öffnen, einige Beispiel-Spulmaschinen der Baureihen SP/SPA/HLM (Demo-Daten „Musterbetrieb") anlegen. | `assets/screenshots/master-data/spulmaschinen.png` |
| 43 | `master-data/winding-machines.md` | Der Dialog *Neue Spulmaschine erstellen* mit Baureihenauswahl und dem Abschnitt „Wickeltechnik". | In **Spulmaschinen** auf **Neu** klicken; als Baureihe einmal SPA (zeigt den Abschnitt „Automatischer Spulenwechsel") und einmal HLM (zeigt „Litzenschlag") wählen. | `assets/screenshots/master-data/spulmaschine-neu-dialog.png` |
| 44 | `master-data/drums.md` | Die Seite *Trommeln*: links die Trommeldatenbank mit Suche, Filter „Materialart" und Trommel-Karten, rechts „Trommel bearbeiten" mit allen Maßfeldern und dem Abschnitt „Trommelaufnahme". | *Stammdaten > Trommeln* öffnen, einige Trommeln über **Aus Herzog-Katalog …** übernehmen und eine davon auswählen. | `assets/screenshots/master-data/trommeln.png` |
| 45 | `master-data/take-up-machines.md` | Die Aufwickler-Liste als Karten (Bild, Baureihe, „Trommel bis Ø … mm", Traglast und Verlegebreite) samt Werkzeugleiste. | Navigationspunkt *Stammdaten > Aufwickler* öffnen; einige Aufwickler der Baureihen AW, AWS und AWH (Demo-Daten „Musterbetrieb") anlegen, einen davon mit Haspel. | `assets/screenshots/master-data/aufwickler.png` |
| 46 | `master-data/take-up-machines.md` | Der Dialog *Neuen Aufwickler erstellen* mit den Abschnitten „Maschinendaten", „Maße und Grenzen" und „Bauart". | In *Stammdaten > Aufwickler* auf **Neu** klicken, Baureihe **AWS** wählen und die Maße mit Demo-Werten füllen; bis zum Abschnitt „Bauart" scrollen. | `assets/screenshots/master-data/aufwickler-neu-dialog.png` |
| 47 | `master-data/pay-off-machines.md` | Die Abwickler-Liste als Karten (Bild, Baureihe, „Trommel bis Ø … mm", Traglast und Trommelbreite) samt Werkzeugleiste. | Navigationspunkt *Stammdaten > Abwickler* öffnen; einige Abwickler der Baureihen AB und ABS (Demo-Daten „Musterbetrieb") anlegen. | `assets/screenshots/master-data/abwickler.png` |
| 48 | `master-data/pay-off-machines.md` | Der Dialog *Neuen Abwickler erstellen* mit den Abschnitten „Maschinendaten", „Maße und Grenzen" und „Bauart". | In *Stammdaten > Abwickler* auf **Neu** klicken, Baureihe **ABS** wählen und die Maße mit Demo-Werten füllen. | `assets/screenshots/master-data/abwickler-neu-dialog.png` |
| 49 | `master-data/creels.md` | Die Gatter-Liste als Karten (Bild, Baureihe, „… Ablaufstellen", Abzug und Spulengröße) samt Werkzeugleiste. | Navigationspunkt *Stammdaten > Gatter* öffnen; einige Gatter der Baureihen GU und GR (Demo-Daten „Musterbetrieb") anlegen. | `assets/screenshots/master-data/gatter.png` |
| 50 | `master-data/creels.md` | Der Dialog *Neues Gatter erstellen* mit den Abschnitten „Ablaufstellen und Spulen" und „Bauart" (Fadenspannung, Überwachung, Material als Ankreuzfelder). | In *Stammdaten > Gatter* auf **Neu** klicken, Baureihe **GU** wählen, Ablaufstellen 8, davon aktiv 4 eintragen und bis „Bauart" scrollen. | `assets/screenshots/master-data/gatter-neu-dialog.png` |

## Desktop-App › Druck-Editor — 2 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 51 | `print-templates/elements.md` | Der Bearbeitungsdialog einer Datentabelle (z. B. „Auftrag“) mit der Zeilen-Werkzeugleiste links und dem Feldvorlagen-Picker rechts. | Druck-Editor öffnen, eine Datentabelle wie „Auftrag“ auf die Seite ziehen, per Doppelklick öffnen. | `assets/screenshots/print-templates/tabelle-bearbeiten.png` |
| 52 | `print-templates/elements.md` | Der Feldvorlagen-Picker (Suche, Bereich-Auswahl, Liste, Schaltfläche „Feld einfügen“) im geöffneten Zustand mit ein paar Suchtreffern. | Bearbeitungsdialog einer Datentabelle öffnen, im Suchfeld einen Begriff eintippen (z. B. „Durchmesser“). | `assets/screenshots/print-templates/feldvorlagen-picker.png` |

## Verwaltung — 10 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 53 | `admin/login.md` | Anmeldefenster „Herzog CAB – Anmelden“ im Kontomodell: blaues Kopfband mit „Herzog CAB“, „Konto: &lt;Firma&gt;“ und dem Zopf rechts; Felder E-Mail-Adresse und Passwort mit Beschriftung darüber, Häkchen „Angemeldet bleiben“, Link „Passwort vergessen?“, Schaltflächen Anmelden und Beenden. | Kunden-Build auf einem am Konto angemeldeten Rechner starten, nachdem der Benutzer sich im Programm abgemeldet hat (sonst startet es dank „Angemeldet bleiben“ ohne Dialog). Musterkonto, keine echte E-Mail-Adresse. | `assets/screenshots/admin/anmelden-konto.png` |
| 54 | `admin/login.md` | Derselbe Dialog im Schritt „Zweiter Faktor“: Kopfband-Unterzeile „Zweiter Faktor“, grüner Haken im Passwortfeld, darunter „Code aus der Authenticator-App“ mit sechs Kästchen in zwei Dreiergruppen (drei Ziffern eingetippt), graue Meldung zur Zwei-Faktor-Anmeldung, Schaltfläche „Bestätigen“. | Mit einem Testbenutzer anmelden, für den im Lizenzportal der zweite Faktor eingerichtet ist; nach **Anmelden** drei Ziffern eintippen und aufnehmen. | `assets/screenshots/admin/anmelden-konto-code.png` |
| 55 | `admin/login.md` | Anmeldefenster „Herzog CAB – Anmelden" mit Logo, Feldern Login/Passwort und der Schaltfläche „Mit Microsoft anmelden" | Herzog CAB mit Dongle starten (Entra-Anmeldung muss unter *Systemverwaltung > Authentifizierung* aktiviert sein, sonst fehlt die Microsoft-Schaltfläche) | `assets/screenshots/admin/anmelden.png` |
| 56 | `admin/users.md` | Benutzerverwaltung im Kontomodell — Benutzerliste links mit dem Hinweistext „Benutzer, Passwörter und Rollen kommen aus dem Kundenkonto …" und den Schaltflächen „Vom Kundenkonto aktualisieren" und „Lizenzportal öffnen", Benutzer-Editor rechts mit ausgegrauten Stammdatenfeldern und der Infozeile „Kontobenutzer (Lizenzserver)" | Kunden-Build mit Kontoanmeldung, *Systemverwaltung > Benutzer* öffnen, einen Benutzer auswählen | `assets/screenshots/admin/benutzer-konto.png` |
| 57 | `admin/users.md` | Benutzerverwaltung bei Dongle-Installation — Benutzerliste links (mit den Schaltflächen „Neuer Benutzer", „Aus Entra importieren", „Aus LDAP importieren"), Benutzer-Editor rechts | Build mit Dongle, *Systemverwaltung > Benutzer* öffnen, einen Benutzer auswählen | `assets/screenshots/admin/benutzer.png` |
| 58 | `admin/authentication.md` | Bildschirm „Authentifizierung", Reiter „Microsoft Entra ID" mit Konfigurationsfeldern und der Tabelle „Entra-Gruppe → Rolle" | *Systemverwaltung > Authentifizierung* öffnen (Reiter Microsoft Entra ID aktiv); Beispieldaten ohne echte Tenant-/Client-IDs verwenden | `assets/screenshots/admin/authentifizierung-entra.png` |
| 59 | `admin/authentication.md` | Bildschirm „Authentifizierung", Reiter „LDAP / Active Directory" mit allen Verbindungsfeldern und der Schaltfläche „Verbindung prüfen" | *Systemverwaltung > Authentifizierung* öffnen, Reiter „LDAP / Active Directory" wählen; Beispieldaten (example.local) verwenden | `assets/screenshots/admin/authentifizierung-ldap.png` |
| 60 | `admin/my-profile.md` | Dialog „Mein Profil“, Reiter „Profil“ eines Kontobenutzers: rundes Profilbild bzw. Initialen, ausgegraute Felder Anzeigename und E-Mail, darunter der Hinweis „Name und E-Mail-Adresse gehören zum Kundenbenutzer …“ und die Schaltfläche **Im Lizenzportal ändern**. | Kunden-Build mit Kontoanmeldung (Musterbenutzer), unten links in der Navigation auf die eigene Benutzerkarte klicken. | `assets/screenshots/admin/mein-profil.png` |
| 61 | `admin/storage-location.md` | Bildschirm „Speicherort" mit Badge NETZWERK/LOKAL, Pfad der zentralen Benutzerdaten und Abschnitt „Arbeitsbereich (aktives Profil)" | *Systemverwaltung > Speicherort* öffnen | `assets/screenshots/admin/speicherort.png` |
| 62 | `admin/storage-location.md` | Dialog „Auf Netzlaufwerk verschieben" mit bisherigem Ordner, Anzahl Dateien und Größe, eingetragenem neuen Ordner | *Systemverwaltung > Speicherort* bei lokalem Arbeitsverzeichnis, **Auf Netzlaufwerk verschieben …** | `assets/screenshots/admin/auf-netzlaufwerk-verschieben.png` |

## Verwaltung › Einstellungen — 4 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 63 | `admin/settings/appearance.md` | Einstellungen, Tab „Allgemein“ ohne Kopfkarte, mit den Karten Profil, Darstellung, Diagnose, Datenschutz, Produktionsplanung und der neuen Karte „Flechtwinkel“ (Auswahl „Flechtwinkel messen“ aufgeklappt); unten rechts **Speichern** und **Abbrechen**. | *Datei > Einstellungen*, Tab **Allgemein**, Dialog so hoch ziehen, dass alle Karten sichtbar sind; die Auswahl „Flechtwinkel messen“ aufklappen. | `assets/screenshots/settings/einstellungen-allgemein.png` (ersetzt das bisherige Bild)` |
| 64 | `admin/settings/legacy-import.md` | Tab „Design" des Einstellungen-Dialogs mit den Karten „Vorgaben für neue Designs", „Vorschau & Ansicht", „Animation", „Speichern" und „Legacy-Designimport". | *Datei > Einstellungen*, Tab **Design**, Dialog so hoch ziehen, dass alle fünf Karten sichtbar sind. | `assets/screenshots/settings/einstellungen-design.png` |
| 65 | `admin/settings/license.md` | Tab „Lizenz" mit den drei Karten „Lizenz – Kundenkonto (Lizenzserver)", „Konto" und „Cloud (app.herzog-cab.com)"; Konto, Benutzer, Edition, Bausteine, Miete und Plätze gefüllt, Cloud-Schalter aktiv. | Kunden-Build mit Kontoanmeldung, *Datei > Einstellungen*, Tab **Lizenz**. | `assets/screenshots/settings/einstellungen-lizenz.png` |
| 66 | `admin/settings/web-server.md` | Einstellungen, Tab „Webserver“ bei laufendem Server mit Passwort: oben „Netzwerk“ (Webserver aktivieren, Port), darunter „Zugangsschutz“ (Passwortfeld mit Platzhalter „Gesetzt – zum Ändern neu eingeben“, Schaltfläche „Passwort entfernen“, Hinweis „Die Weboberfläche ist im Netz erreichbar, nur mit diesem Passwort.“), unten „Live-Status“ mit grünem Punkt, IP-Adressen, QR-Adresse und QR-Code; Speichern/Abbrechen rechts unten. | *Datei > Einstellungen*, Tab **Webserver**; Webserver aktivieren, Testpasswort vergeben, **Speichern**, Dialog erneut öffnen. Interne IP-Adressen dürfen sichtbar sein. | `assets/screenshots/settings/webserver.png` (ersetzt das bisherige Bild)` |

## Alle Desktop-Bestandsbilder — 26 Dateien neu aufnehmen

Alle Bilder der Herzog-CAB-Oberfläche stammen von **vor dem UI-Review (02.10.2026)** und der neuen Startseite (Entwurf 2, 08.10.2026): Seitenkopf als Karte, alte Knopfgrößen und -farben, Navigation ausgeklappt, Menü „Über“. Sie sollten nach denselben Aufnahme-Regeln neu entstehen; die Datei behält ihren Namen. Spalte „Stand“ = letzter Commit der Bilddatei. Bilder, für die schon ein Platzhalter mit derselben Ziel-Datei oben steht, sind hier mit aufgeführt.

| Datei | eingebunden auf | Bildunterschrift | Stand |
|---|---|---|---|
| `assets/screenshots/calculations/beispiel-feinheit.png` | `basics/calc-page-anatomy.md`, `calculations/index.md` | Beispiel-Berechnung „Feinheit": Eingabe-Karte, blaue Ergebnis-Kachel mit Einheiten-Platzhalter und die Schalt… | 26.06.2026 |
| `assets/screenshots/calculations/berechnungen-uebersicht.png` | `calculations/index.md` | Berechnungen-Übersicht mit allen Rechnern, gruppiert nach Material, Produkt und Produktion. | 26.06.2026 |
| `assets/screenshots/design/designer-start.png` | `designer/index.md` | Designer-Startansicht mit Kurzanleitung links und der Liste „Zuletzt bearbeitet oder gespeichert" rechts. | 26.06.2026 |
| `assets/screenshots/master-data/farben-uebersicht.png` | `master-data/colors.md` | Farben-Editor: links die Farbdatenbank, rechts der Bearbeitungsbereich. | 26.06.2026 |
| `assets/screenshots/master-data/flechtmaschinen.png` | `master-data/braiding-machines.md` | Flechtmaschinen: Maschinenliste in den Stammdaten. | 26.06.2026 |
| `assets/screenshots/master-data/grundrisse.png` | `master-data/floor-plans.md` | Grundrisse: Liste links, Grundriss-Ansicht rechts. | 26.06.2026 |
| `assets/screenshots/master-data/hallenplaner.png` | `hall-planner/index.md` | Hallenplaner-Übersicht: Grundriss-Liste links, rechts Belegungs-Pillenleiste, Vorschau, zugewiesene Maschinen… | 26.06.2026 |
| `assets/screenshots/master-data/kunden-uebersicht.png` | `master-data/customers.md` | Kunden-Modul: links die Kundendatenbank, rechts der Bearbeitungsbereich. | 26.06.2026 |
| `assets/screenshots/master-data/maschine-detail.png` | `machine-park/index.md` | Maschinen-Detailseite mit Kopfbereich, Status-Pille und zugewiesenen Aufträgen. | 26.06.2026 |
| `assets/screenshots/master-data/maschinenpark.png` | `machine-park/index.md` | Maschinenpark: Flotten-Übersicht mit Suchfeld, Filterzeile und Maschinenkarten mit Status-Ampel. | 26.06.2026 |
| `assets/screenshots/master-data/materialien-neu-dialog.png` | `master-data/materials.md` | Dialog „Neues Material in der Datenbank anlegen". | 26.06.2026 |
| `assets/screenshots/master-data/materialien-uebersicht.png` | `master-data/index.md`, `master-data/materials.md` | Stammdaten-Übersicht mit den Kacheln aller Stammdatenbereiche. | 26.06.2026 |
| `assets/screenshots/master-data/medien.png` | `master-data/media.md` | Medienbibliothek: Ordner links, Vorschau-Galerie rechts. | 26.06.2026 |
| `assets/screenshots/master-data/parameter-uebersicht.png` | `parameter-overview/index.md` | Parameter-Übersicht: Baumtabelle aller Parameter mit Wert, Quelle, Typ und Beschreibung. | 26.06.2026 |
| `assets/screenshots/master-data/spulen-uebersicht.png` | `master-data/bobbins.md` | Spulen-Editor: links die Spulendatenbank, rechts der Bearbeitungsbereich. | 26.06.2026 |
| `assets/screenshots/orders/auftrag-druckvorschau.png` | `orders/print.md` | Druckvorschau eines Auftrags mit Auftrags-, Kunden-, Maschinen- und Produktionsdaten. | 26.06.2026 |
| `assets/screenshots/orders/auftrag-editor-kunde.png` | `orders/braiding-order.md` | Flechtauftrag-Editor mit dem Tab „Kunde" und der Tab-Leiste. | 26.06.2026 |
| `assets/screenshots/orders/auftrag-tab-auftrag.png` | `orders/braiding-order.md` | Tab „Auftrag" mit Name, Nummer, Auftragslänge, Terminen und Status. | 26.06.2026 |
| `assets/screenshots/orders/auftrag-tab-produkt.png` | `orders/braiding-order.md` | Tab „Produkt" mit den Rechner-Symbolen neben den Feldern. | 26.06.2026 |
| `assets/screenshots/orders/auftrag-tab-uebersicht.png` | `orders/braiding-order.md` | Tab „Übersicht" als kompakte Zusammenfassung des Auftrags. | 26.06.2026 |
| `assets/screenshots/print-templates/druck-editor.png` | `print-templates/editor.md`, `print-templates/index.md`, `print-templates/manage.md`, `print-templates/preview-and-print.md` | Aufbau des Druck-Editors mit den drei Bereichen. | 26.06.2026 |
| `assets/screenshots/print-templates/element-palette.png` | `print-templates/elements.md` | Element-Palette des Druck-Editors mit den Gruppen Datentabellen und Grafische Elemente. | 26.06.2026 |
| `assets/screenshots/settings/einstellungen-allgemein.png` | `admin/settings/appearance.md`, `admin/settings/index.md` | Tab „Allgemein" mit Profil, Darstellung, Diagnose und Datenschutz. | 26.06.2026 |
| `assets/screenshots/settings/firma.png` | `admin/company.md` | Firma: Logo, Stammdaten sowie Steuer- und Handelsregister-Angaben. | 26.06.2026 |
| `assets/screenshots/users/rollen.png` | `admin/roles.md` | Rollen-Verwaltung: Rollenliste links, Rechte-Auswahl rechts. | 26.06.2026 |
| `assets/screenshots/workspace/profile.png` | `admin/profiles.md` | Profilverwaltung: Profilliste links, Profil-Einstellungen rechts. | 26.06.2026 |

## Bilder fremder Programme — 16 Dateien, nicht betroffen

CodeMeter-, Wibu- und Installer-Bilder zeigen keine Herzog-CAB-Oberfläche; das UI-Review betrifft sie nicht. Neu aufnehmen nur, wenn sich das jeweilige Programm ändert.

| Datei | eingebunden auf | Bildunterschrift | Stand |
|---|---|---|---|
| `assets/screenshots/activate-license/cmfas-lizenzaktualisierung-einspielen.png` | `setup/activate-license.md` | CmFAS-Assistent mit ausgewählter Option „Lizenzaktualisierung einspielen". | 26.05.2026 |
| `assets/screenshots/activate-license/kontrollzentrum-vor-aktivierung.png` | `setup/activate-license.md` | CodeMeter Kontrollzentrum mit CmActLicense-Container, bereit für die Aktivierung über den Button „Lizenz akti… | 26.05.2026 |
| `assets/screenshots/codemeter/setup-1-willkommen.png` | `setup/codemeter.md` | CodeMeter Runtime Kit Setup - Willkommen-Bildschirm. | 26.05.2026 |
| `assets/screenshots/codemeter/setup-2-lizenz.png` | `setup/codemeter.md` | Endbenutzer-Lizenzvertrag mit Häkchen bestätigt. | 26.05.2026 |
| `assets/screenshots/codemeter/setup-3-komponenten.png` | `setup/codemeter.md` | Benutzerdefiniertes Setup mit Komponenten-Auswahl, inklusive Netzwerk-Server. | 26.05.2026 |
| `assets/screenshots/codemeter/setup-4-installieren.png` | `setup/codemeter.md` | Bereit zum Installieren - Setup-Assistent vor dem Start. | 26.05.2026 |
| `assets/screenshots/codemeter/tray-und-kontrollzentrum.png` | `setup/codemeter.md` | CodeMeter Kontrollzentrum mit leerer Lizenzliste; das Tray-Symbol ist im Windows-Infobereich sichtbar. | 26.05.2026 |
| `assets/screenshots/codemeter/usb-stick-inhalt.png` | `setup/codemeter.md` | Inhalt des mitgelieferten USB-Sticks: CodeMeterRuntime.exe, HerzogCAB-Installer und eine Installations-PDF. | 26.05.2026 |
| `assets/screenshots/codemeter/wibu-download.png` | `setup/codemeter.md` | Wibu-Download-Seite mit CodeMeter User Runtime für Windows. | 26.05.2026 |
| `assets/screenshots/installer/1-willkommen.png` | `setup/installer.md` | Willkommen zum Herzog CAB-Einrichtungsassistenten. | 26.05.2026 |
| `assets/screenshots/installer/2-installationsordner.png` | `setup/installer.md` | Installationsordner mit Vorgabe C:\\Program Files\\Herzog\\HerzogCAB. | 26.05.2026 |
| `assets/screenshots/installer/3-komponenten.png` | `setup/installer.md` | Komponentenauswahl mit Herzog Cab Main Component. | 26.05.2026 |
| `assets/screenshots/installer/4-lizenzabkommen.png` | `setup/installer.md` | Lizenzabkommen mit Häkchen 'Ich akzeptiere die Lizenzvereinbarung'. | 26.05.2026 |
| `assets/screenshots/installer/5-startmenue.png` | `setup/installer.md` | Auswahl des Startmenü-Ordners mit Vorgabe 'Herzog'. | 26.05.2026 |
| `assets/screenshots/installer/6-bereit.png` | `setup/installer.md` | Bereit zum Installieren - Bestätigungsseite vor dem Start. | 26.05.2026 |
| `assets/screenshots/installer/7-abschliessen.png` | `setup/installer.md` | Den Herzog CAB-Assistent abschließen. | 26.05.2026 |
