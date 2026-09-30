# Versionshinweise

!!! abstract "Referenz — Was sich in welcher Version geändert hat"

## Version 2.1.0 (September 2026)

### Neu

* **Floating-Lizenzen** – das Programm und Herzog CAB Web teilen sich die
  Plätze des Kontos. Jeder Rechner, auf dem Herzog CAB läuft, belegt einen
  Platz und gibt ihn beim Beenden sofort frei (nach einem Absturz
  spätestens nach 15 Minuten). Wer in Herzog CAB Web arbeitet, belegt
  ebenfalls einen Platz, bis 15 Minuten nach der letzten Aktivität — wer im
  Programm und im Browser zugleich arbeitet, belegt also zwei. Sind alle
  Plätze belegt, zeigt Herzog CAB, wer gerade arbeitet; im Lizenz-Tab
  steht, wie viele Plätze belegt sind. Siehe
  [Lizenz und Cloud](../admin/settings/license.md).
* **Angemeldet bleiben** – der Anmeldedialog hat ein Häkchen
  *Angemeldet bleiben*, voreingestellt an. Herzog CAB startet auf diesem
  Rechner dann ohne erneute Anmeldung. Gespeichert wird kein Passwort,
  sondern eine verschlüsselte Kennung für diesen Benutzer auf diesem
  Rechner; sie verfällt 30 Tage nach der letzten Nutzung. Abmelden im
  Programm, ein neues Passwort oder das Sperren des Rechners im
  Lizenzportal beenden sie. Siehe
  [Anmelden und Lizenz beziehen](../setup/activate-license.md).
* **Speicherort der Firma** – das Kundenkonto merkt sich den Ordner auf
  Ihrem Dateiserver, in dem Ihre Firma mit Herzog CAB arbeitet. Ein neuer
  Rechner zeigt ihn nach der Anmeldung an und verbindet sich mit einem
  Klick. Der erste Rechner einer Firma wählt einmal zwischen *Nur auf
  diesem Rechner* und einem Netzlaufwerk; unter *Systemverwaltung >
  Speicherort* zieht ein lokales Arbeitsverzeichnis auf ein Netzlaufwerk
  um. Siehe [Speicherort](../admin/storage-location.md).
* **Aufwickler als eigene Maschinenart** – eigene Stammdatenseite und
  eigener Anlegedialog mit Trommelmaßen, Traglast, Zugregelung, Bild und
  Dokumenten, eigener Filter im Maschinenpark und eigene Gruppe im
  Hallenplan. Baureihen AW, AWS, AWST, AWSP, AWSA und AWH. Siehe
  [Aufwickler](../master-data/take-up-machines.md).
* **Abwickler als eigene Maschinenart** – für Material wie Seele, Seil
  oder Kabel, das von einer Trommel in die nachfolgende Maschine abläuft:
  Trommelmaße, Traglast, Trommelhub und Abwickelspannung. Baureihen AB,
  ABS, ABST und ABA. Siehe [Abwickler](../master-data/pay-off-machines.md).
* **Gatter als eigene Maschinenart** – Ablaufgatter und Ablaufgestelle mit
  Ablaufstellen (gesamt und davon aktiv), Abzug, Antrieb, Spulenart und
  -größe, Fadenspannung, Überwachung und Material. Baureihen GU, GR, GRP,
  GRG, GM, GMG, GS, EGA, VG und AL. Siehe [Gatter](../master-data/creels.md).
* **Trommel-Datenbank** – Trommeln einmal anlegen und in Berechnungen
  wiederverwenden. Herzog-Trommeln übernehmen Sie aus dem Herzog-Katalog,
  eigene kommen daneben. Das Spulvolumen wird aus Wickeldurchmesser,
  Kerndurchmesser und Verlegeweite hergeleitet und bleibt überschreibbar.
  *Produktlänge pro Trommel* wählt die Trommel jetzt aus der Datenbank,
  statt drei Maße abzufragen. Siehe [Trommeln](../master-data/drums.md).
* **Trommel- und Aufwicklerwahl** – eine neue Berechnung führt von der
  Klöppelbestückung bis zum Aufwickler: Produktlänge und -gewicht, der
  Trommelvorschlag aus der Trommel-Datenbank und die passenden Aufwickler
  aus dem Maschinenpark oder dem Herzog-Katalog. Passt nicht alles auf eine
  Trommel, wird aufgeteilt; Füllgrad und Randabstand sind einstellbar.
  Fehlt eine Angabe, sagt die Berechnung *nicht prüfbar* statt
  stillschweigend *passt*; eine Seele zählt wie bei *Kern-Mantel-Produkt*
  zum Gewicht. Siehe
  [Trommel- und Aufwicklerwahl](../calculations/product/drum-take-up-selection.md).
* **Aufwickler und Trommel im Auftrag** – neuer Tab
  [Aufwicklung](../orders/braiding-order.md#tab-aufwicklung) im
  Flechtauftrag: Aufwickler und Trommel werden mit dem Auftrag gespeichert,
  die Auftragslänge wird je Kopf auf die Trommeln aufgeteilt (auch mit
  vorgegebener Lieferlänge je Trommel) und gegen den Aufwickler geprüft.
  **Vorschlag berechnen** sucht beides. Die Angaben erscheinen in der
  Übersicht, in der Webansicht und als Platzhalter in den Druckvorlagen;
  eine Seele zählt zum Metergewicht, zur Traglast und zum Gesamtgewicht
  im Tab **Produktion**.
* **Herzog-Katalog** – der neue Punkt **Katalog** direkt unter dem
  Maschinenpark zeigt die Herzog-Maschinen aller Arten, Klöppelspulen mit
  Artikelnummer sowie Trommeln und Haspeln, mit Reitern, Suche, Baureihe,
  Kacheln oder Liste. Maschinen legen Sie dort mit Abzug, Besetzung und
  Zubehör direkt als eigene Maschine an, bei Flechtmaschinen auf Wunsch
  samt passender Spule; Spulen und Trommeln übernehmen Sie mit einem Klick
  in die Stammdaten, auch über **Aus Herzog-Katalog …**. Das Zubehör steht
  in allen Maschinendialogen der Stammdaten, bei Flechtmaschinen auch der
  Abzug; Maschinen ohne Bild holen es sich über **Bild aus Katalog
  übernehmen**. Siehe [Herzog-Katalog](../catalog/index.md).
* **Druckvorlagen aus Herzog CAB Web** – Vorlagen, die im
  [Druck Editor der Web-App](../web/print-editor.md) angelegt oder
  geändert werden, kommen jetzt auch ins Programm zurück. Löscht man im Web
  die angepasste Fassung einer Standard-Druckvorlage, gilt im Programm
  wieder die mitgelieferte.

### Verbesserungen

* **Ein Kontingent, auch so angezeigt** – ein Abo gilt für das Programm
  und Herzog CAB Web zusammen; der Lizenz-Tab zeigt *Vollversion (Programm
  und Web)*, Herzog CAB Web nennt die Edition.
* **Maschinenseiten öffnen schneller** – Flechtmaschinen, Spulmaschinen,
  Auf- und Abwickler sowie Gatter bauen ihre Karten erst, wenn sie ins
  Bild kommen.

### Fehlerbehebungen

* **Produktgewicht zählt die Fachung** – die Berechnung
  [Produktgewicht](../calculations/product/rope-weight.md) hat ein Feld
  **Fachung**; die Feinheit gilt wie auf allen anderen Seiten für einen
  Faden. Bisher kam bei gefachten Garnen zu wenig Gewicht heraus, auch im
  Auftrag, der die Fachung jetzt aus dem Tab **Material** übernimmt.
* **Design aus dem Auftrag** – jedes Speichern im Fenster *Neues Design*
  oder *Design öffnen* eines Auftrags verknüpft das Design mit dem
  Auftrag, auch wenn das Fenster danach mit **Schließen** verlassen wird.
  Siehe [Flechtauftrag, Tab „Design"](../orders/braiding-order.md#tab-design).

### Kompatibilität

* **Neue Arbeitsverzeichnisse starten ohne mitgelieferte Spulen und
  Trommeln** – übernehmen Sie sie aus dem Herzog-Katalog. Vorhandene
  Arbeitsverzeichnisse bleiben unverändert.

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
