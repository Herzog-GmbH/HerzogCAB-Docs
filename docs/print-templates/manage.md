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
| **Neue Vorlage** | Legt eine neue, leere Vorlage an. |
| **Speichern** | Sichert die aktuelle Vorlage mit allen Änderungen. |
| **Vorlage löschen** | Entfernt die aktuelle Vorlage (mit Sicherheitsabfrage). |
| **Verwendung** | Legt fest, wofür die Vorlage gilt: Berechnung, Design oder Auftrag. Siehe [Editor-Aufbau](editor.md). |

Beim Verlassen des Editors mit ungespeicherten Änderungen fragt Herzog CAB
nach, ob Sie zuerst speichern oder die Änderungen verwerfen möchten.

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
