# Fineness conversion

!!! abstract "Reference — Calculation: convert a fineness value live between yarn units"

## Purpose { #wofur }

With **Fineness conversion** you convert a fineness value (linear
density) live between the common yarn units – from **tex**
to **dtex**, **den**, **Nr_metric** or **Nr_english** and in any
direction. This is useful when a yarn is specified in one unit
but you need a different unit for an order, data sheet or calculation.

## Inputs { #eingabewerte }

The page is built as a live converter with a **From/To** card: you
enter the value and choose the source and target unit; the result
appears immediately.

| Field | Unit | Meaning |
|---|---|---|
| **Input:** | depending on the selected unit | Fineness value to be converted. Only a positive value (> 0) is converted. |
| **From:** | tex, dtex, den, Nr_metric, Nr_english | Unit of the entered value. Default: **tex**. |
| **To:** | tex, dtex, den, Nr_metric, Nr_english | Unit to convert into. Default: **dtex**. |

## Result { #ergebnis }

| Value | Unit | Meaning |
|---|---|---|
| **Result** | the unit selected under **To:** | The fineness value converted into the target unit. For an input ≤ 0 (or an invalid conversion), **0** is output. |

## Operation { #bedienung }

The common structure of all calculation pages is described in
[How calculation pages are structured](../../basics/calc-page-anatomy.md). This
page is a **live converter**: there is no **Calculate** button;
the result updates immediately with every input. Live converters
deliberately do not create an entry in the history bar.

With the green direction arrow between the two fields (tooltip
*"Swap units"*) you swap **From** and **To** with one click and
thus calculate directly in the opposite direction.

## Calculation { #berechnung }

> The exact calculation formula is not part of this documentation.

## Related calculations { #verwandte-berechnungen }

- [Fineness / Titer](linear-density.md)
- [Material diameter from material](material-diameter.md)
- [Materials (master data)](../../master-data/materials.md)
