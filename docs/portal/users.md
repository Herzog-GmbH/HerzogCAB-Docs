# Benutzer einladen und verwalten

!!! abstract "Referenz — Die Seite „Benutzer" im Lizenzportal: Kollegen einladen, Rollen ändern, Zugänge deaktivieren"

## Wofür Sie diesen Bereich nutzen

Jeder, der sich in der Desktop-App, in der Web-App oder im Lizenzportal
anmelden soll, braucht einen **Benutzer im Kundenkonto**. Administratoren
laden hier Kollegen per E-Mail ein, legen ihre Rolle fest und schalten
ausgeschiedene Zugänge ab. Die Plätze gehören dem Konto, nicht dem
Benutzer — Sie können also beliebig viele Benutzer anlegen; die Plätze
begrenzen nur, wie viele Rechner bzw. gleichzeitige Browser-Sitzungen
Herzog CAB nutzen.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Benutzerliste im Lizenzportal mit Rolle, letzter Anmeldung und Status; darunter das Formular „Benutzer einladen".
    **So erzeugen:** Lizenzportal lokal (localhost:8100), Seite `/benutzer`; automatisch per `python _tools/web_screenshots.py shots nur:portal-benutzer`
    **Ziel-Datei:** `assets/screenshots/portal/benutzer.png`
    <!-- web-bild ../assets/screenshots/portal/benutzer.png -->

Oben steht die **Benutzerliste**, darunter das Formular **Benutzer
einladen**. Bearbeiter und Betrachter sehen die Liste nur; verwalten können
sie die Administratoren.

## Bedienelemente im Detail

### Benutzerliste

| Spalte | Bedeutung |
|---|---|
| **E-Mail** | Anmeldename des Benutzers. Ihr eigener Eintrag ist mit *Sie* markiert; Herzog-Mitarbeiter, die Ihrem Konto zur Betreuung zugeordnet sind, mit *Herzog-Zugang*. |
| **Name** | Anzeigename (optional). |
| **Rolle** | **Administrator**, **Bearbeiter** oder **Betrachter** — Administratoren ändern sie direkt in der Zeile mit **Ändern**. Was die Rollen bedeuten, steht unter [Kundenkonto und Einladung](../setup/account.md#benutzer-und-rollen). |
| **Letzte Anmeldung** | Zeitpunkt der letzten Anmeldung (Portal, Desktop oder Web) oder *noch nie*. |
| **Status** | **aktiv**, **deaktiviert**, **Einladung offen bis <Zeit>** oder **Einladung abgelaufen**. |

| Schaltfläche | Wirkung |
|---|---|
| **Ändern** (Rolle) | Speichert die in der Zeile gewählte Rolle. Die neue Rolle gilt in der Web-App sofort, in der Desktop-App nach dem nächsten Start bzw. nach **Vom Kundenkonto aktualisieren** in der [Benutzerverwaltung](../admin/users.md). |
| **Einladung erneuern** | Schickt einer Person mit abgelaufener Einladung einen neuen Link (wieder drei Tage gültig). |
| **Deaktivieren** | Der Benutzer kann sich nirgends mehr anmelden; seine Daten und Zuweisungen bleiben erhalten. Mit Sicherheitsabfrage. |
| **Aktivieren** | Hebt die Deaktivierung auf. |

!!! info "Eingebaute Schutzmechanismen"
    Ihren eigenen Zugang können Sie nicht deaktivieren, und der letzte
    aktive Administrator eines Kontos lässt sich weder deaktivieren noch
    herabstufen.

### Benutzer einladen

| Feld | Bedeutung |
|---|---|
| **E-Mail-Adresse** | Anmeldename der neuen Person; muss im Konto eindeutig sein. |
| **Name (optional)** | Anzeigename. |
| **Rolle** | Rolle des neuen Benutzers (Standard: Bearbeiter). |
| **Einladen** | Legt den Benutzer an und schickt die Einladung. |

So läuft die Einladung ab:

1. Die Person bekommt eine E-Mail mit einem Link und setzt ihr Passwort
   selbst (mindestens 10 Zeichen). Der Link gilt **drei Tage**.
2. Bis dahin steht der Benutzer in der Liste mit *Einladung offen bis …*.
3. Nach dem Setzen des Passworts ist der Zugang **aktiv** und gilt sofort
   für Portal, Desktop-App und Web-App.

!!! tip "Kein Mailversand möglich?"
    Konnte keine E-Mail verschickt werden (z. B. in einer Testumgebung),
    zeigt das Portal den Einladungslink direkt an — geben Sie ihn der
    Person auf einem anderen Weg weiter.

## Was die Rollen in den Programmen bewirken

| | Lizenzportal | Desktop-App | Web-App |
|---|---|---|---|
| **Administrator** | Verwaltet Benutzer, Rechner, Anfragen. | Globaler Administrator: alle Rechte in allen Profilen. | Alle Rechte; kann Rollen anlegen, Firma und Import verwalten. |
| **Bearbeiter** | Sieht das Konto. | Standardrolle *Bearbeiter*: Aufträge, Designs, Stammdaten anlegen und ändern. | dito. |
| **Betrachter** | Sieht das Konto. | Standardrolle *Betrachter*: lesen, berechnen, drucken, exportieren. | dito. |

In der Web-App können Administratoren zusätzlich **eigene Rollen** mit
einzelnen Rechten anlegen und Benutzern zuweisen — siehe
[Rollen (Web-App)](../web/roles.md) und
[Konto und Benutzer (Web-App)](../web/account.md). In der Desktop-App wird
je Profil (Arbeitsbereich) zugewiesen, siehe
[Benutzer verwalten](../admin/users.md).

## Verwandte Seiten

* [Kundenkonto und Einladung](../setup/account.md) — Einladung annehmen, Rollen
* [Benutzer und Rollen einrichten](../tasks/setup-users.md) — der Ablauf als Anleitung
* [Passwort und zweiter Faktor](security.md) — was jeder Benutzer selbst einstellt
* [Mein Konto](licenses.md) — Plätze und Rechner
