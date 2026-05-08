# Berechnungen

Das Herz von Herzog CAB sind die **Berechnungen**. Sie sind nach Themen-
gruppen gegliedert und ueber den Navigationsbaum (*Berechnungen*) bzw.
das Menue *Ansicht > CAB Calculation 2.0* erreichbar.

## Themengruppen

<div class="grid cards" markdown>

- :material-rotate-3d-variant: __[Flechtgeometrie](braid-geometry/index.md)__

    ---
    Flechtwinkel, Verlegelaenge, Flechtdichte

- :material-tune-variant: __[Material](material/index.md)__

    ---
    Lineare Dichte, Materialdurchmesser, Kern-/Mantel-Konstellationen

- :material-cylinder: __[Spulen](bobbins/index.md)__

    ---
    Volumen, Materiallaenge auf Spule, Anzahl Wickler

- :material-cog-outline: __[Maschine](machine/index.md)__

    ---
    Abmessungen, Fluegelteilkreis, Produktionsgeschwindigkeit, Laufzeit

- :material-shape-outline: __[Produkt](product/index.md)__

    ---
    Durchmesser, Seillaenge, Seilgewicht

- :material-hexagon-outline: __[Rohrgeflecht](tubular-braid/index.md)__

    ---
    Rohrtraeger, Rohrueberzug, Garnbreite

- :material-star-four-points-outline: __[Spezial](advanced/index.md)__

    ---
    Horn Gear Layout, Carriers Rules, Braid Mapping

</div>

## Bedienung der Berechnungen

Alle Berechnungen sind nach dem gleichen Schema aufgebaut:

> :material-image-area: *Screenshot: Beispiel-Berechnung mit beschrifteten Bereichen*

| Bereich          | Inhalt                                                    |
|------------------|-----------------------------------------------------------|
| **Eingabe**      | Felder fuer die Eingangsgroessen (gelb hinterlegt).        |
| **Auswahl**      | Optional: Material/Spule/Maschine aus den Stammdaten.     |
| **Ergebnis**     | Ausgaberechnung (grau hinterlegt). Mehrere Werte gleichzeitig. |
| **Aktionen**     | Drucken, in Auftrag uebernehmen, Werte zuruecksetzen.     |

!!! tip "Berechnungen rueckwaerts loesen"
    Viele Berechnungen lassen sich umkehren. Beispiel: Sie kennen die
    Produktionsgeschwindigkeit und wollen wissen, welche Drehzahl noetig
    ist - tragen Sie die Geschwindigkeit ein, das Drehzahlfeld leer.
    Herzog CAB rechnet automatisch in die andere Richtung.

## Werte zwischenspeichern

Eingegebene Werte bleiben erhalten, solange das Programm laeuft. Wechseln
Sie auf eine andere Berechnung und kommen spaeter zurueck, finden Sie
Ihre Eingaben unveraendert vor. Nach einem Programmneustart sind die
Werte zurueckgesetzt.

## In Auftrag uebernehmen

Wenn Sie eine Berechnung im Rahmen eines [Auftrags](../orders/index.md)
durchfuehren, koennen Sie das Ergebnis ueber **In Auftrag uebernehmen**
direkt mit dem Auftrag verknuepfen. So bleibt die Berechnungs-Spur
nachvollziehbar.
