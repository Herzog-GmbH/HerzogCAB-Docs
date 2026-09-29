# Login-Probleme

!!! question "Problemlösung — Anmeldung bei Herzog CAB schlägt fehl"

Herzog CAB verlangt vor dem Öffnen des Arbeitsbereichs eine Anmeldung — mit
dem **Kontobenutzer** (Regelfall seit 2.0), bei Dongle-Installationen lokal
mit Login und Passwort oder über **Microsoft Entra ID**. Grundlagen zur
Anmeldung finden Sie unter [Anmeldung und Abmelden](../admin/login.md).

## Anmeldung mit dem Kontobenutzer (Desktop-App, Web-App, Lizenzportal)

**„E-Mail-Adresse oder Passwort stimmen nicht."**
Prüfen Sie die Adresse und die Feststelltaste. Das Passwort setzen Sie selbst
über **Passwort vergessen** auf der Anmeldeseite des
[Lizenzportals](../portal/index.md) zurück — der Link gilt eine Stunde. Das
neue Passwort gilt sofort auch für Desktop- und Web-App.

**Das Feld „Code (Authenticator-App)" erscheint.**
Kein Fehler: Für Ihren Benutzer ist der [zweite Faktor](../portal/security.md)
eingerichtet. Tragen Sie den aktuellen sechsstelligen Code ein. Stimmt der
Code nicht, prüfen Sie die Uhrzeit des Handys; ist die App verloren, setzt
Herzog den zweiten Faktor zurück ([Support](support.md)).

**„Dieser Benutzer ist deaktiviert."**
Ein Administrator Ihres Kontos hat den Zugang im Lizenzportal deaktiviert —
siehe [Benutzer einladen und verwalten](../portal/users.md).

**„Zu viele Fehlversuche. Bitte später erneut versuchen."**
Der Lizenzserver bremst nach mehreren Fehlversuchen. Warten Sie einige
Minuten.

**„Der Lizenzserver ist nicht erreichbar … Offline anmelden kann sich nur, wer sich auf diesem Rechner schon einmal online angemeldet hat."**
Ohne Verbindung lässt die Desktop-App nur Benutzer herein, die auf diesem
Rechner schon einmal online angemeldet waren — mit dem Passwort von damals.
Verbindung prüfen oder mit einem solchen Benutzer anmelden.

**Einladungslink abgelaufen.**
Der Link aus der Einladungsmail gilt drei Tage. Ein Administrator erneuert
die Einladung im Lizenzportal unter **Benutzer**.

**Die Web-App meldet „Alle Plätze dieses Kontos sind gerade belegt".**
Alle Plätze des Kontos sind belegt, im Programm oder im Browser. Ein Platz
wird frei, sobald ein Kollege Herzog CAB beendet oder sich in der Web-App
abmeldet, im Web spätestens nach 15 Minuten ohne Aktivität. Wer gerade
arbeitet, zeigt das [Lizenzportal](../portal/licenses.md#wer-gerade-arbeitet).
Weitere Plätze bestellt ein Administrator unter
[Abo und Bestellung](../web/subscription.md).

**Nach dem Anmelden erscheint „Kein Zugang zur Webapp".**
Dem Konto fehlt ein Abo mit Web-App, oder die Testphase ist abgelaufen. Siehe
[Abo und Bestellung](../web/subscription.md).

## Lokale Anmeldung (Login und Passwort) — Dongle-Installationen

**„Login oder Passwort ist falsch."**
Prüfen Sie Groß-/Kleinschreibung und Feststelltaste. Nur ein Administrator
kann Ihr Passwort zurücksetzen – siehe [Eigenes Profil](../admin/my-profile.md).

**„Zu viele Fehlversuche. Bitte später erneut versuchen."**
Nach **fünf** fehlgeschlagenen Versuchen sperrt Herzog CAB das Konto für
kurze Zeit, um automatisiertes Passwort-Raten zu erschweren. Warten Sie
einige Minuten und versuchen Sie es erneut.

**„Dieses Benutzerkonto ist deaktiviert."**
Ein Administrator hat den Zugang gesperrt. Wenden Sie sich an ihn – siehe
[Benutzer verwalten](../admin/users.md).

**„Dieses Konto meldet sich über einen anderen Anbieter an."**
Ihr Konto ist als Microsoft-Entra- oder LDAP-Konto angelegt und hat deshalb
kein lokales Passwort. Melden Sie sich stattdessen über **Mit Microsoft
anmelden** an bzw. über Ihr Firmen-/Domänenkonto.

## Anmeldung mit Microsoft Entra ID

### Der Browser öffnet sich nicht

Herzog CAB öffnet die Microsoft-Anmeldung standardmäßig in einem eigenen,
kompakten Anmeldefenster (nicht im normalen Browser-Tab). Ist kein
Chromium-basierter Browser (Edge, Chrome …) als Standard eingerichtet oder
lässt sich dieser nicht starten, weicht Herzog CAB auf den Standardbrowser
in einem normalen Tab aus. Schlägt auch das fehl, erscheint:

> „Der Browser konnte nicht geöffnet werden."

* Prüfen Sie, ob unter Windows ein **Standardbrowser** festgelegt ist
  (*Einstellungen → Apps → Standard-Apps*).
* Öffnen Sie testweise eine beliebige Internetseite von Hand, um den
  Standardbrowser zu prüfen.

### Zeitüberschreitung oder Abbruch

**„Zeitüberschreitung bei der Microsoft-Anmeldung."**
Sie haben das Microsoft-Anmeldefenster zu lange offen gelassen. Klicken Sie
erneut auf **Mit Microsoft anmelden** und melden Sie sich zügig an.

**„Die Microsoft-Anmeldung wurde abgebrochen."**
Das Anmeldefenster wurde geschlossen, bevor die Anmeldung abgeschlossen war.
Versuchen Sie es erneut.

Prüfen Sie in beiden Fällen die Internetverbindung – die Anmeldung braucht
Zugriff auf `login.microsoftonline.com`.

### „Dieses Microsoft-Konto ist nicht für Herzog CAB freigeschaltet."

Diese Meldung bedeutet: Ihr Microsoft-Konto wurde erfolgreich bei Microsoft
angemeldet, aber Herzog CAB kennt es nicht – es existiert weder ein
passendes lokales Konto noch darf ein neues automatisch angelegt werden.

!!! info "Das kann nur ein Administrator klären"
    Bitten Sie Ihren Administrator, unter *Systemverwaltung →
    Authentifizierung* eine der folgenden Optionen zu prüfen:

    * Ist **„Konto beim ersten Login automatisch anlegen (JIT)"** aktiviert?
      Ohne diese Option muss Ihr Konto vorab manuell angelegt werden.
    * Ist Ihre Entra-Gruppe in der Tabelle **„Entra-Gruppe → Rolle"**
      hinterlegt, damit Sie beim Login automatisch die richtige Rolle
      erhalten?
    * Ist ein **Standard-Profil** hinterlegt, dem neue Konten automatisch
      zugewiesen werden?

    Siehe [Authentifizierung (Entra ID / LDAP)](../admin/authentication.md).

### „Die Microsoft-Anmeldung ist nicht konfiguriert."

Die Anmeldung mit Microsoft Entra ID wurde für diese Installation noch nicht
eingerichtet. Ein Administrator richtet sie unter *Systemverwaltung →
Authentifizierung* ein (Verzeichnis/Tenant, Client-ID) – siehe
[Authentifizierung (Entra ID / LDAP)](../admin/authentication.md).

### „Es existiert bereits ein lokales Konto mit diesem Namen."

Ihr Microsoft-Anmeldename stimmt mit einem bestehenden **lokalen** Konto
überein. Aus Sicherheitsgründen übernimmt Herzog CAB ein lokales Konto nicht
automatisch für die Microsoft-Anmeldung. Ein Administrator muss das lokale
Konto umbenennen oder auflösen, bevor Sie sich mit Microsoft anmelden können.

## Verwandte Seiten

* [Anmeldung und Abmelden](../admin/login.md)
* [Anmelden und Konto wählen (Web-App)](../web/login.md)
* [Passwort und zweiter Faktor (Lizenzportal)](../portal/security.md)
* [Authentifizierung (Entra ID / LDAP)](../admin/authentication.md)
* [Eigenes Profil](../admin/my-profile.md)
* [Rollen und Berechtigungen](../admin/roles.md)
