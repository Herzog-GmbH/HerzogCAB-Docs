# Master Data

**Master data** is where you keep everything that you need over and over
again in calculations and jobs. Master data belongs to the workspace - it
is shared by all operators using the same workspace.

## Areas

| Area                            | Contents                                               |
|---------------------------------|--------------------------------------------------------|
| [Materials](materialien.md)  | Wires, yarns, threads with their properties           |
| [Bobbins](spulen.md)         | Bobbin shapes and their volumes                       |
| [Machines](maschinen.md)     | Braiding machines in your fleet                       |
| [Customers](kunden.md)       | Customer master data for jobs                         |
| [Colors](farben.md)          | Color palette for designs                             |

## Common operation

All master data editors are similarly structured:

* **List** on the left - all existing entries.
* **Detail view** on the right - properties of the selected entry.
* **Action bar** at the top:
  * :material-plus: **New** - create entry
  * :material-content-copy: **Duplicate** - copy an existing entry
  * :material-delete: **Delete** - delete an entry (confirmation)
  * :material-content-save: **Save** - persist changes
  * :material-undo: **Discard** - revert unsaved changes

> :material-image-area: *Screenshot: Master data overview (Material editor)*

!!! warning "Permission required"
    Creating, changing or deleting master data requires the **Edit
    master data** permission. Operators with the *Production* or
    *Read-only* role can only view the data.
