# Vorlagen verwalten

!!! abstract "Referenz — Druckvorlagen anlegen, wählen, löschen"

Den Druck-Editor öffnen Sie über den Navigationspunkt **Druck Editor**. Oben
wählen Sie die zu bearbeitende Vorlage; rechts finden Sie die Aktionen zum
Verwalten.

![Druck-Editor mit Vorlagen-Auswahl und Aktionen rechts.](../assets/screenshots/print-templates/druck-editor.png)

## Vorlage wählen

Über das Auswahlfeld **Vorlagen** (z. B. *Standard Auftrag*) rechts unten
wechseln Sie zwischen den vorhandenen Vorlagen. Die gewählte Vorlage wird
sofort im Editor angezeigt.

## Aktionen

| Aktion | Wirkung |
|---|---|
| **Neu** (Kurzhinweis *Neue Vorlage*) | Legt eine neue, leere Vorlage an. |
| **Speichern** | Sichert die aktuelle Vorlage mit allen Änderungen. Gibt es ungespeicherte Änderungen, heißt die Schaltfläche **Speichern \*** und ist blau hervorgehoben. Hat ein Kollege dieselbe Vorlage inzwischen gespeichert, fragt Herzog CAB nach (**Überschreiben**, **Als Kopie speichern**, **Neu laden**). Bearbeitet er sie gerade, ist sie für Sie nur lesbar (Schloss in der Vorlagenauswahl, Band *In Bearbeitung – nur lesen*) — siehe [Mehrere Benutzer](../basics/multi-user.md). |
| **Löschen** (Kurzhinweis *Vorlage löschen*) | Entfernt die aktuelle Vorlage (mit Sicherheitsabfrage). |
| **Verwendung** | Legt fest, wofür die Vorlage gilt: Berechnung, Design oder Auftrag, mit dem Flechtsimulator auch **Flechtsimulator** (Schaltplan, Vorlage *Standard Schaltplan*, siehe [Ausgeben](../braiding-simulator/output.md)). Siehe [Editor-Aufbau](editor.md). |

Beim Verlassen des Editors mit ungespeicherten Änderungen fragt Herzog CAB
nach, ob Sie zuerst speichern oder die Änderungen verwerfen möchten.

## Mitgelieferte Standardvorlagen

Herzog CAB bringt Standardvorlagen mit, z. B. *Standard Auftrag*, *Standard
Design* und *Standard Design (hohe Klöppelzahl)*. Welche Design-Vorlage beim
Drucken angeboten wird, steht unter
[Speichern und Drucken](../designer/save-print.md#druck-starten-und-vorlage-wahlen).

Bringt ein Update eine neue Fassung einer Standardvorlage mit, ersetzt Herzog
CAB die Vorlage beim ersten Start einmal je Arbeitsverzeichnis — aber nur,
solange sie noch ihren ursprünglichen Namen trägt. Vorlagen mit anderem Namen
und Ihre eigenen Vorlagen bleiben unverändert. Eine gelöschte Standardvorlage
legt Herzog CAB nicht wieder an.

!!! warning "Eigene Änderungen an einer Standardvorlage behalten"
    Haben Sie eine Standardvorlage angepasst, speichern Sie sie vor dem
    Update unter einem eigenen Namen: Klicken Sie auf **Speichern** und
    geben Sie unter **Name der Vorlage** einen neuen Namen ein. Herzog CAB
    legt damit eine eigene Vorlage an, die ein Update nicht ersetzt.

## Speicherort

Alle Vorlagen liegen als Datei unter `Printouts/templates/` im aktiven
Workspace. Dadurch lassen sie sich auch sichern oder zwischen Arbeitsplätzen
austauschen, die denselben Workspace nutzen.

!!! tip "Mit einer Kopie starten"
    Statt bei Null anzufangen, gehen Sie von der mitgelieferten Vorlage
    *Standard Auftrag* aus: anpassen, unter neuem Namen speichern – fertig.

!!! warning "Berechtigung erforderlich"
    **Vorlagen ansehen** genügt die Berechtigung **Druckvorlagen anzeigen**.
    Zum Anlegen, Ändern, Speichern und Löschen benötigen Sie zusätzlich
    **Druckvorlagen bearbeiten**. Mehr dazu unter [Rollen](../admin/roles.md).

## Verwandte Seiten

* [Editor-Aufbau](editor.md) – Element-Palette, Filter, Seiteneinstellungen
* [Elemente und Platzhalter](elements.md) – alle Bausteine der Element-Palette im Detail
* [Vorschau und Druck](preview-and-print.md) – Seitenformat, Vorschau, Ausgabe
* [Eine Druckvorlage erstellen](../tasks/create-print-template.md) – Schritt-für-Schritt-Anleitung
* [Aufträge → Drucken](../orders/print.md) – wo Auftrags-Vorlagen zum Einsatz kommen
* [Designer → Speichern und Drucken](../designer/save-print.md) – wo Design-Vorlagen zum Einsatz kommen
