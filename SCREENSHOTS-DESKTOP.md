# Screenshots Desktop-App — Liste für Eike

Stand: 09.10.2026. Insgesamt **18** Platzhalter auf 10 Seiten.

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

## Loslegen — 9 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 1 | `setup/activate-license.md` | CodeMeter-Tray-Icon im Windows-Infobereich vor und nach dem Einstecken des Dongles (Farbwechsel grau → blau). | Dongle abgezogen fotografieren, dann einstecken und nach ein paar Sekunden erneut fotografieren. | `assets/screenshots/activate-license/tray-icon-farbwechsel.png` |
| 2 | `setup/activate-license.md` | CodeMeter Kontrollzentrum mit erkanntem CmDongle, Firmencode 6001037 und Artikel 88805 in der Lizenzliste. | Dongle einstecken, CodeMeter Kontrollzentrum öffnen, Lizenzliste zeigen. | `assets/screenshots/activate-license/kontrollzentrum-dongle-erkannt.png` |
| 3 | `setup/activate-license.md` | CodeMeter Kontrollzentrum direkt nach dem Doppelklick auf den `.WibuCmLif`-Container — Eintrag „Herzog GmbH", Status „Aktivierung ungültig". | `.WibuCmLif`-Datei doppelklicken, Kontrollzentrum fotografieren. | `assets/screenshots/activate-license/kontrollzentrum-leerer-container.png` |
| 4 | `setup/activate-license.md` | CmFAS-Assistent mit ausgewählter Option „Lizenzanforderung erzeugen". | Im CodeMeter Kontrollzentrum **Lizenz aktivieren** anklicken, ersten Assistenten-Schritt fotografieren. | `assets/screenshots/activate-license/cmfas-lizenzanforderung-erzeugen.png` |
| 5 | `setup/first-run.md` | Dialog „Arbeitsverzeichnis einrichten" mit dem Ordner der Firma, grünem Haken „erreichbar" und der Schaltfläche **Verbinden** | Auf einem zweiten Rechner mit einem Konto, das schon einen Speicherort hat, zum ersten Mal anmelden | `assets/screenshots/setup/arbeitsverzeichnis-verbinden.png` |
| 6 | `setup/first-run.md` | Dialog „Benutzerverwaltung einrichten" mit den Feldern Firma, Login-Name, Anzeigename, E-Mail, Passwort, Passwort bestätigen. | Herzog CAB auf einem Rechner ohne bestehende Benutzerverwaltung starten (leerer `%ProgramData%\Herzog GmbH\Herzog Cab`). | `assets/screenshots/setup/erstadmin-einrichten.png` |
| 7 | `setup/update.md` | Dialog „Update verfügbar" mit Versionsangabe, Was-ist-neu-Liste und den drei Schaltflächen. | *Hilfe > Updates* anklicken, wenn eine neuere Version veröffentlicht ist. | `assets/screenshots/setup/update-dialog.png` |
| 8 | `setup/update.md` | Maintenance-Tool-Assistent im Schritt „Komponenten aktualisieren". | Maintenance-Tool über *Herzog > Herzog CAB Maintenance* öffnen und den Update-Schritt fotografieren. | `assets/screenshots/setup/maintenance-tool-update.png` |
| 9 | `setup/uninstall.md` | Maintenance-Tool-Assistent im Schritt „Alle Komponenten entfernen". | Maintenance-Tool über *Herzog > Herzog CAB Maintenance* öffnen und den Deinstallations-Schritt fotografieren. | `assets/screenshots/setup/maintenance-tool-entfernen.png` |

## Grundlagen — 1 Bild

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 10 | `basics/multi-user.md` | Rückfrage „Materialien“ mit dem Text „Das Material "…" wurde inzwischen von … am Rechner … um … geändert. Die eigenen Änderungen sind noch nicht gespeichert.“ und den Schaltflächen **Überschreiben**, **Als Kopie speichern**, **Neu laden** und **Abbrechen**. | Zwei Programmfenster auf zwei Rechnern (oder zwei Windows-Benutzern) mit demselben Arbeitsverzeichnis; in beiden dasselbe Material öffnen, in Fenster A ändern und speichern, danach in Fenster B ändern und **Speichern** klicken. Musterdaten, Musternamen. | `assets/screenshots/basics/mehrbenutzer-rueckfrage.png` |

## Verwaltung — 6 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 11 | `admin/login.md` | Anmeldefenster „Herzog CAB – Anmelden“ im Kontomodell: blaues Kopfband mit „Herzog CAB“, „Konto: &lt;Firma&gt;“ und dem Zopf rechts; Felder E-Mail-Adresse und Passwort mit Beschriftung darüber, Häkchen „Angemeldet bleiben“, Link „Passwort vergessen?“, Schaltflächen Anmelden und Beenden. | Kunden-Build auf einem am Konto angemeldeten Rechner starten, nachdem der Benutzer sich im Programm abgemeldet hat (sonst startet es dank „Angemeldet bleiben“ ohne Dialog). Musterkonto, keine echte E-Mail-Adresse. | `assets/screenshots/admin/anmelden-konto.png` |
| 12 | `admin/login.md` | Derselbe Dialog im Schritt „Zweiter Faktor“: Kopfband-Unterzeile „Zweiter Faktor“, grüner Haken im Passwortfeld, darunter „Code aus der Authenticator-App“ mit sechs Kästchen in zwei Dreiergruppen (drei Ziffern eingetippt), graue Meldung zur Zwei-Faktor-Anmeldung, Schaltfläche „Bestätigen“. | Mit einem Testbenutzer anmelden, für den im Lizenzportal der zweite Faktor eingerichtet ist; nach **Anmelden** drei Ziffern eintippen und aufnehmen. | `assets/screenshots/admin/anmelden-konto-code.png` |
| 13 | `admin/login.md` | Anmeldefenster „Herzog CAB – Anmelden" mit Logo, Feldern Login/Passwort und der Schaltfläche „Mit Microsoft anmelden" | Herzog CAB mit Dongle starten (Entra-Anmeldung muss unter *Systemverwaltung > Authentifizierung* aktiviert sein, sonst fehlt die Microsoft-Schaltfläche) | `assets/screenshots/admin/anmelden.png` |
| 14 | `admin/users.md` | Benutzerverwaltung bei Dongle-Installation — Benutzerliste links (mit den Schaltflächen „Neuer Benutzer", „Aus Entra importieren", „Aus LDAP importieren"), Benutzer-Editor rechts | Build mit Dongle, *Systemverwaltung > Benutzer* öffnen, einen Benutzer auswählen | `assets/screenshots/admin/benutzer.png` |
| 15 | `admin/authentication.md` | Bildschirm „Authentifizierung", Reiter „Microsoft Entra ID" mit Konfigurationsfeldern und der Tabelle „Entra-Gruppe → Rolle" | *Systemverwaltung > Authentifizierung* öffnen (Reiter Microsoft Entra ID aktiv); Beispieldaten ohne echte Tenant-/Client-IDs verwenden | `assets/screenshots/admin/authentifizierung-entra.png` |
| 16 | `admin/authentication.md` | Bildschirm „Authentifizierung", Reiter „LDAP / Active Directory" mit allen Verbindungsfeldern und der Schaltfläche „Verbindung prüfen" | *Systemverwaltung > Authentifizierung* öffnen, Reiter „LDAP / Active Directory" wählen; Beispieldaten (example.local) verwenden | `assets/screenshots/admin/authentifizierung-ldap.png` |

## Verwaltung › Einstellungen — 2 Bilder

| # | Seite | Motiv | So erzeugen | Ziel-Datei |
|---|---|---|---|---|
| 17 | `admin/settings/appearance.md` | Einstellungen, Tab „Allgemein“ ohne Kopfkarte, mit den Karten Profil, Darstellung, Diagnose, Datenschutz, Produktionsplanung und der neuen Karte „Flechtwinkel“ (Auswahl „Flechtwinkel messen“ aufgeklappt); unten rechts **Speichern** und **Abbrechen**. | *Datei > Einstellungen*, Tab **Allgemein**, Dialog so hoch ziehen, dass alle Karten sichtbar sind; die Auswahl „Flechtwinkel messen“ aufklappen. | `assets/screenshots/settings/einstellungen-allgemein.png` (ersetzt das bisherige Bild)` |
| 18 | `admin/settings/web-server.md` | Einstellungen, Tab „Webserver“ bei laufendem Server mit Passwort: oben „Netzwerk“ (Webserver aktivieren, Port), darunter „Zugangsschutz“ (Passwortfeld mit Platzhalter „Gesetzt – zum Ändern neu eingeben“, Schaltfläche „Passwort entfernen“, Hinweis „Die Weboberfläche ist im Netz erreichbar, nur mit diesem Passwort.“), unten „Live-Status“ mit grünem Punkt, IP-Adressen, QR-Adresse und QR-Code; Speichern/Abbrechen rechts unten. | *Datei > Einstellungen*, Tab **Webserver**; Webserver aktivieren, Testpasswort vergeben, **Speichern**, Dialog erneut öffnen. Interne IP-Adressen dürfen sichtbar sein. | `assets/screenshots/settings/webserver.png` (ersetzt das bisherige Bild)` |

## Alle Desktop-Bestandsbilder — 75 Dateien neu aufnehmen

Alle Bilder der Herzog-CAB-Oberfläche stammen von **vor dem UI-Review (02.10.2026)** und der neuen Startseite (Entwurf 2, 08.10.2026): Seitenkopf als Karte, alte Knopfgrößen und -farben, Navigation ausgeklappt, Menü „Über“. Sie sollten nach denselben Aufnahme-Regeln neu entstehen; die Datei behält ihren Namen. Spalte „Stand“ = letzter Commit der Bilddatei. Bilder, für die schon ein Platzhalter mit derselben Ziel-Datei oben steht, sind hier mit aufgeführt.

| Datei | eingebunden auf | Bildunterschrift | Stand |
|---|---|---|---|
| `assets/screenshots/admin/auf-netzlaufwerk-verschieben.png` | `admin/storage-location.md` | Dialog „Auf Netzlaufwerk verschieben“ mit dem bisherigen Arbeitsverzeichnis und dem Feld für den neuen Ordner | – |
| `assets/screenshots/admin/benutzer-konto.png` | `admin/users.md` | Benutzerverwaltung im Kontomodell: Benutzerliste aus dem Kundenkonto links, Benutzer mit ausgegrauten Stammda… | – |
| `assets/screenshots/admin/mein-profil.png` | `admin/my-profile.md` | Dialog „Mein Profil“, Reiter „Profil“: Anzeigename und E-Mail ausgegraut, darunter „Im Lizenzportal ändern“ | – |
| `assets/screenshots/admin/speicherort.png` | `admin/storage-location.md` | Bildschirm „Speicherort“ mit dem lokalen Arbeitsbereich des aktiven Profils und der Schaltfläche „Auf Netzlau… | – |
| `assets/screenshots/basics/gefuehrte-touren-dialog.png` | `basics/guided-tour.md` | Dialog „Geführte Touren“ mit Themenkarten und der runden Start-Schaltfläche in jeder Karte | – |
| `assets/screenshots/basics/hauptfenster.png` | `basics/interface.md` | Hauptfenster mit eingeklappter Navigation, Menüleiste Datei, Ansicht, Hilfe und der Startseite in voller Brei… | – |
| `assets/screenshots/basics/startseite-zweispaltig.png` | `basics/home.md` | Startseite in zwei Spalten: Aufträge über die volle Breite, darunter Produktion links, Favoriten und Zuletzt… | – |
| `assets/screenshots/basics/startseite.png` | `basics/home.md` | Startseite in drei Spalten: Produktion, Aufträge mit Favoriten, Zuletzt geöffnet mit Workspace-Status | – |
| `assets/screenshots/basics/verlauf-leiste.png` | `basics/history.md` | Berechnung mit geöffneter Verlaufs-Leiste: jede Berechnung erscheint mit Ergebnis und Uhrzeit | – |
| `assets/screenshots/calculations/beispiel-feinheit.png` | `basics/calc-page-anatomy.md`, `calculations/index.md` | Beispiel-Berechnung „Feinheit": Eingabe-Karte, blaue Ergebnis-Kachel mit Einheiten-Platzhalter und die Schalt… | 26.06.2026 |
| `assets/screenshots/calculations/berechnungen-uebersicht.png` | `calculations/index.md` | Berechnungen-Übersicht mit allen Rechnern, gruppiert nach Material, Produkt und Produktion. | 26.06.2026 |
| `assets/screenshots/catalog/katalog-anlegen.png` | `catalog/index.md` | Abschnitt „Als eigene Maschine anlegen“ mit Besetzung, Maschinengruppe, Seriennummer und Name in Flechtmaschi… | – |
| `assets/screenshots/catalog/katalog-details.png` | `catalog/index.md` | Detailfenster der KB 1/12-80 mit Kennzahlen, technischen Daten, Lieferumfang, Zubehör sowie Abzug und Aufnahme | – |
| `assets/screenshots/catalog/katalog.png` | `catalog/index.md` | Herzog-Katalog in der Kachelansicht, Reiter Flechtmaschinen, mit Suchfeld, Baureihenfilter und Umschalter Kac… | – |
| `assets/screenshots/design/designer-start.png` | `designer/index.md` | Designer-Startansicht mit Kurzanleitung links und der Liste „Zuletzt bearbeitet oder gespeichert" rechts. | 26.06.2026 |
| `assets/screenshots/designer/designer-3d-ansicht.png` | `designer/view-3d.md` | Designer in der 3D-Ansicht: zweifarbiges Rundgeflecht als räumliches Modell mit Draufsicht, Seitenansicht und… | – |
| `assets/screenshots/designer/designer-bearbeitungsansicht.png` | `designer/index.md` | Designer mit Rundgeflecht: Werkzeugleiste, links Parameter und Besetzungsübersicht, Mitte Klöppeltabelle, rec… | – |
| `assets/screenshots/designer/designer-besetzungsuebersicht.png` | `designer/animation.md` | Besetzungsübersicht eines Packungsgeflechts mit neun Flügelrädern, eingefärbten Klöppeln und den Animations-S… | – |
| `assets/screenshots/designer/designer-druckvorschau.png` | `designer/save-print.md` | Druckvorschau eines Designs mit Designdaten, Besetzungsübersicht, Klöppeltabelle und Flechtbild | – |
| `assets/screenshots/designer/designer-fachungsfarben-dialog.png` | `designer/painting.md` | Dialog „Fachungsfarben – L3“ mit den Farbknöpfen für Garn 1 bis Garn 3 und „Alle wie Garn 1“ | – |
| `assets/screenshots/designer/designer-fachungsfarben.png` | `designer/painting.md` | Designer mit Rundgeflecht und Fachung 3: Garn-Wähler in der Werkzeugleiste mit geöffnetem Menü Garn 1 bis Gar… | – |
| `assets/screenshots/designer/designer-farbpalette.png` | `designer/painting.md` | Geöffnete Farbpalette mit aktiver Farbe, Auswahl „Standardpalette“, Farbfeldern und Farbrad-Schaltfläche | – |
| `assets/screenshots/designer/designer-parameter-panel.png` | `designer/parameters.md` | Parameter-Panel mit aufgeklappter Auswahlliste Geflechtsart und allen sechs Geflechtsarten | – |
| `assets/screenshots/designer/designer-speichern-dialog.png` | `designer/save-print.md` | Dialog „Design speichern“ mit Designname, Ordnerbaum der Design-Bibliothek und Feld für einen neuen Ordner | – |
| `assets/screenshots/designer/designer-zylinder-ansicht.png` | `designer/view-3d.md` | Designer in der Ansicht Zylinder mit den beiden Schaltflächen „Drehen“ in der Werkzeugleiste | – |
| `assets/screenshots/hall-planner/3d-hallenansicht.png` | `hall-planner/view-3d.md` | 3D-Hallenansicht mit Wänden, Maschinen und farbigen Status-Kugeln, oben die Werkzeugleiste | – |
| `assets/screenshots/hall-planner/editor-bestueckung.png` | `hall-planner/editor.md` | Editor im Bestückungs-Modus: links der Maschinenkatalog, über dem Grundriss die Auswahl-Werkzeugleiste, recht… | – |
| `assets/screenshots/hall-planner/editor-geometrie.png` | `hall-planner/editor.md` | Editor im Geometrie-Modus: links Werkzeuge, Wände, Flächen und Objekte, Mitte der Grundriss, rechts die Eigen… | – |
| `assets/screenshots/machine-park/maschinenpark.png` | `machine-park/index.md` | Maschinenpark in der Kartenansicht mit Filterzeile sowie Aufwicklern, Abwickler und Flechtmaschinen | – |
| `assets/screenshots/master-data/abwickler-neu-dialog.png` | `master-data/pay-off-machines.md` | Dialog „Neuen Abwickler erstellen“ mit Bild und Abschnitt Maschinendaten | – |
| `assets/screenshots/master-data/abwickler.png` | `master-data/pay-off-machines.md` | Seite Abwickler mit Suchfeld, Neu, Bearbeiten, Löschen und einer Abwickler-Karte in der Maschinenliste | – |
| `assets/screenshots/master-data/aufwickler-neu-dialog.png` | `master-data/take-up-machines.md` | Dialog „Neuen Aufwickler erstellen“ mit Bild und Abschnitt Maschinendaten | – |
| `assets/screenshots/master-data/aufwickler.png` | `master-data/take-up-machines.md` | Seite Aufwickler mit drei Karten: Baureihe, Trommel- bzw. Haspelgröße, Traglast und Verlegebreite | – |
| `assets/screenshots/master-data/designs-bibliothek.png` | `master-data/designs.md` | Design-Bibliothek mit Ordnerbaum links, Design-Tabelle mit Vorschaubildern rechts und Werkzeugleiste darüber | – |
| `assets/screenshots/master-data/farben-uebersicht.png` | `master-data/colors.md` | Farben-Editor: links die Farbdatenbank, rechts der Bearbeitungsbereich. | 26.06.2026 |
| `assets/screenshots/master-data/flechtmaschine-neu-dialog.png` | `master-data/braiding-machines.md` | Dialog „Neue Maschine erstellen“ mit Bild und Abschnitt Maschinendaten | – |
| `assets/screenshots/master-data/flechtmaschinen.png` | `master-data/braiding-machines.md` | Flechtmaschinen: Maschinenliste in den Stammdaten. | 26.06.2026 |
| `assets/screenshots/master-data/gatter-neu-dialog.png` | `master-data/creels.md` | Dialog „Neues Gatter erstellen“ mit Bild und Abschnitt Maschinendaten | – |
| `assets/screenshots/master-data/gatter.png` | `master-data/creels.md` | Seite Gatter mit Suchfeld, Schaltflächen und einer Gatter-Karte mit Baureihe und Ablaufstellen | – |
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
| `assets/screenshots/master-data/spulmaschine-neu-dialog.png` | `master-data/winding-machines.md` | Dialog „Neue Spulmaschine erstellen“ mit Bild und Abschnitt Maschinendaten samt Baureihe | – |
| `assets/screenshots/master-data/spulmaschinen.png` | `master-data/winding-machines.md` | Seite Spulmaschinen mit vier Karten: Baureihe, Spulstellen, Spulen-Durchmesser und Drehzahl | – |
| `assets/screenshots/master-data/trommeln.png` | `master-data/drums.md` | Seite Trommeln: links Trommeldatenbank mit Suche und Materialart, rechts „Trommel bearbeiten“ mit Maßen und T… | – |
| `assets/screenshots/orders/auftraege-uebersicht.png` | `orders/index.md` | Auftragsübersicht mit Suche, vier Filtern, Flecht- und Spulaufträgen nach Zeitraum gruppiert und Aktionsleist… | 09.10.2026 |
| `assets/screenshots/orders/auftrag-druckvorlage-waehlen.png` | `orders/print.md` | Dialog „Druckvorlage wählen“ mit aufgeklappter Auswahlliste der Vorlagen | – |
| `assets/screenshots/orders/auftrag-druckvorschau.png` | `orders/print.md` | Druckvorschau eines Auftrags mit Auftrags-, Kunden-, Maschinen- und Produktionsdaten. | 26.06.2026 |
| `assets/screenshots/orders/auftrag-editor-kunde.png` | `orders/braiding-order.md` | Flechtauftrag-Editor mit dem Tab „Kunde" und der Tab-Leiste. | 26.06.2026 |
| `assets/screenshots/orders/auftrag-tab-auftrag.png` | `orders/braiding-order.md` | Tab „Auftrag" mit Name, Nummer, Auftragslänge, Terminen und Status. | 26.06.2026 |
| `assets/screenshots/orders/auftrag-tab-aufwicklung.png` | `orders/braiding-order.md` | Tab „Aufwicklung“ mit gewähltem Aufwickler, gewählter Trommel und dem Abschnitt zur Seele | – |
| `assets/screenshots/orders/auftrag-tab-design.png` | `orders/braiding-order.md` | Tab „Design“ mit verknüpftem Design, Vorschau-Miniatur und geöffneter Klöppel-Tabelle | – |
| `assets/screenshots/orders/auftrag-tab-produkt.png` | `orders/braiding-order.md` | Tab „Produkt" mit den Rechner-Symbolen neben den Feldern. | 26.06.2026 |
| `assets/screenshots/orders/auftrag-tab-produktion.png` | `orders/braiding-order.md` | Tab „Produktion“ mit den Abschnitten Produktionswerte und Hochrechnung auf die Auftragslänge | – |
| `assets/screenshots/orders/auftrag-tab-uebersicht.png` | `orders/braiding-order.md` | Tab „Übersicht" als kompakte Zusammenfassung des Auftrags. | 26.06.2026 |
| `assets/screenshots/orders/spulauftrag-editor.png` | `orders/winding-order.md` | Spulauftrag-Editor mit den Karten „Auftrag“ und „Spulerei — was wird gespult?“ samt Farbaufschlüsselung | – |
| `assets/screenshots/print-templates/druck-editor.png` | `print-templates/editor.md`, `print-templates/index.md`, `print-templates/manage.md`, `print-templates/preview-and-print.md` | Aufbau des Druck-Editors mit den drei Bereichen. | 26.06.2026 |
| `assets/screenshots/print-templates/element-palette.png` | `print-templates/elements.md` | Element-Palette des Druck-Editors mit den Gruppen Datentabellen und Grafische Elemente. | 26.06.2026 |
| `assets/screenshots/print-templates/feldvorlagen-picker.png` | `print-templates/elements.md` | Feldvorlagen-Picker mit Suche, Bereich-Auswahl, Trefferliste und Schaltfläche „Feld einfügen“ | – |
| `assets/screenshots/print-templates/tabelle-bearbeiten.png` | `print-templates/elements.md` | Bearbeitungsdialog der Datentabelle „Auftrag“ mit Parameterzeilen links und Feldvorlagen-Picker rechts | – |
| `assets/screenshots/settings/einstellungen-allgemein.png` | `admin/settings/appearance.md`, `admin/settings/index.md` | Tab „Allgemein" mit Profil, Darstellung, Diagnose und Datenschutz. | 26.06.2026 |
| `assets/screenshots/settings/einstellungen-design.png` | `admin/settings/legacy-import.md` | Tab „Design“ der Einstellungen mit Vorgaben für neue Designs, Vorschau & Ansicht, Animation und Speichern | – |
| `assets/screenshots/settings/einstellungen-lizenz.png` | `admin/settings/license.md` | Tab „Lizenz“ der Einstellungen mit den Karten zum Kundenkonto, Konto und Cloud | – |
| `assets/screenshots/settings/firma.png` | `admin/company.md` | Firma: Logo, Stammdaten sowie Steuer- und Handelsregister-Angaben. | 26.06.2026 |
| `assets/screenshots/setup/arbeitsverzeichnis-festlegen.png` | `setup/first-run.md` | Dialog „Arbeitsverzeichnis einrichten“ auf dem ersten Rechner der Firma | 09.10.2026 |
| `assets/screenshots/setup/konto-anmeldung-geraet.png` | `setup/activate-license.md` | Dialog „Herzog CAB – Anmeldung am Kundenkonto“ mit E-Mail-Adresse, Passwort und „Angemeldet bleiben“ | 09.10.2026 |
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
