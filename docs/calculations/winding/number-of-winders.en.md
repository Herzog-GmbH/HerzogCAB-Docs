# Number of bobbin winding machines

!!! abstract "Reference — Calculation: ratio of braiding machines to bobbin winding machines in shift operation"

## Purpose { #wofur }

This calculation determines how many bobbin winding machines are needed to
continuously supply a braiding machine with filled bobbins. It
links the braid key figures (braiding angle, output, machine runtime)
with the winding output of the bobbin winding machines and thus shows the ratio of
braiding machines to bobbin winding machines in shift operation — helpful when planning how
many bobbin winding machines need to be kept available for a given fleet of braiding
machines.

## Inputs { #eingabewerte }

The inputs are divided into three areas: **Braiding machine**,
**Bobbin winding machine** and **Product data**.

| Field | Unit | Meaning |
|---|---|---|
| **Number of shifts:** (braiding machine) | – | Number of shifts in braiding operation (choice of 1, 2 or 3). |
| **Number of carriers per head:** | pcs | Number of carriers of the braiding machine (at least 1). |
| **Number heads per machine:** | pcs | Number of braiding heads (at least 1). |
| **Horngear speed:** | rpm | Speed of the horngears of the braiding machine. |
| **Number of shifts:** (bobbin winding machine) | – | Number of shifts in winding operation (choice of 1, 2 or 3). |
| **Type of bobbin winder:** | – | Choice of **Semi automatic** or **Fully automatic**. Default: fully automatic. |
| **Winding speed:** | m/min | Speed at which the bobbin winding machine winds the material. |
| **Length on Bobbin:** | m | Material length wound onto one bobbin. |
| **Spindles per winder:** | pcs | Number of spindles (positions wound in parallel) per bobbin winding machine (at least 1). |
| **Lay length:** | mm | Lay length of the braid. |
| **Product diameter:** | mm | Diameter of the braid. |

!!! note "Mandatory fields"
    Winding speed, length on bobbin, lay length and braid diameter
    must be greater than 0; number of carriers, number of heads and spindles per
    bobbin winding machine at least 1, the horngear speed greater than 0. If not
    all values are set, the results remain empty.

## Result { #ergebnis }

The main result is **Bobbin Winders per Braiding Machine**; the other values
are output as key figure tiles.

| Value | Unit | Meaning |
|---|---|---|
| **Bobbin Winders per Braiding Machine:** | pcs | Main result: ratio of braiding machines to bobbin winding machines (rounded up). |
| **Number of Bobbins:** | pcs | Calculated number of bobbins required (rounded up). |
| **Machine runtime:** | h | Run time of the braiding machine for the calculated braid length. |
| **Output:** | m/h | Braiding output (braid length produced per hour). |
| **Bobbin winding time:** | min | Time to wind one bobbin. |
| **Braiding angle:** | ° | Braiding angle calculated from lay length and braid diameter. |
| **Product length:** | m | Braid length calculated from length on bobbin and braiding angle. |

## Operation { #bedienung }

The common structure of all calculation pages (input card,
result tiles, **Calculate**/**Clear** buttons, history) is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md) —
here only the special features of this page.

The input is divided into the three sections **Braiding machine**, **Bobbin winding machine**
and **Product data**; the result tiles combine both
intermediate values (braiding angle, output, machine runtime, winding time) and
the main result, so that you can follow the entire calculation path at a
glance.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

* [Winding time](winding-time.md)
* [Bobbin capacity](bobbin-capacity.md)
* [Braiding angle](../product/braid-angle.md)
* [Braid density](../product/lay-length.md)
* [Production speed](../production/production-speed.md)
* [Machine Runtime per Bobbin Set](../production/run-time-bobbin-set.md)
