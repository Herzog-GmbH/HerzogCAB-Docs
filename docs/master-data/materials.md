# Materialien

Im Materialeditor pflegen Sie die Materialien, die in Ihren Flechtungen
zum Einsatz kommen - Draehte, Litzen, Garne, Faeden.

> :material-image-area: *Screenshot: Materialeditor mit gefuellter Materialliste*

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

1. Im Navigationsbaum *Stammdaten > Materialien* oeffnen.
2. Auf :material-plus: **Neu** klicken.
3. Felder ausfuellen.
4. **Speichern**.

## Material in einer Berechnung verwenden

In den meisten Berechnungen koennen Sie statt manueller Eingabe ein
Material aus der Liste waehlen. Die Werte (Durchmesser, lineare Dichte
etc.) werden dann automatisch uebernommen.

> :material-image-area: *Screenshot: Materialauswahl in einer Berechnung*

!!! tip "Wiederkehrende Materialien einmal anlegen"
    Pflegen Sie haeufig genutzte Materialien einmal sauber - das spart
    bei jeder Berechnung Tipparbeit und vermeidet Fehleingaben.
