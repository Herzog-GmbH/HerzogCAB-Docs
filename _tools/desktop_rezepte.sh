nav 243 2500; k -Do "move:1000,600;wait:600;park;wait:1200"; f orders/auftraege-uebersicht.png
k -Do "click:300,176;type:Reepschnur;wait:1200;click:226,931;wait:3500;move:1000,600;park"; f orders/auftrag-editor-kunde.png
for t in "1041 produktion" "1194 aufwicklung" "1346 design"; do set -- $t; k -Do "click:$1,139;wait:1500;park"; f orders/auftrag-tab-$2.png; done
k -Do "click:216,425;wait:1200;park"; f orders/auftrag-tab-design.png
k -Do "click:1396,93;wait:2000;park"; f orders/auftrag-druckvorschau.png -Titel "Druckvorschau|Print preview"; k -Titel "Druckvorschau|Print preview" -Do "keys:%{F4};wait:800"
k -Do "click:123,93;wait:2000"; k -Do "click:300,176;keys:^a{BS};type:A-2026-041;wait:1500;click:600,330;wait:300;click:226,931;wait:3500;move:1000,600;park"; f orders/spulauftrag-editor.png
nav 291 3000; f machine-park/maschinenpark.png
nav 339 3500; k -Do "click:1328,244;wait:2500;park"; f catalog/katalog.png
k -Do "click:500,245;type:KB 1/12-80;wait:1500;click:210,400;wait:2500;park"; T="KB 1/12-80"; k -Titel "$T" -Do "click:58,695;click:58,821;wait:400;park"; f catalog/katalog-details.png -Titel "$T"; k -Titel "$T" -Do "scroll:500,600,-30;wait:800;park"; f catalog/katalog-anlegen.png -Titel "$T"
k -Titel "KB 1/12-80" -Do "click:936,958;wait:600"
nav 387 3500; f master-data/hallenplaner.png
k -Do "click:397,932;wait:4000;click:1519,942;wait:1500;click:754,464;wait:800;park"; f hall-planner/editor-bestueckung.png
k -Do "click:1546,149;wait:5000;park"; k -Titel "Produktionshalle|Production hall" -Do "scroll:550,450,3;wait:1200;park"; f hall-planner/3d-hallenansicht.png -Titel "Produktionshalle|Production hall"; k -Titel "Produktionshalle|Production hall" -Do "keys:%{F4};wait:800"
# Navigation: Stammdaten aufgeklappt, Berechnungen/Favoriten zu. Stammdaten-Eintraege: Designs 623, Farben 663, Flechtmaschinen 703, Grundrisse 743, Kunden 783, Materialien 823, Medien 863
nav 743 2500; f master-data/grundrisse.png
k -Do "click:400,932;wait:4000;click:1519,942;wait:1500;park"
k -Do "click:1519,942;wait:1500;park"; f hall-planner/editor-geometrie.png
for e in 623:master-data/designs-bibliothek 663:master-data/farben-uebersicht 703:master-data/flechtmaschinen 783:master-data/kunden-uebersicht 823:master-data/materialien-uebersicht 863:master-data/medien; do nav ${e%%:*} 2500; f ${e#*:}.png; done
nav 623 2500; k -Do "click:138,278;wait:2000;park"; f master-data/designs-bibliothek.png
nav 783 2500; k -Do "click:200,340;wait:1200;park"; f master-data/kunden-uebersicht.png
# navs = Navigation nach unten gescrollt: Spulen 567, Trommeln 607, Spulmaschinen 647, Aufwickler 687, Abwickler 727, Gatter 767, Druck Editor 811, Systemverwaltung 859
for e in 567:master-data/spulen-uebersicht 607:master-data/trommeln 647:master-data/spulmaschinen 687:master-data/aufwickler 727:master-data/abwickler 767:master-data/gatter; do navs ${e%%:*} 2500; f ${e#*:}.png; done
navs 607 2500; k -Do "click:210,420;wait:1200;park"; f master-data/trommeln.png
# navs-Positionen auch fuer: Designs 287, Farben 327, Flechtmaschinen 367, Grundrisse 407, Kunden 447, Materialien 487, Medien 527
dlg() { navs $1 2500; k -Do "click:128,232;wait:2500;park"; f $2 -Titel "$3"; k -Titel "$3" -Do "keys:{ESC};wait:800"; }
dlg 647 master-data/spulmaschine-neu-dialog.png "Neue Spulmaschine|New bobbin winding|New winding"; dlg 367 master-data/flechtmaschine-neu-dialog.png "Neue Maschine|New machine|New Machine"; dlg 687 master-data/aufwickler-neu-dialog.png "Neuen Aufwickler|take-up"; dlg 727 master-data/abwickler-neu-dialog.png "Neuen Abwickler|pay-off"; dlg 767 master-data/gatter-neu-dialog.png "Neues Gatter|creel"
navs 287 2500; k -Do "click:138,278;wait:1500;dbl:620,502;wait:4000;move:1000,600;park"
k -Do "click:834,155;wait:2500;click:1521,280;wait:4000;park"; f designer/designer-bearbeitungsansicht.png; k -Do "click:1077,155;wait:3500;park"; f designer/designer-3d-ansicht.png; k -Do "click:996,155;wait:2500;click:1521,280;wait:1500;park"; f designer/designer-zylinder-ansicht.png
k -Do "click:834,155;wait:2000;click:1521,280;wait:1000;click:210,400;wait:900;park"; v -Bildschirm; k -Do "keys:{ESC};wait:300"; (cd "$(cygpath -u "$SC")" && python -c "from PIL import Image; Image.open('v.png').crop((55,262,362,945)).save(r'$(cygpath -w "$D/docs/assets/screenshots/designer/designer-parameter-panel$SUF.png")')")
k -Do "click:1409,155;wait:1200;park"; f designer/designer-farbpalette.png -Bildschirm; k -Do "keys:{ESC};wait:300;click:579,155;wait:900;park"; f designer/designer-fachungsfarben.png -Bildschirm; k -Do "keys:{ESC};wait:300"
k -Do "click:1409,155;wait:1200;park"; v -Bildschirm -Plus 400; k -Do "keys:{ESC};wait:300"; (cd "$(cygpath -u "$SC")" && python -c "from PIL import Image, ImageDraw; im=Image.open(\"v.png\").convert(\"RGB\"); pop=im.crop((1374,180,1769,326)); d=ImageDraw.Draw(im); d.rectangle((1600,0,2000,1000),fill=\"white\"); im.paste(pop,(1374,180)); im.crop((1000,60,1790,560)).save(r\"$(cygpath -w "$D/docs/assets/screenshots/designer/designer-farbpalette$SUF.png")\")")  # Popup-Lage pruefen!
k -Do "right:457,394;wait:900;click:540,417;wait:1500"; f designer/designer-fachungsfarben-dialog.png -Titel "Fachungsfarben|Plying colors"; k -Titel "Fachungsfarben|Plying colors" -Do "click:320,330;wait:600"
k -Do "click:1513,231;wait:1500"; f designer/designer-speichern-dialog.png -Titel "Design speichern|Save design"; k -Titel "Design speichern|Save design" -Do "click:307,538;wait:600"
k -Do "click:1437,231;wait:3000"; powershell -ExecutionPolicy Bypass -File "$D/_tools/fenster.ps1" -Titel "Druckvorlage|print template" -Breite 440 -Hoehe 170 -Out "$SC\v.png"; k -Titel "Druckvorlage|print template" -Do "click:200,80;wait:900"; v -Bildschirm; (cd "$(cygpath -u "$SC")" && python -c "from PIL import Image; Image.open(\"v.png\").crop((676,418,1122,566)).save(r\"$(cygpath -w "$D/docs/assets/screenshots/orders/auftrag-druckvorlage-waehlen$SUF.png")\")"); k -Titel "Druckvorlage|print template" -Do "keys:{ESC};wait:300;keys:{ENTER};wait:3000"
f designer/designer-druckvorschau.png -Titel "Druckvorschau|Print preview"; k -Titel "Druckvorschau|Print preview" -Do "keys:%{F4};wait:800"
k -Do "click:210,400;wait:900;click:150,471;wait:2500;park"; v; (cd "$(cygpath -u "$SC")" && python -c "from PIL import Image; Image.open(\"v.png\").crop((66,530,358,942)).save(r\"$(cygpath -w "$D/docs/assets/screenshots/designer/designer-besetzungsuebersicht$SUF.png")\")")
k -Do "click:1551,231;wait:1500"   # Designer schliessen - SPEICHERT OHNE RUECKFRAGE -> danach Musterdesign wiederherstellen:
(cd /c/temp/HerzogCAB_Handbuch/Arbeitsbereich && cp /c/temp/HerzogCAB_Webseite/Arbeitsbereich/809cf44b-2e17-4f1a-b63b-452002f43505.json . && cp /c/temp/HerzogCAB_Webseite/Arbeitsbereich/previews/809cf44b-2e17-4f1a-b63b-452002f43505.png previews/ && rm -rf .verlauf/design/*)   # index.json-Eintrag ebenfalls zuruecksetzen (siehe Sitzung)
k -Do "move:18,500;wait:700;scroll:200,400,10;wait:400"; nav 531 3000; f calculations/berechnungen-uebersicht.png
k -Do "click:498,300;wait:2500;click:850,312;keys:{END}{BS 12};type:45;keys:{TAB};wait:200;click:981,349;wait:300;click:981,349;wait:300;type:8;keys:{TAB};wait:200;type:16;keys:{TAB};wait:300;click:941,631;wait:1500;park"; f calculations/beispiel-feinheit.png
k -Do "click:1580,518;wait:1200;park"; k -Do "click:700,406;wait:200;keys:{HOME}+{END};type:24;keys:{TAB};wait:300;click:829,631;wait:1500;park"; f basics/verlauf-leiste.png
nav 147 3000; f basics/startseite-zweispaltig.png; f basics/hauptfenster.png   # Hauptfenster = dieselbe Ansicht: nach retusche.py die retuschierte startseite-zweispaltig$SUF.png nach hauptfenster$SUF.png kopieren
powershell -ExecutionPolicy Bypass -File "$D/_tools/fenster.ps1" -Breite 2314 -Hoehe 1107 -Out "$SC\v.png"; k -Do "move:1000,600;park;wait:1500"; f basics/startseite.png; powershell -ExecutionPolicy Bypass -File "$D/_tools/fenster.ps1" -Breite 1614 -Hoehe 1007 -Out "$SC\v.png"
# Navigation: nur Systemverwaltung aufgeklappt: Benutzer 719, Rollen 759, Profile 799, Speicherort 839, Firma 879
for e in 719:admin/benutzer-konto 759:users/rollen 799:workspace/profile 839:admin/speicherort 879:settings/firma; do nav ${e%%:*} 2500; f ${e#*:}.png; done
# Firma/Profil sind schon gespeichert (Musterflechterei GmbH) - im EN-Lauf nur aufnehmen
nav 879 2500; f settings/firma.png; nav 839 2500; f admin/speicherort.png; nav 799 2500; f workspace/profile.png
nav 839 2500; k -Do "click:281,325;wait:2500"; f admin/auf-netzlaufwerk-verschieben.png -Titel "Netzlaufwerk|network drive"; k -Titel "Netzlaufwerk|network drive" -Do "click:546,318;wait:800"
k -Do "click:38,46;wait:700;click:92,82;wait:2500"; T="^Einstellungen|^Settings"; f settings/einstellungen-allgemein.png -Titel "$T"
for t in "141 einstellungen-design" "350 webserver" "435 einstellungen-lizenz"; do set -- $t; k -Titel "$T" -Do "click:$1,61;wait:1200;park"; f settings/$2.png -Titel "$T"; done
k -Titel "$T" -Do "keys:{ESC};wait:800"
k -Do "click:164,46;wait:700;click:245,116;wait:2000"; f basics/gefuehrte-touren-dialog.png -Titel "Touren|Tours"; k -Titel "Touren|Tours" -Do "keys:{ESC};wait:600"
k -Do "move:18,500;wait:700;click:200,928;wait:2000"; f admin/mein-profil.png -Titel "Mein Profil|My profile"; k -Titel "Mein Profil|My profile" -Do "keys:{ESC};wait:600;move:1000,600;park"
nav 627 3000; k -Do "click:1456,376;wait:800;click:1400,448;wait:1500;dbl:196,311;wait:1500"; k -Titel "Neue Seite|New page" -Do "click:270,126;wait:2000"; k -Do "click:1456,220;wait:2000"; T='^Auftrag$|^Order$'; f print-templates/tabelle-bearbeiten.png -Titel "$T"
k -Titel "$T" -Do "click:1528,143;type:Durchmesser;wait:1200;park"; v -Titel "$T"; (cd "$(cygpath -u "$SC")" && python -c "from PIL import Image; im=Image.open(\"v.png\"); im.crop((1380,90,im.width,im.height)).save(r\"$(cygpath -w "$D/docs/assets/screenshots/print-templates/feldvorlagen-picker$SUF.png")\")"); k -Titel "$T" -Do "click:1626,762;wait:800"
# EN: Suchbegriff "diameter" statt "Durchmesser"
nav 147 2500; k -Titel "^Druck-Editor$|^Print editor$" -Do "click:376,108;wait:1500"   # Vorlage NICHT speichern (Nein/No)
# --- Neue Motive 11.10.2026 (Einstellungen; Dialog per fenster_setzen.ps1 platzieren, NICHT an der Titelleiste ziehen: Windows-Andocken maximiert ihn) ---
# Allgemein: Datei > Einstellungen; fenster_setzen.ps1 -Titel "^Einstellungen|^Settings" -X 200 -Y 40 -B 776 -H 1180; k -Titel "$T" -Do "click:476,996;wait:1000;park"; f settings/einstellungen-allgemein.png -Titel "$T" -Bildschirm
# Webserver: Port 8080 ist auf diesem Rechner belegt -> Port im Profil (Systemverwaltung > Profile) auf 8095; Reiter Webserver: aktivieren, Wegwerf-Passwort, Speichern;
#   Windows fragt nach der Firewall -> Eike entscheidet (Abbrechen reicht). Erfolgsmeldung haengt ggf. ausserhalb -> fenster_schliessen.ps1 -Titel "^Erfolg|^Success".
#   Dialog -B 776 -H 900, Reiter click:350,61 (DE) / 355,61 (EN), f settings/webserver.png. Danach Passwort entfernen, Webserver aus, Port zurueck (Profilseite zeigt Cache -> profiles.json bei beendetem Programm).
# EN: Designer fragt vor dem Drucken ggf. "Save design" -> ENTER; Auftrag-Druckknopf EN bei click:1442,93; Parameter-Panel EN Ausschnitt (55,262,385,945).
