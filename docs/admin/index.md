# Systemverwaltung

In der **Systemverwaltung** (unterster Bereich der linken Navigation) verwalten
Sie alles, was nicht zum Tagesgeschäft gehört: Benutzerkonten, Rollen und
Rechte, die Anmeldung über Microsoft oder das Firmennetz, Profile
(Arbeitsbereiche), den Speicherort der Daten und die Firmenstammdaten.
Dazu kommt der Einstellungen-Dialog unter *Datei > Einstellungen* mit
Sprache, Darstellung und Webserver.

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

    Das Anmeldefenster: lokales Konto, **Mit Microsoft anmelden**,
    Kontosperre und Profil-Auswahl nach dem Login.

    [:octicons-arrow-right-24: Weiter](login.md)

- :material-account-multiple: **Benutzer**

    Benutzerkonten anlegen, bearbeiten, deaktivieren — inklusive Import aus
    Microsoft Entra oder LDAP und Passwort-Zurücksetzen.

    [:octicons-arrow-right-24: Weiter](users.md)

- :material-shield-account: **Rollen und Berechtigungen**

    Das Rechtesystem: mitgelieferte Standardrollen, Einzelrechte und eigene
    Rollen.

    [:octicons-arrow-right-24: Weiter](roles.md)

- :material-key-chain: **Authentifizierung**

    Anmeldung über Microsoft Entra ID oder LDAP / Active Directory
    einrichten — mit Gruppen-zu-Rollen-Zuordnung.

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
    Datenschutz, Speicherorte, Altdaten-Import und Webserver.

    [:octicons-arrow-right-24: Weiter](settings/index.md)

</div>

## Typische Aufgaben

Für den kompletten Ablauf „Benutzer und Rechte für ein Werk einrichten" gibt
es eine Schritt-für-Schritt-Anleitung:
[Benutzer und Rollen einrichten](../tasks/setup-users.md).
