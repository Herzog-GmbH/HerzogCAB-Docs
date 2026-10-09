# Webserver und QR-Code

!!! abstract "Referenz — Tab „Webserver" des Einstellungen-Dialogs: den eingebauten Webserver starten, mit einem Passwort fürs Netz freigeben, IP-Adresse wählen und den QR-Code für den mobilen Zugriff nutzen."

## Wofür Sie diesen Bereich nutzen

Der eingebaute **Webserver** stellt Auftrags- und Maschinendaten im Browser
bereit — z. B. am Smartphone oder Tablet direkt an der Maschine. Der Zugang
erfolgt bequem über einen **QR-Code**, den Sie hier anzeigen und auch auf
[Auftragspapiere drucken](../../orders/print.md) können.

!!! warning "Im Netz nur mit Passwort"
    Ohne Passwort ist die Weboberfläche **nur auf diesem Rechner**
    erreichbar (Adresse `http://localhost:<Port>`), nicht von Tablets oder
    Handys in der Halle. Erst wenn Sie unter **Zugangsschutz** ein Passwort
    vergeben, ist sie im Firmennetz erreichbar — und dann nur nach Eingabe
    dieses Passworts. Bis Version 2.1.0 war das Passwort freiwillig und der
    Webserver auch ohne Passwort im Netz offen.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Einstellungen, Tab „Webserver“ bei laufendem Server mit Passwort: oben „Netzwerk“ (Webserver aktivieren, Port), darunter „Zugangsschutz“ (Passwortfeld mit Platzhalter „Gesetzt – zum Ändern neu eingeben“, Schaltfläche „Passwort entfernen“, Hinweis „Die Weboberfläche ist im Netz erreichbar, nur mit diesem Passwort.“), unten „Live-Status“ mit grünem Punkt, IP-Adressen, QR-Adresse und QR-Code; Speichern/Abbrechen rechts unten.
    **So erzeugen:** *Datei > Einstellungen*, Tab **Webserver**; Webserver aktivieren, Testpasswort vergeben, **Speichern**, Dialog erneut öffnen. Interne IP-Adressen dürfen sichtbar sein.
    **Ziel-Datei:** `assets/screenshots/settings/webserver.png` (ersetzt das bisherige Bild)

!!! warning "Berechtigung erforderlich"
    Das Ändern der Webserver-Einstellungen erfordert das Recht
    **Workspace-Einstellungen**. Ohne dieses Recht sind alle Felder gesperrt.

## Bedienelemente im Detail

Der Tab ist von oben nach unten so aufgebaut, wie Sie ihn einrichten:
erst einschalten, dann absichern, dann den Status prüfen.

### Karte „Netzwerk“

| Element | Bedeutung |
|---|---|
| **Webserver aktivieren** | Startet bzw. stoppt den Server. |
| **Port** | Port des Servers (Standard 8080). Schlägt der Start fehl (Port belegt), meldet Herzog CAB dies. |

### Karte „Zugangsschutz“

| Element | Bedeutung |
|---|---|
| **Passwort** | Passwort für die Weboberfläche, **mindestens 8 Zeichen**. Das Feld bleibt immer leer — der Platzhalter zeigt, ob schon ein Passwort gesetzt ist (*Gesetzt – zum Ändern neu eingeben*) oder nicht (*Mindestens 8 Zeichen*). Ein neues Passwort gilt erst mit **Speichern** des Dialogs; ist es zu kurz, meldet Herzog CAB *„Das Webserver-Passwort muss mindestens 8 Zeichen lang sein.“* |
| **Passwort entfernen** | Nur sichtbar, wenn ein Passwort gesetzt ist. Nach der Rückfrage *„Webserver-Passwort entfernen? …“* wirkt es **sofort**, ohne **Speichern**: Die Weboberfläche ist danach nur noch auf diesem Rechner erreichbar. |
| Hinweis unter dem Feld | Mit Passwort: *„Die Weboberfläche ist im Netz erreichbar, nur mit diesem Passwort.“* Ohne Passwort: *„Ohne Passwort ist die Weboberfläche nur auf diesem Rechner erreichbar. Für Tablets und Handys in der Halle ein Passwort vergeben.“* |

Setzen, ändern oder entfernen Sie das Passwort, startet der Webserver von
selbst mit der neuen Einstellung neu; alle angemeldeten Browser müssen sich
danach neu anmelden. Herzog CAB speichert das Passwort nicht im Klartext.

### Karte „Live-Status“

| Element | Bedeutung |
|---|---|
| **Status** | Grüner bzw. roter Punkt mit *Server läuft auf Port …*, *Server läuft auf Port …, nur auf diesem Rechner* (ohne Passwort) oder *Server ist nicht aktiv*. |
| **IP-Adressen** | Nur bei laufendem Server: Liste der erreichbaren Adressen (je Netzwerkadapter), z. B. `http://192.168.178.38:8080`. Ohne Passwort steht hier nur `http://localhost:<Port>`. |
| **QR-Adresse** | Nur bei laufendem Server **mit Passwort**: Auswahl der IP-Adresse, die im QR-Code verschlüsselt wird (manche Rechner haben mehrere Adressen). |
| **QR-Code** | Nur bei laufendem Server **mit Passwort**. Smartphone-Kamera darauf richten — der Browser öffnet die Anmeldeseite der mobilen Ansicht. |

## Anmelden im Browser

Ist ein Passwort gesetzt, zeigt der Browser zuerst die Anmeldeseite
**Herzog CAB** mit dem Text *„Bitte Passwort eingeben, um auf die
Weboberfläche zuzugreifen.“*, dem Feld **Passwort** und der Schaltfläche
**Anmelden**.

* Eine Anmeldung gilt **12 Stunden**; danach (oder nach einem
  Passwortwechsel) erscheint die Anmeldeseite erneut.
* Bei falschem Passwort steht dort *„Falsches Passwort. Bitte erneut
  versuchen.“* Nach fünf Fehlversuchen sperrt der Webserver die Anmeldung
  für eine Minute, bei weiteren Fehlversuchen jeweils doppelt so lange,
  höchstens 15 Minuten (*„Zu viele Fehlversuche. Bitte in … Minute(n)
  erneut versuchen.“*).
* Ohne Passwort gibt es keine Anmeldeseite; die Weboberfläche öffnet sich
  dann nur im Browser auf demselben Rechner.

## Meldungen beim Programmstart

Startet der Webserver automatisch mit dem Profil, meldet die Statuszeile:

| Meldung | Bedeutung |
|---|---|
| *Webserver aktiv auf Port …* | Der Server läuft mit Passwort und ist im Netz erreichbar. |
| *Webserver aktiv auf Port …, nur auf diesem Rechner. Für Zugriff aus dem Netz in den Einstellungen ein Passwort vergeben.* | Kein Passwort gesetzt — Tablets und Handys kommen nicht hinein. |
| *Webserver läuft bereits in einer anderen Instanz dieses Arbeitsverzeichnisses.* | Ein zweites Programmfenster mit demselben Arbeitsverzeichnis stellt den Server schon bereit. |
| *Webserver-Start fehlgeschlagen: …* | Meist ist der Port belegt — anderen Port wählen. |

!!! info "Einstellungen gelten pro Profil"
    Port, Autostart (*Webserver beim Start automatisch starten*) und Passwort
    werden **pro Profil** gespeichert und lassen sich auch in der
    [Profilverwaltung](../profiles.md) pflegen. Neue Profile haben den
    Webserver ausgeschaltet. Entfernen lässt sich ein Passwort nur hier im
    Tab **Webserver**.

!!! warning "Nach dem Update: Passwort vergeben"
    War der Webserver bisher **ohne** Passwort im Netz erreichbar, ist er
    nach dem Update nur noch auf dem Rechner selbst erreichbar. Damit
    Tablets und Handys wieder zugreifen, vergeben Sie hier ein Passwort mit
    mindestens 8 Zeichen.

!!! warning "Gemeinsame Profile mit älteren Programmversionen"
    Liegen die Profile auf einem gemeinsamen Speicherort und arbeiten dort
    noch Rechner mit Version 2.1.0 oder älter, gilt: Sobald ein Passwort
    gesetzt ist, ist die Weboberfläche dieser älteren Rechner gesperrt (sie
    verlangen ein Passwort, das niemand kennt). Speichert eine ältere
    Version das Profil, muss das Passwort danach hier neu vergeben werden.
    Aktualisieren Sie deshalb alle Rechner — siehe auch
    [Mehrere Benutzer am selben Arbeitsverzeichnis](../../basics/multi-user.md).

!!! tip "Richtige IP wählen"
    Hat der Rechner mehrere Netzwerkadapter, prüfen Sie, dass die im QR-Code
    verwendete IP auch vom Smartphone erreichbar ist (gleiches WLAN/Netz).

## Verwandte Seiten

* [Aufträge](../../orders/index.md) — welche Daten mobil bereitstehen
* [Auftragspapiere drucken](../../orders/print.md) — QR-Code auf dem Maschinenblatt
* [Profile (Arbeitsbereiche)](../profiles.md) — Port, Autostart und Passwort pro Profil
