# Dateispeicherorte

## Workspace (vom Benutzer waehlbar)

```
<Workspace>\
├── customers.json           Kunden
├── machines.json            Maschinen
├── colors.json              Farben
├── jobs.json                Auftraege
├── products.json            Produkte
├── materials.json           (legacy) Materialliste
├── bobbins.json             (legacy) Spulenliste
├── Materials\               Material-Bibliothek (Detaildaten)
├── Machines\<MaschinenID>\documents\
├── Printouts\
│   ├── templates\           Druckvorlagen (eine .json je Vorlage)
│   └── assets\              Bilder/Logos fuer Vorlagen
└── auth\
    └── assignments.json     Zuordnungen Benutzer <-> Rolle
```

## Maschinenweit (ProgramData)

```
%ProgramData%\Herzog GmbH\Herzog Cab\
├── users.json               alle Benutzerkonten
├── profiles.json            alle Profile (Workspace-Verbindungen)
├── storage.json             Speicher-Metadaten
└── auth\
    └── avatars\             Profilbilder
```

## Benutzer-Registry

Fenstergroessen, Spaltenbreiten und letzter Zustand der Oberflaeche werden in der Windows-Registry abgelegt unter

```
HKEY_CURRENT_USER\Software\Herzog GmbH\Herzog Cab
```

