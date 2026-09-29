# Loslegen

!!! example "Anleitung — Vom Kundenkonto bzw. der Installation bis zum ersten Programmstart"

Dieses Kapitel begleitet Sie von der Erstinstallation bis zum ersten
Programmstart. Rechnen Sie für die komplette Strecke mit rund 15 Minuten.
Wenn Herzog CAB bei Ihnen bereits läuft und Sie nur ein **Update**
einspielen oder das Programm **deinstallieren** wollen, springen Sie direkt
zur passenden Karte unten.

!!! info "Desktop-App oder Web-App?"
    Herzog CAB gibt es seit Version 2.0 in zwei Formen: als **Desktop-App**
    für Windows (macOS auf Anfrage) und als **Web-App** im Browser unter
    [app.herzog-cab.com](https://app.herzog-cab.com). Dieses Kapitel beschreibt
    die Installation der Desktop-App. Für die Web-App gibt es nichts zu
    installieren — Sie brauchen nur Ihr Kundenkonto, siehe
    [Web-App](../web/index.md). Welche Form wofür passt, erklärt
    [Desktop-App oder Web-App?](../basics/platforms.md).

<div class="grid cards" markdown>

- :material-clipboard-check-outline: **Systemvoraussetzungen**

    Windows-Version, Hardware, Internetzugang und Berechtigungen, die für
    die Installation nötig sind.

    [:octicons-arrow-right-24: Weiter](system-requirements.md)

- :material-lan: **Einsatz-Szenarien**

    Single-Client, Server mit RDP-Zugriff, Mixed Setup oder Web-App —
    welche Topologie passt zu Ihrem Werk?

    [:octicons-arrow-right-24: Weiter](topology.md)

- :material-account-key-outline: **Kundenkonto und Einladung**

    Das Kundenkonto ist seit Version 2.0 der normale Lizenzweg: Einladung
    annehmen, Passwort setzen, Bausteine und Plätze verstehen.

    [:octicons-arrow-right-24: Weiter](account.md)

- :material-application-cog-outline: **Herzog CAB installieren**

    Den Einrichtungsassistenten von Herzog CAB durchlaufen.

    [:octicons-arrow-right-24: Weiter](installer.md)

- :material-key-variant: **Anmelden und Lizenz beziehen**

    Beim ersten Start am Kundenkonto anmelden — oder, für Bestandskunden,
    CmDongle einstecken bzw. eine CmAct-Lizenz aktivieren.

    [:octicons-arrow-right-24: Weiter](activate-license.md)

- :material-usb-flash-drive-outline: **CodeMeter installieren**

    Nur für Bestandskunden mit Dongle oder Software-Lizenz: die
    Wibu-Laufzeitumgebung einrichten.

    [:octicons-arrow-right-24: Weiter](codemeter.md)

- :material-rocket-launch-outline: **Erststart und Einrichtung**

    Was beim ersten Programmstart passiert: Benutzer, Speicherort und
    Arbeitsverzeichnis.

    [:octicons-arrow-right-24: Weiter](first-run.md)

- :material-cloud-download-outline: **Updates installieren**

    Neue Version über das Maintenance-Tool einspielen.

    [:octicons-arrow-right-24: Weiter](update.md)

- :material-trash-can-outline: **Deinstallation**

    Herzog CAB entfernen — mit oder ohne Ihre Auftrags- und Stammdaten.

    [:octicons-arrow-right-24: Weiter](uninstall.md)

</div>

## Ablauf der Erstinstallation

Welche Schritte nötig sind, hängt davon ab, wie Ihre Lizenz bereitgestellt
wird. Seit Version 2.0 ist das **Kundenkonto** der Regelfall; wer einen
**CmDongle** oder eine **CmAct-Software-Lizenz** besitzt, arbeitet damit
unverändert weiter.

=== "Kundenkonto (Regelfall ab 2.0)"

    ```mermaid
    flowchart LR
      A[Systemvoraussetzungen] --> B[Einladung annehmen,<br>Passwort setzen]
      B --> C[Herzog CAB installieren]
      C --> D[Erster Start:<br>am Konto anmelden]
      D --> E[Arbeitsverzeichnis<br>einrichten]
    ```

    1. [Systemvoraussetzungen](system-requirements.md) prüfen — der Rechner
       braucht für die Anmeldung eine Internetverbindung.
    2. Die [Einladung ins Kundenkonto](account.md) annehmen und ein Passwort
       setzen. Die Einladung schickt Herzog oder ein Administrator Ihrer Firma.
    3. Den Installer aus dem Lizenzportal laden und
       [Herzog CAB installieren](installer.md).
    4. Beim ersten Start [am Kundenkonto anmelden](activate-license.md) — die
       Lizenz wird aus dem Vorrat Ihres Kontos gezogen.
    5. Das [Arbeitsverzeichnis einrichten](first-run.md).

=== "Dongle oder CmAct-Lizenz (Bestandskunden)"

    ```mermaid
    flowchart LR
      A[Systemvoraussetzungen] --> B[Einsatz-Szenario]
      B --> C[CodeMeter]
      C --> D[Herzog CAB installieren]
      D --> E[Lizenz aktivieren]
      E --> F[Erststart-Assistent]
    ```

    1. [Systemvoraussetzungen](system-requirements.md) und
       [Einsatz-Szenario](topology.md) klären.
    2. [CodeMeter installieren](codemeter.md).
    3. [Herzog CAB installieren](installer.md).
    4. [Dongle einstecken oder CmAct-Lizenz aktivieren](activate-license.md#bestandskunden-dongle-oder-cmact-lizenz).
    5. Den [Erststart-Assistenten](first-run.md) durchlaufen (Administrator
       anlegen, Arbeitsverzeichnis wählen).

Danach ist Herzog CAB einsatzbereit. Wie Sie sich in der Oberfläche
zurechtfinden, zeigt das Kapitel [Grundlagen](../basics/index.md).

!!! info "Sie haben noch kein Kundenkonto und kein Installationspaket?"
    Wenden Sie sich an Ihren Herzog-Ansprechpartner oder schreiben Sie an
    [e.siemering@herzog-online.com](mailto:e.siemering@herzog-online.com).
    Die Web-App können Sie außerdem 30 Tage lang
    [kostenlos testen](../web/trial.md).
