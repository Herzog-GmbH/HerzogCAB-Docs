# Benutzer

!!! abstract "Referenz — Benutzerkonten anlegen, bearbeiten, importieren, deaktivieren und Passwörter zurücksetzen."

## Wofür Sie diesen Bereich nutzen

In der Benutzerverwaltung (*Systemverwaltung > Benutzer*) pflegen Sie alle
Konten, mit denen sich Kolleginnen und Kollegen an Herzog CAB anmelden.
Konten können lokal angelegt oder aus **Microsoft Entra** bzw.
**LDAP / Active Directory** importiert werden. Hier weisen Sie außerdem pro
[Profil](profiles.md) die [Rollen](roles.md) zu.

!!! warning "Berechtigung erforderlich"
    Diesen Bereich sehen und nutzen nur Benutzer mit dem Recht
    **Benutzer verwalten** (siehe [Rollen und Berechtigungen](roles.md)).

## Der Bildschirm im Überblick

Links steht die **Benutzerliste** mit Suchfeld und den Schaltflächen zum
Anlegen und Importieren, rechts der **Editor** des gewählten Benutzers.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Benutzerverwaltung — Benutzerliste links (mit den Schaltflächen „Neuer Benutzer", „Aus Entra importieren", „Aus LDAP importieren"), Benutzer-Editor rechts
    **So erzeugen:** *Systemverwaltung > Benutzer* öffnen, einen Benutzer auswählen
    **Ziel-Datei:** `assets/screenshots/admin/benutzer.png`

## Bedienelemente im Detail

### Benutzerliste (links)

| Element | Beschreibung |
|---|---|
| **Suche** | Filtert die Liste live nach Login, Anzeigename oder E-Mail. Unter der Liste steht die Trefferanzahl (z. B. *3 von 12 Benutzern*). |
| Listeneinträge | Zeigen Anzeigename und Login; deaktivierte Konten sind mit *inaktiv* gekennzeichnet. |
| **Neuer Benutzer** | Öffnet den Dialog *Neuen Benutzer anlegen* (siehe unten). |
| **Aus Entra importieren** | Öffnet den Abgleich mit Microsoft Entra (siehe unten). Nur nutzbar, wenn die Microsoft-Anmeldung unter [Authentifizierung](authentication.md) eingerichtet ist. |
| **Aus LDAP importieren** | Öffnet den Abgleich mit LDAP / Active Directory (siehe unten). Nur nutzbar, wenn LDAP unter [Authentifizierung](authentication.md) eingerichtet ist. |

### Benutzer-Editor (rechts)

| Feld / Schaltfläche | Beschreibung |
|---|---|
| **Login** | Anmeldename (z. B. `m.mustermann`). Muss eindeutig sein. |
| **Anzeigename** | Klartext-Name, der in der Oberfläche und auf Ausdrucken erscheint. |
| **E-Mail** | Optionale Kontaktadresse. |
| **Passwort** | Wird nicht angezeigt; über **Passwort zurücksetzen…** neu setzen (siehe unten). |
| **Aktiv** | Konto aktiv/deaktiviert. Deaktivierte Konten können sich nicht anmelden, bleiben aber mit allen Zuweisungen erhalten. |
| Info-Zeile | Zeigt *angelegt am*, *letzter Login* bzw. *noch nie angemeldet*. |

### Profile und Rollen

Im Abschnitt **Profile und Rollen** weisen Sie dem Benutzer **pro Profil**
(Arbeitsbereich) eine oder mehrere [Rollen](roles.md) zu — in der Tabelle mit
den Spalten *Profil*, *Zugewiesen* und *Rollen*. Über die Rollen-Spalte
öffnen Sie den Auswahl-Dialog **Rollen auswählen**. So kann derselbe Benutzer
in verschiedenen Profilen unterschiedliche Rechte haben.

!!! info "Globaler Administrator (SuperAdmin)"
    Ist ein Benutzer als globaler Administrator gekennzeichnet, hat er in
    **allen** Profilen vollen Zugriff — unabhängig von den Zuweisungen in der
    Tabelle. Der Editor blendet dazu einen entsprechenden Hinweis ein.

### Schaltflächen unten

| Schaltfläche | Beschreibung |
|---|---|
| **Deaktivieren** / **Aktivieren** | Schaltet das gewählte Konto inaktiv bzw. wieder aktiv (mit Sicherheitsabfrage). |
| **Endgültig löschen** | Entfernt das Konto unwiderruflich inklusive seiner Profil-Zuweisungen (mit Sicherheitsabfrage). Für ausgeschiedene Mitarbeiter genügt meist **Deaktivieren**. |
| **Speichern** | Sichert die Änderungen des Editors. |

!!! info "Eingebaute Schutzmechanismen"
    Sie können Ihr **eigenes Konto** weder deaktivieren noch löschen. Ebenso
    verweigert Herzog CAB das Deaktivieren oder Löschen des **letzten aktiven
    Administrators** — so sperren Sie sich nicht versehentlich aus.

## Neuen Benutzer anlegen

**Neuer Benutzer** öffnet den Dialog **Neuen Benutzer anlegen**:

| Feld | Beschreibung |
|---|---|
| **Login** | Eindeutiger Anmeldename. |
| **Anzeigename** | Klartext-Name. |
| **E-Mail** | Optional. |
| **Passwort** / **Passwort bestätigen** | Start-Passwort; beide Eingaben müssen übereinstimmen. |
| **Aktiv** | Konto direkt aktiv anlegen (Standard). |

Mit **Anlegen** wird das Konto erstellt; die Profil- und Rollen-Zuweisung
pflegen Sie anschließend direkt im Editor.

## Passwort zurücksetzen

Hat ein Benutzer sein Passwort vergessen, setzen Sie es hier neu:

1. *Systemverwaltung > Benutzer* öffnen.
2. Den betroffenen Benutzer in der Liste wählen.
3. Im Editor auf **Passwort zurücksetzen…** klicken.
4. Neues Passwort vergeben und bestätigen — Herzog CAB meldet
   *„Das Passwort wurde zurückgesetzt."*

!!! info "Konto nur vorübergehend gesperrt?"
    Nach mehreren fehlgeschlagenen Anmeldeversuchen wird ein Konto kurzzeitig
    gesperrt (siehe [Anmeldung und Abmelden](login.md#kontosperre-bei-fehlversuchen)).
    Die Sperre löst sich nach kurzer Zeit von selbst — ein Passwort-Reset ist
    dafür nicht nötig.

!!! tip "Eigenes Passwort ändern"
    Das eigene Passwort ändert jeder Benutzer selbst im Dialog
    [Mein Profil](my-profile.md#tab-passwort) — dafür ist kein Administrator
    nötig.

## Benutzer aus Microsoft Entra importieren

**Aus Entra importieren** öffnet den Dialog **Benutzer mit Microsoft Entra
abgleichen**. Voraussetzung ist eine eingerichtete Microsoft-Anmeldung
(sonst erscheint der Hinweis *„Die Microsoft-Anmeldung ist nicht konfiguriert
(Systemverwaltung → Authentifizierung)."*).

1. Beim Öffnen meldet sich Herzog CAB zunächst bei Microsoft an — es
   erscheint dasselbe Microsoft-Anmeldefenster wie beim
   [Login](login.md#mit-microsoft-anmelden). Danach lädt der Dialog die
   Benutzer aus dem Verzeichnis (*„Benutzer werden aus dem Verzeichnis
   geladen…"*).
2. Der Reiter **Importieren** listet die Verzeichnis-Benutzer mit *Name*,
   *Login (UPN)* und *E-Mail*. Haken Sie die gewünschten Personen an;
   bereits vorhandene Konten sind mit *„(bereits vorhanden)"* markiert und
   werden beim Import übersprungen. Ist unter
   [Authentifizierung](authentication.md) eine **Import-Gruppe** hinterlegt,
   zeigt die Liste nur deren Mitglieder.
3. Der Reiter **Ausgeschiedene** zeigt Herzog-CAB-Konten, deren Gegenstück im
   Verzeichnis fehlt oder gesperrt ist — mit Begründung (*nicht mehr im
   Verzeichnis*, *nicht in der Import-Gruppe*, *im Verzeichnis gesperrt*).
   Haken Sie an, welche dieser Konten deaktiviert werden sollen.
4. Über das Suchfeld filtern Sie die Listen nach Name, Login oder E-Mail.
5. **Übernehmen** führt Import und Deaktivierung aus; die Zusammenfassung
   meldet z. B. *„5 importiert, 1 deaktiviert. 2 übersprungen (bereits
   vorhanden)."* **Schließen** beendet den Dialog.

## Benutzer aus LDAP / Active Directory importieren

**Aus LDAP importieren** öffnet den Dialog **Benutzer mit LDAP / Active
Directory abgleichen**. Voraussetzung ist eine eingerichtete
LDAP-Konfiguration unter [Authentifizierung](authentication.md).

Der Ablauf entspricht dem Entra-Import, mit zwei Unterschieden:

* Statt einer Microsoft-Anmeldung fragt der Dialog das Verzeichnis direkt im
  Firmennetz ab. Oben können Sie den **Suchfilter** anpassen und mit
  **Suchen** die Abfrage erneut ausführen.
* Die Ergebnis-Tabelle zeigt *Name*, *Login* und *E-Mail*; der Reiter
  **Ausgeschiedene** funktioniert wie beim Entra-Import.

Mit **Übernehmen** werden die angehakten Benutzer angelegt bzw. deaktiviert.

!!! tip "Rollen automatisch über Verzeichnis-Gruppen"
    Damit importierte Benutzer automatisch die richtige Rolle erhalten,
    hinterlegen Sie unter [Authentifizierung](authentication.md) die
    Zuordnung **Gruppe → Rolle**.

## Verwandte Seiten

* [Rollen und Berechtigungen](roles.md) — was eine Rolle darf
* [Authentifizierung](authentication.md) — Microsoft Entra ID und LDAP einrichten
* [Mein Profil](my-profile.md) — was jeder Benutzer selbst ändern kann
* [Benutzer und Rollen einrichten](../tasks/setup-users.md) — Schritt-für-Schritt-Anleitung
