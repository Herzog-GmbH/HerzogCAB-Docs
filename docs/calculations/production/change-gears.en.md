# Change gears rubber feed device

!!! abstract "Reference — Calculation: determines the suitable numbers of teeth of the change gears for the rubber feed device"

## Purpose { #wofur }

This calculation determines the suitable change gear combination for the rubber feed chain of the take-up. From the desired elongation, the diameter of the takeoff disc and the ratio, the software calculates the two numbers of teeth with which you equip the machine – this way you achieve the desired braid density or the planned feed in braiding operation.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Rubber feed device:** | – | Selection of the rubber feed device used: *Small rubber feed device K70* or *Big rubber feed device*. The selection defines the fixed chain characteristics. |
| **Elongation:** | % | Desired elongation. May be 0; maximum value 1500 %. |
| **Takeoff disc diameter:** | mm | Diameter of the takeoff disc. Mandatory field, must be greater than 0. |
| **Ratio takeoff disc - rubber feed chain:** | – | Transmission ratio between takeoff disc and rubber feed chain. Mandatory field, must be greater than 0; maximum value 1500. |

!!! note "Mandatory fields"
    **Takeoff disc diameter** and **Ratio takeoff disc - rubber feed chain** must both be greater than 0, since these values are used as divisors. If one of the two values is missing, the field is marked red and no calculation takes place. The **Elongation**, on the other hand, may be 0.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Number of teeth of change gear 1:** | pcs | Number of teeth of the first change gear (integer). |
| **Number of teeth of change gear 2:** | pcs | Number of teeth of the second change gear (integer). |

## Operation { #bedienung }

This page follows the general structure of the calculation pages without further special features (see [How calculation pages are structured](../../basics/calc-page-anatomy.md)). The only relevant item is the **Rubber feed device** selection: it determines in which range of numbers of teeth a valid result is possible at all (see below).

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

!!! note "Valid range of the change gears"
    Change gear 1 must lie within the range permitted for the selected rubber feed device (small rubber feed device: 20 … 50, big rubber feed device: 20 … 63). If the calculated result lies outside this range, the results are cleared and the note *"Not possible, please choose another option!"* appears. In this case, choose another option – for example a different ratio, a different disc diameter or a different rubber feed device.

!!! tip "Adjustments for \"Not possible\""
    Greater elongation, a greater ratio or a smaller disc diameter reduce change gear 1; the opposite change in each case increases it. This lets you bring the result into the permitted range in a targeted way.

## Related calculations { #verwandte-berechnungen }

* [Machine sizing](dimensions.md)
* [Production speed](production-speed.md)
* [Machine Runtime per Bobbin Set](run-time-bobbin-set.md)
