# Bobbin capacity

!!! abstract "Reference — Calculation: material length that a bobbin holds"

## Purpose { #wofur }

This calculation determines how many meters of material a selected bobbin
holds — either via the material data (density and fineness) or directly
via the material diameter. This lets you check before winding whether an
existing bobbin format is sufficient for the desired material length, or
choose the right bobbin for a winding order.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Calculation via:** | – | Basis of the calculation: *Material* (density + fineness) or *Diameter* (material diameter directly). Shows the matching fields below. |
| **Bobbin:** | – | Selection of the bobbin from the [bobbin master data](../../master-data/bobbins.md) (all bobbin formats, unfiltered). |
| **Material:** | – | Only with the *Material* basis. Optional selection of a material from the [material master data](../../master-data/materials.md); automatically takes over the stored density. |
| **Density:** | g/cm³ | Only with the *Material* basis. Material density (up to 3 decimal places, max. 25). Must be greater than 0. |
| **Fineness:** | tex, dtex, den, Nr_metric, Nr_english | Only with the *Material* basis. Fineness of the material with unit selection next to it. Must correspond to at least 1 tex. |
| **Material diameter:** | mm | Only with the *Diameter* basis. Diameter of the thread or wire. Must be greater than 0 (max. 500 mm). |
| **Filling grade:** | % | How densely the material lies on the bobbin. Initial value 70 %, max. 100 %. Must be at least 1 %. |
| **Ply count:** | pcs | Number of single threads wound together (at least 1, initial value 1). |

!!! note "Mandatory fields"
    A bobbin must be selected; filling grade at least 1 % and ply count
    at least 1. Depending on the basis, also density and fineness (basis
    *Material*) or material diameter (basis *Diameter*) greater than 0.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Bobbin capacity:** | m | Main result: material length that fits on the selected bobbin, to two decimal places. |
| **Bobbin volume:** | cm³ | Holding volume of the selected bobbin (from outer/core diameter and winding length), to one decimal place. |

## Operation { #bedienung }

The common structure of all calculation pages (input card,
result tiles, **Calculate**/**Clear** buttons, history) is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md) —
here only the special features of this page.

!!! tip "Take over the bobbin from the order"
    If you open this calculation from within an order, the
    matching bobbin is preselected automatically based on its dimensions — you
    then no longer have to search for it manually.

With the *Material* basis, selecting a material from the master data fills
the **Density** automatically; you enter the **Fineness** independently of this
with the desired unit.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

* [Material length on bobbin](../material/material-length.md)
* [Bobbin volume](../material/bobbin-volume.md)
* [Bobbin weight](bobbin-weight.md)
* [Winding time](winding-time.md)
