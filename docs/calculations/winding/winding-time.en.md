# Winding time

!!! abstract "Reference — Calculation: duration for one bobbin and for a whole winding batch"

## Purpose { #wofur }

This calculation determines how long winding a single bobbin
takes and how long a whole batch of several identical bobbins
needs. It helps with time planning in the winding department — for example to
estimate when a winding order will be finished, or to assess the utilisation of a
bobbin winding machine over a shift.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Length on bobbin:** | m | Material length wound onto one bobbin. Must be greater than 0. |
| **Winding speed:** | m/min | Speed at which the bobbin winding machine winds the material. Must be greater than 0. |
| **Number of bobbins:** | pcs | Number of bobbins in the batch (at least 1, initial value 1). |
| **Bobbin change time:** | min | Optional time for bobbin changes and setup between two bobbins. If the field remains empty or at 0, Herzog CAB calculates without change time. |

!!! note "Mandatory fields"
    Length on bobbin and winding speed must be greater than 0, the
    number of bobbins at least 1. If one of these values is missing, the
    result fields remain empty.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Winding time per bobbin:** | min | Main result: pure winding time of one bobbin (without change time), to two decimal places. |
| **Total time:** | h | Time for the complete batch including bobbin changes, to two decimal places. |
| **Bobbins per hour:** | pcs | Throughput of the bobbin winding machine including changes, to one decimal place. |

## Operation { #bedienung }

The common structure of all calculation pages (input card,
result tiles, **Calculate**/**Clear** buttons, history) is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md) —
here only the special features of this page.

The **Bobbin change time** is optional: if you leave the field empty or at 0,
Herzog CAB calculates the total time and throughput without
setup/change share, solely from winding time and number of bobbins.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

* [Yarn speed](line-speed.md)
* [Bobbin capacity](bobbin-capacity.md)
* [Number of bobbin winding machines](number-of-winders.md)
* [Material demand](material-demand.md)
