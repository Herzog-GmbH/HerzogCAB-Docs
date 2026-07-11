# Maschinen-Dimensionierung

Diese Berechnung liefert eine überschlägige Schätzung der **Aufstellfläche** einer Flechtmaschine – also Länge und Breite des Grundrisses – anhand von Klöppelanzahl, Stichgröße und Bauform. Sie hilft im Flecht-Alltag bei der Stellplatz- und Hallenplanung, bevor die genaue Maschine feststeht. Rechts auf der Seite wird der ermittelte Grundriss zusätzlich als Skizze (Rechteck mit Flechtkreis) gezeichnet.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **einköpfige Maschine / zweiköpfige Maschine** | – | Bauform der Maschine. Auswahl zwischen einköpfig (Standard) und zweiköpfig. Die zweiköpfige Variante belegt zwei Flechtkreise und ergibt eine deutlich größere Länge. |
| **Klöppelanzahl:** | stk. | Anzahl der Klöppel der Maschine. Muss mindestens **4** betragen (gültiger Bereich 4 … 1500). |
| **Stichgröße:** | mm | Stichgröße (Teilung) der Maschine. Muss größer als 0 sein (bis max. 3000 mm). |

!!! note "Mindestwerte beachten"
    Liegt die Klöppelanzahl unter 4 oder ist die Stichgröße nicht größer als 0, wird kein Ergebnis berechnet und die Ergebnisfelder bleiben leer.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Länge:** | cm | Geschätzte Länge des Maschinengrundrisses (eine Nachkommastelle). Bei zweiköpfigen Maschinen entsprechend größer. |
| **Breite:** | cm | Geschätzte Breite des Maschinengrundrisses (eine Nachkommastelle). |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

Die Schätzung leitet sich aus der Geometrie des Flechtkreises ab; Bauform, Klöppelanzahl und Stichgröße bestimmen Länge und Breite des Grundrisses. Für die Skizze rechts wird zusätzlich ein Flechtkreis gezeichnet – bei einer zweiköpfigen Maschine zwei, bei einer einköpfigen einer.

!!! note "Nur Vorwärtsberechnung"
    Diese Funktion rechnet ausschließlich vorwärts: Aus Bauform, Klöppelanzahl und Stichgröße werden Länge und Breite ermittelt. Eine Umkehrung (Rückrechnung eines leeren Eingabefeldes aus den Ergebnissen) ist hier nicht vorgesehen. Die Ergebnisse sind bewusst überschlägig und dienen der Planung, nicht der maßgenauen Konstruktion.

!!! tip "Skizze nutzen"
    Über die Zeichenfläche rechts können Sie den ermittelten Grundriss verschieben, mehrere Maschinen nebeneinander darstellen, die Farbe des Flechtkreises ändern (**Farbe wählen**) und die Ansicht mit **Reset Zoom** zurücksetzen. So lässt sich eine Hallenbelegung schnell grob skizzieren.

## Verwandte Berechnungen

* [Wechselräder Gummibandkette](./change-gears.md)
* [Produktionsgeschwindigkeit](./production-speed.md)
* [Maschinenlaufzeit pro Spule-Satz](./run-time-bobbin-set.md)
