# Berechnungen

Das Herz von Herzog CAB sind die **Berechnungen**. Sie sind nach Themen-
gruppen gegliedert und über den Navigationsbaum (*Berechnungen*) bzw.
das Menü *Ansicht > CAB Calculation 2.0* erreichbar.

## Themengruppen

<div class="grid cards" markdown>

- :material-rotate-3d-variant: __[Flechtgeometrie](braid-geometry/index.md)__

    ---
    Flechtwinkel, Verlegelänge, Flechtdichte

- :material-tune-variant: __[Material](material/index.md)__

    ---
    Lineare Dichte, Materialdurchmesser, Kern-/Mantel-Konstellationen

- :material-cylinder: __[Spulen](bobbins/index.md)__

    ---
    Volumen, Materiallänge auf Spule, Anzahl Wickler

- :material-cog-outline: __[Maschine](machine/index.md)__

    ---
    Abmessungen, Flügelteilkreis, Produktionsgeschwindigkeit, Laufzeit

- :material-shape-outline: __[Produkt](product/index.md)__

    ---
    Durchmesser, Seillänge, Seilgewicht

- :material-hexagon-outline: __[Rohrgeflecht](tubular-braid/index.md)__

    ---
    Rohrträger, Rohrüberzug, Garnbreite

- :material-star-four-points-outline: __[Spezial](advanced/index.md)__

    ---
    Horn Gear Layout, Carriers Rules, Braid Mapping

</div>

## Bedienung der Berechnungen

Alle Berechnungen sind nach dem gleichen Schema aufgebaut:

> :material-image-area: *Screenshot: Beispiel-Berechnung mit beschrifteten Bereichen*

| Bereich          | Inhalt                                                    |
|------------------|-----------------------------------------------------------|
| **Eingabe**      | Felder für die Eingangsgrößen (gelb hinterlegt).        |
| **Auswahl**      | Optional: Material/Spule/Maschine aus den Stammdaten.     |
| **Ergebnis**     | Ausgaberechnung (grau hinterlegt). Mehrere Werte gleichzeitig. |
| **Aktionen**     | Drucken, in Auftrag übernehmen, Werte zurücksetzen.     |

!!! tip "Berechnungen rückwärts lösen"
    Viele Berechnungen lassen sich umkehren. Beispiel: Sie kennen die
    Produktionsgeschwindigkeit und wollen wissen, welche Drehzahl nötig
    ist - tragen Sie die Geschwindigkeit ein, das Drehzahlfeld leer.
    Herzog CAB rechnet automatisch in die andere Richtung.

## Werte zwischenspeichern

Eingegebene Werte bleiben erhalten, solange das Programm läuft. Wechseln
Sie auf eine andere Berechnung und kommen später zurück, finden Sie
Ihre Eingaben unverändert vor. Nach einem Programmneustart sind die
Werte zurückgesetzt.

## In Auftrag übernehmen

Wenn Sie eine Berechnung im Rahmen eines [Auftrags](../orders/index.md)
durchführen, können Sie das Ergebnis über **In Auftrag übernehmen**
direkt mit dem Auftrag verknüpfen. So bleibt die Berechnungs-Spur
nachvollziehbar.
