# Bobbin Volume

!!! abstract "Reference — Calculation: winding volume of a bobbin from its geometry"

## Purpose { #wofur }

Calculates the winding volume of a bobbin from its geometry. In everyday
braiding, the result helps you estimate how much material fits on a bobbin
and whether the chosen bobbin is sufficient for a yarn.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Outer diameter:** | mm | Maximum diameter of the full bobbin (over the wound material). |
| **Core diameter:** | mm | Diameter of the bobbin core (winding body without material). |
| **Winding length:** | mm | Length of the usable winding surface between the flanges. |

!!! note "All inputs in millimetres"
    Outer diameter, core diameter and winding length are entered in millimetres. All three values must be greater than 0.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Bobbin Volume:** | ccm (cm³) | Volume of the winding space, i.e. the cavity between core and outer diameter over the winding length. Displayed with two decimal places. |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md). This
page has no further special features – three dimensions, one result.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Material Length on Bobbin](material-length.md)
- [Fineness / titer](linear-density.md)
- [Material diameter from material](material-diameter.md)
- [Product weight](../product/rope-weight.md)
