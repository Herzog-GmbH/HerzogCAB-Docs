# Trommel- und Aufwicklerwahl

!!! abstract "Referenz — Berechnung: von der Klöppelbestückung zu Produktlänge und -gewicht, dazu der Trommelvorschlag aus den Trommel-Stammdaten und die passenden Aufwickler"

## Wofür

Diese Berechnung führt in einem Schritt von der Klöppelbestückung bis zum
Aufwickler. Aus Spule, Material, Feinheit, Fachung, Klöppelzahl und
Flechtwinkel entstehen Produktlänge und -gewicht wie in den übrigen
Berechnungen, mit dem Produktdurchmesser der Platzbedarf. Daraus schlägt
die Seite Trommeln aus Ihren [Trommel-Stammdaten](../../master-data/drums.md)
vor und nennt die Aufwickler, die Trommelmaße, Produktdurchmesser und
Gewicht tragen — aus Ihrem Maschinenpark oder aus dem
[Herzog-Katalog](../../catalog/index.md). Passt das Produkt nicht auf eine
Trommel, teilt die Seite es auf mehrere auf.

!!! info "Neu ab Version 2.1.0"
    Die Berechnung steht unter *Berechnungen > Produkt*. Voraussetzung sind
    Trommeln in den [Stammdaten](../../master-data/drums.md) und —
    für die Quelle *Maschinenpark* — angelegte
    [Aufwickler](../../master-data/take-up-machines.md).

## Eingabewerte

Die Eingaben sind in vier Abschnitte gegliedert.

### Geflecht

| Feld | Einheit / Auswahl | Bedeutung |
|---|---|---|
| **Klöppelspule:** | – | Spule aus den [Spulen-Stammdaten](../../master-data/bobbins.md). Ihr Spulvolumen bestimmt, wie viel Garn auf eine Spule passt. |
| **Material:** | – | Material aus den [Stammdaten](../../master-data/materials.md); übernimmt Dichte und Feinheit. |
| **Feinheit:** | tex, dtex, den, Nr_metrisch, Nr_englisch | Feinheit eines Fadens. |
| **Dichte:** | g/cm³ | Dichte des Materials (drei Nachkommastellen). |
| **Fachung:** | stk. | Fäden je Klöppel; vorbelegt mit 1. |
| **Füllungsgrad der Spule:** | % | Anteil des Spulenvolumens, den das Garn ausfüllt; vorbelegt mit 70 %. Zusammen mit Feinheit, Dichte und Fachung ergibt das die Fadenlänge je Spule, wie bei [Materiallänge auf Spule](../material/material-length.md). |
| **Klöppelanzahl:** | stk. | Anzahl der Klöppel. |
| **Flechtwinkel:** | ° | Flechtwinkel des Geflechts. |
| **Produktdurchmesser:** | mm | Zählt für den Platz auf der Trommel, für die Prüfung der Aufwickler und — mit Seele — für deren Durchmesser. Länge und Gewicht des Mantels kommen aus Material, Feinheit und Flechtwinkel. |

### Seele

Nur für Produkte mit Seele, etwa ein Kern-Mantel-Seil. Die Angaben unter
*Geflecht* gelten dann für den Mantel; die Seele zählt nur zum Gewicht, die
Länge liefern die Mantelspulen.

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Anteil Seele:** | % | Anteil der Seele am Querschnitt des Produkts, wie bei [Kern-Mantel-Produkt](core-sheath.md). Leer lassen, wenn das Produkt keine Seele hat. |
| **Material:** | – | Material der Seele; übernimmt die Dichte. |
| **Dichte:** | g/cm³ | Dichte der Seele. Pflicht, sobald ein Anteil eingetragen ist. |
| **Füllungsgrad:** | % | Füllungsgrad der Seele wie bei *Kern-Mantel-Produkt*; vorbelegt mit 65 %. Pflicht, sobald ein Anteil eingetragen ist. |

### Trommel

| Feld | Einheit | Bedeutung |
|---|---|---|
| **Füllgrad auf der Trommel:** | % | Anteil des Trommelvolumens, den das Geflecht ausfüllt. Das runde Geflecht lässt Hohlräume; üblich sind 70 bis 80 %. Vorbelegt mit 75 %. |
| **Randabstand:** | mm | Abstand der obersten Lage unter der Flanschkante. Bei 0 mm (Vorgabe) wird bis zur Flanschkante gerechnet, wie bei den Volumenangaben der Herzog-Trommeln. |

### Aufwickler

| Feld | Auswahl | Bedeutung |
|---|---|---|
| **Aufwickler aus:** | *Maschinenpark* (Vorgabe) oder *Herzog-Katalog* | Woher die Aufwickler für die Prüfung kommen: Ihre angelegten [Aufwickler](../../master-data/take-up-machines.md) oder alle Aufwickler-Modelle aus dem Herzog-Katalog. |
| **Aufteilung:** | *Gleich große Teilmengen*, *Volle Trommeln + Rest*, *Rest auf kleinerer Trommel* | Wie das Produkt verteilt wird, wenn es nicht auf eine Trommel passt (siehe unten). |

!!! note "Pflichtangaben"
    Klöppelspule, Feinheit, Dichte, Fachung (mindestens 1), Füllungsgrad
    der Spule, Klöppelanzahl, Flechtwinkel, Produktdurchmesser und Füllgrad
    auf der Trommel müssen gefüllt sein; mit Anteil Seele außerdem Dichte
    und Füllungsgrad der Seele. Fehlende Werte werden rot markiert.

## Ergebnis

| Wert | Einheit | Bedeutung |
|---|---|---|
| **Produktlänge:** | m | Produktlänge, die ein voller Spulensatz liefert (blau hervorgehoben). |
| **Trommeln:** | – | Der Trommelvorschlag, z. B. *„3 × Holztrommel … à 23,6 m + 1 × … à 11,6 m"*. Bei einem Haspelaufwickler steht dort *„Haspel des …"*. |
| **Aufwickler:** | – | Der erste passende Aufwickler je Teil, bei mehreren mit *„(+… weitere)"*. |
| **Platzbedarf auf der Trommel:** | l | Raum, den die Produktlänge beim vollen Produktdurchmesser einnimmt. |
| **Produktgewicht:** | kg | Gewicht der gesamten Produktlänge. |
| **Metergewicht:** | g/m | Gewicht je Meter, mit Seele. |
| **davon Seele:** | g/m | Anteil der Seele am Metergewicht (nur mit Seele). |
| **Gesamtgewicht je Trommel:** | – | Produkt plus Leergewicht der Trommel, je Teil des Vorschlags. Fehlt das Leergewicht, steht dort *„… kg + Leergewicht"*; bei einer Haspel *„… kg ohne Haspel"*. |
| **Prüfung:** | – | *Alle Prüfungen bestanden.* oder *Nicht prüfbar: …* mit den fehlenden Angaben (siehe unten). |

### Tabelle „Trommeln und Haspeln"

Rechts neben den Eingaben listet die Seite alle Trommeln aus den
Stammdaten und die Haspeln der Haspelaufwickler, nach Größe sortiert:

| Spalte | Bedeutung |
|---|---|
| **Trommel / Haspel** | Name der Trommel (mit Artikelnummer in Klammern, falls gepflegt) bzw. *Haspel des …*. |
| **Kapazität** | Produktlänge, die auf eine Trommel passt. |
| **Anzahl** | Trommeln dieser Art für das ganze Produkt. |
| **Passende Aufwickler** | Bis zu drei Aufwickler, dahinter *(+…)*; alle stehen im Tooltip. |
| **Hinweis** | Warum eine Trommel nicht geht oder was fehlt (siehe unten). |

Blau hinterlegt ist der Vorschlag; Trommeln, die zu keinem Aufwickler
passen, sind grau.

## Bedienung

Der gemeinsame Aufbau aller Berechnungsseiten steht in
[So sind Berechnungsseiten aufgebaut](../../basics/calc-page-anatomy.md).
Die Trommeln liest die Seite bei jeder Berechnung neu aus den Stammdaten —
Änderungen im Trommel-Editor wirken sofort.

### Der Vorschlag

Passt das ganze Produkt auf eine Trommel, schlägt die Seite die kleinste
passende Trommel vor. Sonst teilt sie nach der gewählten **Aufteilung**:

| Aufteilung | Ergebnis |
|---|---|
| **Gleich große Teilmengen** | Die Trommelart mit den wenigsten Trommeln (bei Gleichstand die kleinere); das Produkt wird gleichmäßig auf alle verteilt. |
| **Volle Trommeln + Rest** | Dieselbe Trommelart; alle Trommeln bis auf die letzte werden voll gewickelt, der Rest kommt auf eine weitere Trommel derselben Art. |
| **Rest auf kleinerer Trommel** | Volle Trommeln einer Art, der Rest auf die kleinste Trommel, die ihn aufnimmt. Gewählt wird die Lösung mit den wenigsten Trommeln, bei Gleichstand die mit dem kleineren Gesamtvolumen. |

Die Kapazität einer Trommel folgt aus ihrem Spulvolumen in den
Stammdaten, dem **Füllgrad auf der Trommel** und dem **Randabstand**. Bei
einer Haspel zählt das Haspelvolumen des Aufwicklers; einen Randabstand
gibt es dort nicht. Begrenzt die Traglast eines Aufwicklers die Länge je
Trommel, rechnet die Seite mit der kürzeren Länge.

### Was geprüft wird

Für jeden Aufwickler vergleicht die Seite Trommel-Außendurchmesser,
Trommelbreite, Produktdurchmesser und das Gewicht von Produkt und leerer
Trommel mit seinen Grenzen — die Einzelheiten stehen unter
[Aufwickler](../../master-data/take-up-machines.md#welche-angaben-gepruft-werden).
Haspelaufwickler nehmen keine Trommel auf; bei ihnen zählen nur
Produktdurchmesser und Traglast.

!!! warning "Nicht prüfbar statt stillschweigend passend"
    Fehlt eine Angabe, sagt die Berechnung *nicht prüfbar*, statt eine
    Trommel als passend auszugeben. Mögliche Gründe:
    *Trommeldurchmesser des Aufwicklers fehlt*, *Verlegebreite des
    Aufwicklers fehlt*, *Traglast des Aufwicklers fehlt*,
    *Leergewicht der Trommel fehlt*, *Metergewicht fehlt*. Aufwickler mit
    fehlenden Angaben bleiben im Vorschlag, stehen aber hinter denen, die
    sicher passen.

In der Spalte **Hinweis** der Tabelle erscheinen:

| Hinweis | Bedeutung |
|---|---|
| *Kein Aufwickler nimmt diese Trommel auf* | Die Trommelmaße passen zu keinem Aufwickler. |
| *Passt nicht* | Eine Haspel fasst das Produkt nicht. |
| *Produktdurchmesser passt zu keinem Aufwickler* | Die Trommel passt, das Produkt ist zu dünn oder zu dick. |
| *Zu schwer für jeden Aufwickler* | Maße und Produkt passen, das Gewicht nicht. |
| *Traglast: höchstens … m je Trommel* | Die Traglast begrenzt die Länge auf dieser Trommel. |
| *Leergewicht fehlt* | Die Trommel hat kein Leergewicht in den Stammdaten. |

### Meldungen ohne Vorschlag

| Meldung unter **Prüfung** | Abhilfe |
|---|---|
| *Im Maschinenpark ist kein Aufwickler angelegt. Als Quelle den Herzog-Katalog wählen.* | Aufwickler anlegen oder **Aufwickler aus:** *Herzog-Katalog* wählen. |
| *In den Trommeln ist noch keine angelegt. Übernehmen Sie sie unter Stammdaten → Trommeln mit "Aus Herzog-Katalog …".* | Trommeln in den [Stammdaten](../../master-data/drums.md) anlegen oder aus dem Katalog übernehmen. Neue Arbeitsverzeichnisse starten ab Version 2.1.0 ohne Trommeln. |
| *Das Produkt passt in den Wickelraum keiner Trommel.* | Größere Trommel anlegen oder Produktdurchmesser prüfen. |
| *Keine Trommel passt zu einem der Aufwickler. Hinweise stehen in der Tabelle.* | Die Spalte **Hinweis** nennt den Grund je Trommel. |

## Berechnung

> Die genaue Berechnungsformel ist nicht Bestandteil dieser Dokumentation.

## Verwandte Berechnungen

- [Produktlänge pro Trommel](rope-length-on-drum.md)
- [Produktgewicht](rope-weight.md)
- [Kern-Mantel-Produkt](core-sheath.md)
- [Materiallänge auf Spule](../material/material-length.md)
- [Maschinenlaufzeit pro Spule-Satz](../production/run-time-bobbin-set.md)
- Im Auftrag: [Flechtauftrag, Tab „Aufwicklung"](../../orders/braiding-order.md#tab-aufwicklung)
