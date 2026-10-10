# Production speed

!!! abstract "Reference — Calculation: determines the production speed of a braiding machine"

## Purpose { #wofur }

Calculates how fast a braid is produced – as a linear speed in meters per hour. It is based on the machine type, the braid designation (lay length or picks per unit of length), the horngear speed and the number of carriers. This lets you estimate for an order how long the machine needs for a certain product length.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Machine type:** | – | Selection of the braider type: *Round braider*, *Lace braider*, *Soutache braider*, *Square braider*, *Spiral braider*, *Packing braider, 2 lanes*, *Packing braider, 3 lanes*, *Packing braider, 4 lanes*. Determines how much feed one horngear revolution produces. |
| **Braid designation:** | depending on unit | Describes the braid (braid designation). The unit is chosen via the selection field to the right of it: *Lay length* (the value is directly the lay length), *Picks / 10 mm*, *Picks / Inch* or *Picks / French Inch* (picks per unit of length). |
| **Horngear speed:** | rpm | Speed of the horngear. Maximum value 500 rpm. |
| **Number of carriers:** | pcs | Number of carriers. At least 3. Required for the feed calculation with round and lace braiders (RU/LZ) and for conversion if the braid designation is specified as picks per unit of length. |

!!! note "Mandatory details and limits"
    Braid designation and horngear speed must be greater than 0, the number of carriers at least 3. Fields that violate these limits are marked red.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Production speed:** | m/h | Braid length produced per hour, to two decimal places. |

## Operation { #bedienung }

You choose the unit of the **Braid designation** field via the dropdown directly next to the field; if you change the unit, the page does not automatically convert the value already entered – enter it again in the newly selected unit. The general structure of the calculation pages is described in [How calculation pages are structured](../../basics/calc-page-anatomy.md).

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

!!! note "Number of carriers not always needed"
    With *Soutache*, *Square*, *Spiral* and *Packing braiders (2, 3 and 4 lanes)* with the unit *Lay length*, the number of carriers does not enter into the speed. It is only needed for round and lace braiders (RU/LZ) or when entering *picks per unit of length*. As long as mandatory values are missing, the result field remains empty.

## Related calculations { #verwandte-berechnungen }

* [Machine runtime per bobbin set](run-time-bobbin-set.md)
* [Change gears rubber feed device](change-gears.md)
* [Braid density](../product/lay-length.md)
* [Braid density conversion](../product/picks-density.md)
