# Product length

!!! abstract "Reference — Calculation: achievable braid length from one bobbin set"

## Purpose { #wofur }

Calculates how much finished braid (length in meters) results from the material
available on the bobbins. This lets you estimate before braiding
which product length a bobbin loading delivers, without the
machine having to run empty.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Bobbin volume:** | cm³ | Material volume per bobbin (yarn/wire supply of one bobbin). |
| **Number of carriers:** | pcs | Number of carriers (bobbins) running on the machine. Must be at least 8. |
| **Product diameter:** | mm | Diameter of the finished braid. |

!!! note "Valid inputs"
    For the calculation to run, **Bobbin volume** and **Product diameter** must be greater than 0 and the **Number of carriers** must be at least 8. Invalid fields are marked red.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Product length:** | m | Braid length achievable from the entire bobbin supply (two decimal places). |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

The volume is entered in cm³, the product diameter in mm; the result is
output in meters. The calculation runs in one direction only: the
**Product length** is always determined from the three input values. Calculating
an empty input field backwards from the product length is not
intended.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Product weight](rope-weight.md)
- [Product diameter](product-diameter.md)
- [Product length per drum](rope-length-on-drum.md)
- [Bobbin volume](../material/bobbin-volume.md)
