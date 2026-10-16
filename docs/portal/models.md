# Maschinenmodelle zuweisen

!!! abstract "Referenz — Die Seite „Maschinenmodelle" im Lizenzportal: Modell-Lizenzen für den Flechtsimulator einzelnen Benutzern zuweisen und neu verteilen"

## Wofür Sie diesen Bereich nutzen

Für den [Flechtsimulator](../braiding-simulator/index.md) lizenziert
Ihre Firma bei Herzog einzelne **Maschinenmodelle**. Jede Modell-Lizenz
gilt für **einen Benutzer**, im Programm und im Browser. Wer welches Modell
bekommt, legen die Administratoren Ihres Kontos auf dieser Seite fest.
Herzog weist nicht zu.

* Lizenziert wird der **Maschinentyp**, nicht die einzelne Maschine: Stehen
  vier baugleiche Maschinen in der Halle, braucht jeder Benutzer, der sie
  im Simulator bearbeiten soll, trotzdem nur eine Lizenz für dieses Modell.
* Ein Benutzer kann mehrere Modelle haben.
* Sie verteilen die Lizenzen jederzeit neu, ohne Wartezeit. Beim Öffnen
  eines Modells wird nichts belegt.
* Hat eine Maschine mehrere Modelle (umbaubare Maschinen), ist jedes Modell
  eine eigene Lizenz.

Den Flechtsimulator gibt es nur mit der **Herzog CAB Vollversion im Abo**,
siehe [Flechtsimulator: Lizenz und Rechte](../braiding-simulator/licence.md#voraussetzungen).
Weitere Modell-Lizenzen bestellen Sie beim Vertrieb von Herzog; im Portal
gibt es dafür keinen Bestellweg.

## Wer die Seite sieht

* Den Menüpunkt **Maschinenmodelle** (zwischen **Benutzer** und
  **Bestellen**) sehen nur **Administratoren** des Kontos (Recht
  *Firmendaten verwalten*), und nur, wenn das Konto mindestens eine
  Modell-Lizenz hat.
* Alle anderen Benutzer sehen die Modell-Lizenzen auf
  [Mein Konto](licenses.md) in der Karte **Maschinenmodelle**, ohne sie
  ändern zu können.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Seite „Maschinenmodelle" im Lizenzportal mit zwei Modellen, Zähler „1 von 2 zugewiesen“ und einem Haken je Benutzer, darunter Speichern.
    **So erzeugen:** Lizenzportal lokal (localhost:8100), Seite `/modelle` mit einem Konto, das zwei Modell-Lizenzen hat; noch nicht im Skript `_tools/web_screenshots.py` (Name `portal-modelle` ergänzen).
    **Ziel-Datei:** `assets/screenshots/portal/modelle.png`
    <!-- web-bild ../assets/screenshots/portal/modelle.png -->

Oben steht eine Karte mit der Überschrift **Maschinenmodelle** und zwei
Sätzen zu den Regeln:

* *Jede Modell-Lizenz gilt für einen Benutzer, im Programm und im Browser.
  Setzen Sie die Haken und speichern Sie. Neu verteilen geht jederzeit,
  ohne Wartezeit. Beim Öffnen eines Modells wird nichts belegt.*
* *Eine Änderung kommt im Programm nach etwa fünf Minuten an. Ohne
  Verbindung zum Lizenzserver zeigt Herzog CAB ein Modell noch bis zu
  7 Tagen.*

Hat das Konto Modell-Lizenzen, aber gerade keine Vollversion im Abo,
erscheint dazu gelb: *Der Flechtsimulator läuft nur mit der Vollversion
im Abo. Ihr Konto hat gerade keins.*

Darunter folgt die Tabelle mit allen Modellen und am Ende **Speichern**.

## Bedienelemente im Detail

### Tabelle der Modelle

| Spalte | Bedeutung |
|---|---|
| **Modell** | Name des Maschinenmodells, darunter *gültig bis &lt;Datum&gt;*. Dahinter steht gegebenenfalls ein Zustand: **ab später** (die Lizenz beginnt erst später), **abgelaufen** oder **wird nicht mehr ausgeliefert** (Herzog hat das Modell zurückgezogen). Eine aktive Lizenz hat kein Kennzeichen. |
| **Lizenzen** | *n von m zugewiesen*: wie viele Benutzer das Modell bekommen und wie viele Lizenzen Ihr Konto dafür hat. Beim Anklicken der Kästchen zählt die Seite sofort mit. Setzen Sie mehr Haken, als Lizenzen da sind, wird die Zahl rot. Geprüft wird beim **Speichern**. Darunter steht rot *n überzählig*, wenn mehr Zuweisungen bestehen als Lizenzen, siehe unten. |
| **Benutzer** | Ein Kästchen je **aktivem** Benutzer des Kontos, beschriftet mit dem Namen (ohne Namen mit der E-Mail-Adresse). Haken gesetzt = Benutzer bekommt das Modell. |

Beendete Lizenzen stehen nicht in der Tabelle.

### Speichern

**Speichern** übernimmt alle Haken aller Modelle auf einmal. Danach
erscheint eine der folgenden Meldungen:

| Meldung | Bedeutung |
|---|---|
| *Gespeichert. Herzog CAB übernimmt die Änderung beim nächsten Abgleich, nach etwa fünf Minuten.* | Die Zuweisung gilt. Die Web-App lädt die Liste der Maschinen alle fünf Minuten und beim Zurückkehren ins Browserfenster neu, das Programm bei seinem nächsten Abgleich mit dem Lizenzserver. |
| *Für &lt;Modell&gt; hat Ihr Konto &lt;n Lizenzen&gt;, gewählt sind &lt;m&gt;. Bitte Haken entfernen oder weitere Lizenzen bei Herzog anfragen. Nichts wurde gespeichert.* | Zu viele Haken. Es wird **nichts** gespeichert, auch nicht für die anderen Modelle. Entfernen Sie Haken und speichern Sie erneut. |
| *Für &lt;Modell&gt; ist ein Benutzer gewählt, der keine Lizenz bekommen kann, weil er deaktiviert ist oder nicht zu diesem Konto gehört. Nichts wurde gespeichert.* | Der Benutzer wurde inzwischen deaktiviert. Laden Sie die Seite neu. |
| *Es gab nichts zu ändern.* | Die Haken entsprachen schon dem gespeicherten Stand. |
| *&lt;Name&gt; arbeitet gerade offline. Dort verschwindet das Modell erst beim nächsten Abgleich, spätestens nach 7 Tagen.* | Sie haben einem Benutzer ein Modell weggenommen, der gerade mit *Offline arbeiten* im Programm ist. Gespeichert ist trotzdem. Das Programm erfährt die Änderung erst, wenn es wieder Verbindung hat; nach höchstens 7 Tagen ohne Verbindung öffnet es das Modell ohnehin nicht mehr. |

Wegnehmen geht immer. Dazugeben geht nur bis zur Zahl der Lizenzen.

### Überzählige Zuweisungen

Verkleinert Herzog die Zahl der Lizenzen eines Modells, bleiben Ihre Haken
stehen. Wirksam sind dann die **ältesten** Zuweisungen bis zur Zahl der
Lizenzen. Die jüngsten sind **überzählig**: Der Name steht rot, und der
Kurzhinweis sagt *Überzählig: mehr Zuweisungen als Lizenzen. Dieser
Benutzer bekommt das Modell nicht, bis ein Haken weg ist.* Entfernen Sie so
viele Haken, bis keine Zuweisung mehr überzählig ist.

### Fußzeile und Sonderfälle

* *Weitere Modell-Lizenzen bestellen Sie beim Vertrieb von Herzog.*
* Gibt es deaktivierte Benutzer: *Deaktivierte Benutzer verbrauchen keine
  Lizenz und stehen hier nicht.*
* Hat das Konto noch keine Modell-Lizenz: *Für dieses Konto ist noch kein
  Maschinenmodell freigeschaltet. Modell-Lizenzen bestellen Sie beim
  Vertrieb von Herzog.*
* Gibt es noch keinen aktiven Benutzer: *Es gibt noch keinen aktiven
  Benutzer, dem Sie ein Modell zuweisen können.* Mit einem Link zu
  [Benutzer](users.md).

## Was sonst noch die Zuweisung ändert

* **Deaktivieren** oder **Löschen** eines Benutzers unter
  [Benutzer](users.md) gibt seine Modell-Lizenzen frei. Hat der Benutzer
  Modelle, fragt das Portal *Diesen Zugang deaktivieren? Seine
  Modell-Lizenzen werden frei.* und bestätigt danach *Der Zugang ist
  deaktiviert. Seine Modell-Lizenzen sind frei und lassen sich anderen
  Benutzern zuweisen.*
* Wird ein deaktivierter Benutzer **wieder aktiviert**, bekommt er seine
  Modelle nicht automatisch zurück. Setzen Sie die Haken hier neu.
* Läuft eine Modell-Lizenz ab oder beendet Herzog sie, bleiben die Haken
  stehen. Verlängert Herzog die Lizenz, gelten sie wieder.
* Die App-Rolle eines Benutzers ändert die Zuweisung nicht. Damit er das
  Modell auch öffnen kann, braucht seine Rolle das Recht *Flechtsimulator
  anzeigen* (siehe [Lizenz und Rechte](../braiding-simulator/licence.md#rechte)).

## Mein Konto und Benutzer

* Auf [Mein Konto](licenses.md) steht unter den Bausteinen die Karte
  **Maschinenmodelle** mit den Spalten **Modell**, **Lizenzen** (*n von m
  zugewiesen*, gegebenenfalls *n überzählig*) und **Gültig** (*bis
  &lt;Datum&gt;*, gegebenenfalls *abgelaufen*) und dem Satz *Jede
  Modell-Lizenz gilt für einen Benutzer. Wem welches Modell zur Verfügung
  steht, legen die Administratoren des Kontos fest.* Administratoren
  springen mit **Zuweisen** auf diese Seite.
* Auf [Benutzer](users.md) zeigt die Spalte **Maschinenmodelle** je
  Benutzer die Modelle, die er wirksam bekommt, sonst *keine*. Für
  Administratoren ist die Spaltenüberschrift ein Link auf diese Seite.

Der Flechtsimulator selbst steht nicht in der Karte **Bausteine**. Im
Programm nennt ihn *Einstellungen > Lizenz* in der Zeile **Bausteine:**,
sobald Ihr Konto ihn nutzen darf.

## Verwandte Seiten

* [Flechtsimulator: Lizenz und Rechte](../braiding-simulator/licence.md) — was
  der Benutzer im Programm und in der Web-App sieht.
* [Flechtsimulator](../braiding-simulator/index.md) — Überblick.
* [Benutzer einladen und verwalten](users.md)
* [Mein Konto — Bausteine, Rechner, Plätze](licenses.md)
