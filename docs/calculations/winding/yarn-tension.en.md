# Yarn tension

!!! abstract "Reference — Calculation: sensible yarn tension when winding bobbins"

## Purpose { #wofur }

This calculation estimates a sensible yarn tension for the winding process.
It is based on the fineness of the material, the ply count and a
tension factor that describes the usual ratio of tension to fineness.
This helps you avoid bobbins that are wound too loosely
(yarn tangles) or too tightly (material distortion,
ballooning when unwinding).

## Inputs { #eingabewerte }

| Field | Unit | Meaning |
|---|---|---|
| **Material:** | – | Optional selection of a material from the [master data](../../master-data/materials.md). Automatically takes over the stored fineness into the *Fineness* field. |
| **Fineness:** | tex, dtex, den, Nr_metric, Nr_english | Fineness (titer) of the thread. Selection of the display unit via the dropdown next to it. Must correspond to at least 1 tex. |
| **Ply count:** | pcs | Number of single threads wound together (at least 1, initial value 1). |
| **Tension factor (typically 0.3–0.7):** | cN/tex | Ratio of yarn tension to fineness. Initial value 0.5 as a common guide value. Must be greater than 0 (max. 10). |

!!! note "Mandatory fields"
    Fineness, ply count and tension factor must be filled in and greater than 0
    (ply count at least 1). If a value is missing, the result field remains
    empty.

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Yarn tension:** | cN | Recommended yarn tension when winding bobbins, to one decimal place. |

## Operation { #bedienung }

The common structure of all calculation pages (input card,
result tile, **Calculate**/**Clear** buttons, history) is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md) —
here only the special features of this page.

!!! tip "Take over material from the master data"
    If you select a material at the top, the **Fineness** is entered
    automatically. This way you always work with the same maintained values as
    in the material master data.

The **Tension factor** is an empirical value. 0.5 is preset as the initial
value; depending on the material and bobbin winding machine, a value between 0.3
(sensitive material, looser winding) and 0.7 (robust material,
tighter winding) may be more sensible.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

* [Bobbin weight](bobbin-weight.md)
* [Yarn speed](line-speed.md)
* [Bobbin capacity](bobbin-capacity.md)
