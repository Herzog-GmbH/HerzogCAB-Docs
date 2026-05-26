# Materialien

Im Materialeditor pflegen Sie die Materialien, die in Ihren Flechtungen
zum Einsatz kommen - Drähte, Litzen, Garne, Fäden.

> :material-image-area: *Screenshot: Materialeditor mit gefüllter Materialliste*

## Eigenschaften eines Materials

> :material-alert-circle-outline: **TODO** *Eike validiert die Feldnamen anhand des Editors. Stand jetzt aus dem Code abgeleitet:*

| Feld                | Beschreibung                                                |
|---------------------|-------------------------------------------------------------|
| Bezeichnung         | Klartext-Name (z. B. "Draht 0,2 mm verzinkt")               |
| Materialtyp         | Draht, Garn, Litze, ...                                     |
| Durchmesser         | in mm                                                       |
| Lineare Dichte      | in dtex / tex / g/m                                         |
| Farbe               | Verweis auf Farben-Stammdaten                               |
| Hersteller          | Optional                                                    |
| Bemerkung           | Frei-Text                                                   |

## Material anlegen

1. Im Navigationsbaum *Stammdaten > Materialien* öffnen.
2. Auf :material-plus: **Neu** klicken.
3. Felder ausfüllen.
4. **Speichern**.

## Material in einer Berechnung verwenden

In den meisten Berechnungen können Sie statt manueller Eingabe ein
Material aus der Liste wählen. Die Werte (Durchmesser, lineare Dichte
etc.) werden dann automatisch übernommen.

> :material-image-area: *Screenshot: Materialauswahl in einer Berechnung*

!!! tip "Wiederkehrende Materialien einmal anlegen"
    Pflegen Sie häufig genutzte Materialien einmal sauber - das spart
    bei jeder Berechnung Tipparbeit und vermeidet Fehleingaben.
