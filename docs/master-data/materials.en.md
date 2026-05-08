# Materials

The material editor is where you maintain the materials used in your
braids - wires, strands, yarns, threads.

> :material-image-area: *Screenshot: Material editor with a populated list*

## Material properties

> :material-alert-circle-outline: **TODO** *Field names to be validated against the running editor. Derived from code:*

| Field               | Description                                                 |
|---------------------|-------------------------------------------------------------|
| Name                | Plain-text name (e.g. "Wire 0.2 mm galvanised")             |
| Material type       | Wire, yarn, strand, ...                                     |
| Diameter            | in mm                                                       |
| Linear density      | in dtex / tex / g/m                                         |
| Color               | Reference to colors master data                             |
| Manufacturer        | Optional                                                    |
| Note                | Free text                                                   |

## Create a material

1. Open *Master Data > Materials* in the navigation tree.
2. Click :material-plus: **New**.
3. Fill in the fields.
4. **Save**.

## Use a material in a calculation

In most calculations you can pick a material from the list instead of
entering values manually. The values (diameter, linear density, etc.)
are then taken over automatically.

> :material-image-area: *Screenshot: Material picker in a calculation*

!!! tip "Maintain recurring materials once"
    Maintain frequently used materials cleanly once - this saves typing
    on every calculation and avoids data entry mistakes.
