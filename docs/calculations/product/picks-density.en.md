# Braid density conversion

!!! abstract "Reference — Calculation: convert braid density live between lay length and picks units"

## Purpose { #wofur }

With **Braid density conversion** you convert the density of a
braid between different reference dimensions – between the
**Lay length** and the number of **picks** per reference length
(10 mm, 25.4 mm or 27 mm). This lets you compare figures from different
sources at a glance without converting by hand.

The function works as a live converter: you enter a value, choose
the source and target unit, and the result appears immediately.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Input:** | depending on **From:** | The numerical value to be converted (lay length or picks density). Values ≤ 0 give no result. |
| **From:** | – | Source unit. Choice: *Lay length*, *Picks / 10 mm*, *Picks / Inch*, *Picks / French Inch*. |
| **To:** | – | Target unit. Same choice as for **From:**. |
| **Braid type:** | – | *Round braid* or *Lace braid*. Only visible if **Lay length** is on exactly one side (From or To). |
| **Number of carriers:** | pcs | Number of carriers of the machine. Only visible if **Lay length** is on exactly one side. Value range 0–20000. |

!!! note "When braid type and number of carriers are needed"
    The **Braid type** and **Number of carriers** rows only appear if the **Lay length** is on exactly one side of the conversion (i.e. lay length ↔ picks). Only then does the machine enter into the calculation. If, on the other hand, you convert between two picks units (e.g. *Picks / 10 mm* to *Picks / French Inch*), these details are not needed and remain hidden.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Result** | depending on **To:** | The value converted into the target unit (lay length or picks density per reference length). |

If the **Number of carriers** is missing (value 0) for the conversion lay length ↔ picks, no calculation is possible and no result (–) is shown.

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md). This
page is a **live converter**: there is no **Calculate** button;
the result updates immediately with every input, and no
entry is created in the history bar.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Braiding angle](braid-angle.md)
- [Braid density](lay-length.md)
