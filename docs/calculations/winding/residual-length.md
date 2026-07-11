# Restlänge über Gewicht

!!! abstract "Referenz — Berechnung: Restliche Materiallänge aus dem Gewicht einer angebrochenen Spule"

## Wofür

Diese Berechnung ermittelt, wie viele Meter Material noch auf einer
angebrochenen Spule vorhanden sind. Dazu wiegen Sie die Spule und rechnen
aus dem Gewicht über die Feinheit auf die Restlänge zurück — praktisch, um
Restspulen ohne Abspulen einzuschätzen, etwa bei der Bestandsaufnahme oder
vor der Wiederverwendung einer Spule.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Bruttogewicht (mit Spule):** | g | Verwogenes Gewicht der Spule inklusive Restmaterial, bis zu einer Nachkommastelle. Muss größer als 0 sein. |
| **Leergewicht Spule:** | g | Gewicht der leeren Spule (Hülse/Trommel ohne Material), bis zu einer Nachkommastelle. Bei 0 gilt das Bruttogewicht bereits als Nettogewicht (netto gewogen). Muss kleiner als das Bruttogewicht sein. |
| **Material:** | – | Optionale Auswahl eines Materials aus den [Stammdaten](../../master-data/materials.md). Übernimmt die hinterlegte Feinheit automatisch. |
| **Feinheit:** | tex, dtex, den, Nr_metrisch, Nr_englisch | Feinheit des Materials mit Einheiten-Auswahl daneben. Muss mindestens 1 tex entsprechen. |
| **Fachung:** | stk. | Anzahl der gemeinsam gespulten Einzelfäden (mindestens 1, Startwert 1). |

!!! note "Pflichtfelder"
    Bruttogewicht muss größer als 0 sein, das Leergewicht Spule kleiner als
    das Bruttogewicht. Feinheit (mindestens 1 tex) und Fachung (mindestens
    1) sind ebenfalls Pflicht.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Restlänge:** | m | Hauptergebnis: verbleibende Materiallänge auf der Spule, auf eine Nachkommastelle. |
| **Nettogewicht Material:** | g | Reines Materialgewicht ohne Spulenkörper (Bruttogewicht abzüglich Leergewicht Spule), auf eine Nachkommastelle. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten (Eingabe-Karte,
Ergebnis-Kacheln, Schaltflächen **Berechnen**/**Löschen**, Verlauf) steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md) —
hier nur die Besonderheiten dieser Seite.

!!! tip "Bereits netto gewogen?"
    Haben Sie das Material bereits ohne Spulenkörper gewogen, tragen Sie das
    Gewicht unter **Bruttogewicht (mit Spule)** ein und lassen **Leergewicht
    Spule** auf 0.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

* [Spulengewicht](bobbin-weight.md)
* [Spulen aus Liefergebinde](from-supplier-spool.md)
* [Materialbedarf](material-demand.md)
