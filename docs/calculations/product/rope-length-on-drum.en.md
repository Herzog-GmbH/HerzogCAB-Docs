# Product length per drum

!!! abstract "Reference — Calculation: product length that can be wound onto a drum"

## Purpose { #wofur }

This calculation determines how much product (rope, strand, braid) can be
wound onto a drum. From the dimensions of the selected drum
and the product diameter, the total wound length in meters is
determined – useful for planning drum sizes, delivery quantities and
winding orders.

!!! info "Changed in version 2.1.0"
    The page no longer asks for drum dimensions (previously *Outer diameter*,
    *Core diameter* and *Winding length*), but selects the drum from the
    [drum master data](../../master-data/drums.md). The dimensions come from
    the record. New workspace folders start without drums —
    take them over there with **From Herzog catalogue …** or create
    your own.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Drum:** | – | Drum from the [drum master data](../../master-data/drums.md). The calculation uses its winding diameter (otherwise the outer diameter), its core diameter and its traverse width (otherwise the drum width). |
| **Product diameter:** | mm | Diameter of a single wound strand (two decimal places). |
| **Ply count:** | pcs | Number of strands wound together side by side. |

!!! note "Mandatory details"
    The selected drum needs an outer or winding diameter, a
    core diameter and a traverse width (or drum width); the core must be
    smaller than the winding diameter. The product diameter must be
    greater than zero, the ply count at least **1 pcs**. Missing or
    invalid inputs are marked red; without complete values the
    result remains empty.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Product length:** | m | Total wound product length that fits onto the drum given its dimensions. |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

The **Drum** selection list shows the name of each drum, or its dimension line
if it has no name. It is reloaded when the page is opened;
drums that you have created or changed in the meantime are therefore
available.

If several strands are wound side by side at the same time (ply count > 1),
the available winding width is divided among all strands – the length per
strand decreases accordingly.

!!! tip "Have drum and take-up unit suggested"
    Which drums are needed for a certain product length and which
    take-up unit carries them is determined by the calculation
    [Drum and take-up unit selection](drum-take-up-selection.md).

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Drum and take-up unit selection](drum-take-up-selection.md)
- [Product weight](rope-weight.md)
- [Material diameter from material](../material/material-diameter.md)
- [Product length](rope-length.md)
