# Anmeldung und Abmelden

!!! abstract "Referenz — Das Anmeldefenster der Desktop-App: Kontobenutzer, lokale Anmeldung, Microsoft-Anmeldung, Kontosperre und Profil-Auswahl."

## Wofür Sie diesen Bereich nutzen

Herzog CAB verlangt vor dem Öffnen des Arbeitsbereichs eine **Anmeldung**. So
ist nachvollziehbar, wer welche Daten bearbeitet, und die
[Rollen und Berechtigungen](roles.md) greifen pro Benutzer. Nach der
Anmeldung wählen Sie das [Profil](profiles.md) (den Arbeitsbereich), mit dem
Sie arbeiten möchten.

Welches Anmeldefenster Sie sehen, hängt vom Lizenzweg ab:

| Lizenzweg | Anmeldefenster | Benutzer kommen aus … |
|---|---|---|
| **Kundenkonto** (Regelfall seit 2.0) | **Herzog CAB – Anmelden** mit E-Mail-Adresse, Passwort und ggf. Code | dem [Kundenkonto](../setup/account.md) — dieselben Zugangsdaten wie im Lizenzportal und in der Web-App. |
| **Dongle / CmAct-Lizenz** | **Herzog CAB – Anmelden** mit Login und Passwort, ggf. **Mit Microsoft anmelden** | der lokalen [Benutzerverwaltung](users.md), Microsoft Entra ID oder LDAP. |

!!! info "Erstanmeldung"
    Beim Kundenkonto ist der Benutzer, der den Rechner angemeldet hat, sofort
    im Programm angemeldet — siehe
    [Anmelden und Lizenz beziehen](../setup/activate-license.md). Bei einer
    Dongle-Installation legen Sie beim ersten Programmstart zunächst ein
    Administrator-Konto an — siehe
    [Erststart und Einrichtung](../setup/first-run.md).

---

## Anmeldung mit dem Kontobenutzer

Beim Start erscheint das Fenster **Herzog CAB – Anmelden** mit dem Hinweis
*„Melden Sie sich mit Ihrem Benutzer im Kundenkonto an – mit denselben
Zugangsdaten wie im Lizenzportal und in Herzog CAB Web."* Darunter steht
der Name Ihres Kontos (*Konto: &lt;Firma&gt;*).

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Anmeldefenster „Herzog CAB – Anmelden" im Kontomodell: Hinweistext, Zeile „Konto: &lt;Firma&gt;", Felder E-Mail-Adresse und Passwort, Schaltflächen Anmelden und Beenden.
    **So erzeugen:** Kunden-Build auf einem am Konto angemeldeten Rechner ein zweites Mal starten.
    **Ziel-Datei:** `assets/screenshots/admin/anmelden-konto.png`

### Bedienelemente

| Element | Beschreibung |
|---|---|
| **E-Mail-Adresse** | Ihr Anmeldename im Kundenkonto. Herzog CAB füllt hier den zuletzt an diesem Rechner angemeldeten Benutzer vor, beim ersten Mal den Benutzer, der den Rechner angemeldet hat. Ein Klick in das Feld markiert den Inhalt, damit Sie ihn direkt überschreiben können. |
| **Passwort** | Ihr Konto-Passwort (verdeckte Eingabe). Mit ++enter++ lösen Sie die Anmeldung direkt aus. |
| **Code (Authenticator-App)** | Erscheint nur, wenn für Ihren Benutzer der [zweite Faktor](../portal/security.md) eingerichtet ist — nach dem ersten Klick auf **Anmelden**. Sechs Ziffern aus der Authenticator-App. |
| **Anmelden** | Prüft die Zugangsdaten am Lizenzserver und öffnet bei Erfolg die Profil-Auswahl. |
| **Beenden** | Beendet Herzog CAB. |

### Rollen und Rechte

Ihre Rolle im Programm entspricht Ihrer Rolle im Kundenkonto:
**Administrator** = globaler Administrator mit allen Rechten in allen
Profilen, **Bearbeiter** und **Betrachter** = die gleichnamigen
Standardrollen. Ändert ein Administrator Ihre Rolle im Lizenzportal, gilt
das ab der nächsten Online-Anmeldung. Welche Profile Sie sehen, legt
weiterhin die lokale [Benutzerverwaltung](users.md) fest.

### Anmelden ohne Internet

Ist der Lizenzserver nicht erreichbar, lässt Herzog CAB die Anmeldung
trotzdem zu — für Benutzer, die sich **auf diesem Rechner schon einmal
online angemeldet** haben, mit dem Passwort von damals. Nach der Anmeldung
erscheint der Hinweis *„Der Lizenzserver ist nicht erreichbar. Sie sind mit
den zuletzt bekannten Rollen angemeldet …"*. Änderungen an Benutzern und
Rollen im Konto kommen erst beim nächsten Online-Start an.

### Meldungen des Anmeldefensters (Kontobenutzer)

| Meldung | Bedeutung |
|---|---|
| *E-Mail-Adresse oder Passwort stimmen nicht.* | Zugangsdaten prüfen; das Passwort setzen Sie über **Passwort vergessen** im [Lizenzportal](../portal/index.md) zurück. |
| *Für diesen Benutzer ist die Zwei-Faktor-Anmeldung eingerichtet. Bitte den aktuellen Code …* | Kein Fehler — den Code aus der Authenticator-App eintragen. |
| *Der Code stimmt nicht.* | Uhrzeit des Handys prüfen und den nächsten Code abwarten. |
| *Dieser Benutzer ist deaktiviert.* | Ein Administrator hat den Benutzer im Lizenzportal deaktiviert. |
| *Zu viele Fehlversuche. Bitte später erneut versuchen.* | Der Lizenzserver bremst nach mehreren Fehlversuchen — einige Minuten warten. |
| *Der Lizenzserver ist nicht erreichbar (…). Offline anmelden kann sich nur, wer sich auf diesem Rechner schon einmal online angemeldet hat …* | Verbindung prüfen — oder einen Benutzer nehmen, der hier schon einmal online war. |
| *Die Anmeldung am Kundenkonto war erfolgreich, aber der Benutzer konnte im Programm nicht angemeldet werden …* | Selten; meist ist die lokale Benutzerdatei nicht beschreibbar — siehe [Login-Probleme](../help/login-problems.md). |

---

## Anmeldung bei Dongle-Installationen

Beim Start erscheint das Anmeldefenster **Herzog CAB – Anmelden** mit dem
HERZOG-Logo, den Eingabefeldern und — falls eingerichtet — der
Microsoft-Schaltfläche.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Anmeldefenster „Herzog CAB – Anmelden" mit Logo, Feldern Login/Passwort und der Schaltfläche „Mit Microsoft anmelden"
    **So erzeugen:** Herzog CAB mit Dongle starten (Entra-Anmeldung muss unter *Systemverwaltung > Authentifizierung* aktiviert sein, sonst fehlt die Microsoft-Schaltfläche)
    **Ziel-Datei:** `assets/screenshots/admin/anmelden.png`

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

### Kontosperre bei Fehlversuchen

Nach **fünf** fehlgeschlagenen Anmeldeversuchen kurz hintereinander wird die
Anmeldung für dieses Konto vorübergehend gesperrt (*„Zu viele Fehlversuche.
Bitte später erneut versuchen."*). Das schützt vor dem systematischen
Durchprobieren von Passwörtern. Warten Sie etwa eine Minute und versuchen Sie
es erneut — die Sperre löst sich von selbst. Ist das Passwort tatsächlich
vergessen, kann ein Administrator es
[zurücksetzen](users.md#passwort-zurucksetzen).

### Meldungen des Anmeldefensters (lokale Konten)

| Meldung | Bedeutung |
|---|---|
| *Login oder Passwort ist falsch.* | Anmeldename unbekannt oder Passwort falsch. |
| *Dieses Benutzerkonto ist deaktiviert.* | Das Konto wurde in der [Benutzerverwaltung](users.md) deaktiviert. |
| *Zu viele Fehlversuche. Bitte später erneut versuchen.* | Kontosperre, siehe oben. |
| *Dieses Konto meldet sich über einen anderen Anbieter an.* | Für dieses Konto ist z. B. die Microsoft-Anmeldung vorgesehen — nutzen Sie **Mit Microsoft anmelden** statt des Passwort-Felds. |
| *Die Microsoft-Anmeldung ist nicht konfiguriert.* | Die Einrichtung unter [Authentifizierung](authentication.md) ist unvollständig — wenden Sie sich an Ihren Administrator. |

---

## Profil-Auswahl nach der Anmeldung

Direkt nach der erfolgreichen Anmeldung fragt der Dialog **Profil auswählen**,
welcher Arbeitsbereich geöffnet werden soll — sofern Ihnen mehr als ein
Profil zugewiesen ist. Mit **Profil öffnen** starten Sie in das gewählte
Profil; **Profile verwalten …** führt in die [Profilverwaltung](profiles.md).
Ist genau ein Profil zugewiesen, öffnet Herzog CAB es ohne Nachfrage.

## Abmelden und Profil wechseln

* **Abmelden:** Klicken Sie unten links in der Navigationsleiste auf Ihren
  Namen bzw. Ihr Profilbild und wählen Sie im Dialog
  [Mein Profil](my-profile.md) die Schaltfläche **Abmelden**. Das meldet nur
  den **Benutzer** ab — der Rechner bleibt am Kundenkonto angemeldet und
  behält seine Plätze. Den Rechner selbst melden Sie unter
  [*Einstellungen > Lizenz*](settings/license.md) ab.
* **Profil wechseln:** erfolgt über einen Programmneustart, damit keine
  ungespeicherten Eingaben verloren gehen — siehe
  [Profile (Arbeitsbereiche)](profiles.md#profil-wechseln).

## Verwandte Seiten

* [Anmelden und Lizenz beziehen](../setup/activate-license.md) — Rechner am Kundenkonto anmelden
* [Passwort, zweiter Faktor und Name](../portal/security.md) — Passwort ändern, Authenticator-App
* [Benutzer](users.md) — Konten anlegen bzw. aus dem Kundenkonto übernehmen
* [Authentifizierung](authentication.md) — Microsoft Entra ID und LDAP einrichten (Dongle-Installationen)
* [Mein Profil](my-profile.md) — eigenes Konto und Abmelden
* [Probleme bei der Anmeldung](../help/login-problems.md)
