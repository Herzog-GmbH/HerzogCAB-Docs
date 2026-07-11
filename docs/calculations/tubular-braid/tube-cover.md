# Hohlgeflecht – Bedeckung

!!! abstract "Referenz — Berechnung: ermittelt den erreichten Bedeckungsgrad eines Hohlgeflechts"

## Wofür

Diese Berechnung ermittelt die **Bedeckung** eines Hohlgeflechts – also wie vollständig die Oberfläche des Schlauchs/Rohrs vom Geflecht bedeckt ist (in Prozent). So prüfen Sie, ob eine Konstellation aus Material, Klöppelzahl und Flechtwinkel die gewünschte Dichte erreicht.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Garnart** | – | **Multifil** oder **Monofil**. Bestimmt, ob mit Materialbreite oder Materialdurchmesser gerechnet wird. |
| **Geflechtsdurchmesser** | mm | Durchmesser des Hohlgeflechts. |
| **Flechtwinkel** | ° | Flechtwinkel (kleiner 90°, Vorgabe 45). |
| **Materialbreite** / **Materialdurchmesser** | mm | Bei *Multifil* die Materialbreite, bei *Monofil* der Materialdurchmesser. |
| **Faktor Breite/Ø** | – | Verhältnis Breite zu Durchmesser (1–3, Vorgabe 1,25; nur bei *Multifil*). |
| **Klöppelanzahl** | Stück | Anzahl der Klöppel. |
| **Fachung** | Stück | Anzahl der Fäden je Klöppel (Vorgabe 1). |

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Bedeckung** | % | Bedeckungsgrad des Geflechts (1 Nachkommastelle). Werte über 100 % werden als „Bedeckung > 100 %" gekennzeichnet. |

## Bedienung

Wie bei den übrigen Hohlgeflecht-Berechnungen läuft rechts eine live mitlaufende **Schema-Skizze** mit, die das gerade bearbeitete Feld hervorhebt. Führen Ihre Eingaben geometrisch zu keinem gültigen Ergebnis, meldet die Seite dies als Fehler statt einen unsinnigen Wert anzuzeigen (siehe unten). Der allgemeine Aufbau der Berechnungsseiten ist in [So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md) beschrieben.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

!!! warning "Bedeckung > 100 %"
    Sind die Eingaben geometrisch nicht möglich (das Material würde sich mehrfach überlappen), meldet die Seite **„Bedeckung > 100 %"** statt eines Zahlenwerts. Verringern Sie in diesem Fall Materialbreite/-durchmesser, Klöppelanzahl oder Fachung, oder erhöhen Sie den Geflechtsdurchmesser.

## Verwandte Berechnungen

* [Hohlgeflecht – Anzahl Klöppel](tube-carriers.md)
* [Hohlgeflecht – Durchmesser](tube-diameter.md)
* [Hohlgeflecht – Materialbreite](yarn-width.md)
