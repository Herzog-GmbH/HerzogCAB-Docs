# Material diameter from product

!!! abstract "Reference — Calculation: required material diameter and fineness from the product specifications"

## Purpose { #wofur }

This calculation reverses the point of view compared with
[Material diameter from material](material-diameter.md): instead of calculating
the diameter from a known yarn, you specify which
braid is to be produced in the end (diameter or width, number of carriers,
braiding angle, filling grade, ply count). From this, Herzog CAB determines which
fineness and which diameter the yarn to be used must have, and
directly suggests a suitable material from the material database. This way
you start the material selection from the finished product instead of trying
out yarn after yarn.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Braid type:** | – | Choice between *Round braid* and *Lace braid*. Determines the label and calculation of the dimension field and whether the **Band thickness** result tile is shown. |
| **Material:** | – | Optional selection of a material from the [master data](../../master-data/materials.md). Automatically takes over the stored **Density** and also serves as a filter for the material suggestion in the result. |
| **Density:** | g/cm³ | Material density (up to 3 decimal places, max. 25). Must be greater than 0. |
| **Product diameter:** / **Product width:** | mm | Dimension of the finished braid (max. 100000). The label changes automatically: *Product diameter* for round braid, *Product width* for lace braid. Must be greater than 0. |
| **Number of carriers per head:** | pcs | Number of carriers of the braiding machine (max. 1500). Minimum value 1. |
| **Braiding angle:** | ° | Angle of the strands to the product axis (max. 89°). Must be greater than 0. |
| **Filling grade:** | % | How densely the cross-section is to be filled with material (max. 100 %, initial value 80 %). Must be greater than 0. |
| **Ply count:** | pcs | Number of ends with which the suggested yarn is run per carrier (max. 1000). Minimum value 1. |

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Material diameter:** | mm | Main tile: required diameter of the single yarn, to 3 decimal places. |
| **Required fineness:** | tex, dtex, den, Nr_metric or Nr_english | Fineness the yarn must have per carrier and end. With a switch directly in the tile header you choose the display unit without recalculating. |
| **Band thickness (lace):** | mm | Only visible for braid type *Lace braid*: thickness of the full band made of all ends of one carrier. For round braid, the tile remains hidden. |
| **Material suggestion:** | Text | Names the material from the database whose fineness comes closest to the required fineness – restricted to the same material type as the material selected above (same name, otherwise same density). If none is found, the note "no matching material of the same type found" appears. |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

This calculation runs forwards only: material diameter, fineness and material
suggestion are determined from the product specifications; calculating
individual input fields backwards from the result is not intended.
If density, product dimension, braiding angle or filling grade is missing, or the
number of carriers or ply count is less than 1, the result tiles remain empty
and the affected field is marked red.

!!! tip "Read the result in any fineness unit"
    The **Required fineness** tile has its own unit switch
    in the header. With it you read the same result in tex,
    dtex, den, Nr_metric or Nr_english as you prefer, without triggering
    the calculation again.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Material diameter from material](material-diameter.md) – diameter from an already known yarn.
- [Ply count from product](required-ply.md) – conversely determines the required ply count for an already selected material.
- [Fineness / titer](linear-density.md) – fineness of a single thread from the braid parameters.
- [Materials](../../master-data/materials.md) – maintenance of density and titer in the master data.
