# Yarn speed

!!! abstract "Reference — Calculation: conversion between spindle speed and yarn speed"

## Purpose { #wofur }

This calculation converts between the spindle speed of a bobbin winding machine and
the actual yarn speed at the winding body. Because the
winding diameter changes continuously during winding, each
speed corresponds to a different yarn speed — useful for setting the bobbin winding machine
to a desired yarn tension or, conversely, for determining the suitable
spindle speed for a certain winding diameter.

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Calculation:** | – | Direction of the conversion: *Yarn speed from spindle speed* or *Spindle speed from yarn speed*. Controls which of the two following inputs is shown. |
| **Spindle speed:** | rpm | Only visible with the direction *Yarn speed from spindle speed*. Speed of the winding spindle (at least 1, max. 100,000 rpm). |
| **Yarn speed:** | m/min | Only visible with the direction *Spindle speed from yarn speed*. Desired speed of the yarn at the winding body. Must be greater than 0. |
| **Winding diameter:** | mm | Current diameter of the winding body (empty bobbin to full bobbin). Must be greater than 0 (max. 5000 mm). |

!!! note "Mandatory fields"
    The winding diameter must always be greater than 0. Depending on the selected
    direction, the spindle speed must also be at least 1 rpm or the
    yarn speed greater than 0.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Yarn speed:** | m/min | Only visible with the direction *Yarn speed from spindle speed*. Calculated yarn speed, to two decimal places. |
| **Spindle speed:** | rpm | Only visible with the direction *Spindle speed from yarn speed*. Calculated speed, as an integer. |

## Operation { #bedienung }

The common structure of all calculation pages (input card,
result tiles, **Calculate**/**Clear** buttons, history) is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md) —
here only the special features of this page.

The selection under **Calculation:** shows only the matching
input field and the matching result tile in each case: with *Yarn speed
from spindle speed* you specify the spindle speed and obtain the
yarn speed; with *Spindle speed from yarn speed* it is the
other way round. The winding diameter is required in both directions.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

* [Winding time](winding-time.md)
* [Yarn tension](yarn-tension.md)
* [Bobbin capacity](bobbin-capacity.md)
