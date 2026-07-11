# 3D-Hallenansicht

!!! abstract "Referenz — interaktive dreidimensionale Ansicht der geplanten Halle mit Maschinen, Wänden und Status-Leuchtkugeln"

## Wofür Sie diesen Bereich nutzen

Die 3D-Hallenansicht zeigt das aktuelle Hallenlayout als begehbares
dreidimensionales Modell: Boden, Wände, Flächen, Türen, Tore, Fenster,
Treppen, Banner und alle platzierten Maschinen. Damit prüfen Sie
Raumwirkung, Wege und Sichtachsen — und sehen zugleich über die
Status-Leuchtkugeln, an welchen Maschinen gerade produziert wird oder ein
Fehler anliegt.

## Öffnen und Schließen

Sie öffnen die Ansicht im [Hallenplaner-Editor](editor.md) über den
Ansicht-Schalter **3D** (oben rechts in der Kopf-Werkzeugleiste). Die Halle
erscheint in einem eigenen Fenster mit dem Titel *Produktionshalle 3D —
„Name des Layouts"*. Das Fenster bleibt neben dem Editor geöffnet und übernimmt
Änderungen am Layout laufend. Beim Schließen des Fensters springt der
Ansicht-Schalter im Editor zurück auf **2D**.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** 3D-Hallenansicht mit Wänden, mehreren Maschinen und mindestens einer farbigen Status-Leuchtkugel; oben die dunkle Werkzeugleiste (Kamera zurücksetzen, Wände Voll/Aus/Stufen, Kugeln-Regler, Puls)
    **So erzeugen:** Bestückte Belegung im Editor öffnen > Ansicht-Schalter **3D**; Kamera leicht schräg von oben ausrichten
    **Ziel-Datei:** `assets/screenshots/hall-planner/3d-hallenansicht.png`

## Steuerung mit der Maus

| Aktion | Bedienung |
|---|---|
| **Drehen** (Orbit um den Zielpunkt) | linke Maustaste gedrückt halten und ziehen |
| **Schwenken** (seitlich verschieben) | rechte Maustaste gedrückt halten und ziehen |
| **Zoomen** | Mausrad |

Die wichtigsten Maus-Funktionen stehen als Merkhilfe rechts in der
Werkzeugleiste des Fensters.

## Bedienelemente im Detail

### Kamera zurücksetzen

Stellt den Standard-Blickwinkel wieder her — hilfreich, wenn Sie sich beim
Navigieren „verflogen" haben.

### Wände: Voll / Aus / Stufen

Drei Schaltflächen steuern die Wanddarstellung:

* **Voll** — alle Wände in voller Höhe (Standard).
* **Aus** — Wände ausgeblendet; freier Blick auf die gesamte Aufstellung.
* **Stufen** — blickabhängig: hintere Wände bleiben voll, dem Betrachter
  zugewandte Wände werden stufenweise abgesenkt — Sie schauen in die Halle
  hinein, ohne die Außenkontur zu verlieren.

### Kugeln: Größe und Puls

* **Größen-Regler** — skaliert die Status-Leuchtkugeln über den Maschinen
  (von dezent bis weithin sichtbar, 30 % bis 300 % der Standardgröße).
* **Puls** — schaltet das Pulsieren der Kugeln ein oder aus.

### Status-Leuchtkugeln

Über jeder Maschine, bei der im Editor **Statusampel anzeigen** aktiv ist,
schwebt eine leuchtende Kugel in der Ampelfarbe des aktuellen
Auftragsstatus:

| Farbe | Bedeutung |
|---|---|
| 🔴 Rot | Fehler gemeldet |
| 🟢 Grün | In Produktion |
| 🟡 Gelb | Aufträge warten (freigegeben) |
| ⚪ Grau | Keine aktiven Aufträge |

Die Farblogik ist dieselbe wie im [Maschinenpark](../machine-park/index.md).

## Was dargestellt wird

* **Boden und Flächen** — die im Grundriss gezeichneten Funktionsbereiche.
* **Wände** — mit den im Editor hinterlegten **Wand-Texturen** (innen/außen);
  ohne Textur in neutraler Darstellung. Innenwände erhalten beidseitig die
  Innen-Textur.
* **Bauelemente** — Türen (je nach Türtyp mit Sichtfenster, als Füllungs-
  oder Glastür), Tore, Fenster, Treppen mit ihren Stufen sowie Banner mit dem
  hinterlegten Bild.
* **Maschinen** — als Körper in ihren Stammdaten-Maßen (L × B × H). Sind in
  den Maschinen-Stammdaten **Ansichtsbilder** hinterlegt (Vorder-, Rück-,
  Seiten- und Draufsicht), werden die Seitenflächen damit dargestellt — die
  Maschine ist so auf einen Blick erkennbar. Maschinen ohne gepflegte Maße
  erscheinen mit der Ersatzgröße 2,0 × 1,0 × 1,5 m.

!!! tip "Maschinen erkennbar machen"
    Pflegen Sie in den [Flechtmaschinen](../master-data/braiding-machines.md)-
    bzw. [Spulmaschinen](../master-data/winding-machines.md)-Stammdaten die
    Maße und die Ansichtsbilder der Maschine — beides bestimmt, wie realistisch
    die Halle in 3D wirkt.

## Verwandte Seiten

* [Hallenplaner-Editor](editor.md) — hier entstehen Geometrie und Bestückung;
  dort werden auch die Wand-Texturen hinterlegt.
* [Hallenplaner-Übersicht](index.md) — Grundrisse und Belegungen verwalten.
* [Maschinenpark](../machine-park/index.md) — dieselben Status-Informationen
  als Flotten-Übersicht.
