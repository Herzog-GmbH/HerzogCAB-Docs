# Hollow braid – Diameter

!!! abstract "Reference — Calculation: determines the achievable braid diameter of a hollow braid"

## Purpose { #wofur }

This calculation determines the **Braid diameter** of a hollow braid (hose or round braid) from braiding angle, material, number of carriers, ply count and desired covering. This lets you estimate in advance which diameter a braid with a planned configuration will take on.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Yarn type** | – | **Multifilament** / **Monofilament** switch. Multifilament (e.g. yarn) lies flat and is described via the width/Ø factor; monofilament (wire, round) has diameter = width. |
| **Braiding angle** | ° | Braiding angle of the braid. Permitted: greater than 0 and less than 90; default 45. |
| **Material width** *(Multifilament)* or **Material diameter** *(Monofilament)* | mm | With multifilament the laid width of the material, with monofilament directly the material diameter. The label changes depending on the yarn type. |
| **Width/Ø factor** | – | Only visible with **Multifilament**. Ratio of material width to material diameter (range 1.0 to 3.0; default 1.25). With monofilament fixed at 1.0 and hidden. |
| **Number of carriers** | pcs | Number of carriers (threads) in the braid. Must be greater than 0. |
| **Ply count** | pcs | Number of threads combined per carrier. Default 1; must be greater than 0. |
| **Covering** | % | Desired covering of the braid surface (0 to 100 %; default 70 %). |

!!! note "Material diameter as an info row"
    With multifilament, an additional read-only row **Material diameter** shows the diameter derived from material width and factor. With monofilament this row is omitted, since diameter and width are identical.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Braid diameter** | mm | Calculated (outer) diameter of the hollow braid for the entered configuration. |

## Operation { #bedienung }

On the right of the page, the same **schematic sketch** runs alongside as with the other hollow braid calculations: it shows the unrolled cover and highlights the field currently being edited. The structure of the calculation pages is described in general in [How calculation pages are structured](../../basics/calc-page-anatomy.md).

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

!!! note "Mandatory inputs"
    A result is only output if braiding angle (between 0 and 90°), ply count, covering, number of carriers and the material diameter are each greater than 0. Missing or invalid values are marked red in the field.

!!! tip "Effect of the covering"
    With otherwise identical values, a higher covering leads to a smaller braid diameter. With the braiding angle and the number of carriers you additionally control how dense and how large the braid turns out.

## Related calculations { #verwandte-berechnungen }

* [Hollow braid – Number of carriers](tube-carriers.md)
* [Hollow braid – Covering](tube-cover.md)
* [Braiding angle](../product/braid-angle.md)
* [Material diameter](../material/material-diameter.md)
