# Lizenz und Rechte

!!! abstract "Referenz — Wer den Flechtsimulator bekommt: Vollversion im Abo, Modell-Lizenzen je Benutzer, Rechte, Offline-Grenze und was passiert, wenn eine Lizenz wegfällt"

## Wofür Sie diese Seite brauchen

Der Flechtsimulator ist ein Zusatz zur Herzog CAB Vollversion. Herzog
liefert für jede Flechtmaschine, die Sie bei uns kaufen können, ein
fertiges **Maschinenmodell**. Ihre Firma lizenziert die Modelle, die sie
braucht, und weist sie einzelnen Benutzern zu. Diese Seite erklärt, was
dafür nötig ist und wie sich Programm und Web-App verhalten, wenn eine
Lizenz fehlt, abläuft oder neu verteilt wird.

## Voraussetzungen

Den Eintrag **Flechtsimulator** in der Navigation sehen Sie, wenn alles
Folgende zutrifft:

| Voraussetzung | Erklärung |
|---|---|
| **Herzog CAB Vollversion im Abo** | Der Flechtsimulator läuft nur mit der Vollversion im Jahresabo (siehe [Bausteine](../setup/account.md#bausteine)). Eine Vollversion ohne Enddatum, eine Dongle-Lizenz, der Designer und die Testversion schalten ihn nicht frei. |
| **Mindestens eine gültige Modell-Lizenz** | Herzog schaltet die Modelle Ihrem Konto frei; Sie bestellen sie beim Vertrieb. |
| **Anmeldung mit dem Kundenkonto** | Die Modelle kommen vom Lizenzserver. Im Programm müssen Sie mit Ihrem Herzog-Konto angemeldet sein, siehe [Anmelden und Lizenz beziehen](../setup/activate-license.md). |
| **Recht *Flechtsimulator anzeigen*** | Ihre Rolle muss den Simulator anzeigen dürfen, siehe [Rechte](#rechte). |
| **Programmversion ab 2.1.1** | Die Modelle vom Lizenzserver und die Zuweisung je Benutzer gibt es im Programm ab Version 2.1.1. In der Web-App gelten sie schon. |

Fehlt eine Voraussetzung, gibt es den Eintrag nicht; er ist nicht
ausgegraut. Im Programm fehlen dann auch der Reiter **Flechtsimulator** in
den Einstellungen und die Verwendung **Flechtsimulator** im
[Druck-Editor](../print-templates/index.md).

Im Programm nennt *Einstellungen > Lizenz* in der Zeile **Bausteine:** den
**Flechtsimulator**, sobald Ihr Konto ihn nutzen darf. Im Lizenzportal
stehen die Modelle in einer eigenen Karte **Maschinenmodelle**, nicht bei
den Bausteinen.

## Modell-Lizenz je Benutzer

* **Eine Lizenz = ein Modell für einen Benutzer**, im Programm und im
  Browser. Ein Benutzer kann mehrere Modelle haben.
* Lizenziert wird der **Maschinentyp**: Für vier baugleiche Maschinen
  braucht jeder Benutzer eine Lizenz dieses Modells, nicht vier.
* **Beim Öffnen wird nichts belegt.** Der Simulator braucht keinen eigenen
  Platz; beim Programmstart zählt nur der Platz der Vollversion.
* Wer welches Modell bekommt, legen die Administratoren Ihres Kontos im
  Lizenzportal fest: [Maschinenmodelle zuweisen](../portal/models.md).
  Neu verteilen geht jederzeit, ohne Wartezeit.
* Deaktivierte Benutzer verbrauchen keine Lizenz.
* Hat eine umbaubare Maschine mehrere Modelle, ist jedes Modell eine eigene
  Lizenz.

Ihre eigenen Besetzungen und Programme gehören nicht zur Lizenz. Sie
bleiben erhalten, wenn eine Lizenz abläuft oder einem anderen Benutzer
zugewiesen wird, und öffnen wieder, sobald Sie das Modell wieder haben.

## Rechte

In der Rollenverwaltung ([Desktop](../admin/roles.md),
[Web-App](../web/roles.md)) steht die Gruppe **Flechtsimulator** mit zwei
Rechten. Sie erscheint nur, wenn Ihr Konto den Flechtsimulator nutzen darf.

| Recht | Erlaubt | Standardrollen |
|---|---|---|
| **Flechtsimulator anzeigen** | Den Flechtsimulator öffnen, Besetzungen und Programme laden, abspielen, prüfen und den Schaltplan ausgeben. | Administrator, Bearbeiter, Betrachter |
| **Flechtsimulator bearbeiten** | Eigene Besetzungen und Programme anlegen, speichern und löschen, **Betriebsart einfügen…**. Ohne dieses Recht können Sie alles ausprobieren; beim Verlassen werden die Änderungen ohne Rückfrage verworfen. | Administrator, Bearbeiter |

Die Rechte sagen nur, was eine Rolle tun darf. Welche Maschinen ein
Benutzer sieht, bestimmt allein die Zuweisung der Modell-Lizenzen.

## Wann eine Änderung ankommt

| Wo | Wann |
|---|---|
| **Web-App** | Lädt die Liste der Maschinen alle fünf Minuten und beim Zurückkehren ins Browserfenster neu. |
| **Programm, online** | Merkt beim regelmäßigen Abgleich mit dem Lizenzserver (alle fünf Minuten), dass sich etwas geändert hat, und lädt die Liste neu. Eine neue Zuweisung oder ein Entzug wirkt also nach etwa fünf Minuten. |
| **Programm, offline** | Zeigt ein Modell ohne Verbindung zum Lizenzserver **höchstens 7 Tage** lang, auch wenn Sie mit *Offline arbeiten* bis zu 30 Tage ohne Verbindung arbeiten dürfen. Danach steht das Modell mit *Verbindung zum Lizenzserver nötig* in der Liste und öffnet erst wieder, wenn das Programm Verbindung hatte. |

Neue Fassungen eines Modells, die Herzog freigibt, kommen ebenfalls mit dem
Abgleich, siehe [Startseite](index.md#startseite).

## Wenn eine Lizenz wegfällt

### In der Liste

Die Startseite des Flechtsimulators zeigt unter dem Namen des Modells den
Grund, warum es nicht öffnet:

| Anzeige | Bedeutung |
|---|---|
| *Lizenz abgelaufen am &lt;Datum&gt;* | Die Lizenz ist abgelaufen. Das Modell steht grau in der Liste. Ihre Besetzungen und Programme bleiben sichtbar, öffnen aber erst wieder, wenn Herzog die Lizenz verlängert. |
| *Keine gültige Lizenz* | Für das Modell gibt es keine gültige Lizenz. |
| *Verbindung zum Lizenzserver nötig* | Die Lizenz gilt, aber das Programm war zu lange ohne Verbindung zum Lizenzserver. |

Ist Ihnen gar kein Modell zugewiesen, steht in der leeren Liste *Ihnen ist
kein Maschinenmodell zugewiesen. Ihr Administrator weist Modell-Lizenzen
im Lizenzportal zu.* In der Web-App erscheint darunter für Administratoren
der Knopf **Im Lizenzportal zuweisen**.

### Während Sie arbeiten

Wird Ihnen ein Modell entzogen, während es geöffnet ist, oder läuft seine
Lizenz ab, hält die Wiedergabe sofort an.

=== "Desktop-App"

    Ein Fenster **Flechtsimulator** nennt den Grund, zum Beispiel *Die
    Maschine „…“ ist Ihnen nicht mehr zugewiesen. Ihr Administrator hat die
    Lizenz im Lizenzportal einem anderen Benutzer gegeben. Die Wiedergabe
    ist angehalten.*

    * Haben Sie ungespeicherte eigene Änderungen, steht dabei *Ihre eigenen
      Besetzungen und Programme können Sie jetzt noch speichern.* Wählen Sie
      **Speichern und zurück** oder **Verwerfen und zurück**.
    * Sonst führt **Zurück zur Liste** auf die Startseite.
    * Schließen Sie das Fenster mit dem Kreuz, bleiben Sie in der Maschine,
      aber die Wiedergabe bleibt gesperrt.

    Kommt die Lizenz zurück (zum Beispiel weil die Verbindung wieder steht),
    geht es ohne Rückfrage weiter.

=== "Web-App"

    Über der Maschine erscheint *Diese Maschine ist Ihnen nicht mehr
    zugewiesen oder ihre Lizenz ist abgelaufen. Die Wiedergabe ist
    angehalten.* Mit **Zum Flechtsimulator** kommen Sie zurück zur Liste.

## Verwandte Seiten

* [Maschinenmodelle zuweisen](../portal/models.md) — die Seite im
  Lizenzportal für Administratoren.
* [Flechtsimulator](index.md) — Überblick und Startseite.
* [Kundenkonto und Einladung](../setup/account.md) — Bausteine, Plätze,
  Rollen.
* [Rollen und Berechtigungen](../admin/roles.md)
