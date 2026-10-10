# Core-cover product

!!! abstract "Reference — Calculation: two-layer product made of core and cover"

## Purpose { #wofur }

Calculates a two-layer braided product made of a braided **core**
and a **Cover** braided over it. From the outer diameter, the
percentage split between core and cover and the braiding parameters
of both layers, the function determines geometry, strand fineness, bobbin lengths,
production and weight – separately for core and cover and as a total value.
This way you can fully calculate a core-cover product in one step.

## Inputs { #eingabewerte }

The inputs are divided into three areas: common **Product** data
and two identically structured panels for **Core** and **Cover**.

### Product { #produkt }

| Field | Unit | Meaning |
|---|---|---|
| **Outer diameter:** | mm | Finished outer diameter of the complete core-cover product. |
| **Filling grade:** | % | How densely the cross-section is filled with material (material share compared with the theoretically available cross-section). |

### Core and cover (identical for each panel) { #seele-und-mantel-je-panel-identisch }

| Field | Unit | Meaning |
|---|---|---|
| **Machine type:** | – | Selection of the braiding machine type (Round braider, Square braider, Horizontal braider, Carbon fiber braider, Wire braider, Packing braider). |
| **Bobbin:** | – | Selection of a bobbin from the master data (matching the selected machine type). Supplies the outer diameter, core diameter and winding length of the bobbin for the length calculation. |
| **Material:** | – | Optional selection of a material from the master data; the **Density** is taken over from it automatically. |
| **Density:** | g/cm³ | Material density (three decimal places). Filled when a material is selected, but can also be overwritten manually. |
| **Core share:** or **Cover share:** | % | Cross-sectional share of the respective layer in the overall product. **Core share + Cover share must add up to 100 %.** |
| **Braiding angle:** | ° | Braiding angle of the layer. |
| **Number of carriers per head:** | pcs | Number of carriers of the machine (core ≥ 1, cover ≥ 3). |
| **Ply count / carrier:** | pcs | Number of threads/strands running in parallel per carrier. |
| **Horngear speed:** | rpm | Speed of the machine's horngear. |

!!! note "Shares must add up to 100 %"
    If **Core share** and **Cover share** together deviate from 100 % by more than 0.01 %, the calculation reports *"The proportions of the core and cover do not add up to 100%"* and marks both share fields.

## Result { #ergebnis }

The headline values are **Output (Total)** and **Weight (Total)**;
below them, **Core diameter** and **Cover thickness** as well as all other
values are shown in pairs for core and cover.

| Value | Unit | Meaning |
|---|---|---|
| **Output (Total)** | kg/h | Total throughput of the product in mass per hour. |
| **Weight (Total)** | kg/100m | Weight of the finished core-cover product per 100 m. |
| **Core diameter** | mm | Diameter of the core. |
| **Cover thickness** | mm | Wall thickness of the cover (radial). |
| **Output (Core)** / **Output (Cover)** | kg/h | Throughput of the respective layer. |
| **Weight (Core)** / **Weight (Cover)** | kg/100m | Weight share of the respective layer per 100 m. |
| **Strand (Core)** / **Strand (Cover)** | tex | Fineness (titer) of the strand per layer. |
| **Strand diameter (Core)** / **Strand diameter (Cover)** | mm | Diameter of the single strand per layer. |
| **Length per bobbin (Core)** / **Length per bobbin (Cover)** | m | Material length that can be wound per bobbin. |
| **Product length (Core)** / **Product length (Cover)** | m | Braid length that can be produced per bobbin. |
| **Reduction (Core)** / **Reduction (Cover)** | % | Length reduction caused by braiding (bobbin length compared with braid length). |
| **Braiding length (Core)** / **Braiding length (Cover)** | mm | Length of travel of a thread per product revolution (pitch). |
| **Production (Core)** / **Production (Cover)** | m/h | Production speed of the respective layer. |
| **Braiding time (Core)** / **Braiding time (Cover)** | h | Braiding time until a bobbin runs empty. |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md). For
this computation-intensive product, the result card is located to the right of the
input.

The function calculates purely **forwards**: all results are calculated
from all inputs. It is not reversible – no empty
input field is calculated back from the results. If inputs are missing or
invalid (no bobbin selected, value ≤ 0), the results are cleared.

!!! tip "Maintain material once, take over density automatically"
    Select a [material](../../master-data/materials.md) from the master data in both panels – the **Density** is then set automatically. This is faster and avoids typing errors with this computation-intensive product.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Material diameter from material](../material/material-diameter.md) – diameter from density and titer of a single material.
- [Fineness / Titer](../material/linear-density.md) – fineness (tex) of individual yarns.
- [Product weight](rope-weight.md) – weight calculation for single-layer products.
- [Product diameter](product-diameter.md) – outer diameter of a braided product.
- [Production speed](../production/production-speed.md) – production speed of a braiding machine.
