# Braid density (lay length)

!!! abstract "Reference — Calculation: lay length or picks density from braid dimension and braiding angle"

## Purpose { #wofur }

The **Braid density** describes how dense a braid appears. This
calculation determines the **lay length** from braid dimension and braiding angle –
i.e. the axial advance for one full revolution of a strand around the
product – and can optionally convert the result directly into common density units
(picks per unit of length).

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Braid type** | – | Choice between **Round braid** and **Flat braid**. Determines the formula used. With *Round braid* the dimension field is the braid diameter, with *Flat braid* the braid width. |
| **Product diameter** / **Product width** | mm | Dimension of the braid. The label changes depending on the braid type: *Product diameter* for round braid, *Product width* for flat braid. |
| **Braiding angle** | ° | Angle of the strands in the set [reference](../../admin/settings/appearance.md#flechtwinkel) (0–90°). |
| **Result unit** | – | The unit in which the result is output: **Lay length [mm]**, **Picks / 10 mm**, **Picks / inch** or **Picks / French inch**. |
| **Number of carriers** | pcs | Number of carriers. **Only required** if a *Picks / …* variant is selected as the result unit; with *Lay length [mm]* the field is hidden. |

!!! note "Mandatory fields"
    For the calculation, **Product diameter/width** and **Braiding angle** must be greater than 0. With the *Picks / …* units, a **Number of carriers** of at least 1 is also required.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Lay length** | mm | With result unit *Lay length [mm]*: axial advance per full revolution. |
| **Picks / 10 mm** | – | Number of picks (crossing points per carrier) over a length of 10 mm. |
| **Picks / inch** | – | Number of picks per inch (25.4 mm). |
| **Picks / French inch** | – | Number of picks per French inch (27 mm). |

The result label and unit automatically adapt to the selected **Result unit**.

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

Via the **Result unit** you obtain from the same inputs either
the pure lay length or the picks density customary in practice (picks
per 10 mm, inch or French inch) – without having to enter the values
again.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Braiding angle](braid-angle.md)
- [Braid density conversion](picks-density.md)
