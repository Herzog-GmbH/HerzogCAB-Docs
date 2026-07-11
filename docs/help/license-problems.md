# Lizenzprobleme

!!! question "Problemlösung — Herzog CAB startet nicht oder meldet einen Lizenzfehler"

Herzog CAB nutzt **Wibu CodeMeter** als Lizenzsystem. Ohne gültige Lizenz lässt
sich das Programm nicht starten. Die folgenden Abschnitte helfen bei den
häufigsten Fehlerbildern. Grundlagen zur Aktivierung finden Sie unter
[Lizenz aktivieren](../setup/activate-license.md).

## „Keine gültige Lizenz" beim Programmstart

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
| Lizenz vorhanden, gültig | Programm startet normal. |
| Lizenz abgelaufen | Hinweis-Dialog, Programm startet nicht. |
| Keine gültige Lizenz | Hinweis-Dialog, Programm startet nicht. |
| Firm Access Counter = 0 (Error 38) | Programm startet nicht, Support-Fall (siehe oben). |

## Verwandte Seiten

* [Lizenz aktivieren](../setup/activate-license.md)
* [CodeMeter installieren](../setup/codemeter.md)
* [Einsatz-Szenarien](../setup/topology.md) – Einzelplatz, Netzwerk, RDP
* [Support kontaktieren](support.md)
