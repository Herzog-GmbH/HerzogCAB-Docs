# Fadenspannung

!!! abstract "Referenz — Berechnung: Sinnvolle Fadenspannung beim Bespulen"

## Wofür

Diese Berechnung schätzt eine sinnvolle Fadenspannung für den Spulvorgang
ab. Grundlage sind die Feinheit des Materials, die Fachung und ein
Spannungsfaktor, der das übliche Verhältnis von Spannung zu Feinheit
beschreibt. So vermeiden Sie beim Bespulen zu lose gewickelte Spulen
(Fadenverwicklungen) oder zu straff gewickelte Spulen (Materialverzug,
Ballonbildung beim Abspulen).

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Material:** | – | Optionale Auswahl eines Materials aus den [Stammdaten](../../master-data/materials.md). Übernimmt die hinterlegte Feinheit automatisch in das Feld *Feinheit*. |
| **Feinheit:** | tex, dtex, den, Nr_metrisch, Nr_englisch | Feinheit (Titer) des Fadens. Auswahl der Anzeige-Einheit über das Dropdown daneben. Muss mindestens 1 tex entsprechen. |
| **Fachung:** | stk. | Anzahl der zusammen gespulten Einzelfäden (mindestens 1, Startwert 1). |
| **Spannungsfaktor (üblich 0,3–0,7):** | cN/tex | Verhältnis von Fadenspannung zu Feinheit. Startwert 0,5 als gängiger Richtwert. Muss größer als 0 sein (max. 10). |

!!! note "Pflichtfelder"
    Feinheit, Fachung und Spannungsfaktor müssen ausgefüllt und größer als 0
    (Fachung mindestens 1) sein. Fehlt ein Wert, bleibt das Ergebnisfeld
    leer.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Fadenspannung:** | cN | Empfohlene Fadenspannung beim Bespulen, auf eine Nachkommastelle. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten (Eingabe-Karte,
Ergebnis-Kachel, Schaltflächen **Berechnen**/**Löschen**, Verlauf) steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md) —
hier nur die Besonderheiten dieser Seite.

!!! tip "Material aus den Stammdaten übernehmen"
    Wählen Sie oben ein Material aus, wird die **Feinheit** automatisch
    eingetragen. So arbeiten Sie immer mit denselben gepflegten Werten wie
    in den Materialstammdaten.

Der **Spannungsfaktor** ist ein Erfahrungswert. 0,5 ist als Startwert
voreingestellt; je nach Material und Spulmaschine kann ein Wert zwischen 0,3
(empfindliches Material, lockere Spulung) und 0,7 (robustes Material,
straffere Spulung) sinnvoller sein.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

* [Spulengewicht](bobbin-weight.md)
* [Fadengeschwindigkeit](line-speed.md)
* [Spulenkapazität](bobbin-capacity.md)
