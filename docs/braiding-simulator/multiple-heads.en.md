# Multiple braiding heads

!!! abstract "Reference — How the Braiding Simulator shows two-head machines: number of carriers, numbers and running direction per head, shared take-up, Machine 3D"

## What you need this page for { #wofur-sie-diese-seite-brauchen }

Multi-head machines such as the RU 2/12-80 have several **braiding heads**
on one drive: each head has its own horngears, its own braiding point and
its own take-up disc; motor and take-up gearbox are shared. The Braiding
Simulator detects the heads by itself and shows counts, numbers and
running direction per head.

## How the simulator recognizes a head { #woran-der-simulator-einen-kopf-erkennt }

A braiding head is a group of gears that has no transfer to the rest of
the machine, regardless of how the switches are set. A single gear without
a transfer belongs to the nearest head.

Machines whose braiding circles are connected via switches, for example a
machine that switches between *flat braid 32* and *2 × round 16*, have
**one** head. There, the switches decide whether one or two braids are
produced; the [3D preview](views.md#infozeilen-unter-dem-bild) shows this
in its info line.

The term *braiding head* does not appear in the user interface; you
recognize a multi-head machine by the number of carriers.

## What applies per head { #was-je-kopf-gilt }

| Topic | Behavior |
|---|---|
| **Number of carriers** | The start page, the setups and the status line show *2 × 12 carriers* if all heads are set up the same way, otherwise for example *12 + 10 carriers*. |
| **Carrier numbers** | Each head counts from 1: an RU 2/12-80 has the numbers 1 to 12 twice. A new carrier gets the lowest free number **in its head**. |
| **Running direction** | Applies around the center of the respective head, not around the machine center. This affects the [Running direction](editor.md#ansicht) view and **Color by running direction** in the [selection card](populate.md#auswahlkarte-kloppel). |
| **Configurations** | *Full*, *Half* and *Tandem* from Herzog apply per head; *Full* and *Half* occupy both running directions equally. |
| **Take-up** | All heads are connected to the same take-up gearbox. The [take-up](views.md#abzug) is set as on a single-head machine and applies to all heads; it is measured at head 1. |
| **Machine 3D** | The ["Machine" view](views.md#ansicht-maschine) shows braiding point, braid and take-up disc per head. Labels and fixed views refer to head 1. |

Switches, gears, timeline and switching plan work as on a single-head
machine; a program switches all heads together because they are connected
to one drive.

## Desktop app and web app { #desktop-app-und-web-app }

Both show multiple braiding heads in the same way.

## Related pages { #verwandte-seiten }

* [Set up](populate.md)
* [3D preview and take-up](views.md)
* [Braiding Simulator](index.md)
