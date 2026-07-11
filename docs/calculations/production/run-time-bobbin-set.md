# Maschinenlaufzeit pro Spulensatz

Diese Berechnung beantwortet die zentrale Planungsfrage am Flechter: **Wie lange läuft die Maschine, bis ein voller Spulensatz aufgebraucht ist?** Dazu führt sie drei Teilwerte zusammen – die Fadenlänge auf einer Spule, die Produktionsleistung der Maschine und den Flechtwinkel – und gibt neben der Laufzeit auch die produzierte Seillänge je Spulensatz sowie die Verkürzung durch den Flechtwinkel aus.

!!! note "Drei Teilblöcke, je Block: eingeben oder berechnen"
    Die Seite besteht aus den drei nebeneinanderliegenden Blöcken **Fadenlänge auf Spule**, **Produktionsgeschwindigkeit** und **Flechtwinkel**. Jeder Block hat oben den Umschalter **Wert eingeben | Berechnen**. Bei *Wert eingeben* tragen Sie den Teilwert direkt ein, bei *Berechnen* ermittelt ihn Herzog CAB aus den eingeblendeten Hilfsfeldern. Erst aus allen drei Teilwerten entsteht das Endergebnis.

## Eingabewerte

### Block „Fadenlänge auf Spule"

Im Modus *Berechnen* sichtbar; die Felder hängen von der **Berechnung über:** ab. Im Modus *Wert eingeben* genügt das Feld **Fadenlänge / Spule**.

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Berechnung über:** | – | Berechnungsbasis: *Material*, *Fadendurchmesser*, *Rechteckfaden* oder *Drahtdurchmesser*. |
| **Maschinentype:** | – | Flechtmaschinen-Bauart (*Rundflechtmaschine*, *Quadratflechtmaschine*, *Horizontalflechtmaschine*, *Kohlenstofffaser-Flechtmaschine*, *Drahtflechtmaschine*, *Packungsflechtmaschine*). Steuert die verfügbare Spulenauswahl; bei Basis *Drahtdurchmesser* fest auf *Drahtflechtmaschine* gesetzt. |
| **Spule:** | – | Auswahl eines Spulentyps aus den [Spulen-Stammdaten](../../master-data/bobbins.md). Liefert Außendurchmesser, Kerndurchmesser und Wickellänge. |
| **Material:** | – | Nur bei Basis *Material*: Auswahl aus den [Material-Stammdaten](../../master-data/materials.md). Übernimmt Dichte, Garnstärke und deren Einheit. |
| **Garnstärke:** | tex, dtex, den, Nr_metrisch, Nr_englisch | Nur bei Basis *Material*: Feinheit des Garns (Einheit im Feld rechts daneben). |
| **Dichte:** | g/cm³ | Nur bei Basis *Material*: Materialdichte. |
| **Füllungsgrad:** | % | Nur bei Basis *Material*: Wickel-Füllungsgrad der Spule (Vorbelegung 70 %). |
| **Fachung:** | stk. | Anzahl parallel gewickelter Fäden auf der Spule. |
| **Fadendurchmesser:** | mm | Nur bei Basis *Fadendurchmesser* oder *Drahtdurchmesser*: Durchmesser des Einzelfadens bzw. Drahts. |
| **Rechteckhöhe:** | mm | Nur bei Basis *Rechteckfaden*: Höhe des Rechteckquerschnitts (geht in die Lagenrechnung ein). |
| **Rechteckbreite:** | mm | Nur bei Basis *Rechteckfaden*: Pflichteingabe, geht jedoch **nicht** in die Formel ein. |
| **Fadenlänge / Spule:** | m | Teilwert. Im Modus *Wert eingeben* manuell, im Modus *Berechnen* gesperrt und automatisch gefüllt. |

### Block „Produktionsgeschwindigkeit"

Im Modus *Berechnen* sichtbar; im Modus *Wert eingeben* genügt **Produktionsleistung**.

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Maschinentyp:** | – | Flechtertyp (*RU-Flechter*, *LZ-Flechter*, *ST-Flechter*, *QSE-Flechter*, *SP-Flechter*, *PA2-/PA3-/PA4-Flechter*). Geht in die Berechnung der Produktionsleistung ein. |
| **Flechtbezeichnung:** | – (Einheit wählbar) | Schlaglänge bzw. Flechtdichte. Einheit: *Schlaglänge*, *FL / 10 mm*, *FL / Engl. Zoll*, *FL / Franz. Zoll*. |
| **Klöppelanzahl:** | stk. | Anzahl der Klöppel (mind. 3). |
| **Flügelraddrehzahl:** | u/min | Drehzahl des Flügelrads. |
| **Produktionsleistung:** | m/h | Teilwert. Im Modus *Wert eingeben* manuell, im Modus *Berechnen* gesperrt und automatisch gefüllt. |

### Block „Flechtwinkel"

Im Modus *Berechnen* sichtbar; im Modus *Wert eingeben* genügt **Flechtwinkel**.

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Geflechtsart** | – | *Rundgeflecht* oder *Litzengeflecht*. |
| **Flechtbezeichnung:** | – (Einheit wählbar) | Schlaglänge bzw. Flechtdichte; Einheiten wie oben. |
| **Geflechtsdurchmesser:** | mm | Durchmesser des fertigen Geflechts. |
| **Klöppelanzahl:** | stk. | Nur bei einer FL-pro-Länge-Einheit sichtbar/optional. Fehlt sie, wird die Flechtbezeichnung **immer** als Schlaglänge gewertet. |
| **Flechtwinkel:** | ° | Teilwert. Im Modus *Wert eingeben* manuell, im Modus *Berechnen* gesperrt und automatisch gefüllt. |

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Maschinenlaufzeit:** | h | Laufzeit, bis der Spulensatz aufgebraucht ist (Hauptergebnis). |
| **Seillänge / Spule-Satz:** | m | Aus einem Spulensatz produzierbare Seillänge (Fadenlänge unter Berücksichtigung des Flechtwinkels). |
| **Verkürzung:** | % | Längenverlust gegenüber der reinen Fadenlänge durch den Flechtwinkel. |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

Das Hauptergebnis (**Maschinenlaufzeit**) sowie **Seillänge / Spule-Satz** und **Verkürzung** entstehen aus den drei Teilwerten **Fadenlänge / Spule**, **Produktionsleistung** und **Flechtwinkel**. Ist einer der drei Teilwerte 0 oder kleiner, bleiben die Ergebnisse leer.

!!! tip "Teilwerte je nach Vorwissen mischen"
    Sie müssen nicht alle drei Blöcke rechnen lassen. Kennen Sie z. B. die Produktionsleistung Ihrer Maschine bereits aus der Praxis, stellen Sie diesen Block auf **Wert eingeben** und lassen nur Fadenlänge und Flechtwinkel berechnen. So kombinieren Sie gemessene Erfahrungswerte mit den errechneten Größen.

## Verwandte Berechnungen

* [Produktionsgeschwindigkeit](./production-speed.md) – derselbe Teilwert als eigenständige Berechnung.
* [Flechtwinkel](../braid-geometry/braid-angle.md) – derselbe Teilwert als eigenständige Berechnung.
* [Schlaglänge](../braid-geometry/lay-length.md) – Grundlage der Flechtbezeichnung.
* [Produktlänge](../product/rope-length.md) – produzierbare Länge aus einem Materialvorrat.
* Stammdaten: [Spulen](../../master-data/bobbins.md), [Materialien](../../master-data/materials.md).
