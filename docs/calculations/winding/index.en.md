# Winding

!!! abstract "Reference — Overview of the winding calculations"

The **Winding** department prepares the material for braiding: yarn, wire
or strand is rewound from a supplier spool onto bobbins, which are then
inserted into the carriers of the braiding machine. The nine calculations
in this group support exactly this step — from the winding time through
bobbin capacity to the material demand for a whole winding batch.

## The winding calculations { #die-spulerei-berechnungen }

<div class="grid cards" markdown>

- :material-timer-outline: **Winding time**

    ---

    Duration for a single bobbin and for a whole batch of bobbins.

    [:octicons-arrow-right-24: Open](winding-time.md)

- :material-speedometer: **Yarn speed**

    ---

    Conversion between spindle speed and yarn speed via the winding diameter.

    [:octicons-arrow-right-24: Open](line-speed.md)

- :material-tune-vertical: **Yarn tension**

    ---

    Sensible tension when winding bobbins, derived from fineness and tension factor.

    [:octicons-arrow-right-24: Open](yarn-tension.md)

- :material-database-outline: **Bobbin capacity**

    ---

    How many meters of material a selected bobbin holds.

    [:octicons-arrow-right-24: Open](bobbin-capacity.md)

- :material-weight-kilogram: **Bobbin weight**

    ---

    Net and gross weight of a wound bobbin.

    [:octicons-arrow-right-24: Open](bobbin-weight.md)

- :material-package-variant-closed: **Material demand**

    ---

    Total material demand for a winding batch including waste/reserve.

    [:octicons-arrow-right-24: Open](material-demand.md)

- :material-swap-horizontal: **Bobbins from supplier spool**

    ---

    How many bobbins can be wound from one supplier spool.

    [:octicons-arrow-right-24: Open](from-supplier-spool.md)

- :material-ruler: **Residual length by weight**

    ---

    Remaining material length of a partly used bobbin, calculated back from its weight.

    [:octicons-arrow-right-24: Open](residual-length.md)

- :material-counter: **Number of bobbin winding machines**

    ---

    How many braiding machines one bobbin winding machine can supply in shift operation.

    [:octicons-arrow-right-24: Open](number-of-winders.md)

</div>

## Common structure { #gemeinsamer-aufbau }

All winding calculations follow the same building-block system as the other
calculations in Herzog CAB: input card, result tiles, **Calculate**/**Clear**
buttons and a history sidebar. The common
structure is explained under
[How calculation pages are structured](../../basics/calc-page-anatomy.md).

You reach the winding calculations via their own tile overview
**Winding** and via the *Calculations > Winding* navigation group in
the left navigation bar.

## Related areas { #verwandte-bereiche }

* [Bobbin winding machines](../../master-data/winding-machines.md) — master data of the
  bobbin winding machines (series SP, SPA, HLM)
* [Bobbins](../../master-data/bobbins.md) — bobbin formats with their
  dimensions
* [Winding order](../../orders/winding-order.md) — separate order type for
  the winding department
* [Calculations](../index.md) — overview of all calculation groups
