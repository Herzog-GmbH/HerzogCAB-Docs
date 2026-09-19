# Rollen (Web-App)

!!! abstract "Referenz — Die Seite „Rollen" im Benutzermenü der Web-App: Standardrollen ansehen, eigene Rollen mit einzelnen Rechten anlegen"

## Wofür Sie diesen Bereich nutzen

Eine **Rolle** bündelt Rechte. Die Web-App liefert die Standardrollen
**Administrator**, **Bearbeiter** und **Betrachter** mit; Administratoren
können eigene Rollen ergänzen — etwa *Vertrieb* (nur Aufträge und Designs
anzeigen) oder *Spulerei* (Aufträge bearbeiten, keine Stammdaten). Welche
Benutzer welche Rolle haben, legen Sie unter
[Konto und Benutzer](account.md) fest.

Sie öffnen die Seite über *Benutzermenü > Rollen*; sie erscheint nur mit
dem Recht **Rollen verwalten** oder **Benutzer verwalten**.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Rollen in der Web-App: Liste der Standard- und eigenen Rollen mit Rechtezahl und Benutzerzahl.
    **So erzeugen:** Web-App lokal (127.0.0.1:5173), Seite `/rollen`; automatisch per `python _tools/web_screenshots.py shots nur:rollen`
    **Ziel-Datei:** `assets/screenshots/web/rollen.png`
    <!-- web-bild ../assets/screenshots/web/rollen.png -->

| Element | Bedeutung |
|---|---|
| **Neue Rolle** | Öffnet den Dialog *Neue Rolle anlegen*. |
| **Name oder Id** / **Suchen** | Filtert die Liste. |
| Rollenkarte | Name, Kennzeichen **Standard** oder **eigene**, Beschreibung, *alle Rechte* bzw. *n Rechte* und *n Benutzer*. |
| **Ansehen** | Standardrollen sind nur lesbar. |
| **Bearbeiten** / **Löschen** | Eigene Rollen ändern oder entfernen; eine Rolle, die noch Benutzern zugewiesen ist, lässt sich nicht löschen. |

## Rolle anlegen oder bearbeiten

| Feld | Bedeutung |
|---|---|
| **Id** | Kennung: beginnt mit einem Kleinbuchstaben, nur a–z, 0–9 und _, höchstens 32 Zeichen (z. B. `supervisor`). Nach dem Anlegen nicht mehr änderbar. |
| **Name** | Anzeigename. Standardrollen werden automatisch übersetzt. |
| **Beschreibung** | Freitext. |
| **Alle Rechte (Administrator)** | Die Rolle hat sämtliche Rechte; die einzelnen Kästchen werden dann ignoriert. |
| **Einzelne Rechte** | Kästchen je Recht, nach Gruppen geordnet (siehe unten). Mindestens ein Recht ist Pflicht. |
| **Anlegen** / **Speichern** / **Abbrechen** | |

### Die Rechte

| Gruppe | Recht | Wirkung in der Web-App |
|---|---|---|
| Administration | **Benutzer verwalten** | Rollen zuweisen unter Konto und Benutzer; Seite Rollen sichtbar. |
| | **Rollen verwalten** | Rollen anlegen, ändern, löschen. |
| | **Firmendaten verwalten** | [Firma](company.md) bearbeiten. |
| | **Workspace-Einstellungen** | [Import und Export](import.md) des Arbeitsbereichs. |
| Stammdaten | **Stammdaten anzeigen** / **bearbeiten** | [Stammdaten](master-data.md) und [Maschinen](machines.md) sehen bzw. ändern. |
| Hallenplaner | **Hallenplaner anzeigen** / **bearbeiten** | [Hallenplaner](hall-planner.md). |
| Aufträge | **Aufträge anzeigen** / **bearbeiten** | [Aufträge](orders.md). |
| Designer | **Designer anzeigen** / **bearbeiten** | [Designs und Designer](designer.md). |
| Druckvorlagen | **Druckvorlagen anzeigen** / **bearbeiten** | Vorlagen in der Druckseite nutzen. |
| Berechnungen / Export | **Berechnungen ausführen** | [Berechnungen](calculations.md). |
| | **Drucken / Export** | [Drucken](print.md) und Export. |
| Spezialwerkzeuge | **Parameter Explorer öffnen** | Vorbereitet für spätere Funktionen. |

Die Rechte entsprechen denen der Desktop-App
([Rollen und Berechtigungen](../admin/roles.md)); eigene Rollen werden
aber je Programm getrennt gepflegt.

## Verwandte Seiten

* [Konto und Benutzer (Web-App)](account.md) — Rollen zuweisen
* [Benutzer einladen und verwalten (Lizenzportal)](../portal/users.md)
* [Rollen und Berechtigungen (Desktop-App)](../admin/roles.md)
