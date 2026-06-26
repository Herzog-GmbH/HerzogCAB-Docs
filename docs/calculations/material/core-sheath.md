# Kern-Mantel-Produkt

Berechnet ein zweilagiges Flechtprodukt aus einer geflochtenen **Seele (Kern)** und einem darüber geführten **Mantel**. Aus Außendurchmesser, der prozentualen Aufteilung zwischen Seele und Mantel sowie den Flechtparametern beider Lagen ermittelt die Funktion Geometrie, Litzenfeinheit, Spulenlängen, Produktion und Gewicht – getrennt für Kern und Mantel sowie als Gesamtwert. So lässt sich ein Kern-Mantel-Seil in einem Schritt vollständig durchkalkulieren.

## Eingabewerte

Die Eingaben sind in drei Bereiche gegliedert: gemeinsame **Produkt**-Daten sowie zwei gleich aufgebaute Panels für **Seele** und **Mantel**.

### Produkt

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Außendurchmesser** | mm | Fertiger Außendurchmesser des kompletten Kern-Mantel-Produkts. |
| **Füllungsgrad** | % | Wie dicht der Querschnitt mit Material gefüllt ist (Materialanteil gegenüber dem theoretisch verfügbaren Querschnitt). |

### Seele und Mantel (je Panel identisch)

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Maschinentype** | – | Auswahl der Flechtmaschinenart (Rundflechtmaschine, Quadratflechtmaschine, Horizontalflechtmaschine, Kohlenstofffaser-Flechtmaschine, Drahtflechtmaschine, Packungsflechtmaschine). |
| **Spule** | – | Auswahl einer Spule aus den Stammdaten (passend zur gewählten Maschinentype). Liefert Außendurchmesser, Kerndurchmesser und Wickellänge der Spule für die Längenberechnung. |
| **Material** | – | Optionale Auswahl eines Materials aus den Stammdaten; die **Dichte** wird daraus automatisch übernommen. |
| **Dichte** | g/cm³ | Materialdichte (drei Nachkommastellen). Wird bei Materialauswahl gefüllt, ist aber auch manuell überschreibbar. |
| **Anteil Seele** bzw. **Anteil Mantel** | % | Querschnittsanteil der jeweiligen Lage am Gesamtprodukt. **Anteil Seele + Anteil Mantel müssen zusammen 100 % ergeben.** |
| **Flechtwinkel** | ° | Flechtwinkel der Lage. |
| **Anzahl Klöppel** | stk. | Anzahl der Klöppel der Maschine (Seele ≥ 1, Mantel ≥ 3). |
| **Fachung pro Klöppel** | stk. | Anzahl der parallel laufenden Fäden/Litzen je Klöppel. |
| **Flügelrad-Drehzahl** | rpm | Drehzahl des Flügelrads (Horngear) der Maschine. |

!!! note "Anteile müssen 100 % ergeben"
    Weichen **Anteil Seele** und **Anteil Mantel** zusammen um mehr als 0,01 % von 100 % ab, meldet die Berechnung *„Die Anteile von Kern und Mantel ergeben nicht 100 %"* und markiert beide Anteilsfelder.

## Ergebnis

Spitzenwerte sind **Leistung (Gesamt)** und **Seilgewicht (Gesamt)**; darunter werden **Seeldurchmesser** und **Mantelstärke** sowie alle übrigen Werte paarweise für Kern und Mantel ausgewiesen.

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Leistung (Gesamt)** | kg/h | Gesamtdurchsatz des Produkts in Masse pro Stunde. |
| **Seilgewicht (Gesamt)** | kg/100m | Gewicht des fertigen Kern-Mantel-Seils je 100 m. |
| **Seeldurchmesser** | mm | Durchmesser der Seele (Kern). |
| **Mantelstärke** | mm | Wandstärke des Mantels (radial). |
| **Leistung (Kern)** / **Leistung (Mantel)** | kg/h | Durchsatz der jeweiligen Lage. |
| **Seilgewicht (Kern)** / **Seilgewicht (Mantel)** | kg/100m | Gewichtsanteil der jeweiligen Lage je 100 m. |
| **Litze (Kern)** / **Litze (Mantel)** | tex | Feinheit (lineare Dichte) der Litze je Lage. |
| **Litzendurchmesser (Kern)** / **Litzendurchmesser (Mantel)** | mm | Durchmesser der Einzellitze je Lage. |
| **Länge pro Spule (Kern)** / **Länge pro Spule (Mantel)** | m | Aufwickelbare Materiallänge je Spule. |
| **Länge Geflecht (Kern)** / **Länge Geflecht (Mantel)** | m | Pro Spule erzeugbare Geflechtlänge. |
| **Verkürzung (Kern)** / **Verkürzung (Mantel)** | % | Längenverkürzung durch das Flechten (Spulenlänge gegenüber Geflechtlänge). |
| **Flechtlänge (Kern)** / **Flechtlänge (Mantel)** | mm | Umlauflänge eines Fadens je Produktumdrehung (Steigung). |
| **Produktion (Kern)** / **Produktion (Mantel)** | m/h | Fertigungsgeschwindigkeit der jeweiligen Lage. |
| **Flechtzeit (Kern)** / **Flechtzeit (Mantel)** | h | Flechtdauer bis zum Leerlaufen einer Spule. |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

Die Funktion rechnet rein **vorwärts**: Aus allen Eingaben werden sämtliche Ergebnisse berechnet. Sie ist nicht umkehrbar – es wird kein leeres Eingabefeld aus den Ergebnissen rückgerechnet. Fehlen oder sind Eingaben ungültig (keine Spule gewählt, Wert ≤ 0), werden die Ergebnisse geleert.

!!! tip "Material einmal pflegen, Dichte automatisch übernehmen"
    Wählen Sie in beiden Panels ein [Material](../../master-data/materials.md) aus den Stammdaten – die **Dichte** wird dann automatisch gesetzt. Das ist schneller und vermeidet Tippfehler bei diesem rechenintensiven Produkt.

## Verwandte Berechnungen

* [Materialdurchmesser](./material-diameter.md) – Durchmesser aus Dichte und Titer eines Einzelmaterials.
* [Feinheit / Titer](./linear-density.md) – Feinheit (tex) einzelner Garne.
* [Produktgewicht](../product/rope-weight.md) – Gewichtsberechnung für einlagige Produkte.
* [Produktdurchmesser](../product/product-diameter.md) – Außendurchmesser eines Flechtprodukts.
* [Produktionsgeschwindigkeit](../machine/production-speed.md) – Fertigungsgeschwindigkeit einer Flechtmaschine.
