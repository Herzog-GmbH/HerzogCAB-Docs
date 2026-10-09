# Material demand

!!! abstract "Reference — Calculation: total material demand for a winding batch"

## Purpose { #wofur }

This calculation determines the total material demand for a winding batch
of several bobbins of equal length, including a waste or
reserve allowance. If a fineness is also specified, the total weight is
calculated from it as well — useful for ordering material
before a larger winding order.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Number of bobbins:** | pcs | Number of bobbins in the batch. Must be at least 1. |
| **Length per bobbin:** | m | Material length per bobbin. Must be greater than 0. |
| **Waste/reserve:** | % | Optional percentage allowance for waste, start-up winding losses or reserve, up to one decimal place. If the field remains at 0, the calculation is made without an allowance. |
| **Material:** | – | Optional selection of a material from the [master data](../../master-data/materials.md); only relevant for the total weight. Automatically takes over the stored fineness. |
| **Fineness:** | tex, dtex, den, Nr_metric, Nr_english | Optional, only for the total weight. Fineness of the material with unit selection next to it. |
| **Ply count:** | pcs | Number of single threads wound together (at least 1, initial value 1). Only relevant if a fineness is specified. |

!!! note "Mandatory fields"
    Number of bobbins (at least 1) and length per bobbin (greater than 0) are
    mandatory. Material and fineness are optional — without fineness only
    the total weight remains empty; total length and reserve are still
    calculated.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Total length (incl. reserve):** | m | Main result: sum of all bobbins plus waste/reserve, as an integer. |
| **Total weight:** | kg | Only visible if a fineness is specified. Weight of the total length, to two decimal places. |
| **of which reserve:** | m | Share of the total length attributable to the waste/reserve allowance, as an integer. |

## Operation { #bedienung }

The common structure of all calculation pages (input card,
result tiles, **Calculate**/**Clear** buttons, history) is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md) —
here only the special features of this page.

**Material** and **Fineness** are deliberately optional: without them, the
calculation only provides the total length and the reserve quantity; with fineness, the
total weight is added.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

* [Bobbins from supplier spool](from-supplier-spool.md)
* [Bobbin weight](bobbin-weight.md)
* [Winding time](winding-time.md)
