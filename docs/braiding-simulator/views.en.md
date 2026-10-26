# 3D preview and take-up

!!! abstract "Reference — The 3D preview of the Braiding Simulator with braid, schematic and machine, and the dialogs for take-up and speed"

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

To the right of the machine view, the **3D preview** shows what becomes of
the setup and the program: the **Braid** being produced, the
**Schematic** of the interlacing or the loaded **Machine** with yarns,
braiding point and take-up disc. The preview runs along with the
simulation. With **Take-up** and **Speed** you define the braiding angle,
lay length and speed at which the program braids; these values are stored
in the time program and go into the
[switching plan](output.md).

## The screen at a glance { #der-bildschirm-im-uberblick }

!!! warning "📷 Screenshot missing"
    **Subject:** Braiding Simulator with the loaded machine on the left and the 3D preview on the right in “Braid” mode, side view, the info lines below it; the “3D preview” gear icon window is open.
    **How to create:** Customer build with a model licence, Braiding Simulator > open a machine with a saved setup, play a few steps, click the gear icon at the top of the 3D preview.
    **Target file:** `assets/screenshots/braiding-simulator/vorschau-geflecht.png`

At the top of the 3D preview, from left to right, are:

1. the switch **Braid** | **Schematic** | **Machine**,
2. the **gear icon** with the settings of the 3D preview,
3. **✕** to hide it.

In the image itself, the fixed views are at the top, and one or two info
lines are below the image. You distribute the space between machine and
3D preview with the splitter between them (*Drag: share the space between
machine and 3D preview*).

How to operate the preview with the mouse:

* At the top of the image there are three [fixed views](#feste-ansichten-und-schloss);
  the **lock** next to them blocks rotation. The
  [Machine](#ansicht-maschine) view has no lock.
* With the lock open, the left mouse button rotates the braid and the
  right one pans it. A double-click restores the selected view.
* The mouse wheel always zooms, even when the lock is closed.
* The preview shows a scale in millimeters as soon as a material diameter
  is entered under [Set up > Yarn](populate.md#garn) or a
  [core is threaded in](populate.md#rohr), see
  [Info lines below the image](#infozeilen-unter-dem-bild).

## Controls in detail { #bedienelemente-im-detail }

### Braid, Schematic, Machine { #geflecht-schema-maschine }

| Mode | Shows |
|---|---|
| **Braid** | *The braid as it is produced, in 3D.* The carrier colors, the ply count and the [material diameter](populate.md#garn) determine the image. A flat braid appears as a flat ribbon, even if the carriers have a ply count above 1. This is the default. |
| **Schematic** | *Interlacing only: thread sequence and over- and under-crossings, without gear positions and gear sizes.* Helpful for checking the binding when the braid in the image is very dense or flat. |
| **Machine** | *The loaded machine in 3D: carriers, yarns to the braiding point, the braid up to the take-up disc.* See ["Machine" view](#ansicht-maschine). |

The program remembers the choice. **✕** hides the preview (*bring it back
via “View”*); you switch it on again in the **View** menu of the header
with **3D preview**.

### Fixed views and lock { #feste-ansichten-und-schloss }

In **Braid** and **Schematic** mode, there are three fixed views at the
top of the image:

| View | Shows |
|---|---|
| **Top view** | Looking at the cross-section, oriented like the machine in the drawing. |
| **Side view** | The whole braid from the side, that is the braid pattern. This is the default. |
| **Braiding point** | Close-up of the spot where the braid is being formed. The camera follows the simulation; best with **Build braid during simulation**. |

To the right of them is the **lock**. When locked (default), the mouse
does not rotate the braid; the mouse wheel still zooms. If you drag while
it is locked, *View locked — open the lock to rotate* appears briefly.
When open:

| Action | Operation |
|---|---|
| Rotate | Drag with the left mouse button |
| Pan | Drag with the right mouse button |
| Zoom | Mouse wheel |
| Restore the selected view | Double-click |

### Displays in the empty image { #anzeigen-im-leeren-bild }

| Display | Meaning |
|---|---|
| *No machine loaded* | No machine has been opened yet. |
| *No carriers placed — choose a setup, then the braid appears here.* | The machine is empty. Choose a **Setup** at the top or [set up](populate.md) the machine. |
| *Press Start — the braid builds up with the simulation.* | **Build braid during simulation** is on; the braid grows from **Start**. |
| *⛔ Collision at step n — the braid ends here* | Two carriers meet. The braid is only drawn up to this step. How to find collisions is described under [Check](check.md). |
| *⛔ Dead end at step n — the braid ends here* | A carrier cannot move on, for example at a wrongly set switch. |

### Settings of the 3D preview (gear icon) { #einstellungen-der-3d-vorschau-zahnrad }

The gear icon opens the **3D preview** window:

| Setting | Effect |
|---|---|
| **Braiding angle** | Slider for the inclination of the yarns in the image (default 45°), shown in the [selected reference](#flechtwinkel-bezug). If the program has a [take-up](#abzug), the slider is locked: *The braiding angle comes from the take-up in the time program ("Take-up" row of the timeline).* |
| **Material** | **Smooth filament**, **Twisted yarn** (default), **Wire**, **Rope** or **Simple display**. Only determines fiber structure, roughness and gloss. **Rope** draws each thread as a braided rope with light and dark tracers, for braids made of ropes; set the [material diameter](populate.md#garn) to the rope diameter, for example 10 mm. The simple display is faster and helps with weak graphics. The carrier colors are kept in all modes. |
| **Cross-section like the gear layout** | Shows the cross-section exactly like the gear layout of the machine, without conversion: the view for troubleshooting. Off (default) shows the braid as it leaves the machine; the preview then detects flat braid operation and several braiding circles by itself. The switch is not saved. |
| **Cut parked threads flush** | Only visible if the program parks carriers on a switch-out gear. Off (default): the threads of the parked carriers stand outside the braid and run back in when the carrier returns, as during braiding. On: this length is cut off flush, as on the finished braid. |
| **Build braid during simulation** | On: the braid grows from **Start** with the carrier movement. Off: the complete braid is visible immediately. |
| **3D orientation** | **Top → bottom** or **Bottom → top**. Only rotates the display; simulation, take-up and braiding direction remain unchanged. |
| **Axial threads** | Only for machines with tubes: thickness of the axial threads in the image, 20 to 250 %. |

You do not set the material diameter and the covering here, but under
[Set up > Yarn](populate.md#garn): they belong to the setup.

### Info lines below the image { #infozeilen-unter-dem-bild }

The first line begins with **Shown:** and says how the preview builds up
the braid, for example:

* *Round braid*, *Flat braid, pulled flat* or *2 round braids side by
  side*,
* *2 braiding circles stacked* or *2 braiding circles as far apart as in
  the machine*,
* *thinner while carriers are parked (12 instead of 16 carriers)*,
* *nothing converted* with **Cross-section like the gear layout**,
* *effective braiding angle …° instead of …° (the braid gets longer so the
  ribbons have room)* or *no more yarn fits, the picture stays as it is*,
  if the material no longer fits side by side at the set angle.

In **Schematic** mode it reads *Shown: interlacing schematic, without gear
positions and gear sizes.*

The second line gives the size as soon as there is a scale (a
[material diameter](populate.md#garn) or a threaded core):
*Braid Ø … mm* or *Flat braid … mm wide*, if applicable *over core Ø
… mm*, *· covering … %* and the width of the ribbon of one carrier. The
lay length is not shown here, but in the
[summary of the take-up](program.md#drehzahl-und-abzug) and at the
take-up disc in the **Machine** view.

## "Machine" view { #ansicht-maschine }

!!! warning "📷 Screenshot missing"
    **Subject:** “Machine” view of the 3D preview: loaded machine with bobbins in yarn colors, yarns to the braiding point, braid up to the take-up disc; labels take-up, lay length, rpm, braiding angle.
    **How to create:** As above, switch to “Machine”, fixed view “Overview”, play a program with take-up and speed.
    **Target file:** `assets/screenshots/braiding-simulator/vorschau-maschine.png`

The view shows the loaded machine schematically, the way it produces the
braid: carriers with bobbins in the yarn colors on the track plate, the
yarns to the braiding point, the braid up to the take-up disc and a little
beyond. Gears and disc run with the simulation. The frame is a typical
design (table, portal, horizontal, housing of the variation braider), not
an image of your machine. The view does not show take-up units.

| Fixed view | Shows |
|---|---|
| **Overview** | The whole machine: carriers, braiding point, braid and take-up. |
| **Braiding point** | Close-up of the braiding point: the yarns converge here and the braid is formed. |
| **Take-up** | The take-up disc with the braid. |

Dragging with the left mouse button rotates, with the right one pans, the
mouse wheel zooms towards the mouse pointer, a double-click restores the
selected view. There is no lock here.

In the image, the take-up in m/min and the lay length are shown at the
disc, the speed (or *Speed missing*) at the drive, the braiding angle at
the braiding point, and the diameter or width and the covering at the
braid.

* **Clicking the take-up disc** opens the [take-up](#abzug) for the range
  at the playhead.
* **Clicking the drive** opens the [speed](#drehzahl).

Without a program, a click reports *Take-up and speed are part of the time
program. Without a program, the view shows the braiding angle of the
preview.*

## Take-up { #abzug }

The take-up determines how fast the braid is drawn off the machine, and
thus braiding angle, lay length and PPI. It belongs to the time program
and applies from one step until the next take-up change. At that point it
switches over; there is no ramp.

How to open the dialog:

* in the timeline, a click in the **Take-up** row (from this step) or
  dragging over a range (only for this range), see
  [Program](program.md#abzug-und-drehzahl-in-der-zeitachse),
* in the **Program** task with **Change take-up…** (from the step at the
  playhead),
* in the **Machine** view with a click on the take-up disc.

!!! warning "📷 Screenshot missing"
    **Subject:** “Take-up from step 1” dialog with setpoint Braiding angle, value 30°, horngear speed, material diameter and the results table.
    **How to create:** Choose a program, click in the “Take-up” row of the timeline at step 1.
    **Target file:** `assets/screenshots/braiding-simulator/abzug-dialog.png`

The title reads *Take-up from step n* or, for a dragged range, *Take-up
for steps n to m*. Below it: *Specify one quantity; the others follow
from it.*

| Area | Field | Meaning |
|---|---|---|
| **Setpoint** | **Quantity** | Which quantity you specify: **Take-up [m/min]**, **Lay length [mm]**, **Braiding angle [°]** or **PPI [1/inch]**. If you change the quantity, the dialog converts the same take-up into the new quantity. |
| | **Value** | The value of the selected quantity. The dialog shows the braiding angle in the [selected reference](#flechtwinkel-bezug). |
| | **Horngear speed** | Display only: the speed at this step or *not set*. You set it in the **Speed** row; if it changes, the take-up follows. |
| **For the whole program** | **Material diameter** | Diameter of **one** yarn in mm. It gives the preview its scale. The value belongs to the setup, see [Set up > Yarn](populate.md#garn). |
| **Results in** | Table | Take-up (m/min), **Take-up per horngear revolution** (mm), lay length (mm), braiding angle, PPI, **Braid diameter** (for a flat braid **Braid width**) and **Covering**. The specified quantity is shown in bold. Diameter and covering are always results. |

Orange notes in the dialog:

| Note | What to do |
|---|---|
| *Material diameter missing: take-up, lay length and PPI cannot be converted into the braiding angle.* | Enter the material diameter. |
| *Horngear speed missing: the take-up in m/min is unknown.* | Set a speed in the **Speed** row. |
| *The carrier cycle cannot be determined in this range: lay length and PPI are missing.* | The carriers do not complete a full cycle in this range (for example during a changeover); only take-up and angle can be determined. |
| *At this angle the material does not fit on the core: the covering would exceed 100 %.* | Change the angle or choose a thinner material. |
| *The lay length is shorter than the material needs side by side: it cannot be braided this tight.* | Specify a longer lay length or a smaller braiding angle. |

**Apply** sets the take-up change, **Cancel** discards it.
**Remove take-up change** appears if there is already a change at this
step. If the program had no take-up yet, the dialog starts with the
quantity *Braiding angle* and the angle of the preview. After a dragged
range, the take-up before it applies again.

## Speed { #drehzahl }

The **horngear speed** in rpm gives the program its timing: the duration,
the take-up in m/min and the **Machine speed** of the playback follow from
it. You open the dialog via the **Speed** row of the timeline, with
**Change speed…** in the **Program** task or with a click on the drive in
the **Machine** view.

The title reads *Start speed of the program* (step 1), *Speed from step n*
or *Speed for steps n to m*. The note explains: *All horngears run
synchronously at this speed. The take-up follows: lay length and braiding
angle stay the same, only the take-up in m/min and the time change.*

| Field | Meaning |
|---|---|
| **Speed** | 0 to 2000 rpm; 0 means *not set*. |
| **Remove speed change** | Removes the change at this step (not at step 1). |

## Braiding angle reference { #flechtwinkel-bezug }

The simulator shows the braiding angle in the reference you selected under
*Settings > General > Braiding angle*:
**To the cross direction (Herzog)** or **To the braid axis (technical
literature)**, see [braiding angle setting](../admin/settings/appearance.md#flechtwinkel).
This applies to the slider in the gear icon window (with the braid axis
reference it runs the other way round), the take-up dialog, the timeline,
the summary, the info lines and the labels in the **Machine** view.

The labels do not name the reference. If you point the mouse at an angle,
the tooltip gives both values, for example *30.0° to the cross direction
(Herzog) = 60.0° to the braid axis (technical literature)*. The
[switching plan](output.md) names the reference in the row **Braiding
angle measured to**. The values are always stored the same way; changing
the reference does not change any program.

## Start values in the settings { #startwerte-in-den-einstellungen }

In the program, *Settings* has the **Braiding Simulator** tab with
personal start values:

| Area | Setting | Effect |
|---|---|---|
| **Playback** | **Build braid during simulation** | Start value for the switch of the same name in the gear icon window. |
| | **Default speed** | Speed at which playback starts (0.5 to 4 steps/s). |
| **3D preview** | **3D orientation** | Start value for **Top → bottom** or **Bottom → top**. |

## In the web app { #in-der-web-app }

The 3D preview has the same structure. Differences:

* A **Full screen** button enlarges the preview.
* In the **Machine** view, the lock only exists on touch devices.
* If the braiding angle slider is locked, it shows the angle of the
  longest take-up range.
* The **Braiding Simulator** tab in the settings is missing; you set the
  orientation and the build-up in the gear icon window, and the browser
  remembers them.
* On a smartphone the preview is locked at first so that one finger
  scrolls the page.

Details: [Braiding Simulator in the web app](../web/braiding-simulator.md).

## Related pages { #verwandte-seiten }

* [Set up](populate.md) — material diameter and covering.
* [Program](program.md) — **Take-up** and **Speed** rows of the
  timeline.
* [Output](output.md) — take-up ranges in the switching plan.
* [Braiding angle](../calculations/product/braid-angle.md) and
  [Braiding angle from take-up](../calculations/product/braid-angle-takeup.md)
  — the same quantities as a calculation.
