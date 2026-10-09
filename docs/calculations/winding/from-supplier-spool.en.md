# Bobbins from supplier spool

!!! abstract "Reference — Calculation: number of bobbins from one supplier spool"

## Purpose { #wofur }

This calculation determines how many bobbins can be wound from one supplier spool
(e.g. a large spool, a coil or a barrel from the supplier) — specified
either via the weight or directly via the length of the
supplier spool. Optionally, it also calculates how many supplier spools are needed for
a desired total number of bobbins.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Supplier spool specified via:** | – | Basis of the specification: *Weight* or *Length*. Shows the matching fields below. |
| **Supplier spool weight:** | kg | Only with the *Weight* basis. Weight of the complete supplier spool, up to three decimal places. Must be greater than 0. |
| **Material:** | – | Only with the *Weight* basis. Optional selection of a material from the [master data](../../master-data/materials.md); automatically takes over the stored fineness. |
| **Fineness:** | tex, dtex, den, Nr_metric, Nr_english | Only with the *Weight* basis. Fineness of the material with unit selection next to it. Must correspond to at least 1 tex. |
| **Ply count:** | pcs | Only with the *Weight* basis. Number of single threads wound together (at least 1, initial value 1). |
| **Supplier spool length:** | m | Only with the *Length* basis. Material length of the supplier spool, entered directly. Must be greater than 0. |
| **Length per bobbin:** | m | Always visible. Material length to be wound onto a single bobbin. Must be greater than 0. |
| **Bobbins required (optional):** | pcs | Always visible, optional. Target number of bobbins for which you want to know how many supplier spools are needed. |

!!! note "Mandatory fields"
    Length per bobbin is always mandatory. Depending on the basis, also supplier spool
    weight, fineness (at least 1 tex) and ply count (basis *Weight*)
    or supplier spool length (basis *Length*).

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Bobbins per supplier spool:** | pcs | Main result: number of bobbins that can be wound completely from the supplier spool, rounded down (a partly wound bobbin does not count). |
| **Supplier spool length:** | m | Only visible with the *Weight* basis (calculated from weight, fineness and ply count). With direct length input this tile is hidden, as it would be redundant. |
| **Supplier spools required:** | pcs | Only visible if **Bobbins required** is filled in. Rounded-up number of supplier spools for the desired number of bobbins. |

## Operation { #bedienung }

The common structure of all calculation pages (input card,
result tiles, **Calculate**/**Clear** buttons, history) is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md) —
here only the special features of this page.

**Bobbins required** is an optional additional field: if it remains empty,
the page only shows how many bobbins come out of one supplier spool. If you enter
a target number, the **Supplier spools
required** tile also appears.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

* [Material demand](material-demand.md)
* [Bobbin capacity](bobbin-capacity.md)
* [Residual length by weight](residual-length.md)
