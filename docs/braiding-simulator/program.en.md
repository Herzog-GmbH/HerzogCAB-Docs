# Program

!!! abstract "Reference — The “Program” task: switching switches and gears, start position, recording, timeline, pitch in this run, horngear groups, speed and take-up"

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

A **time program** describes how the machine runs: the **start position**
of all switches and gears and the **commands** that switch at certain
steps during the run. This is how changeovers such as round ⇄ flat braid,
twisting or spiral come about. You write a program in two ways:

* **Record:** switch on recording, let the run go, pause, click a switch,
  continue. Each click becomes a command at the current step.
* **Set in the timeline:** in the row of a switch or gear, click the step
  at which the change should happen.

Each program belongs to exactly one setup. You create new programs at the
top in the header bar on the selected setup (**⋯** next to **Program** >
**New program…**) or on the [start page](index.md#startseite) in the card
of the setup with **+ New program**. How programs and setups belong
together is described under
[Setup and program](editor.md#besetzung-und-programm).

## The screen at a glance { #der-bildschirm-im-uberblick }

!!! warning "📷 Screenshot missing"
    **Subject:** “Program” task with the groups Switches and gears and Speed and take-up; at the bottom the timeline with the rows Take-up, Speed, Direction, Switches (expanded) and Gears; the red “Recording” band in the machine view.
    **How to create:** Customer build with a model licence, open a machine with one of your own changeover programs, “Program” tab, start recording.
    **Target file:** `assets/screenshots/braiding-simulator/programm.png`

In the **Program** task, a **click on a switch** switches it. A click on
a carrier or a gear selects it.

## Switching switches { #weichen-schalten }

What a click on a switch does depends on whether a program is selected
and whether recording is on. In short: without recording the start
position, with recording from here on.

| State | Effect |
|---|---|
| **Program selected, without recording** | Changes the **start position** of the program, whatever step the run is currently at. The switch is then in this position from the beginning: *W12 is now closed from the beginning — the program's start position has changed.* |
| **With recording** | Becomes a switching command from the current step. |
| **Without a program** | At the start, the click changes the switch over; mid-run, it applies to this run only. |

If you change the start position mid-run, the simulator recalculates the
run with the new start position up to the previous spot. A command in
step 1 for the same switch is adjusted as well. If the program switches
the switch itself later on, the message names the step: *From step 20 the
program switches it.* Up to there, the new start position applies.

The machine already shows the commands of step 1 at the start: switches,
run state and direction of the gears appear there as step 1 sets them.

* If the switch is on a **shift lever**, one click sets all switches of
  the lever together.
* **++ctrl++ + click** collects several switches into a **switch group**:
  a click on one of them then switches all of them; a click on another
  switch dissolves the group.
* Shift levers and switch groups follow the same rule as a single switch:
  without recording the start position, with recording a command from
  here on.
* **Fixed components** (X crossing, Y piece, groove blocks) cannot be
  switched; a click only selects them.

## "Switches and gears" group { #gruppe-weichen-und-rader }

At the top of the group, a note sums up the click rule: *A click on a
switch switches it; Ctrl+click collects several to switch together.
Without recording this changes the program's start position, i.e. from
the beginning. With recording on it becomes a command from the current
step. The same applies to starting and stopping gears.*

| Element | Effect |
|---|---|
| **Reverse all gears** | Reverses the running direction of all gears; all pairs stay counter-rotating, the braiding circle continues backwards. Grouped gears stay rigidly coupled. Takes effect from the next step boundary: at the start as the start position, mid-run without recording for this run only, with recording as a command. |
| **Adopt start state** | Saves the current position of gears and switches as the start of the program (*Program start adopted: … gears, … switches · setup: …*). The program stays with its setup. The run is then at the start. |
| **Repeat program** | Tick (on by default): the commands repeat with the program length as the period, typical for braid patterns. Without the tick, the program runs through once; after that, all positions stay as they are. |

Without a selected program, the program-related buttons are locked.

## "Speed and take-up" group { #drehzahl-und-abzug }

The summary shows the take-up range at the playhead: **Take-up**, steps,
braiding angle, lay length, PPI, take-up in m/min, speed in rpm, braid
diameter or braid width, and covering; the specified quantity is shown in
bold. Without a take-up, it reads *Take-up constant — the angle comes from
the preview. Set it in the “Take-up” row.*

| Button | Effect |
|---|---|
| **Change speed…** | Speed of the horngears from the step at the playhead, see [Speed](views.md#drehzahl). |
| **Change take-up…** | Take-up from the step at the playhead, see [Take-up](views.md#abzug). |

You drag a range in the **Speed** or **Take-up** row of the timeline. If
the operating mode changes within a take-up range (for example from round
to flat braid), the summary warns: *From step … the operating mode
changes. For the same target this part needs its own take-up, but the
machine runs one per take-up change: set a take-up change there.*

## Selection card: switch { #weiche }

If you click a switch in **Set up**, **Check** or **Output**, the card
shows *Switch W12 selected*. (In **Program**, the click switches the
switch instead of selecting it.)

* **Position:** *closed* (the tracks cross, carriers pass to the other
  horngear) or *open* (the tracks run past each other, every carrier stays
  on its gear). If it differs from the default position, the card says
  so.
* **Open switch** or **Close switch** switches it, in every task, with the
  same effect as a click.
* A switch with *No function (co-rotating or unsynchronized gears).*
  cannot be switched.

If the switch is on a **shift lever**, the card shows the lever below it
with its switches and the position (*Position 1*, *Position 2* or *mixed
(individually set)*). **Set lever to "…"** sets all switches of the lever
together; with recording, as program commands.

Fixed components only show their description:

| Component | Effect |
|---|---|
| **X crossing** | The tracks cross; transfer always takes place in both directions. |
| **Y piece** | Two inlets, one outlet. |
| **Groove block half circles** | Each track runs past the other, no transfer. Common on flat braid gears. |
| **Groove block diagonal** | Only one diagonal groove (/ instead of X). If a carrier runs against its end, a dead end results. |

## Selection card: gear { #rad }

The card *Gear n selected* shows how the gear is driven, and only the
buttons for what the real machine can do on this gear.

### Horngear group and switch-out gear { #flugelradgruppe-und-switch-out-rad }

Normal gears run in sync with all others (*Not grouped. In operation it
runs in sync with all gears.*); there are no buttons for them. The
following have their own drive:

* a **horngear group** (the gears are marked *G1*, *G2* …): start, stop
  and direction change always affect the whole group,
* a **switch-out gear**: it can be stopped so that its carriers park.

| Button | Effect |
|---|---|
| **Stop horngear group** / **Start horngear group** | Stops or starts the whole group; while it stands, its carriers park. |
| **Reverse horngear group** | Reverses only this group; within the group, neighbors stay counter-rotating. |
| **Stop switch-out** / **Start switch-out** | Stops or starts the switch-out gear; while it stands, its carriers park. |
| **Reverse switch-out** | Reverses only this gear. |

**Stop** and **Start** follow the same rule as a switch click: with a
program selected and without recording, they change the program's start
position, whatever step the run is at (*Horngear group 1 (gears …) is
now stopped from the beginning — the program's start position has
changed.*); a command in step 1 is adjusted as well, and a later command
for the same gear is named in the message. With recording they become a
command from the current step. Without a program they act as the start
position at the start and for this run only mid-run.

**Reverse** takes effect from the next step boundary: at the start as the
start position, mid-run without recording for this run only, with
recording as a program command.

Below the hub of these gears, a run symbol shows whether they are running
(▶) or stopped (⏸); in the **Program** task, a click on it starts or stops
the gear, with the same effect as the buttons.

If a gear runs against its base direction, the card warns: *Runs
backwards in operation, against the base direction.*

### Turning unit: carrier exchange { #dreheinheit-kloppelwechsel }

On a **turning unit**, **Trigger carrier exchange** swaps one carrier
each between the two neighboring gears; meanwhile, the rest of the
machine stands still. With recording, this becomes a command in the
program; without recording, the exchange applies to this run only. If the
exchange is not possible right now, the card states the
reason and the *Next possible step* with the link **jump there**.

### Pitch in this run { #teilung-im-lauf }

Some gears have several pitches, for example an edge gear with 7 slots
that can work as a 5-slot or 3-slot gear. For these, the card shows the
selection **Pitch in this run** with *5-slot pitch*, *3-slot pitch*,
etc.:

| State | Effect |
|---|---|
| At the start | The selected pitch becomes the start position of the program: *Gear 3 uses the 5-slot pitch in this program.* |
| With recording | The gear changes from the current step: *Gear 3 uses the 3-slot pitch from step 12 — recorded in the program.* |
| Mid-run without recording | For this run only. |

The change happens at the step boundary. The gear is driven individually
and turns to the next position of the new pitch; the carriers stay in
their slots.

!!! warning "When a pitch change is dropped"
    If, at the change, a carrier sits in a slot that the new pitch does
    not use, **the change is dropped**: the gear keeps its pitch, and a
    note under [Check](check.md) names the step and the gear. Otherwise
    the carrier would arrive at the transfer point at the wrong time.
    Place the change at a step at which no carrier is in such a slot.

Without a program, the selection is locked: *The pitch is saved in the
time program. Without a program the gear uses the largest one.*

## Recording { #aufnahme }

**Record** in the [playback bar](editor.md#wiedergabe) switches recording
on. The following are recorded as a command at the current step: switch
clicks (also via shift levers), **Reverse all gears**, stopping, starting
and reversing horngear groups and switch-out gears, carrier exchanges and
pitch changes. Placing and removing carriers remains part of the setup.
Without recording, a click on a switch or on the run state of a gear
changes the start position, see [Switching switches](#weichen-schalten).

* During recording, a red band **Recording** with the position and the
  number of commands appears at the top left of the machine, and the
  button is called **Stop recording**.
* A click on a switch always switches it, whichever task is open on the
  right; a right-click also switches it.
* If the run continues or you jump beyond the end with **Go to step**,
  the program gets longer.
* Undo and redo are locked.
* If no program has been created yet, the simulator asks whether it
  should create one (**Create program**).

When you stop, it reports how many commands were recorded.

How to record a changeover:

1. Select or create a program, set the run to the start.
2. Switch on **Record** and press **Start**.
3. At the desired step, press **Pause** (or jump there with **Go to
   step**).
4. Click the switches that should change over.
5. Let the run continue, switch back if necessary, and at the end click
   **Stop recording**.
6. Check the result in the [Check](check.md) task, then click **Save**.

## Timeline { #zeitachse }

The timeline at the bottom shows the selected program as rows over the
steps. It is only visible with a program; with the **Timeline** button on
the right of the playback bar you hide and show it. You change its height
at the splitter between the machine and the playback bar.

!!! warning "📷 Screenshot missing"
    **Subject:** Timeline of a changeover program with the rows Take-up (two colored ranges), Speed, Direction, Switches with W rows (blocks and switching points), Gears with a horngear group and a pitch row; context menu open.
    **How to create:** Open a machine with a program (e.g. variation braider with a pitch change), “All rows” off, right-click in a W row.
    **Target file:** `assets/screenshots/braiding-simulator/zeitachse.png`

### Timeline header { #kopf-der-zeitachse }

| Element | Effect |
|---|---|
| *Timeline — &lt;program&gt;* | Title. |
| Zoom − / + | Levels 50 to 300 %. |
| **Whole program** | Fits the whole program to the width (default). |
| **Length** − / + | Program length in steps (1 to 999). Lengthening makes room for further commands; shorter than the last command is not possible. |
| **All rows** | Default: only rows with commands or a differing start state. With the tick, the other rows too, so that you can set commands in fresh rows. **New program…** switches it on. |

### Rows { #zeilen }

| Row | Shows |
|---|---|
| Step row (top) | Step numbers from 1 and the red playhead. A click or drag jumps. |
| **Take-up** | The take-up ranges as colored blocks with their value, the color depending on the setpoint (take-up blue, lay length turquoise, braiding angle orange, PPI violet). Hatched where the operating mode changes. Without a take-up: *uniform (angle from the preview)*. |
| **Speed** | The speed in rpm per range, or *not set*. |
| **Direction** | Running direction of **all** gears: block = forward, chevrons = backward, triangle at a reversal. |
| **Switches** (expandable) | Below it, one row per switch **W12**: block = closed, thin line = open, circle = switching command. The group row shows as a bar how many switches are closed. |
| **Gears** (expandable) | Below it, one row per horngear group **Group 1**, per switch-out gear and turning unit **G5** (block = running, line = stopped, chevrons = backward, diamond = carrier exchange) and per gear with several pitches **G5 pitch** with the blocks *5-slot*, *3-slot*. |

### Mouse { #maus }

| Action | Effect |
|---|---|
| Click in a W row | Sets a switching command (the switch changes over from here) or removes an existing one. |
| Click in the **Switches** row | Changes over all switches from here. |
| Click in **Direction** | Reverses all gears from here or removes the reversal. |
| Click in a group or switch-out row | Run/stop from here; with ++ctrl++, reverse the direction of rotation from here. |
| Click in a turning unit row | Sets or removes a carrier exchange. |
| Click in a pitch row | The other pitch from here; on a marker, removes the change. |
| Click in **Take-up** or **Speed** | Opens the dialog from this step, see [Take-up](views.md#abzug) and [Speed](views.md#drehzahl). |
| Drag in a row | Applies the state only over the dragged range; afterwards, the old state applies again. In **Take-up** and **Speed**, the dialog for the range opens. |
| Drag that starts on a command | Moves the command. |
| Click in the label | Selects the row; with ++ctrl++ further rows, with ++shift++ a range (only rows of the same kind). Dragging in a selected row switches all selected rows together. |

A double-click in a row does not remove the command you have just set.
The mouse wheel scrolls the timeline.

### Take-up and speed in the timeline { #abzug-und-drehzahl-in-der-zeitachse }

A click in **Take-up** or **Speed** sets a new value **from this step**;
it applies until the next change. Dragging sets it **only for the
range**; afterwards, the previous value applies again. The dialogs are
described under [3D preview and take-up](views.md#abzug).

Like **Direction** and **Switches**, **Take-up** and **Speed** span the
full width of the timeline, also beyond the end of the program:

* Without **Repeat program**, the last range continues to apply after the
  end of the program.
* With **Repeat program**, the ranges recur with the program length.
* Identical neighboring ranges merge into one block.
* Beyond the end of the program, the tooltip names the range that applies
  there.

### Right-click menu { #rechtsklick-menu }

Depending on the row, a matching command appears at the top, for example
*Switch W12 at step 20*, *Reverse all gears at step 20*, *Stop at step
20* or *From step 20 with 3-slot pitch*. Below it, always:

| Entry | Effect |
|---|---|
| **Insert steps…** | Inserts empty steps before a step (default 4); what follows moves back. In the new steps, the state before them continues to apply. |
| **Delete steps…** | Deletes steps; what was switched there continues to apply afterwards, later commands move forward. |
| **Move section…** | Moves the commands of a step range by a number of steps (positive later, negative earlier), optionally **Selected rows only**. |
| **Copy section…** | Copies the commands of a section to another place, also from another program of this machine (**From program**). |
| **Go to step n** | Sets the playhead. |

If a gear row contains a command that the machine cannot execute
(stopping or reversing a single gear without its own drive, from an older
program), the row is hatched and the tooltip says *Not machine-capable:
on the machine all gears run in sync.* Use **Remove single-gear commands
of G…** in the right-click menu to delete these commands.

## In the web app { #in-der-web-app }

* The timeline has no right-click menu and no row selection; dragging
  applies a state over the range but does not move a command. You move,
  jump to and remove commands in the **Commands (n)** list of the
  **Program** task; the **Length** of the program is also there.
* The rows are arranged somewhat differently: one row per shift lever,
  one row **All gears**, plus one row each per horngear group, switch-out
  gear, turning unit and pitch.
* During recording, the program plays without repetition; when you stop,
  the length grows up to the step reached.

Details: [Braiding Simulator (web app)](../web/braiding-simulator.md).

## Related pages { #verwandte-seiten }

* [Check](check.md) — check whether the program runs collision-free.
* [3D preview and take-up](views.md) — take-up and speed.
* [Output](output.md) — the program as a switching plan.
* [Multiple braiding heads](multiple-heads.md)
