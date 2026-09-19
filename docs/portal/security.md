# Passwort und zweiter Faktor

!!! abstract "Referenz — Die Seite „Passwort und zweiter Faktor" im Lizenzportal: eigenes Passwort ändern und die Anmeldung in zwei Schritten einrichten"

## Wofür Sie diesen Bereich nutzen

Ihr Konto-Passwort gilt für das Lizenzportal, die Desktop-App und die
Web-App gleichermaßen — geändert wird es **nur hier**. Außerdem richten Sie
hier den **zweiten Faktor** ein: Danach verlangt jede Anmeldung zusätzlich
einen sechsstelligen Code aus einer Authenticator-App, und ein erratenes
Passwort allein reicht nicht mehr.

Sie erreichen die Seite über den Menüpunkt **Passwort und zweiter Faktor**
in der Kopfleiste des Portals.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Passwort und zweiter Faktor im Lizenzportal: Formular zum Passwortwechsel und die Karte „Zweiter Faktor".
    **So erzeugen:** Lizenzportal lokal (localhost:8100), Seite `/passwort`; automatisch per `python _tools/web_screenshots.py shots nur:portal-passwort`
    **Ziel-Datei:** `assets/screenshots/portal/passwort.png`
    <!-- web-bild ../assets/screenshots/portal/passwort.png -->

## Bedienelemente im Detail

### Passwort ändern

| Feld / Schaltfläche | Bedeutung |
|---|---|
| **Aktuelles Passwort** | Ihr bisheriges Passwort. |
| **Neues Passwort** | Mindestens **10 Zeichen**. |
| **Noch einmal** | Wiederholung des neuen Passworts. |
| **Passwort ändern** | Speichert das neue Passwort. Es gilt sofort — auch für die nächste Anmeldung in der Desktop-App und der Web-App. |

!!! warning "Desktop-App offline"
    Die Desktop-App merkt sich für die Offline-Anmeldung das Passwort der
    letzten **Online**-Anmeldung. Nach einer Passwortänderung melden Sie sich
    dort einmal mit Internetverbindung an, damit auch der Offline-Weg das
    neue Passwort kennt.

### Zweiter Faktor

| Zustand | Was die Karte zeigt |
|---|---|
| **Nicht eingerichtet** | Hinweis und Schaltfläche **Jetzt einrichten**. Für Kundenbenutzer ist der zweite Faktor freiwillig, aber empfohlen — besonders für Administratoren. |
| **Eingerichtet** | Bestätigung, dass bei jeder Anmeldung der Code verlangt wird, und der Hinweis, dass Herzog den zweiten Faktor bei Bedarf zurücksetzt. |

#### So richten Sie den zweiten Faktor ein

1. Klicken Sie auf **Jetzt einrichten**. Die Seite **Zweiter Faktor
   einrichten** zeigt einen QR-Code.
2. Öffnen Sie eine Authenticator-App auf dem Handy — z. B. **1Password**,
   **Bitwarden**, **Microsoft Authenticator** oder **Google Authenticator**
   — und scannen Sie den Code. Kann die App nicht scannen, tragen Sie den
   darunter angezeigten **Schlüssel** von Hand ein; am Handy geht es auch
   über den Link **In der Authenticator-App öffnen**.
3. Tippen Sie zur Bestätigung den **aktuellen Code** aus der App in das
   Feld ein und klicken Sie auf **Einrichten**.

Ab jetzt fragen Portal, Desktop-App und Web-App nach Passwort **und** Code:

* Im **Portal** folgt nach dem Passwort eine eigene Seite für den Code.
* In der **Desktop-App** blendet der Anmeldedialog nach dem ersten Klick auf
  **Anmelden** das Feld **Code (Authenticator-App)** ein.
* In der **Web-App** erscheint das Feld **Code** unter dem Passwort.

!!! warning "Zugriff auf die App verloren?"
    Der zweite Faktor lässt sich nicht selbst abschalten. Ist das Handy weg,
    wenden Sie sich an Herzog — der Support setzt den zweiten Faktor für
    Ihren Benutzer zurück, danach können Sie ihn neu einrichten.

## Verwandte Seiten

* [Lizenzportal](index.md) — Anmelden und *Passwort vergessen*
* [Anmelden und Abmelden (Desktop-App)](../admin/login.md)
* [Anmelden (Web-App)](../web/login.md)
* [Login-Probleme](../help/login-problems.md)
