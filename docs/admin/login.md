# Anmeldung und Abmelden

!!! abstract "Referenz — Das Anmeldefenster von Herzog CAB: lokale Anmeldung, Microsoft-Anmeldung, Kontosperre und Profil-Auswahl."

## Wofür Sie diesen Bereich nutzen

Herzog CAB verlangt vor dem Öffnen des Arbeitsbereichs eine **Anmeldung**. So
ist nachvollziehbar, wer welche Daten bearbeitet, und die
[Rollen und Berechtigungen](roles.md) greifen pro Benutzer. Nach der
Anmeldung wählen Sie das [Profil](profiles.md) (den Arbeitsbereich), mit dem
Sie arbeiten möchten.

!!! info "Erstanmeldung"
    Bei einer frischen Installation legen Sie beim ersten Programmstart
    zunächst ein Administrator-Konto an — siehe
    [Erststart und Einrichtung](../setup/first-run.md).

## Der Bildschirm im Überblick

Beim Start erscheint das Anmeldefenster **Herzog CAB – Anmelden** mit dem
HERZOG-Logo, den Eingabefeldern und — falls eingerichtet — der
Microsoft-Schaltfläche.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Anmeldefenster „Herzog CAB – Anmelden" mit Logo, Feldern Login/Passwort und der Schaltfläche „Mit Microsoft anmelden"
    **So erzeugen:** Herzog CAB starten (Entra-Anmeldung muss unter *Systemverwaltung > Authentifizierung* aktiviert sein, sonst fehlt die Microsoft-Schaltfläche)
    **Ziel-Datei:** `assets/screenshots/admin/anmelden.png`

## Bedienelemente im Detail

### Login und Passwort

| Element | Beschreibung |
|---|---|
| **Login** | Ihr Anmeldename. Herzog CAB füllt hier automatisch den zuletzt verwendeten Anmeldenamen dieses Windows-Benutzers vor; der Cursor steht dann bereits im Passwort-Feld. |
| **Passwort** | Ihr Passwort (verdeckte Eingabe). Mit ++enter++ lösen Sie die Anmeldung direkt aus. |
| **Anmelden** | Prüft die Eingaben und öffnet bei Erfolg die Profil-Auswahl. |
| **Abbrechen** | Beendet den Anmeldevorgang. |

Über die Felder Login/Passwort melden sich sowohl **lokale Konten** als auch
**LDAP-/Active-Directory-Konten** an — bei letzteren prüft Herzog CAB das
Passwort direkt gegen den Domänencontroller im Firmennetz (kein Browser
nötig, funktioniert offline im LAN).

### Mit Microsoft anmelden

Die Schaltfläche **Mit Microsoft anmelden** erscheint nur, wenn ein
Administrator die Microsoft-Anmeldung unter
[*Systemverwaltung > Authentifizierung*](authentication.md) eingerichtet und
aktiviert hat. So läuft die Anmeldung ab:

1. Klicken Sie auf **Mit Microsoft anmelden**. Im Anmeldefenster erscheint
   der Hinweis *„Browser geöffnet — bitte im Microsoft-Fenster anmelden…"*;
   die Schaltfläche ist währenddessen gesperrt.
2. Herzog CAB öffnet ein **eigenes kleines Browser-Fenster** (ohne Tabs und
   Adressleiste, mittig auf dem Bildschirm) mit der vertrauten
   Microsoft-Anmeldeseite. Melden Sie sich dort mit Ihrem Microsoft-Konto an.
3. Nach erfolgreicher Anmeldung zeigt das Fenster kurz *„Anmeldung
   erfolgreich"* und **schließt sich automatisch**. Herzog CAB fährt sofort
   mit der Profil-Auswahl fort.

!!! info "Ihr Microsoft-Passwort bleibt bei Microsoft"
    Das Microsoft-Passwort wird **nie** in Herzog CAB eingegeben oder
    gespeichert — die gesamte Anmeldung läuft im Microsoft-Fenster.

!!! tip "Fenster schließt sich nicht automatisch?"
    Das eigene Anmeldefenster nutzt Herzog CAB, wenn Ihr Standardbrowser auf
    Chromium basiert (z. B. Microsoft Edge, Google Chrome). Bei anderen
    Browsern öffnet sich die Microsoft-Anmeldung als normaler Browser-Tab —
    die Anmeldung funktioniert genauso, nur schließen Sie den Tab danach
    selbst.

Bricht die Microsoft-Anmeldung ab oder dauert sie zu lange, zeigt das
Anmeldefenster eine Meldung (z. B. *„Zeitüberschreitung bei der
Microsoft-Anmeldung."*) und Sie können es erneut versuchen.

### Profil-Auswahl nach der Anmeldung

Direkt nach der erfolgreichen Anmeldung fragt der Dialog **Profil auswählen**,
welcher Arbeitsbereich geöffnet werden soll. Mit **Profil öffnen** starten
Sie in das gewählte Profil; **Profile verwalten …** führt in die
[Profilverwaltung](profiles.md).

## Kontosperre bei Fehlversuchen

Nach **fünf** fehlgeschlagenen Anmeldeversuchen kurz hintereinander wird die
Anmeldung für dieses Konto vorübergehend gesperrt (*„Zu viele Fehlversuche.
Bitte später erneut versuchen."*). Das schützt vor dem systematischen
Durchprobieren von Passwörtern. Warten Sie etwa eine Minute und versuchen Sie
es erneut — die Sperre löst sich von selbst. Ist das Passwort tatsächlich
vergessen, kann ein Administrator es
[zurücksetzen](users.md#passwort-zurucksetzen).

## Meldungen des Anmeldefensters

| Meldung | Bedeutung |
|---|---|
| *Login oder Passwort ist falsch.* | Anmeldename unbekannt oder Passwort falsch. |
| *Dieses Benutzerkonto ist deaktiviert.* | Das Konto wurde in der [Benutzerverwaltung](users.md) deaktiviert. |
| *Zu viele Fehlversuche. Bitte später erneut versuchen.* | Kontosperre, siehe oben. |
| *Dieses Konto meldet sich über einen anderen Anbieter an.* | Für dieses Konto ist z. B. die Microsoft-Anmeldung vorgesehen — nutzen Sie **Mit Microsoft anmelden** statt des Passwort-Felds. |
| *Die Microsoft-Anmeldung ist nicht konfiguriert.* | Die Einrichtung unter [Authentifizierung](authentication.md) ist unvollständig — wenden Sie sich an Ihren Administrator. |

## Abmelden und Profil wechseln

* **Abmelden:** Klicken Sie unten links in der Navigationsleiste auf Ihren
  Namen bzw. Ihr Profilbild und wählen Sie im Dialog
  [Mein Profil](my-profile.md) die Schaltfläche **Abmelden**.
* **Profil wechseln:** erfolgt über einen Programmneustart, damit keine
  ungespeicherten Eingaben verloren gehen — siehe
  [Profile (Arbeitsbereiche)](profiles.md#profil-wechseln).

## Verwandte Seiten

* [Benutzer](users.md) — Konten anlegen, Passwort zurücksetzen
* [Authentifizierung](authentication.md) — Microsoft Entra ID und LDAP einrichten
* [Mein Profil](my-profile.md) — eigenes Konto und Abmelden
* [Probleme bei der Anmeldung](../help/login-problems.md)
