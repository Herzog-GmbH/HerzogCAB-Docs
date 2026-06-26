# F1-Kontexthilfe: Zuordnung App-Key → Handbuch-Seite

Diese Datei ordnet die **internen Navigations-/Berechnungs-Keys** von Herzog CAB
(aus `mainwindow.cpp` bzw. `calculations_overview.cpp`) den Seiten dieses
Handbuchs zu. Sie ist die Grundlage für die **F1-Kontexthilfe**: Drückt der
Bediener auf einer Seite F1, öffnet die App `BASIS_URL + Pfad` des aktuellen Keys.

**Basis-URL:** `https://cab.herzog-online.com/handbuch/`
(lokal: `http://127.0.0.1:8800/handbuch/`)

> Diese Datei ist **nicht** Teil des gebauten Handbuchs (liegt im Repo-Root, nicht unter `docs/`).

## Module / Navigation

| App-Key | Bildschirm | Handbuch-Pfad |
|---|---|---|
| `home` | Startseite | `getting-started/interface/` |
| `uiJobs` / `jobs` | Aufträge | `orders/` |
| `machinePark` | Maschinenpark | `master-data/machine-park/` |
| `productionLayout` | Hallenplaner | `master-data/hall-planner/` |
| `uiDesigner` / `designs` | Designer | `design/designer/` |
| `calculations` | Berechnungen (Übersicht) | `calculations/` |
| `masterdata` | Stammdaten (Übersicht) | `master-data/` |
| `uiCustomers` | Kunden | `master-data/customers/` |
| `uiProduct` | Designs (Stammdaten) | `design/index/` |
| `braidingMachines` / `braiding_machines` | Flechtmaschinen | `master-data/machines/` |
| `floorPlans` | Grundrisse | `master-data/floor-plans/` |
| `mediaLibrary` | Medien | `master-data/media/` |
| `materials` | Materialien | `master-data/materials/` |
| `bobbins` | Spulen | `master-data/bobbins/` |
| `uiColors` | Farben | `master-data/colors/` |
| `output` / `uiPrintEditor` | Druck Editor | `print-templates/` |
| `experts` / `parameterExplorer` | Parameter-Übersicht | `master-data/parameter-overview/` |
| `systemAdmin` | Systemverwaltung | `users/` |
| `userManagement` | Benutzer | `users/manage/` |
| `roleManagement` | Rollen | `users/roles/` |
| `profileManagement` | Profile | `workspace/concept/` |
| `companyData` | Firma | `settings/company/` |

## Berechnungen

| App-Key | Bildschirm | Handbuch-Pfad |
|---|---|---|
| `linearDensity` | Feinheit / Titer | `calculations/material/linear-density/` |
| `conversionOfLinearDensity` | Umrechnung Feinheit | `calculations/material/linear-density-conversion/` |
| `materialDiameter` | Materialdurchmesser über Material | `calculations/material/material-diameter/` |
| `requiredMaterial` | Materialdurchmesser über Produkt | `calculations/material/material-diameter/` |
| `requiredPly` | Fachung über Produkt | `calculations/material/material-diameter/` |
| `coreCoverProduct` | Kern-Mantel-Produkt | `calculations/material/core-sheath/` |
| `bobinVolume` | Spulvolumen | `calculations/bobbins/bobbin-volume/` |
| `materialLengthOnBobbin` | Materiallänge auf Spule | `calculations/bobbins/material-length/` |
| `numberOfWindingMachines` | Anzahl Spulmaschinen | `calculations/bobbins/number-of-winders/` |
| `braidAngle` | Flechtwinkel | `calculations/braid-geometry/braid-angle/` |
| `layLength` | Geflechtsdichte | `calculations/braid-geometry/lay-length/` |
| `conversionOfBraidDensity` | Umrechnung Geflechtsdichte | `calculations/braid-geometry/picks-density/` |
| `productDiameter` | Produktdurchmesser | `calculations/product/product-diameter/` |
| `productLength` | Produktlänge | `calculations/product/rope-length/` |
| `productLengthOnDrum` | Produktlänge pro Trommel | `calculations/product/rope-length-on-drum/` |
| `productWeight` | Produktgewicht | `calculations/product/rope-weight/` |
| `numberOfCarriers` | Hohlgeflecht – Anzahl Klöppel | `calculations/tubular-braid/tube-carriers/` |
| `diameter` | Hohlgeflecht – Durchmesser | `calculations/tubular-braid/tube-diameter/` |
| `materialWidth` | Hohlgeflecht – Materialbreite | `calculations/tubular-braid/yarn-width/` |
| `covering` | Hohlgeflecht – Bedeckung | `calculations/tubular-braid/tube-cover/` |
| `productionSpeed` | Produktionsgeschwindigkeit | `calculations/machine/production-speed/` |
| `machineDimensons` | Maschinen-Dimensionierung | `calculations/machine/dimensions/` |
| `machineRunningTimePerBobbinSet` | Maschinenlaufzeit pro Spulensatz | `calculations/machine/run-time-bobbin-set/` |
| `changeGearRubberFeedDevice` | Wechselräder Gummibandkette | `calculations/machine/change-gears/` |

## Maschinenlesbar (JSON)

```json
{
  "home": "getting-started/interface/",
  "uiJobs": "orders/", "jobs": "orders/",
  "machinePark": "master-data/machine-park/",
  "productionLayout": "master-data/hall-planner/",
  "uiDesigner": "design/designer/", "designs": "design/designer/",
  "calculations": "calculations/",
  "masterdata": "master-data/",
  "uiCustomers": "master-data/customers/",
  "uiProduct": "design/index/",
  "braidingMachines": "master-data/machines/", "braiding_machines": "master-data/machines/",
  "floorPlans": "master-data/floor-plans/",
  "mediaLibrary": "master-data/media/",
  "materials": "master-data/materials/",
  "bobbins": "master-data/bobbins/",
  "uiColors": "master-data/colors/",
  "output": "print-templates/", "uiPrintEditor": "print-templates/",
  "experts": "master-data/parameter-overview/", "parameterExplorer": "master-data/parameter-overview/",
  "systemAdmin": "users/",
  "userManagement": "users/manage/",
  "roleManagement": "users/roles/",
  "profileManagement": "workspace/concept/",
  "companyData": "settings/company/",
  "linearDensity": "calculations/material/linear-density/",
  "conversionOfLinearDensity": "calculations/material/linear-density-conversion/",
  "materialDiameter": "calculations/material/material-diameter/",
  "requiredMaterial": "calculations/material/material-diameter/",
  "requiredPly": "calculations/material/material-diameter/",
  "coreCoverProduct": "calculations/material/core-sheath/",
  "bobinVolume": "calculations/bobbins/bobbin-volume/",
  "materialLengthOnBobbin": "calculations/bobbins/material-length/",
  "numberOfWindingMachines": "calculations/bobbins/number-of-winders/",
  "braidAngle": "calculations/braid-geometry/braid-angle/",
  "layLength": "calculations/braid-geometry/lay-length/",
  "conversionOfBraidDensity": "calculations/braid-geometry/picks-density/",
  "productDiameter": "calculations/product/product-diameter/",
  "productLength": "calculations/product/rope-length/",
  "productLengthOnDrum": "calculations/product/rope-length-on-drum/",
  "productWeight": "calculations/product/rope-weight/",
  "numberOfCarriers": "calculations/tubular-braid/tube-carriers/",
  "diameter": "calculations/tubular-braid/tube-diameter/",
  "materialWidth": "calculations/tubular-braid/yarn-width/",
  "covering": "calculations/tubular-braid/tube-cover/",
  "productionSpeed": "calculations/machine/production-speed/",
  "machineDimensons": "calculations/machine/dimensions/",
  "machineRunningTimePerBobbinSet": "calculations/machine/run-time-bobbin-set/",
  "changeGearRubberFeedDevice": "calculations/machine/change-gears/"
}
```
