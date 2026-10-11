# Terminologie — Fachwörter Deutsch ↔ Englisch

Verbindlich für das Handbuch in beiden Sprachen (seit 09.10.2026; am 10.10.2026 an die abgeglichene englische Übersetzung von Programm und Web-App angepasst: Desktop `fix/begriffe-horngear` 53f2622, Web `fix/uebersetzungen-en` 0c8e00b).

**Grundregel:** Im Handbuch heißt alles so wie im Programm. Bedienelemente (Schaltflächen, Reiter, Feldnamen, Menüs) werden **wörtlich** aus der Oberfläche übernommen, im Deutschen aus dem Quelltext, im Englischen aus der englischen Programmübersetzung (`app_en.ts`, Web-App `web/src/i18n/en.json` + Überschreibungen `web/src/i18n/web/en.json`, Lizenzportal `translations/en.php`). Gleicher deutscher Quelltext hat in Desktop und Web dieselbe Übersetzung; wo ein Wort je nach Stelle anders heißt, trägt der Web-Schlüssel einen Kontext (`"Kontext|Text"`, z. B. `Gatter|Ablauf` = Pay-off). Die vollständige Zuordnung erzeugt `python _tools/begriffe.py <HerzogCAB> <Lizenzserver>` nach `_tools/begriffe_de_en.json`; `_tools/begriffe_handbuch.tsv` listet die fett gesetzten Handbuch-Begriffe mit ihrer Programm-Übersetzung.

Ein Begriff = ein Wort. Keine Synonyme zur Abwechslung.

## Verbotene Wörter

| Nie | Stattdessen (DE) | Stattdessen (EN) |
|---|---|---|
| Hornrad, Hornräder | **Flügelrad**, Flügelräder | **horngear**, horngears |
| horn gear, horn-gear, horn wheel | Flügelrad | **horngear** (ein Wort, auch in „Horngear group“, „horngear speed“) |
| Rohrgeflecht | Hohlgeflecht | hollow braid |
| Verlegelänge | Geflechtsdichte | braid density |
| lineare Dichte, linear density | Feinheit / Titer | fineness / titer (Feld meist **Fineness:** bzw. **Fineness / Titer:**) |
| Seillänge, Seilgewicht | Produktlänge, Produktgewicht | product length, product weight |
| Spindel (für den Klöppel) | Klöppel | carrier |
| Hallenplanung, Fabrikplaner, hall planner | Hallenplaner | Factory Planner |
| machine park, machine fleet (klein) | Maschinenpark | Machine Fleet |
| working directory | Arbeitsverzeichnis | workspace folder |
| occupation (für Besetzung) | Besetzung | setup |
| plying (für Fachung) | Fachung | ply count (nur Fachungsfarben = plying colors) |
| braid angle | Flechtwinkel | braiding angle |
| takeoff disc, take-up wheel, take-off | Abzugsscheibe, Abzug | take-up disc, take-up |
| bobbin winder, winding machine | Spulmaschine | bobbin winding machine |
| flat braid (für das Litzengeflecht) | Litzengeflecht | flat braid |
| transverse direction | Querrichtung | cross direction |
| fill factor, filling degree | Füllgrad, Füllungsgrad | filling grade |
| braid weave, braid configuration | Geflechtsbindung | braid binding |
| standing threads, inlay threads | Stehfäden, Einlegefäden | axial threads |
| timing program | Zeitprogramm | time program |

## Kernbegriffe

| Deutsch (Programm) | Englisch (Programm / Handbuch) | Hinweis |
|---|---|---|
| Flügelrad | horngear | ein Wort, in Programm und Web-App durchgehend |
| Flügelradgruppe | horngear group | als Überschrift/Anfang „Horngear group“ |
| Flügelraddrehzahl | horngear speed | |
| Klöppel | carrier | |
| Klöppelanzahl, Anzahl Klöppel | number of carriers | |
| Klöppelnummer | carrier number | |
| Einschnitte | slots | eines Flügelrads |
| Weiche | switch | |
| Teilung | pitch | „Teilung im Lauf“ = „Pitch in this run“ |
| Stich | pitch (Maschinen-Stich) | Feld „Stich“ in den Maschinendaten |
| Stichgröße | pitch size | Auftrag, Maschinendimensionierung |
| Konstruktionsgeometrie | guide geometry | Maschinenmodelle |
| Radmitten | gear centers | Maschinenmodelle |
| nicht maßstäblich | not to scale | |
| Flechtmaschine | braiding machine | |
| Spulmaschine | bobbin winding machine | auch in Feldnamen: **Bobbin winding machine type:**, **Spindles per bobbin winding machine:**, **Add to bobbin winding machines** |
| Spulmaschinentyp | bobbin winding machine type | |
| Flechtmaschinen / Spulmaschine | braiding machines per bobbin winding machine | Ergebnis „Anzahl Spulmaschinen“ |
| Spulstelle(n) | winding head(s) | |
| Spule | bobbin | |
| Spulvolumen | bobbin volume | auch bei der Trommel (**Bobbin volume [ccm]**; „Spulvolumen der Trommel“ = bobbin volume of the drum); im Fließtext „Wickelvolumen“ = winding volume |
| Trommel | drum | DIN-Trommel = DIN drum |
| Trommelbreite max. / Verlegebreite max. / Spulengewicht max. | Max. drum width / Max. traverse width / Max. bobbin weight | „Max.“ vorn |
| Aufwickler | take-up unit | |
| Aufwicklung | take-up winding | Reiter im Flechtauftrag, Feld bei der Flechtmaschine |
| Abwickler | pay-off unit | |
| Gatter | creel | |
| Abzug (Flechtmaschine) | take-up | Feld bei der Flechtmaschine, Berechnung „Flechtwinkel über Abzug“ |
| Abzugsoption(en) | take-up option(s) | Web-App, Katalog |
| Abzug, Ablauf (Gatter) | pay-off | Ablauf über Kopf / rollend, im Katalog und im Gatter-Dialog |
| Abzugsscheibe | take-up disc | |
| Abzugstabelle | take-up table | Dokumentart bei der Flechtmaschine |
| Flechtauftrag | braiding order | |
| Spulauftrag | winding order | |
| Klöppel-Tabelle | carrier table | Unterreiter im Flechtauftrag |
| Fachung | ply count | im Designer: Fachungsfarben = plying colors |
| Feinheit | fineness | Feld je nach Seite **Fineness:** oder **Fineness / Titer:** (großes T); Kopfzeilen FINENESS / TITER und CONVERSION OF FINENESS / TITER; Navigation „Fineness“ |
| Umrechnung Feinheit | fineness conversion | |
| Titer | titer | im Feldnamen „Titer“ groß |
| Dichte | density | |
| Flechtwinkel | braiding angle | |
| Flechtbezeichnung | braid designation | Schlaglänge oder Flechten je Länge |
| Flechten pro … | picks per … | z. B. Picks per 10 millimeters, Picks / French inch |
| Geflechtsdichte | braid density | |
| Geflechtsdurchmesser | braid diameter | die Rechenseiten beschriften ihr Eingabefeld weiter **Product diameter:** |
| Schlaglänge | lay length | |
| Bedeckung | covering | |
| Füllgrad, Füllungsgrad | filling grade | |
| Querrichtung | cross direction | Bezug des Flechtwinkels |
| Geflechtsart | braid type | |
| Geflechtsbindung | braid binding | |
| Rundgeflecht | round braid | |
| Flachgeflecht | flat braid | nur als Beschreibung; die Geflechtsart heißt Litzengeflecht = flat braid |
| Litzengeflecht, Litze (Geflechtsart) | flat braid | Litzenflechter = flat braider, Litzen-Modus = flat braid, im Druck-Editor kurz „Flat braid“ |
| Hohlgeflecht | hollow braid | |
| Quadratgeflecht | square braid | |
| Packung | packing | |
| Spirale | spiral | |
| SP-Flechter | spiral braider | |
| PA4-Flechter | packing braider, 4 lanes | ebenso PA2/PA3 |
| Soutache | soutache | |
| Litze (Material, Kern-Mantel) | strand | Litzendurchmesser = strand diameter — **Entscheidung Eike**, siehe unten |
| Kern, Seele | core | |
| Mantel | cover | |
| Anteil Seele / Anteil Mantel | core share / cover share | |
| Kern-Mantel-Produkt | core-cover product | |
| Zettelfaden, Stehfäden, Einlegefäden | axial thread(s) | Feldname „Axial threads“ |
| Mitleitrohr | guide tube | |
| Flechtpunkt | braiding point | |
| Besetzung | setup | Klöppelbesetzung im Designer |
| Normale / Halbe / Tandem-Besetzung | normal / half / tandem setup | mit Bindung: „Normal setup 1-1“, „Half setup 1-3“, „Tandem setup 2-2“ |
| Standardbesetzung | default setup | z. B. „Default setup flat braid“; im Fließtext „the default setup“ |
| Besetzungsübersicht | setup overview | Element im Druck-Editor „Setup overview“; im Designer Name des Bereichs |
| Besetzung bearbeiten | Edit setup | Dialog im Druck-Editor |
| Gangbahn-Animation | track animation | |
| Flechtbild | braid pattern | |
| Rapport | repeat | |
| Abbindung | interlacing | |
| Tandem | tandem | |
| Verzwirnen | twisting | |
| Zeitprogramm | time program | |
| Zeitachse | timeline | |
| Schaltplan | switching plan | |
| Wechselräder Gummibandkette | change gears rubber feed device | |
| Fadenspannung | yarn tension | |
| Fadengeschwindigkeit | yarn speed | |
| Spulzeit | winding time | auch „Winding time details…“ im Spulauftrag |
| Materialbedarf | material demand | |
| Spulenkapazität | bobbin capacity | |
| Restlänge | residual length | |
| Liefergebinde | supplier spool | |
| Produktdurchmesser / -länge / -gewicht | product diameter / length / weight | |
| Produktlänge pro Trommel | product length per drum | |
| Produktlänge pro Spulensatz | product length per bobbin set | |
| Materialdurchmesser | material diameter | |
| Materiallänge auf Spule, Fadenlänge auf Spule | material length on bobbin | |
| Maschinenlaufzeit pro Spulensatz | machine runtime per bobbin set | |
| Maschinendimensionierung | machine sizing | Seitenkopf der Berechnung: „Machine dimensions“ |
| einköpfige / zweiköpfige Maschine | single-head / two-head machine | |
| Favorisieren | Add to favorites | Kontextmenü der Navigation, Stern im Web |
| Stufen (Treppe im Hallenplaner) | Steps | Wandanzeige der 3D-Hallenansicht bleibt „Stepped“ |
| Wiederherstellen (Versionen, Papierkorb, Katalogpflege) | Restore | Rückgängig / Wiederholen bleiben Undo / Redo |
| Größe (Medien, Schriftgröße) | Size | |
| Abgleich mit proALPHA | reconciliation with proALPHA | Katalogpflege |
| Demnächst (Startseite) | Coming up | |
| Id | ID | Rollen |

## Programmbereiche (Navigation)

| Deutsch | Englisch |
|---|---|
| Startseite (Home), Web-App „Start“ | Home page (Home), Web-App „Home“ |
| Aufträge | Orders |
| Maschinenpark | Machine Fleet |
| Herzog-Katalog (Navigation: Katalog) | Herzog catalogue (Navigation: Catalogue) |
| Hallenplaner | Factory Planner |
| Hallenansicht | Shop floor view |
| Designer | Designer |
| Berechnungen | Calculations |
| Stammdaten | Master data |
| Druck Editor | Print editor |
| Parameter-Übersicht | Parameter Explorer |
| Maschinenmodelle | Machine models |
| Flechtsimulator | Braiding Simulator |
| Favoriten | Favorites |
| Zuletzt geöffnet | Recently opened |
| Workspace-Status | Workspace status |
| Geführte Touren | Guided Tours |
| Mein Profil | My profile |
| Benutzerverwaltung | User management |
| Rollen | Roles |
| Arbeitsverzeichnis | workspace folder |
| Kundenkonto | customer account |
| Lizenzportal | licence portal |

Rechte: *View Factory Planner*, *Edit Factory Planner* (Programmname groß).

## Schreibweise Englisch

Wie im Programm: **catalogue** und **licence** (Substantiv) britisch, sonst amerikanisch: **color**, **center**, **fiber**, **meter**/**millimeter**, **gray**, **behavior**, **neighbor**, Endungen auf **-ize** (synchronize, recognize). Groß nur am Anfang: *Master data*, *Bobbin volume*, *Material length on bobbin*, *Input table*, *Result table*, *Outer diameter*, *Core diameter*, *Material database*, *Color database*, *Braiding machines*. Eigennamen der Programmbereiche bleiben groß (*Machine Fleet*, *Factory Planner*, *Braiding Simulator*). Anrede „you“, Imperativ in Anleitungen („Click **Save**“). Menüpfade *File > Settings*.

Fremde Oberflächen bleiben wörtlich, z. B. die Schaltfläche **Activate License** im CodeMeter-Kontrollzentrum.

## Entscheidungen (Eike)

| Thema | Stand im Programm und Handbuch (10.10.2026) | Zu entscheiden |
|---|---|---|
| **Litze** | Zwei Bedeutungen, zwei Wörter: Litze als **Material** (Kern-Mantel-Produkt: „Litze:“, „Litzendurchmesser:“; Spulmaschine HLM „Litzenschlag“) = **strand**; Litze als **Geflechtsart** (Litzengeflecht, Litzenflechter, Litzen-Modus, Druck-Editor-Auswahl „Litze“) = **flat braid** bzw. kurz **flat braid**. So umgesetzt in Programm, Web-App und englischem Handbuch. | **Entschieden 11.10.2026 (Eike):** wie auf herzog-online.com — Litzengeflecht = flat braid, Litzenflechtmaschine = flat braiding machine, Litzenschlagmaschine = stranding machine (Litze als Material = strand). Ebenso Aufwickler = take-up unit, Abwickler = pay-off unit (Seite „Pay-off and take-up units“). |
