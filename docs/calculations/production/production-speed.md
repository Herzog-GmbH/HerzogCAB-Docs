# Produktionsgeschwindigkeit

Berechnet, wie schnell ein Geflecht entsteht – als Längengeschwindigkeit in Metern pro Stunde. Grundlage sind der Maschinentyp, die Flechtbezeichnung (Schlaglänge bzw. Flechten je Längeneinheit), die Flügelraddrehzahl und die Klöppelanzahl. So lässt sich für einen Auftrag abschätzen, wie lange die Maschine für eine bestimmte Produktlänge braucht.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Maschinentyp:** | – | Auswahl des Flechtertyps: *RU-Flechter*, *LZ-Flechter*, *ST-Flechter*, *QSE-Flechter*, *SP-Flechter*, *PA2-Flechter*, *PA3-Flechter*, *PA4-Flechter*. Bestimmt, wie viel Vorschub eine Flügelrad-Umdrehung ergibt. |
| **Flechtbezeichnung:** | je nach Einheit | Beschreibt das Geflecht. Über das Auswahlfeld rechts daneben wird die Einheit gewählt: *Schlaglänge* (Wert ist direkt die Schlaglänge), *FL / 10 mm*, *FL / Engl. Zoll* oder *FL / Franz. Zoll* (Flechten je Längeneinheit). |
| **Flügelraddrehzahl:** | u/min | Drehzahl des Flügelrades. Höchstwert 500 u/min. |
| **Klöppelanzahl:** | stk. | Anzahl der Klöppel. Mindestens 3. Wird zur Vorschubberechnung bei RU-/LZ-Flechtern benötigt sowie zur Umrechnung, wenn die Flechtbezeichnung als Flechten je Längeneinheit angegeben ist. |

!!! note "Pflichtangaben und Grenzen"
    Flechtbezeichnung und Flügelraddrehzahl müssen größer als 0 sein, die Klöppelanzahl mindestens 3. Felder, die diese Grenzen verletzen, werden rot markiert.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Produktionsgeschwindigkeit:** | m/h | Hergestellte Geflechtlänge pro Stunde, auf zwei Nachkommastellen. |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

!!! note "Klöppelanzahl nicht immer nötig"
    Bei *ST-, QSE-, SP-, PA2-, PA3-* und *PA4-Flechtern* mit der Einheit *Schlaglänge* geht die Klöppelanzahl nicht in die Geschwindigkeit ein. Sie wird nur bei RU-/LZ-Flechtern oder bei Eingabe als *Flechten je Längeneinheit* gebraucht. Solange Pflichtwerte fehlen, bleibt das Ergebnisfeld leer.

## Verwandte Berechnungen

* [Maschinenlaufzeit pro Spule-Satz](./run-time-bobbin-set.md)
* [Wechselräder Gummibandkette](./change-gears.md)
* [Geflechtsdichte](../braid-geometry/lay-length.md)
* [Flechtdichte](../braid-geometry/picks-density.md)
