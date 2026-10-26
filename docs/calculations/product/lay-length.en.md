# Braid density (lay length)

!!! abstract "Reference — Calculation: lay length or picks density from braid dimension and braiding angle or lay length factor"

## Purpose { #wofur }

The **Braid density** describes how dense a braid appears. This
calculation determines the **lay length** from braid dimension and braiding angle –
i.e. the axial advance for one full revolution of a strand around the
product – and can optionally convert the result directly into common density units
(picks per unit of length). Instead of the braiding angle you can also
specify the **lay length factor**, as is common for ropes.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Braid type** | – | Choice between **Round braid** and **Flat braid**. Determines the formula used. With *Round braid* the dimension field is the braid diameter, with *Flat braid* the braid width. |
| **Product diameter** / **Product width** | mm | Dimension of the braid. The label changes depending on the braid type: *Product diameter* for round braid, *Product width* for flat braid. |
| **Input via** | – | **Braiding angle** or **Lay length factor**: which of the two values you specify. The other one appears in the result. Orders and history from before version 2.1.2 open with *Braiding angle*. |
| **Braiding angle** | ° | Only with *Input via Braiding angle*. Angle of the strands in the set [reference](../../admin/settings/appearance.md#flechtwinkel) (0–90°). |
| **Lay length factor** | – | Only with *Input via Lay length factor*. Ratio of lay length to product diameter, for flat braid to product width. Factors of 7 to 12 are common for ropes. |
| **Result unit** | – | The unit in which the result is output: **Lay length [mm]**, **Picks / 10 mm**, **Picks / inch** or **Picks / French inch**. |
| **Number of carriers** | pcs | Number of carriers. **Only required** if a *Picks / …* variant is selected as the result unit; with *Lay length [mm]* the field is hidden. |

!!! note "Mandatory fields"
    For the calculation, **Product diameter/width** and, depending on **Input via**, **Braiding angle** or **Lay length factor** must be greater than 0. With the *Picks / …* units, a **Number of carriers** of at least 1 is also required.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Lay length** | mm | With result unit *Lay length [mm]*: axial advance per full revolution. |
| **Picks / 10 mm** | – | Number of picks (crossing points per carrier) over a length of 10 mm. |
| **Picks / inch** | – | Number of picks per inch (25.4 mm). |
| **Picks / French inch** | – | Number of picks per French inch (27 mm). |
| **Lay length factor** | – | With *Input via Braiding angle*: the factor that belongs to dimension and angle. |
| **Braiding angle** | ° | With *Input via Lay length factor*: the angle that belongs to dimension and factor. |

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
