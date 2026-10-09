# From customer order to machine sheet

!!! example "Guide — at the end you have a complete, printed braiding order that is assigned to a machine and appears in the Machine Fleet"

**Prerequisites:**

* The [master data](../master-data/index.md) is maintained: at least one
  [material](../master-data/materials.md), one
  [bobbin](../master-data/bobbins.md) and one
  [braiding machine](../master-data/braiding-machines.md).
* You have permission to create customers and orders (if in doubt:
  [Roles and permissions](../admin/roles.md)).
* Optional: a finished design in the
  [design library](../master-data/designs.md) — but you can also create it
  along the way.

```mermaid
flowchart LR
  A["Create customer"] --> B["Provide design & material"]
  B --> C["Create braiding order"]
  C --> D["Use calculations"]
  D --> E["Print"]
  E --> F["Check Machine Fleet"]
```

## Step 1: Create a customer { #schritt-1-kunde-anlegen }

1. Open *Master data > Customers* and click **New Customer**.
2. Enter the customer data and click **Save**.

All fields of the customer form are explained on the reference page
[Customers](../master-data/customers.md). Newly saved customers are
immediately available in the customer selection of the order editor.

!!! tip "Shortcut"
    You can also create the customer later directly from within the order —
    the braiding order editor provides a separate button for this in the
    **Customer** tab (see [Braiding order editor](../orders/braiding-order.md)).

## Step 2: Provide design and material { #schritt-2-design-und-material-bereitstellen }

1. Check whether the desired design is available in the
   [design library](../master-data/designs.md). If not,
   create it first — the workflow
   [Create and print a design](design-from-scratch.md) guides you through
   the Designer.
2. Under *Master data > Materials*, check whether the braiding material is recorded with
   density and titer (reference:
   [Materials](../master-data/materials.md)).

## Step 3: Create a braiding order { #schritt-3-flechtauftrag-anlegen }

1. Open the navigation item **Orders** (reference:
   [Order overview](../orders/index.md)).
2. Click **New order** and select **New braiding order**.
   The [braiding order editor](../orders/braiding-order.md) opens.
3. Work through the tabs from left to right: **Customer**, **Order**,
   **Machine**, **Material**, **Bobbin**, **Product**, **Production**,
   **Design**. What each field means is described on the reference page —
   here only the most important stages:
    * In the **Machine** tab, select the braiding machine from your master data.
      This assigns the order to the machine, and it later appears in the
      Machine Fleet.
    * In the **Design** tab, load the design from the library or create
      a new one directly via **New design**.
4. Click **Save order**.

## Step 4: Use calculations { #schritt-4-berechnungen-nutzen }

Many fields in the order have a **calculator icon** right next to them that
opens the matching calculation as a window (e.g. braiding angle or
product length) — the result is applied to the order. The common
structure of all calculation pages is described under
[How calculation pages are structured](../basics/calc-page-anatomy.md);
you can find all available calculations in the chapter
[Calculations](../calculations/index.md).

## Step 5: Check the overview { #schritt-5-ubersicht-prufen }

Switch to the **Overview** tab. It summarizes the complete order;
the **Bobbin Table** sub-tab shows the setup with colors for each
carrier position (details: [Braiding order editor](../orders/braiding-order.md)).

## Step 6: Print the machine sheet { #schritt-6-maschinenzettel-drucken }

1. In the order, click **Print**.
2. If several print templates are available, select the desired template in the
   **Choose print template** dialog (e.g. *Default Order*).
3. Check the print preview and start printing.

The printout is the production accompanying sheet ("machine sheet") for the
workshop. Details on the preview and on the QR code with which the operator opens the
mobile order view on a smartphone are described under
[Print order](../orders/print.md). You control the appearance and content of the printout
with your own [print templates](../print-templates/index.md) — see the
workflow [Create a print template](create-print-template.md).

## Step 7: Check the machine in the Machine Fleet { #schritt-7-maschine-im-maschinenpark-prufen }

Open the navigation item **Machine Fleet** (reference:
[Machine Fleet](../machine-park/index.md)). The machine selected in step 3
now shows the order in its list of assigned orders;
the machine's status light follows the order status. You set the
status itself (Draft, Released, In production, Completed)
in the order in the **Order** tab.

## Result { #ergebnis }

* The braiding order is saved and appears in the
  [order overview](../orders/index.md) and under "Recently opened" on
  the [Home page](../basics/home.md).
* The machine sheet is printed.
* The [Machine Fleet](../machine-park/index.md) shows the order at the
  assigned machine.

## If something does not work { #wenn-etwas-nicht-klappt }

* The printout looks wrong or nothing happens →
  [Print problems](../help/print-problems.md)
* You cannot create any more orders (trial version) →
  [Trial version and licence quotas](../basics/trial-quotas.md) and
  [Licence problems](../help/license-problems.md)
* Buttons are greyed out → you are probably missing a permission,
  see [Roles and permissions](../admin/roles.md)
* Further help → [Help overview](../help/index.md) and
  [Contact support](../help/support.md)
