# Einstellungen (Web-App)

!!! abstract "Referenz — Die Seite „Einstellungen" im Benutzermenü der Web-App: Sprache, Flechtwinkel, Produktionsplanung, angemeldeter Benutzer, Datenschutz, Designer-Vorgaben und der Weg zu Passwort und Sicherheit"

## Wofür Sie diesen Bereich nutzen

Die Web-App hat bewusst wenige Einstellungen: Das meiste — Benutzer, Rollen,
Bausteine, Firmendaten — liegt im [Kundenkonto](account.md) bzw. im
[Lizenzportal](../portal/index.md). Hier stellen Sie Ihre **Sprache** ein,
wählen, wie der **Flechtwinkel** gemessen wird, legen die
**Produktionsstunden je Arbeitstag** fest und passen den **Designer** an.

Sie öffnen die Seite über *Benutzermenü > Einstellungen*.

## Der Bildschirm im Überblick

![Einstellungen der Web-App mit den Karten Sprache, Flechtwinkel, Produktionsplanung, Angemeldet als, Datenschutz, Designer und Passwort und Sicherheit.](../assets/screenshots/web/einstellungen.png)

Die Karten stehen untereinander. Unter jedem Kartentitel steht, für wen die
Einstellung gilt: für **diesen Benutzer** (auf allen Geräten), für **alle
Benutzer dieses Kontos** oder nur für **diesen Browser**.

## Bedienelemente im Detail

| Karte | Gilt für | Inhalt |
|---|---|---|
| **Sprache** | diesen Benutzer | Deutsch, Englisch, Polnisch, Spanisch, Italienisch oder Chinesisch. Dieselbe Auswahl steht in der Kopfzeile. |
| **Flechtwinkel** | diesen Benutzer | **Flechtwinkel messen**: gegen welche Richtung Herzog CAB den Flechtwinkel zeigt (siehe [unten](#flechtwinkel)). |
| **Produktionsplanung** | alle Benutzer dieses Kontos | **Produktionsstunden je Arbeitstag**, 1 bis 24 h in Schritten von 0,5 h (Vorgabe 8 h). Damit rechnet ein Auftrag die Laufzeit-Hochrechnung in Kalendertage um, wenn Sie das Produktionsende aus der Hochrechnung übernehmen; Wochenenden werden übersprungen. Sehen dürfen die Karte alle mit dem Recht *Aufträge anzeigen*, ändern alle mit *Aufträge bearbeiten*. Mit dem Baustein *Herzog CAB Designer* fehlt sie. Die Desktop-App merkt sich denselben Wert je Rechner, siehe [Produktionsplanung (Desktop-App)](../admin/settings/appearance.md#produktionsplanung). |
| **Angemeldet als** | — | Name, E-Mail-Adresse und Firma, dazu die Edition als Chip (bei internen Konten der Vermerk *internes Konto*). Ihren Namen ändern Sie im [Lizenzportal](../portal/security.md#name). |
| **Datenschutz** | diesen Browser | **Anonyme Nutzungsstatistik senden**: welche Funktionen und Berechnungen genutzt werden, ohne Inhalte, Namen oder Konto. Darf der Browser keine Daten speichern, ist das Kästchen gesperrt. Mehr dazu unter [Datenschutz (Desktop-App)](../admin/settings/appearance.md#datenschutz). |
| **Designer** | diesen Browser | Vorgaben für neue Designs, Vorschau und Ansicht, Animation und das Verhalten bei ungespeicherten Änderungen — dieselben Einstellungen wie in der Desktop-App unter [Design](../admin/settings/legacy-import.md#vorgaben-fur-neue-designs). Nur mit dem Recht *Designer anzeigen*. |
| **Passwort und Sicherheit** | — | Hinweis: *Passwort und Zwei-Faktor-Anmeldung werden im Lizenzportal verwaltet.* Der Knopf darunter öffnet dort die Seite [Passwort, zweiter Faktor und Name](../portal/security.md). |

### Flechtwinkel

Herzog misst den Flechtwinkel gegen die **Querrichtung** des Geflechts, die
Fachliteratur meist gegen die **Geflechtsachse**. Beide Angaben ergeben
zusammen 90°, bei 45° sind sie gleich.

| Auswahl | Wirkung |
|---|---|
| **Zur Querrichtung (Herzog)** | Vorgabe. Winkel wie in der Desktop-App. |
| **Zur Geflechtsachse (Fachliteratur)** | Alle Winkel erscheinen als Ergänzung zu 90°, zum Beispiel 30° statt 60°. |

Die Wahl gilt für Anzeige, Eingabe und Ausdruck in Berechnungen,
Aufträgen, im Designer und im Druck. Ihre gespeicherten Daten ändern sich
dabei nicht. Wenn Sie auf einen Winkel zeigen, nennt eine Einblendung beide
Werte.

!!! info "Unterschied zur Desktop-App"
    Schriftgröße, Design (hell/dunkel), Diagnose, Speicherorte,
    Legacy-Designimport und Webserver gibt es nur in der
    [Desktop-App](../admin/settings/index.md). Die Web-App folgt der
    Schriftgröße und dem Zoom des Browsers.

## Verwandte Seiten

* [Oberfläche der Web-App](interface.md) — Sprachauswahl in der Kopfzeile
* [Konto und Benutzer](account.md)
* [Aufträge (Web-App)](orders.md) — Produktionsende aus der Hochrechnung
* [Passwort, zweiter Faktor und Name (Lizenzportal)](../portal/security.md)
