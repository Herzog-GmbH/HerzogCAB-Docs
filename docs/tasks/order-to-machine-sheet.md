# Vom Kundenauftrag zum Maschinenzettel

!!! example "Anleitung — am Ende haben Sie einen vollständigen, gedruckten Flechtauftrag, der einer Maschine zugewiesen ist und im Maschinenpark erscheint"

**Voraussetzungen:**

* Die [Stammdaten](../master-data/index.md) sind gepflegt: mindestens ein
  [Material](../master-data/materials.md), eine
  [Spule](../master-data/bobbins.md) und eine
  [Flechtmaschine](../master-data/braiding-machines.md).
* Sie haben die Berechtigung, Kunden und Aufträge anzulegen (bei Fragen:
  [Rollen und Berechtigungen](../admin/roles.md)).
* Optional: ein fertiges Design in der
  [Design-Bibliothek](../master-data/designs.md) — Sie können es aber auch
  unterwegs anlegen.

```mermaid
flowchart LR
  A["Kunde anlegen"] --> B["Design & Material bereitstellen"]
  B --> C["Flechtauftrag anlegen"]
  C --> D["Berechnungen nutzen"]
  D --> E["Drucken"]
  E --> F["Maschinenpark prüfen"]
```

## Schritt 1: Kunde anlegen

1. Öffnen Sie *Stammdaten > Kunden* und klicken Sie auf **Neuer Kunde**.
2. Erfassen Sie die Kundendaten und klicken Sie auf **Speichern**.

Alle Felder des Kundenformulars sind auf der Referenzseite
[Kunden](../master-data/customers.md) erklärt. Neu gespeicherte Kunden stehen
sofort in der Kunden-Auswahl des Auftrags-Editors zur Verfügung.

!!! tip "Abkürzung"
    Sie können den Kunden auch später direkt aus dem Auftrag heraus anlegen —
    der Flechtauftrag-Editor bietet dafür eine eigene Schaltfläche im Tab
    **Kunde** (siehe [Flechtauftrag-Editor](../orders/braiding-order.md)).

## Schritt 2: Design und Material bereitstellen

1. Prüfen Sie, ob das gewünschte Design in der
   [Design-Bibliothek](../master-data/designs.md) vorhanden ist. Falls nicht,
   entwerfen Sie es zuerst — der Ablauf
   [Ein Design entwerfen und drucken](design-from-scratch.md) führt Sie durch
   den Designer.
2. Prüfen Sie unter *Stammdaten > Materialien*, ob das Flechtmaterial mit
   Dichte und Titer erfasst ist (Referenz:
   [Materialien](../master-data/materials.md)).

## Schritt 3: Flechtauftrag anlegen

1. Öffnen Sie den Navigationspunkt **Aufträge** (Referenz:
   [Auftragsübersicht](../orders/index.md)).
2. Klicken Sie auf **Neuer Auftrag** und wählen Sie **Neuer Flechtauftrag**.
   Der [Flechtauftrag-Editor](../orders/braiding-order.md) öffnet sich.
3. Arbeiten Sie die Tabs von links nach rechts durch: **Kunde**, **Auftrag**,
   **Maschine**, **Material**, **Spule**, **Produkt**, **Produktion**,
   **Design**. Was jedes Feld bedeutet, steht auf der Referenzseite —
   hier nur die wichtigsten Stationen:
    * Im Tab **Maschine** wählen Sie die Flechtmaschine aus Ihren Stammdaten.
      Damit ist der Auftrag der Maschine zugewiesen und erscheint später im
      Maschinenpark.
    * Im Tab **Design** laden Sie das Design aus der Bibliothek oder legen
      über **Neues Design** direkt ein neues an.
4. Klicken Sie auf **Auftrag speichern**.

## Schritt 4: Berechnungen nutzen

Viele Felder im Auftrag haben direkt daneben ein **Rechner-Symbol**, das
die passende Berechnung als Fenster öffnet (z. B. Flechtwinkel oder
Produktlänge) — das Ergebnis wird in den Auftrag übernommen. Der gemeinsame
Aufbau aller Berechnungsseiten ist unter
[So sind Berechnungsseiten aufgebaut](../basics/calc-page-anatomy.md)
beschrieben; alle verfügbaren Berechnungen finden Sie im Kapitel
[Berechnungen](../calculations/index.md).

## Schritt 5: Übersicht prüfen

Wechseln Sie in den Tab **Übersicht**. Er fasst den kompletten Auftrag
zusammen; der Unter-Tab **Klöppel-Tabelle** zeigt die Besetzung mit Farben je
Klöppelposition (Details: [Flechtauftrag-Editor](../orders/braiding-order.md)).

## Schritt 6: Maschinenzettel drucken

1. Klicken Sie im Auftrag auf **Drucken**.
2. Sind mehrere Druckvorlagen vorhanden, wählen Sie im Dialog
   **Druckvorlage wählen** die gewünschte Vorlage (z. B. *Standard Auftrag*).
3. Prüfen Sie die Druckvorschau und starten Sie den Druck.

Der Ausdruck ist der Produktionsbegleitschein („Maschinenzettel") für die
Werkstatt. Details zur Vorschau und zum QR-Code, über den der Bediener die
mobile Auftragssicht am Smartphone öffnet, stehen unter
[Auftrag drucken](../orders/print.md). Aussehen und Inhalt des Ausdrucks
steuern Sie über eigene [Druckvorlagen](../print-templates/index.md) — siehe
Ablauf [Eine Druckvorlage erstellen](create-print-template.md).

## Schritt 7: Maschine im Maschinenpark prüfen

Öffnen Sie den Navigationspunkt **Maschinenpark** (Referenz:
[Maschinenpark](../machine-park/index.md)). Die in Schritt 3 gewählte
Maschine zeigt jetzt den Auftrag in ihrer Liste der zugewiesenen Aufträge;
die Status-Ampel der Maschine richtet sich nach dem Auftragsstatus. Den
Status selbst (Entwurf, Freigegeben, In Produktion, Abgeschlossen) setzen Sie
im Auftrag im Tab **Auftrag**.

## Ergebnis

* Der Flechtauftrag ist gespeichert und erscheint in der
  [Auftragsübersicht](../orders/index.md) sowie unter „Letzte Aufträge" auf
  der [Startseite](../basics/home.md).
* Der Maschinenzettel ist gedruckt.
* Der [Maschinenpark](../machine-park/index.md) zeigt den Auftrag an der
  zugewiesenen Maschine.

## Wenn etwas nicht klappt

* Der Ausdruck sieht falsch aus oder es passiert nichts →
  [Druckprobleme](../help/print-problems.md)
* Sie können keine weiteren Aufträge anlegen (Testversion) →
  [Testversion und Lizenz-Quoten](../basics/trial-quotas.md) und
  [Lizenzprobleme](../help/license-problems.md)
* Schaltflächen sind ausgegraut → Ihnen fehlt vermutlich eine Berechtigung,
  siehe [Rollen und Berechtigungen](../admin/roles.md)
* Weitere Hilfe → [Hilfe-Übersicht](../help/index.md) und
  [Support kontaktieren](../help/support.md)
