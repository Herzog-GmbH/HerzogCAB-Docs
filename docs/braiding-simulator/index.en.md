# Braiding Simulator

!!! abstract "Reference — The Braiding Simulator: set up machine models from Herzog, create time programs, check them for collisions and output them as a switching plan; plus the start page with your machines"

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

With the **Braiding Simulator** you create the program for a braiding
machine on the PC instead of at the machine. You place the carriers,
define when which switch changes over, and see immediately whether the
carriers run without collisions and what the braid will look like. You
pass the finished program on to the control as a switching plan.

Herzog supplies the machine as a ready-made **machine model**: horngears,
slots, switches and tubes exactly as the machine is built. You do not have
to design anything. The model does not bring carriers or programs: you set
up the empty machine yourself and create your setups and programs on it.

The Braiding Simulator is available in the desktop app and in the web
app, with a [model licence](licence.md) in addition to the full version
subscription.

## Basic terms { #grundbegriffe }

| Term | Meaning |
|---|---|
| **Machine model** | The empty machine from Herzog: gears, switches, tubes. It cannot be changed in the Braiding Simulator. New versions of a model arrive automatically. |
| **Setup** | Which carriers stand where, with colors, ply count, material diameter and covering. A setup is created when you set up the empty machine and save it. A machine can have any number of setups. |
| **Time program** (program for short) | The start position of switches and gears and the commands that switch during the run: switches, reversal, take-up, speed. Each program belongs to exactly one setup; on a setup you create as many programs as you like. |
| **Step** | The time unit of the simulation: every gear turns on by one pitch. Programs are as many steps long as you define; as a rule, they repeat. |
| **Repeat** | After how many steps the machine is back in its start state. A repeat reached without a collision proves that the program runs collision-free permanently. |
| **Collision**, **dead end** | Two carriers meet, or a carrier cannot go any further. Both stop the simulation. |

!!! info "The machine decides"
    The Braiding Simulator only allows what the real machine can do. All
    horngears run synchronously on one drive. You can switch the switches
    (individually or via a shift lever), the running direction of **all**
    gears together, and gears with their own drive, that is horngear
    groups and switch-out gears. Stopping or reversing a single gear is
    not possible on the machine and therefore not in the simulator either.

## How you work with the Braiding Simulator { #so-arbeiten-sie-mit-dem-flechtsimulator }

```mermaid
flowchart LR
  A["Start page:<br>choose machine"] --> B["Set up:<br>carriers, colors, yarn"]
  B --> C["Program:<br>switches, take-up, speed"]
  C --> D["Check:<br>collision-free, repeat"]
  D --> E["Output:<br>switching plan"]
  D -. Errors .-> C
```

On the right of the simulator, the **task bar** guides you through these
steps: **Set up**, **Program**, **Check** and **Output**. Instructions
from the first click to the switching plan are given under
[Create a braiding program](../tasks/create-braiding-program.md).

<div class="grid cards" markdown>

- :material-monitor-dashboard: **The simulator screen**

    ---

    Header bar, machine view, selection card, playback, keys and mouse.

    [:octicons-arrow-right-24: Screen](editor.md)

- :material-dots-hexagon: **Set up**

    ---

    Place and color carriers; ply count, yarn, tubes.

    [:octicons-arrow-right-24: Set up](populate.md)

- :material-timeline-clock-outline: **Program**

    ---

    Switching switches, recording, timeline, pitch in this run,
    horngear groups.

    [:octicons-arrow-right-24: Program](program.md)

- :material-check-decagram-outline: **Check**

    ---

    Messages, collision check, repeat and interlacing.

    [:octicons-arrow-right-24: Check](check.md)

- :material-file-table-outline: **Output**

    ---

    The switching plan for the control: print, PDF, CSV.

    [:octicons-arrow-right-24: Output](output.md)

- :material-video-3d: **3D preview and take-up**

    ---

    Braid, schematic and machine in 3D; take-up, speed,
    braiding angle reference.

    [:octicons-arrow-right-24: 3D preview](views.md)

- :material-numeric-2-box-multiple-outline: **Multiple braiding heads**

    ---

    Two-head machines: numbers, running direction and take-up per head.

    [:octicons-arrow-right-24: Multiple braiding heads](multiple-heads.md)

- :material-key-outline: **Licence and rights**

    ---

    Full version subscription, model licence per user, rights, offline limit.

    [:octicons-arrow-right-24: Licence and rights](licence.md)

</div>

## Start page { #startseite }

Clicking **Braiding Simulator** in the navigation opens the start page
with the machines assigned to you.

!!! warning "📷 Screenshot missing"
    **Subject:** Start page of the Braiding Simulator: on the left the list of licensed machines with status line, on the right the selected machine with “valid until”, 2D top view and the section Setups and programs: two cards, one per setup, with key figures, below each its indented programs with Open and ⋯, “+ New program” in every card; at the bottom the buttons New setup and Delete own….
    **How to create:** Customer build with account sign-in and at least one assigned model licence, Navigation > Braiding Simulator.
    **Target file:** `assets/screenshots/braiding-simulator/startseite.png`

### List of machines (left) { #liste-der-maschinen-links }

One entry per machine model, in alphabetical order:

* **Name of the model**, in bold. Gray if the model cannot be used at the
  moment.
* Below it your own [braiding machines](../master-data/braiding-machines.md)
  with the same catalogue type, otherwise the catalogue type. The tooltip
  names the catalogue type.
* Where applicable, a status line: *New version from Herzog* (blue; the
  model has been updated, the line disappears after the first opening),
  *Loading*, *Licence expired on &lt;date&gt;*, *No valid licence* or
  *Connection to the licence server required*. What the red states mean
  is described under [Licence and rights](licence.md#wenn-eine-lizenz-wegfallt).
* A **lock** indicates that another user is currently editing the setups
  and programs of this model; the tooltip names that user. See
  [Multiple users in the same workspace folder](../basics/multi-user.md).

A **double-click** opens the model, provided it can be used. Below the
list you can see whether synchronization with the licence server is
running (*Synchronizing with the licence server.*), when it last succeeded
(*As of: …*) or that there is currently no connection (*No connection to
the licence server; showing the last known state.*).

If the list is empty, it shows the reason:

| Text | Meaning |
|---|---|
| *Sign in with your Herzog account. The machines your account holds a licence for will then appear here.* | The program is not signed in with the customer account. |
| *The machines are being loaded from the licence server.* | The list is about to arrive. |
| *No machine model is assigned to you. Your administrator assigns model licences in the licence portal.* | Your account has model licences, but none for you. See [Assign machine models](../portal/models.md). |
| *No machines yet. Herzog activates the machine models for your account; they then appear here.* | Your account does not have a model licence yet. |

### Selected machine (right) { #gewahlte-maschine-rechts }

At the top are the name and the validity of the licence (*valid until
&lt;date&gt;* or, in red, *expired on &lt;date&gt;*) and, where applicable,
a note, for example *Herzog has updated the model, version … instead of
…. Your setups and programs are kept.* Below that, a top view shows the
gear layout of the machine.

Below that follows the section **Setups and programs**: one card per
setup, with its programs indented below it. If the machine has no setup
yet, it reads *No own setup yet. “New setup” places the carriers on the
empty machine; you then create programs on it.*

#### Card of a setup { #karte-einer-besetzung }

| Element | Content or effect |
|---|---|
| Name and key figures | Name of the setup, below it the number of carriers, ply count, yarn Ø, covering and core Ø, where set, and the number of programs, for example *32 carriers · Ply count 2 · Yarn Ø 0.25 mm · 2 programs*. Without a program it reads *no program yet*. |
| **Open** | Opens the setup with its most recently used program in the [simulator screen](editor.md). |
| **⋯** | **Rename…**, **Duplicate** (copy of the setup including its programs, name *… – copy*) and **Delete…** (deletes the setup together with its programs; the confirmation prompt names the programs). |
| Program row | One row per program of the setup with name, number of steps, speed and take-up, for example *Round · 48 steps · 120 rpm · Take-up 1.20 m/min*. Speed and take-up only appear if the program has them; several ranges appear as a span. |
| **Open** in the program row | Opens the program with its setup. |
| **⋯** in the program row | **Rename…**, **Duplicate** (copy on the same setup, name *… – copy*), **Assign to another setup** (submenu with the other setups of the machine) and **Delete…**. |
| **+ New program** | Opens the setup and creates a new time program on it; the simulator asks for the name. |

#### Programs without a setup { #programme-ohne-besetzung }

Your setups and programs from older program versions are kept. A setup
from Herzog that one of your programs refers to appears as a normal setup
in the list. Programs that do not belong to any setup yet appear at the
end in the group **Without setup** (*Older programs that do not belong to
any setup yet. “Assign” gives them one.*). Instead of **Open**, each row
has the button **Assign…**: it lists the setups of the machine, and your
choice gives the program to that setup. If there is no setup yet,
**Assign…** is locked. Here the **⋯** menu only contains **Rename…** and
**Delete…**.

#### Buttons below the section { #knopfe-unter-dem-abschnitt }

| Button | Effect |
|---|---|
| **New setup** | Opens the empty machine in the [Set up](populate.md) task. Place the carriers and save them with **Save as new setup…**. |
| **Delete own…** | After a confirmation prompt, deletes all your own setups and time programs for this machine. The machine stays as Herzog supplies it. |

**New setup**, **Delete own…**, **+ New program** and the entries of the
**⋯** menus require the *Edit Braiding Simulator* right. Without a valid
licence, **Open**, **New setup** and the menus of the cards are locked;
your setups and programs remain visible.

Whatever you rename, duplicate, assign or delete on the start page takes
effect immediately, without **Save**. If another user is currently editing
the setups and programs of this machine (lock in the list), the start page
refuses every change with *Someone else is editing the programs of this
machine right now.*

!!! info "Where your setups and programs are stored"
    The desktop app stores your own setups and programs per model in the
    [workspace folder](../admin/storage-location.md); with
    [cloud synchronization](../admin/settings/license.md) they also reach
    the web app and come back from it. The machine model itself remains
    unchanged and is only accessible via your licence.

## Desktop app and web app { #desktop-app-und-web-app }

Operation and tasks are the same in both. The web app does not yet have
some of the functions:

| Function | Desktop app | Web app |
|---|---|---|
| Print the switching plan, save it as PDF and CSV | ✔ | — |
| Covering and material diameter per setup | ✔ | Material diameter per browser, no covering |
| Thread yarns into tubes with a click | ✔ | — |
| Operation on tablet and smartphone | — | ✔ |

The details are given under [Braiding Simulator (web app)](../web/braiding-simulator.md).

## Related pages { #verwandte-seiten }

* [Create a braiding program](../tasks/create-braiding-program.md) —
  guide.
* [Licence and rights](licence.md)
* [Assign machine models](../portal/models.md) — in the licence portal.
* [Designer](../designer/index.md) — design and color braids; the
  Braiding Simulator, by contrast, creates programs for a specific machine.
