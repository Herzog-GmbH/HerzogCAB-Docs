# Bobbin weight

!!! abstract "Reference — Calculation: net and gross weight of a wound bobbin"

## Purpose { #wofur }

This calculation provides the net and gross weight of a wound
bobbin from fineness, ply count and winding length. The gross weight (including
the bobbin body) is useful, for example, for transport, warehouse logistics or a
weighing check at goods receipt.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Material:** | – | Optional selection of a material from the [master data](../../master-data/materials.md). Automatically takes over the stored fineness. |
| **Fineness:** | tex, dtex, den, Nr_metric, Nr_english | Fineness of the material with unit selection next to it. Must correspond to at least 1 tex. |
| **Ply count:** | pcs | Number of single threads wound together (at least 1, initial value 1). |
| **Length on bobbin:** | m | Material length wound on the bobbin. Must be greater than 0. |
| **Empty bobbin weight:** | g | Optional weight of the empty bobbin (tube/drum without material), up to one decimal place. If the field remains empty or at 0, only the net weight is output. |

!!! note "Mandatory fields"
    Length on bobbin and fineness must be greater than 0 (fineness
    at least 1 tex), ply count at least 1. If one of these values is missing,
    the result fields remain empty.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Net material weight:** | kg | Main result: pure material weight without bobbin body, to three decimal places. |
| **Gross weight (with bobbin):** | kg | Total weight of the wound bobbin including bobbin body, to three decimal places. |

## Operation { #bedienung }

The common structure of all calculation pages (input card,
result tiles, **Calculate**/**Clear** buttons, history) is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md) —
here only the special features of this page.

The **Empty bobbin weight** is optional: if you leave it empty or at 0,
the gross weight equals the net weight.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

* [Residual length by weight](residual-length.md)
* [Material demand](material-demand.md)
* [Bobbin capacity](bobbin-capacity.md)
* [Yarn tension](yarn-tension.md)
