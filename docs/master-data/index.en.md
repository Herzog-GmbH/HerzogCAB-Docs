# Master data

!!! abstract "Reference — Overview of all master data areas"

In **Master data** you store all data that you need again and again in
calculations, in the Designer and in orders: customers, designs, machines,
materials, bobbins, drums and colors. Master data belongs to the workspace – it
is therefore shared by all operators who work with the same
workspace.

You reach the areas via the navigation item **Master data**. It first opens
an overview with one tile per master data area.

![Master data overview with the tiles of all master data areas.](../assets/screenshots/master-data/materialien-uebersicht.png)

## The areas { #die-bereiche }

<div class="grid cards" markdown>

- :material-account-group: **Customers**

    ---

    Company and contact details of your customers for orders and print templates.

    [:octicons-arrow-right-24: Customers](customers.md)

- :material-view-grid-outline: **Designs**

    ---

    The design library: manage saved braid patterns in folders.

    [:octicons-arrow-right-24: Designs](designs.md)

- :material-robot-industrial: **Braiding machines**

    ---

    Create braiding machines – with category, braid type, carriers, image and
    documents.

    [:octicons-arrow-right-24: Braiding machines](braiding-machines.md)

- :material-floor-plan: **Floor plans**

    ---

    Draw hall floor plans (walls and areas) for the Factory Planner.

    [:octicons-arrow-right-24: Floor plans](floor-plans.md)

- :material-image-multiple: **Media**

    ---

    Central image store for machines, print templates and the company.

    [:octicons-arrow-right-24: Media](media.md)

- :material-cube-outline: **Materials**

    ---

    Yarns, wires, strands and threads with density and titer.

    [:octicons-arrow-right-24: Materials](materials.md)

- :material-record-circle-outline: **Bobbins**

    ---

    Bobbin formats (dimensions and volume) and their machine types.

    [:octicons-arrow-right-24: Bobbins](bobbins.md)

- :material-barrel: **Drums**

    ---

    Drums of the take-up units with dimensions, bobbin volume and empty weight.

    [:octicons-arrow-right-24: Drums](drums.md)

- :material-movie-roll: **Bobbin winding machines**

    ---

    Bobbin winding machines of the series SP, SPA and HLM with winding technology.

    [:octicons-arrow-right-24: Bobbin winding machines](winding-machines.md)

- :material-tape-drive: **Take-up units**

    ---

    Take-up units with drum dimensions, load capacity, design and reel.

    [:octicons-arrow-right-24: Take-up units](take-up-machines.md)

- :material-rotate-left: **Pay-off units**

    ---

    Pay-off units with drum dimensions, load capacity, drum lift and unwinding tension.

    [:octicons-arrow-right-24: Pay-off units](pay-off-machines.md)

- :material-view-grid-plus-outline: **Creels**

    ---

    Pay-off creels and pay-off stands with pay-off positions, bobbins and yarn tension.

    [:octicons-arrow-right-24: Creels](creels.md)

- :material-palette: **Colors**

    ---

    Color palette for the Designer, with RAL and Pantone reference colors.

    [:octicons-arrow-right-24: Colors](colors.md)

</div>

## General operation { #allgemeine-bedienung }

Most master data editors share the same layout:

* **List** on the left – a search field and all existing entries
  as cards. Below the search field you see how many entries match the current
  search.
* **Detail view** on the right – the properties of the entry selected in the
  list.
* **Buttons** – for creating (e.g. **New material**, **New Bobbin**),
  **Save** and **Delete** (with confirmation prompt).

How to search and filter lists is described for all areas in
[Search and filter](../basics/search-filter.md).

!!! info "Special cases"
    Some areas differ from this layout: **Designs** is a
    folder library (like a file explorer); **Braiding machines**,
    **Bobbin winding machines**, **Take-up units**, **Pay-off units** and **Creels** show
    their machines as cards and open a separate dialog for creating and
    editing.

!!! tip "Bobbins, drums and machines from the Herzog catalogue"
    Since version 2.1.0, new workspace folders start without supplied
    bobbins and drums. You take over Herzog bobbins and drums with
    **From Herzog catalogue …**; you create Herzog machines directly in the
    [Herzog catalogue](../catalog/index.md).

!!! warning "Permission required"
    To create, change or delete master data you need the
    permission **Edit master data**. Operators with read-only
    permission can only view the data. In the
    [trial version](../basics/trial-quotas.md), customers, designs and machines
    are limited in number.
