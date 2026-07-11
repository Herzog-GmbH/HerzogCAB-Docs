# Dateispeicherorte

!!! abstract "Referenz — Kurzübersicht, wo Herzog CAB welche Daten ablegt"

Diese Seite ist die schnelle Übersicht. Die vollständige, für Ihre
Installation aktuelle Liste mit allen Datei- und Ordnerpfaden zeigt Herzog
CAB selbst unter [Speicherort](../admin/storage-location.md) an
(*Systemverwaltung → Speicherort*) – das ist die maßgebliche Quelle, diese
Seite dupliziert sie nicht.

## Auf einen Blick

| Ebene | Inhalt | Ort |
|---|---|---|
| **Arbeitsverzeichnis** (pro Profil wählbar) | Stammdaten, Aufträge, Designs, Druckvorlagen, Protokoll | frei wählbar – siehe [Profile](../admin/profiles.md) |
| **Maschinenweit** (`%ProgramData%`) | Benutzerkonten, Profile, Profilbilder | rechnerweit, unabhängig vom Arbeitsverzeichnis |
| **Windows-Registry** | Fenstergrößen, Spaltenbreiten, letzter Oberflächen-Zustand | `HKEY_CURRENT_USER\Software\Herzog GmbH\Herzog Cab` |

!!! info "Arbeitsverzeichnis ändern"
    Der Ort des Arbeitsverzeichnisses wird nicht hier, sondern in den
    [Profilen](../admin/profiles.md) festgelegt.

## Verwandte Seiten

* [Speicherort (Systemverwaltung)](../admin/storage-location.md)
* [Profile (Arbeitsbereiche)](../admin/profiles.md)
* [Update-Fehler](../help/update-errors.md) – warum Ihre Daten bei einem Update erhalten bleiben
