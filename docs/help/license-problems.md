# Lizenzprobleme

!!! question "Problemlösung — Herzog CAB startet nicht, meldet einen Lizenzfehler oder findet keinen freien Platz"

Ohne gültige Lizenz lässt sich Herzog CAB nicht starten. Seit Version 2.0
gibt es zwei Lizenzwege — das **Kundenkonto** (Regelfall) und **Wibu
CodeMeter** (Bestandskunden mit Dongle oder CmAct-Lizenz). Die folgenden
Abschnitte helfen bei den häufigsten Fehlerbildern beider Wege. Grundlagen
finden Sie unter [Anmelden und Lizenz beziehen](../setup/activate-license.md).

## Kundenkonto: Meldungen beim Start

| Meldung | Ursache | Abhilfe |
|---|---|---|
| Dialog **Anmeldung am Kundenkonto** erscheint, obwohl der Rechner schon angemeldet war | Die Anmeldung wurde aufgehoben — über **Von diesem Rechner abmelden**, **Plätze freigeben** bzw. **Sperren** im Lizenzportal, oder die Miete ist nach längerer Zeit ohne Verbindung abgelaufen. | Erneut anmelden; ist der Rechner im Portal gesperrt, muss ihn ein Administrator [entsperren](../portal/licenses.md#rechner). |
| *E-Mail-Adresse oder Passwort stimmen nicht.* | Tippfehler oder geändertes Passwort. | Passwort über **Passwort vergessen** im [Lizenzportal](../portal/index.md) zurücksetzen. |
| *Der Code stimmt nicht.* | Zweiter Faktor: Code abgelaufen oder Uhrzeit des Handys weicht ab. | Nächsten Code abwarten; Uhrzeit des Handys automatisch stellen lassen. Ist die Authenticator-App verloren, setzt Herzog den zweiten Faktor zurück ([Support](support.md)). |
| *Kein freier Platz für: <Baustein>. Bitte im Lizenzportal einen Platz freigeben oder anfragen.* | Alle Plätze des Bausteins sind von anderen Rechnern belegt. | Ein Administrator gibt im [Lizenzportal](../portal/licenses.md) einen Rechner frei (z. B. einen ausgemusterten) oder [fragt Plätze an](../portal/requests.md). Rechner, die sieben Tage nicht gestartet wurden, geben ihren Platz von selbst frei. |
| *Dieser Benutzer ist deaktiviert.* | Der Benutzer wurde im Portal deaktiviert. | Administrator des Kontos ansprechen ([Benutzer](../portal/users.md)). |
| *Zu viele Fehlversuche. Bitte später erneut versuchen.* | Der Lizenzserver bremst nach mehreren Fehlversuchen aus derselben Verbindung. | Einige Minuten warten. |
| *Der Lizenzserver ist nicht erreichbar …* | Keine Verbindung zu `license.herzog-cab.com` (Internet, Proxy, Firewall). | Verbindung prüfen. Ein bereits angemeldeter Rechner läuft mit seiner Miete weiter (sieben Tage, mit Offline-Miete bis 30 Tage); für die **erste** Anmeldung ist eine Verbindung Pflicht. |
| *keine gültige Bestätigung* unter *Einstellungen > Lizenz > Miete* | Die Miete konnte zuletzt nicht verlängert werden (Server nicht erreichbar oder Freischaltung beendet). | Verbindung prüfen und **Miete jetzt verlängern**; ist der Baustein im Portal *abgelaufen* oder *beendet*, [verlängern](../portal/requests.md). |
| Dieses Konto ist gesperrt (Meldung im Portal) | Herzog hat das Konto gesperrt; es gibt keine neuen Lizenzen mehr aus. | [Support](support.md) kontaktieren. |

!!! tip "Länger ohne Internet unterwegs?"
    Ziehen Sie vorher unter *Einstellungen > Lizenz* eine
    [Offline-Miete](../admin/settings/license.md) für bis zu 30 Tage.

## CodeMeter: „Keine gültige Lizenz" beim Programmstart

1. Öffnen Sie das **CodeMeter Kontrollzentrum** (Doppelklick auf das
   Tray-Symbol unten rechts, oder über die Windows-Suche).
2. Prüfen Sie, ob dort eine Lizenz für **Firmencode 6001037**, **Artikel
   88805** (Vollversion, Product Code 200006) angezeigt wird.
3. Ist gar kein Eintrag vorhanden, wurde die Lizenz noch nicht eingespielt –
   siehe [Lizenz aktivieren](../setup/activate-license.md).

=== "USB-Dongle (CmDongle)"

    * Steckt der Dongle in einem **freien USB-Anschluss**? Ein anderer Port
      oder ein direkter Anschluss am Rechner (ohne USB-Hub) hilft bei
      Erkennungsproblemen.
    * Der Dongle muss während des gesamten Betriebs **eingesteckt bleiben**.
    * Nutzen Sie den Dongle bereits an einem anderen Rechner? Er funktioniert
      immer nur an **einem** Rechner gleichzeitig.

=== "Software-Lizenz (CmActLicense)"

    * Diese Lizenz ist an den **Fingerabdruck** des Rechners gebunden und
      läuft nach einem Hardware-Wechsel oder Rechnerumzug ins Leere – siehe
      die Hinweise zu Hardware-Wechsel und Umzug unter
      [Lizenz aktivieren](../setup/activate-license.md).
    * Prüfen Sie im Kontrollzentrum, ob der Status **„Aktivierung ungültig"**
      zeigt – dann fehlt noch die Aktivierungsdatei (`.WibuCmRaU`), siehe
      Schritt 4 unter [Lizenz aktivieren](../setup/activate-license.md).

=== "Netzwerklizenz"

    * Ist der Lizenzserver im Netzwerk erreichbar? Prüfen Sie im
      CodeMeter **WebAdmin** (`http://localhost:22350` auf dem Client) unter
      *Server-Suchliste*, ob der Server gefunden wird.
    * Firewall zwischen Arbeitsplatz und Lizenzserver freigeben – CodeMeter
      benötigt Port 22350 (TCP/UDP).
    * Sind bereits **alle Lizenzplätze** durch andere Arbeitsplätze belegt?
      Ein Kollege muss Herzog CAB dann zuerst schließen.

## „The Firm Access Counter has a value of 0" / Error 38

Dieser Fehler unterscheidet sich von den oberen Fällen: Er bedeutet, dass der
Kopierschutz von Herzog CAB die Lizenz **aus Sicherheitsgründen gesperrt**
hat – zum Beispiel weil ein Debugger, ein Remote-Support-Tool oder eine
Virtualisierungsumgebung erkannt wurde, während Herzog CAB lief. Das kann
auch bei völlig harmloser Software (Fernwartung, Virenscanner) passieren.

!!! warning "Kein Selbsthilfe-Fall"
    Diese Sperre lässt sich **nicht** durch Neustart, Deinstallation oder
    Dongle-Aus-/Einstecken aufheben – der Zähler steckt in der Lizenz selbst.
    Sie muss von Herzog GmbH zurückgesetzt werden.

So gehen Sie vor:

1. Öffnen Sie das **CodeMeter Kontrollzentrum** und notieren Sie sich die
   **Container-Seriennummer** der betroffenen Lizenz (Firmencode 6001037).
2. Wenden Sie sich an den [Support](support.md) und nennen Sie die
   Seriennummer sowie den genauen Fehlertext.
3. Herzog GmbH schickt Ihnen eine Freischaltdatei zurück, die Sie im
   CodeMeter Kontrollzentrum einspielen.

## Lizenzprüfung im Überblick

| Status | Verhalten |
|---|---|
| CodeMeter-Lizenz vorhanden, gültig | Programm startet normal. |
| Kein CodeMeter-Container, Rechner am Konto angemeldet | Programm startet normal; Miete wird im Hintergrund verlängert. |
| Kein CodeMeter-Container, Rechner nicht angemeldet | Dialog *Anmeldung am Kundenkonto*. |
| Miete abgelaufen, Server nicht erreichbar | Hinweis-Dialog; mit Verbindung startet das Programm wieder. |
| Lizenz abgelaufen / Baustein beendet | Hinweis-Dialog, Programm startet nicht. |
| Keine gültige Lizenz | Hinweis-Dialog, Programm startet nicht. |
| Firm Access Counter = 0 (Error 38) | Programm startet nicht, Support-Fall (siehe oben). |

## Web-App: kein Zugang

| Meldung | Abhilfe |
|---|---|
| *Für das Konto … ist Herzog CAB Web nicht freigeschaltet oder die Testphase ist abgelaufen.* | Web-Baustein unter [Abo und Kauf](../web/subscription.md) kaufen bzw. anfragen oder im [Lizenzportal](../portal/requests.md) anfordern. Die Daten bleiben erhalten. |
| *Belegt: n von m Plätzen.* | Alle Web-Plätze sind belegt; ein Platz wird nach 15 Minuten ohne Aktivität frei — oder mehr Plätze anfragen. |

## Verwandte Seiten

* [Lizenz aktivieren](../setup/activate-license.md)
* [CodeMeter installieren](../setup/codemeter.md)
* [Einsatz-Szenarien](../setup/topology.md) – Einzelplatz, Netzwerk, RDP
* [Support kontaktieren](support.md)
