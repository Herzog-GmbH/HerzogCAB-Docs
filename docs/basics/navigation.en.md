# Navigating the app

!!! info "Concept — The navigation tree on the left: all entries, groups and operating rules"

The navigation at the left edge of the window is the central route to all modules
of Herzog CAB. This page shows the complete tree and explains how
you operate it.

## The navigation tree { #der-navigationsbaum }

```
Home
Favorites                        (your pinned entries)
Orders
Machine Fleet
Catalogue                        (Herzog catalogue, not in Herzog CAB Designer)
Factory Planner
Designer
Calculations
  ├─ Material
  │    ├─ Fineness
  │    ├─ Fineness conversion
  │    ├─ Material diameter from material
  │    ├─ Material diameter from product
  │    ├─ Ply count from product
  │    ├─ Material length on bobbin
  │    └─ Bobbin volume
  ├─ Product
  │    ├─ Braiding angle
  │    ├─ Braiding angle from take-up
  │    ├─ Braid density
  │    ├─ Product length
  │    ├─ Product length per drum
  │    ├─ Drum and take-up unit selection
  │    ├─ Product weight
  │    ├─ Product diameter
  │    ├─ Core-cover product
  │    ├─ Braid density conversion
  │    └─ Hollow braid
  │         ├─ Number of carriers
  │         ├─ Diameter
  │         ├─ Material width
  │         └─ Covering
  ├─ Production
  │    ├─ Production speed
  │    ├─ Machine sizing
  │    ├─ Machine runtime per bobbin set
  │    └─ Change gears rubber feed device
  └─ Winding
       ├─ Winding time
       ├─ Yarn speed
       ├─ Yarn tension
       ├─ Bobbin capacity
       ├─ Bobbin weight
       ├─ Material demand
       ├─ Bobbins from supplier spool
       ├─ Residual length by weight
       └─ Number of bobbin winding machines
Master data
  ├─ Designs
  ├─ Colors
  ├─ Braiding machines
  ├─ Floor plans
  ├─ Customers
  ├─ Materials
  ├─ Media
  ├─ Bobbins
  ├─ Drums
  ├─ Bobbin winding machines
  ├─ Take-up units
  ├─ Pay-off units
  └─ Creels
Print editor
System administration            (visible only with administration permissions)
  ├─ Users
  ├─ Roles
  ├─ Profiles
  ├─ Storage location
  ├─ Company
  ├─ Authentication
  └─ Parameter Explorer
```

You find the target pages of the entries in the manual under
[Orders](../orders/index.md), [Machine Fleet](../machine-park/index.md),
[Herzog catalogue](../catalog/index.md), [Factory Planner](../hall-planner/index.md), [Designer](../designer/index.md),
[Calculations](../calculations/index.md),
[Master data](../master-data/index.md),
[Print editor](../print-templates/index.md),
[Parameter Explorer](../parameter-overview/index.md) and
[System administration](../admin/index.md).

!!! info "Parameter Explorer now in System administration"
    The **Parameter Explorer** is a view for specialists and is no longer
    in the main navigation, but the last item under
    **System administration**. Users without administration permission who are allowed to
    open the Parameter Explorer still find it at the very bottom of the
    navigation.

## How to operate the tree { #so-bedienen-sie-den-baum }

* **One click is enough.** Clicking an entry opens the corresponding
  page; clicking a group expands or collapses it. You can also
  click the small **arrow (chevron)** in front of the
  group name to expand/collapse it.
* **Groups with their own overview page.** The groups **Calculations**
  (including the subgroups *Material*, *Product*, *Hollow braid*, *Production*,
  *Winding*) and **Master data** additionally open a
  tile overview of their area when clicked.
* **Pinning favorites.** With a **Right-click** on an entry you pin
  it at the very top under *Favorites* — details under
  [Favorites](favorites.md).
* **Collapsing the navigation.** Using the arrow icon in the header of the
  navigation (or *View > Navigation*) you reduce it to an
  icon bar and expand it again. When collapsed, it is enough to move the
  mouse over the bar: the navigation expands and **floats
  over the content** until the mouse leaves it again. Below a window width of 1500 pixels,
  it collapses on its own. The structure is described under
  [Interface overview](interface.md#navigation-links).

!!! info "You see fewer entries?"
    The navigation only shows areas for which your
    [role](../admin/roles.md) has the necessary permission. If, for example, the
    permission "View master data" is missing, the entire
    *Master data* group disappears. **System administration** only appears for users with
    at least one administration permission — and within it only the sub-items
    covered by their own set of permissions.

!!! tip "Similar names, different pages"
    Three pairs are easily confused:
    **Machine Fleet** shows the operating state of all machines, while
    *Master data > Braiding machines* or *Bobbin winding machines* manage the machine data
    itself. **Designer** is the drawing tool, *Master data >
    Designs* the library of all saved designs. **Factory Planner**
    equips floor plans with machines, *Master data > Floor plans* edits
    the building geometry.

## Inputs are kept during the session { #eingaben-bleiben-in-der-sitzung-erhalten }

Within a session, Herzog CAB remembers your inputs in the
calculations. You can switch to another page and open the calculation
again later with all values. After a program restart, the
values are reset. You load earlier calculations again via the
[history](history.md).

## Help for the current page { #hilfe-zur-aktuellen-seite }

With ++f1++ you open the page of this manual that matches the page
you are currently on; ++shift+f1++ starts the
[guided tour](guided-tour.md) for it. A complete list of
keyboard shortcuts can be found under [Keyboard shortcuts](../appendix/keyboard-shortcuts.md).

## Related pages { #verwandte-seiten }

* [Interface overview](interface.md)
* [Favorites](favorites.md)
* [Home page (Home)](home.md)
* [Roles and permissions](../admin/roles.md)
