# Erststart und Einrichtung

!!! example "Anleitung — Speicherort, Benutzer und Arbeitsverzeichnis beim ersten Programmstart eingerichtet"

**Voraussetzungen:** Herzog CAB ist [installiert](installer.md) und der
Rechner ist [am Kundenkonto angemeldet](activate-license.md) — bzw. bei
Bestandskunden: der Dongle steckt oder die CmAct-Lizenz ist aktiviert.

Wenn Sie Herzog CAB zum ersten Mal auf einem Rechner starten, führt Sie das
Programm durch eine kurze Einrichtung. Je nachdem, ob Sie der **erste**
Anwender in Ihrem Werk sind oder einem bereits bestehenden Setup beitreten
(z. B. weil die Benutzerverwaltung schon auf einem Netzlaufwerk liegt),
sehen Sie unterschiedlich viele der folgenden Dialoge.

=== "Kundenkonto"

    ```mermaid
    flowchart LR
      A[Anmeldung am<br>Kundenkonto] --> B[Arbeitsverzeichnis<br>der Firma]
      B --> D[Herzog CAB startet]
    ```

    Der Benutzer, mit dem Sie den Rechner am Konto angemeldet haben, ist
    zugleich Ihr Programmbenutzer — ein Administrator-Konto legen Sie
    **nicht** mehr an. Statt der Schritte 1 bis 3 unten erscheint nur ein
    Dialog: [Arbeitsverzeichnis der Firma](#kundenkonto-arbeitsverzeichnis-der-firma).
    Kennt Ihr Kundenkonto den Ordner Ihrer Firma schon, klicken Sie dort nur
    auf **Verbinden**.

=== "Dongle / CmAct-Lizenz"

    ```mermaid
    flowchart LR
      A[Speicherort wählen] --> B[Administrator anlegen]
      B --> C[Profil einrichten]
      C --> D[Herzog CAB startet]
    ```

    Ohne Kundenkonto verwaltet Herzog CAB seine Benutzer lokal. Beim ersten
    Start legen Sie den ersten Administrator an (Schritt 2).

!!! info "Diese Dialoge erscheinen nur bei Bedarf"
    Jeder Dialog wird **nur dann** angezeigt, wenn der jeweilige Zustand
    noch nicht existiert. Auf einem zweiten oder dritten Rechner, der auf
    dieselbe (bereits eingerichtete) Benutzerverwaltung zugreift, sehen Sie
    meist nur noch den normalen [Anmeldedialog](../admin/login.md) und ggf.
    die [Profil-Auswahl](#profil-auswahlen-statt-einrichten).

## Kundenkonto: Arbeitsverzeichnis der Firma

Im Kontomodell fragt Herzog CAB nach der Anmeldung nur noch, wo die Daten
der Firma liegen — Designs, Aufträge, Maschinen und Stammdaten. Den
Speicherort merkt sich Ihr [Kundenkonto](account.md): Der erste Rechner der
Firma legt ihn fest, jeder weitere Rechner verbindet sich damit. Niemand
muss dafür den Netzwerkpfad kennen.

### Das Konto kennt den Ordner: verbinden

Hat Ihre Firma schon einen Speicherort, zeigt der Dialog
**„Arbeitsverzeichnis einrichten"** diesen Ordner und prüft sofort, ob er
von diesem Rechner aus erreichbar ist.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Dialog „Arbeitsverzeichnis einrichten" mit dem Ordner der Firma, grünem Haken „erreichbar" und der Schaltfläche **Verbinden**
    **So erzeugen:** Auf einem zweiten Rechner mit einem Konto, das schon einen Speicherort hat, zum ersten Mal anmelden
    **Ziel-Datei:** `assets/screenshots/setup/arbeitsverzeichnis-verbinden.png`

| Element | Bedeutung |
|---|---|
| Ordner der Firma | Der Netzwerkpfad aus dem Kundenkonto, z. B. `\\fileserver\freigabe\HerzogCAB`. |
| Prüfergebnis | ✔ = der Ordner ist erreichbar. ✘ = nicht erreichbar; dann ist meist das Netzlaufwerk nicht verbunden (im Homeoffice: VPN) oder Ihr Windows-Benutzer darf dort nicht schreiben. |
| **Verbinden** | Richtet den Ordner auf diesem Rechner ein und startet Herzog CAB. Nur aktiv, wenn der Ordner erreichbar ist. |
| **Erneut prüfen** | Erscheint, wenn der Ordner nicht erreichbar ist. Prüft nach dem Verbinden des Netzlaufwerks noch einmal. |
| **Anderen Ordner wählen …** | Nur für Benutzer mit dem Recht **Workspace-Einstellungen**. Öffnet die Auswahl unten, z. B. für einen Test-Ordner. |
| **Beenden** | Beendet Herzog CAB, ohne etwas einzurichten. |

!!! info "Kein stilles Ausweichen"
    Ist der Ordner nicht erreichbar, legt Herzog CAB **keinen** lokalen
    Ersatzordner an. So entstehen keine zwei getrennten Datenbestände.

### Erster Rechner der Firma: Speicherort festlegen

Kennt das Konto noch keinen Speicherort, fragt der Dialog einmal:

| Element | Bedeutung |
|---|---|
| **Nur auf diesem Rechner** | Für einen einzelnen Arbeitsplatz. Vorbelegt mit *Dokumente\HerzogCAB*, über **Durchsuchen …** änderbar. Kommt später ein zweiter Rechner dazu, verschieben Sie den Ordner unter [Speicherort](../admin/storage-location.md#auf-netzlaufwerk-verschieben) auf ein Netzlaufwerk. |
| **Auf einem Netzlaufwerk, für mehrere Rechner** | Für mehrere Arbeitsplätze. Pfad eintragen oder über **Auswählen …** wählen. Ein verbundenes Laufwerk wie `Z:\HerzogCAB` wandelt Herzog CAB selbst in den Netzwerkpfad um, damit jeder Rechner ihn findet. |
| **Übernehmen** | Richtet den Ordner ein. Mit dem Recht **Workspace-Einstellungen** wird ein Netzlaufwerk zugleich als Speicherort der Firma im Kundenkonto hinterlegt. |

!!! tip "Speicherort vorab festlegen"
    Administratoren können den Speicherort auch in der Web-App unter
    [Konto und Benutzer](../web/account.md#speicherort-der-firma)
    eintragen, bevor der erste Rechner eingerichtet wird.

## Schritt 1: Speicherort für die Benutzerverwaltung wählen (nur Dongle / CmAct)

!!! info "Entfällt beim Kundenkonto"
    Im Kontomodell kommen die Benutzer aus dem Kundenkonto. Den Ordner der
    Daten legt der Dialog [Arbeitsverzeichnis der Firma](#kundenkonto-arbeitsverzeichnis-der-firma) fest.

Dieser Dialog **„Daten-Speicherort einrichten"** erscheint nur beim
allerersten Start auf einem Rechner, der noch keine Benutzerverwaltung
kennt (weder lokal noch über einen bereits konfigurierten Netzwerk-Pfad).
Er legt fest, wo Benutzerkonten, Profile und Rollen gespeichert werden.

| Element | Bedeutung |
|---|---|
| **Lokal — nur dieser Rechner** | Vorbelegte Option. Benutzerverwaltung liegt unter `%ProgramData%\Herzog GmbH\Herzog Cab` auf diesem Rechner. Passend für Variante 1 der [Einsatz-Szenarien](topology.md). |
| **Netzwerk-Pfad — geteilt mit anderen Rechnern** | Aktiviert das Pfad-Feld. Passend für Variante 2/3, wenn mehrere Rechner dieselben Benutzerkonten sehen sollen. |
| Pfad-Feld | Freitextfeld für den UNC-Pfad (z. B. `\\fileserver\share\HerzogCAB`), nur bei „Netzwerk-Pfad" aktiv. |
| **Auswählen …** | Öffnet die Ordnerauswahl. |
| **Verbindung testen** | Prüft, ob der Pfad existiert bzw. angelegt werden kann und beschreibbar ist. Zeigt zusätzlich an, ob dort bereits Benutzerdaten liegen. |
| **Übernehmen** | Speichert die Wahl. Bei „Netzwerk-Pfad" startet Herzog CAB danach automatisch neu, damit der neue Pfad überall greift. |

!!! tip "Bereits Daten am Zielort vorhanden?"
    Findet der Verbindungstest an einem Netzwerk-Pfad bereits Benutzerdaten
    (z. B. weil ein Kollege dort schon einen Administrator angelegt hat),
    werden diese weiterverwendet — es wird **kein** neuer Administrator
    angelegt. Sie springen dann direkt zum normalen Anmeldedialog.

Der gewählte Speicherort lässt sich später jederzeit unter
[Speicherort](../admin/storage-location.md) in der Systemverwaltung ändern.

## Schritt 2: Administrator-Konto anlegen (nur Dongle / CmAct)

!!! info "Entfällt beim Kundenkonto"
    Im Kontomodell kommen Benutzer, Passwörter und Rollen aus dem
    [Kundenkonto](account.md). Wer den Rechner angemeldet hat, ist sofort im
    Programm angemeldet; Kollegen melden sich beim nächsten Start mit ihrem
    eigenen Kontobenutzer an (siehe [Anmelden und Abmelden](../admin/login.md)).
    Ihre Rolle im Programm entspricht der Rolle im Konto — ein
    Konto-Administrator hat alle Rechte.

Existiert in der lokalen Benutzerverwaltung noch **kein** Konto, zeigt
Herzog CAB den Dialog **„Benutzerverwaltung einrichten"**. Das hier angelegte Konto
wird automatisch zum ersten **SuperAdmin** und ist danach sofort
angemeldet — eine erneute Anmeldung ist nicht nötig.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Dialog „Benutzerverwaltung einrichten" mit den Feldern
    Firma, Login-Name, Anzeigename, E-Mail, Passwort, Passwort bestätigen.
    **So erzeugen:** Herzog CAB auf einem Rechner ohne bestehende
    Benutzerverwaltung starten (leerer `%ProgramData%\Herzog GmbH\Herzog Cab`).
    **Ziel-Datei:** `assets/screenshots/setup/erstadmin-einrichten.png`

| Feld | Bedeutung |
|---|---|
| **Firma** | Firmenname, der im Programm angezeigt wird. Lässt sich später unter *Systemverwaltung > Firma* ändern. |
| **Login-Name** | Anmeldename für den Login-Dialog. Groß-/Kleinschreibung wird nicht unterschieden. |
| **Anzeigename** | Voll ausgeschriebener Name, der im Programm angezeigt wird. |
| **E-Mail** (optional) | Wird im Benutzerkonto hinterlegt. |
| **Passwort** / **Passwort bestätigen** | Muss mindestens **6 Zeichen** lang sein und in beiden Feldern übereinstimmen. |

Klicken Sie auf **Einrichtung abschließen**, sobald alle Pflichtfelder
ausgefüllt sind — der Button ist bis dahin gesperrt.

!!! tip "Wer sollte der erste Administrator sein?"
    Idealerweise eine Person, die organisatorisch für Herzog CAB im Werk
    verantwortlich ist — z. B. ein Schichtführer oder Werkstattleiter.
    Weitere Benutzer mit eingeschränkten Rechten legen Sie später unter
    [Benutzer verwalten](../admin/users.md) an.

!!! warning "Passwort sicher aufbewahren"
    Wenn Sie das Administrator-Passwort vergessen, kann nur ein weiterer
    SuperAdmin es über [Benutzer verwalten](../admin/users.md)
    zurücksetzen. Gibt es noch keinen zweiten SuperAdmin, notieren Sie das
    Passwort an einem sicheren Ort.

## Schritt 3: Profil einrichten (nur Dongle / CmAct)

!!! info "Entfällt beim Kundenkonto"
    Das Profil legt dort der Dialog [Arbeitsverzeichnis der Firma](#kundenkonto-arbeitsverzeichnis-der-firma)
    selbst an; es heißt wie Ihre Firma.

Ein **Profil** ist ein eigenständiger Arbeitsbereich mit eigenem
Arbeitsverzeichnis (Aufträge, Stammdaten, Druckvorlagen) und eigenem
Webserver-Port. Sieht der neu angemeldete SuperAdmin **kein** Profil, zeigt
Herzog CAB automatisch den Dialog **„Profil einrichten"**.

| Feld | Bedeutung |
|---|---|
| **Profilname** | Bezeichnung des Profils, vorbelegt mit „Standard". Bei mehreren Firmen/Werken auf derselben Installation vergeben Sie hier einen sprechenden Namen. |
| **Arbeitsverzeichnis** | Ordner für Aufträge, Maschinen, Materialien, Farben und Druckvorlagen dieses Profils. Vorbelegt mit *Dokumente\HerzogCAB*. Über **Durchsuchen …** wählbar. |
| **Webserver-Port** | Port, unter dem die mobile Weboberfläche dieses Profils erreichbar ist. Vorbelegt mit 8080. |
| **Webserver beim Start automatisch starten** | Checkbox, standardmäßig aktiviert. |
| **Webserver-Passwort** (optional) | Schützt den Zugriff auf die Weboberfläche. |

!!! warning "Arbeitsverzeichnis bei Mehrplatz-Betrieb"
    Profile werden zentral gespeichert. Wenn mehrere Rechner mit demselben
    Profil arbeiten sollen, muss das Arbeitsverzeichnis ein
    **Netzwerk-Pfad** sein (z. B. `\\fileserver\share\HerzogCAB-Daten`).
    Ein lokaler Pfad wie `C:\Daten\…` ist nur auf dem Rechner erreichbar,
    auf dem Sie ihn hier eingegeben haben.

Klicken Sie auf **Profil anlegen**, sobald Name und Arbeitsverzeichnis
gültig sind (grüner Haken unter dem Formular).

### Profil auswählen statt einrichten

Sieht der angemeldete Benutzer **mehr als ein** Profil (z. B. weil bereits
mehrere Werke/Profile angelegt wurden), erscheint stattdessen der Dialog
**„Profil auswählen"**: eine Liste aller zugewiesenen Profile mit
Arbeitsverzeichnis und Webserver-Status zur ausgewählten Zeile, den
Schaltflächen **Profile verwalten …** (nur für SuperAdmins) und
**Profil öffnen**. Ist genau ein Profil zugewiesen, öffnet Herzog CAB es
automatisch — ohne Dialog.

Weitere Profile anlegen, umbenennen oder löschen erledigen Sie später unter
[Profile (Arbeitsbereiche)](../admin/profiles.md).

## Ergebnis

Herzog CAB öffnet das Hauptfenster, angemeldet mit Ihrem Benutzer und dem
eingerichteten Profil. Im Arbeitsverzeichnis
legt das Programm die nötigen Grunddateien automatisch an (u. a. für
Aufträge, Flechtmaschinen, Materialien und Farben) — Details dazu finden
Sie unter [Profile (Arbeitsbereiche)](../admin/profiles.md).

## Wenn nachträglich kein Arbeitsverzeichnis mehr erreichbar ist

Ist das im Profil hinterlegte Arbeitsverzeichnis bei einem **späteren**
Programmstart nicht mehr erreichbar oder nicht beschreibbar (z. B.
Netzlaufwerk nicht verbunden), meldet Herzog CAB das direkt beim Start mit
einer Fehlermeldung samt Lösungshinweis. In einem älteren Sonderfall — ganz
frühe Installationen ohne Profil-Zuordnung — kann stattdessen automatisch
der Dialog **„Arbeitsverzeichnis einrichten"** erscheinen: Pfad-Feld,
**Durchsuchen …**, ein Status-Hinweis (grüner Haken bei Schreibzugriff,
rotes Kreuz sonst) und **Arbeitsverzeichnis übernehmen**. Brechen Sie
diesen Dialog ab, weicht Herzog CAB automatisch auf *Dokumente\HerzogCAB*
aus, damit das Programm in jedem Fall startfähig bleibt.

## Wenn etwas nicht klappt

* Passwort wird nicht akzeptiert oder die beiden Passwort-Felder stimmen
  nicht überein → Meldung im Dialog beachten, mindestens 6 Zeichen
  verwenden.
* Ordner ist nicht beschreibbar (rotes Kreuz) → einen anderen Ordner
  wählen oder Berechtigungen prüfen; keinen Ordner unter
  `C:\Programme` oder auf einem schreibgeschützten Netzlaufwerk wählen.
* Anmeldung schlägt bei einem weiteren Rechner fehl → siehe
  [Login-Probleme](../help/login-problems.md).
* Lizenz wird nicht erkannt → siehe [Lizenzprobleme](../help/license-problems.md).

## Verwandte Seiten

* [Einsatz-Szenarien](topology.md) — welche Topologie zu Ihrem Werk passt
* [Speicherort](../admin/storage-location.md) — Speicherort nachträglich ändern
* [Profile (Arbeitsbereiche)](../admin/profiles.md) — weitere Profile anlegen und verwalten
* [Benutzer verwalten](../admin/users.md) — weitere Benutzer anlegen bzw. aus dem Kundenkonto übernehmen
* [Kundenkonto und Einladung](account.md) — Kollegen ins Konto einladen
* [Oberfläche im Überblick](../basics/interface.md) — wie es nach dem Start weitergeht
