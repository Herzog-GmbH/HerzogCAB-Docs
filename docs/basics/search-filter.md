# Suchen und Filtern

!!! info "Konzept — Die wiederkehrenden Such-, Filter- und Sortier-Muster in Listen"

Ob Auftragsübersicht, Maschinenpark oder Stammdaten-Listen: Überall in
Herzog CAB finden Sie dieselben Bedienmuster, um lange Listen schnell auf
das Wesentliche einzugrenzen. Diese Seite erklärt die Muster einmal zentral;
die Referenzseiten der Module nennen nur noch ihre Besonderheiten.

## Das Suchfeld

Fast jede Liste hat oben ein **Suchfeld**. Es filtert **während der
Eingabe** — Sie müssen nicht ++enter++ drücken. Der graue Platzhaltertext im
leeren Feld verrät, welche Angaben durchsucht werden, zum Beispiel:

| Liste | Durchsucht |
|---|---|
| [Aufträge](../orders/index.md) | Auftragsname, Nummer, Kunde, Maschine |
| [Maschinenpark](../machine-park/index.md) | Name, Typ, Seriennummer, Gruppe, Standort |
| [Kunden](../master-data/customers.md) | Name, Nummer, Firma, Kontakt, E-Mail, Ort |
| [Materialien](../master-data/materials.md) | Name, Marke, Notiz |
| [Spulen](../master-data/bobbins.md) | Durchmesser, Volumen, Maschinentyp |
| [Farben](../master-data/colors.md) | Kennung, Name, Hex-Wert, Referenzfarbe |

Um die Suche aufzuheben, leeren Sie das Feld einfach wieder.

## Filter-Auswahllisten

Neben dem Suchfeld liegen je nach Liste eine oder mehrere
**Filter-Auswahllisten**. Der erste Eintrag („Alle …") hebt den jeweiligen
Filter wieder auf. Beispiele:

* **Auftragsübersicht:** *Auftragsart* (Alle / Flechtaufträge /
  Spulaufträge), *Status* (Entwurf, Freigegeben, In Produktion,
  Abgeschlossen) und *Zeitraum* (Heute, Diese Woche, Letzte Woche, Dieser
  Monat, Letzte 30 Tage).
* **Maschinenpark:** *Maschinenart* (Flecht-/Spulmaschinen), *Kategorie*,
  *Status* (Fehler gemeldet, In Produktion, Aufträge warten, Keine aktiven
  Aufträge), *Gruppe*, *Geflechtsart* und *Standort*.
* **Spulen:** Filter nach *Maschinentyp*.

Suche und Filter wirken **zusammen**: Angezeigt wird nur, was auf den
Suchbegriff **und** alle gesetzten Filter passt. Passt nichts mehr, zeigt
die Liste einen Hinweis wie „Keine Maschinen entsprechen den aktuellen
Filtern" — lockern Sie dann Suche oder Filter.

## Sortierung

Viele Listen haben zusätzlich eine Auswahlliste **Sortierung**, z. B.
*Neueste zuerst*, *Älteste zuerst*, *Produktionsdatum* und *Auftragsdatum*
in der Auftragsübersicht oder *Name*, *Status (Fehler zuerst)*,
*Maschinentyp* und *Standort* im Maschinenpark. Die Sortierung ändert nur
die Reihenfolge, nicht die Auswahl.

## Ansicht umschalten

Einzelne Listen bieten rechts oben einen Umschalter zwischen
**Karten**-Ansicht (große Kacheln mit Bild und Kennzahlen) und
**Listen**-Ansicht (kompakte Zeilen) — etwa der
[Maschinenpark](../machine-park/index.md). Die gewählte Ansicht wirkt nur
auf die Darstellung; Suche, Filter und Sortierung gelten in beiden.

## Verwandte Seiten

* [Auftragsübersicht](../orders/index.md)
* [Maschinenpark](../machine-park/index.md)
* [Stammdaten](../master-data/index.md)
