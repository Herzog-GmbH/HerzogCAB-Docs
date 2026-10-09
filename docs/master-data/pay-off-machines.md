# Abwickler

!!! abstract "Referenz — Abwickler der Baureihen AB, ABS, ABST und ABA anlegen und pflegen: Trommelmaße, Traglast, Trommelhub, Abwickelspannung, Zubehör und Dokumente."

## Wofür Sie diesen Bereich nutzen

Unter *Stammdaten > Abwickler* legen Sie die Abwickler Ihres Werks an. Ein
Abwickler lässt Material wie Seele, Seil oder Kabel von einer Trommel in
die nachfolgende Maschine ablaufen — etwa die Seele, die in einer
Flechtmaschine umflochten wird. Im [Maschinenpark](../machine-park/index.md)
haben Abwickler einen eigenen Filter.

!!! info "Neu ab Version 2.1.0"
    Abwickler sind eine eigene Maschinenart. Liste und Dialog sind
    aufgebaut wie bei den [Aufwicklern](take-up-machines.md).

## Der Bildschirm im Überblick

![Seite Abwickler mit Suchfeld, Neu, Bearbeiten, Löschen und einer Abwickler-Karte in der Maschinenliste](../assets/screenshots/master-data/abwickler.png)

Oben liegt eine Werkzeugleiste, darunter die **Maschinenliste** als Karten.
Jede Karte zeigt Bild, Baureihe (ohne Baureihe *Abwickler*),
**Trommel bis Ø … mm** sowie **Traglast … kg** und
**Trommelbreite … mm**, soweit hinterlegt.

Werkzeugleiste (**Maschine suchen**, **Neu**, **Bearbeiten**, **Löschen**),
Doppelklick und Kontextmenü (**Öffnen**, **Bearbeiten**, **Duplizieren**,
**Löschen**) funktionieren wie bei den
[Aufwicklern](take-up-machines.md#werkzeugleiste). Herzog-Abwickler legen
Sie am schnellsten über den [Herzog-Katalog](../catalog/index.md) an
(Reiter **Abwickler**).

## Der Dialog „Neuen Abwickler erstellen"

![Dialog „Neuen Abwickler erstellen“ mit Bild und Abschnitt Maschinendaten](../assets/screenshots/master-data/abwickler-neu-dialog.png)

Der Dialog ist von oben nach unten in Abschnitte gegliedert. Leere Felder
bleiben leer und gelten als nicht hinterlegt.

### Bild

* **Bild hochladen** – wählt ein Maschinenbild aus der
  [Medienbibliothek](media.md).
* **Bild aus Katalog übernehmen** – erscheint nur, solange der Abwickler
  kein eigenes Bild hat und sein **Maschinentyp** einem Modell aus dem
  [Herzog-Katalog](../catalog/index.md) entspricht (Internetverbindung
  nötig).
* **Bild entfernen** – nimmt das Bild wieder weg.

### Maschinendaten

| Feld | Bedeutung |
|---|---|
| **Name** | Anzeigename der Maschine. Pflichtfeld. |
| **Baureihe** | Eine der Baureihen (siehe [unten](#die-baureihen)) oder *–*. |
| **Maschinentyp** | Typbezeichnung, z. B. *AB 800*. Bleibt das Feld leer, wird die Baureihe als Maschinentyp gespeichert. |
| **Seriennummer** | Seriennummer der Maschine. |
| **Gruppe** | Frei vergebbare Gruppierung. |
| **Standort** | Halle/Werk/Abteilung. |
| **Baujahr** | Baujahr (oder *–*). |

### Maße und Grenzen

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Trommeldurchmesser (min–max)** | mm | Kleinster und größter Trommeldurchmesser, den der Abwickler aufnimmt. |
| **Trommelbreite max.** | mm | Größte Trommelbreite. |
| **Traglast** | kg | Gesamtgewicht der bestückten Trommel: Trommel plus aufgewickeltes Material. |
| **Pinolendurchmesser** | mm | Durchmesser der Pinole. Er wird an die jeweilige Trommel angepasst und entscheidet nicht, ob eine Trommel passt. |
| **Materialdurchmesser (min–max)** | mm | Durchmesser des Materials, das vom Abwickler abläuft, z. B. Seele oder Seil (eine Nachkommastelle). |

### Bauart

| Feld | Bedeutung |
|---|---|
| **Trommelhub** | *kein Hub*, *Handhubkurbel*, *elektrisch*, *pneumatisch* oder *hydraulisch* (oder *–*). |
| **Abwickelspannung** | Ankreuzfelder *Bremse*, *Tänzerarm*, *Flaschenzugtänzer* — mehrere zugleich möglich. Kein Haken bedeutet: ohne Bremse. |
| **Antrieb** | Ankreuzfeld *motorisch angetrieben*. |
| **Trommel** | Ankreuzfeld *traversierend*. |

### Zubehör und Dokumente

**Zubehör** zum Ankreuzen (Katalogvorschläge und eigenes Zubehör) und
**Dokumente** (Kategorien *Bedienungsanleitung*, *Datenblatt*, *Wartung*,
*Ersatzteile*, *Sonstiges*) funktionieren wie bei den
[Aufwicklern](take-up-machines.md#zubehor).

### Speichern

Unten schließen Sie den Dialog mit **Abwickler erstellen** ab oder
verwerfen ihn mit **Abbrechen**. Beim Bearbeiten heißt die Schaltfläche
**Speichern**. Ohne Namen erscheint *Bitte einen Namen eingeben.*; ist bei
Trommeldurchmesser oder Materialdurchmesser der untere Wert größer als der
obere, meldet der Dialog *„…: der untere Wert ist größer als der obere."*

## Die Baureihen

| Baureihe | Bezeichnung |
|---|---|
| **AB** | Abwickler |
| **ABS** | Abwickler mit hydraulischem Trommelhub |
| **ABST** | Abwickler mit traversierender Trommel |
| **ABA** | Angetriebener Abwickler |

## Verwandte Seiten

* [Aufwickler](take-up-machines.md) – das Gegenstück hinter der Flechtmaschine
* [Gatter](creels.md) – Ablaufgatter und Ablaufgestelle
* [Herzog-Katalog](../catalog/index.md) – Abwickler von Herzog übernehmen
* [Maschinenpark](../machine-park/index.md) – Betriebsübersicht aller Maschinen
