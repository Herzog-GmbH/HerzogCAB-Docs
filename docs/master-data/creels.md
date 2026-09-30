# Gatter

!!! abstract "Referenz — Ablaufgatter und Ablaufgestelle anlegen und pflegen: Ablaufstellen, Abzug, Spulenart und -größe, Fadenspannung, Überwachung, Material, Zubehör und Dokumente."

## Wofür Sie diesen Bereich nutzen

Unter *Stammdaten > Gatter* legen Sie die Ablaufgatter und Ablaufgestelle
Ihres Werks an. Ein Gatter führt Garne, Monofile, Drähte oder Kernmaterial
von seinen Ablaufstellen in eine Spul- oder Flechtmaschine. Im
[Maschinenpark](../machine-park/index.md) haben Gatter einen eigenen
Filter.

!!! info "Neu ab Version 2.1.0"
    Gatter sind eine eigene Maschinenart. Liste und Dialog sind aufgebaut
    wie bei den [Aufwicklern](take-up-machines.md).

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Die Gatter-Liste als Karten (Bild, Baureihe, „… Ablaufstellen", Abzug und Spulengröße) samt Werkzeugleiste.
    **So erzeugen:** Navigationspunkt *Stammdaten > Gatter* öffnen; einige Gatter der Baureihen GU und GR (Demo-Daten „Musterbetrieb") anlegen.
    **Ziel-Datei:** `assets/screenshots/master-data/gatter.png`

Oben liegt eine Werkzeugleiste, darunter die **Maschinenliste** als Karten.
Jede Karte zeigt Bild, Baureihe (ohne Baureihe *Gatter*),
**… Ablaufstellen** sowie den Abzug (*Überkopf* oder *rollend*) und
**Spule bis Ø … mm**, soweit hinterlegt.

Werkzeugleiste (**Maschine suchen**, **Neu**, **Bearbeiten**, **Löschen**),
Doppelklick und Kontextmenü (**Öffnen**, **Bearbeiten**, **Duplizieren**,
**Löschen**) funktionieren wie bei den
[Aufwicklern](take-up-machines.md#werkzeugleiste). Herzog-Gatter legen Sie
am schnellsten über den [Herzog-Katalog](../catalog/index.md) an (Reiter
**Gatter**).

## Der Dialog „Neues Gatter erstellen"

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Der Dialog *Neues Gatter erstellen* mit den Abschnitten „Ablaufstellen und Spulen" und „Bauart" (Fadenspannung, Überwachung, Material als Ankreuzfelder).
    **So erzeugen:** In *Stammdaten > Gatter* auf **Neu** klicken, Baureihe **GU** wählen, Ablaufstellen 8, davon aktiv 4 eintragen und bis „Bauart" scrollen.
    **Ziel-Datei:** `assets/screenshots/master-data/gatter-neu-dialog.png`

Der Dialog ist von oben nach unten in Abschnitte gegliedert. Leere Felder
bleiben leer und gelten als nicht hinterlegt.

### Bild

* **Bild hochladen** – wählt ein Maschinenbild aus der
  [Medienbibliothek](media.md).
* **Bild aus Katalog übernehmen** – erscheint nur, solange das Gatter kein
  eigenes Bild hat und sein **Maschinentyp** einem Modell aus dem
  [Herzog-Katalog](../catalog/index.md) entspricht (Internetverbindung
  nötig).
* **Bild entfernen** – nimmt das Bild wieder weg.

### Maschinendaten

| Feld | Bedeutung |
|---|---|
| **Name** | Anzeigename der Maschine. Pflichtfeld. |
| **Baureihe** | Eine der Baureihen (siehe [unten](#die-baureihen)) oder *–*. |
| **Maschinentyp** | Typbezeichnung, z. B. *GU 8/16*. Bleibt das Feld leer, wird die Baureihe als Maschinentyp gespeichert. |
| **Seriennummer** | Seriennummer der Maschine. |
| **Gruppe** | Frei vergebbare Gruppierung. |
| **Standort** | Halle/Werk/Abteilung. |
| **Baujahr** | Baujahr (oder *–*). |

### Ablaufstellen und Spulen

| Feld | Bedeutung |
|---|---|
| **Ablaufstellen** | Anzahl der Ablaufstellen insgesamt. |
| **davon aktiv** | Wie viele Stellen gleichzeitig laufen. Beispiel GU 4/8: 4 Stellen laufen, die übrigen 4 stehen für den schnellen Kopswechsel bereit. |
| **Abzug** | *Überkopf* oder *rollend* (oder *–*). |
| **Antrieb** | Ankreuzfeld *motorisch angetrieben*. |
| **Spulenart** | Ankreuzfelder *Kops*, *Papphülse*, *DIN-Trommel*, *Trommel*. |
| **Spulendurchmesser max.** | Größter Spulendurchmesser in mm. |
| **Spulenlänge max.** | Größte Spulenlänge in mm. |
| **Spulengewicht max.** | Größtes Spulengewicht in kg. |

### Bauart

| Feld | Bedeutung |
|---|---|
| **Fadenspannung** | Ankreuzfelder *Tellerbremse*, *Magnumbremse*, *Bandbremse*, *Umschlingungsbremse*, *Krokodilbremse*, *Magnetbremse*, *Tänzerarm*, *berührungslos geregelt*. |
| **Überwachung** | Ankreuzfelder *Fadenbruch*, *Blockade*, *Stillstand*. |
| **Material** | Ankreuzfelder für verarbeitbare Materialien: *Garn*, *Feinstgarn*, *Monofil*, *Draht*, *Glasfaser*, *Kohlefaser*, *Kernmaterial*, *Zettelfäden*, *Strickschlauch*. |

### Zubehör und Dokumente

**Zubehör** zum Ankreuzen (Katalogvorschläge und eigenes Zubehör) und
**Dokumente** (Kategorien *Bedienungsanleitung*, *Datenblatt*, *Wartung*,
*Ersatzteile*, *Sonstiges*) funktionieren wie bei den
[Aufwicklern](take-up-machines.md#zubehor).

### Speichern

Unten schließen Sie den Dialog mit **Gatter erstellen** ab oder verwerfen
ihn mit **Abbrechen**. Beim Bearbeiten heißt die Schaltfläche
**Speichern**. Ohne Namen erscheint *Bitte einen Namen eingeben.*; sind
mehr Stellen aktiv als vorhanden, meldet der Dialog *Aktive
Ablaufstellen: mehr als Ablaufstellen insgesamt.*

## Die Baureihen

| Baureihe | Bezeichnung |
|---|---|
| **GU** | Überkopf-Ablaufgatter |
| **GR** | Rollendes Ablaufgatter |
| **GRP** | Rollendes Ablaufgatter mit pneumatischer Stoppbremse |
| **GRG** | Rollendes Ablaufgatter, berührungslos geregelt |
| **GM** | Motorisch angetriebenes Ablaufgatter |
| **GMG** | Motorisch angetriebenes Ablaufgatter mit Tänzer je Ablaufstelle |
| **GS** | Ablaufgatter für Strickschläuche |
| **EGA** | Ablaufgatter für Papphülsen |
| **VG** | Variationsgatter |
| **AL** | Ablaufgestell |

## Verwandte Seiten

* [Abwickler](pay-off-machines.md) · [Aufwickler](take-up-machines.md) · [Spulmaschinen](winding-machines.md) · [Flechtmaschinen](braiding-machines.md)
* [Herzog-Katalog](../catalog/index.md) – Gatter von Herzog übernehmen
* [Maschinenpark](../machine-park/index.md) – Betriebsübersicht aller Maschinen
