# Hollow braid – Material width

!!! abstract "Reference — Calculation: determines the required material width or material diameter for a hollow braid"

## Purpose { #wofur }

The calculation estimates how wide a yarn (multifilament) or how large a monofilament/wire must be so that the hollow braid achieves the desired **Covering** at a given diameter, braiding angle and number of carriers. This lets you judge before braiding whether an available material suits the desired cover layer.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Yarn type** | – | Choice between **Multifilament** and **Monofilament**. With monofilament, the width/Ø factor is hidden (internally = 1), and the result is the material diameter instead of the material width. |
| **Braid diameter** | mm | Outer diameter of the hollow braid. |
| **Braiding angle** | ° | Angle of the threads in the set [reference](../../admin/settings/appearance.md#flechtwinkel) (0–89°, default 45°). |
| **Number of carriers** | pcs | Number of carriers of the braiding machine. |
| **Ply count** | pcs | Number of yarns running in parallel per carrier (default 1). The result is calculated down to the width **per yarn**. |
| **Covering** | % | Desired covering of the braid surface (0–100 %, default 70 %). 100 % is calculated internally as 99.9999 %. |
| **Width/Ø factor** | – | Ratio of yarn width to yarn diameter (1.00–3.00, default 1.25). Only visible with multifilament; with monofilament = 1. Used to convert the width into the diameter. |

!!! note "Mandatory fields"
    Braid diameter, braiding angle (0 < α < 90°), number of carriers, ply count and covering must be greater than 0. If one of these values is missing, the result remains empty.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Material width (multifilament)** | mm | Required yarn width per yarn for the desired covering. With yarn type **Monofilament**, the same tile is labelled **Material diameter**. |
| **Material diameter** | mm | Diameter derived from the width. Only visible as an additional tile with multifilament; with monofilament it corresponds to the main figure. |

## Operation { #bedienung }

Here too, a **schematic sketch** that updates live accompanies the input on the right and highlights the field currently being edited. The main tile automatically renames itself depending on the **Yarn type** (*Material width* with multifilament, *Material diameter* with monofilament) – you do not need to set anything for this. General information on the structure of the calculation pages is given in [How calculation pages are structured](../../basics/calc-page-anatomy.md).

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

!!! tip "Choosing the width/Ø factor correctly"
    With multifilament yarns, the flattened width is typically larger than the round diameter. The width/Ø factor (default 1.25) represents this ratio. Adapt it to your actual yarn if the derived material diameter is to become more realistic.

!!! note "Covering 100 %"
    Complete covering cannot be represented exactly by calculation; the value is therefore limited internally to 99.9999 %.

## Related calculations { #verwandte-berechnungen }

* [Hollow braid – Number of carriers](tube-carriers.md)
* [Hollow braid – Diameter](tube-diameter.md)
* [Hollow braid – Covering](tube-cover.md)
* [Material diameter](../material/material-diameter.md)
* [Fineness / Titer](../material/linear-density.md)
