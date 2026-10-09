# Ply count from product

!!! abstract "Reference — Calculation: required ply count for an already selected material"

## Purpose { #wofur }

This calculation is the counterpart to
[Material diameter from product](material-diameter-product.md): instead of suggesting a
suitable material, you start from a yarn that is already fixed
and determine with how many ends (**Ply count**) it must be run per carrier
to achieve the desired braid. Typical
use: a yarn is already in stock or is specified, and you
want to know how many threads of it must be used in parallel per carrier.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Braid type:** | – | Choice between *Round braid* and *Lace braid*. Determines the label and calculation of the dimension field. |
| **Material:** | – | Optional selection of a material from the [master data](../../master-data/materials.md). Automatically takes over **Density** and **Fineness (material)** (in tex). |
| **Density:** | g/cm³ | Material density (up to 3 decimal places, max. 25). Must be greater than 0. |
| **Fineness (material):** | tex, dtex, den, Nm, Ne | Fineness of the already selected yarn. You choose the unit in the selection field to the right of it (default: tex). Must be greater than 0. |
| **Product diameter:** / **Product width:** | mm | Dimension of the finished braid (max. 100000). The label changes automatically: *Product diameter* for round braid, *Product width* for lace braid. Must be greater than 0. |
| **Number of carriers per head:** | pcs | Number of carriers of the braiding machine (max. 1500). Minimum value 1. |
| **Braiding angle:** | ° | Angle of the strands to the product axis (max. 89°). Must be greater than 0. |
| **Filling grade:** | % | How densely the cross-section is to be filled with material (max. 100 %, initial value 80 %). Must be greater than 0. |

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Required ply count:** | pcs | Number of ends of the selected yarn that are required per carrier. |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

This calculation runs forwards only: the required ply count is determined from the
product specifications and the fineness of the selected yarn; calculating
individual input fields backwards from the result is not intended.
If density, fineness, product dimension, braiding angle or filling grade is missing, or
the number of carriers is less than 1, the result field remains empty and the
affected field is marked red.

!!! note "Result is rounded up"
    Since a ply count can only consist of whole threads, Herzog CAB always rounds
    the calculated result up to the next whole number (at least 1
    pcs). If the ply count actually chosen is not quite sufficient by calculation,
    choose the next higher level if in doubt.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Material diameter from product](material-diameter-product.md) – conversely suggests a suitable material including fineness.
- [Material diameter from material](material-diameter.md) – diameter of an already known yarn.
- [Fineness / titer](linear-density.md) – fineness of a single thread from the braid parameters.
- [Materials](../../master-data/materials.md) – maintenance of density and titer in the master data.
