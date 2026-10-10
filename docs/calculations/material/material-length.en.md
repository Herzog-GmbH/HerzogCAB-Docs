# Material length on bobbin

!!! abstract "Reference — Calculation: usable yarn length on a loaded bobbin"

## Purpose { #wofur }

This calculation determines **how much material fits on a bobbin** – the
usable yarn length on the bobbin. It is based on the winding volume of the bobbin
and the material data (density, fineness or dimensions).

## Inputs { #eingabewerte }

With **Calculation via** you choose the calculation basis; depending on your choice,
different fields are shown.

| Field | Unit | Meaning |
|---|---|---|
| **Calculation via** | – | Calculation basis: **Material**, **Diameter** or **Rectangle material**. |
| **Machine type** | – | Filters the selectable bobbins. |
| **Bobbin** | – | Bobbin from the [bobbin master data](../../master-data/bobbins.md); supplies the dimensions for the winding volume. |
| **Material** | – | Optional: material from the master data; automatically takes over the **Density**. |
| **Density** | g/cm³ | Material density. |
| **Fineness** | tex, dtex, den, Nr_metric, Nr_english | Fineness of the material (only with calculation basis *Material*). |
| **Diameter** | mm | Material diameter (only with calculation basis *Diameter*). |
| **Rectangle height**, **Rectangle width** | mm | Dimensions of the flat thread (only with calculation basis *Rectangle material*). |
| **Filling grade** | % | Share of the bobbin volume that is actually wound (default 70). |
| **Ply count** | pcs | Number of threads per carrier. |

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Material length** | m | Yarn length that fits on the bobbin (2 decimal places). |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

From within an order, the bobbin can also be preselected automatically based on its
dimensions instead of searching for it manually here.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Bobbin volume](bobbin-volume.md)
- [Fineness / Titer](linear-density.md)
- [Material diameter from material](material-diameter.md)
- [Bobbin formats (master data)](../../master-data/bobbins.md)
