# Konto und Benutzer (Web-App)

!!! abstract "Referenz — Die Seite „Konto und Benutzer" im Benutzermenü der Web-App: Edition, Bausteine, Plätze, Speicherort der Firma, Benutzer und ihre Rollen"

## Wofür Sie diesen Bereich nutzen

Hier sehen Sie, was Ihr Konto in der Web-App freigeschaltet hat und wer
gerade damit arbeitet — und Administratoren weisen den Benutzern ihre
**Rollen für die Web-App** zu. Neue Benutzer einladen, Passwörter und
Rechner verwaltet weiterhin das [Lizenzportal](../portal/index.md); die
Seite verlinkt dorthin.

Sie öffnen die Seite über *Benutzermenü > Konto und Benutzer* oder die
Kachel **Konto und Benutzer** auf der Startseite.

## Der Bildschirm im Überblick

![Konto und Benutzer in der Web-App: Edition, Plätze, Bausteine und die Benutzerliste mit Rollen-Kästchen.](../assets/screenshots/web/konto-benutzer.png)

| Element | Bedeutung |
|---|---|
| **Rollen verwalten** | Rechts neben dem Seitentitel, nur mit dem Recht *Rollen verwalten*: wechselt zu [Rollen](roles.md). |
| **Lizenzportal öffnen** | Öffnet [license.herzog-cab.com](https://license.herzog-cab.com) in einem neuen Tab. |
| **Edition** | Mit welchem Abo Sie arbeiten: *Vollversion*, *Designer* oder *Testversion*. Bei internen Konten der Vermerk *internes Konto*. |
| **Plätze** | Belegte und vorhandene Plätze, zum Beispiel *2 / 3*. Programm und Web-App zählen zusammen. |
| **Bausteine** | Die Bausteine, die die Web-App öffnen, mit der Zahl der Plätze und der Laufzeit (*bis &lt;Datum&gt;* oder *Lebenszeit*). *Programm und Web* heißt: ein Kontingent für Desktop-App und Web-App zusammen. |

### Speicherort der Firma

Der Ordner auf Ihrem Fileserver, in dem die Firma mit der Desktop-App
arbeitet, z. B. `\\fileserver\freigabe\HerzogCAB`. Ein neuer Rechner
verbindet sich beim ersten Start damit, ohne dass jemand den Pfad kennen
muss (siehe [Erststart](../setup/first-run.md#kundenkonto-arbeitsverzeichnis-der-firma)).
Meist trägt die Desktop-App den Ordner selbst ein, sobald ein Administrator
dort arbeitet.

| Element | Bedeutung |
|---|---|
| Pfad und *festgelegt …* | Der hinterlegte Ordner und wann er zuletzt festgelegt wurde. Ohne Eintrag steht hier *Noch kein Speicherort hinterlegt*. |
| **Festlegen** / **Ändern** | Öffnet das Feld **Netzwerkpfad**. Nur Netzwerkpfade wie `\\server\freigabe\ordner` sind erlaubt, keine Laufwerksbuchstaben. **Speichern** übernimmt, **Abbrechen** verwirft. |
| **Entfernen** | Löscht den Eintrag. Neue Rechner fragen dann wieder nach dem Ordner. |

Festlegen, Ändern und Entfernen dürfen nur Benutzer mit dem Recht
**Workspace-Einstellungen** (z. B. Administratoren); alle anderen sehen den
Ordner nur.

### Benutzer und Rollen

Die Tabelle listet alle Benutzer des Kontos mit **Name**, **E-Mail**,
**Letzte Anmeldung**, dem Kennzeichen **Gerade angemeldet** bzw. *inaktiv*
und je Rolle ein **Kästchen**.

* **Rolle zuweisen:** Benutzer mit dem Recht *Benutzer verwalten* haken die
  Kästchen an oder ab; die Änderung gilt sofort. Ein Benutzer kann mehrere
  Rollen haben — die Rechte addieren sich.
* **Ohne Rolle** arbeitet ein Benutzer als **Bearbeiter**.
* Die Rolle **Administrator** hat immer alle Rechte.

Damit sich niemand mehr Rechte verschafft, als er hat, gelten drei Regeln.
Verstößt eine Änderung dagegen, lehnt die Web-App sie mit einer roten
Meldung ab.

* Ihre **eigenen** Rollen ändert ein anderer Administrator. In Ihrer
  eigenen Zeile sind die Kästchen gesperrt.
* Eine Rolle vergeben oder entziehen Sie nur, wenn Sie selbst **alle ihre
  Rechte** haben. Wer mehr Rechte hat als Sie, lässt sich auch nicht
  herabstufen.
* Das Konto behält immer mindestens **einen Administrator** (*Das Konto
  braucht mindestens einen Administrator.*).

Dieselben Regeln gelten im [Lizenzportal](../portal/users.md).

### Gerade angemeldet

Die Karte unten auf der Seite listet, wer gerade einen Platz belegt und wo:
Rechnername, *Web* oder *(offline)*, dazu der Zeitpunkt der letzten
Aktivität. Die Zahl im Kartentitel nennt die belegten Plätze. Die Liste
lädt jede Minute neu.

!!! info "Zwei Orte, ein Benutzer"
    Die Konto-Rolle (Administrator / Bearbeiter / Betrachter) vergibt das
    [Lizenzportal](../portal/users.md); sie gilt in Desktop-App und Web-App.
    Die Kästchen hier ergänzen sie um **Web-App-Rollen** mit einzelnen
    Rechten — nützlich, wenn z. B. der Vertrieb nur Designs und Aufträge
    sehen soll.

## Verwandte Seiten

* [Rollen (Web-App)](roles.md) — eigene Rollen mit einzelnen Rechten
* [Benutzer einladen und verwalten (Lizenzportal)](../portal/users.md)
* [Abo und Bestellung](subscription.md): Jahresabo bestellen und verlängern
* [Kundenkonto und Einladung](../setup/account.md)
