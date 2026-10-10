# Residual length by weight

!!! abstract "Reference — Calculation: remaining material length from the weight of a partly used bobbin"

## Purpose { #wofur }

This calculation determines how many meters of material are still on a
partly used bobbin. To do so, you weigh the bobbin and calculate
back from the weight via the fineness to the residual length — useful for
estimating remaining bobbins without unwinding them, for example during stocktaking or
before reusing a bobbin.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Gross weight (with bobbin):** | g | Weighed weight of the bobbin including the remaining material, up to one decimal place. Must be greater than 0. |
| **Empty bobbin weight:** | g | Weight of the empty bobbin (tube/drum without material), up to one decimal place. At 0, the gross weight is already taken as the net weight (weighed net). Must be less than the gross weight. |
| **Material:** | – | Optional selection of a material from the [master data](../../master-data/materials.md). Automatically takes over the stored fineness. |
| **Fineness:** | tex, dtex, den, Nr_metric, Nr_english | Fineness of the material with unit selection next to it. Must correspond to at least 1 tex. |
| **Ply count:** | pcs | Number of single threads wound together (at least 1, initial value 1). |

!!! note "Mandatory fields"
    The gross weight must be greater than 0, the empty bobbin weight less than
    the gross weight. Fineness (at least 1 tex) and ply count (at least
    1) are also mandatory.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Residual length:** | m | Main result: remaining material length on the bobbin, to one decimal place. |
| **Net material weight:** | g | Pure material weight without bobbin body (gross weight minus empty bobbin weight), to one decimal place. |

## Operation { #bedienung }

The common structure of all calculation pages (input card,
result tiles, **Calculate**/**Clear** buttons, history) is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md) —
here only the special features of this page.

!!! tip "Already weighed net?"
    If you have already weighed the material without the bobbin body, enter the
    weight under **Gross weight (with bobbin)** and leave **Empty bobbin
    weight** at 0.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

* [Bobbin weight](bobbin-weight.md)
* [Bobbins from supplier spool](from-supplier-spool.md)
* [Material demand](material-demand.md)
