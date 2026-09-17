# Versionshinweise

!!! abstract "Referenz — Was sich in welcher Version geändert hat"

## Version 2.0.0 (September 2026)

### Neu

* **Kundenkonto statt Dongle** – Herzog CAB lässt sich auf jedem Rechner
  installieren; beim ersten Start meldet sich das Programm am Kundenkonto
  Ihrer Firma an und zieht seine Lizenz aus dem Vorrat des Kontos. Ein Platz
  je Baustein und Rechner; ein Rechner, der nicht mehr gestartet wird, gibt
  seinen Platz nach sieben Tagen von selbst zurück. Siehe
  [Kundenkonto und Einladung](../setup/account.md).
* **Ein Login für alles** – der Kontobenutzer ist zugleich der
  Programmbenutzer: dieselbe E-Mail-Adresse und dasselbe Passwort in der
  Desktop-App, im Lizenzportal und in der Web-App, auf Wunsch mit zweitem
  Faktor (Authenticator-App). Rollen kommen aus dem Konto.
* **Offline arbeiten** – nach der Anmeldung läuft das Programm ohne Netz
  normalerweise bis zu sieben Tage; über *Einstellungen > Lizenz* lässt sich
  eine Offline-Miete für bis zu 30 Tage ziehen.
* **Lizenzportal** – Bausteine und belegte Plätze, Rechner freigeben oder
  sperren, Kollegen einladen, Lizenzen anfragen oder verlängern, neueste
  Version herunterladen: [license.herzog-cab.com](https://license.herzog-cab.com).
* **Herzog CAB Web** – das komplette Programm im Browser unter
  [app.herzog-cab.com](https://app.herzog-cab.com): Aufträge, Berechnungen,
  Designer mit allen Geflechtsarten und 3D, Maschinen mit Katalog,
  Stammdaten, Hallenplaner 2D/3D, Druck als PDF, Rollen und Import — auch am
  Tablet und Smartphone. Eigener Abo-Baustein, 30 Tage kostenlos testbar.
  Siehe [Web-App](../web/index.md).
* **Cloud-Upload** – die Desktop-App lädt ihr Arbeitsverzeichnis auf Wunsch
  automatisch in die Web-App hoch (*Einstellungen > Lizenz*).
* **Echte 3D-Ansicht im Designer** – der Schalter **3D** zeigt das Geflecht
  als räumliches Modell aus den Klöppelbahnen, für alle sechs
  Geflechtsarten, mit Draufsicht, Seitenansicht und Flechtpunkt, Material,
  Darstellung und Ausrichtung. Die bisherigen Projektionen heißen jetzt
  **Zylinder**, **Vierkant** und **Kante**.
* **Tab „Lizenz" in den Einstellungen** – Konto, angemeldeter Benutzer,
  Edition, Bausteine, Miete mit Ablaufdatum sowie *Miete jetzt verlängern*,
  *Offline-Miete ziehen*, *Von diesem Rechner abmelden* und der
  Cloud-Upload.

### Verbesserungen

* **Ein Installer** für Vollversion, Designer-Edition und Testversion — die
  Bausteine des Kontos entscheiden.
* **Benutzerverwaltung im Kontomodell** – Benutzer und Rollen kommen aus
  dem Kundenkonto (*Vom Kundenkonto aktualisieren*); lokal bleibt die
  Zuweisung zu Profilen.
* **Lizenzportal auf Englisch**, Ablauf-Erinnerungen 30 und 7 Tage vor dem
  Ende einer Freischaltung, Vertriebsrolle bei Herzog.

### Kompatibilität

* **Bestandskunden mit Dongle oder CmAct-Lizenz ändern nichts** – der Dongle
  bleibt gültig, die lokale Benutzerverwaltung samt Microsoft Entra ID und
  LDAP bleibt. Das Kontomodell greift nur, wenn kein CodeMeter-Container
  vorhanden ist.

## Version 1.4.6 (August 2026)

### Neu

* **Flechtwinkel über Abzug** – eine neue Berechnung verbindet
  Maschineneinstellung und Geflecht: Aus Flügelraddrehzahl und Abzug ergibt
  sich der Flechtwinkel; der Abzug lässt sich als Geschwindigkeit oder über
  Abzugsscheibe und Drehzahl angeben. Umgekehrt liefert die Seite Abzug,
  Flügelraddrehzahl und Scheibendrehzahl für einen Soll-Flechtwinkel. Für
  Rund- und Litzengeflecht. Siehe
  [Flechtwinkel über Abzug](../calculations/product/braid-angle-takeup.md).
* **Favoriten auf den Rechen-Kacheln** – der Stern sitzt jetzt auf jeder
  Rechen-Kachel, überall gleich gestaltet.

### Fehlerbehebungen

* **Rollen behalten ihre Rechte** – beim Speichern einer Rolle gingen genau
  die Rechte verloren, die der Editor gerade nicht anzeigte.
* **Gesperrte Bereiche bleiben verborgen** – ein Favorit auf einen
  gesperrten Bereich blieb sichtbar, und die eingeklappte Werkzeugleiste
  zeigte Symbole für längst ausgeblendete Bereiche.
* **Update-Prüfung je Plattform** – Windows und macOS fragen wieder ihren
  eigenen Update-Kanal ab.

## Version 1.4.5 (Juli 2026)

### Neu

* **Spulerei komplett eingebunden** – Spulmaschinen sind jetzt eigene
  Stammdaten (Baureihe, Spulstellen, Spulengrößen, Drehzahl, Wickeltechnik).
  Für Spulaufträge gibt es einen eigenen Auftragstyp mit Verknüpfung zum
  Flechtauftrag, eigener Farbaufschlüsselung und Klöppeltabelle sowie neun
  neuen Berechnungen in der eigenen Gruppe **Spulerei** (Spulzeit,
  Fadengeschwindigkeit, Fadenspannung, Spulenkapazität, Spulengewicht,
  Materialbedarf, Spulen aus Liefergebinde, Restlänge über Gewicht, Anzahl
  Spulmaschinen). Der Hallenplaner gruppiert Maschinen jetzt nach Flecht- und
  Spulmaschinen, und die Startseite unterscheidet beide Auftragsarten.
* **Neue Geflechtsarten im Designer** – Quadratgeflecht (8 bis 36 Klöppel,
  Voll, Halb und Tandem), Spiralflechter (12 und 20 Klöppel),
  Packungsflechter in allen Größen mit Familienauswahl (2-, 3-, 4-bahnig und
  rund) sowie Soutachegeflecht. Jedes Flechtbild ist aus der
  Maschinenkinematik hergeleitet.
* **Gangbahn-Animation** – der Designer zeigt jetzt animiert, wie sich die
  Klöppel durch die Maschine bewegen und das Geflecht Lage für Lage
  entsteht, mit Geschwindigkeits-Buttons. Verfügbar für alle Geflechtsarten.
* **Spulzeit und Maschinenverteilung** – der Spulauftrag rechnet die
  Spulzeit hoch, zeigt den Produktionszeitraum von–bis und verteilt die
  Spulen auf mehrere Maschinen; eine Schaltfläche verteilt gleichmäßig nach
  Spulstellen. Ein Rechner ermittelt die Zielspulenzahl aus der
  Gesamtlänge. Spulaufträge sind auch ohne Flechtauftrag mit eigener
  Farb- und Materialaufschlüsselung planbar.
* **Anmeldung mit Microsoft Entra ID** öffnet jetzt ein eigenes, kompaktes
  Anmeldefenster statt eines vollen Browser-Tabs.

### Verbesserungen

* **Feinheit-Ergebnis umschaltbar** zwischen tex, dtex, den, Nm und Ne
  (Feedback #47).
* **Farbpalette im Designer** nicht mehr auf 20 Farben begrenzt und
  durchscrollbar (Feedback #45).
* **Flechtmaschinen-Stammdaten** – die möglichen Werte für Köpfe,
  Einschnitte und Klöppel richten sich jetzt nach der Maschinenkategorie
  (z. B. Soutache, Quadrat).
* **Speicherort-Verwaltung** als eigener Bereich in der Systemverwaltung.
* **Vorschau und Ansichten** – die Vorschau nennt Material, Bedeckung und
  Geflechtsdurchmesser in der Maßzeile; Voll, Halb und die Projektion sind
  Schalter in der Werkzeugleiste. Geflechtsart und Bindung sind
  Auswahllisten, die Design-Karte ist kompakt und scrollbar, und neun
  Designer-Vorgaben stehen unter *Einstellungen > Design*.
* **Druck-Editor** – die Klöppeltabelle kann eine Spalte je Gangbahn
  ausgeben, der Zellstil wechselt zwischen Farbfläche und Farbfeld, und die
  Datentabellen sind in Allgemein, Flechterei und Spulerei unterteilt.
  Spulaufträge lassen sich drucken.
* **Maschinen-Dialoge** – Feldhöhen und Beschriftungen vereinheitlicht,
  Baujahr auf gültige Jahre begrenzt, Doppelklick öffnet direkt die Bearbeitung. Der
  Einstellungen-Dialog ist scrollbar und passt sich der Bildschirmhöhe an.
* **Spulauftrag** – Berechnungen lassen sich wie beim Flechtauftrag direkt
  aus dem Eingabefeld heraus starten.

## Version 1.4.4 (30.06.2026)

### Neu

* **Weitere Anmeldemethoden** – zusätzlich zur lokalen Benutzerverwaltung
  können Sie sich jetzt über **Microsoft Entra ID** (Azure AD) und über
  **LDAP / Active Directory** anmelden. Benutzer und Gruppen lassen sich aus
  dem Verzeichnis importieren, Rollen werden automatisch anhand der
  Gruppenzugehörigkeit vergeben.

### Verbesserungen

* **Berechnungsfelder** – Felder mit Platzhalter „–" lassen sich jetzt
  direkt per Klick bearbeiten; Nachkommastellen werden korrekt übernommen.

### Fehlerbehebungen

* **Fensterfokus** – das Hauptfenster (und der 3D-Hallenansicht-Dialog)
  kommen nach dem Start bzw. Öffnen jetzt zuverlässig in den Vordergrund.

## Version 1.4.3 (24.06.2026)

### Fehlerbehebungen

* **Ausrichtleiste im Hallenplaner** – die Werkzeugleiste (Ausrichten ·
  Verteilen · Anordnen) über der Zeichenfläche behält jetzt eine feste,
  schlanke Höhe, statt den gesamten oberen Bereich zu füllen.
* **Übersetzungen im Grundriss** – Bezeichnungen im
  Hallenplaner-Grundriss (Produktionsfläche, Transportweg, Lagerfläche,
  Wartung, Büro, Qualitätskontrolle, Tür, Tor, Fenster, Treppe,
  Banner/Logo, Türstile) waren fest auf Deutsch codiert und sind jetzt in
  allen sechs Sprachen übersetzt.

## Version 1.4.2 (23.06.2026)

### Fehlerbehebungen

* **Farben in der Klöppeltabelle** *(Issue #44)* – die angezeigte Farbe
  (ID/Name/Hex/Pantone) je Klöppel konnte nach dem Rotieren der
  Design-Farben nicht mehr zur tatsächlichen Farbe passen. Das ist jetzt
  korrekt verknüpft; bereits gespeicherte Designs werden beim erneuten
  Öffnen automatisch korrigiert.
* **Tooltip der Farbpalette** – der dunkle, schwer lesbare
  Tooltip-Hintergrund auf den Farbfeldern und im Farbwähler ist behoben.

## Version 1.4.1 (23.06.2026)

### Neu

* **Hallenplaner (Produktionslayout)** – Hallen-Grundrisse zeichnen
  (Außen-/Innenwände, Flächen, Türen, Tore, Fenster, Treppen), Maschinen aus
  dem Katalog platzieren (ausrichten, gleichmäßig verteilen, anordnen,
  aneinanderreihen, drehen, duplizieren), mit Maßstab, Raster-/Winkelfang
  und Messwerkzeug.
* **3D-Hallenansicht** – der fertige Grundriss in 3D, inklusive Maschinen,
  Wandtexturen, Bannern/Logos und Live-Maschinenstatus.
* **Grundrisse als eigene Stammdaten** – ein Grundriss kann mehrere
  Belegungen/Szenarien enthalten (Ist-Zustand und Planungsvarianten) und
  wird unabhängig angelegt, umbenannt, dupliziert und verwaltet.
* **Medienbibliothek** – zentrale Verwaltung aller Bilder (Flechtmaschinen,
  Wandtexturen, Banner & Logos, Hallengrundrisse, Firmenlogo) mit Ordnern,
  Suche, Upload und Ersetzen.

### Verbesserungen

* **Maschinenpark** – neue Karten- und Listenansicht mit Statusanzeige.
* **Umschaltbares Erscheinungsbild** – neues Oberflächen-Design, wahlweise
  Flach oder Neumorph, live in den Einstellungen umschaltbar.
* Verbesserte Rollen- und Benutzerverwaltung, inklusive eigenem Recht für
  den Hallenplaner.
* Zahlreiche weitere Detailverbesserungen an der Oberfläche.

## Version 1.3.4 (April 2026)

* Druckvorlagen werden pro Datei unter `Printouts/templates/` abgelegt (Migration läuft automatisch).
* Profilbilder werden maschinenweit unter `ProgramData` gespeichert.
* Performance-Verbesserungen im Designer.

## Ältere Versionen

Vollständiger Verlauf: siehe Datei `CHANGELOG.md` im Programmverzeichnis.
