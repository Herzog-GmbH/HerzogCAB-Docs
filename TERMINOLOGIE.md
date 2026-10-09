# Terminologie — Fachwörter Deutsch ↔ Englisch

Verbindlich für das Handbuch in beiden Sprachen (seit 09.10.2026).

**Grundregel:** Im Handbuch heißt alles so wie im Programm. Bedienelemente (Schaltflächen, Reiter, Feldnamen, Menüs) werden **wörtlich** aus der Oberfläche übernommen, im Deutschen aus dem Quelltext, im Englischen aus der englischen Programmübersetzung (`app_en.ts`, Web-App `en.json`). Die vollständige Zuordnung erzeugt `python _tools/begriffe.py <HerzogCAB> <Lizenzserver>` nach `_tools/begriffe_de_en.json`; `_tools/begriffe_handbuch.tsv` listet die fett gesetzten Handbuch-Begriffe mit ihrer Programm-Übersetzung.

Ein Begriff = ein Wort. Keine Synonyme zur Abwechslung.

## Verbotene Wörter

| Nie | Stattdessen (DE) | Stattdessen (EN) |
|---|---|---|
| Hornrad, Hornräder | **Flügelrad**, Flügelräder | **horngear**, horngears |
| horn gear, horn-gear, horn wheel | Flügelrad | **horngear** (ein Wort, auch in „horngear group“, „horngear speed“) |
| Rohrgeflecht | Hohlgeflecht | hollow braid |
| Verlegelänge | Geflechtsdichte | braid density |
| lineare Dichte | Feinheit / Titer | fineness / titer |
| Seillänge, Seilgewicht | Produktlänge, Produktgewicht | product length, product weight |
| Spindel (für den Klöppel) | Klöppel | carrier |
| Hallenplanung, Fabrikplaner | Hallenplaner | Factory Planner |
| machine park | Maschinenpark | Machine Fleet |

## Kernbegriffe

| Deutsch (Programm) | Englisch (Programm / Handbuch) | Hinweis |
|---|---|---|
| Flügelrad | horngear | EN-Programm schreibt teils „horn gear“ — Handbuch immer „horngear“ |
| Flügelradgruppe | horngear group | |
| Flügelraddrehzahl | horngear speed | |
| Klöppel | carrier | |
| Klöppelanzahl | number of carriers | |
| Klöppelnummer | carrier number | |
| Einschnitte | slots | eines Flügelrads |
| Weiche | switch | |
| Teilung | pitch | „Teilung im Lauf“ = „Pitch in this run“ |
| Stich | pitch (Maschinen-Stich) | Feld „Stich“ in den Maschinendaten |
| Flechtmaschine | braiding machine | |
| Spulmaschine | bobbin winding machine | |
| Spulstelle(n) | winding head(s) | |
| Spule | bobbin | |
| Spulvolumen | bobbin volume | |
| Trommel | drum | |
| Aufwickler | take-up winder | |
| Abwickler | pay-off | |
| Gatter | creel | |
| Abzug | take-up | |
| Flechtauftrag | braiding order | |
| Spulauftrag | winding order | |
| Fachung | ply count | im Designer: Fachungsfarben = plying colors |
| Feinheit | fineness | |
| Titer | titer | |
| Dichte | density | |
| Flechtwinkel | braiding angle | |
| Geflechtsdichte | braid density | |
| Schlaglänge | lay length | |
| Bedeckung | covering | |
| Geflechtsart | braid type | |
| Rundgeflecht | round braid | |
| Flachgeflecht | flat braid | |
| Hohlgeflecht | hollow braid | |
| Quadratgeflecht | square braid | |
| Packung | packing | |
| Spirale | spiral | |
| Soutache | soutache | |
| Litze | strand | |
| Kern, Seele | core | |
| Mantel | cover | |
| Kern-Mantel-Produkt | core-cover product | |
| Zettelfaden | axial thread | |
| Mitleitrohr | guide tube | |
| Flechtpunkt | braiding point | |
| Besetzung | setup | Klöppelbesetzung im Designer |
| Gangbahn-Animation | track animation | |
| Flechtbild | braid pattern | |
| Rapport | repeat | |
| Abbindung | interlacing | |
| Tandem | tandem | |
| Verzwirnen | twisting | |
| Zeitprogramm | time program | |
| Schaltplan | switching plan | |
| Wechselräder Gummibandkette | change gears rubber feed device | |
| Fadenspannung | yarn tension | |
| Fadengeschwindigkeit | yarn speed | |
| Spulzeit | winding time | |
| Materialbedarf | material demand | |
| Spulenkapazität | bobbin capacity | |
| Restlänge | residual length | |
| Liefergebinde | supplier spool | |
| Produktdurchmesser / -länge / -gewicht | product diameter / length / weight | |
| Materialdurchmesser | material diameter | |

## Programmbereiche (Navigation)

| Deutsch | Englisch |
|---|---|
| Startseite (Home) | Home page (Home) |
| Aufträge | Orders |
| Maschinenpark | Machine Fleet |
| Herzog-Katalog | Herzog catalogue |
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

## Schreibweise Englisch

Wie im Programm: **catalogue**, **licence** (Substantiv), **color**. Anrede „you“, Imperativ in Anleitungen („Click **Save**“). Menüpfade *File > Settings*.
