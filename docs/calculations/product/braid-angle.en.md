# Braiding angle

!!! abstract "Reference — Calculation: braiding angle from braid designation and product dimension"

## Purpose { #wofur }

The **Braiding angle** is the angle at which a single strand runs in the
braid. By default, Herzog measures it to the **cross direction** of the
product, the technical literature usually to the **braid axis**; you set which reference
Herzog CAB shows under
[*Settings > General > Braiding angle*](../../admin/settings/appearance.md#flechtwinkel). It largely determines the appearance,
strength and elongation of the finished braid. The calculation determines
this angle from the braid designation and product dimension – separately for
round braid and lace braid.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Braid type:** | – | Choice between *Round braid* and *Lace braid*. Determines the formula and the name of the next field. |
| **Braid designation:** | Lay length, Picks / 10 mm, Picks / Inch, Picks / French Inch | Characteristic value of the braid (braid designation). You choose the unit in the selection field to the right of it. With *Lay length* the value is used directly; with the picks units (picks per unit of length) it is converted internally into a lay length. |
| **Product diameter:** / **Product width:** | mm | Dimension of the product. With *Round braid* the field is called **Product diameter:**, with *Lace braid* **Product width:**. |
| **Number of carriers:** | pcs | Number of carriers. Only shown and required if a picks unit is selected as the unit of the braid designation (not with *Lay length*). |

!!! note "Number of carriers only with picks units"
    The **Number of carriers:** field only appears once you select *Picks / 10 mm*, *Picks / Inch* or *Picks / French Inch* as the unit of the braid designation. With the *Lay length* unit, the number of carriers is not needed and remains hidden.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Braiding angle** | ° | Angle of the strand in the set [reference](../../admin/settings/appearance.md#flechtwinkel) (cross direction or braid axis), to two decimal places. The tooltip on the tile shows both values. |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

Product dimension and braid designation must be greater than 0, otherwise no
calculation is possible.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Braid density](lay-length.md)
- [Braid density conversion](picks-density.md)
- [Product diameter](product-diameter.md)
