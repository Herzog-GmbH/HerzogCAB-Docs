# Spulen aus Liefergebinde

!!! abstract "Referenz — Berechnung: Anzahl Spulen aus einem Liefergebinde"

## Wofür

Diese Berechnung ermittelt, wie viele Spulen sich aus einem Liefergebinde
(z. B. einer Großspule, einem Coil oder Fass vom Lieferanten) bespulen
lassen — angegeben wahlweise über das Gewicht oder direkt über die Länge des
Gebindes. Optional errechnet sie zusätzlich, wie viele Liefergebinde für
eine gewünschte Gesamtzahl an Spulen nötig sind.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Liefergebinde angegeben über:** | – | Grundlage der Angabe: *Gewicht* oder *Länge*. Blendet die passenden Felder darunter ein. |
| **Gewicht Liefergebinde:** | kg | Nur bei Basis *Gewicht*. Gewicht des vollständigen Liefergebindes, bis zu drei Nachkommastellen. Muss größer als 0 sein. |
| **Material:** | – | Nur bei Basis *Gewicht*. Optionale Auswahl eines Materials aus den [Stammdaten](../../master-data/materials.md); übernimmt die hinterlegte Feinheit automatisch. |
| **Feinheit:** | tex, dtex, den, Nr_metrisch, Nr_englisch | Nur bei Basis *Gewicht*. Feinheit des Materials mit Einheiten-Auswahl daneben. Muss mindestens 1 tex entsprechen. |
| **Fachung:** | stk. | Nur bei Basis *Gewicht*. Anzahl der gemeinsam gespulten Einzelfäden (mindestens 1, Startwert 1). |
| **Länge Liefergebinde:** | m | Nur bei Basis *Länge*. Materiallänge des Liefergebindes direkt eingetragen. Muss größer als 0 sein. |
| **Länge pro Spule:** | m | Immer sichtbar. Materiallänge, die auf eine einzelne Spule aufgespult werden soll. Muss größer als 0 sein. |
| **Benötigte Spulen (optional):** | stk. | Immer sichtbar, optional. Zielanzahl an Spulen, für die Sie wissen möchten, wie viele Liefergebinde nötig sind. |

!!! note "Pflichtfelder"
    Länge pro Spule ist immer Pflicht. Je nach Basis zusätzlich Gewicht
    Liefergebinde, Feinheit (mindestens 1 tex) und Fachung (Basis *Gewicht*)
    bzw. Länge Liefergebinde (Basis *Länge*).

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Spulen pro Liefergebinde:** | stk. | Hauptergebnis: Anzahl vollständig bespulbarer Spulen aus dem Liefergebinde, abgerundet (eine angebrochene Spule zählt nicht mit). |
| **Länge Liefergebinde:** | m | Nur bei Basis *Gewicht* sichtbar (aus Gewicht, Feinheit und Fachung errechnet). Bei direkter Längen-Eingabe wird diese Kachel ausgeblendet, da sie redundant wäre. |
| **Benötigte Liefergebinde:** | stk. | Nur sichtbar, wenn **Benötigte Spulen** ausgefüllt ist. Aufgerundete Anzahl an Liefergebinden für die gewünschte Spulenzahl. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten (Eingabe-Karte,
Ergebnis-Kacheln, Schaltflächen **Berechnen**/**Löschen**, Verlauf) steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md) —
hier nur die Besonderheiten dieser Seite.

**Benötigte Spulen** ist ein optionales Zusatzfeld: Bleibt es leer, zeigt
die Seite nur an, wie viele Spulen aus einem Gebinde herauskommen. Tragen
Sie eine Zielanzahl ein, erscheint zusätzlich die Kachel **Benötigte
Liefergebinde**.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

* [Materialbedarf](material-demand.md)
* [Spulenkapazität](bobbin-capacity.md)
* [Restlänge über Gewicht](residual-length.md)
