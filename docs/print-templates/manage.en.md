# Manage templates

!!! abstract "Reference — create, choose and delete print templates"

You open the print editor via the navigation item **Print editor**. At the top
you choose the template to edit; on the right you find the actions for
managing it.

![Print editor with template selection and actions on the right.](../assets/screenshots/print-templates/druck-editor.png)

## Choose a template { #vorlage-wahlen }

Use the **Templates** selection field (e.g. *Default Order*) at the bottom right
to switch between the existing templates. The selected template is
displayed in the editor immediately.

## Actions { #aktionen }

| Action | Effect |
|---|---|
| **New** (tooltip *New template*) | Creates a new, empty template. |
| **Save** | Saves the current template with all changes. If there are unsaved changes, the button is called **Save \*** and is highlighted in blue. If a colleague has saved the same template in the meantime, the most recently saved version applies — see [Multiple users](../basics/multi-user.md). |
| **Delete** (tooltip *Delete template*) | Removes the current template (with confirmation prompt). |
| **Usage** | Specifies what the template is for: calculation, design or order. See [Editor layout](editor.md). |

If you leave the editor with unsaved changes, Herzog CAB asks
whether you want to save first or discard the changes.

## File location { #speicherort }

All templates are stored as files under `Printouts/templates/` in the active
workspace. This means they can also be backed up or exchanged between workstations
that use the same workspace.

!!! tip "Start with a copy"
    Instead of starting from scratch, start from the supplied template
    *Default Order*: adapt it, save it under a new name – done.

!!! warning "Permission required"
    To **view templates**, the permission **View print templates** is sufficient.
    To create, change, save and delete you additionally need
    **Edit print templates**. More on this under [Roles](../admin/roles.md).

## Related pages { #verwandte-seiten }

* [Editor layout](editor.md) – element palette, filter, page settings
* [Elements and placeholders](elements.md) – all building blocks of the element palette in detail
* [Preview and print](preview-and-print.md) – page format, preview, output
* [Create a print template](../tasks/create-print-template.md) – step-by-step guide
* [Orders → Print](../orders/print.md) – where order templates are used
* [Designer → Save and print](../designer/save-print.md) – where design templates are used
