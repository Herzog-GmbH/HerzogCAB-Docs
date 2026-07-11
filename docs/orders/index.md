# Aufträge

!!! abstract "Referenz — Auftragsübersicht: alle Flecht- und Spulaufträge suchen, filtern, anlegen und verwalten."

## Wofür Sie diesen Bereich nutzen

Der Auftrag ist die zentrale Arbeitsmappe in Herzog CAB: Er bündelt Kunde,
Maschine, Material, Spule, Produkt, Produktionswerte und Design zu einem
konkreten Kundenauftrag. Über den Navigationspunkt **Aufträge** öffnen Sie die
**Auftragsübersicht** — die Liste aller Aufträge im Workspace. Von hier aus
legen Sie neue Aufträge an, öffnen bestehende im passenden Editor, duplizieren
ähnliche Aufträge als Vorlage und löschen nicht mehr benötigte.

Herzog CAB kennt zwei Auftragsarten:

| Auftragsart | Zweck | Editor |
|---|---|---|
| **Flechtauftrag** | Ein Produkt wird auf einer Flechtmaschine gefertigt. | [Flechtauftrag-Editor](braiding-order.md) |
| **Spulauftrag** | Spulen werden in der Spulerei bewickelt — häufig als Vorstufe („Schritt 1") eines Flechtauftrags. | [Spulauftrag-Editor](winding-order.md) |

Beide Auftragsarten erscheinen gemeinsam in der Übersicht und lassen sich
miteinander verknüpfen: Ein Flechtauftrag kann beliebig viele zugehörige
Spulaufträge haben.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Auftragsübersicht mit Suchfeld, den vier Filtern (Auftragsart, Status, Zeitraum, Sortierung), zeitlich gruppierten Auftragskarten (Flecht- und Spulauftrag gemischt, mit Auftragsart-Chips und Verknüpfungszeile) und der Aktionsleiste unten inkl. **Spulauftrag erstellen**
    **So erzeugen:** Navigationspunkt *Aufträge* öffnen; Workspace „Musterbetrieb" mit mindestens einem Flechtauftrag samt verknüpftem Spulauftrag; einen Flechtauftrag anwählen, damit alle Schaltflächen aktiv sind
    **Ziel-Datei:** `assets/screenshots/orders/auftraege-uebersicht.png`

Der Bildschirm ist von oben nach unten aufgebaut:

1. **Suchfeld und Filter** — Suche, Auftragsart, Status, Zeitraum, Sortierung
2. **Ergebniszeile** — wie viele Aufträge sichtbar sind und welche Filter aktiv sind
3. **Auftragsliste** — Karten, zeitlich gruppiert (z. B. *Heute*, *Diese Woche*, *Juni 2026*)
4. **Aktionsleiste** — **Neuer Auftrag**, **Öffnen**, **Duplizieren**, **Spulauftrag erstellen**, **Löschen**

## Bedienelemente im Detail

### Suchfeld

Freitextsuche über die sichtbaren Auftragsdaten: Auftragsname, Auftragsnummer,
Kundenname, Kundennummer, Maschinenname sowie Auftragsart und Status. Die
Liste filtert sich bei jeder Eingabe sofort; Groß-/Kleinschreibung spielt
keine Rolle.

### Filter „Auftragsart"

| Auswahl | Wirkung |
|---|---|
| **Alle Auftragsarten** | Flecht- und Spulaufträge gemeinsam (Standard). |
| **Flechtaufträge** | Nur Flechtaufträge. |
| **Spulaufträge** | Nur Spulaufträge. |

### Filter „Status"

Zeigt nur Aufträge mit dem gewählten Status: **Alle Status** (Standard),
**Entwurf**, **Freigegeben**, **In Produktion** oder **Abgeschlossen**
(Bedeutung siehe [Status eines Auftrags](#status-eines-auftrags)).

### Filter „Zeitraum"

Grenzt die Liste zeitlich ein: **Alle Zeiträume** (Standard), **Heute**,
**Diese Woche**, **Letzte Woche**, **Dieser Monat** oder **Letzte 30 Tage**.
Maßgeblich ist das **Auftragsdatum**; fehlt es, greift ersatzweise das
Produktionsdatum bzw. das Änderungs- oder Anlagedatum des Auftrags.

### Auswahlliste „Sortierung"

| Auswahl | Reihenfolge |
|---|---|
| **Neueste zuerst** | Nach Auftragsdatum absteigend (Standard). |
| **Älteste zuerst** | Nach Auftragsdatum aufsteigend. |
| **Produktionsdatum** | Nach Produktionsdatum absteigend. |
| **Auftragsdatum** | Nach Auftragsdatum absteigend. |

### Ergebniszeile

Unter den Filtern steht, wie viele Aufträge der Workspace enthält (z. B.
*11 Aufträge im Workspace*). Sobald ein Filter oder eine Suche aktiv ist,
wechselt die Anzeige zu *x von y Aufträgen sichtbar* und nennt die aktiven
Filter. Findet die Kombination aus Suche und Filtern keinen Auftrag, zeigt die
Liste den Hinweis *Keine passenden Aufträge gefunden*.

### Auftragsliste (Karten)

Die Aufträge erscheinen als Karten, gruppiert nach Zeitraum (*Heute*,
*Diese Woche*, *Letzte Woche*, danach Monat und Jahr, zuletzt *Ohne Datum*).
Jede Karte zeigt:

* **Titel** — der Auftragsname; ohne Namen ersatzweise *Auftrag &lt;Nummer&gt;* bzw. *Unbenannter Auftrag*.
* **Auftragsart-Chip** — *Flechtauftrag* (blau) oder *Spulauftrag* (petrol).
* **Status-Chip** — aktueller Status mit farbiger Kennung.
* **Kopfzeile** — Auftragsnummer, Kundenname und Kundennummer.
* **Maschinenzeile** — Maschine, Material und Spulenformat (Außen-/Kerndurchmesser, Wickellänge, Volumen).
* **Verknüpfungszeile** (nur bei verknüpften Aufträgen, mit ⛓-Symbol) — bei einem Spulauftrag: *Schritt 1 (Spulen) für Flechtauftrag: …*; bei einem Flechtauftrag: *n verknüpfte Spulaufträge*. Wurde der verknüpfte Flechtauftrag gelöscht, steht das ebenfalls hier.
* **Fußzeile** — Auftrags- und Produktionsdatum; bei Flechtaufträgen zusätzlich das verknüpfte Design (bzw. *Kein Design verknüpft*), bei Spulaufträgen die Sollwerte (*n Spulen*, *… m/Spule*).

Ein Klick wählt die Karte aus (die Aktionsleiste bezieht sich immer auf die
ausgewählte Karte). Ein **Doppelklick** öffnet den Auftrag direkt im passenden
Editor — Flechtaufträge im [Flechtauftrag-Editor](braiding-order.md),
Spulaufträge im [Spulauftrag-Editor](winding-order.md).

### Schaltfläche „Neuer Auftrag"

Öffnet ein Untermenü mit zwei Einträgen:

* **Neuer Flechtauftrag** — öffnet den leeren [Flechtauftrag-Editor](braiding-order.md).
* **Neuer Spulauftrag** — öffnet den leeren [Spulauftrag-Editor](winding-order.md).

### Schaltfläche „Öffnen"

Öffnet den ausgewählten Auftrag im passenden Editor (gleiche Wirkung wie ein
Doppelklick auf die Karte). Nur aktiv, wenn ein Auftrag ausgewählt ist.

### Schaltfläche „Duplizieren"

Legt eine vollständige Kopie des ausgewählten Auftrags an — der Name erhält
den Zusatz *(Kopie)* — und öffnet sie sofort im Editor. Das spart Zeit, wenn
ein neuer Auftrag einem bestehenden stark ähnelt: Sie passen anschließend nur
die abweichenden Werte an.

### Schaltfläche „Spulauftrag erstellen"

Nur aktiv, wenn ein **Flechtauftrag** ausgewählt ist. Erzeugt aus dem
Flechtauftrag einen **verknüpften Spulauftrag** und öffnet ihn direkt im
[Spulauftrag-Editor](winding-order.md). Übernommen werden Kunde, Material,
Spulenformat, Produktionstermin, die Sollwerte (Zielspulenzahl, Länge pro
Spule) sowie die Farbaufschlüsselung aus dem verknüpften Design. Der neue
Auftrag heißt *Spulen: &lt;Name des Flechtauftrags&gt;*; die Auftragsnummer
erhält den Zusatz *-SP*.

### Schaltfläche „Löschen"

Entfernt den ausgewählten Auftrag nach einer Sicherheitsabfrage. Hat ein
Flechtauftrag verknüpfte Spulaufträge, weist die Abfrage ausdrücklich darauf
hin: Die Spulaufträge **bleiben bestehen**, verlieren aber ihre Verknüpfung.

!!! warning "Löschen lässt sich nicht rückgängig machen"
    Ein gelöschter Auftrag kann nicht wiederhergestellt werden. Im Zweifel
    genügt es, den Status auf *Abgeschlossen* zu setzen.

!!! info "Berechtigungen"
    **Neuer Auftrag**, **Duplizieren**, **Spulauftrag erstellen** und
    **Löschen** setzen das Recht voraus, Aufträge zu bearbeiten. Fehlt es
    Ihrer Rolle, sind die Schaltflächen gesperrt — siehe
    [Rollen und Rechte](../admin/roles.md).

## Status eines Auftrags

Jeder Auftrag trägt einen Status, den Sie im jeweiligen Editor im Tab
**Auftrag** setzen. Er erscheint als farbiger Chip auf der Auftragskarte:

| Status | Bedeutung |
|---|---|
| **Entwurf** | In Bearbeitung, noch nicht freigegeben (Standard für neue Aufträge). |
| **Freigegeben** | Zur Produktion freigegeben. |
| **In Produktion** | Wird aktuell gefertigt. |
| **Abgeschlossen** | Fertiggestellt. |

Die Startseite ([Home](../basics/home.md)) zeigt die Anzahl der Aufträge je
Status; ein Klick auf eine dieser Kacheln öffnet die Auftragsübersicht mit
bereits vorgewähltem Status-Filter. Geöffnete Aufträge landen außerdem im
[Verlauf „Letzte Aufträge"](../basics/history.md).

## In diesem Kapitel

<div class="grid cards" markdown>

- :material-file-document-edit-outline: **Flechtauftrag**

    ---

    Der Flechtauftrag-Editor mit allen Tabs — von Kunde über Maschine,
    Material und Produkt bis zu Design und Übersicht.

    [:octicons-arrow-right-24: Öffnen](braiding-order.md)

- :material-sync: **Spulauftrag**

    ---

    Der Spulauftrag-Editor: Sollwerte der Spulerei, Farbaufschlüsselung,
    Wickelparameter und die Verknüpfung zum Flechtauftrag.

    [:octicons-arrow-right-24: Öffnen](winding-order.md)

- :material-printer: **Drucken**

    ---

    Druckvorlage wählen, Druckvorschau nutzen und den QR-Code für die
    mobile Auftragssicht an der Maschine einrichten.

    [:octicons-arrow-right-24: Öffnen](print.md)

</div>

## Verwandte Seiten

* [Vom Auftrag zum Maschinenschein](../tasks/order-to-machine-sheet.md) — der komplette Ablauf als Anleitung
* [Spulen für einen Flechtauftrag planen](../tasks/plan-winding.md) — Zusammenspiel von Flecht- und Spulauftrag
* [Suchen und Filtern](../basics/search-filter.md) — die gemeinsamen Bedienkonzepte für Listen
* [Home](../basics/home.md) — Status-Kacheln und anstehende Produktionen
* [Kunden](../master-data/customers.md), [Flechtmaschinen](../master-data/braiding-machines.md), [Materialien](../master-data/materials.md), [Spulen](../master-data/bobbins.md) — die Stammdaten, aus denen Aufträge schöpfen
