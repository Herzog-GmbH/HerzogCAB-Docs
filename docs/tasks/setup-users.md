# Benutzer und Rollen einrichten

!!! example "Anleitung — am Ende können sich Ihre Mitarbeiter mit eigenen Konten anmelden und sehen genau die Bereiche, die ihre Rollen erlauben"

**Voraussetzungen:**

* Sie sind mit einem Administrator-Konto angemeldet (die Kategorie
  **Systemverwaltung** ist nur mit entsprechenden Berechtigungen sichtbar).
* Im Kontomodell: Sie sind **Administrator des Kundenkontos** im
  [Lizenzportal](../portal/index.md).
* Für die Anbindung an Microsoft Entra ID oder LDAP/Active Directory
  (nur Dongle-Installationen): die Zugangsdaten Ihrer IT (z. B. Tenant und
  Client-ID bzw. LDAP-URL und Bind-Konto) liegen bereit.

=== "Kundenkonto (Regelfall seit 2.0)"

    ```mermaid
    flowchart LR
      A["Benutzer im Lizenzportal einladen"] --> B["Rolle im Konto festlegen"]
      B --> C["Desktop: Profile zuordnen<br>Web: Web-Rollen ankreuzen"]
      C --> D["Anmeldung testen"]
    ```

    1. **Einladen:** Im Lizenzportal unter **Benutzer** die E-Mail-Adresse
       eintragen, Rolle wählen (Administrator, Bearbeiter, Betrachter) und
       auf **Einladen** klicken — siehe
       [Benutzer einladen und verwalten](../portal/users.md). Die Person
       setzt über den Link ihr Passwort selbst.
    2. **Desktop-App:** Unter *Systemverwaltung > Benutzer* auf **Vom
       Kundenkonto aktualisieren** klicken (oder den nächsten Start des
       Benutzers abwarten) und im Bereich **Profile und Rollen** die
       Arbeitsbereiche zuordnen — siehe [Benutzer](../admin/users.md). Die
       Rolle selbst kommt aus dem Konto; eigene Rollen aus
       *Systemverwaltung > Rollen* können Sie zusätzlich je Profil zuweisen.
    3. **Web-App:** Unter *Benutzermenü > Konto und Benutzer* die
       Web-Rollen ankreuzen — siehe [Konto und Benutzer](../web/account.md);
       eigene Web-Rollen legen Sie unter [Rollen](../web/roles.md) an.
    4. **Testen:** Die Person meldet sich in der Desktop-App (E-Mail und
       Passwort) bzw. in der Web-App an und sieht die Bereiche ihrer Rolle.

    Die Schritte unten gelten für **Dongle-Installationen** mit lokaler
    Benutzerverwaltung.

=== "Dongle-Installation (lokale Benutzer)"

    ```mermaid
    flowchart LR
      A["Rollen prüfen/anlegen"] --> B["Benutzer anlegen oder importieren"]
      B --> C["Profile & Rollen zuordnen"]
      C --> D["Anmeldung testen"]
    ```

## Schritt 1: Rollen prüfen oder anlegen

1. Öffnen Sie *Systemverwaltung > Rollen* (Referenz:
   [Rollen und Berechtigungen](../admin/roles.md)).
2. Prüfen Sie, ob die vorhandenen Standard-Rollen für Ihre Arbeitsteilung
   ausreichen.
3. Falls nicht, klicken Sie auf **Neue Rolle**, vergeben Name und
   Beschreibung und wählen die einzelnen Rechte aus — oder aktivieren Sie
   **Alle Rechte (Administrator)** für eine Vollzugriffs-Rolle.

Eine Rolle ist ein wiederverwendbares Rechte-Set; jeder Benutzer kann eine
oder mehrere Rollen erhalten.

## Schritt 2: Benutzer anlegen oder importieren

Je nachdem, wie sich Ihre Mitarbeiter anmelden sollen:

=== "Lokale Benutzer"

    1. Öffnen Sie *Systemverwaltung > Benutzer* (Referenz:
       [Benutzer](../admin/users.md)).
    2. Klicken Sie auf **Neuer Benutzer** und vergeben Sie Login,
       Anzeigename, E-Mail und ein Anfangspasswort.
    3. Legen Sie das Konto an und ordnen Sie ihm anschließend im Bereich
       **Profile und Rollen** die Rollen aus Schritt 1 zu.

=== "Microsoft Entra ID"

    1. Konfigurieren Sie zuerst die Anmeldung unter
       *Systemverwaltung > Authentifizierung*, Tab **Microsoft Entra ID**:
       aktivieren, Tenant und Client-ID eintragen und in der Tabelle
       **Entra-Gruppe → Rolle** festlegen, welche Entra-Gruppe welche
       Herzog-CAB-Rolle erhält (Referenz:
       [Authentifizierung](../admin/authentication.md)).
    2. Speichern Sie die Konfiguration.
    3. Importieren Sie die Benutzer unter *Systemverwaltung > Benutzer* über
       **Aus Entra importieren** — oder überlassen Sie das der automatischen
       Kontoerstellung bei der ersten Anmeldung, falls Sie diese in der
       Konfiguration aktiviert haben.

=== "LDAP / Active Directory"

    1. Konfigurieren Sie die Anmeldung unter
       *Systemverwaltung > Authentifizierung*, Tab
       **LDAP / Active Directory**: aktivieren, LDAP-URL, Bind-Konto,
       Basis-DN und Suchfilter eintragen (Referenz:
       [Authentifizierung](../admin/authentication.md)).
    2. Speichern Sie die Konfiguration.
    3. Importieren Sie die Benutzer unter *Systemverwaltung > Benutzer* über
       **Aus LDAP importieren**.

Alle Felder der Benutzerverwaltung — einschließlich Deaktivieren, endgültigem
Löschen und **Passwort zurücksetzen** — erklärt die Referenzseite
[Benutzer](../admin/users.md).

## Schritt 3: Profile und Rollen zuordnen

Öffnen Sie jeden Benutzer und prüfen Sie im Bereich **Profile und Rollen**:

* **Rollen** — bestimmen, was der Benutzer darf. Bei importierten
  Entra-Benutzern werden Rollen über die Gruppen-Zuordnung aus Schritt 2
  vergeben.
* **Profile** — bestimmen, mit welchen Arbeitsbereichen der Benutzer arbeiten
  darf (Referenz: [Profile](../admin/profiles.md)).

## Schritt 4: Anmeldung testen

1. Melden Sie sich ab und mit dem neuen Konto wieder an (Referenz:
   [Anmelden und Abmelden](../admin/login.md)):
    * Lokale Benutzer: Login und Passwort eingeben, **Anmelden**.
    * Entra-Benutzer: **Mit Microsoft anmelden** klicken und die
      Microsoft-Anmeldung durchlaufen.
    * LDAP-Benutzer: Domänen-Login und Domänen-Passwort in die normalen
      Anmeldefelder eingeben, **Anmelden**.
2. Prüfen Sie, ob die Navigation nur die Bereiche zeigt, die die Rollen des
   Benutzers erlauben — Einträge ohne Berechtigung werden ausgeblendet oder
   gesperrt.

## Ergebnis

* Die Rollen bilden Ihre Arbeitsteilung ab.
* Jeder Mitarbeiter hat ein eigenes Konto (lokal oder aus Entra/LDAP
  importiert) mit zugeordneten Rollen und Profilen.
* Die Anmeldung ist mit mindestens einem neuen Konto erfolgreich getestet.

## Wenn etwas nicht klappt

* Anmeldung schlägt fehl, Konto gesperrt oder „Mit Microsoft anmelden"
  bricht ab → [Login-Probleme](../help/login-problems.md)
* Import findet keine Benutzer → Konfiguration im jeweiligen Tab prüfen,
  siehe [Authentifizierung](../admin/authentication.md)
* Ein Benutzer sieht zu viel oder zu wenig → Rollen-Zuordnung prüfen, siehe
  [Rollen und Berechtigungen](../admin/roles.md) und
  [Benutzer](../admin/users.md)
* Weitere Hilfe → [Hilfe-Übersicht](../help/index.md) und
  [Support kontaktieren](../help/support.md)
