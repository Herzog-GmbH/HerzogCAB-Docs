# Web app interface

!!! info "Concept — How the web app is structured: sidebar, header, tabs, user menu, lists and dialogs, operation on tablet and smartphone"

## The frame { #der-rahmen }

![Frame of the web app: sidebar on the left with one entry per module, header with company, language and user menu, content on the right.](../assets/screenshots/web/oberflaeche.png)

| Area | Content |
|---|---|
| **Sidebar** (left) | One entry per module (see [below](#eintrage-der-seitenleiste)), each only with the matching permission. At the bottom your name, the account and the **Sign out** icon. The sidebar only answers the question "which module am I in" — subpages and actions are located in the page itself. |
| **Header** (top) | On the left the name of the account with a label (e.g. *internal*, the edition or *Trial: n days left*), on the right the **language selection** and the **user menu**. |
| **Content** | The current page with the **page title**, actions to the right of it (e.g. **New braiding order**) and below it **tabs** for subpages (e.g. *Materials*, *Bobbins*, *Drums*, *Colors*, *Customers* under Master data or the machine kinds in the Herzog catalogue). |

### Sidebar entries { #eintrage-der-seitenleiste }

From top to bottom, each only with the stated permission
([Roles](roles.md)):

| Entry | Visible with | Page |
|---|---|---|
| **Home page** | always | [Home page](start.md) |
| **Orders** | *View orders* | [Orders](orders.md) |
| **Shop floor view** | *View orders* and *View master data* | Orders per machine with their status |
| **Calculations** | *Run calculations* | [Calculations](calculations.md) |
| **Designs** | *View designer* | [Designs and Designer](designer.md) |
| **Machines** | *View master data* | [Machines](machines.md) |
| **Catalogue** | *View master data* | [Herzog catalogue](catalog.md) |
| **Master data** | permission for at least one master data tab | [Master data](master-data.md) |
| **Factory Planner** | *View factory planner* | [Factory Planner](hall-planner.md) |
| **Print editor** | *View print templates* | [Print editor](print-editor.md) |
| **Parameter Explorer** | *Open Parameter Explorer* and *View orders* | Parameters of the orders |

Which entries you see also depends on the module: with
*Herzog CAB Designer*, Orders, Shop floor view, Calculations,
Machines, Catalogue, Factory Planner and Parameter Explorer are missing; under Master data
Colors and Customers remain.

## User menu { #benutzermenu }

Clicking your initials or your name at the top right opens the
user menu:

| Entry | Target |
|---|---|
| **Account** (selection) | Only for Herzog employees with several internal accounts: switches the account. |
| **Language** | On a smartphone here instead of in the header. |
| **Settings** | [Language, user, password note](settings.md). |
| **Account and users** | [Edition, modules, seats, users and roles](account.md). |
| **Subscription and orders** | [Activations, trial, ordering an annual subscription or sending an inquiry](subscription.md). |
| **Company** | [Company data and logo for print templates](company.md). |
| **Media library** | [Uploaded images and documents](media.md). |
| **Recycle bin** | [View and restore deleted entries](versions.md#papierkorb). |
| **Roles** | [Roles and permissions](roles.md) — only with the permissions *Manage roles* or *Manage users*. |
| **Import from the desktop app** | [ZIP import and export of the workspace](import.md) — only with the permission *Workspace settings*. |
| **Sign out** | Ends the session. |

## Lists, cards and forms { #listen-karten-und-formulare }

* **Lists** have a **search field** and **Filter** at the top; the number of hits
  is shown next to them (*n of m …*). On narrow screens, tables become
  **Cards**.
* **New…** buttons are to the right of the page title; **Open**
  or a click on the row leads into the editor.
* **Save** is at the top right of the editor. After saving, a
  confirmation (*Saved.*) briefly appears at the bottom edge; errors appear
  as a red message box.
* **Confirmation prompts** (e.g. when deleting) open as a dialog — on a
  smartphone as a sheet from the bottom. Deleted orders, designs, machines,
  master data, hall plans and print templates end up in the
  [recycle bin](versions.md#papierkorb).
* **Versions:** Editors have a **Versions** button with the earlier
  versions of the entry, see [Versions and recycle bin](versions.md).
* **Version conflict:** If two people edit the same entry, the web app reports
  on the second save *"This entry has since been changed by someone
  else. Please reload."* — reload the page and enter
  your change again. You can then see what the other person saved under
  **Versions**.

## Tablet and smartphone { #tablet-und-smartphone }

The web app adapts to the screen width:

* **From 768 px (tablet):** sidebar and header as on the desktop, lists
  as cards depending on the space.
* **Smartphone:** The sidebar becomes a **drawer**, which you open via the
  menu icon at the top left. At the bottom edge there is a **tab bar**
  with **Home**, **Orders**, **Calculators**, **Designs** and **More** (opens
  the drawer). In the drawing areas (Designer, Factory Planner) you zoom
  with two fingers.

!!! tip "As an app on the home screen"
    Most browsers offer to *add the page to the home screen*.
    The web app then starts like an app — without an address bar.

## Related pages { #verwandte-seiten }

* [Sign in and select account](login.md)
* [Home page](start.md)
* [Versions and recycle bin](versions.md)
* [Interface at a glance (desktop app)](../basics/interface.md) — for comparison
