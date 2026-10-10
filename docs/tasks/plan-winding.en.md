# Plan bobbins for a braiding order

!!! example "Guide — at the end, a printed winding order with calculated target values exists, linked to the associated braiding order"

**Prerequisites:**

* A saved [braiding order](../orders/braiding-order.md) — if none
  exists yet, first follow the workflow
  [From customer order to machine sheet](order-to-machine-sheet.md).
* [Bobbin winding machines](../master-data/winding-machines.md),
  [bobbins (bobbin formats)](../master-data/bobbins.md) and
  [materials](../master-data/materials.md) are maintained in the master data.
* You have permission to create orders.

```mermaid
flowchart LR
  A["Check master data"] --> B["Create winding order from braiding order"]
  B --> C["Calculate target values"]
  C --> D["Save"]
  D --> E["Print"]
```

## Step 1: Check the bobbin winding machine master data { #schritt-1-spulmaschinen-stammdaten-prufen }

Open *Master data > Bobbin winding machines* and check whether the bobbin winding machine
to be used for winding is recorded with its winding technology data.
If not, create it via **New** — all fields are explained on the
reference page [Bobbin winding machines](../master-data/winding-machines.md).

While you are at it, also check the
[bobbin formats](../master-data/bobbins.md) (dimensions of the bobbins) and the
[material](../master-data/materials.md) — both are offered as a selection in the
winding calculations.

## Step 2: Create a winding order from the braiding order { #schritt-2-spulauftrag-aus-dem-flechtauftrag-erstellen }

1. Open the navigation item **Orders** (reference:
   [Order overview](../orders/index.md)).
2. Select the braiding order for which bobbins are to be wound.
3. Click **Create winding order**. The
   [winding order editor](../orders/winding-order.md) opens; the new
   winding order is already linked to the braiding order, and you can
   apply target values such as target bobbin count and length per bobbin from the braiding order.
4. Work through the tabs (**Order**, **Customer**, **Machine**,
   **Material and bobbin**, **Winding**), selecting the
   bobbin winding machine from step 1. All fields — including the
   color breakdown, which is suggested from the carrier setup of the linked design,
   and the winding technology data — are explained on the
   reference page [Winding order editor](../orders/winding-order.md).

!!! tip "Winding order without braiding order"
    You create a free winding order without a link via
    **New order** → **New winding order**. The link can also be
    set or removed later in the editor.

## Step 3: Calculate target values { #schritt-3-sollwerte-berechnen }

In the **Winding** tab of the winding order, **calculator icons** sit directly at
the target value fields:

* At **Length per bobbin**: opens the calculation
  [Bobbin capacity](../calculations/winding/bobbin-capacity.md) — the
  result is applied as the length per bobbin.
* At **Total length**: opens the calculation
  [Winding time](../calculations/winding/winding-time.md), with which you estimate the duration
  of the winding item.

For further planning, the chapter
[Calculations > Winding](../calculations/winding/index.md) provides further calculators,
including:

* [Material demand](../calculations/winding/material-demand.md) — total length
  and total weight including reserve
* [Bobbins from supplier spool](../calculations/winding/from-supplier-spool.md)
  — how many bobbins a supplier spool yields
* [Number of bobbin winding machines](../calculations/winding/number-of-winders.md) — how
  many braiding machines one bobbin winding machine can supply
* [Yarn tension](../calculations/winding/yarn-tension.md) and
  [Yarn speed](../calculations/winding/line-speed.md) — guide values
  for the winding technology

The common structure of all calculation pages is described under
[How calculation pages are structured](../basics/calc-page-anatomy.md).

## Step 4: Save { #schritt-4-speichern }

Click **Save winding order**. The winding order appears in the
[order overview](../orders/index.md) — there you can restrict the list to
winding orders using the order type filter; for the linked
braiding order, the winding order is shown as a link.

## Step 5: Print { #schritt-5-drucken }

1. In the winding order, click **Print**.
2. If there are several templates, select the desired one (for winding orders,
   the *Default Winding Order* template is pre-selected).
3. Check the print preview and start printing.

The printout contains the winding target values and the color breakdown for
the winding department. Details: [Print order](../orders/print.md); your own templates:
[Print editor](../print-templates/index.md).

## Result { #ergebnis }

* The winding order is saved, linked to the braiding order and
  contains calculated target values (target bobbin count, length per bobbin,
  total length).
* The accompanying sheet for the winding department is printed.
* If a bobbin winding machine is selected in the winding order, the order appears in the
  [Machine Fleet](../machine-park/index.md) at this machine.

## If something does not work { #wenn-etwas-nicht-klappt }

* The printout looks wrong or nothing happens →
  [Print problems](../help/print-problems.md)
* You cannot create any more orders (trial version) →
  [Trial version and licence quotas](../basics/trial-quotas.md)
* The bobbin winding machine is missing from the selection → check the master data, see
  [Bobbin winding machines](../master-data/winding-machines.md)
* Further help → [Help overview](../help/index.md) and
  [Contact support](../help/support.md)
