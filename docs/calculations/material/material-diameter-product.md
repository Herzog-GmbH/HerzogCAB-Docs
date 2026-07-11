# Materialdurchmesser über Produkt

!!! abstract "Referenz — Berechnung: benötigter Materialdurchmesser und Feinheit aus den Produktvorgaben"

## Wofür

Diese Berechnung dreht die Blickrichtung gegenüber
[Materialdurchmesser über Material](material-diameter.md) um: Statt aus einem
bekannten Garn den Durchmesser zu berechnen, geben Sie vor, welches
Geflecht am Ende entstehen soll (Durchmesser bzw. Breite, Klöppelanzahl,
Flechtwinkel, Füllungsgrad, Fachung). Herzog CAB ermittelt daraus, welche
Feinheit und welchen Durchmesser das einzusetzende Garn haben muss, und
schlägt dazu direkt ein passendes Material aus der Materialdatenbank vor. So
starten Sie die Materialauswahl vom fertigen Produkt her, statt Garn für
Garn durchzuprobieren.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Geflechtstyp:** | – | Auswahl zwischen *Rundgeflecht* und *Litzengeflecht*. Bestimmt Beschriftung und Berechnung des Maßfeldes sowie, ob die Ergebniskachel **Banddicke** eingeblendet wird. |
| **Material:** | – | Optionale Auswahl eines Materials aus den [Stammdaten](../../master-data/materials.md). Übernimmt die hinterlegte **Dichte** automatisch und dient zugleich als Filter für den Material-Vorschlag im Ergebnis. |
| **Dichte:** | g/cm³ | Materialdichte (bis 3 Nachkommastellen, max. 25). Muss größer als 0 sein. |
| **Produktdurchmesser:** / **Produktbreite:** | mm | Maß des fertigen Geflechts (max. 100000). Die Beschriftung wechselt automatisch: *Produktdurchmesser* bei Rundgeflecht, *Produktbreite* bei Litzengeflecht. Muss größer als 0 sein. |
| **Anzahl Klöppel:** | stk. | Anzahl der Klöppel der Flechtmaschine (max. 1500). Mindestwert 1. |
| **Flechtwinkel:** | ° | Winkel der Stränge zur Produktachse (max. 89°). Muss größer als 0 sein. |
| **Füllungsgrad:** | % | Wie dicht der Querschnitt mit Material gefüllt sein soll (max. 100 %, Startwert 80 %). Muss größer als 0 sein. |
| **Fachung:** | stk. | Anzahl der Enden, mit der das vorgeschlagene Garn je Klöppel gefahren wird (max. 1000). Mindestwert 1. |

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Materialdurchmesser:** | mm | Hauptkachel: benötigter Durchmesser des Einzelgarns, auf 3 Nachkommastellen. |
| **Benötigte Feinheit:** | tex, dtex, den, Nr_metrisch oder Nr_englisch | Feinheit, die das Garn je Klöppel und Ende haben muss. Über einen Umschalter direkt in der Kachel-Kopfzeile wählen Sie die Anzeige-Einheit, ohne neu zu rechnen. |
| **Banddicke (Litze):** | mm | Nur bei Geflechtstyp *Litzengeflecht* sichtbar: Dicke des vollen Bandes aus allen Enden eines Klöppels (Strangdurchmesser × 2). Bei Rundgeflecht bleibt die Kachel ausgeblendet. |
| **Material-Vorschlag:** | Text | Nennt das Material aus der Datenbank, dessen Feinheit der benötigten Feinheit am nächsten kommt – eingeschränkt auf denselben Werkstoff wie das oben gewählte Material (gleicher Name, sonst gleiche Dichte). Findet sich keines, erscheint der Hinweis „kein passendes Material gleichen Typs gefunden". |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md).

Diese Berechnung läuft nur vorwärts: Aus den Produktvorgaben werden
Materialdurchmesser, Feinheit und Material-Vorschlag ermittelt; ein
Rückrechnen einzelner Eingabefelder aus dem Ergebnis ist nicht vorgesehen.
Fehlen Dichte, Produktmaß, Flechtwinkel, Füllungsgrad oder ist die
Klöppelanzahl bzw. Fachung kleiner als 1, bleiben die Ergebniskacheln leer
und das betroffene Feld wird rot markiert.

!!! tip "Ergebnis in jeder Feinheits-Einheit ablesen"
    Die Kachel **Benötigte Feinheit** hat einen eigenen Einheiten-Umschalter
    in der Kopfzeile. Damit lesen Sie dasselbe Ergebnis wahlweise in tex,
    dtex, den, Nr_metrisch oder Nr_englisch ab, ohne die Berechnung erneut
    auszulösen.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

- [Materialdurchmesser über Material](material-diameter.md) – Durchmesser aus einem bereits bekannten Garn.
- [Fachung über Produkt](required-ply.md) – ermittelt umgekehrt die nötige Fachung für ein bereits gewähltes Material.
- [Feinheit / Titer](linear-density.md) – Feinheit eines Einzelfadens aus den Geflechtparametern.
- [Materialien](../../master-data/materials.md) – Pflege von Dichte und Titer in den Stammdaten.
