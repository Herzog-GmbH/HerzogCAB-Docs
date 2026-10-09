# Allgemein: Sprache, Darstellung, Datenschutz, Produktionsplanung und Flechtwinkel

!!! abstract "Referenz — Tab „Allgemein" des Einstellungen-Dialogs: Profil-Schnellzugriff, Sprache, Schriftgröße, Design, Diagnose-Protokoll, anonyme Nutzungsstatistik, Produktionsplanung und Bezug des Flechtwinkels."

## Wofür Sie diesen Bereich nutzen

Im Tab **Allgemein** (*Datei > Einstellungen*) stellen Sie die Sprache und
das Erscheinungsbild der gesamten Oberfläche ein, aktivieren bei Bedarf das
Diagnose-Protokoll, entscheiden über die anonyme Nutzungsstatistik und
legen fest, wie Herzog CAB den Flechtwinkel misst.

![Tab „Allgemein" mit Profil, Darstellung, Diagnose und Datenschutz.](../../assets/screenshots/settings/einstellungen-allgemein.png)

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Einstellungen, Tab „Allgemein“ ohne Kopfkarte, mit den Karten Profil, Darstellung, Diagnose, Datenschutz, Produktionsplanung und der neuen Karte „Flechtwinkel“ (Auswahl „Flechtwinkel messen“ aufgeklappt); unten rechts **Speichern** und **Abbrechen**.
    **So erzeugen:** *Datei > Einstellungen*, Tab **Allgemein**, Dialog so hoch ziehen, dass alle Karten sichtbar sind; die Auswahl „Flechtwinkel messen“ aufklappen.
    **Ziel-Datei:** `assets/screenshots/settings/einstellungen-allgemein.png` (ersetzt das bisherige Bild)

## Bedienelemente im Detail

### Profil

Die Karte **Profil** zeigt das aktive Profil und bietet die Schaltflächen
**Profil wechseln …** und **Profile verwalten …**. Details dazu stehen auf
der Seite [Profile (Arbeitsbereiche)](../profiles.md) — Profilname,
Arbeitsverzeichnis und Webserver-Port werden dort gepflegt.

### Darstellung

| Einstellung | Optionen | Wirkung |
|---|---|---|
| **Sprache** | Deutsch, Englisch, Italienisch, Spanisch, Polnisch, Chinesisch | Sprache der gesamten Oberfläche. |
| **Schriftgröße** | Normal, Groß | Größere Schrift für bessere Lesbarkeit an großen oder weit entfernten Bildschirmen. Wirkt beim Umschalten sofort als Vorschau. |
| **Design** | Flach, Neumorph | Erscheinungsbild der Oberfläche (flache Flächen oder weiche, plastische Karten). Wirkt beim Umschalten sofort als Vorschau. |

!!! info "Sprachwechsel startet Herzog CAB neu"
    Damit alle Texte vollständig in der neuen Sprache geladen werden,
    startet ein Sprachwechsel das Programm nach dem **Speichern** neu.
    Speichern Sie offene Eingaben vorher.

### Diagnose

| Einstellung | Wirkung |
|---|---|
| **Logging aktivieren** | Schreibt ein Protokoll in den Ordner `logs` im Arbeitsbereich (Datei `logs\herzogcab.log`, siehe [Speicherort](../storage-location.md)). Der Hinweis daneben: *„Nur zur Fehlersuche nötig — im Normalbetrieb ausgeschaltet lassen.“* |

!!! tip "Diagnose nur bei Bedarf"
    Das Protokoll ist nur zur Fehlersuche nötig — im Normalbetrieb
    ausgeschaltet lassen. Der [Support](../../help/support.md) bittet Sie
    ggf., es vorübergehend einzuschalten.

### Datenschutz

| Einstellung | Wirkung |
|---|---|
| **Anonyme Nutzungsstatistik senden** | Sendet anonyme, technische Nutzungsdaten, damit Herzog CAB gezielt verbessert werden kann. |

Gesendet werden ausschließlich technische Angaben, zum Beispiel:

* welche Funktionen und Berechnungen genutzt werden,
* wie oft gedruckt oder exportiert wird,
* die Anzahl der angelegten Maschinen und Benutzer,
* Programmversion, Betriebssystem und Sprache,
* wie lange das Programm genutzt wird.

Es werden **keine personenbezogenen Daten** übertragen — ein Rückschluss auf
Sie oder Ihr Unternehmen ist nicht möglich.

!!! info "Ihre Entscheidung, jederzeit änderbar"
    Beim ersten Programmstart fragt Herzog CAB einmalig um Zustimmung
    (Dialog *„Herzog CAB verbessern"*). Ihre Wahl können Sie hier jederzeit
    ändern. In der **Testversion** ist die Statistik standardmäßig
    eingeschaltet, lässt sich aber ebenfalls hier abschalten.

### Produktionsplanung

| Einstellung | Wirkung |
|---|---|
| **Produktionsstunden je Arbeitstag** | Wie viele Stunden pro Arbeitstag produziert wird (1–24 h in Halbstundenschritten, Standard **8 h**). Damit rechnet Herzog CAB die Laufzeit-Hochrechnung eines Auftrags in Kalendertage um, wenn Sie im [Flechtauftrag](../../orders/braiding-order.md#tab-auftrag) oder [Spulauftrag](../../orders/winding-order.md) das **Produktionsende aus der Hochrechnung übernehmen**. Wochenenden werden dabei übersprungen. |

### Flechtwinkel

Den Flechtwinkel kann man auf zwei Arten angeben: Herzog misst ihn gegen
die **Querrichtung** des Geflechts, die Fachliteratur meist gegen die
**Geflechtsachse**. Beide Angaben ergänzen sich zu 90° — ein Winkel von 30°
zur Querrichtung sind 60° zur Geflechtsachse; bei 45° sind beide gleich.
Mit dieser Karte legen Sie fest, in welchem Bezug Herzog CAB den
Flechtwinkel anzeigt und Eingaben erwartet.

| Einstellung | Optionen | Wirkung |
|---|---|---|
| **Flechtwinkel messen** | *Zur Querrichtung (Herzog)* (Standard), *Zur Geflechtsachse (Fachliteratur)* | Bezug aller Flechtwinkel-Anzeigen und -Eingaben im Programm. Der Kurzhinweis an jedem Eintrag zeigt ein Erklärbild des Bezugs. Gilt ab **Speichern**; offene Seiten zeigen den neuen Bezug sofort. |

**Was der Bezug ändert** — überall nur die **Anzeige und Eingabe**, nicht die
gespeicherten Daten:

* **Berechnungen:** jedes Flechtwinkel-Feld und jedes Flechtwinkel-Ergebnis,
  z. B. in [Flechtwinkel](../../calculations/product/braid-angle.md),
  [Flechtwinkel über Abzug](../../calculations/product/braid-angle-takeup.md),
  [Geflechtsdichte](../../calculations/product/lay-length.md),
  [Produktdurchmesser](../../calculations/product/product-diameter.md),
  [Produktgewicht](../../calculations/product/rope-weight.md),
  [Kern-Mantel-Produkt](../../calculations/product/core-sheath.md), den
  [Hohlgeflecht](../../calculations/tubular-braid/index.md)-Seiten und dem
  Ausdruck der Berechnungsseiten. Im Hohlgeflecht-Schema liegt die
  Bezugslinie bei *Querrichtung* waagerecht, bei *Geflechtsachse* senkrecht.
* **Designer:** das Feld und der Regler **Flechtwinkel** im
  [Parameter-Panel](../../designer/parameters.md#flechtwinkel) und die
  Vorgabe für neue Designs im Tab [Design](legacy-import.md). Der Regler
  bleibt so gerichtet, dass nach rechts ein größerer angezeigter Wert
  folgt.
* **Auftrag:** das Feld **Flechtwinkel** im
  [Flechtauftrag](../../orders/braiding-order.md).
* **Ausdrucke:** Design-Ausdruck und Platzhalter für den Flechtwinkel in
  [Druckvorlagen](../../print-templates/elements.md), die Winkel-Spalte der
  Design-Bibliothek und die mobile Ansicht des
  [Webservers](web-server.md).

Herzog CAB speichert den Flechtwinkel intern immer gleich. Wechseln Sie den
Bezug, wird nichts umgerechnet oder überschrieben — Aufträge, Designs und
Druckvorlagen zeigen denselben Winkel nur im anderen Bezug. Die
Feldbeschriftungen nennen den Bezug nicht; zeigen Sie mit der Maus auf ein
Flechtwinkel-Feld, nennt der Kurzhinweis beide Werte, z. B. *30,0° zur
Querrichtung (Herzog) = 60,0° zur Geflechtsachse (Fachliteratur)*.

!!! info "Mit Kundenkonto gilt die Wahl für Ihren Benutzer"
    Melden Sie sich über das [Kundenkonto](../../setup/account.md) an,
    speichert Herzog CAB die Wahl zusätzlich bei Ihrem Benutzer im Konto und
    holt sie beim Programmstart von dort — so gilt sie auf jedem Rechner,
    an dem Sie sich anmelden, und in der [Web-App](../../web/settings.md).
    Ohne Verbindung gilt die zuletzt bekannte Wahl. Bei
    Dongle-Installationen gilt die Einstellung für diesen Rechner.

## Verwandte Seiten

* [Einstellungen (Dialog)](index.md) — Überblick über alle Tabs
* [Profile (Arbeitsbereiche)](../profiles.md)
* [Speicherort](../storage-location.md) — wo Arbeitsbereich und Protokoll liegen
* [Flechtwinkel (Berechnung)](../../calculations/product/braid-angle.md)
