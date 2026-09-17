# Flechtwinkel über Abzug

!!! abstract "Referenz — Berechnung: Flechtwinkel aus Flügelraddrehzahl und Abzug — oder umgekehrt der nötige Abzug bzw. die nötige Flügelraddrehzahl für einen Soll-Flechtwinkel"

## Wofür

Diese Berechnung verbindet die **Maschineneinstellung** mit dem Geflecht.
Aus Flügelraddrehzahl und Abzugsgeschwindigkeit ergibt sich, unter welchem
Flechtwinkel das Geflecht entsteht — und umgekehrt: Welche
Abzugsgeschwindigkeit oder welche Flügelraddrehzahl brauchen Sie, damit ein
gewünschter Flechtwinkel herauskommt? Der Abzug lässt sich dabei als
Geschwindigkeit oder über Durchmesser und Drehzahl der Abzugsscheibe
angeben. Für Rund- und Litzengeflecht.

## Eingabewerte

Welche Felder sichtbar sind, hängt von **Berechnen** und **Abzug
vorgegeben als** ab.

| Feld | Einheit / Auswahl | Bedeutung |
|---|---|---|
| **Berechnen:** | *Flechtwinkel*, *Abzug*, *Flügelraddrehzahl* | Was gesucht ist. Bei *Flechtwinkel* sind Drehzahl und Abzug gegeben; bei *Abzug* bzw. *Flügelraddrehzahl* geben Sie den Soll-Flechtwinkel vor. |
| **Geflechtsart:** | *Rundgeflecht*, *Litzengeflecht* | Bestimmt die Maschinenangaben unten. |
| **Geflecht-Außendurchmesser:** / **Geflechtbreite:** | mm | Maß des Geflechts — Durchmesser beim Rundgeflecht, Breite bei der Litze. Das Rechner-Symbol öffnet [Produktdurchmesser](product-diameter.md); **Übernehmen** schreibt das Ergebnis zurück. |
| **Flügelradanzahl im Lauf:** | stk. | Nur Rundgeflecht: Anzahl der Flügelräder im Ring (bis 256). |
| **Schlitze je Normalflügelrad:** | stk. | Nur Litzengeflecht: Einschnitte eines normalen Flügelrads (Standard 4). |
| **Schlitze in der Laufbahn:** | stk. | Nur Litzengeflecht: Einschnitte über die ganze Laufbahn. |
| **Soll-Flechtwinkel:** | ° | Nur bei *Abzug* und *Flügelraddrehzahl*: der gewünschte Flechtwinkel (bis 85°). |
| **Flügelraddrehzahl:** | u/min | Drehzahl der Flügelräder (bis 2000). Entfällt, wenn sie berechnet wird. |
| **Abzug vorgegeben als:** | *Geschwindigkeit*, *Abzugsscheibe* | Wie der Abzug angegeben wird — entfällt, wenn der Abzug berechnet wird. |
| **Abzugsgeschwindigkeit:** | m/h | Bei *Geschwindigkeit*: die Abzugsgeschwindigkeit. Das Rechner-Symbol öffnet [Produktionsgeschwindigkeit](../production/production-speed.md). |
| **Abzugsscheibendurchmesser:** | mm | Bei *Abzugsscheibe* und beim Berechnen des Abzugs: Durchmesser der Abzugsscheibe (bis 5000). |
| **Drehzahl Abzugsscheibe:** | u/min | Bei *Abzugsscheibe*: Drehzahl der Scheibe (bis 10000). |
| **Wirksamer Abzug:** | % | Bei *Abzugsscheibe* und beim Berechnen des Abzugs: welcher Anteil der Scheibengeschwindigkeit wirklich am Geflecht ankommt (Schlupf; Standard 100 %). |

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Flechtwinkel** | ° | Bei *Berechnen: Flechtwinkel* — der Flechtwinkel, der sich aus Drehzahl und Abzug ergibt (zwei Nachkommastellen). |
| **Erforderliche Abzugsgeschwindigkeit** | m/h | Bei *Berechnen: Abzug*. |
| **Erforderliche Drehzahl Abzugsscheibe** | u/min | Bei *Berechnen: Abzug*, sobald ein Abzugsscheibendurchmesser eingetragen ist. |
| **Erforderliche Flügelraddrehzahl** | u/min | Bei *Berechnen: Flügelraddrehzahl*. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md).

Der Flechtwinkel wird — wie überall in Herzog CAB — gegen die
**Querrichtung** des Geflechts angegeben, genau wie in
[Flechtwinkel](braid-angle.md). Die Berechnung ist nur in der Desktop-App
enthalten; in der [Web-App](../../web/calculations.md) fehlt sie noch.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

- [Flechtwinkel](braid-angle.md) — aus Flechtbezeichnung und Produktmaß
- [Produktionsgeschwindigkeit](../production/production-speed.md)
- [Produktdurchmesser](product-diameter.md)
