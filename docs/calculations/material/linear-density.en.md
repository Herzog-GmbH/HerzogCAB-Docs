# Fineness / Titer

!!! abstract "Reference — Calculation: required yarn fineness for a desired braid"

## Purpose { #wofur }

This calculation determines the **fineness (titer) of a single thread**
needed to produce a braid with the desired geometric properties.
From product diameter, braiding angle, number of carriers, filling grade
and material density, the fineness (titer) per carrier is calculated – useful
for selecting the right yarn or wire before production.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Material:** | – | Optional selection of a material from the [master data](../../master-data/materials.md). Automatically takes over the stored **Density** into the *Density* field. |
| **Density:** | g/cm³ | Material density (up to 3 decimal places, max. 25). Must be greater than 0. |
| **Fineness / Titer:** | tex, dtex, den, Nr_metric, Nr_english | Selection of the unit in which the result is output. The result unit automatically follows this selection. |
| **Braiding angle:** | ° | Braiding angle of the product (max. 85°). Must be at least 5°. |
| **Product diameter:** | mm | Outer diameter of the finished braid. Must be greater than 0. |
| **Number of carriers:** | pcs | Number of carriers (max. 1500). Must be at least 8. |
| **Filling grade:** | % | Desired covering/filling grade of the surface (max. 100 %, initial value 70 %). Must be at least 1 %. |

!!! tip "Take over material from the master data"
    If you select a material at the top, the **Density** is entered automatically. This avoids typing errors, and you always work with the same maintained values.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Fineness / Titer:** | follows the *Fineness / Titer* selection (tex, dtex, den, Nr_metric, Nr_english) | Calculated fineness (titer) per single thread/carrier, to 2 decimal places. |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

This calculation runs in one direction only – the fineness is determined from
the inputs; individual input fields are not calculated backwards from the
result. The calculation only runs when density, filling grade,
number of carriers, braiding angle and product diameter are filled in with positive values.
If a value is missing, the result field remains empty. Values outside the stated
limits (e.g. number of carriers below 8 or braiding angle below 5°) are marked
red.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Convert fineness](linear-density-conversion.md)
- [Material diameter from material](material-diameter.md)
- [Material diameter from product](material-diameter-product.md)
- [Braiding angle](../product/braid-angle.md)
- [Product weight](../product/rope-weight.md)
