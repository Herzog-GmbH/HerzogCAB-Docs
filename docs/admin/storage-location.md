# Speicherort

!!! abstract "Referenz — Wo Herzog CAB seine Daten speichert: zentrale Benutzerdaten (lokal oder Netzwerk) und der Arbeitsbereich des aktiven Profils."

## Wofür Sie diesen Bereich nutzen

Der Bildschirm **SPEICHERORT** (*Systemverwaltung > Speicherort*) zeigt auf
einen Blick, wo Herzog CAB gerade seine Daten speichert — praktisch beim
Wechsel zwischen einer lokalen Test-Konfiguration und der Umgebung auf dem
Dateiserver. Hier stellen Sie außerdem um, ob die **zentralen Benutzerdaten**
lokal auf diesem Rechner oder auf einem **Netzwerk-Pfad** liegen, den sich
mehrere Arbeitsplätze teilen.

Herzog CAB unterscheidet zwei Speicherorte:

* **Zentrale Benutzerdaten** — Benutzerkonten, Profile, Rollen-Zuweisungen
  und Profilbilder. Sie gelten rechnerweit bzw. (bei Netzwerk-Speicherort)
  standortweit und liegen **nicht** im Arbeitsbereich.
* **Arbeitsbereich (Workspace)** — die Fachdaten des aktiven
  [Profils](profiles.md): Stammdaten, Aufträge, Designs, Druckvorlagen.

!!! warning "Berechtigung erforderlich"
    Diesen Bereich sehen nur Benutzer mit dem Recht
    **Workspace-Einstellungen**; auch das Ändern des Speicherorts erfordert
    dieses Recht.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Bildschirm „Speicherort" mit Badge NETZWERK/LOKAL, Pfad der zentralen Benutzerdaten und Abschnitt „Arbeitsbereich (aktives Profil)"
    **So erzeugen:** *Systemverwaltung > Speicherort* öffnen
    **Ziel-Datei:** `assets/screenshots/admin/speicherort.png`

## Bedienelemente im Detail

### Zentrale Benutzerdaten (Benutzer, Profile, Zuweisungen)

| Element | Beschreibung |
|---|---|
| Badge **LOKAL** / **NETZWERK** | Zeigt den aktuellen Modus: **LOKAL** = die Benutzerdaten liegen nur auf diesem Rechner; **NETZWERK** = sie liegen auf einem geteilten Netzwerk-Pfad. |
| Pfad-Anzeige | Der vollständige Ordnerpfad (mit der Maus markier- und kopierbar). |
| **Pfad kopieren** | Kopiert den Pfad in die Zwischenablage. |
| **Ändern …** | Öffnet den Dialog *Daten-Speicherort einrichten* (siehe unten). Nur mit dem Recht **Workspace-Einstellungen** nutzbar. |

### Arbeitsbereich (aktives Profil)

| Element | Beschreibung |
|---|---|
| *Profil: …* | Name des aktuell aktiven Profils. |
| Pfad-Anzeige | Das Arbeitsverzeichnis dieses Profils (markier- und kopierbar). |
| **Pfad kopieren** | Kopiert den Pfad in die Zwischenablage. |
| **Profile verwalten →** | Springt direkt in die [Profilverwaltung](profiles.md), wo das Arbeitsverzeichnis geändert wird. |

## Dialog „Daten-Speicherort einrichten"

Über **Ändern …** legen Sie fest, wo die zentralen Benutzerdaten liegen:

| Element | Beschreibung |
|---|---|
| **Lokal — nur dieser Rechner** | Benutzerdaten liegen im Standardordner auf diesem Rechner. |
| **Netzwerk-Pfad — geteilt mit anderen Rechnern** | Benutzerdaten liegen auf einer Freigabe, z. B. `\\fileserver\share\HerzogCAB` — alle Arbeitsplätze mit demselben Pfad nutzen dieselben Konten, Profile und Zuweisungen. |
| Pfad-Feld / **Auswählen …** | Netzwerk-Pfad eintragen oder per Ordnerauswahl wählen. |
| **Verbindung testen** | Prüft, ob der Pfad existiert und beschreibbar ist. Das Ergebnis meldet auch, ob dort **bereits Benutzerdaten** liegen (dann übernimmt dieser Rechner die vorhandenen) oder ob der Pfad leer ist. |
| **Übernehmen** / **Abbrechen** | Speichert bzw. verwirft die Auswahl. |

Beim Umstellen auf einen leeren Netzwerk-Pfad bietet Herzog CAB an, die auf
diesem Rechner vorhandenen Benutzerdaten dorthin zu **kopieren**, damit
nichts verloren geht. Nach einer Umstellung fragt Herzog CAB nach einem
**Neustart** — erst danach greift der neue Speicherort überall.

!!! info "Wo die Auswahl gespeichert wird"
    Die Einstellung selbst wird in einer kleinen Konfigurationsdatei **lokal
    auf jedem Rechner** gespeichert. Auf jedem Arbeitsplatz, der die
    gemeinsamen Benutzerdaten nutzen soll, stellen Sie den Netzwerk-Pfad
    daher einmal ein. Ohne Umstellung liegen die zentralen Benutzerdaten im
    Windows-Ordner `%ProgramData%\Herzog GmbH\Herzog Cab`.

## Was liegt im Arbeitsbereich?

Alle Fachdaten eines Profils liegen als Dateien und Ordner direkt im
**Arbeitsverzeichnis**:

| Inhalt | Datei / Ordner |
|---|---|
| Design-Index / Design-Ordnerliste | `index.json`, `folders.json` |
| Vorschaubilder der Designs | `previews\` |
| Materialien | `materials.json` |
| Spulen | `bobbins.json` |
| Farben | `colors.json` |
| Kunden | `customers.json` |
| Aufträge (Flecht- und Spulaufträge) | `orders.json` |
| Eigene Maschinen | `my_machines.json` |
| Farbpalette des Designers | `designer_palette_state.json` |
| Hallenplaner: Grundrisse und Belegungen | `floor_plans.json`, `placements.json` |
| Maschinen-Dokumente | `machines\` |
| Medienbibliothek | `media\` |
| Druckvorlagen | `Printouts\` (darin `templates\` und `assets\`) |
| Protokoll (falls aktiviert) | `logs\herzogcab.log` |

Dieselben Pfade zeigt auch der Einstellungen-Dialog im Tab
[Speicherorte](settings/files.md) — dort nur zur Information.

!!! tip "Datensicherung"
    Für ein vollständiges Backup genügt es, das **Arbeitsverzeichnis** jedes
    Profils und den Ordner der **zentralen Benutzerdaten** zu sichern.

## Verwandte Seiten

* [Profile (Arbeitsbereiche)](profiles.md) — Arbeitsverzeichnis festlegen und wechseln
* [Einstellungen: Speicherorte](settings/files.md) — Pfadübersicht im Einstellungen-Dialog
* [Dateiablage im Überblick](../appendix/file-locations.md)
