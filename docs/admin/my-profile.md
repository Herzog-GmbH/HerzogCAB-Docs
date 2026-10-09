# Mein Profil

!!! abstract "Referenz — Der Dialog „Mein Profil": Profilbild, Anzeigename, E-Mail und Passwort selbst ändern, Konto-Infos einsehen, abmelden."

## Wofür Sie diesen Bereich nutzen

Jeder angemeldete Benutzer kann sein eigenes Konto ohne Administrator
pflegen: Profilbild, Anzeigename, E-Mail-Adresse und Passwort. Außerdem
melden Sie sich hier ab. Für Änderungen an **fremden** Konten ist dagegen die
[Benutzerverwaltung](users.md) zuständig (Recht **Benutzer verwalten**
erforderlich).

## Den Dialog öffnen

Klicken Sie unten links in der Navigationsleiste auf Ihre **Benutzerkarte**
(Profilbild + Name). Bei eingeklappter Navigation übernimmt das die kompakte
Schaltfläche mit Ihren Initialen an derselben Stelle. Es öffnet sich der
Dialog **Mein Profil** mit drei Reitern.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Dialog „Mein Profil", Reiter „Profil" mit Profilbild, Anzeigename und E-Mail
    **So erzeugen:** unten links in der Navigation auf die eigene Benutzerkarte klicken
    **Ziel-Datei:** `assets/screenshots/admin/mein-profil.png`

## Tab „Profil"

| Element | Beschreibung |
|---|---|
| **Bild...** | Wählt ein Profilbild (Foto/Avatar) aus einer Bilddatei. |
| **Entfernen** | Löscht das aktuelle Profilbild. |
| **Anzeigename** | Name, der in der Oberfläche und auf Ausdrucken erscheint. |
| **E-Mail** | Optionale Kontaktadresse. |
| **Speichern** | Sichert die Änderungen; die Statuszeile meldet *„Profil gespeichert."* |

!!! info "Kontobenutzer: Name und E-Mail kommen aus dem Kundenkonto"
    Melden Sie sich mit Ihrem Benutzer aus dem
    [Kundenkonto](../setup/account.md) an, übernimmt Herzog CAB Anzeigename
    und E-Mail-Adresse bei jeder Anmeldung aus dem Kundenkonto. Ändern Sie
    Ihren Namen deshalb im Lizenzportal, siehe
    [Passwort, zweiter Faktor und Name](../portal/security.md#name).

!!! tip "Wiedererkennung an gemeinsamen Rechnern"
    Gerade an Arbeitsplätzen, die mehrere Bediener teilen, hilft ein
    Profilbild, auf einen Blick zu sehen, wer gerade angemeldet ist.

!!! info "Profilbild gilt überall"
    Das Profilbild wird zusammen mit den zentralen Benutzerdaten gespeichert
    (siehe [Speicherort](storage-location.md)), nicht im Arbeitsbereich —
    Sie haben also in jedem [Profil](profiles.md) dasselbe Bild.

## Tab „Passwort"

| Element | Beschreibung |
|---|---|
| **Aktuelles Passwort** | Zur Bestätigung, dass Sie es selbst sind. |
| **Neues Passwort** / **Neues Passwort bestätigen** | Beide Eingaben müssen übereinstimmen, sonst erscheint *„Die neuen Passwörter stimmen nicht überein."* |
| **Ändern** | Führt die Änderung aus; bei Erfolg: *„Passwort erfolgreich geändert."* |

!!! info "Kontobenutzer: Passwort gehört zum Kundenkonto"
    Melden Sie sich mit Ihrem Benutzer aus dem [Kundenkonto](../setup/account.md)
    an, sind die Felder dieses Tabs gesperrt und ein Hinweis erklärt: *„Ihr
    Passwort gehört zum Kundenbenutzer und gilt auch für das Lizenzportal
    und Herzog CAB Web. Ändern Sie es im Lizenzportal (Einstellungen →
    Lizenz → Lizenzportal öffnen)."* — siehe
    [Passwort, zweiter Faktor und Name](../portal/security.md).

!!! info "Microsoft- und Domänenkonten"
    Melden Sie sich [mit Microsoft](login.md#mit-microsoft-anmelden) oder
    über das Firmenverzeichnis an, verwaltet Ihr Unternehmen das Passwort
    dort — nicht in Herzog CAB.

## Tab „Info"

Reine Anzeige, nicht änderbar:

| Angabe | Beschreibung |
|---|---|
| **Login** | Ihr Anmeldename. |
| **Rolle(n)** | Ihre [Rollen](roles.md) im aktuellen Profil; globale Administratoren sehen zusätzlich *Administrator (System)*. |
| **Firma** | Die hinterlegten [Firmendaten](company.md). |
| **Arbeitsbereich** | Das Arbeitsverzeichnis des aktiven [Profils](profiles.md). |

## Abmelden und Schließen

* **Abmelden** meldet Sie nach einer Sicherheitsabfrage (*„Wirklich
  abmelden?"*) vom Programm ab — es erscheint wieder das
  [Anmeldefenster](login.md).
* **Schließen** schließt den Dialog, Sie bleiben angemeldet.

## Verwandte Seiten

* [Anmeldung und Abmelden](login.md)
* [Benutzer](users.md) — Konten anderer Benutzer verwalten
* [Speicherort](storage-location.md) — wo Benutzerdaten und Profilbilder liegen
