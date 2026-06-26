# Materialdurchmesser

Berechnet den Durchmesser eines einzelnen Materialstrangs (Garn, Litze oder Draht) aus seiner Feinheit, der Materialdichte, der Fachung und dem Füllungsgrad. So lässt sich abschätzen, wie dick ein Strang auf dem Klöppel tatsächlich aufträgt – etwa um Klöppelbelegung, Spulenfüllung oder die Geometrie eines Geflechts einzuschätzen.

## Eingabewerte

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Material:** | – | Optionale Auswahl aus der [Materialdatenbank](../../master-data/materials.md). Bei Auswahl wird die **Dichte** automatisch in das Dichte-Feld übernommen. |
| **Dichte:** | g/cm³ | Materialdichte (muss größer als 0 sein). Wird durch die Materialauswahl gefüllt oder manuell eingetragen. |
| **Feinheit:** | tex, dtex, den, Nr_metrisch, Nr_englisch | Feinheit (lineare Dichte) des Materials. Die Einheit wählen Sie im Auswahlfeld rechts daneben (Standard: tex). Mindestwert 1. |
| **Fachung:** | stk. | Anzahl der parallel geführten Enden, die den Strang bilden. Mindestwert 1. |
| **Füllungsgrad:** | % | Wie dicht das Material im Strangquerschnitt gepackt ist (1–100 %, Startwert 80 %). |

!!! note "Dichte kommt aus dem Material"
    Wählen Sie ein Material aus der Datenbank, wird die hinterlegte Dichte
    automatisch eingetragen. Sie können den Wert anschließend bei Bedarf
    überschreiben. Materialien haben keinen festen Durchmesser – dieser
    ergibt sich erst aus den hier eingegebenen Werten.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Materialdurchmesser:** | mm | Berechneter Durchmesser des Strangs aus allen gefachten Enden, gerundet auf 2 Nachkommastellen. |

## Berechnung

Herzog CAB ermittelt das Ergebnis intern aus den eingegebenen Werten. Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

!!! tip "Einheit der Feinheit beachten"
    Geben Sie die Feinheit immer in der Einheit ein, die im Auswahlfeld
    eingestellt ist. dtex, den, Nm und Ne werden vor der Rechnung intern
    nach tex umgerechnet – eine falsch gewählte Einheit verfälscht den
    Durchmesser.

## Verwandte Berechnungen

* **Materialdurchmesser über Produkt** (auf dieser Seite mitbeschrieben) – ermittelt umgekehrt aus Produktdurchmesser bzw. -breite und den Geflechtsparametern die benötigte Feinheit, den Materialdurchmesser und einen Material-Vorschlag.
* [Feinheit / Titer](./linear-density.md) – Umrechnung und Bestimmung der Feinheit.
* [Materialien](../../master-data/materials.md) – Pflege von Dichte und Titer in den Stammdaten.
