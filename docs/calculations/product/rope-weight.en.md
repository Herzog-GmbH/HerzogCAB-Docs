# Product weight

!!! abstract "Reference — Calculation: total weight of a braided product"

## Purpose { #wofur }

Calculates the total weight of a braided product (rope, strand,
hose) from the material fineness, the ply count, the number of carriers, the
braiding angle and the product length. This lets you estimate before production
how much material an order requires and how heavy the
finished product will be.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Fineness / Titer** | tex, dtex, den, Nr_metric, Nr_english | Fineness (titer) of one thread. You choose the unit in the selection field to the right of it (default: tex). For the calculation, the value is converted internally to tex. |
| **Ply count** | pcs | Threads per carrier; preset to 1. As on all other pages, the fineness applies to one thread. In the order, the ply count comes from the **Material** tab. |
| **Number of carriers** | pcs | Number of carriers braiding. |
| **Braiding angle** | ° | Angle of the threads in the set [reference](../../admin/settings/appearance.md#flechtwinkel). |
| **Product length** | m | Length of the finished product for which the weight is calculated. |

!!! note "Valid input ranges"
    The inputs are checked before the calculation. The following apply: number of carriers ≥ 8, braiding angle ≥ 4°, fineness ≥ 1 and product length > 0. If a limit is not reached, the program marks the affected field red and does not calculate.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Product weight** | kg | Total weight of the product over the specified product length. |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

The smaller the braiding angle to the cross direction (or the larger to the
braid axis), the higher the product weight. Therefore make sure you use a realistic braiding angle
that suits the machine.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Fineness / Titer](../material/linear-density.md)
- [Material diameter from material](../material/material-diameter.md)
- [Materials](../../master-data/materials.md) – maintain the fineness (titer) per material centrally and take it over into the calculation.
