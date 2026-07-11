# Maschinen-Dimensionierung

!!! abstract "Referenz — Berechnung: schätzt Länge und Breite einer Flechtmaschine und zeichnet den Grundriss"

## Wofür

Diese Berechnung liefert eine überschlägige Schätzung der **Aufstellfläche** einer Flechtmaschine – also Länge und Breite des Grundrisses – anhand von Klöppelanzahl, Stichgröße und Bauform. Sie hilft im Flecht-Alltag bei der Stellplatz- und Hallenplanung, bevor die genaue Maschine feststeht. Rechts auf der Seite wird der ermittelte Grundriss zusätzlich als Skizze (Rechteck mit Flechtkreis) gezeichnet.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **einköpfige Maschine / zweiköpfige Maschine** | – | Bauform der Maschine. Auswahl zwischen einköpfig (Standard) und zweiköpfig. Die zweiköpfige Variante belegt zwei Flechtkreise und ergibt eine deutlich größere Länge. |
| **Klöppelanzahl** | stk. | Anzahl der Klöppel der Maschine. Muss mindestens **4** betragen (gültiger Bereich 4 … 1500). |
| **Stichgröße** | mm | Stichgröße (Teilung) der Maschine. Muss größer als 0 sein (bis max. 3000 mm). |

!!! note "Mindestwerte beachten"
    Liegt die Klöppelanzahl unter 4 oder ist die Stichgröße nicht größer als 0, wird kein Ergebnis berechnet und die Ergebnisfelder bleiben leer.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Länge** | cm | Geschätzte Länge des Maschinengrundrisses (eine Nachkommastelle). Bei zweiköpfigen Maschinen entsprechend größer. |
| **Breite** | cm | Geschätzte Breite des Maschinengrundrisses (eine Nachkommastelle). |

## Bedienung

Neben der Eingabekarte zeichnet eine interaktive **Zeichenfläche** den ermittelten Grundriss samt Flechtkreis(en). Darüber stehen zwei Schaltflächen:

* **Reset Zoom** – setzt Zoomstufe und Bildausschnitt der Zeichenfläche zurück.
* **Farbe wählen** – öffnet die Farbauswahl für die aktuell markierte Maschine in der Zeichnung.

Sie können mehrere berechnete Maschinen nacheinander in derselben Zeichenfläche platzieren, einzeln anklicken und verschieben, um eine Hallenbelegung grob zu skizzieren. Die Schaltfläche **Löschen** entfernt dabei nur die gerade **markierten** Maschinen aus der Zeichnung – nicht die Eingabewerte des Formulars. Der allgemeine Aufbau der Berechnungsseiten ist in [So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md) beschrieben.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

Die Schätzung leitet sich aus der Geometrie des Flechtkreises ab; Bauform, Klöppelanzahl und Stichgröße bestimmen Länge und Breite des Grundrisses.

!!! note "Nur Vorwärtsberechnung"
    Diese Funktion rechnet ausschließlich vorwärts: Aus Bauform, Klöppelanzahl und Stichgröße werden Länge und Breite ermittelt. Eine Umkehrung (Rückrechnung eines leeren Eingabefeldes aus den Ergebnissen) ist hier nicht vorgesehen. Die Ergebnisse sind bewusst überschlägig und dienen der Planung, nicht der maßgenauen Konstruktion.

## Verwandte Berechnungen

* [Wechselräder Gummibandkette](change-gears.md)
* [Produktionsgeschwindigkeit](production-speed.md)
* [Maschinenlaufzeit pro Spulensatz](run-time-bobbin-set.md)
* [Hallenplaner](../../hall-planner/index.md)
