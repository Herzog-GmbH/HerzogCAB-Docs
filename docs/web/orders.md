# Aufträge (Web-App)

!!! abstract "Referenz — Das Modul Aufträge der Web-App: Auftragsliste, Flechtauftrag-Editor, Spulauftrag-Editor und Druck"

## Wofür Sie diesen Bereich nutzen

Unter **Aufträge** verwalten Sie Flecht- und Spulaufträge Ihres Kontos —
dieselben Aufträge, die auch die Desktop-App kennt, wenn Sie den
Arbeitsbereich [importieren](import.md) oder per Cloud-Upload abgleichen.
Die Editoren entsprechen Feld für Feld denen der Desktop-App; diese Seite
beschreibt die Bedienung in der Web-App und verweist für die Bedeutung der
Felder auf die Referenzseiten der Desktop-App.

## Auftragsliste

![Auftragsliste der Web-App mit Suche, Filtern und Statusspalte.](../assets/screenshots/web/auftraege.png)

| Element | Bedeutung |
|---|---|
| **Neuer Flechtauftrag** / **Neuer Spulauftrag** | Öffnen einen leeren Editor (rechts neben dem Seitentitel). |
| **Suche** | Filtert live nach Auftragsname, Nummer, Kunde oder Maschine. |
| **Auftragsart** | *Alle Auftragsarten*, *Flechtaufträge*, *Spulaufträge*. |
| **Status** | *Alle Status* oder ein Status: Entwurf, Freigegeben, In Produktion, Abgeschlossen. |
| **Maschine** | *Alle Maschinen* oder eine Maschine aus Ihrem Maschinenpark. |
| Trefferzahl | *n Aufträge im Workspace* bzw. *n von m Aufträgen sichtbar*. |

Die Tabelle zeigt **Nr.**, **Auftragsname**, **Kunde**, **Zeitraum**
(Produktion von–bis), **Design** (Name oder *Kein Design verknüpft*) und
**Status**. Den Status ändern Sie direkt in der Zeile über die Auswahlliste —
die Änderung wird sofort gespeichert. Spulaufträge tragen den Zusatz
*Schritt 1 (Spulen) für Flechtauftrag: …*, Flechtaufträge nennen die Zahl
ihrer verknüpften Spulaufträge.

| Aktion in der Zeile | Wirkung |
|---|---|
| **Öffnen** (oder Klick auf die Zeile) | Öffnet den Editor. |
| **Spulauftrag erstellen** | Nur bei Flechtaufträgen: legt einen verknüpften Spulauftrag an, vorbelegt mit Kunde, Material, Spulenformat, Termin und Sollwerten. |
| **Löschen** | Mit Sicherheitsabfrage. Hat ein Flechtauftrag verknüpfte Spulaufträge, bleiben diese bestehen und verlieren nur die Verknüpfung. |

Auf schmalen Bildschirmen erscheint die Liste als Karten. Ein Zeitraumfilter
und **Duplizieren** gibt es — anders als in der Desktop-App — in der Web-App
nicht.

## Flechtauftrag-Editor

Der Editor hat dieselben neun Reiter wie der
[Flechtauftrag-Editor der Desktop-App](../orders/braiding-order.md):
**Kunde**, **Auftrag**, **Maschine**, **Material**, **Spule**, **Produkt**,
**Produktion**, **Design**, **Übersicht**. Die Bedeutung jedes Felds steht
dort — hier nur die Besonderheiten der Web-App:

![Flechtauftrag-Editor der Web-App, Reiter „Auftrag".](../assets/screenshots/web/flechtauftrag.png)

* Die Kopfzeile zeigt Auftragsname und Nummer, den Vermerk *ungespeichert*
  bei offenen Änderungen sowie **Zur Auftragsliste**, **Drucken** und
  **Auftrag speichern**.
* **Kunde**, **Maschine**, **Material** und **Spule** wählen Sie aus den
  Stammdaten des Kontos; die Schaltflächen **Kunden öffnen**,
  **Flechtmaschinen öffnen**, **Materialverwaltung öffnen** und
  **Spule-Verwaltung öffnen** springen in die jeweilige Pflege. Nicht mehr
  vorhandene Einträge stehen als *… (nicht mehr vorhanden)* im Feld.
* Die **Rechner-Symbole** neben den Feldern der Reiter Produkt und
  Produktion öffnen den jeweiligen Rechner als Dialog, vorbelegt mit den
  Auftragswerten; **Übernehmen** schreibt das Ergebnis zurück. Der Rechner
  *Flechtwinkel über Abzug* ist in der Web-App nicht enthalten.
* **Produktion von / bis** und **Produktionsende aus Hochrechnung
  übernehmen** arbeiten wie am Desktop mit 8 Produktionsstunden je
  Arbeitstag.
* Der Reiter **Design** zeigt das verknüpfte Design mit Vorschau und der
  Klöppel-Tabelle; **Design öffnen** wechselt in den [Designer](designer.md),
  **Neues Design** legt ein neues an.
* **Spulaufträge (Vorstufe)** listet die verknüpften Spulaufträge; neue
  legen Sie nach dem Speichern über die Auftragsliste an.

## Spulauftrag-Editor

Der Spulauftrag ist wie in der Desktop-App in drei Bereiche gegliedert —
**Auftrag** (Verknüpfung, Grunddaten, Kunde), **Material und Spule**
(Standardmaterial, Spulenformat, Länge pro Spule, Zielspulenzahl,
Gesamtlänge, Farbaufschlüsselung, Wickelparameter) und **Maschinen und
Zeitplan** (Spulmaschinen, Verteilung, Spulzeit, Produktionszeitraum). Die
Felder erklärt der [Spulauftrag-Editor der Desktop-App](../orders/winding-order.md).

![Spulauftrag-Editor der Web-App mit Farbaufschlüsselung.](../assets/screenshots/web/spulauftrag.png)

Besonderheiten der Web-App:

* Beim Verknüpfen eines Flechtauftrags fragt ein Dialog, ob Kunde,
  Material, Spulenformat, Produktionstermin und Sollwerte übernommen werden
  sollen (**Übernehmen** oder **Nur verknüpfen**).
* Warnungen erscheinen als Hinweisboxen: abweichende Spulenzahl, fehlende
  Wickelzeit, oder wenn das Spul-Ende nach dem Flechtbeginn des verknüpften
  Auftrags liegt.
* Der Rechner **Spulzeit-Details** ist in der Web-App nicht enthalten; die
  Spulzeit-Hochrechnung selbst ist vorhanden.

## Drucken

**Drucken** in der Kopfzeile öffnet die [Druckseite](print.md) mit der
Standardvorlage für Flecht- bzw. Spulaufträge.

## Verwandte Seiten

* [Flechtauftrag-Editor (Desktop-App)](../orders/braiding-order.md) — Bedeutung aller Felder
* [Spulauftrag-Editor (Desktop-App)](../orders/winding-order.md)
* [Vom Kundenauftrag zum Maschinenzettel](../tasks/order-to-machine-sheet.md) — der Ablauf
* [Drucken (Web-App)](print.md)
