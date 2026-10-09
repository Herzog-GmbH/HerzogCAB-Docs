# Product diameter

!!! abstract "Reference — Calculation: outer diameter of the finished braid"

## Purpose { #wofur }

Calculates the outer diameter of the finished braid from the yarn or
material properties, the number of carriers, the braiding angle and the
filling grade. This lets you estimate before braiding which
diameter a planned product will reach – useful for design,
machine selection and quotation costing.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Material:** | – | Optional selection of a material from the [material database](../../master-data/materials.md). **Density** and **Linear density / Titer** are then taken over automatically. |
| **Density:** | g/cm³ | Material density (three decimal places, max. 25). Must be greater than 0. |
| **Linear density / Titer:** | tex, dtex, den, Nr_metric, Nr_english | Fineness (titer) of the yarn. You choose the unit in the selection field to the right of it; internally the value is converted to tex. Minimum value 1. |
| **Ply count:** | pcs | Number of threads run in parallel per carrier. Minimum value 1. |
| **Number of carriers:** | pcs | Number of carriers of the braiding machine (max. 1500). Minimum value 5. |
| **Braiding angle:** | ° | Angle of the strands in the set [reference](../../admin/settings/appearance.md#flechtwinkel). Permitted 5° to 85°. |
| **Filling grade:** | % | How densely the theoretically available cross-section is filled with material (1–100 %). Initial value 70 %. |

!!! tip "Maintain material once, use it again and again"
    Select a material from the database at the top instead of typing in density and fineness by hand. This is faster and avoids input errors. How to create materials is described under [Materials](../../master-data/materials.md).

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Product diameter:** | mm | Calculated outer diameter of the finished braid (two decimal places). |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

The calculation only runs if density, fineness, ply count, number of carriers,
braiding angle and filling grade contain meaningful values (> 0 or within the
stated limits). If a value is missing or outside the
permitted range, the field is marked red and no
result appears.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Braiding angle](braid-angle.md)
- [Material diameter from material](../material/material-diameter.md)
- [Fineness / titer](../material/linear-density.md)
- [Product weight](rope-weight.md)
