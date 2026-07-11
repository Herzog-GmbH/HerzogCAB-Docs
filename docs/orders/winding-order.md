# Spulauftrag-Editor

!!! abstract "Referenz — Spulauftrag anlegen und bearbeiten: Sollwerte der Spulerei, Farbaufschlüsselung, Wickelparameter und die Verknüpfung zum Flechtauftrag."

## Wofür Sie diesen Bereich nutzen

Ein **Spulauftrag** plant die Arbeit der Spulerei: Wie viele Spulen werden
mit welchem Material und welcher Fadenlänge bewickelt, auf welcher
Spulmaschine und mit welchen Wickelparametern. Meist ist der Spulauftrag die
Vorstufe („Schritt 1") eines Flechtauftrags — die bewickelten Spulen werden
anschließend in die Klöppel der Flechtmaschine eingesetzt.

```mermaid
flowchart LR
  A[Flechtauftrag] -->|Spulauftrag erstellen| B[Spulauftrag<br>Schritt 1: Spulen]
  B -->|bewickelte Spulen| C[Produktion auf der<br>Flechtmaschine]
```

Sie erreichen den Editor auf drei Wegen:

* In der [Auftragsübersicht](index.md) über **Neuer Auftrag** > *Neuer Spulauftrag* (leerer Spulauftrag),
* über **Spulauftrag erstellen** bei ausgewähltem Flechtauftrag (vorbefüllter, verknüpfter Spulauftrag),
* per **Öffnen** oder Doppelklick auf eine Spulauftrags-Karte.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Spulauftrag-Editor mit Tab-Leiste (Auftrag, Kunde, Maschine, Material und Spule, Spulerei), Kopfzeile mit **Zur Auftragsübersicht**, **Drucken**, **Spulauftrag speichern**; Tab „Auftrag" mit dem Bereich „Verknüpfter Flechtauftrag"
    **So erzeugen:** In der Auftragsübersicht einen Flechtauftrag anwählen und **Spulauftrag erstellen** klicken; der Editor öffnet sich mit Tab *Auftrag*
    **Ziel-Datei:** `assets/screenshots/orders/spulauftrag-editor-auftrag.png`

Oben links bringt Sie **Zur Auftragsübersicht** zurück zur
[Auftragsübersicht](index.md). Oben rechts liegen **Drucken** (öffnet die
[Druckausgabe](print.md) mit der Spulauftrags-Standardvorlage) und
**Spulauftrag speichern**.

Der Editor ist in fünf Tabs gegliedert:

| Tab | Inhalt |
|---|---|
| **Auftrag** | Name, Nummer, Status, Termine und die Verknüpfung zum Flechtauftrag. |
| **Kunde** | Kunde aus dem Kundenstamm oder aus dem Flechtauftrag übernommen. |
| **Maschine** | Spulmaschine für diesen Auftrag. |
| **Material und Spule** | Welches Material auf welches Spulenformat gewickelt wird. |
| **Spulerei** | Sollwerte, Farbaufschlüsselung und optionale Wickelparameter. |

## Tab „Auftrag"

### Grunddaten

| Feld | Bedeutung |
|---|---|
| **Auftragsname** | Frei wählbarer Name, z. B. *Spulen für Seilauftrag 4711*. |
| **Auftragsnummer** | Ihre Auftragsnummer. Bei aus einem Flechtauftrag erzeugten Spulaufträgen ist sie mit *&lt;Nummer&gt;-SP* vorbelegt. |
| **Status** | *Entwurf*, *Freigegeben*, *In Produktion* oder *Abgeschlossen* — gleiche Bedeutung wie beim [Flechtauftrag](index.md#status-eines-auftrags). |
| **Auftragsdatum** | Datum des Auftrags, mit Kalenderauswahl. |
| **Produktionsdatum** | Geplanter Spultermin, mit Kalenderauswahl. Bei der Übernahme aus einem Flechtauftrag mit dessen Produktionstermin vorbelegt. |

### Bereich „Verknüpfter Flechtauftrag"

Zeigt, für welchen Flechtauftrag dieser Spulauftrag die Spulen fertigt —
z. B. *Schritt 1 (Spulen) für: Abschleppseil (Nr. A-2026-015)*. Ohne
Verknüpfung steht hier ein entsprechender Hinweis; wurde der verknüpfte
Auftrag gelöscht, wird auch das angezeigt.

| Schaltfläche | Wirkung |
|---|---|
| **Flechtauftrag wählen…** | Öffnet eine Liste aller Flechtaufträge. Nach der Auswahl (Doppelklick oder **Verknüpfen**) bietet Herzog CAB an, Kunde, Material, Spulenformat, Produktionstermin und Sollwerte (Zielspulenzahl, Länge pro Spule) aus dem Flechtauftrag zu übernehmen — bereits eingegebener Auftragsname, Nummer und Wickelparameter bleiben dabei erhalten. |
| **Öffnen** | Öffnet den verknüpften Flechtauftrag im [Flechtauftrag-Editor](braiding-order.md). Nur aktiv, wenn der verknüpfte Auftrag existiert. |
| **Verknüpfung lösen** | Entfernt die Verknüpfung. Der Spulauftrag bleibt mit allen Werten bestehen. |

## Tab „Kunde"

### Kunde

Auswahlliste mit drei Arten von Einträgen:

* **Kein Kunde** — dem Spulauftrag ist kein Kunde zugeordnet.
* Die Kunden aus den [Kundenstammdaten](../master-data/customers.md).
* **Übernommen: &lt;Name&gt;** — erscheint nur, wenn der Auftrag Kundendaten
  trägt (z. B. aus dem Flechtauftrag übernommen), die keinem Eintrag im
  Kundenstamm entsprechen. Mit dieser Auswahl bleiben die übernommenen Daten
  unverändert erhalten.

Unter der Auswahl fasst eine Infozeile den gewählten Kunden zusammen (Firma,
Name, Anschrift, Kontakt).

## Tab „Maschine"

### Maschine

Auswahlliste Ihrer **Spulmaschinen** (erster Eintrag: *Keine Maschine
ausgewählt*). Flechtmaschinen erscheinen hier bewusst nicht — sie gehören in
den Flechtauftrag. Spulmaschinen legen Sie unter
[Stammdaten > Spulmaschinen](../master-data/winding-machines.md) an. Eine
nicht mehr vorhandene Maschine wird als *… (nicht mehr vorhanden)*
angezeigt.

Unter der Auswahl zeigt eine Infozeile die Eckdaten der Maschine: Kategorie,
Anzahl der Spulstellen, maximale Spindeldrehzahl, maximaler Spulendurchmesser
sowie die laut Stammdaten passenden Spulen.

## Tab „Material und Spule"

| Feld | Bedeutung |
|---|---|
| **Material** | Material, das gespult wird — aus den [Material-Stammdaten](../master-data/materials.md). |
| **Spulenformat** | Spulenformat, auf das gewickelt wird — aus den [Spulen-Stammdaten](../master-data/bobbins.md), angezeigt mit Abmessungen und Volumen. |

Bei einem aus dem Flechtauftrag erzeugten Spulauftrag sind beide Felder
bereits passend vorbelegt: Es wird dasselbe Material auf dasselbe
Spulenformat gewickelt, das später auf der Flechtmaschine läuft. Nicht mehr
vorhandene Einträge werden als *… (nicht mehr vorhanden)* gekennzeichnet.

## Tab „Spulerei"

### Sollwerte

| Feld | Bedeutung |
|---|---|
| **Zielspulenzahl** | Wie viele Spulen insgesamt bewickelt werden sollen; 0 wird als *Nicht gesetzt* angezeigt. Bei der Übernahme aus dem Flechtauftrag ist der Wert vorbelegt — abgeleitet aus den benötigten Spulensätzen und den aktiven Klöppeln des Flechtauftrags. |
| **Länge pro Spule** | Fadenlänge je Spule in Metern. Das Rechner-Symbol im Feld öffnet die Berechnung [Spulenkapazität](../calculations/winding/bobbin-capacity.md) — vorbelegt mit dem gewählten Spulenformat und Material; **Übernehmen** schreibt die berechnete Kapazität in das Feld zurück. |
| **Gesamtlänge** | Anzeige: benötigte Materiallänge insgesamt, z. B. *12.000 m Material (60 Spulen × 200,00 m)* — ergibt sich aus Zielspulenzahl und Länge pro Spule. Das Rechner-Symbol an dieser Zeile öffnet die Info-Berechnung [Spulzeit](../calculations/winding/winding-time.md), vorbelegt mit den Sollwerten (hier gibt es nichts zu übernehmen — das Fenster dient der Information). |

### Farbaufschlüsselung

Tabelle, die zeigt, wie viele Spulen **je Materialfarbe** zu bewickeln sind —
abgeleitet aus der Klöppel-Tabelle des Flechtdesigns im verknüpften
Flechtauftrag.

| Spalte | Inhalt |
|---|---|
| **Farbe** | Farbfeld (Zellhintergrund in der Materialfarbe). |
| **Bezeichnung** | Farbbezeichnung gemäß der Auswahl **Anzeige**. |
| **Klöppel** | Wie viele Klöppel des Designs diese Farbe tragen (Anzeige). |
| **Spulen** | Zu bewickelnde Spulen dieser Farbe — **editierbar**, falls Sie manuell anpassen möchten. |

Bedienelemente unter der Tabelle:

* **Aus Flechtauftrag aktualisieren** — liest die Farbaufschlüsselung neu
  aus dem Design des verknüpften Flechtauftrags ein; die Spulenzahl je Farbe
  ergibt sich aus den Klöppeln dieser Farbe und den benötigten Spulensätzen.
  Ohne Verknüpfung bzw. ohne Design im Flechtauftrag erscheint ein
  entsprechender Hinweis.
* **Anzeige** — Farbbezeichnung als **Farbname**, **Kennung**, **Hex-Wert**
  oder **Pantone**. Die Einstellung ist mit der Klöppel-Tabelle im
  [Flechtauftrag](braiding-order.md#unter-tabs-ubersicht-und-kloppel-tabelle)
  gemeinsam.
* **Summenzeile** — zeigt *Summe: n Spulen*. Weicht die Summe von der
  Zielspulenzahl ab, erscheint eine Warnung direkt daneben.

!!! info "Automatischer Abgleich"
    Beim Öffnen des Spulauftrags aktualisiert sich die Farbaufschlüsselung
    automatisch aus dem verknüpften Flechtauftrag — aber nur, solange Sie
    die Spulenzahlen nicht manuell verändert haben. Manuell angepasste
    Tabellen bleiben unangetastet; dafür gibt es die Schaltfläche
    **Aus Flechtauftrag aktualisieren**.

### Wickelparameter (optional)

Alle Felder dieses Abschnitts sind optional; 0 bzw. der erste Eintrag steht
für *Nicht gesetzt*.

| Feld | Bedeutung / Auswahl |
|---|---|
| **Wickelart** | *Nicht gesetzt*, **Parallelwicklung**, **Kreuzwicklung**, **Präzisionswicklung**. |
| **Verlegeschritt** | Verlegeschritt in mm. |
| **Fadenspannung** | Fadenspannung in cN. Das Rechner-Symbol öffnet die Berechnung [Fadenspannung](../calculations/winding/yarn-tension.md), vorbelegt mit dem gewählten Material; **Übernehmen** schreibt den Richtwert zurück. |
| **Geschwindigkeitsführung** | *Nicht gesetzt*, **Konstante Spindeldrehzahl**, **Konstante Fadengeschwindigkeit**. |
| **Spindeldrehzahl** | Drehzahl in UpM. |
| **Fadengeschwindigkeit** | Geschwindigkeit in m/min. Das Rechner-Symbol öffnet die Berechnung [Fadengeschwindigkeit](../calculations/winding/line-speed.md) (Umrechnung Drehzahl ↔ Geschwindigkeit über den Wickeldurchmesser); **Übernehmen** schreibt das Ergebnis in Fadengeschwindigkeit und Spindeldrehzahl zurück. |
| **Wickelrichtung** | *Nicht gesetzt*, **S-Wicklung**, **Z-Wicklung**. |
| **Bemerkung** | Freitext mit Hinweisen für die Spulerei. |

## Speichern

**Spulauftrag speichern** (oben rechts) sichert den Auftrag; eine kurze
Erfolgsmeldung bestätigt das Speichern. Voraussetzung: mindestens ein
**Auftragsname oder eine Auftragsnummer** ist eingetragen — sonst weist eine
Meldung darauf hin. Das Speichern und das Ändern der Verknüpfung setzen das
Recht voraus, Aufträge zu bearbeiten — siehe
[Rollen und Rechte](../admin/roles.md).

## Verwandte Seiten

* [Auftragsübersicht](index.md) — Spulaufträge suchen, duplizieren, löschen
* [Flechtauftrag-Editor](braiding-order.md) — der Auftrag, für den gespult wird
* [Drucken](print.md) — Spulauftrag mit der Spulauftrags-Vorlage drucken
* [Spulen für einen Flechtauftrag planen](../tasks/plan-winding.md) — der Ablauf als Anleitung
* [Spulerei-Berechnungen](../calculations/winding/index.md) — Spulzeit, Spulenkapazität, Fadenspannung u. a.
* [Spulmaschinen](../master-data/winding-machines.md) · [Materialien](../master-data/materials.md) · [Spulen](../master-data/bobbins.md) — die zugehörigen Stammdaten
