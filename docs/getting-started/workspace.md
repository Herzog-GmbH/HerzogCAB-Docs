# Workspace einrichten

Ein **Workspace** ist der zentrale Daten-Ordner von Herzog CAB. Hier liegen
Ihre Stammdaten, Auftraege, Druckvorlagen und benutzerdefinierten Profile.

## Was gehoert in einen Workspace?

Im Workspace-Ordner finden Sie:

```
<Workspace>\
├── customers.json           Kunden
├── machines.json            Maschinen
├── colors.json              Farben
├── jobs.json                Auftraege
├── products.json            Produkte
├── Materials\               Material-Bibliothek
├── Printouts\
│   ├── templates\           Druckvorlagen (eine Datei je Vorlage)
│   └── assets\              Bilder/Logos fuer Druckvorlagen
└── auth\
    └── assignments.json     Wer-darf-was-Zuordnungen
```

!!! info "Was ist NICHT im Workspace?"
    Benutzerkonten und Passwoerter liegen **nicht** im Workspace, sondern
    maschinenweit unter `C:\ProgramData\Herzog GmbH\Herzog Cab`.
    So koennen sich Benutzer am gleichen Rechner mit ihren persoenlichen
    Konten an verschiedenen Workspaces anmelden, ohne sich neu anlegen
    zu muessen.

## Wo soll der Workspace liegen?

| Szenario                                      | Empfehlung                                |
|-----------------------------------------------|-------------------------------------------|
| Sie arbeiten allein an einem Rechner          | Lokal, z. B. `C:\HerzogCAB\Workspace`     |
| Mehrere Bediener am gleichen Rechner          | Lokal - Benutzer trennen sich ueber Login |
| Mehrere Rechner sollen die gleichen Daten sehen | Netzlaufwerk (SMB-Share)                |

!!! warning "Netzlaufwerk-Hinweise"
    Wenn der Workspace auf einem Netzlaufwerk liegt:

    - Stellen Sie sicher, dass alle Bediener Schreibrechte haben.
    - Greifen Sie nicht von zwei Rechnern gleichzeitig auf den gleichen
      Auftrag zu - Aenderungen koennten verloren gehen.
    - Eine stabile Verbindung ist wichtig - bei Verbindungsabbruch
      koennen Daten beschaedigt werden.

## Workspace beim ersten Start anlegen

Nach der Installation oeffnet sich beim ersten Programmstart der
**Workspace-Setup-Dialog**.

> :material-image-area: *Screenshot: Workspace-Setup-Dialog*

1. Klicken Sie auf **Durchsuchen** und waehlen Sie einen Ordner.
2. Optional: Geben Sie einen **Profilnamen** an (z. B. "Werk Halle 2"),
   wenn Sie spaeter mehrere Workspaces nutzen wollen.
3. Bestaetigen Sie mit **Weiter**.

Die Datei-Struktur wird dann automatisch angelegt.

## Workspace spaeter aendern

Sie koennen den Workspace jederzeit wechseln:

* *Werkzeuge > Profil verwalten* (alternativ: Klick auf den Profilnamen
  oben in der Anwendung)
* Bestehendes Profil waehlen oder ein neues anlegen.
* Programm startet neu, das gewaehlte Profil ist dann aktiv.

Mehr dazu unter [Profil wechseln](../workspace/switch-profile.md).
