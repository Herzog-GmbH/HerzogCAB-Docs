# Web-App

!!! abstract "Referenz — Herzog CAB im Browser unter app.herzog-cab.com: was die Web-App ist, was sie kann und wo sich die Module finden"

## Was die Web-App ist

**Herzog CAB Web** ist Herzog CAB als Anwendung im Browser. Es gibt nichts
zu installieren: Sie öffnen [app.herzog-cab.com](https://app.herzog-cab.com),
melden sich mit Ihrem Benutzer aus dem [Kundenkonto](../setup/account.md) an
und arbeiten im **Arbeitsbereich Ihrer Firma** — alle Benutzer des Kontos
sehen dieselben Aufträge, Designs, Maschinen und Stammdaten. Die Rechner
liefern dieselben Ergebnisse wie die Desktop-App, der Designer zeichnet
dieselben Flechtbilder, und der Druck nutzt dieselben Druckvorlagen.

Die Web-App gehört zum Jahresabo (**Herzog CAB Vollversion** oder
**Herzog CAB Designer**) und teilt sich dessen Plätze mit dem Programm. Ein
Platz ist eine Person, die gerade arbeitet. Wer im Programm und im Browser
zugleich arbeitet, belegt zwei Plätze. Zum Ausprobieren legt Herzog Ihnen
auf Anfrage eine kostenlose [Testversion](trial.md) an: 30 Tage, im
Programm und im Browser.

![Startseite der Web-App mit Seitenleiste, Begrüßung, Aufträgen, Produktion und Favoriten.](../assets/screenshots/web/startseite.png)

## Die Module

<div class="grid cards" markdown>

- :material-login-variant: **Anmelden und Konto wählen**

    ---

    Anmeldung mit E-Mail-Adresse, Passwort und Code; Kontowahl; Abmelden.

    [:octicons-arrow-right-24: Anmelden](login.md)

- :material-view-quilt-outline: **Oberfläche**

    ---

    Seitenleiste, Kopfzeile, Reiter, Benutzermenü und die Bedienung am
    Tablet und Smartphone.

    [:octicons-arrow-right-24: Oberfläche](interface.md)

- :material-home-outline: **Startseite**

    ---

    Aufträge nach Status, anstehende Produktion, Favoriten, zuletzt
    Geöffnetes und Schnellzugriff auf alle Module; anpassbar.

    [:octicons-arrow-right-24: Startseite](start.md)

- :material-clipboard-list-outline: **Aufträge**

    ---

    Flecht- und Spulaufträge anlegen, filtern, bearbeiten und drucken.

    [:octicons-arrow-right-24: Aufträge](orders.md)

- :material-calculator-variant-outline: **Berechnungen**

    ---

    Alle Rechner der Desktop-App in fünf Gruppen — dieselben Eingaben und
    Ergebnisse, mit Favoriten und Historie.

    [:octicons-arrow-right-24: Berechnungen](calculations.md)

- :material-palette-outline: **Designs und Designer**

    ---

    Design-Bibliothek und Designer mit allen sechs Geflechtsarten,
    Besetzungsübersicht und echter 3D-Ansicht.

    [:octicons-arrow-right-24: Designs und Designer](designer.md)

- :material-factory: **Maschinen**

    ---

    Maschinenpark mit Flecht- und Spulmaschinen sowie der Herzog-Katalog.

    [:octicons-arrow-right-24: Maschinen](machines.md)

- :material-database-outline: **Stammdaten**

    ---

    Materialien, Spulen, Farben und Kunden.

    [:octicons-arrow-right-24: Stammdaten](master-data.md)

- :material-floor-plan: **Hallenplaner**

    ---

    Grundrisse zeichnen, Belegungen mit Maschinen planen, 2D und 3D.

    [:octicons-arrow-right-24: Hallenplaner](hall-planner.md)

- :material-printer-outline: **Drucken**

    ---

    Aufträge, Spulaufträge und Designs mit Druckvorlagen als Seite oder PDF.

    [:octicons-arrow-right-24: Drucken](print.md)

- :material-file-document-edit-outline: **Druck Editor**

    ---

    Druckvorlagen für Aufträge, Designs und Berechnungen im Browser
    gestalten.

    [:octicons-arrow-right-24: Druck Editor](print-editor.md)

- :material-history: **Versionen und Papierkorb**

    ---

    Frühere Fassungen eines Eintrags ansehen und wiederherstellen,
    gelöschte Einträge zurückholen.

    [:octicons-arrow-right-24: Versionen und Papierkorb](versions.md)

- :material-account-cog-outline: **Benutzermenü**

    ---

    Einstellungen, Konto und Benutzer, Abo und Bestellung, Firma,
    Medienbibliothek, Papierkorb, Rollen und der Import aus dem Desktop.

    [:octicons-arrow-right-24: Einstellungen](settings.md) ·
    [Konto und Benutzer](account.md) ·
    [Abo und Bestellung](subscription.md) ·
    [Firma](company.md) ·
    [Medienbibliothek](media.md) ·
    [Papierkorb](versions.md#papierkorb) ·
    [Rollen](roles.md) ·
    [Import aus dem Desktop](import.md)

- :material-clock-start: **Testphase und Registrierung**

    ---

    30 Tage kostenlos testen: Testversion anfragen, Grenzen der
    Testphase, Weg zum Abo.

    [:octicons-arrow-right-24: Testphase](trial.md)

</div>

## Desktop-App und Web-App im Vergleich

Beide Programme arbeiten mit demselben Datenmodell; ein Arbeitsbereich der
Desktop-App lässt sich [in die Web-App übernehmen](import.md). Nicht alles
gibt es in beiden — die wichtigsten Unterschiede:

| | Desktop-App | Web-App |
|---|---|---|
| Installation | Windows / macOS, Installer | keine — Browser |
| Daten | Arbeitsverzeichnis auf Rechner oder Netzlaufwerk, je Profil | zentral im Kundenkonto, ein Arbeitsbereich je Konto |
| Benutzer | Kontobenutzer (oder lokal / Entra / LDAP bei Dongle) | ausschließlich Kontobenutzer |
| Berechnungen | alle Rechner, Verlauf, Favoriten | dieselben Rechner, Historie und Favoriten je Benutzer auf allen Geräten, Suche |
| Designer | alle sechs Geflechtsarten, Färben per Klick, Texturen, Gangbahn-Animation, echtes 3D, Zwei-Fenster-Vergleich, Mischdesigns | alle sechs Geflechtsarten, Färben per Klick, Texturen, Fachungsfarben (Farbe je Garn), Besetzungsübersicht mit Animation, echtes 3D; ein Design je Seite, Mischdesigns nur ansehen |
| Versionen | — | frühere Fassungen und Papierkorb für Aufträge, Designs, Maschinen, Stammdaten, Hallenpläne und Druckvorlagen, auch für Änderungen aus dem Cloud-Abgleich |
| Aufträge | Flecht- und Spulauftrag, Zeitraumfilter, Duplizieren | Flecht- und Spulauftrag, Filter nach Art, Status und Maschine |
| Druck | Druck-Editor für Vorlagen, Drucken über Windows | Druck Editor für Vorlagen (mit Rückgängig und Vorschau mit Beispieldaten), Drucken über den Browser, PDF |
| Hallenplaner | 2D-Editor mit Wandtexturen, Kontextmenüs, automatische Flächen, 3D | 2D-Editor (Wände, Flächen, Türen, Tore, Fenster, Treppen, Kalibrieren), 3D-Ansicht |
| Maschinen | Maschinenpark, Herzog-Katalog (ab 2.1.0), Stammdaten-Dialoge, 3D-Modelle | Maschinenpark mit Karten/Liste, Katalog, volle Maschinenpflege |
| Mobile Nutzung | Webserver mit QR-Code (Auftragsansicht) | die ganze App, angepasst an Tablet und Smartphone |
| Lizenz | Jahresabo, ein Platz je laufendem Programm | dasselbe Jahresabo, ein Platz je Person im Browser |

Eine Gegenüberstellung für die Entscheidung im Werk steht unter
[Desktop-App oder Web-App?](../basics/platforms.md).

!!! info "Sprachen"
    Die Web-App gibt es wie die Desktop-App in Deutsch, Englisch, Polnisch,
    Spanisch, Italienisch und Chinesisch. Die Sprache wählen Sie in der
    Kopfzeile oder unter [Einstellungen](settings.md); sie gilt für Ihren
    Benutzer auf allen Geräten.

## Verwandte Seiten

* [Kundenkonto und Einladung](../setup/account.md)
* [Systemvoraussetzungen](../setup/system-requirements.md#web-app) — Browser und Bildschirm
* [Daten vom Desktop in die Web-App bringen](../tasks/desktop-to-web.md)
* [Lizenzportal](../portal/index.md) — Bausteine und Plätze
