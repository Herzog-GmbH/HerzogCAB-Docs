# Spulen

Im Spulen-Editor (Bobbin Editor) pflegen Sie die Spulentypen, die auf
Ihren Maschinen zum Einsatz kommen. Ueber die Spuleneigenschaften (z. B.
Volumen, Hub, Flanschdurchmesser) berechnet Herzog CAB anschliessend
Materiallaengen, Standzeiten und Wechselintervalle.

> :material-image-area: *Screenshot: Spulen-Editor (Bobbin Editor)*

## Eigenschaften einer Spule

> :material-alert-circle-outline: **TODO** *Felder anhand des Editors validieren. Aus dem Code abgeleitet:*

| Feld                  | Beschreibung                                              |
|-----------------------|-----------------------------------------------------------|
| Bezeichnung           | Name der Spulenform                                       |
| Aussendurchmesser     | in mm                                                     |
| Innendurchmesser      | in mm                                                     |
| Flanschbreite         | in mm                                                     |
| Wickelvolumen         | berechnet aus den Abmessungen                             |
| Bemerkung             | Frei-Text                                                 |

## Verwendung

Spulen werden in folgenden Berechnungen herangezogen:

* [Spulenvolumen](../calculations/bobbins/bobbin-volume.md)
* [Materiallaenge auf Spule](../calculations/bobbins/material-length.md)
* [Laufzeit und Spulensatz](../calculations/machine/run-time-bobbin-set.md)
