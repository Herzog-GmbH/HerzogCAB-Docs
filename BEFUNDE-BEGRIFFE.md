# Befunde aus der Übersetzung (10/2026)

Gesammelt beim Übersetzen des Handbuchs ins Englische. Abgearbeitet = ~~durchgestrichen~~.

## A. Deutsche Handbuchseiten — weichen vom Programm ab

| Datei:Zeile | Befund |
|---|---|
| ~~calculations/winding/number-of-winders.md:25~~ | ~~„(Hörnerräder)“ — Wort gibt es nicht, raus~~ |
| ~~calculations/product/core-sheath.md:39~~ | ~~„(Horngear)“ englisch im deutschen Text → Flügelrad~~ |
| ~~help/support.md:19,22,29; help/update-errors.md:11,15,19~~ | ~~Menü *Über → …* — das Menü heißt **Hilfe**, Pfade mit `>`~~ (EN-Pfade ebenfalls auf `>`) |
| ~~help/login-problems.md:8,145~~ | ~~Linktext „Anmeldung und Abmelden“ → „Anmelden und Abmelden“~~ (auch H1 von admin/login.md = Navigation, und Links in admin/authentication, index, my-profile, profiles, users) |
| ~~help/license-problems.md:39,55,58,125~~ | ~~Linktext „Lizenz aktivieren“ → „Anmelden und Lizenz beziehen“~~ |
| setup/account.md:65, help/login-problems.md:14 | **Passwort vergessen** → Programm: „Passwort vergessen?“ — **Befund falsch:** beide Stellen meinen den Link auf der Anmeldeseite des **Lizenzportals**, dort heißt er „Passwort vergessen“ (ohne ?, `templates/anmelden.php`); „Passwort vergessen?“ ist nur der Link im Desktop-/Web-Anmeldedialog. DE bleibt; EN auf Portaltext „Forgot password“ korrigiert (auch license-problems.en, activate-license.en). |
| ~~admin/roles.md:82~~ | ~~**Einzelnen Rechte** → „Einzelne Rechte“~~ |
| ~~admin/authentication.md:94, admin/users.md:213~~ | ~~**Gruppe → Rolle** → Programm: „Entra-Gruppe → Rolle“~~ |
| ~~appendix/keyboard-shortcuts.md:33~~ | ~~Design-Bibliothek → Designbibliothek~~ (auch admin/settings/appearance, legacy-import, designer/index, designer/parameters) |
| ~~appendix/keyboard-shortcuts.md:59, basics/guided-tour.md~~ | ~~„Guided Tour“ / „Geführte Touren...“ → **Geführte Touren…**~~ (auch basics/interface, designer/index; EN „Guided Tours…“) |
| ~~appendix/changelog.md:125~~ | ~~Hallenplan → Hallenplaner~~ |
| ~~basics/navigation.md:90–91~~ | ~~Linktexte „Parameter-Übersicht“, „Verwaltung“ ≠ Baum (Parameter Explorer, Systemverwaltung)~~ (dazu „Druck-Editor“ → „Druck Editor“) |
| basics/calc-page-anatomy.md:39 | „Maschinentype“ → Maschinentyp — **teilweise:** Fließtext (Z. 37) korrigiert. Als Feldname bleibt *Maschinentype*, denn das Programm beschriftet das Feld so (`materiallengthonbobbin.cpp:46`, `corecoverropes.cpp:133`, `machinerunningtimeandbobbinset.cpp:113` + `.ui`) — Tippfehler im Programm, dort zuerst beheben. |
| ~~basics/trial-quotas.md:24–26~~ | ~~Badge grün/orange ≤ 30 Tage, Testphase dauert aber nur 30 Tage — Widerspruch~~ (Code `home_page.cpp`: ≤ 7 rot, ≤ 30 orange, sonst grün → bei 30 Tagen Testphase praktisch immer orange/rot; Text danach) |
| ~~print-templates/elements.md:83,136~~ | ~~„Mediathek“ → Medienbibliothek~~ |
| ~~master-data/braiding-machines.md:98~~ | ~~„U/min“ → UpM~~ — Programm zeigt **rpm** (Suffix der Drehzahl-Eingabe, `my_machines.cpp:1838`), daher „rpm“ statt „UpM“ |
| ~~calculations/material/material-length.md:23,27; tubular-braid/tube-cover.md:18~~ | ~~„Nr. metrisch/englisch“, „Stück“ → Nr_metrisch / Nr_englisch / stk.~~ |
| ~~calculations/product/core-sheath.md:42~~ | ~~zitierte Meldung „ergeben nicht 100 %“ gibt es nicht~~ — **Befund falsch:** die Meldung gibt es als Hinweis-Toast (`CoreCoverRopes::outOfRangeMessage`), nur der Wortlaut war falsch → „Die Anteile von Kern und Mantel ergeben zusammen keine 100 %“ / EN „The proportions of the core and cover do not add up to 100%“ |
| ~~orders/index.md (Statustabelle)~~ | ~~Status **Fehler** fehlt~~ (nur Flechtauftrag, `job_editor.cpp:1324`; im Status-Filter und bei Spulaufträgen nicht vorhanden) |
| ~~designer/animation.md~~ | ~~„alle vier Geflechtsarten“ — Designer hat sechs; Spirale/Soutache fehlen~~ (`horngear_overview.cpp`: Besetzungsübersicht + Animation für alle sechs) |
| ~~tasks/design-from-scratch.md:139,155,193~~ | ~~**Design erstellen**, **Bindung/Besetzung**, **3D-Rundansicht** keine Programmtexte~~ → **Neu**, **Laden**, **Geflechtsbindung**, Schalter **3D**; Geflechtsarten-Aufzählung auf sechs, **Rückgängig** → **Zurück** |
| ~~tasks/build-hall.md:221–222,277~~ | ~~Außenwände/Innenwände (Programm Singular), **3D-Ansicht**~~ → Werkzeuge **Außenwand**/**Innenwand**, Ansicht-Schalter **3D** |
| tasks/create-print-template.md:26–27, 90–94 | ~~Druck Editor/Druck-Editor gemischt~~ (Datei vereinheitlicht). TODO „Stand 1.4.5“ **bleibt**: eine Funktion „Vorlage als Standard setzen“ gibt es weiterhin nicht. Hinweis: „Druck-Editor“ steht noch auf ~19 weiteren DE-Seiten (Programm selbst mischt: Navigation „Druck Editor“, `media_library.cpp` „Druck-Editor“). |
| mehrere (master-data/index.md:7, braiding-machines.md:65, media.md:50, print-templates/index.md:18) | Arbeitsbereich / Arbeitsverzeichnis / Workspace gemischt — **offen:** das Programm mischt selbst (Arbeitsbereich ~18×, Arbeitsverzeichnis ~37×, Workspace ~39× in `tr()`); erst Begriff in TERMINOLOGIE.md festlegen (dort „Arbeitsverzeichnis“ / „Workspace-Status“), dann Programm + Handbuch angleichen. |
| ~~calculations/production/dimensions.md:1 (dazu index.md, change-gears.md, Navigation)~~ | ~~„Maschinen-Dimensionierung“ — Programm-Navigation: „Maschinendimensionierung“~~ (10.10.; EN „Machine sizing“) |

## B. Englische Programmübersetzung (`app_en.ts`, Web `en.json`) — uneinheitlich

| Deutsch | Programm EN heute | Soll (TERMINOLOGIE.md) |
|---|---|---|
| ~~Flügelrad, Flügelradgruppe, Flügel-Speichen~~ | ~~„horn gear“ (61×), „Horn spokes“, Web „horn gears“~~ | ~~**horngear**~~ (Desktop 1da5702: „horngear“, „Horngear spokes“; Web: Nachtrag folgt) |
| ~~Klöppel-Tabelle (Auftrag)~~ | ~~„Bobbin Table“~~ | ~~Carrier table~~ (Desktop 1da5702, Handbuch angeglichen) |
| ~~Besetzung (Normale/Halbe/Tandem … 1-1 usw.), Besetzungsübersicht~~ | ~~„occupation“ / „setup“ gemischt~~ | ~~einheitlich~~ → „Setup“, „Normal/Half/Tandem setup …“, „Setup Overview“, „Edit Setup“ (Desktop; Web: Nachtrag folgt) |
| ~~Arbeitsverzeichnis~~ | ~~„Working directory“ / „Workspace folder“~~ | ~~workspace folder~~ (überall „Workspace folder“) |
| Litze, Litzengeflecht | ~~„Lace braid“ / „flat braid“ / „Strand“~~ | umgesetzt: Material (Kern-Mantel, HLM) = „Strand“, Geflechtsart = „Lace braid“ (Druck-Editor „Lace“) — **Entscheidung Eike offen**, siehe TERMINOLOGIE.md |
| ~~Spulvolumen~~ | ~~„Bobbin Volume“ / „Winding volume“~~ | ~~bobbin volume~~ (Trommel-Editor bleibt „Winding volume“) |
| ~~Spulmaschinen~~ | ~~„Bobbin winding machines“ / „winding machines“~~ | ~~einheitlich~~ → „bobbin winding machine(s)“ |
| ~~Abzug (Gatter)~~ | ~~„Take-up“ — beim Gatter ist es ein Abzug über Kopf/rollend~~ | ~~pay-off~~ (Katalog und Gatter-Dialog) |
| ~~Aufwicklung und Abzug (Flechtmaschine)~~ | ~~beide „Take-up“~~ | ~~trennen~~ → Aufwicklung = „Take-up winding“, Abzug = „Take-up“ |
| ~~Stufen (Treppe)~~ | ~~„Stepped“ (Kollision mit Wandanzeige)~~ | ~~Steps~~ (Wandanzeige bleibt „Stepped“) |
| Wiederherstellen (Web, Versionen) | „Redo“ | Restore |
| Größe (Web, Medien) | „Quantity“ | Size |
| ~~Favorisieren~~ | ~~„Favor“~~ | ~~Add to favorites~~ |
| ~~Flechtmaschinen / Spulmaschine~~ | ~~„Bobbin Winders per Braiding Machine“ (Sinn verdreht)~~ | ~~Braiding machines per bobbin winding machine~~ |
| ~~Flechtbezeichnung~~ | ~~„Linear density:“~~ | ~~Braid designation~~ (Feinheit dafür „Fineness“) |
| ~~Laylength~~ | ~~Tippfehler~~ | ~~Lay length~~ |
| ~~SP-Flechter / PA4 / Querrichtung~~ / Geflechtsdurchmesser | ~~je zwei Übersetzungen~~ | ~~einheitlich~~ → „Spiral braider“, „Packing braider, 4 lanes“, „cross direction“; **Geflechtsdurchmesser offen** („Product diameter:“ / „Braid diameter“, Abgleich Desktop/Web läuft) |
| Seilgewicht / Seillänge (Kern-Mantel, Laufzeit) | ~~„Rope weight/length“~~ | EN erledigt („Weight:“, „Product length per bobbin set:“); **DE-Quelltext noch „Seilgewicht:“, „Seillänge / Spule-Satz:“** |
| ~~colour/color, licence/license~~ | ~~gemischt~~ | ~~color, licence~~ (Desktop; dazu catalogue, sonst US-Schreibung; Handbuch-Desktopseiten angeglichen) |
| ~~Neuer Auftrag~~ | ~~„New Job“ (sonst order)~~ | ~~New order~~ (auch „+ New design“) |
| Web `schema.ts` Feldnamen (Hersteller, Einheit der Feinheit, Aussendurchmesser, Flügelrad-Durchmesser, Farbwert, Referenzsystem, Strasse) | ohne Übersetzungsschlüssel → im englischen Web deutsch | übersetzen |

## C. Diagramme ergänzt / vorgeschlagen

Siehe Commit-Liste; Vorschläge der Übersetzer: orders/index (Statusablauf), machine-park (Ampel), catalog (Ablauf), basics/multi-user (Speichern-Konflikt), help/license-problems (Lizenzprüfung beim Start), setup/account (Platz frei/belegt), portal/users (Einladung), admin/settings/license + tasks/desktop-to-web (Cloud-Abgleich), web/versions (Versionen/Papierkorb), hall-planner/index (Grundriss/Belegungen), master-data/take-up-machines (Prüfkette), product/drum-take-up-selection, print-templates (Vorlage → Verwendung).
