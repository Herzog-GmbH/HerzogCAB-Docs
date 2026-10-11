# Machine runtime per bobbin set

!!! abstract "Reference — Calculation: determines how long a braiding machine runs with one bobbin set"

## Purpose { #wofur }

This calculation answers the central planning question at the braider: **How long does the machine run until a full bobbin set is used up?** To do so, it combines three partial values – the yarn length on one bobbin, the production output of the machine and the braiding angle – and, in addition to the run time, also outputs the product length produced per bobbin set and the reduction caused by the braiding angle.

## Inputs { #eingabewerte }

The page consists of three blocks side by side: **Material length on bobbin**, **Production speed** and **Braiding angle**. Each block supplies one of the three partial values for the final result (for details on the switch, see [Operation](#bedienung)).

### Block "Material length on bobbin" { #block-fadenlange-auf-spule }

Visible in *Calculate* mode; the fields depend on **Calculation via:**. In *Enter value* mode, the **Material length on bobbin** field is sufficient.

| Field | Unit | Meaning |
|---|---|---|
| **Calculation via** | – | Calculation basis: *Material*, *Material diameter*, *Rectangle material* or *Wire diameter*. |
| **Machine type** | – | Braiding machine design (*Round braider*, *Square braider*, *Horizontal braider*, *Carbon fiber braider*, *Wire braider*, *Packing braider*). Controls the available bobbin selection; with the *Wire diameter* basis it is fixed to *Wire braider*. |
| **Bobbin** | – | Selection of a bobbin type from the [bobbin master data](../../master-data/bobbins.md). Supplies outer diameter, core diameter and winding length. |
| **Material** | – | Only with the *Material* basis: selection from the [material master data](../../master-data/materials.md). Takes over density, yarn fineness and its unit. |
| **Fineness / Titer** | tex, dtex, den, Nr_metric, Nr_english | Only with the *Material* basis: fineness of the yarn (unit in the field to the right of it). |
| **Density** | g/cm³ | Only with the *Material* basis: material density. |
| **Filling grade** | % | Only with the *Material* basis: winding filling grade of the bobbin (preset 70 %). |
| **Ply count** | pcs | Number of threads wound in parallel on the bobbin. |
| **Material diameter** | mm | Only with the *Material diameter* or *Wire diameter* basis: diameter of the single thread or wire. |
| **Rectangle height** | mm | Only with the *Rectangle material* basis: height of the rectangular cross-section (enters into the layer calculation). |
| **Rectangle width** | mm | Only with the *Rectangle material* basis: mandatory input, but does **not** enter into the formula. |
| **Material length on bobbin** | m | Partial value. Entered manually in *Enter value* mode, locked and filled automatically in *Calculate* mode. |

### Block "Production speed" { #block-produktionsgeschwindigkeit }

Visible in *Calculate* mode; in *Enter value* mode, **Production output** is sufficient.

| Field | Unit | Meaning |
|---|---|---|
| **Machine type** | – | Braider type (*Round braider*, *Flat braider*, *Soutache braider*, *Square braider*, *Spiral braider*, *Packing braider, 2/3/4 lanes*). Enters into the calculation of the production output. |
| **Braid designation** | – (unit selectable) | Lay length or picks density (braid designation). Unit: *Lay length*, *Picks / 10 mm*, *Picks / Inch*, *Picks / French Inch*. |
| **Number of carriers** | pcs | Number of carriers (min. 3). |
| **Horngear speed** | rpm | Speed of the horngear. |
| **Production output** | m/h | Partial value. Entered manually in *Enter value* mode, locked and filled automatically in *Calculate* mode. |

### Block "Braiding angle" { #block-flechtwinkel }

Visible in *Calculate* mode; in *Enter value* mode, **Braiding angle** is sufficient.

| Field | Unit | Meaning |
|---|---|---|
| **Braid type** | – | *Round braid* or *Flat braid*. |
| **Braid designation** | – (unit selectable) | Lay length or picks density (braid designation); units as above. |
| **Product diameter** | mm | Diameter of the finished braid. |
| **Number of carriers** | pcs | Only visible/optional with a picks-per-length unit. If it is missing, the braid designation is **always** treated as a lay length. |
| **Braiding angle** | ° | Partial value. Entered manually in *Enter value* mode, locked and filled automatically in *Calculate* mode. |

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Machine runtime** | h | Run time until the bobbin set is used up (main result). |
| **Product length per bobbin set** | m | Product length that can be produced from one bobbin set (yarn length taking the braiding angle into account). |
| **Reduction** | % | Length loss compared with the pure yarn length due to the braiding angle. |

## Operation { #bedienung }

Each of the three blocks has the **Enter value | Calculate** switch at the top:

* With **Enter value** you enter the partial value (material length on bobbin, production output or braiding angle) directly – the other detail fields of the block are hidden.
* With **Calculate** the page shows the associated detail fields and determines the partial value from them; the partial value field itself is then locked.

You do not have to set all three blocks to *Calculate*. If, for example, you already know the production output of your machine from practice, set this block to **Enter value** and have only the yarn length and braiding angle calculated. This way you combine measured empirical values with the calculated quantities. The general structure of the calculation pages is described in [How calculation pages are structured](../../basics/calc-page-anatomy.md).

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

The main result (**Machine runtime**) as well as **Product length per bobbin set** and **Reduction** are obtained from the three partial values **Material length on bobbin**, **Production output** and **Braiding angle**. If one of the three partial values is 0 or less, the results remain empty.

## Related calculations { #verwandte-berechnungen }

* [Production speed](production-speed.md) – the same partial value as a separate calculation.
* [Braiding angle](../product/braid-angle.md) – the same partial value as a separate calculation.
* [Braid density](../product/lay-length.md) – basis of the braid designation.
* [Product length](../product/rope-length.md) – producible length from a material supply.
* Master data: [Bobbins](../../master-data/bobbins.md), [Materials](../../master-data/materials.md).
