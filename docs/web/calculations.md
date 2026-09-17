# Berechnungen (Web-App)

!!! abstract "Referenz — Das Modul Berechnungen der Web-App: Rechnerübersicht mit Suche und die Rechnerseite"

## Wofür Sie diesen Bereich nutzen

Die Web-App enthält **32 Rechner in fünf Gruppen** — Material, Produkt,
Hohlgeflecht, Produktion und Spulerei. Eingaben, Auswahlfelder, Einheiten
und Ergebnisse sind dieselben wie in der Desktop-App; die Bedeutung jedes
Felds steht auf der Referenzseite des jeweiligen Rechners im Kapitel
[Berechnungen](../calculations/index.md). Diese Seite beschreibt nur die
Bedienung im Browser.

!!! info "Unterschied zur Desktop-App"
    Der Rechner **Flechtwinkel über Abzug** ist in der Web-App nicht
    enthalten. Verlauf und Favoriten gibt es im Browser nicht; stattdessen
    finden Sie jeden Rechner über die Suche. Die Formeln sind identisch.

## Rechnerübersicht

![Rechnerübersicht der Web-App: Suchfeld und Kacheln je Gruppe.](../assets/screenshots/web/berechnungen.png)

| Element | Bedeutung |
|---|---|
| **Rechner suchen …** | Filtert die Kacheln live nach dem Namen des Rechners. Passt nichts, meldet die Seite *Kein Rechner passt zu „…"*. |
| Gruppen | **Material**, **Produkt**, **Hohlgeflecht**, **Produktion**, **Spulerei** — jede mit ihren Rechner-Kacheln (Symbol, Name, Eingabefelder in Kurzform). |
| Kachel | Ein Klick öffnet die Rechnerseite. |

## Rechnerseite

![Rechnerseite der Web-App am Beispiel Flechtwinkel: Eingaben links, Ergebnis rechts.](../assets/screenshots/web/rechner-flechtwinkel.png)

| Element | Bedeutung |
|---|---|
| **Zur Übersicht** | Zurück zur Rechnerübersicht. |
| **Eingaben** | Alle Eingabefelder mit Einheit; Auswahlfelder wie *Material wählen …* und *Spule wählen …* greifen auf Ihre [Stammdaten](master-data.md) zu. Ein kleines Bild neben manchen Feldern erklärt die Größe (z. B. den Flechtwinkel). |
| **Einheit** | Wo die Desktop-App einen Einheiten-Umschalter hat (z. B. Feinheit in tex, dtex, den, Nm, Ne), gibt es ihn auch hier. |
| **Berechnen** | Führt die Berechnung aus. Fehlende oder ungültige Eingaben werden am Feld markiert. |
| **Löschen** | Setzt alle Eingaben auf die Vorgabewerte zurück. |
| **Ergebnis** | Die Ergebniswerte mit Einheit — dieselben Werte und Nachkommastellen wie am Desktop. |
| **Drucken** | Druckt Eingaben und Ergebnis über den Browser (siehe [Drucken](print.md)). |

Die Werte bleiben erhalten, solange Sie auf der Seite sind; beim Verlassen
der Seite werden sie verworfen.

!!! tip "Rechner aus dem Auftrag heraus"
    Im [Flechtauftrag](orders.md) und [Spulauftrag](orders.md) öffnen die
    Rechner-Symbole neben den Feldern denselben Rechner als Dialog —
    vorbelegt mit den Auftragswerten und mit **Übernehmen** zurück in den
    Auftrag.

## Verwandte Seiten

* [Berechnungen (Referenz aller Rechner)](../calculations/index.md)
* [So sind Berechnungsseiten aufgebaut](../basics/calc-page-anatomy.md) — Aufbau in der Desktop-App
* [Material richtig kalkulieren](../tasks/material-calculation.md)
