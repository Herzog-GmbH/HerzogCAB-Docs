# Authentifizierung

!!! abstract "Referenz — Anmeldung über Microsoft Entra ID oder LDAP / Active Directory einrichten, inklusive Gruppen-zu-Rollen-Zuordnung."

## Wofür Sie diesen Bereich nutzen

Unter *Systemverwaltung > Authentifizierung* binden Sie Herzog CAB an das
Benutzerverzeichnis Ihres Unternehmens an. Danach können sich Mitarbeiter
zusätzlich zu den lokalen Konten

* mit ihrem **Microsoft-Konto** anmelden (Schaltfläche
  [**Mit Microsoft anmelden**](login.md#mit-microsoft-anmelden) im
  Anmeldefenster), oder
* mit ihrem **Windows-Domänenkonto** über LDAP / Active Directory — direkt im
  Firmennetz, auch ohne Internet.

Lokale Herzog-CAB-Konten (Benutzername + Passwort) funktionieren unabhängig
davon weiter und auch offline.

!!! warning "Berechtigung erforderlich"
    Diesen Bereich sehen und nutzen nur Benutzer mit dem Recht
    **Benutzer verwalten**.

!!! info "Voraussetzung für Microsoft Entra ID"
    Bevor Sie hier Werte eintragen können, muss die IT-Administration Ihres
    Unternehmens einmalig eine **App-Registrierung** im eigenen
    Microsoft-Entra-Verzeichnis anlegen (Dauer ca. 10 Minuten). Die
    Schritt-für-Schritt-Anleitung dafür erhalten Sie von Ihrem
    Herzog-Ansprechpartner. Herzog erhält dabei keinerlei Zugriff auf Ihr
    Verzeichnis; ein Client-Geheimnis oder Zertifikat ist **nicht** nötig.

## Der Bildschirm im Überblick

Der Bildschirm **AUTHENTIFIZIERUNG** hat zwei Reiter — **Microsoft Entra ID**
und **LDAP / Active Directory**. Unter den Reitern liegen eine gemeinsame
Fehlerzeile und die Schaltfläche **Speichern**, die die Einstellungen beider
Reiter sichert.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Bildschirm „Authentifizierung", Reiter „Microsoft Entra ID" mit Konfigurationsfeldern und der Tabelle „Entra-Gruppe → Rolle"
    **So erzeugen:** *Systemverwaltung > Authentifizierung* öffnen (Reiter Microsoft Entra ID aktiv); Beispieldaten ohne echte Tenant-/Client-IDs verwenden
    **Ziel-Datei:** `assets/screenshots/admin/authentifizierung-entra.png`

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Bildschirm „Authentifizierung", Reiter „LDAP / Active Directory" mit allen Verbindungsfeldern und der Schaltfläche „Verbindung prüfen"
    **So erzeugen:** *Systemverwaltung > Authentifizierung* öffnen, Reiter „LDAP / Active Directory" wählen; Beispieldaten (example.local) verwenden
    **Ziel-Datei:** `assets/screenshots/admin/authentifizierung-ldap.png`

## Reiter „Microsoft Entra ID"

Solange **Anmeldung mit Microsoft Entra ID aktivieren** nicht angehakt ist,
sind alle übrigen Felder des Reiters gesperrt.

### Verbindungsdaten

| Feld | Bedeutung |
|---|---|
| **Anmeldung mit Microsoft Entra ID aktivieren** | Schaltet die Microsoft-Anmeldung frei. Erst danach erscheint im Anmeldefenster die Schaltfläche **Mit Microsoft anmelden**. |
| **Verzeichnis (Tenant)** | Ihr Microsoft-Verzeichnis: entweder das Schlüsselwort `organizations` (Standard) oder die konkrete **Verzeichnis-(Mandanten-)ID** aus der App-Registrierung. |
| **Client-ID** | Die **Anwendungs-(Client-)ID** der in Ihrem Verzeichnis registrierten Herzog-CAB-App. Pflichtfeld — ohne Client-ID lässt sich die aktivierte Entra-Anmeldung nicht speichern. |
| **Redirect-Port (Loopback)** | Port, über den die Antwort der Microsoft-Anmeldung auf diesem Rechner ankommt. Empfehlung: **automatisch** (Wert 0) — Herzog CAB wählt dann selbst einen freien Port. |
| **Login-Name aus** | Legt fest, welcher Verzeichnis-Eintrag zum Herzog-CAB-Anmeldenamen wird: **Benutzerprinzipalname (userPrincipalName)** (Regelfall), **E-Mail (mail)** oder **Lokaler Anmeldename (onPremisesSamAccountName)**. |
| **Konto beim ersten Login automatisch anlegen (JIT)** | Ist das Häkchen gesetzt, legt Herzog CAB beim ersten erfolgreichen Microsoft-Login automatisch ein passendes Benutzerkonto an — Sie müssen niemanden vorab importieren. Ohne Häkchen können sich nur bereits vorhandene bzw. [importierte](users.md#benutzer-aus-microsoft-entra-importieren) Konten anmelden. |
| **Standard-Profil** | Optional: Profil (Arbeitsbereich), dem Microsoft-Anmelder automatisch zugewiesen werden. *— keine automatische Zuweisung —* lässt die Zuweisung dem Administrator. |
| **Import nur aus Gruppe** | Optional, empfohlen: Objekt-ID einer Verzeichnis-Gruppe. Der [Benutzer-Import](users.md#benutzer-aus-microsoft-entra-importieren) zeigt dann nur deren Mitglieder statt aller Verzeichnis-Benutzer. **Suchen…** öffnet den Dialog *Entra-Gruppe auswählen*, damit Sie die Gruppe bequem per Name finden, statt die ID von Hand einzutragen; unter dem Feld erscheint danach *Gewählt: &lt;Gruppenname&gt;*. Leer = alle Benutzer importierbar. |

### Tabelle „Entra-Gruppe → Rolle"

Mitglieder einer Entra-Sicherheitsgruppe erhalten bei der Anmeldung
automatisch die zugeordnete [Rolle](roles.md). Passt keine Gruppe, bleiben
die manuell zugewiesenen Rollen unangetastet.

| Element | Beschreibung |
|---|---|
| Spalten **Gruppe / Gruppen-ID / Rolle** | Anzeigename der Gruppe, ihre Objekt-ID im Verzeichnis und die Herzog-CAB-Rolle, die Mitglieder erhalten. Die Rolle wählen Sie je Zeile per Auswahlliste. |
| **Aus Entra wählen…** | Öffnet den Dialog *Entra-Gruppe auswählen* (Suchfeld, Spalten *Gruppe* und *Beschreibung*, **Übernehmen**) und fügt die gewählte Gruppe als neue Zeile ein. |
| **Manuell hinzufügen** | Fügt eine leere Zeile ein, in die Sie Gruppenname und Objekt-ID selbst eintragen. |
| **Entfernen** | Löscht die markierte Zeile. |

!!! info "Anmeldung für die Gruppensuche"
    Für **Suchen…** und **Aus Entra wählen…** meldet sich Herzog CAB einmalig
    per Microsoft-Fenster am Verzeichnis an, um die Gruppenliste zu laden.

## Reiter „LDAP / Active Directory"

Anmeldung gegen einen Domänencontroller im Haus — funktioniert offline im
LAN. Benutzer melden sich mit Name + Passwort im normalen Anmeldefenster an
(kein Browser). Solange **Anmeldung über LDAP / Active Directory aktivieren**
nicht angehakt ist, sind alle übrigen Felder gesperrt.

| Feld | Bedeutung |
|---|---|
| **Anmeldung über LDAP / Active Directory aktivieren** | Schaltet die LDAP-Anmeldung frei. |
| **LDAP-URL** | Adresse des Domänencontrollers, z. B. `ldaps://dc-1.example.local:636`. Pflichtfeld (zusammen mit dem Basis-DN). Empfohlen ist die verschlüsselte Variante `ldaps://`. |
| **Domänenname** | Name Ihrer Windows-Domäne, z. B. `example.local`. |
| **Domänenpräfix** | Präfix vor dem Anmeldenamen, z. B. `EXAMPLE\`. |
| **Bind-Konto** | Dienstkonto, mit dem Herzog CAB das Verzeichnis durchsuchen darf (als UPN oder DN). |
| **Bind-Passwort** | Passwort des Dienstkontos (verdeckte Eingabe). |
| **Basis-DN (Personensuche)** | Startpunkt der Benutzersuche im Verzeichnisbaum, z. B. `DC=example,DC=local`. Pflichtfeld. |
| **Suchfilter Personen** | Filter, mit dem Anmeldename auf Verzeichniseintrag abgebildet wird; Standard: `(&(objectClass=person)(sAMAccountName={user}))` — `{user}` steht für den eingegebenen Anmeldenamen. |
| **Login-Attribut** | Verzeichnis-Attribut, das als Herzog-CAB-Anmeldename dient; Standard `sAMAccountName` (der Windows-Anmeldename). |
| **Basis-DN (Gruppensuche)** | Optionaler eigener Startpunkt für die Gruppensuche — leer lassen, wenn Gruppen im selben Zweig liegen. |
| **Verbindungs-Timeout (Sek.)** / **Such-Timeout (Sek.)** | Wartezeiten (1–120 Sekunden), bevor ein Verbindungs- bzw. Suchversuch abgebrochen wird. |
| **LDAPS-Zertifikat nicht prüfen (nur Test / selbstsigniert)** | Überspringt die Zertifikatsprüfung der verschlüsselten Verbindung. Nur für Tests oder selbstsignierte Zertifikate — im Produktivbetrieb ausgeschaltet lassen. |
| **Verbindung prüfen** | Testet die Verbindung mit den aktuellen Eingaben (auch vor dem Speichern). Ergebnis erscheint direkt daneben: *Verbindung erfolgreich.* oder eine Fehlermeldung. |

!!! info "Rollen und Profil bei LDAP-Konten"
    Die Tabelle **Gruppe → Rolle** und das **Standard-Profil** vom
    Entra-Reiter gelten auch für LDAP-Konten: Bei jeder Anmeldung liest
    Herzog CAB die Gruppenmitgliedschaften aus dem Verzeichnis und
    aktualisiert die Rollen entsprechend (das Verzeichnis ist führend).
    Liefert keine Gruppe einen Treffer, bleiben manuell zugewiesene Rollen
    erhalten. Ist das Verzeichnis vorübergehend nicht erreichbar, gilt der
    zuletzt gespeicherte Stand — die Anmeldung gelingt trotzdem.

## Speichern

**Speichern** sichert beide Reiter gemeinsam. Vor dem Speichern prüft
Herzog CAB die Eingaben:

* Ist Entra aktiviert, muss eine **Client-ID** eingetragen sein.
* Ist LDAP aktiviert, müssen **LDAP-URL** und **Basis-DN** eingetragen sein.

Fehler erscheinen in der roten Fehlerzeile über der Schaltfläche; bei Erfolg
meldet Herzog CAB *„Anmelde-Einstellungen gespeichert."*

## Verwandte Seiten

* [Anmeldung und Abmelden](login.md) — wie die Microsoft-Anmeldung für Benutzer aussieht
* [Benutzer](users.md) — Import aus Entra bzw. LDAP, Konten pflegen
* [Rollen und Berechtigungen](roles.md) — welche Rechte eine Rolle bündelt
* [Benutzer und Rollen einrichten](../tasks/setup-users.md)
