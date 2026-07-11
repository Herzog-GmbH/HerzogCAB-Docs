# Materiallänge auf Spule

!!! abstract "Referenz — Berechnung: nutzbare Fadenlänge auf einer bestückten Spule"

## Wofür

Diese Berechnung ermittelt, **wie viel Material auf eine Spule passt** – die
nutzbare Fadenlänge auf der Spule. Grundlage sind das Wickelvolumen der Spule
und die Materialdaten (Dichte, Feinheit bzw. Abmessungen).

## Eingabewerte

Über **Berechnung über** wählen Sie die Rechenbasis; je nach Wahl werden
unterschiedliche Felder eingeblendet.

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Berechnung über** | – | Rechenbasis: **Material**, **Durchmesser** oder **Rechteckfaden**. |
| **Maschinentype** | – | Filtert die wählbaren Spulen. |
| **Spule** | – | Spule aus den [Spulen-Stammdaten](../../master-data/bobbins.md); liefert die Abmessungen für das Wickelvolumen. |
| **Material** | – | Optional: Material aus den Stammdaten; übernimmt die **Dichte** automatisch. |
| **Dichte** | g/cm³ | Materialdichte. |
| **Feinheit** | tex, dtex, den, Nr. metrisch, Nr. englisch | Feinheit des Materials (nur bei Rechenbasis *Material*). |
| **Durchmesser** | mm | Materialdurchmesser (nur bei Rechenbasis *Durchmesser*). |
| **Rechteckhöhe**, **Rechteckbreite** | mm | Maße des Flachfadens (nur bei Rechenbasis *Rechteckfaden*). |
| **Füllungsgrad** | % | Anteil des Spulenvolumens, der tatsächlich bewickelt wird (Vorgabe 70). |
| **Fachung** | Stück | Anzahl der Fäden je Klöppel. |

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Materiallänge** | m | Auf die Spule passende Fadenlänge (2 Nachkommastellen). |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md).

Die Spule kann aus einem Auftrag heraus auch automatisch anhand ihrer
Abmessungen vorausgewählt werden, statt sie hier manuell zu suchen.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

- [Spulvolumen](bobbin-volume.md)
- [Feinheit / Titer](linear-density.md)
- [Materialdurchmesser über Material](material-diameter.md)
- [Spulenformate (Stammdaten)](../../master-data/bobbins.md)
