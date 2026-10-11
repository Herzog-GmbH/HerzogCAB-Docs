# Braiding angle from take-up

!!! abstract "Reference — Calculation: braiding angle from horngear speed and take-up — or conversely the required take-up or the required horngear speed for a target braiding angle"

## Purpose { #wofur }

This calculation links the **machine setting** with the braid.
Horngear speed and take-up speed determine the
braiding angle at which the braid is produced — and conversely: which
take-up speed or which horngear speed do you need to obtain a
desired braiding angle? The take-up can be specified as a
speed or via the diameter and speed of the take-up disc.
For round braid and flat braid.

## Inputs { #eingabewerte }

Which fields are visible depends on **Calculate** and **Take-up
specified as**.

| Field | Unit / selection | Meaning |
|---|---|---|
| **Calculate:** | *Braiding angle*, *Take-up*, *Horngear speed* | What you are looking for. With *Braiding angle*, speed and take-up are given; with *Take-up* or *Horngear speed* you specify the target braiding angle. |
| **Braid type:** | *Round braid*, *Flat braid* | Determines the machine data below. |
| **Braid outer diameter:** / **Braid width:** | mm | Dimension of the braid — diameter for round braid, width for flat braid. The calculator icon opens [Product diameter](product-diameter.md); **Apply** writes the result back. |
| **Horngears in the track:** | pcs | Round braid only: number of horngears in the ring (up to 256). |
| **Slots per standard horngear:** | pcs | Flat braid only: slots of a standard horngear (default 4). |
| **Slots in the track:** | pcs | Flat braid only: slots over the whole track. |
| **Target braiding angle:** | ° | Only with *Take-up* and *Horngear speed*: the desired braiding angle (up to 85°). |
| **Horngear speed:** | rpm | Speed of the horngears (up to 2000). Omitted when it is calculated. |
| **Take-up specified as:** | *Speed*, *Take-up disc* | How the take-up is specified — omitted when the take-up is calculated. |
| **Take-up speed:** | m/h | With *Speed*: the take-up speed. The calculator icon opens [Production speed](../production/production-speed.md). |
| **Take-up disc diameter:** | mm | With *Take-up disc* and when calculating the take-up: diameter of the take-up disc (up to 5000). |
| **Take-up disc speed:** | rpm | With *Take-up disc*: speed of the disc (up to 10000). |
| **Effective take-up:** | % | With *Take-up disc* and when calculating the take-up: which share of the disc speed actually reaches the braid (slip; default 100 %). |

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Braiding angle** | ° | With *Calculate: Braiding angle* — the braiding angle that results from speed and take-up (two decimal places). |
| **Required take-up speed** | m/h | With *Calculate: Take-up*. |
| **Required take-up disc speed** | rpm | With *Calculate: Take-up*, as soon as a take-up disc diameter is entered. |
| **Required horngear speed** | rpm | With *Calculate: Horngear speed*. |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

The braiding angle — as **Target braiding angle** as well as the result — appears
in the set **braiding angle reference**: by default to the
**cross direction** (Herzog), optionally to the **braid axis**
(technical literature). You change this under
[*Settings > General > Braiding angle*](../../admin/settings/appearance.md#flechtwinkel); a target braiding angle
is entered in the selected reference. If you point at the
field with the mouse, the tooltip shows both values. The calculation is also available in the
[web app](../../web/calculations.md).

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Braiding angle](braid-angle.md) — from braid designation and product dimension
- [Production speed](../production/production-speed.md)
- [Product diameter](product-diameter.md)
