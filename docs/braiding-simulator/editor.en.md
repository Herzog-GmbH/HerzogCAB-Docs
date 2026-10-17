# The simulator screen

!!! abstract "Reference — The working screen of the Braiding Simulator: header bar with setup and program, machine view, task bar with selection card, playback, keys and mouse"

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

When you open a machine on the [start page](index.md#startseite), you see
this screen. Here you set up the machine, write and check programs and
output the switching plan. This page describes what is the same in all
tasks; the tasks themselves have their own pages.

## The screen at a glance { #der-bildschirm-im-uberblick }

!!! warning "📷 Screenshot missing"
    **Subject:** Simulator screen of a round braiding machine: header bar with setup and program, machine view with carriers, on the right the task bar with the opened selection card of a switch, 3D preview, at the bottom playback bar and timeline; numbers 1–6 at the areas.
    **How to create:** Customer build with model licence, open a machine with a program, click a switch, play a few steps; navigation collapsed.
    **Target file:** `assets/screenshots/braiding-simulator/bildschirm.png`

1. **Header bar** — back to the start page, name of the machine, setup,
   program, messages, view, quick help, undo, save.
2. **Machine view** — the machine from above with gears, switches,
   tubes and carriers. This is where you click to set up, switch and
   select.
3. **3D preview** — braid, schematic or machine in 3D, see
   [3D preview and take-up](views.md).
4. **Selection card** — at the top of the right-hand bar, as long as
   something is selected.
5. **Task bar** — the tabs **Set up**, **Program**, **Check** and
   **Output**.
6. **Playback bar and timeline** — at the bottom, across the full width.

## Header bar { #kopfzeile }

| Element | Effect |
|---|---|
| **← Braiding Simulator** | Back to the [start page](index.md#startseite). If there are unsaved changes, the program asks first. |
| Name of the machine | With an asterisk if there are unsaved changes. The tooltip states the number of gears, switches and carrier positions. |
| **Setup** | List of the setups for this machine: your own, those supplied by Herzog (with a symbol, *Supplied by Herzog with the machine.*) and the configurations (*Configuration: Full* etc.). Choosing one places the setup on the machine immediately; if the current arrangement has not been saved, the program asks first (*Change setup*, **Discard and load**). Switches and gears stay as they are. |
| **⋯** next to Setup | **Save as new setup…** and **Delete setup…** (own setups only), see [Set up](populate.md#besetzung-speichern). |
| **Program** | List of the time programs for this machine, programs from Herzog with a symbol. Choosing one loads it immediately; if the program brings a setup, the setup comes along, provided your current arrangement has been saved. The next time you open the machine, program and setup are selected again. |
| **⋯** next to Program | **New program…** (enter a name; the program takes the current position of switches and gears as its start and the selected setup) and **Delete program…** (it is only deleted once you **Save**). Programs from Herzog cannot be deleted. |
| **⛔ n errors**, **⚠ n notes** | Appear as soon as there are messages (red or orange). The tooltip lists them; a click opens the [Check](check.md) task. |
| **View** | What the machine view shows, see [below](#ansicht). |
| **?** | Quick help with mouse and keys, see [Keys and mouse](#tasten-und-maus). |
| Undo, Redo | Multi-level (++ctrl+z++, ++ctrl+y++). The run is then back at the start. Locked during recording. |
| **Save** | Saves your own setups and programs (++ctrl+s++). Active as soon as there are changes and you have the *Edit Braiding Simulator* right. See [Save](#speichern). |

### View { #ansicht }

| Toggle | Shows | Default |
|---|---|---|
| **Switches with numbers** | Switches and fixed components with their W number, as in the timeline. Round symbols can be switched, square ones are fixed components. | on |
| **Running direction** | Colors each empty position by the direction in which a carrier would run around the machine from there: the two thread systems of the braid. Plus rotation arrows on the hubs, direction arrows on the carriers and a legend at the bottom left (*clockwise*, *counterclockwise*, *oscillates*, *stays on the horngear*, *Dead end*). If you move the mouse over an empty position, the view shows its track. | on |
| **Carrier numbers** | Number of each carrier and the labels of the tubes. | off |
| **Empty positions** | Empty carrier positions. | on |
| **Slots** | The slots of the horngears. | on |
| **3D preview** | Shows or hides the [3D preview](views.md). | on |
| **Fit machine** | Shows the whole machine (also ++ctrl+0++ or a double-click on an empty spot). | — |

The program remembers the toggles.

## Machine view { #maschinenansicht }

The machine appears from above, as it lies in the design. Besides the
carriers and gears you see:

* **Switches** with their number (*W12*); if a switch is attached to a
  shift lever, the lever follows the number (*W12·H1*). Round symbols are
  switchable switches, square ones fixed components.
* **G1**, **G2** … on the gears of a horngear group.
* a **run symbol** below the hub of gears with their own drive
  (▶ running, ⏸ stopped), see [Program](program.md#rad).
* the **gear number** in the hub when you move the mouse over it or the
  gear is selected.
* during recording, a red **Recording** band at the top left with the
  position and the number of recorded commands.
* after a collision, the marked spot.

What a click does depends on the open task, see
[Keys and mouse](#tasten-und-maus).

## Task bar and selection card { #aufgaben-leiste-und-auswahlkarte }

The right-hand bar has a fixed width. At the bottom are the four tasks:

| Tab | Content |
|---|---|
| [**Set up**](populate.md) | Place and color carriers; yarn and tube threads. A click on an empty position places a carrier. |
| [**Program**](program.md) | Switches and gears during the run, operating modes, speed and take-up. A click on a switch switches it. |
| [**Check**](check.md) | Errors and notes, collision check over the whole run. A red or orange dot on the tab indicates errors or notes. |
| [**Output**](output.md) | Switching plan for the control: print, as PDF or CSV. |

If you click a carrier position, a switch, a gear or a tube in the
machine, the **selection card** with its properties appears above the
tabs, for example *Carrier 7 selected* or *Switch W12 selected*. **✕** or
++esc++ closes it, as does a click on an empty area.

| Card | Described under |
|---|---|
| Carrier, several carriers, tube | [Set up](populate.md#auswahlkarte-kloppel) |
| Switch, shift lever | [Program](program.md#weiche) |
| Gear, horngear group, pitch | [Program](program.md#rad) |

## Playback bar { #wiedergabe }

The bar above the timeline controls the run of the simulation:

| Element | Effect |
|---|---|
| **Start** / **Pause** | Starts and stops (++space++). Pause stops exactly at the current spot, even in the middle of a step. After a collision, playback no longer starts until you go back. |
| Step back | One step back; in the middle of a step, first to the start of the step (++arrow-left++). Also works after a collision. |
| Single step | One step forward (++arrow-right++). |
| Reset | Back to the start. |
| **Record** | Switches recording on and off, see [Program](program.md#aufnahme). |
| Playback speed | **0.5**, **1** (default), **2** or **4 steps/s**; plus **Machine speed**, **Machine speed 1:4** and **Machine speed 1:10**: as fast as the real machine at the program's [horngear speed](views.md#drehzahl), or as slow motion. Without a speed in the program, machine speed runs at 1 step/s. |
| **Go to step** | Enter a step and press ++enter++: the run is calculated from the start up to there. While recording, the program grows with it. |
| Step display | *Step n* without a program, *Program step n/m* with a program, from the second pass on with *· cycle n*. |
| **Timeline** | Hides and shows the [timeline](program.md#zeitachse) (only with a program). When it is hidden, the machine gets the space. |

At the very bottom, a status line shows on the left the current state
(for example *Program step 3/48 · 32 carriers · program (length 48,
repeated)*) and the last message, and on the right the zoom of the
machine view.

## Save { #speichern }

**Save** writes changed arrangements into the selected setup and saves
the programs:

* If the selected setup is a configuration or a setup from Herzog, a copy
  of your own *&lt;Name&gt; – own* is created; the original remains
  unchanged.
* If no setup is selected (for example after **Remove all carriers**),
  the program asks for a name.
* If you change a program from Herzog, the simulator immediately creates a
  copy of your own: *Own copy "… – own" created — the program from Herzog
  remains unchanged.*

If you leave the machine with unsaved changes (going back, via the
navigation or when closing the program), the program asks *The machine
"…" has unsaved changes. Save before leaving?* with **Save**, **Discard**
and **Cancel**. Without the *Edit Braiding Simulator* right there is no
prompt: changes count as tried out and are discarded. If another user is
currently editing the programs of this machine, you can only discard or
stay, see [Multiple users](../basics/multi-user.md).

Switching the program in the header bar does not prompt: your changes
are kept until you save or discard them.

## Keys and mouse { #tasten-und-maus }

### Machine view { #maschinenansicht_1 }

| Action | Effect |
|---|---|
| Click | **Set up:** place a carrier (empty position) or select it. **Program:** toggle a switch. **Check**, **Output:** select. During recording, a click on a switch always toggles it, whichever task is open. |
| Right-click | **Set up:** remove a carrier. Otherwise and during recording: toggle a switch. |
| ++ctrl++ + click, ++ctrl++ + drag | Select several carriers or drag a frame around carriers. In **Program**: collect switches into a switch group. |
| ++ctrl+a++ | Select all carriers. |
| ++esc++ | Clear the selection. |
| Mouse wheel | Zoom around the mouse pointer. |
| Drag with the right or middle mouse button | Pan. |
| Double-click on empty space, ++ctrl+0++ | Fit machine. |

If a carrier position and a switch lie on top of each other, the click
selects the position; you then toggle the switch with a right-click.

### Keyboard { #tastatur }

| Key | Effect |
|---|---|
| ++space++ | Start and pause (not in input fields). |
| ++arrow-left++ / ++arrow-right++ | Step back / forward. Works if you have clicked into the machine view first. |
| ++ctrl+a++ | Select all carriers (the machine view has the focus). |
| ++esc++ | Clear the selection. |
| ++ctrl+z++ / ++ctrl+y++ | Undo / Redo. |
| ++ctrl+s++ | Save. |
| ++ctrl+0++ | Fit machine. |

The quick help **?** summarizes mouse and keys for the machine, playback,
timeline and 3D preview.

## In the web app { #in-der-web-app }

Layout and operation are the same. Differences, with details under
[Braiding Simulator (web app)](../web/braiding-simulator.md):

* Dragging with the **left** or middle mouse button pans the machine;
  **Zoom in**, **Zoom out** and **Fit** are at the top right.
* The **⋯** menu next to **Program** additionally contains **Rename…** and
  **Duplicate…**.
* The playback speed additionally offers **8 steps/s**.
* On a smartphone everything is stacked, the selection card slides up from
  the bottom as a sheet, and a **Long press** replaces the right-click.
* The prompt when leaving is called *Save changes?* and offers **Save**,
  **Don't save** and **Cancel**.

## Related pages { #verwandte-seiten }

* [Braiding Simulator](index.md) — overview and start page.
* [Set up](populate.md), [Program](program.md), [Check](check.md),
  [Output](output.md)
* [3D preview and take-up](views.md)
