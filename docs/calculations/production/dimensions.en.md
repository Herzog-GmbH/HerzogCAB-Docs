# Machine sizing

!!! abstract "Reference — Calculation: estimates the length and width of a braiding machine and draws the floor plan"

## Purpose { #wofur }

This calculation provides a rough estimate of the **footprint** of a braiding machine – i.e. the length and width of the floor plan – based on number of carriers, pitch size and design. In everyday braiding it helps with planning machine locations and the shop floor before the exact machine has been decided. On the right of the page, the determined floor plan is also drawn as a sketch (rectangle with braiding circle).

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Single-head machine / Two-head machine** | – | Design of the machine. Choice between single-head (default) and two-head. The two-head variant occupies two braiding circles and results in a considerably greater length. |
| **Number of carriers:** | pcs | Number of carriers of the machine. Must be at least **4** (valid range 4 … 1500). |
| **Pitch size:** | mm | Pitch size of the machine. Must be greater than 0 (up to max. 3000 mm). |

!!! note "Observe minimum values"
    If the number of carriers is below 4 or the pitch size is not greater than 0, no result is calculated and the result fields remain empty.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Length:** | cm | Estimated length of the machine floor plan (one decimal place). Correspondingly greater for two-head machines. |
| **Width:** | cm | Estimated width of the machine floor plan (one decimal place). |

## Operation { #bedienung }

Next to the input card, an interactive **drawing area** draws the determined floor plan including the braiding circle(s). Above it are two buttons:

* **Reset Zoom** – resets the zoom level and view of the drawing area.
* **Color** – opens the color selection for the currently selected machine in the drawing.

You can place several calculated machines one after the other in the same drawing area, click them individually and move them to roughly sketch a shop floor layout. The **Clear** button only removes the currently **selected** machines from the drawing – not the input values of the form. The general structure of the calculation pages is described in [How calculation pages are structured](../../basics/calc-page-anatomy.md).

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

The estimate is derived from the geometry of the braiding circle; design, number of carriers and pitch size determine the length and width of the floor plan.

!!! note "Forward calculation only"
    This function calculates forwards only: length and width are determined from design, number of carriers and pitch size. Reversing it (calculating an empty input field back from the results) is not intended here. The results are deliberately rough and serve planning, not dimensionally accurate design.

## Related calculations { #verwandte-berechnungen }

* [Change gears rubber feed device](change-gears.md)
* [Production speed](production-speed.md)
* [Machine runtime per bobbin set](run-time-bobbin-set.md)
* [Factory Planner](../../hall-planner/index.md)
