# Update-Fehler

!!! question "Problemlösung — Ein Update lässt sich nicht installieren"

## Der Update-Dialog erscheint nicht

Herzog CAB prüft beim Start automatisch im Hintergrund, ob eine neuere
Version vorliegt. Erscheint kein Hinweis, obwohl Sie eine neue Version
erwarten:

* Prüfen Sie über Menü *Über → Updates* manuell – dabei erscheint auch die
  Meldung, falls bereits die aktuelle Version installiert ist.
* Prüfen Sie die Internetverbindung sowie, ob eine Firewall oder ein Proxy
  den Zugriff auf `herzog-gmbh.github.io` blockiert.
* Die aktuell installierte Version sehen Sie unter *Über → Über Herzog CAB*.

## „Update-Prüfung fehlgeschlagen"

Diese Meldung erscheint bei der manuellen Prüfung (*Über → Updates*), wenn
die Versionsinformationen nicht abgerufen oder nicht ausgewertet werden
konnten – meist ein Netzwerk- oder Firewall-Problem. Prüfen Sie die
Internetverbindung und versuchen Sie es später erneut. Besteht das Problem
weiterhin, wenden Sie sich an den [Support](support.md).

## Das Maintenance-Tool startet, bricht aber ab

* **Zu wenig Rechte.** Das Maintenance-Tool muss mit Administratorrechten
  laufen können. Starten Sie `HerzogCAB_Maintenance` per Rechtsklick über
  **Als Administrator ausführen**.
* **„Repository nicht erreichbar".** Prüfen Sie die Internetverbindung und
  ob die Adresse
  `https://herzog-gmbh.github.io/HerzogCAB-Feedback/repository/` im Browser
  erreichbar ist.
* **„Komponente fehlt".** Schließen Sie Herzog CAB vollständig – auch das
  Maintenance-Tool selbst, falls es bereits im Hintergrund läuft – und
  starten Sie das Update erneut.

## Sind meine Daten nach einem Update noch da?

Ja. Das Maintenance-Tool ersetzt ausschließlich die Programmdateien im
Installationsverzeichnis. Ihre Stammdaten liegen davon getrennt – im
Arbeitsverzeichnis Ihres Profils und maschinenweit unter `%ProgramData%` –
und werden von einem Update nicht angefasst. Details dazu finden Sie unter
[Dateispeicherorte](../appendix/file-locations.md).

!!! tip "Im Zweifel sichern"
    Legen Sie vor einem größeren Update sicherheitshalber eine Kopie Ihres
    Arbeitsverzeichnisses an, insbesondere wenn es auf einem Netzlaufwerk
    liegt.

## Verwandte Seiten

* [Updates installieren](../setup/update.md)
* [Deinstallation](../setup/uninstall.md)
* [Dateispeicherorte](../appendix/file-locations.md)
