# Search and Filter

!!! info "Concept — The recurring search, filter and sort patterns in lists"

Whether order overview, Machine Fleet or master data lists: throughout
Herzog CAB you find the same operating patterns for quickly narrowing long lists down
to what matters. This page explains the patterns once, in one place;
the reference pages of the modules only mention their special features.

## The search field { #das-suchfeld }

Almost every list has a **search field** at the top. It filters **as you
type** — you do not have to press ++enter++. The grey placeholder text in the
empty field tells you which details are searched, for example:

| List | Searches |
|---|---|
| [Orders](../orders/index.md) | Order name, number, customer, machine |
| [Machine Fleet](../machine-park/index.md) | Name, type, serial number, group, location |
| [Customers](../master-data/customers.md) | Name, number, company, contact, e-mail, city |
| [Materials](../master-data/materials.md) | Name, brand, note |
| [Bobbins](../master-data/bobbins.md) | Diameter, volume, machine type |
| [Colors](../master-data/colors.md) | Identifier, name, hex value, reference color |

To clear the search, simply empty the field again.

## Filter selection lists { #filter-auswahllisten }

Next to the search field, depending on the list, there are one or more
**filter selection lists**. The first entry ("All …") clears the respective
filter again. Examples:

* **Order overview:** *Order type* (All / Braiding orders /
  Winding orders), *Status* (Draft, Released, In production,
  Completed) and *Period* (Today, This week, Last week, This
  month, Last 30 days).
* **Machine Fleet:** *Machine type* (braiding/winding machines), *Category*,
  *Status* (Error reported, In production, Orders waiting, No active
  orders), *Group*, *Braid type* and *Location*.
* **Bobbins:** filter by *Machine type*.

Search and filters work **together**: Only what matches the
search term **and** all filters set is displayed. If nothing matches any more,
the list shows a hint such as "No machines match the current
filters." — then relax the search or filters.

## Sorting { #sortierung }

Many lists also have a **Sorting** selection list, e.g.
*Newest first*, *Oldest first*, *Production date* and *Order date*
in the order overview or *Name*, *Status (errors first)*,
*Machine type* and *Location* in the Machine Fleet. Sorting only changes
the order, not the selection.

## Switching the view { #ansicht-umschalten }

Some lists offer a switch at the top right between the
**Cards** view (large tiles with image and key figures) and the
**List** view (compact rows) — for example the
[Machine Fleet](../machine-park/index.md). The selected view only affects
the display; search, filters and sorting apply in both.

## Related pages { #verwandte-seiten }

* [Order overview](../orders/index.md)
* [Machine Fleet](../machine-park/index.md)
* [Master data](../master-data/index.md)
