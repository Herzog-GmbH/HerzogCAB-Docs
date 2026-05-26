# Rollen und Berechtigungen

Herzog CAB hat ein **rollenbasiertes Rechtesystem**. Statt einzelne
Berechtigungen pro Benutzer zu setzen, weisen Sie Rollen zu - die Rolle
bündelt typische Berechtigungen.

## Eingebaute Rollen

| Rolle              | Zielgruppe                  | Darf typischerweise                                      |
|--------------------|-----------------------------|----------------------------------------------------------|
| **Inhaber**        | Werkstattleiter / Eigentümer | Alles, inkl. Workspace-Verwaltung und Firmen-Einstellungen |
| **Administrator**  | IT / Fachverantwortlicher   | Alles ausser Firmen-Einstellungen                        |
| **Stammdatenpflege** | Datenpfleger              | Stammdaten und Druckvorlagen bearbeiten, Berechnungen nutzen, Aufträge ansehen |
| **Produktion**     | Maschinenbediener           | Berechnungen nutzen, Aufträge bearbeiten, Drucken      |
| **Nur lesen**      | Auszubildende / Gäste      | Alles ansehen, nichts verändern                         |

> :material-image-area: *Screenshot: Rollen-Verwaltungs-Dialog*

## Verfügbare Berechtigungen

Eine Rolle ist eine Liste aus folgenden Einzel-Berechtigungen:

| Berechtigung              | Bedeutung                                       |
|---------------------------|-------------------------------------------------|
| `users.manage`            | Benutzer anlegen / ändern / löschen            |
| `company.manage`          | Firmenname und globale Einstellungen ändern    |
| `workspace.manage`        | Workspace-Pfad ändern, Profil verwalten        |
| `masterdata.view`         | Stammdaten ansehen                               |
| `masterdata.edit`         | Stammdaten bearbeiten                            |
| `jobs.view`               | Aufträge ansehen                                |
| `jobs.edit`               | Aufträge bearbeiten                             |
| `designer.view`           | Designer ansehen                                 |
| `designer.edit`           | Designer bearbeiten                              |
| `print_templates.view`    | Druckvorlagen ansehen                            |
| `print_templates.edit`    | Druckvorlagen bearbeiten                         |
| `calculations.use`        | Berechnungen durchführen                        |
| `exports.print`           | Drucken / Export                                 |

## Eigene Rollen anlegen

Im Dialog *Rollen-Verwaltung* (Admin-Bereich) können Sie:

* eingebaute Rollen ansehen (nicht ändern)
* neue Rollen anlegen
* eigene Rollen bearbeiten oder löschen

> :material-alert-circle-outline: **TODO** *Screenshots des Dialogs einfügen.*

!!! tip "Sparsam mit Rollen"
    Beginnen Sie mit den eingebauten Rollen. Eigene Rollen lohnen sich
    erst bei Sonderfällen, z. B. einer "Springer"-Rolle, die nur
    zeitweilig Berechnungen ohne Druck darf.
