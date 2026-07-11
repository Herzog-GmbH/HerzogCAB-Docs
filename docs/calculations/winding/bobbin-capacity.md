# Spulenkapazität

!!! abstract "Referenz — Berechnung: Materiallänge, die eine Spule fasst"

## Wofür

Diese Berechnung ermittelt, wie viele Meter Material eine gewählte Spule
fasst — wahlweise über die Materialdaten (Dichte und Feinheit) oder direkt
über den Materialdurchmesser. Damit prüfen Sie vor dem Spulen, ob eine
vorhandene Spulenform für die gewünschte Materiallänge ausreicht, oder
wählen die passende Spule für einen Spulauftrag.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Berechnung über:** | – | Grundlage der Berechnung: *Material* (Dichte + Feinheit) oder *Durchmesser* (Materialdurchmesser direkt). Blendet die passenden Felder darunter ein. |
| **Spule:** | – | Auswahl der Spule aus den [Spulen-Stammdaten](../../master-data/bobbins.md) (alle Spulenformate, ungefiltert). |
| **Material:** | – | Nur bei Basis *Material*. Optionale Auswahl eines Materials aus den [Materialstammdaten](../../master-data/materials.md); übernimmt die hinterlegte Dichte automatisch. |
| **Dichte:** | g/cm³ | Nur bei Basis *Material*. Materialdichte (bis 3 Nachkommastellen, max. 25). Muss größer als 0 sein. |
| **Feinheit:** | tex, dtex, den, Nr_metrisch, Nr_englisch | Nur bei Basis *Material*. Feinheit des Materials mit Einheiten-Auswahl daneben. Muss mindestens 1 tex entsprechen. |
| **Materialdurchmesser:** | mm | Nur bei Basis *Durchmesser*. Durchmesser des Fadens bzw. Drahtes. Muss größer als 0 sein (max. 500 mm). |
| **Füllungsgrad:** | % | Wie dicht das Material auf der Spule liegt. Startwert 70 %, max. 100 %. Muss mindestens 1 % betragen. |
| **Fachung:** | stk. | Anzahl der gemeinsam gespulten Einzelfäden (mindestens 1, Startwert 1). |

!!! note "Pflichtfelder"
    Es muss eine Spule gewählt sein; Füllungsgrad mindestens 1 % und Fachung
    mindestens 1. Je nach Basis zusätzlich Dichte und Feinheit (Basis
    *Material*) bzw. Materialdurchmesser (Basis *Durchmesser*) größer als 0.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Spulenkapazität:** | m | Hauptergebnis: Materiallänge, die auf die gewählte Spule passt, auf zwei Nachkommastellen. |
| **Spulvolumen:** | cm³ | Aufnahmevolumen der gewählten Spule (aus Außen-/Kerndurchmesser und Wickellänge), auf eine Nachkommastelle. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten (Eingabe-Karte,
Ergebnis-Kacheln, Schaltflächen **Berechnen**/**Löschen**, Verlauf) steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md) —
hier nur die Besonderheiten dieser Seite.

!!! tip "Spule aus dem Auftrag übernehmen"
    Öffnen Sie diese Berechnung aus einem Auftrag heraus, wird die
    passende Spule anhand ihrer Abmessungen automatisch vorausgewählt — Sie
    müssen sie dann nicht mehr manuell suchen.

Bei Basis *Material* füllt die Auswahl eines Materials aus den Stammdaten
die **Dichte** automatisch; die **Feinheit** tragen Sie unabhängig davon mit
der gewünschten Einheit ein.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

* [Materiallänge auf Spule](../material/material-length.md)
* [Spulvolumen](../material/bobbin-volume.md)
* [Spulengewicht](bobbin-weight.md)
* [Spulzeit](winding-time.md)
