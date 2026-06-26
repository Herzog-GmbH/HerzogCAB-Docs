# Dateispeicherorte

Die genauen Pfade zeigt Herzog CAB auch unter
[Einstellungen → Speicherorte](../settings/file-locations.md).

## Arbeitsverzeichnis (pro Profil wählbar)

```
<Arbeitsverzeichnis>\
├── materials.json                Materialien
├── bobbins.json                  Spulen
├── colors.json                   Farben
├── customers.json                Kunden
├── orders.json                   Aufträge
├── my_machines.json              Maschinen
├── designer_palette_state.json   Farbpalette des Designers
├── index.json                    Design-Index
├── folders.json                  Ordnerliste der Designs
├── previews\                     Vorschaubilder der Designs
├── machines\                     Maschinen-Dokumente
└── Printouts\
    ├── templates\                Druckvorlagen (eine .json je Vorlage)
    └── assets\                   Bilder/Logos für Vorlagen
```

Die Log-Datei liegt – sofern das Protokoll aktiviert ist – unter
`logs\herzogcab.log` im Arbeitsverzeichnis.

## Maschinenweit (ProgramData)

Benutzer- und Profildaten gelten rechnerweit, unabhängig vom Arbeitsverzeichnis:

```
%ProgramData%\Herzog GmbH\Herzog Cab\
├── (Benutzerkonten und Profile)
└── auth\
    └── avatars\                  Profilbilder
```

## Benutzer-Registry

Fenstergrößen, Spaltenbreiten und der letzte Zustand der Oberfläche werden in der
Windows-Registry abgelegt unter:

```
HKEY_CURRENT_USER\Software\Herzog GmbH\Herzog Cab
```

!!! info "Arbeitsverzeichnis festlegen"
    Wo das Arbeitsverzeichnis liegt, bestimmen Sie pro Profil in der
    [Profilverwaltung](../workspace/change-path.md).
