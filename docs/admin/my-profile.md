# Mein Profil

!!! abstract "Referenz — Der Dialog „Mein Profil": Profilbild, Anzeigename, E-Mail und Passwort selbst ändern, Konto-Infos einsehen, abmelden."

## Wofür Sie diesen Bereich nutzen

Jeder angemeldete Benutzer kann sein eigenes Konto ohne Administrator
pflegen: Profilbild, Anzeigename, E-Mail-Adresse und Passwort. Bei
Benutzern aus dem Kundenkonto ändern Sie Name, E-Mail und Passwort im
Lizenzportal; hier bleibt das Profilbild. Außerdem melden Sie sich hier ab. Für Änderungen an **fremden** Konten ist dagegen die
[Benutzerverwaltung](users.md) zuständig (Recht **Benutzer verwalten**
erforderlich).

## Den Dialog öffnen

Klicken Sie unten links in der Navigationsleiste auf Ihre **Benutzerkarte**
(Profilbild + Name). Bei eingeklappter Navigation übernimmt das die kompakte
Schaltfläche mit Ihren Initialen an derselben Stelle. Es öffnet sich der
Dialog **Mein Profil** mit drei Reitern.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Dialog „Mein Profil“, Reiter „Profil“ eines Kontobenutzers: rundes Profilbild bzw. Initialen, ausgegraute Felder Anzeigename und E-Mail, darunter der Hinweis „Name und E-Mail-Adresse gehören zum Kundenbenutzer …“ und die Schaltfläche **Im Lizenzportal ändern**.
    **So erzeugen:** Kunden-Build mit Kontoanmeldung (Musterbenutzer), unten links in der Navigation auf die eigene Benutzerkarte klicken.
    **Ziel-Datei:** `assets/screenshots/admin/mein-profil.png`

## Tab „Profil“

| Element | Beschreibung |
|---|---|
| **Profilbild** | Rundes Bild oben links. Ohne eigenes Bild zeigt es Ihre Initialen — die Anfangsbuchstaben der ersten beiden Namensteile, wie in der Navigation (aus „Max Muster“ wird „MM“). |
| **Bild...** | Wählt ein Profilbild (Foto/Avatar) aus einer Bilddatei. |
| **Entfernen** | Löscht das aktuelle Profilbild. |
| **Anzeigename** | Name, der in der Oberfläche und auf Ausdrucken erscheint. Bei Kontobenutzern schreibgeschützt (siehe unten). |
| **E-Mail** | Kontaktadresse. Bei Kontobenutzern schreibgeschützt (siehe unten). |
| **Im Lizenzportal ändern** | Nur bei Kontobenutzern: öffnet im Browser die Seite des Lizenzportals mit Passwort, zweitem Faktor und Name. |
| **Speichern** | Sichert die Änderungen; die Statuszeile meldet *„Profil gespeichert.“* |

### Kontobenutzer: Name und E-Mail kommen aus dem Kundenkonto

Melden Sie sich mit Ihrem Benutzer aus dem [Kundenkonto](../setup/account.md)
an, übernimmt Herzog CAB **Anzeigename und E-Mail-Adresse** bei jeder
Anmeldung aus dem Konto. Deshalb sind beide Felder hier **schreibgeschützt**;
darunter steht der Hinweis *„Name und E-Mail-Adresse gehören zum
Kundenbenutzer. Den Namen ändern Sie im Lizenzportal, das Programm übernimmt
ihn bei der nächsten Anmeldung.“*

So ändern Sie Ihren Namen:

1. Klicken Sie auf **Im Lizenzportal ändern**. Der Browser öffnet die
   Lizenzportal-Seite [Passwort, zweiter Faktor und Name](../portal/security.md#name)
   mit der Karte für den Namen.
2. Tragen Sie dort den neuen Namen ein und speichern Sie.
3. Herzog CAB übernimmt ihn bei der nächsten Anmeldung (bzw. beim nächsten
   Abgleich mit dem Kundenkonto).

Den Namen anderer Benutzer ändert ein Administrator im Lizenzportal unter
[Benutzer einladen und verwalten](../portal/users.md). Die E-Mail-Adresse
ist der Anmeldename im Konto. Das **Profilbild** bleibt auch für
Kontobenutzer hier im Programm änderbar.

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
    [Passwort und zweiter Faktor](../portal/security.md).

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
