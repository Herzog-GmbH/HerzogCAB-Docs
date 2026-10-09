# Release notes

!!! abstract "Reference — What changed in which version"

## Next version (in preparation) { #nachste-version-in-vorbereitung }

### New { #neu }

* **Multiple users in the same workspace folder** – materials, bobbins,
  drums, own machines, orders, customers, colors, floor plans,
  layouts, designs and print templates are saved individually and with a lock;
  a colleague's changes to other entries are no longer
  lost. If someone has changed or deleted the same entry in the meantime,
  Herzog CAB asks what to do (**Overwrite**, **Save as
  copy**, **Reload**) and states who changed it, when and on which computer.
  Old versions are retained. **All computers using the
  shared folder need the new version.** See
  [Multiple users in the same workspace folder](../basics/multi-user.md).
* **Selectable braiding angle reference** – under *Settings > General >
  Braiding angle* you choose whether Herzog CAB displays the braiding angle relative to the
  transverse direction (Herzog, default) or to the braid axis (technical literature)
  — in all calculations, in the Designer, in the order and on
  printouts. Saved values remain unchanged; the short hint at the
  field shows both values. With a customer account, the choice applies to your user.
  See [General](../admin/settings/appearance.md#flechtwinkel).
* **Plying colors in the Designer** – from ply count 2 onwards, each yarn of a
  carrier gets its own color, via the yarn selector in the toolbar
  or the dialog *Plying colors…* by right-clicking in the carrier table.
  The yarns appear as stripes in the braid pattern, in the
  setup overview, in 3D, on the printout, in the order and in the
  color breakdown of the winding order. See
  [Plying colors](../designer/painting.md#fachungsfarben-farbe-je-garn).
* **New home page** – uses the full window width in one to three
  columns: welcome with quick actions, order counters, the card
  *Production* with the tabs *Overdue*, *This week* and
  *Coming up* (shown as a table when wide enough), favorites as tiles
  and *Recently opened* with the icon of each calculation. See
  [Home page](../basics/home.md).
* **New sign-in dialog** – header band with account name and running braid,
  authenticator app code in six boxes that check automatically after the sixth
  digit. See [Signing in and out](../admin/login.md).
* **F1 opens the manual** – ++f1++ and the new menu item *Help >
  Manual* open the page of this manual that matches the page or
  dialog that has the focus, also in dialogs. The guided tour of the
  current page now starts with ++shift+f1++. See
  [Keyboard shortcuts](keyboard-shortcuts.md#hilfe-tasten).

### Improvements { #verbesserungen }

* **Navigation** – when expanded with the mouse, it floats over the content
  instead of pushing it aside; below a window width of 1500 pixels it collapses
  automatically. The window can be reduced to 960 × 600 pixels. The
  Parameter Explorer is now located under *System administration*; the items
  of the *About* menu are in the *Help* menu. See
  [Interface overview](../basics/interface.md).
* **Clearer pages** – simple title bar instead of a header card,
  explanatory sentences as a short hint at the card heading, smaller buttons
  in Herzog blue, calculator pages scroll instead of being cut off; braiding and
  winding order with a single-line header.
* **History** only where it shows something: on the pages under
  *Calculations*. See [Calculation history](../basics/history.md).
* **Settings** – without the *Storage locations* tab (the paths are under
  [Storage location](../admin/storage-location.md)), buttons **Save**
  and **Cancel** at the bottom right.
* **My profile** – for users from the customer account, name and e-mail are
  read-only; **Change in licence portal** opens the matching page.
  See [My profile](../admin/my-profile.md).
* **User synchronisation** – at program start, Herzog CAB synchronises the
  user list with the customer account; users removed from the account are
  deactivated. See [Users](../admin/users.md).
* **Herzog catalogue from the licence server** – new Herzog models, bobbins and
  drums arrive without a program update. See
  [Herzog catalogue](../catalog/index.md).
* **Network licence (CodeMeter)** – Herzog CAB holds the seat until the
  program is closed; if all seats are taken, *All seats taken* appears.
  See [Licence problems](../help/license-problems.md).

### Security { #sicherheit }

* **Web server on the network only with a password** – without a password, the
  web interface can only be reached on the computer itself; with a password
  (at least 8 characters) it can be reached on the company network after signing in. The password is
  no longer stored in plain text; after failed attempts, sign-in is
  briefly locked. **If you use tablets or phones, set a password after the
  update.** See [Web server and QR code](../admin/settings/web-server.md).

### Compatibility { #kompatibilitat }

* **Update all computers using the shared workspace folder at the same
  time** — older versions do not respect the new lock and
  can discard changes made by other computers; on shared profiles with a
  web server password, their web interface is locked.

## Version 2.1.0 (September 2026)

### New { #neu_1 }

* **Floating licences** – the program and Herzog CAB Web share the
  seats of the account. Each computer on which Herzog CAB is running takes one
  seat and releases it immediately on exit (after a crash
  at the latest after 15 minutes). Anyone working in Herzog CAB Web also
  takes a seat, until 15 minutes after the last activity — anyone working in the
  program and in the browser at the same time therefore takes two. If all
  seats are taken, Herzog CAB shows who is currently working; the licence tab
  shows how many seats are taken. See
  [Licence and cloud](../admin/settings/license.md).
* **Stay signed in** – the sign-in dialog has a check box
  *Stay signed in*, enabled by default. Herzog CAB then starts on this
  computer without signing in again. No password is stored,
  but an encrypted identifier for this user on this
  computer; it expires 30 days after last use. Signing out in the
  program, a new password or locking the computer in the
  licence portal ends it. See
  [Signing in and obtaining a licence](../setup/activate-license.md).
* **Company storage location** – the customer account remembers the folder on
  your file server in which your company works with Herzog CAB. A new
  computer shows it after signing in and connects with one
  click. The first computer of a company chooses once between *On this computer
  only* and a network drive; under *System administration >
  Storage location*, a local workspace folder can be moved to a network drive.
  See [Storage location](../admin/storage-location.md).
* **Take-up winders as a separate machine type** – own master data page and
  own creation dialog with drum dimensions, load capacity, tension control, image and
  documents, own filter in the Machine Fleet and own group in the
  Factory Planner. Series AW, AWS, AWST, AWSP, AWSA and AWH. See
  [Take-up winders](../master-data/take-up-machines.md).
* **Pay-offs as a separate machine type** – for material such as core, rope
  or cable that runs off a drum into the downstream machine:
  drum dimensions, load capacity, drum stroke and pay-off tension. Series AB,
  ABS, ABST and ABA. See [Pay-offs](../master-data/pay-off-machines.md).
* **Creels as a separate machine type** – pay-off creels and pay-off stands with
  pay-off positions (total and of which active), take-up, drive, bobbin type and
  size, yarn tension, monitoring and material. Series GU, GR, GRP,
  GRG, GM, GMG, GS, EGA, VG and AL. See [Creels](../master-data/creels.md).
* **Drum database** – create drums once and reuse them in calculations.
  You take over Herzog drums from the Herzog catalogue;
  your own are added alongside. The bobbin volume is derived from winding diameter,
  core diameter and traverse width and can still be overwritten.
  *Product length per drum* now selects the drum from the database
  instead of asking for three dimensions. See [Drums](../master-data/drums.md).
* **Drum and take-up winder selection** – a new calculation leads from the
  carrier loading to the take-up winder: product length and weight, the
  drum suggestion from the drum database and the matching take-up winders
  from the Machine Fleet or the Herzog catalogue. If not everything fits on one
  drum, it is split; fill level and edge clearance are adjustable.
  If a value is missing, the calculation says *not checkable* instead of
  silently *fits*; a core counts towards the weight as in *Core-Cover-Product*.
  See
  [Drum and take-up winder selection](../calculations/product/drum-take-up-selection.md).
* **Take-up winder and drum in the order** – new tab
  [Take-up](../orders/braiding-order.md#tab-aufwicklung) in the
  braiding order: take-up winder and drum are saved with the order,
  the order length is split across the drums per head (also with a
  specified delivery length per drum) and checked against the take-up winder.
  **Calculate suggestion** searches for both. The details appear in the
  overview, in the web view and as placeholders in the print templates;
  a core counts towards the weight per metre, the load capacity and the total weight
  in the **Production** tab.
* **Herzog catalogue** – the new item **Catalogue** directly below the
  Machine Fleet shows Herzog machines of all types, carrier bobbins with
  article numbers as well as drums and reels, with tabs, search, series,
  tiles or list. There you create machines with take-up, setup and
  accessories directly as your own machine, for braiding machines optionally
  together with the matching bobbin; you take over bobbins and drums with one click
  into the master data, also via **From Herzog catalogue …**. The accessories are available
  in all machine dialogs of the master data, for braiding machines the
  take-up as well; machines without an image get one via **Use catalogue
  image**. See [Herzog catalogue](../catalog/index.md).
* **Print templates from Herzog CAB Web** – templates that are created or
  changed in the [Print editor of the web app](../web/print-editor.md)
  now also come back into the program. If you delete the customised version of a
  standard print template on the web, the supplied one applies again
  in the program.

### Improvements { #verbesserungen_1 }

* **One quota, also displayed as such** – a subscription applies to the program
  and Herzog CAB Web together; the licence tab shows *Full version (program
  and web)*, Herzog CAB Web states the edition.
* **Machine pages open faster** – braiding machines, bobbin winding machines,
  take-up winders and pay-offs as well as creels only build their cards when they come into
  view.

### Bug fixes { #fehlerbehebungen }

* **Product weight counts the ply count** – the calculation
  [Product weight](../calculations/product/rope-weight.md) has a field
  **Ply count**; as on all other pages, the fineness applies to one
  thread. Previously, too little weight was calculated for plied yarns, also in the
  order, which now takes the ply count from the **Material** tab.
* **Design from the order** – every save in the window *New design*
  or *Open design* of an order links the design to the
  order, even if the window is then left with **Close**.
  See [Braiding order, tab „Design"](../orders/braiding-order.md#tab-design).

### Compatibility { #kompatibilitat_1 }

* **New workspace folders start without supplied bobbins and
  drums** – take them over from the Herzog catalogue. Existing
  workspace folders remain unchanged.

## Version 2.0.0 (September 2026)

### New { #neu_2 }

* **Customer account instead of dongle** – Herzog CAB can be installed on any
  computer; on first start, the program signs in to your company's customer account
  and obtains its licence from the account's pool. One seat
  per module and computer; a computer that is no longer started returns
  its seat automatically after seven days. See
  [Customer account and invitation](../setup/account.md).
* **One login for everything** – the account user is also the
  program user: the same e-mail address and the same password in the
  desktop app, in the licence portal and in the web app, optionally with a second
  factor (authenticator app). Roles come from the account.
* **Working offline** – after signing in, the program normally runs without a network
  for up to seven days; via *Settings > Licence* an
  offline lease for up to 30 days can be taken.
* **Licence portal** – modules and seats taken, release or
  lock computers, invite colleagues, request or renew licences, download the latest
  version: [license.herzog-cab.com](https://license.herzog-cab.com).
* **Herzog CAB Web** – the complete program in the browser at
  [app.herzog-cab.com](https://app.herzog-cab.com): orders, calculations,
  Designer with all braid types and 3D, machines with catalogue,
  master data, Factory Planner 2D/3D, printing as PDF, roles and import — also on
  tablets and smartphones. Separate subscription module, free 30-day trial.
  See [Web app](../web/index.md).
* **Cloud upload** – the desktop app optionally uploads its workspace folder
  automatically to the web app (*Settings > Licence*).
* **True 3D view in the Designer** – the **3D** switch shows the braid
  as a spatial model built from the carrier paths, for all six
  braid types, with top view, side view and braiding point, material,
  display and orientation. The previous projections are now called
  **Cylinder**, **Square** and **Edge**.
* **Tab „Licence" in the settings** – account, signed-in user,
  edition, modules, lease with expiry date as well as *Renew lease now*,
  *Take offline lease*, *Sign out this computer* and the
  cloud upload.

### Improvements { #verbesserungen_2 }

* **One installer** for the full version, Designer edition and trial version — the
  modules of the account decide.
* **User management in the account model** – users and roles come from
  the customer account (*Refresh from customer account*); the
  assignment to profiles remains local.
* **Licence portal in English**, expiry reminders 30 and 7 days before the
  end of an activation, sales role at Herzog.

### Compatibility { #kompatibilitat_2 }

* **Existing customers with a dongle or CmAct licence change nothing** – the dongle
  remains valid, the local user management including Microsoft Entra ID and
  LDAP remains. The account model only applies if no CodeMeter container
  is present.

## Version 1.4.6 (August 2026)

### New { #neu_3 }

* **Braiding angle from take-up** – a new calculation connects
  machine setting and braid: the braiding angle results from horngear speed and take-up;
  the take-up can be specified as a speed or via
  take-up wheel and speed. Conversely, the page provides take-up,
  horngear speed and wheel speed for a target braiding angle. For
  round and strand braids. See
  [Braiding angle from take-up](../calculations/product/braid-angle-takeup.md).
* **Favorites on the calculation tiles** – the star is now on every
  calculation tile, designed the same everywhere.

### Bug fixes { #fehlerbehebungen_1 }

* **Roles keep their permissions** – when saving a role, exactly those
  permissions were lost that the editor was not currently showing.
* **Locked areas stay hidden** – a favorite pointing to a
  locked area remained visible, and the collapsed toolbar
  showed icons for areas that had long been hidden.
* **Update check per platform** – Windows and macOS again query their
  own update channel.

## Version 1.4.5 (July 2026) { #version-145-juli-2026 }

### New { #neu_4 }

* **Winding fully integrated** – bobbin winding machines are now separate
  master data (series, winding heads, bobbin sizes, speed, winding technology).
  For winding orders there is a separate order type with a link to the
  braiding order, its own color breakdown and carrier table as well as nine
  new calculations in their own group **Winding** (winding time,
  yarn speed, yarn tension, bobbin capacity, bobbin weight,
  material demand, bobbins from supplier spool, residual length from weight, number of
  bobbin winding machines). The Factory Planner now groups machines into braiding and
  bobbin winding machines, and the home page distinguishes both order types.
* **New braid types in the Designer** – square braid (8 to 36 carriers,
  full, half and tandem), spiral braider (12 and 20 carriers),
  packing braider in all sizes with family selection (2-, 3-, 4-track and
  round) as well as soutache braid. Every braid pattern is derived from the
  machine kinematics.
* **Track animation** – the Designer now shows in an animation how the
  carriers move through the machine and the braid is formed layer by layer,
  with speed buttons. Available for all braid types.
* **Winding time and machine distribution** – the winding order calculates the
  winding time, shows the production period from–to and distributes the
  bobbins across several machines; a button distributes evenly by
  winding heads. A calculator determines the target number of bobbins from the
  total length. Winding orders can also be planned without a braiding order, with their own
  color and material breakdown.
* **Sign-in with Microsoft Entra ID** now opens its own compact
  sign-in window instead of a full browser tab.

### Improvements { #verbesserungen_3 }

* **Fineness result switchable** between tex, dtex, den, Nm and Ne
  (feedback #47).
* **Color palette in the Designer** no longer limited to 20 colors and
  scrollable (feedback #45).
* **Braiding machine master data** – the possible values for heads,
  slots and carriers now depend on the machine category
  (e.g. soutache, square).
* **Storage location management** as a separate area in System administration.
* **Preview and views** – the preview states material, covering and
  braid diameter in the dimension line; full, half and the projection are
  switches in the toolbar. Braid type and weave are
  drop-down lists, the design card is compact and scrollable, and nine
  Designer defaults are available under *Settings > Design*.
* **Print editor** – the carrier table can output one column per
  track, the cell style switches between color area and color swatch, and the
  data tables are divided into General, Braiding and Winding.
  Winding orders can be printed.
* **Machine dialogs** – field heights and labels standardised,
  year of construction limited to valid years, double-click opens editing directly. The
  Settings dialog is scrollable and adapts to the screen height.
* **Winding order** – calculations can be started directly from the input field,
  as in the braiding order.

## Version 1.4.4 (30.06.2026)

### New { #neu_5 }

* **Additional sign-in methods** – in addition to local user management,
  you can now sign in via **Microsoft Entra ID** (Azure AD) and via
  **LDAP / Active Directory**. Users and groups can be imported from
  the directory; roles are assigned automatically based on
  group membership.

### Improvements { #verbesserungen_4 }

* **Calculation fields** – fields with the placeholder „–" can now be
  edited directly with a click; decimal places are taken over correctly.

### Bug fixes { #fehlerbehebungen_2 }

* **Window focus** – the main window (and the 3D shop floor view dialog)
  now reliably come to the foreground after starting or opening.

## Version 1.4.3 (24.06.2026)

### Bug fixes { #fehlerbehebungen_3 }

* **Alignment bar in the Factory Planner** – the toolbar (Align ·
  Distribute · Arrange) above the drawing area now keeps a fixed,
  slim height instead of filling the entire upper area.
* **Translations in the floor plan** – labels in the
  Factory Planner floor plan (production area, transport route, storage area,
  maintenance, office, quality control, door, gate, window, stairs,
  banner/logo, door styles) were hard-coded in German and are now translated into
  all six languages.

## Version 1.4.2 (23.06.2026)

### Bug fixes { #fehlerbehebungen_4 }

* **Colors in the carrier table** *(Issue #44)* – the displayed color
  (ID/name/hex/Pantone) per carrier could stop matching the actual color after rotating the
  design colors. This is now
  linked correctly; designs that have already been saved are corrected automatically when
  reopened.
* **Color palette tooltip** – the dark, hard-to-read
  tooltip background on the color swatches and in the color picker has been fixed.

## Version 1.4.1 (23.06.2026)

### New { #neu_6 }

* **Factory Planner (production layout)** – draw hall floor plans
  (outer/inner walls, areas, doors, gates, windows, stairs), place machines from
  the catalogue (align, distribute evenly, arrange,
  line up, rotate, duplicate), with scale, grid/angle snap
  and measuring tool.
* **3D shop floor view** – the finished floor plan in 3D, including machines,
  wall textures, banners/logos and live machine status.
* **Floor plans as separate master data** – a floor plan can contain several
  layouts/scenarios (current state and planning variants) and
  is created, renamed, duplicated and managed independently.
* **Media library** – central management of all images (braiding machines,
  wall textures, banners & logos, hall floor plans, company logo) with folders,
  search, upload and replace.

### Improvements { #verbesserungen_5 }

* **Machine Fleet** – new card and list view with status display.
* **Switchable appearance** – new interface design, either
  Flat or Neumorphic, switchable live in the settings.
* Improved role and user management, including a separate permission for
  the Factory Planner.
* Numerous other detailed improvements to the interface.

## Version 1.3.4 (April 2026)

* Print templates are stored per file under `Printouts/templates/` (migration runs automatically).
* Profile pictures are stored machine-wide under `ProgramData`.
* Performance improvements in the Designer.

## Older versions { #altere-versionen }

Complete history: see the file `CHANGELOG.md` in the program directory.
