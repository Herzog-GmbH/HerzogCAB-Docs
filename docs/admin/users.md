# Benutzer verwalten

Die Benutzerverwaltung öffnen Sie über **Systemverwaltung → Benutzer**. Links
steht die Benutzerliste, rechts der Editor des gewählten Benutzers.

![Benutzerverwaltung: Liste links, Benutzer-Editor rechts.](../assets/screenshots/users/benutzer.png)

## Eigenschaften eines Benutzers

| Feld | Beschreibung |
|---|---|
| **Login** | Anmeldename (z. B. `admin`). |
| **Anzeigename** | Klartext-Name des Benutzers. |
| **E-Mail** | Optionale E-Mail-Adresse. |
| **Passwort** | Über **Passwort zurücksetzen…** neu setzen (siehe [Passwort zurücksetzen](password-reset.md)). |
| **Aktiv** | Konto aktiv/deaktiviert. |

Darunter zeigt der Editor *angelegt* und *letzter Login*.

## Profile und Rollen

Im Abschnitt **Profile und Rollen** weisen Sie dem Benutzer **pro Profil**
(Arbeitsbereich) eine oder mehrere [Rollen](roles.md) zu – in der Tabelle
*Profil · Zugewiesen · Rollen*. So kann derselbe Benutzer in verschiedenen
Profilen unterschiedliche Rechte haben.

!!! info "Globaler Administrator (SuperAdmin)"
    Ein als globaler Administrator gekennzeichneter Benutzer hat in **allen**
    Profilen vollen Zugriff – unabhängig von den Zuweisungen in der Tabelle.

## Benutzer anlegen, deaktivieren, speichern

* **Neuer Benutzer** (unten links) legt einen Benutzer an.
* **Speichern** sichert die Änderungen.
* **Deaktivieren** schaltet das Konto inaktiv, ohne es zu löschen.

!!! warning "Berechtigung erforderlich"
    Benutzer verwalten dürfen nur Bediener mit dem Recht **Benutzer verwalten**
    (Rolle *Administrator*).
