# Material diameter from material

!!! abstract "Reference — Calculation: strand diameter from fineness and density"

## Purpose { #wofur }

Calculates the diameter of a single material strand (yarn, strand or
wire) from its fineness, the material density, the ply count and the
filling grade. This lets you estimate how thick a strand actually builds up
on the carrier – for example to assess carrier loading, bobbin filling or the
geometry of a braid.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Material:** | – | Optional selection from the [material database](../../master-data/materials.md). When selected, the **Density** is automatically taken over into the density field. |
| **Density:** | g/cm³ | Material density (must be greater than 0). Filled by the material selection or entered manually. |
| **Linear density / Titer:** | tex, dtex, den, Nr_metric, Nr_english | Fineness (titer) of the material. You choose the unit in the selection field to the right of it (default: tex). Minimum value 1. |
| **Ply count:** | pcs | Number of ends run in parallel that form the strand. Minimum value 1. |
| **Filling grade:** | % | How densely the material is packed in the strand cross-section (1–100 %, initial value 80 %). |

!!! note "Density comes from the material"
    If you select a material from the database, the stored density is
    entered automatically. You can then overwrite the value if
    required. Materials have no fixed diameter – it only
    results from the values entered here.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Material diameter:** | mm | Calculated diameter of the strand made of all plied ends, rounded to 2 decimal places. |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

Always enter the fineness in the unit that is set in the selection field.
dtex, den, Nm and Ne are converted internally to tex before the calculation
– a wrongly selected unit falsifies the diameter.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Material diameter from product](material-diameter-product.md) – conversely determines the required fineness, the material diameter and a material suggestion from product diameter or width and the braid parameters.
- [Ply count from product](required-ply.md) – determines the required ply count for a selected material.
- [Fineness / titer](linear-density.md) – conversion and determination of the fineness.
- [Materials](../../master-data/materials.md) – maintenance of density and titer in the master data.
