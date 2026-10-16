# Check

!!! abstract "Reference — The “Check” task: errors and notes, collision check over the whole run, basic run without program, repeat and interlacing"

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

Before a program goes to the machine, it must be certain that the
carriers run **permanently collision-free** and that the braid interlaces
as intended. The **Check** task collects all errors and notes and, at the
click of a button, calculates the whole run until the machine is back in
its start state (repeat). Only then is it proven that the program can be
repeated as often as required.

## The screen at a glance { #der-bildschirm-im-uberblick }

!!! warning "📷 Screenshot missing"
    **Subject:** “Check” task with the Messages group (a note with “Show location”) and the Collision check group after “Check current arrangement”: “✅ Collision-free — repeat after … steps”, color pattern, interlacing per section; in the header the chip “⚠ 1 note”.
    **How to create:** Customer build with a model licence, open a machine with a changeover program, “Check” tab, click “Check current arrangement”.
    **Target file:** `assets/screenshots/braiding-simulator/pruefen.png`

A dot on the **Check** tab shows whether there is something to pay
attention to: red for errors, orange for notes. The chips **⛔ n errors**
and **⚠ n notes** in the header count the same messages; clicking a chip
opens this task. In the **Check** task, a click in the machine selects,
a right-click toggles a switch.

## "Messages" group { #gruppe-meldungen }

The list shows the **errors** (⛔, red) first, then the **notes** (⚠,
orange); without messages it reads *No errors or notes.*

| Button on a message | Effect |
|---|---|
| **Show location** | Selects the gears concerned, zooms the machine to them and, for a collision, jumps to the start of the step. |
| **Jump to step** | Collisions only: sets the run to this step. |

Typical messages:

| Message | Type | Meaning |
|---|---|---|
| *Collision at Program step …: gear … and gear … block each other.* | Error | Two carriers meet at the transfer between these gears. Playback stops, the gears are marked. |
| *Dead end at …: on gear … a carrier runs into the diagonal groove block …* | Error | A carrier runs into the end of a diagonal groove. |
| *No transfer works — this machine model cannot be simulated like this.* | Error | The model does not fit; contact Herzog. |
| Notes on the 3D preview | Note | For example, that a core is only shown in tubular mode or that the preview cannot draw a covering. |
| Notes on the layout and the program | Note | For example, commands the simulator ignores, or a [dropped pitch change](program.md#teilung-im-lauf) with step and gear. |

## "Collision check" group { #gruppe-kollisionsprufung }

| Element | Effect |
|---|---|
| **Check current arrangement** | Sets the run to the start and calculates it in one go: collisions, repeat, color pattern, whether every carrier returns to its place, and the interlacing per section. |
| **Basic run without program** | Checkbox: checks the setup only with the start position of the switches and gears, without the commands of the time program. This shows you whether the setup runs as such before you add changeovers. |

After every change to the program, arrangement or start position, it reads
*Program or arrangement changed — please check again.*

### Reading the result { #das-ergebnis-lesen }

The result begins with *Check from start arrangement:* (or *…, basic
run without program:*). Then:

| Line | Meaning |
|---|---|
| *✅ Collision-free — repeat after n steps (m carriers)* | The run returns to the start state after n steps without carriers meeting. The program runs permanently collision-free. |
| *❌ Collision at step n: gear a ↔ gear b* | Carriers meet at this transfer. |
| *❌ Dead end at step n: …* | A carrier runs into the end of a diagonal groove. |
| *No collision in n steps, repeat not reached.* | There was no collision up to the check limit, but the start state did not come back. This does not prove that the run is collision-free. |
| *Check not possible.* | For example without carriers. |

Below this, where applicable:

* **Return of the carriers and the color pattern**, for example *Afterwards
  every carrier is back at its starting place.*, *The color pattern is as at
  the start again after n steps.* or *⚠ The color pattern does not return to
  the start within n steps.* *Carriers of the same color swap places
  permanently* means: the pattern is correct, but not every carrier returns
  to its own place.
* For programs with a changeover: *After one pass the color pattern is as in
  the basic run without changeover.* or *⚠ … shifted against the basic run —
  the changeover does not return cleanly.*
* **Repeat longer than the program:** *Occupancy and color pattern are as at
  the start after every pass; only after n steps are the horngears also back
  in their starting rotation.* Plus a suggestion *With length …, repeat =
  program length.*; clicking **length …** sets the program length and
  checks again.
* **Interlacing:** per section (*Step a–b:*) the type of braid, for
  example *Braid, every yarn crosses 4 others.*, *Flat braid, …*,
  *Twisting — no carrier changes horngear.*, *Spiral — all carriers run in
  one direction, the yarns do not interlace.* or *Standstill.*
  *⚠ Carrier n does not interlace here.* points to a carrier that does not
  take part in the braiding in this section.
* **Take-up during twisting:** *ℹ During twisting in steps a–b the take-up
  keeps running.* With **Set take-up to 0 there**, the simulator sets the
  take-up in this range to 0.

## What the simulator does not allow { #was-der-simulator-nicht-zulasst }

The simulator also checks whether a program can be executed on the real
machine. All horngears run synchronously; only horngear groups and
switch-out gears can be stopped or reversed individually. If you try it
on another gear, the status line reports *Gear … has no drive of its own
and runs in sync with all gears.* If such commands come from an older
program, the [timeline](program.md#zeitachse) shows the row hatched as
*Not machine-capable*; remove the commands with a right-click.

## Typical procedure { #typischer-ablauf }

1. Choose a setup, switch on **Basic run without program**, click
   **Check current arrangement**: the setup must run collision-free.
2. Clear the checkbox, choose a program and check again.
3. With ❌: **Jump to step**, look at the machine, move or change the
   command in the [timeline](program.md#zeitachse).
4. With *repeat not reached* or a repeat that is much longer than the
   program: accept the **length …** suggestion.
5. When everything is ✅: **Save** and output the
   [switching plan](output.md).

## In the web app { #in-der-web-app }

* The collision check runs automatically after every change; there is no
  **Check current arrangement** button.
* It shows collision or dead end, repeat and number of carriers, plus
  *All commands can be executed on the machine.* or the findings, for
  example *Step …: gear … stops or starts on its own — on the machine all
  gears run synchronously.* or a pitch change that is dropped. It does not
  show the color pattern, the return of the carriers or the interlacing
  per section.
* On a finding, **Remove command** removes the command concerned.
* If Herzog has stored notes on the model, they appear under **Notes**.

Details: [Braiding Simulator in the web app](../web/braiding-simulator.md).

## Related pages { #verwandte-seiten }

* [Program](program.md)
* [Set up](populate.md)
* [Output](output.md) — the notes of the switching plan.
