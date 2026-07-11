# Fachung über Produkt

!!! abstract "Referenz — Berechnung: benötigte Fachung für ein bereits gewähltes Material"

## Wofür

Diese Berechnung ist das Gegenstück zu
[Materialdurchmesser über Produkt](material-diameter-product.md): Statt ein
passendes Material vorzuschlagen, gehen Sie von einem bereits feststehenden
Garn aus und ermitteln, mit wie vielen Enden (**Fachung**) es je Klöppel
gefahren werden muss, um das gewünschte Geflecht zu erreichen. Typischer
Einsatz: Ein Garn liegt bereits auf Lager oder ist vorgegeben, und Sie
möchten wissen, wie viele Fäden davon parallel je Klöppel eingesetzt werden
müssen.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Geflechtstyp:** | – | Auswahl zwischen *Rundgeflecht* und *Litzengeflecht*. Bestimmt die Beschriftung und Berechnung des Maßfeldes. |
| **Material:** | – | Optionale Auswahl eines Materials aus den [Stammdaten](../../master-data/materials.md). Übernimmt **Dichte** und **Feinheit (Material)** (in tex) automatisch. |
| **Dichte:** | g/cm³ | Materialdichte (bis 3 Nachkommastellen, max. 25). Muss größer als 0 sein. |
| **Feinheit (Material):** | tex, dtex, den, Nm, Ne | Feinheit des bereits gewählten Garns. Die Einheit wählen Sie im Auswahlfeld rechts daneben (Standard: tex). Muss größer als 0 sein. |
| **Produktdurchmesser:** / **Produktbreite:** | mm | Maß des fertigen Geflechts (max. 100000). Die Beschriftung wechselt automatisch: *Produktdurchmesser* bei Rundgeflecht, *Produktbreite* bei Litzengeflecht. Muss größer als 0 sein. |
| **Anzahl Klöppel:** | stk. | Anzahl der Klöppel der Flechtmaschine (max. 1500). Mindestwert 1. |
| **Flechtwinkel:** | ° | Winkel der Stränge zur Produktachse (max. 89°). Muss größer als 0 sein. |
| **Füllungsgrad:** | % | Wie dicht der Querschnitt mit Material gefüllt sein soll (max. 100 %, Startwert 80 %). Muss größer als 0 sein. |

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Benötigte Fachung:** | stk. | Anzahl der Enden des gewählten Garns, die je Klöppel benötigt werden. |

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md).

Diese Berechnung läuft nur vorwärts: Aus den Produktvorgaben und der
Feinheit des gewählten Garns wird die benötigte Fachung ermittelt; ein
Rückrechnen einzelner Eingabefelder aus dem Ergebnis ist nicht vorgesehen.
Fehlen Dichte, Feinheit, Produktmaß, Flechtwinkel oder Füllungsgrad, oder ist
die Klöppelanzahl kleiner als 1, bleibt das Ergebnisfeld leer und das
betroffene Feld wird rot markiert.

!!! note "Ergebnis wird aufgerundet"
    Da eine Fachung nur aus ganzen Fäden bestehen kann, rundet Herzog CAB das
    rechnerische Ergebnis stets auf die nächste ganze Zahl auf (mindestens 1
    stk.). Reicht die tatsächlich gewählte Fachung rechnerisch nicht ganz
    aus, greifen Sie im Zweifel zur nächsthöheren Stufe.

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

- [Materialdurchmesser über Produkt](material-diameter-product.md) – schlägt umgekehrt ein passendes Material samt Feinheit vor.
- [Materialdurchmesser über Material](material-diameter.md) – Durchmesser eines bereits bekannten Garns.
- [Feinheit / Titer](linear-density.md) – Feinheit eines Einzelfadens aus den Geflechtparametern.
- [Materialien](../../master-data/materials.md) – Pflege von Dichte und Titer in den Stammdaten.
