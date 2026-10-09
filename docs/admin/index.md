# Verwaltung

!!! abstract "Referenz — Übersicht: Kundenkonto und Lizenzportal, Systemverwaltung der Desktop-App, Einstellungen-Dialog"

Die Verwaltung von Herzog CAB verteilt sich seit Version 2.0 auf zwei Orte:

* Das **Kundenkonto** im [Lizenzportal](../portal/index.md) — Bausteine,
  Plätze, Rechner, Benutzer und Passwörter. Es gilt für die Desktop-App
  **und** die Web-App und wird im Browser gepflegt.
* Die **Systemverwaltung** der Desktop-App (unterster Bereich der linken
  Navigation) — Rollen-Zuweisung je Arbeitsbereich, Profile, Speicherort
  und Firmenstammdaten; bei Dongle-Installationen zusätzlich die lokalen
  Benutzerkonten und die Anmeldung über Microsoft oder das Firmennetz. Dazu
  kommt der Einstellungen-Dialog unter *Datei > Einstellungen* mit Sprache,
  Darstellung, Designer-Vorgaben, Lizenz, Cloud und Webserver.

Die Verwaltung der **Web-App** (Firma, Medien, Rollen, Import) steckt in
deren Benutzermenü — siehe [Web-App](../web/index.md).

<div class="grid cards" markdown>

- :material-account-key-outline: **Kundenkonto und Lizenzportal**

    Bausteine und Plätze, angemeldete Rechner, Benutzer einladen, Lizenzen
    anfordern, Passwort, zweiter Faktor und Name.

    [:octicons-arrow-right-24: Lizenzportal](../portal/index.md)

- :material-cog-outline: **Lizenz und Cloud (Einstellungen)**

    Lizenzstatus in der Desktop-App, Offline-Miete, Abmelden und der
    Cloud-Upload des Arbeitsverzeichnisses in die Web-App.

    [:octicons-arrow-right-24: Lizenz und Cloud](settings/license.md)

</div>

## Systemverwaltung der Desktop-App

!!! info "Sichtbarkeit hängt von Ihren Rechten ab"
    Die Gruppe **Systemverwaltung** erscheint in der Navigation nur, wenn Ihr
    Benutzerkonto mindestens eines der Verwaltungsrechte besitzt. Auch
    innerhalb der Gruppe sehen Sie nur die Einträge, für die Sie berechtigt
    sind — ein Benutzer mit dem Recht *Firmendaten verwalten* sieht z. B. nur
    **Firma**, nicht aber **Benutzer** oder **Rollen**. Welche Rechte es gibt,
    erklärt [Rollen und Berechtigungen](roles.md).

| Eintrag in der Navigation | Benötigtes Recht |
|---|---|
| **Benutzer** | Benutzer verwalten |
| **Rollen** | Rollen verwalten |
| **Profile** | Workspace-Einstellungen |
| **Speicherort** | Workspace-Einstellungen |
| **Firma** | Firmendaten verwalten |
| **Authentifizierung** | Benutzer verwalten |

## Die Bereiche im Überblick

<div class="grid cards" markdown>

- :material-login: **Anmeldung und Abmelden**

    Das Anmeldefenster: Kontobenutzer, lokales Konto, **Mit Microsoft
    anmelden**, Kontosperre und Profil-Auswahl nach dem Login.

    [:octicons-arrow-right-24: Weiter](login.md)

- :material-account-multiple: **Benutzer**

    Benutzer aus dem Kundenkonto übernehmen und Arbeitsbereichen zuweisen;
    bei Dongle-Installationen lokale Konten anlegen, aus Microsoft Entra
    oder LDAP importieren und Passwörter zurücksetzen.

    [:octicons-arrow-right-24: Weiter](users.md)

- :material-shield-account: **Rollen und Berechtigungen**

    Das Rechtesystem: mitgelieferte Standardrollen, Einzelrechte und eigene
    Rollen.

    [:octicons-arrow-right-24: Weiter](roles.md)

- :material-key-chain: **Authentifizierung**

    Nur bei Dongle-Installationen: Anmeldung über Microsoft Entra ID oder
    LDAP / Active Directory einrichten — mit Gruppen-zu-Rollen-Zuordnung.

    [:octicons-arrow-right-24: Weiter](authentication.md)

- :material-account-circle: **Mein Profil**

    Ihr eigenes Konto: Profilbild, Anzeigename, E-Mail, Passwort ändern und
    abmelden.

    [:octicons-arrow-right-24: Weiter](my-profile.md)

- :material-briefcase-outline: **Profile (Arbeitsbereiche)**

    Mehrere Mandanten oder Test-/Produktivumgebungen betreiben, das
    Arbeitsverzeichnis festlegen, Profile wechseln.

    [:octicons-arrow-right-24: Weiter](profiles.md)

- :material-database-marker: **Speicherort**

    Wo liegen die zentralen Benutzerdaten und der aktive Arbeitsbereich?
    Lokal oder auf dem Netzlaufwerk — hier sehen und ändern Sie es.

    [:octicons-arrow-right-24: Weiter](storage-location.md)

- :material-domain: **Firma**

    Firmenstammdaten und Logo für Briefkopf und Druckvorlagen pflegen.

    [:octicons-arrow-right-24: Weiter](company.md)

- :material-cog-outline: **Einstellungen (Dialog)**

    Der Dialog unter *Datei > Einstellungen*: Sprache, Schriftgröße, Design,
    Datenschutz, Speicherorte, Designer-Vorgaben, Altdaten-Import, Lizenz
    und Cloud, Webserver.

    [:octicons-arrow-right-24: Weiter](settings/index.md)

</div>

## Typische Aufgaben

* [Benutzer und Rollen einrichten](../tasks/setup-users.md) — der komplette
  Ablauf „Benutzer und Rechte für ein Werk einrichten", für Kontomodell und
  Dongle-Installation.
* [Daten vom Desktop in die Web-App bringen](../tasks/desktop-to-web.md) —
  Cloud-Upload oder ZIP-Import.
