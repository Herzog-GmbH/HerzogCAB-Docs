# Flechtwinkel

!!! abstract "Referenz — Berechnung: Flechtwinkel aus Flechtbezeichnung und Produktmaß"

## Wofür

Der **Flechtwinkel** ist der Winkel, unter dem ein einzelner Strang im
Geflecht zur Längsachse des Produkts verläuft. Er bestimmt maßgeblich Optik,
Festigkeit und Dehnung des fertigen Geflechts. Die Berechnung ermittelt
diesen Winkel aus Flechtbezeichnung und Produktmaß – getrennt für
Rundgeflecht und Litzengeflecht.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Geflechtsart:** | – | Auswahl zwischen *Rundgeflecht* und *Litzengeflecht*. Bestimmt die Formel und die Bezeichnung des nächsten Feldes. |
| **Flechtbezeichnung:** | Schlaglänge, FL / 10 mm, FL / Engl. Zoll, FL / Franz. Zoll | Kennwert der Flechtung. Die Einheit wählen Sie im Auswahlfeld rechts daneben. Bei *Schlaglänge* wird der Wert direkt verwendet; bei den FL-Einheiten (Flechtungen pro Längeneinheit) wird er intern in eine Schlaglänge umgerechnet. |
| **Produktdurchmesser:** / **Produktbreite:** | mm | Maß des Produkts. Bei *Rundgeflecht* heißt das Feld **Produktdurchmesser:**, bei *Litzengeflecht* **Produktbreite:**. |
| **Klöppelanzahl:** | stk. | Anzahl der Klöppel. Wird nur eingeblendet und benötigt, wenn als Flechtbezeichnung eine FL-Einheit gewählt ist (nicht bei *Schlaglänge*). |

!!! note "Klöppelanzahl nur bei FL-Einheiten"
    Das Feld **Klöppelanzahl:** erscheint erst, sobald Sie als Einheit der Flechtbezeichnung *FL / 10 mm*, *FL / Engl. Zoll* oder *FL / Franz. Zoll* wählen. Bei der Einheit *Schlaglänge* wird die Klöppelanzahl nicht gebraucht und bleibt ausgeblendet.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Flechtwinkel** | ° | Winkel des Strangs zur Längsachse des Produkts, auf zwei Nachkommastellen. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md).

Produktmaß und Flechtbezeichnung müssen größer als 0 sein, sonst ist keine
Berechnung möglich.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

- [Geflechtsdichte](lay-length.md)
- [Umrechnung Geflechtsdichte](picks-density.md)
- [Produktdurchmesser](product-diameter.md)
