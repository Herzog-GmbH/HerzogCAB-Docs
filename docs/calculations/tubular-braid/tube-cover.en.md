# Hollow braid – Covering

!!! abstract "Reference — Calculation: determines the achieved covering of a hollow braid"

## Purpose { #wofur }

This calculation determines the **Covering** of a hollow braid – i.e. how completely the surface of the hose/tube is covered by the braid (in percent). This lets you check whether a combination of material, number of carriers and braiding angle achieves the desired density.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Yarn type** | – | **Multifilament** or **Monofilament**. Determines whether the calculation uses material width or material diameter. |
| **Braid diameter** | mm | Diameter of the hollow braid. |
| **Braiding angle** | ° | Braiding angle (less than 90°, default 45). |
| **Material width** / **Material diameter** | mm | With *Multifilament* the material width, with *Monofilament* the material diameter. |
| **Width/Ø factor** | – | Ratio of width to diameter (1–3, default 1.25; only with *Multifilament*). |
| **Number of carriers** | pcs | Number of carriers. |
| **Ply count** | pcs | Number of threads per carrier (default 1). |

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Covering** | % | Covering of the braid (1 decimal place). Values above 100 % are flagged as "Covering > 100 %". |

## Operation { #bedienung }

As with the other hollow braid calculations, a **schematic sketch** that updates live runs alongside on the right and highlights the field currently being edited. If your inputs do not lead to a geometrically valid result, the page reports this as an error instead of showing a meaningless value (see below). The general structure of the calculation pages is described in [How calculation pages are structured](../../basics/calc-page-anatomy.md).

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

!!! warning "Covering > 100 %"
    If the inputs are geometrically impossible (the material would overlap several times), the page reports **"Covering > 100 %"** instead of a numerical value. In this case, reduce the material width/diameter, number of carriers or ply count, or increase the braid diameter.

## Related calculations { #verwandte-berechnungen }

* [Hollow braid – Number of carriers](tube-carriers.md)
* [Hollow braid – Diameter](tube-diameter.md)
* [Hollow braid – Material width](yarn-width.md)
