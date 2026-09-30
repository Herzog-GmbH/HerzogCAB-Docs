# Produktlänge pro Trommel

!!! abstract "Referenz — Berechnung: aufwickelbare Produktlänge auf eine Trommel"

## Wofür

Diese Berechnung ermittelt, wie viel Produkt (Seil, Litze, Geflecht) auf
eine Trommel aufgewickelt werden kann. Aus den Maßen der gewählten Trommel
und dem Produktdurchmesser wird die gesamte aufgewickelte Länge in Metern
bestimmt – nützlich für die Planung von Trommelgrößen, Liefermengen und
Wickelaufträgen.

!!! info "Geändert in Version 2.1.0"
    Die Seite fragt keine Trommelmaße mehr ab (früher *Außendurchmesser*,
    *Kerndurchmesser* und *Wickellänge*), sondern wählt die Trommel aus den
    [Trommel-Stammdaten](../../master-data/drums.md). Die Maße kommen aus
    dem Datensatz. Neue Arbeitsverzeichnisse starten ohne Trommeln —
    übernehmen Sie sie dort mit **Aus Herzog-Katalog …** oder legen Sie
    eigene an.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Trommel:** | – | Trommel aus den [Trommel-Stammdaten](../../master-data/drums.md). Gerechnet wird mit ihrem Wickeldurchmesser (sonst dem Außendurchmesser), ihrem Kerndurchmesser und ihrer Verlegeweite (sonst der Trommelbreite). |
| **Produktdurchmesser:** | mm | Durchmesser eines einzelnen aufgewickelten Stranges (zwei Nachkommastellen). |
| **Fachung:** | stk. | Anzahl der nebeneinander gemeinsam aufgewickelten Stränge. |

!!! note "Pflichtangaben"
    Die gewählte Trommel braucht einen Außen- bzw. Wickeldurchmesser, einen
    Kerndurchmesser und eine Verlegeweite (oder Trommelbreite); der Kern muss
    kleiner sein als der Wickeldurchmesser. Der Produktdurchmesser muss
    größer als null sein, die Fachung mindestens **1 stk.** Fehlende oder
    ungültige Eingaben werden rot markiert; ohne vollständige Werte bleibt
    das Ergebnis leer.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Produktlänge:** | m | Gesamte aufgewickelte Produktlänge, die unter den Maßen der Trommel auf sie passt. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md).

Die Auswahlliste **Trommel** zeigt die Bezeichnung jeder Trommel, ohne
Bezeichnung ihre Maßzeile. Sie wird beim Öffnen der Seite neu geladen;
Trommeln, die Sie inzwischen angelegt oder geändert haben, stehen also
bereit.

Werden mehrere Stränge gleichzeitig nebeneinander aufgewickelt (Fachung > 1),
teilt sich die verfügbare Wickelbreite auf alle Stränge auf – die Länge pro
Strang sinkt entsprechend.

!!! tip "Trommel und Aufwickler vorschlagen lassen"
    Welche Trommeln für eine bestimmte Produktlänge nötig sind und welcher
    Aufwickler sie trägt, ermittelt die Berechnung
    [Trommel- und Aufwicklerwahl](drum-take-up-selection.md).

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

- [Trommel- und Aufwicklerwahl](drum-take-up-selection.md)
- [Produktgewicht](rope-weight.md)
- [Materialdurchmesser über Material](../material/material-diameter.md)
- [Produktlänge](rope-length.md)
