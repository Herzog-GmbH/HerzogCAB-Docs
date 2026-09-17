# Spulauftrag-Editor

!!! abstract "Referenz — Spulauftrag anlegen und bearbeiten: Verknüpfung zum Flechtauftrag, Material und Spulen, Farbaufschlüsselung, Wickelparameter, Spulmaschinen mit Verteilung, Spulzeit und Produktionszeitraum."

## Wofür Sie diesen Bereich nutzen

Ein **Spulauftrag** plant die Arbeit der Spulerei: Wie viele Spulen werden
mit welchem Material und welcher Fadenlänge bewickelt, auf welchen
Spulmaschinen, mit welchen Wickelparametern — und wie lange dauert das.
Meist ist der Spulauftrag die Vorstufe („Schritt 1") eines Flechtauftrags:
Die bewickelten Spulen werden anschließend in die Klöppel der Flechtmaschine
eingesetzt. Ein Spulauftrag kann aber auch **für sich stehen**, ohne
verknüpften Flechtauftrag — dann pflegen Sie Farbaufschlüsselung und
Sollwerte von Hand.

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
    **Motiv:** Spulauftrag-Editor mit Kopfzeile (**Zur Auftragsübersicht**, **Drucken**, **Spulauftrag speichern**) und den drei Karten „Auftrag", „Spulerei — was wird gespult?" und „Maschinen und Zeitplan" auf einer Scroll-Seite; verknüpfter Flechtauftrag, gefüllte Farbaufschlüsselung und zwei Spulmaschinen in der Verteiltabelle
    **So erzeugen:** In der Auftragsübersicht einen Flechtauftrag mit Design anwählen und **Spulauftrag erstellen** klicken; zwei Spulmaschinen hinzufügen, **Spulen gleichmäßig verteilen**
    **Ziel-Datei:** `assets/screenshots/orders/spulauftrag-editor.png`

Oben links bringt Sie **Zur Auftragsübersicht** zurück zur
[Auftragsübersicht](index.md). Oben rechts liegen **Drucken** (öffnet die
[Druckausgabe](print.md) mit der Spulauftrags-Standardvorlage) und
**Spulauftrag speichern**.

Der Editor ist **eine** Scroll-Seite mit drei nummerierten Karten — von oben
nach unten in der Reihenfolge, in der Sie planen:

| Karte | Inhalt |
|---|---|
| **1 · Auftrag** | Verknüpfter Flechtauftrag, Name, Nummer, Status, Datum, Kunde. |
| **2 · Spulerei — was wird gespult?** | Standardmaterial, Spulenformat, Länge pro Spule, Zielspulenzahl, Gesamtlänge, Farbaufschlüsselung, Wickelparameter (einklappbar). |
| **3 · Maschinen und Zeitplan** | Wickelzeit je Spule, Spulmaschinen mit Verteilung, Spulzeit-Hochrechnung, Produktionszeitraum. |

## Karte 1: Auftrag

### Verknüpfter Flechtauftrag

Zeigt, für welchen Flechtauftrag dieser Spulauftrag die Spulen fertigt —
z. B. *Schritt 1 (Spulen) für: Abschleppseil (Nr. A-2026-015)*. Ohne
Verknüpfung steht hier *Kein Flechtauftrag verknüpft*; wurde der verknüpfte
Auftrag gelöscht, wird auch das angezeigt.

| Schaltfläche | Wirkung |
|---|---|
| **Flechtauftrag wählen…** | Öffnet eine Liste aller Flechtaufträge. Nach der Auswahl (Doppelklick oder **Verknüpfen**) bietet Herzog CAB an, Kunde, Material, Spulenformat, Produktionstermin und Sollwerte (Zielspulenzahl, Länge pro Spule) aus dem Flechtauftrag zu übernehmen (**Daten übernehmen**) — bereits eingegebener Auftragsname, Nummer und Wickelparameter bleiben dabei erhalten. |
| **Öffnen** | Öffnet den verknüpften Flechtauftrag im [Flechtauftrag-Editor](braiding-order.md). Nur aktiv, wenn der verknüpfte Auftrag existiert. |
| **Verknüpfung lösen** | Entfernt die Verknüpfung. Der Spulauftrag bleibt mit allen Werten bestehen und wechselt in den manuellen Modus (siehe Farbaufschlüsselung). |

### Grunddaten

| Feld | Bedeutung |
|---|---|
| **Auftragsname** | Frei wählbarer Name, z. B. *Spulen für Seilauftrag 4711*. |
| **Auftragsnummer** | Ihre Auftragsnummer. Bei aus einem Flechtauftrag erzeugten Spulaufträgen ist sie mit *&lt;Nummer&gt;-SP* vorbelegt. |
| **Status** | *Entwurf*, *Freigegeben*, *In Produktion* oder *Abgeschlossen* — gleiche Bedeutung wie beim [Flechtauftrag](index.md#status-eines-auftrags). |
| **Auftragsdatum** | Datum des Auftrags, mit Kalenderauswahl. |
| **Kunde** | Auswahlliste mit **Kein Kunde**, den Kunden aus den [Kundenstammdaten](../master-data/customers.md) und — falls der Auftrag Kundendaten trägt, die keinem Stammdateneintrag entsprechen — **Übernommen: &lt;Name&gt;**. Darunter fasst eine Infozeile den gewählten Kunden zusammen. |

## Karte 2: Spulerei — was wird gespult?

Die Felder stehen in der Reihenfolge der Rechenkette: Material und
Spulenformat bestimmen die Länge pro Spule, Länge und Gesamtbedarf die
Zielspulenzahl.

| Feld | Bedeutung |
|---|---|
| **Standardmaterial** | Material aus den [Material-Stammdaten](../master-data/materials.md). Treibt Spulenkapazität, Gewicht und Gesamtlänge; in der Farbaufschlüsselung lässt es sich **je Zeile abweichend** wählen. Nicht mehr vorhandene Einträge stehen als *… (nicht mehr vorhanden)* im Feld. |
| **Spulenformat** | Spulenformat aus den [Spulen-Stammdaten](../master-data/bobbins.md), angezeigt mit Abmessungen und Volumen. |
| **Länge pro Spule** | Fadenlänge je Spule in Metern. Das Rechner-Symbol öffnet die Berechnung [Spulenkapazität](../calculations/winding/bobbin-capacity.md), vorbelegt mit Spulenformat und Material; **Übernehmen** schreibt das Ergebnis zurück. |
| **Zielspulenzahl** | Wie viele Spulen insgesamt bewickelt werden sollen; 0 wird als *Nicht gesetzt* angezeigt. Bei der Übernahme aus dem Flechtauftrag vorbelegt (aus Spulensätzen und aktiven Klöppeln). Das Rechner-Symbol öffnet **Zielspulenzahl aus Gesamtlänge** (siehe unten). |
| **Gesamtlänge** | Anzeige: *n m Material (Spulen × Länge)*, ergänzt um das Materialgewicht *≈ n kg* (aus Länge und Feinheit des Materials). |

Bei einem aus dem Flechtauftrag erzeugten Spulauftrag sind Material und
Spulenformat bereits passend vorbelegt: Es wird dasselbe Material auf
dasselbe Spulenformat gewickelt, das später auf der Flechtmaschine läuft.

### Rechner „Zielspulenzahl aus Gesamtlänge"

| Element | Bedeutung |
|---|---|
| **Benötigte Gesamtlänge** | Gesamt zu spulende Materiallänge in Metern (z. B. 5.000 m). |
| **Spulen pro Spulensatz** | Wie viele Spulen ein Satz auf der Flechtmaschine braucht; **Aus Flechtmaschine…** übernimmt die aktiven Klöppel einer Flechtmaschine aus den Stammdaten. |
| Ergebnis | *Ergibt n Spulen — die Zielspulenzahl wird auf n gesetzt* und *Das entspricht m Spulensätzen (à k Spulen)*. **Übernehmen** schreibt die Zielspulenzahl. |

Voraussetzung ist eine eingetragene **Länge pro Spule**.

### Farbaufschlüsselung

Tabelle, wie viele Spulen **je Farbe und Material** zu bewickeln sind. Sie
arbeitet in zwei Modi:

| | Verknüpfter Flechtauftrag | Ohne Verknüpfung (manuell) |
|---|---|---|
| Woher die Zeilen kommen | Aus der Klöppel-Tabelle des Designs im Flechtauftrag; **Aus Flechtauftrag aktualisieren** liest sie neu ein. | Sie legen die Zeilen selbst an (**Zeile hinzufügen…**, **Zeile entfernen**). |
| Spalte **Klöppel/Satz** | Anzeige: Klöppel des Designs mit dieser Farbe. | ausgeblendet |
| Spalte **Spulen** | berechnet aus Klöppeln je Satz und Spulensätzen, nur lesbar | **editierbar** — absolute Spulenzahl je Zeile |
| Summenzeile | *Klöppel/Satz: n von k* (⚠, wenn die Summe nicht zur Maschine passt) · *Spulen: m* | *Spulen gesamt: m · entspricht s Spulensätzen (à k)* |

| Spalte / Element | Bedeutung |
|---|---|
| **Farbe** | Farbfeld. Doppelklick (bzw. **Zeile hinzufügen…**) öffnet die Auswahl **Farbe wählen** aus den [Farben-Stammdaten](../master-data/colors.md) oder **Freie Farbe…** über den Farbwähler. |
| **Bezeichnung** | Farbbezeichnung gemäß der Auswahl **Anzeige**. |
| **Material** | Auswahlliste je Zeile; Standard ist das Standardmaterial des Auftrags. |
| **Anzeige** | Farbbezeichnung als **Farbname**, **Kennung**, **Hex-Wert** oder **Pantone**. Die Einstellung ist mit der Klöppel-Tabelle im [Flechtauftrag](braiding-order.md#unter-tabs-ubersicht-und-kloppel-tabelle) gemeinsam. |
| Warnung | Weicht die Spulensumme von der Zielspulenzahl ab, steht das direkt neben der Summe. |

!!! info "Automatischer Abgleich"
    Beim Öffnen eines verknüpften Spulauftrags aktualisiert sich die
    Farbaufschlüsselung automatisch aus dem Flechtauftrag — aber nur,
    solange Sie die Tabelle nicht von Hand verändert haben. Manuell
    angepasste Tabellen bleiben unangetastet; dafür gibt es die Schaltfläche
    **Aus Flechtauftrag aktualisieren**.

### Wickelparameter (optional)

Der Abschnitt ist eingeklappt; **Wickelparameter anzeigen (optional)**
öffnet ihn (**Wickelparameter ausblenden** schließt ihn wieder). Sind
Werte gesetzt, ist er beim Öffnen des Auftrags bereits aufgeklappt. Alle
Felder sind optional; 0 bzw. der erste Eintrag steht für *Nicht gesetzt*.
Die Werte fließen in die Wickelzeit ein (Karte 3).

| Feld | Bedeutung / Auswahl |
|---|---|
| **Wickelart** | *Nicht gesetzt*, **Parallelwicklung**, **Kreuzwicklung**, **Präzisionswicklung**. |
| **Verlegeschritt** | Verlegeschritt in mm. |
| **Fadenspannung** | Fadenspannung in cN. Das Rechner-Symbol öffnet die Berechnung [Fadenspannung](../calculations/winding/yarn-tension.md), vorbelegt mit dem gewählten Material; **Übernehmen** schreibt den Richtwert zurück. |
| **Geschwindigkeitsführung** | *Nicht gesetzt*, **Konstante Spindeldrehzahl**, **Konstante Fadengeschwindigkeit**. |
| **Spindeldrehzahl** | Umdrehungen der Spindel pro Minute (UpM), auf der die Spule sitzt. |
| **Fadengeschwindigkeit** | Geschwindigkeit in m/min. Das Rechner-Symbol öffnet die Berechnung [Fadengeschwindigkeit](../calculations/winding/line-speed.md) (Umrechnung Drehzahl ↔ Geschwindigkeit über den Wickeldurchmesser); **Übernehmen** schreibt das Ergebnis in Fadengeschwindigkeit und Spindeldrehzahl zurück. |
| **Wickelrichtung** | *Nicht gesetzt*, **S-Wicklung**, **Z-Wicklung**. |
| **Bemerkung** | Freitext mit Hinweisen für die Spulerei. |

## Karte 3: Maschinen und Zeitplan

### Wickelzeit je Spule

| Element | Bedeutung |
|---|---|
| **Wickelzeit je Spule** | Zeit in Minuten für eine Spule. Leer = Herzog CAB ermittelt sie selbst: **aus Länge ÷ Fadengeschwindigkeit** (wenn die Fadengeschwindigkeit gesetzt ist) oder **geschätzt aus Spindeldrehzahl und mittlerem Wickel-Ø** (wenn nur die Spindeldrehzahl und das Spulenformat bekannt sind). Ein eingetragener Wert gilt als **manuell vorgegeben** und schlägt beide. Die Quelle steht unter dem Feld: *Wickelzeit je Spule: 4:12 (aus Länge ÷ Fadengeschwindigkeit)*. |

Ist keine Wickelzeit ermittelbar, nennt eine Meldung die Möglichkeiten:
Fadengeschwindigkeit, Spindeldrehzahl mit Spulenformat, Wickelzeit je Spule
oder eine Geschwindigkeit je Maschine in der Tabelle.

### Spulmaschinen (Verteiltabelle)

Ein Spulauftrag kann auf **mehrere Spulmaschinen** verteilt werden. Jede
Zeile ist eine Maschine:

| Spalte | Bedeutung |
|---|---|
| **Maschine** | Spulmaschine aus den [Spulmaschinen-Stammdaten](../master-data/winding-machines.md); Flechtmaschinen erscheinen hier nicht. Nicht mehr vorhandene Maschinen sind gekennzeichnet. |
| **Spulstellen** | Anzahl der Spulstellen der Maschine (aus den Stammdaten). |
| **Spulen** | Anzahl der Spulen, die diese Maschine wickelt — **per Doppelklick direkt editierbar**. |
| **Einrichtzeit (min)** | Einmalige Rüstzeit je Auftrag; vorbelegt aus den Stammdaten der Maschine, hier übersteuerbar. |
| **Bestückung je Spule (min)** | Zeit für den Spulenwechsel je Spule; vorbelegt aus den Stammdaten. |
| **Geschwindigkeit (m/min)** | Optionale Fadengeschwindigkeit nur für diese Maschine; leer = Auftragswert. Ein Wert hier gilt vor der globalen Wickelzeit. |
| **Zeit** | Berechnete Zeit dieser Maschine: Einrichtzeit + Zyklen × Wickelzeit je Spule + Spulen × Bestückung, wobei ein Zyklus so viele Spulen wickelt, wie die Maschine Spulstellen hat. |

| Schaltfläche | Wirkung |
|---|---|
| **Maschine hinzufügen…** | Öffnet die Auswahl **Spulmaschine hinzufügen** (Karten mit Name und Spulstellen); bereits zugewiesene Maschinen fehlen in der Liste. Die neue Maschine bekommt die noch nicht verteilten Spulen. |
| **Entfernen** | Nimmt die gewählte Maschine aus der Tabelle. |
| **Spulen gleichmäßig verteilen** | Verteilt die Zielspulenzahl im Verhältnis der Spulstellen auf alle Maschinen — jede Maschine läuft dann gleich viele Zyklen. Voraussetzung: mindestens eine Maschine und eine Zielspulenzahl. |
| **Spulzeit-Details…** | Öffnet die Info-Berechnung [Spulzeit](../calculations/winding/winding-time.md), vorbelegt mit den Werten des Auftrags (zur Information — hier gibt es nichts zu übernehmen). |

Unter der Tabelle fasst eine **Zeit-Kachel** zusammen: je Maschine die
Zeit, darunter **Gesamtdauer (parallel)** — die längste Maschinenzeit, weil
die Maschinen gleichzeitig laufen — sowie *Materialgewicht gesamt*. Eine
Warnung erscheint, wenn die zugewiesenen Spulen von der Zielspulenzahl
abweichen (*⚠ Zugewiesene Spulen (n) weichen von der Zielspulenzahl (m)
ab.*) oder noch keine Maschine zugewiesen ist.

### Produktionszeitraum

| Feld | Bedeutung |
|---|---|
| **Produktion von** | Geplanter Beginn der Spulerei, mit Kalenderauswahl. Bei der Übernahme aus einem Flechtauftrag rückwärts terminiert: Das Spul-Ende liegt am Flechtbeginn. |
| **Produktion bis** | Geplantes Ende. **Aus Hochrechnung übernehmen** setzt es auf Beginn + Gesamtdauer, umgerechnet über die *Produktionsstunden je Arbeitstag* aus den [Einstellungen](../admin/settings/appearance.md#produktionsplanung); Wochenenden werden übersprungen. |

Liegt das Spul-Ende nach dem Flechtbeginn des verknüpften Flechtauftrags,
warnt der Editor — die Spulen wären nicht rechtzeitig fertig. Die Warnung
blockiert das Speichern nicht.

## Speichern

**Spulauftrag speichern** (oben rechts) sichert den Auftrag; eine kurze
Erfolgsmeldung bestätigt das Speichern. Voraussetzung: mindestens ein
**Auftragsname oder eine Auftragsnummer** ist eingetragen — sonst weist eine
Meldung darauf hin. Verlassen Sie den Editor mit ungespeicherten Änderungen,
fragt Herzog CAB nach (**Speichern**, **Nicht speichern**, **Abbrechen**).
Das Speichern und das Ändern der Verknüpfung setzen das Recht voraus,
Aufträge zu bearbeiten — siehe [Rollen und Rechte](../admin/roles.md).

## Verwandte Seiten

* [Auftragsübersicht](index.md) — Spulaufträge suchen, duplizieren, löschen
* [Flechtauftrag-Editor](braiding-order.md) — der Auftrag, für den gespult wird
* [Drucken](print.md) — Spulauftrag mit der Spulauftrags-Vorlage drucken
* [Spulen für einen Flechtauftrag planen](../tasks/plan-winding.md) — der Ablauf als Anleitung
* [Spulerei-Berechnungen](../calculations/winding/index.md) — Spulzeit, Spulenkapazität, Fadenspannung u. a.
* [Spulmaschinen](../master-data/winding-machines.md) · [Materialien](../master-data/materials.md) · [Spulen](../master-data/bobbins.md) — die zugehörigen Stammdaten
* [Spulauftrag in der Web-App](../web/orders.md)
