# Calculate material correctly

!!! example "Guide — at the end you know the suitable material for your product, the material length per bobbin as well as product length and product weight"

**Prerequisites:**

* The materials are recorded with **Density** and **Titer** in the
  [material master data](../master-data/materials.md) — the
  material selection lists of the calculations are filled from there and apply
  density and fineness automatically.
* The [bobbin formats](../master-data/bobbins.md) are maintained with their
  dimensions.
* You know the common structure of the calculation pages —
  see [How calculation pages are structured](../basics/calc-page-anatomy.md).

```mermaid
flowchart LR
  A["Maintain master data"] --> B["Determine fineness"]
  B --> C["Material diameter & ply count"]
  C --> D["Material length on bobbin"]
  D --> E["Product length & weight"]
```

The steps build on each other — but you can also use just a single
calculation from the chain at any time. You can reach all calculators via the
tile overview [Calculations](../calculations/index.md) or via the
navigation bar on the left.

## Step 1: Maintain material master data { #schritt-1-material-stammdaten-pflegen }

Under *Master data > Materials*, check whether the material has been created with name, density
and titer; if not, create it via **New material**
(reference: [Materials](../master-data/materials.md)). The maintenance effort
pays off: in all subsequent calculations, simply selecting the
material from the selection list is then sufficient.

## Step 2: Determine and convert the fineness { #schritt-2-feinheit-bestimmen-und-umrechnen }

* With the calculation
  [Fineness](../calculations/material/linear-density.md) you determine
  which yarn count is required for the desired braid.
* If supplier specifications are in a different unit (tex, dtex, den,
  Nm, Ne), use the live converter
  [Fineness conversion](../calculations/material/linear-density-conversion.md).

## Step 3: Determine material diameter and ply count { #schritt-3-materialdurchmesser-und-fachung-ermitteln }

Depending on what you know:

* You know the **material** (fineness, density) and want to know its
  diameter →
  [Material diameter from material](../calculations/material/material-diameter.md).
* You know the **finished product** (diameter, number of carriers, braiding angle)
  and are looking for the suitable yarn →
  [Material diameter from product](../calculations/material/material-diameter-product.md)
  — this calculation additionally suggests a suitable material from your
  material database.
* You want to know **how many threads per carrier** the selected
  material must be used with →
  [Ply count from product](../calculations/material/required-ply.md).

## Step 4: Calculate the material length on the bobbin { #schritt-4-materiallange-auf-der-spule-berechnen }

* [Bobbin volume](../calculations/material/bobbin-volume.md) provides the
  capacity volume of a bobbin from its dimensions (if the
  [bobbin master data](../master-data/bobbins.md) is maintained, it is already
  stored there).
* [Material length on bobbin](../calculations/material/material-length.md)
  calculates how many metres of your material fit on the selected bobbin.

## Step 5: Calculate product length and product weight { #schritt-5-produktlange-und-produktgewicht-berechnen }

* [Product length](../calculations/product/rope-length.md) — how many metres
  of finished product a bobbin set yields.
* [Product weight](../calculations/product/rope-weight.md) — the weight of the
  produced braid section.
* For take-up winding:
  [Product length per drum](../calculations/product/rope-length-on-drum.md).

## Result { #ergebnis }

* You have a continuous calculation chain from raw material to the
  finished product.
* Every completed calculation is stored in the
  [History](../basics/history.md) and can be reloaded from there with the
  inputs used at the time.
* You can output the results via [print templates](../print-templates/index.md)
  and use them in the [braiding order](../orders/braiding-order.md) —
  many of these calculations are linked directly at the fields there.

## If something does not work { #wenn-etwas-nicht-klappt }

* A field has a red border → the input is missing or invalid; details
  on input validation under
  [How calculation pages are structured](../basics/calc-page-anatomy.md)
* The material does not appear in the selection list → check the master data, see
  [Materials](../master-data/materials.md)
* The calculation quota of the trial version is used up →
  [Trial version and licence quotas](../basics/trial-quotas.md)
* Further help → [Help overview](../help/index.md) and
  [Contact support](../help/support.md)
