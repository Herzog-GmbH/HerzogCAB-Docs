# F1-Kontexthilfe: Zuordnung App-Key → Handbuch-Seite

**Kanonische, maschinenlesbare Quelle ist [`f1-mapping.json`](f1-mapping.json)** (Repo-Root).
Diese Markdown-Datei ist nur die menschenlesbare Erläuterung dazu.

Drückt der Bediener in Herzog CAB ++f1++, ermittelt die App über
`resolveHelpContextKey()` (mainwindow.cpp) den Nav-Key des aktiven Moduls und
öffnet `Basis-URL + Pfad` aus der JSON-Tabelle im Standardbrowser.

* **Basis-URL online:** `https://cab.herzog-online.com/handbuch/`
* **Basis-URL lokal (Vorschau/Offline-Bündel):** `http://127.0.0.1:8800/handbuch/`
* **Fallback:** leerer oder unbekannter Key → Handbuch-Startseite (leerer Pfad).

> Diese Dateien sind **nicht** Teil des gebauten Handbuchs (Repo-Root, nicht unter `docs/`).
> Die App erhält eine vendored Kopie der JSON als Qt-Ressource (`Resources/help/f1-mapping.json`).

## Pflege-Regeln

1. Seite im Handbuch verschoben/umbenannt → Pfad in `f1-mapping.json` anpassen
   **und** Redirect in `mkdocs.yml` ergänzen.
2. Neues Modul / neue Berechnung in der App → neuen Key mit Zielseite eintragen.
3. Der CI-Workflow (`.github/workflows/docs.yml`) validiert nach jedem Build,
   dass **jeder** Pfad der JSON auf eine real gebaute Seite zeigt — sonst ist der
   Build rot.
4. Die vendored Kopie in der App beim nächsten App-Release aktualisieren.

## Struktur der Zuordnung (Stand Neuaufbau 07/2026)

| Bereich | Keys (Auszug) | Ziel |
|---|---|---|
| Startseite/Navigation | `home`, `favorites` | `basics/…` |
| Aufträge | `uiJobs`/`jobs`, `jobEditor`, `windingOrderEditor` | `orders/…` |
| Maschinenpark | `machinePark` | `machine-park/` |
| Hallenplaner | `productionLayout`, `productionLayoutEditor` | `hall-planner/…` |
| Designer | `uiDesigner`, `designs`, `designer` | `designer/` |
| Berechnungen (Gruppen) | `calculations`, `material`, `product`, `hollowBraid`, `production`, `windingCalcs` | `calculations/…` |
| Berechnungen (32 Rechner) | `braidAngle`, `windingTime`, … | je eigene Seite |
| Stammdaten | `masterdata`, `uiCustomers`, `uiProduct`, `braidingMachines`, `windingMachines`, `floorPlans`, `mediaLibrary`, `materials`, `bobbins`, `uiColors` | `master-data/…` |
| Druck-Editor | `output`/`uiPrintEditor` | `print-templates/` |
| Parameter-Übersicht | `experts`/`parameterExplorer` | `parameter-overview/` |
| Verwaltung | `systemAdmin`, `userManagement`, `roleManagement`, `loginSettings`, `profileManagement`, `storageLocation`, `companyData`, `settingsDialog` | `admin/…` |

Die vollständige Liste steht ausschließlich in `f1-mapping.json` — bitte dort
nachsehen und pflegen, damit es keine zwei Wahrheiten gibt.
