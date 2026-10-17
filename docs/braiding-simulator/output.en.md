# Output: switching plan

!!! abstract "Reference — The “Output” task: print the switching plan of a time program for the braiding machine's control, save it as a PDF or as a CSV table"

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

The **switching plan** translates a time program into what the control of
the real machine needs: when which switch, which shift lever, which gear
and which take-up changes, each with step, horngear revolution, time from
start and take-up length. You pass it on to the electrical or controls
department or file it with the program in the order documents.

!!! info "Only in the desktop app"
    The switching plan only exists in the program. In the web app, the
    **Output** task only shows a note about it, see
    [Web app](../web/braiding-simulator.md).

It is based on the **states** of the simulation, not on the individual
commands: the switching plan shows what actually changes on the machine.
A shift lever appears as **one** action if all its switches are moved
together.

## The screen at a glance { #der-bildschirm-im-uberblick }

!!! warning "📷 Screenshot missing"
    **Subject:** “Output” task in the right-hand bar: heading Switching plan, program name, program length, switching points, take-up ranges, print template “Standard switching plan”, buttons Print…, Save as PDF…, Save as CSV….
    **How to create:** Customer build with a model licence, open a machine, choose a program with take-up, open the “Output” tab on the right.
    **Target file:** `assets/screenshots/braiding-simulator/ausgeben.png`

The **Output** task (*Switching plan for the control: print, as PDF or
CSV.*) shows a summary of the selected program at the top, below it the
print template and the buttons.

## Controls in detail { #bedienelemente-im-detail }

### Summary { #zusammenfassung }

Under the heading **Switching plan** you see the name of the program and:

| Line | Meaning |
|---|---|
| **Program length** | Length of one run in steps. |
| **Switching points** | How many steps contain an action. |
| **Take-up ranges** | How many sections with their own take-up the program has (only if there are any). |
| **Shift levers** | How many shift levers the machine has (only if there are any). |

Below this, the [notes](#hinweise) appear in orange. If no program is
selected, it reads *No time program selected. Choose or create one under
“Program” at the top.*, and the buttons are locked.

### Print template { #druckvorlage }

Selection of the templates with the usage **Braiding Simulator**.
**Standard switching plan** is always first. You design your own templates
in the [Print editor](../print-templates/index.md): it has the usage
**Braiding Simulator** with the element group **Braiding Simulator**
(elements **Program data**, **Start state**, **Switching sequence**,
**Take-up**, **Shift lever** and **Switching diagram**). The program
remembers the template selected last.

### Buttons { #knopfe }

| Button | Effect |
|---|---|
| **Print…** | Opens the switching plan with the selected template in the print preview (window *Switching plan: &lt;program&gt;*). |
| **Save as PDF…** | Saves the switching plan with the selected template as a PDF. |
| **Save as CSV…** (**Data** area) | Saves program data, start state, switching sequence, take-up, shift levers and the states of all switches and gears per switching point as a table, for example for Excel. |

When saving, the program suggests the file name *&lt;machine&gt; -
&lt;program&gt; - Switching plan* and remembers the folder. Afterwards
*Saved: &lt;file&gt;* appears.

The *View Braiding Simulator* right is sufficient for output, see
[Rights](licence.md#rechte).

## Content of the switching plan { #inhalt-des-schaltplans }

The **Standard switching plan** template is A4 landscape and has three
pages. Page 1 carries the title *Switching plan: &lt;program&gt;* with
the date, the machine, program data and start state side by side, and the
switching diagram; page 2 the switching sequence; page 3 take-up and
shift levers.

### Program data { #programmdaten }

| Row | Content |
|---|---|
| **Version** | Version of the program. |
| **Program length** | Steps per run. |
| **Horngear revolutions per run** | |
| **Sequence** | *repeats* or *once*. |
| **Steps per horngear revolution** | |
| **Horngear speed** | rpm or *not set*. |
| **Step duration** | Seconds per step. |
| **Duration per run** | Minutes and seconds. |
| **Take-up length per run** | mm. |
| **Setup**, **Carriers** | Name of the setup and number of carriers. |
| **Material diameter** | mm. |
| **Braiding angle measured to** | *cross direction* or *braid axis* (only if the program has take-up ranges), see [Braiding angle reference](views.md#flechtwinkel-bezug). |

### Start state { #startzustand }

How shift levers, switches, gears (running, stopped, direction of
rotation), pitches and take-up are set at the start; columns
**Component**, **State**, **Details**.

### Switching sequence { #schaltfolge }

One row per action with **No.**, **Step**, **Revolution**, **Time from
start**, **Length from start**, **Component**, **Action** and
**Details**. Examples:

| Component | Action |
|---|---|
| *Switch W3* | *close*, *open* |
| *Shift lever 1* | *to …* (position) |
| *All gears* | *stop* (*carriers park*), *start*, *reverse* |
| *Take-up* | new take-up with its target |

At the end it reads *End of program after step n — continue with step 1*
(the program repeats) or *— all positions stay as they are*. These are
followed, if applicable, by the actions that are needed when repeating.

### Take-up, shift lever, switching diagram { #abzug-stellhebel-schaltdiagramm }

* **Take-up** — the take-up ranges with step, length, take-up, take-up
  per revolution, lay length, braiding angle, PPI and target.
* **Shift lever** — which switches belong to which shift lever and how
  they are set in position 1 and 2.
* **Switching diagram** — a displacement-step diagram: one row per
  component whose state changes, the program steps horizontally.

### CSV table { #csv-tabelle }

The CSV file (separator: semicolon) contains the same blocks as the
printout. The numbers are in the cell without a unit so that Excel can
calculate with them. In addition there is the block **States per
switching point**: one row per switching point with one column per switch
(W1, W2 …), per gear (G1, G2 …) and the take-up in m/min. Legend:
*Switches 1 = closed, 0 = open · Gears 1 = running, 0 = stopped, -1 =
running against the design direction · valid until the next row*. This
block only exists in the CSV, not in the printout.

## Notes { #hinweise }

The switching plan reports what cannot be implemented like this on the
machine or is still missing. In the printout, the notes appear at the
beginning of the switching sequence.

| Note | Meaning |
|---|---|
| *Horngear speed missing: times and take-up lengths are unknown.* | Set a [speed](views.md#drehzahl) in the timeline. |
| *Lay length, braiding angle and PPI come from the 3D preview: switch on the braid preview for complete values.* | The 3D preview is hidden; switch it on via **View > 3D preview**. |
| *Shift lever n is mixed at the start — not possible on the machine.* | The switches of a shift lever are set differently at the start. |
| *The program only partly moves a shift lever — not possible on the machine. The switches are listed individually in the switching sequence.* | The program switches only some of the switches of a shift lever. |
| *When repeating, switches or gears are set differently than at the first start — the second run differs from the first.* | The program does not return to its start state at the end. See [Check](check.md). |

## Related pages { #verwandte-seiten }

* [Program](program.md) — the time program from which the switching plan
  is created.
* [3D preview and take-up](views.md) — take-up and speed.
* [Print editor](../print-templates/index.md) — your own templates with
  the usage **Braiding Simulator**.
