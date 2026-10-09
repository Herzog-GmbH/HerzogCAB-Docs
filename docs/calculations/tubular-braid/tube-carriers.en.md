# Hollow braid – Number of carriers

!!! abstract "Reference — Calculation: determines the required number of carriers for a hollow braid"

## Purpose { #wofur }

This calculation determines the required **Number of carriers** for a hollow braid (hose braid) from braid diameter, braiding angle, material width and desired covering. This way you specify as early as order preparation how many carriers a braiding machine must be loaded with to achieve the required geometry and coverage.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Yarn type** | – | Choice between *Multifilament* and *Monofilament*. With *Monofilament*, the width/Ø factor is omitted (internally = 1), and the width field is called **Material diameter**. |
| **Braid diameter** | mm | Outer diameter of the finished hollow braid. |
| **Braiding angle** | ° | Angle of the threads in the set [reference](../../admin/settings/appearance.md#flechtwinkel). Permitted: greater than 0° and less than 90° (default 45°). |
| **Material width** or **Material diameter** | mm | With *Multifilament* the flattened width of the yarn, with *Monofilament* the material diameter. |
| **Width/Ø factor** | – | Ratio of width to diameter of the yarn (1.0 – 3.0; default 1.25). Only visible with *Multifilament*; fixed at 1.0 with *Monofilament*. |
| **Ply count** | pcs | Number of threads running in parallel per carrier (default 1). |
| **Covering** | % | Desired covering of the braid surface (default 70 %). |

!!! note "Material diameter display field"
    With *Multifilament*, the **Material diameter** field shows the material diameter derived from material width
    and width/Ø factor. It
    is a pure display field and cannot be edited. With *Monofilament*
    it is hidden, since width and diameter are identical here.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Number of carriers** | pcs | Required number of carriers, **rounded up to the next multiple of 4**. |

## Operation { #bedienung }

On the right of the page, a **schematic sketch** of the braid runs alongside (unrolled cover). It shows live how your inputs affect the geometry and highlights the field currently being edited in color. The **Yarn type** switch immediately affects the labels and visibility of the other fields (see above). The general structure of calculation pages is described in [How calculation pages are structured](../../basics/calc-page-anatomy.md).

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

Finally, the result is rounded up to the next **multiple of 4** (e.g. 18 → 20). If no meaningful positive value results, the field remains empty.

!!! note "Covering 100 %"
    A covering of exactly 100 % cannot be solved mathematically and is
    limited internally to 99.9999 % so that a result can be output.

!!! tip "Multiple of 4"
    Carriers run in groups of four (equal numbers of left-hand and right-hand
    carriers). That is why the software always rounds up to the next multiple of 4
    – the number output is directly suitable for the machine.

The calculation is **not reversible**: the number of carriers is always the result, all other fields are inputs. As soon as a mandatory detail is missing or invalid (diameter ≤ 0, angle outside 0–90°, ply count ≤ 0, covering ≤ 0 or effective material diameter ≤ 0), the result remains empty.

## Related calculations { #verwandte-berechnungen }

* [Hollow braid – Diameter](tube-diameter.md)
* [Hollow braid – Material width](yarn-width.md)
* [Hollow braid – Covering](tube-cover.md)
* [Material diameter](../material/material-diameter.md)
* [Fineness / titer](../material/linear-density.md)
