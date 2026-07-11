# Versionshinweise

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
* **Quadratgeflecht und Packungsgeflecht im Designer** – zwei neue
  Geflechtarten mit eigenen Besetzungsvarianten und Gangbahn-Animation.
* **Gangbahn-Animation** – der Designer zeigt jetzt animiert, wie sich die
  Klöppel durch die Maschine bewegen und das Geflecht Lage für Lage
  entsteht, mit Geschwindigkeits-Buttons. Verfügbar für Rund-, Quadrat-,
  Packungs- und Litzengeflecht.
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
* **Druck-Editor** – Datentabellen sind jetzt in Allgemein, Flechterei und
  Spulerei unterteilt.
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
