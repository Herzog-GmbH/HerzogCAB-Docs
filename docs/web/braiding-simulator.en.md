# Braiding Simulator (web app)

!!! abstract "Reference — The Braiding Simulator in the browser: opening it, start page, operation on the PC and on the smartphone, and all differences from the desktop app"

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

The Braiding Simulator of the web app works with the same machine models,
setups and programs as the desktop app: what you save in the browser opens
in the program and vice versa. Structure and operation are the same, with
the task bar **Set up**, **Program**, **Check** and **Output**. The fields
and buttons are described in the reference of the desktop app
([Braiding Simulator](../braiding-simulator/index.md)); this page only
lists what is different in the browser.

## Opening it { #aufrufen }

The **Braiding Simulator** entry is in the sidebar after the Parameter
Explorer (address `/flechtsimulator`). On a smartphone you open it via
**Menu** (☰) or **More**. You see it if your account has the full version
in a subscription and at least one valid model licence, and your role
includes the *View Braiding Simulator* right, see
[Licence and rights](../braiding-simulator/licence.md). If the account's
last valid model licence expires, the entry disappears.

## Start page { #startseite }

!!! warning "📷 Screenshot missing"
    **Subject:** Start page of the Braiding Simulator in the web app: the machines on the left, the selected machine on the right with preview, Configurations from Herzog, My setups, My programs and the buttons New setup, New program, Open.
    **How to create:** Web app locally (127.0.0.1:5173), page `/flechtsimulator` with a customer account with an assigned model licence; not yet in the script `_tools/web_screenshots.py` (add the name `flechtsimulator`).
    **Target file:** `assets/screenshots/web/flechtsimulator.png`
    <!-- web-bild ../assets/screenshots/web/flechtsimulator.png -->

The start page corresponds to the [start page of the desktop app](../braiding-simulator/index.md#startseite).
In the browser, the following is added:

* Below the title is the number of machines; from seven machines onward
  there is a search field (name, catalogue type, your own machines).
* From a width of 1024 px, list and details are side by side, below that
  one above the other. On a smartphone the page jumps to the details after
  you make a selection.
* Next to **New setup** and **New program** there is the **Open** button
  for the selected machine.
* The list reloads every five minutes and when you return to the window;
  a new assignment in the licence portal thus arrives without reloading.
* If no model is assigned to you, it reads *No machine model is assigned
  to you. Your administrator assigns model licences in the licence
  portal.* Administrators go directly to the
  [Assign machine models](../portal/models.md) page with **Assign in the
  licence portal**.
* Each browser remembers the *New version from Herzog* note by itself.

Your own setups and programs belong to the company: all users with
*View Braiding Simulator* can read them; they can be saved by anyone who
has been assigned a valid licence for this model and has the
*Edit Braiding Simulator* right.

## The simulator in the browser { #der-simulator-im-browser }

!!! warning "📷 Screenshot missing"
    **Subject:** Braiding Simulator of the web app on a wide screen: header with setup and program, machine with the 3D preview next to it, selection card and task bar on the right, playback bar and timeline at the bottom.
    **How to create:** Web app locally (127.0.0.1:5173), page `/flechtsimulator/<id>` with a program, click a switch; not yet in the script (add the name `flechtsimulator-editor`).
    **Target file:** `assets/screenshots/web/flechtsimulator-editor.png`
    <!-- web-bild ../assets/screenshots/web/flechtsimulator-editor.png -->

The screen is structured as in the desktop app
([The simulator screen](../braiding-simulator/editor.md)). The 3D preview
is next to the machine as soon as there is enough space, otherwise below
the timeline.

### Only in the web app { #nur-in-der-web-app }

| Function | Description |
|---|---|
| **Commands (n)** | Collapsible list of all commands of the program in the **Program** task. For each command you change the **Step** (the command moves there), jump with **Jump to step** or remove it with **Remove command**. Commands that the machine cannot execute are shown in orange. |
| **Length** | The program length is in the **Program** task (empty = as long as the commands). |
| **Rename…**, **Duplicate…** | Additionally in the **⋯** menu next to **Program**. A program from Herzog becomes your own copy when you rename it. |
| **Thread path (unrolled)** | In the **Output** task: **Calculate thread path** shows the path of each carrier around the braid, unrolled (circumference horizontally, time downward, repeat dashed). |
| **8 steps/s** | Additional playback speed. |
| **Full screen** | Button in the 3D preview. |
| The check runs by itself | The collision check recalculates after every change; there is no **Check current arrangement** button. |
| **Notes** | In **Check**, if Herzog has stored notes on the model. |
| Colors | **Color for new carriers** with selection of the **Palette**, **Color all carriers** and **Open color database**. |

### Not yet in the web app { #noch-nicht-in-der-web-app }

| Function of the desktop app | In the browser |
|---|---|
| Print the [switching plan](../braiding-simulator/output.md), save it as PDF and CSV | **Output** only shows: *The switching plan for the control (print, PDF, CSV) is so far only available in Herzog CAB on the PC.* |
| **Covering** | Cannot be set; it is shown in the info line, the take-up and Machine 3D. |
| **Material diameter** per setup | Applies per browser to all machines and is not saved with the setup. A material diameter from a desktop app program takes precedence in the take-up. |
| Threading [tube threads](../braiding-simulator/populate.md#rohrfaden) in with a click | Tube threads only come from a saved setup. |
| [Insert operating mode](../braiding-simulator/program.md#betriebsart-einfugen) | Missing. |
| **Running direction** view colors empty positions | Only rotation arrows and direction arrows. |
| Timeline: right-click menu (insert/delete steps, move/copy a section), selecting rows, moving a command by dragging | Missing. You move commands via the command list. Dragging in a row applies the state over the range. |
| Check with color pattern, return of the carriers and interlacing per section | Only collision, repeat and number of carriers, plus *All commands can be executed on the machine.* or the findings. |
| Placing carriers in the middle of the run | Only while stopped: *Clicking a position adds or removes a carrier (only while stopped).* |

### Other differences { #weitere-unterschiede }

* **Mouse:** dragging with the **left** or middle button pans the
  machine. At the top right there are the buttons **Zoom in**, **Zoom out**
  and **Fit**.
* **Timeline:** shift levers have a row of their own, the gears are in one
  row **All gears**, plus one row each per horngear group, switch-out gear,
  turning unit and pitch. After a change, playback stays at the current
  step.
* **Recording:** during recording the program plays without repetition;
  when you stop, the program length grows up to the step reached.
* **Stopping and reversing** horngear groups and switch-out gears has no
  *for this run only* variant without recording, as there is for
  switches.
* **Undo** applies to program changes, not to placing or coloring
  individual carriers.
* **Without *Edit Braiding Simulator***, recording, **Adopt start state**,
  **Change speed…**, **Change take-up…** and **Save as new setup…** are
  missing; placing and coloring carriers works for trying things out.
* Each browser remembers the view switches, the task, the speed and the
  settings of the 3D preview.

## On a tablet and smartphone { #am-tablet-und-smartphone }

!!! warning "📷 Screenshot missing"
    **Subject:** Braiding Simulator on a smartphone (390 px wide): machine at the top, playback and timeline below it, the selection card of a switch as a sheet at the bottom edge.
    **How to create:** Web app locally (127.0.0.1:5173), page `/flechtsimulator/<id>` at a width of 390 px, tap a switch; not yet in the script (add the name `flechtsimulator-handy`).
    **Target file:** `assets/screenshots/web/flechtsimulator-handy.png`
    <!-- web-bild ../assets/screenshots/web/flechtsimulator-handy.png -->

Below a width of 1024 px, everything is arranged one above the other:
header, machine, playback bar, timeline, tasks, 3D preview.

| Gesture | Effect |
|---|---|
| Tap | Like a click, depending on the task. |
| **Long press** | Like a right-click: in **Set up** removes a carrier, otherwise toggles a switch. |
| One finger vertically | Scrolls the page; horizontally it pans the machine. |
| Two fingers | Zoom. |

* The **selection card** appears as a sheet at the bottom edge; the
  machine remains visible above it.
* You select several carriers with **Select all carriers**; Ctrl+click
  and frame selection only exist with mouse and keyboard.
* In the 3D preview, the view is **locked** at first so that one finger
  scrolls the page. Tapping the lock allows rotating; in the **Machine**
  view the lock only exists on touch devices.
* The **⛔ errors** and **⚠ notes** chips scroll to the **Check** task.

## Saving, edit lock, withdrawal { #speichern-bearbeitungssperre-entzug }

* **Save** (++ctrl+s++) writes your setups and programs to the server
  (*Machine saved.*). If you leave the page with unsaved changes, the web
  app asks *Save changes?* with **Save**, **Don't save** and **Cancel**;
  when you close the tab, the browser warns you.
* If a colleague has the same machine open, *Being edited – read only*
  appears with **Try again**; when it becomes free, *Available now –
  reload*. See [Multiple users](../basics/multi-user.md).
* If the model is withdrawn from you or the licence expires, playback
  stops, see [Licence and rights](../braiding-simulator/licence.md#wenn-eine-lizenz-wegfallt).

## Related pages { #verwandte-seiten }

* [Braiding Simulator](../braiding-simulator/index.md) — reference with all
  fields.
* [Create a braiding program](../tasks/create-braiding-program.md)
* [Assign machine models](../portal/models.md)
* [Settings](settings.md#flechtwinkel) — braiding angle reference, also
  applies in the simulator.
