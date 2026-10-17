# Set up

!!! abstract "Reference — The “Set up” task: placing and removing carriers, colors, ply count and numbers, yarn and covering, tube threads and saving setups"

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

Before a program can run, the machine needs carriers. The quickest way is
to select a **configuration** from Herzog at the top (*Full*, *Half*,
*Tandem* …) and adjust it. You can also set up the machine by hand.
Colors, ply count and yarn determine what the braid looks like in the
[3D preview](views.md); together you save everything as a **setup**.

Placing and removing carriers always belongs to the setup, never to the
program. Even during recording, it does not become a program command.

## The screen at a glance { #der-bildschirm-im-uberblick }

!!! warning "📷 Screenshot missing"
    **Subject:** “Set up” task with the groups Carriers (Color for new carriers, Select all carriers, Remove all carriers), Yarn (Material diameter, Covering) and Setup; above it the selection card of a carrier with ply count 3 and individual colors.
    **How to create:** Customer build with a model licence, open a machine, “Set up” tab, click a carrier and set the ply count to 3.
    **Target file:** `assets/screenshots/braiding-simulator/bestuecken.png`

In the **Set up** task, the following applies in the machine view:

* **Click on an empty position** places a carrier in the color for new
  carriers.
* **Click on a carrier** selects it; the
  [selection card](#auswahlkarte-kloppel) shows its properties.
* **Right-click on a carrier** removes it.
* **++ctrl++ + click** or **++ctrl++ + drag** selects several carriers,
  **++ctrl+a++** selects all.
* **Click on an empty tube** threads the yarn in, see
  [Tube threads](#rohrfaden).

If you place a carrier mid-run, the simulator puts it in the start
arrangement at the position from which it runs exactly to this spot. If
that is not possible without a collision, it reports *No carrier can be
placed here at …*; then place it at the start or on another position.

## Controls in detail { #bedienelemente-im-detail }

### "Carriers" group { #gruppe-kloppel }

| Element | Effect |
|---|---|
| **Color for new carriers** | Button showing the current placement color. A click opens the selection: **Standard colors** from the [color library](../master-data/colors.md), **Recently used** and **Choose custom color…**. New carriers always get the selected color; the default is blue. Carriers without a color of their own from configurations and older setups keep their automatically assigned colors. |
| **Select all carriers** | Selects all carriers so that you can change ply count, arrangement or color together (in the machine also ++ctrl+a++). |
| **Remove all carriers** | After a confirmation prompt, takes all carriers off the machine. A saved setup is kept; the **Setup** list then no longer shows a setup. |

### "Yarn" group { #garn }

| Field | Meaning |
|---|---|
| **Material diameter** | Diameter of **one** yarn in mm (as in the [calculation](../calculations/material/material-diameter.md)), 0.05 to 50 mm. With a ply count above 1, the ribbon of a carrier is that many yarns wide. The value gives the 3D preview its scale: without a core, the braid pulls together down to the set covering, and its diameter follows from the yarn. With a core, core and yarn determine how densely the threads cover the core. It is the same value as in the [take-up](views.md#abzug). **✕** clears the setup's value; then the value of an older program or this PC's default applies. |
| **Covering** | How densely the material covers the braid, calculated as in the calculation [Covering](../calculations/tubular-braid/tube-cover.md) (for a flat braid, the filling grade), 30 to 100 % in steps of 5. 100 % means pulled tight as on the machine. Less keeps the braid wider with the same material; diameter, lay length and take-up follow from it. |

Material diameter and covering belong to the **setup**, like color and
ply count, and are saved with it. The program stays unchanged; only for
your own program with a take-up does the simulator recalculate the m/min.

The covering can only be set **without a core**:

* **With a core**, it follows from core, yarn and braiding angle; the
  field only shows it.
* A **spiral** and compact cross-sections such as **packing** are always
  full; the field is at 100 % and locked.

If the preview cannot draw this little covering at a very flat angle, it
reports *At …° the preview cannot draw this little covering: … % is set,
the picture shows … %. The take-up calculates with … %.*

### Tube threads { #rohrfaden }

If the machine has tubes, the **Yarn** group shows the note *Tubes: a
click on a tube threads the yarn; color and core diameter then appear in
the card at the top.*

| Tube | Thread |
|---|---|
| **Guide tube** (at the gear center) | Axial thread |
| **Axial thread tube** (between gears) | Axial thread |
| **Central tube** (machine center) | Core |

A click on an empty tube threads the yarn in (*Guide tube Z3: Axial
thread threaded in.*). A click on a tube that already has a thread only
selects it. You remove the thread and set its color and the core diameter
in the [selection card](#rohr). The tube threads belong to the setup.

### "Setup" group { #gruppe-besetzung }

**Save as new setup…** creates the current arrangement as a new setup
(the same as in the **⋯** menu next to **Setup**). The note below it
reminds you: *“Save” at the top writes changes back to the selected
setup.*

## Selection card: carrier and tube { #auswahlkarte-kloppel }

### A single carrier { #ein-kloppel }

The card is titled *Carrier n selected*, or for an empty position *Gear n
· position m selected*, and shows *Occupied by carrier n · 2 yarns.* or
*Empty.*

| Field | Meaning |
|---|---|
| **Ply count** | Number of yarns run in parallel on this carrier, 1 to 12. |
| **Arrangement** | **Compactly packed** keeps the combined thread roughly round. **Flat side by side** lays all yarns side by side and makes the combined thread wider and thinner. |
| **Individual colors** | Button *1 color…* or *n colors…*: opens **Individual colors of the plying** with one color per yarn. You also change the color of a carrier with ply count 1 here. |
| **Number** | The carrier number. New carriers automatically get the lowest free number (*Assign automatically*); you can overwrite it. If another carrier already has the number, the program offers to swap the numbers (**Swap numbers**). Each number exists only once. |
| **Remove carrier** / **Place carrier** | Removes the carrier or places one on the empty position. |

### Several carriers { #mehrere-kloppel }

With *n carriers selected*, changes apply immediately to the whole
selection. The card shows differing initial values as *— different —*.

| Element | Effect |
|---|---|
| **Ply count**, **Arrangement** | For all selected carriers. |
| **Color…** | One color for all selected carriers; with a ply count above 1, for all yarns. |
| **Color by running direction** | The clockwise carriers get one color, the counterclockwise carriers the other, red and yellow by default. |

### Tube { #rohr }

The card names the tube type and identifier (for example *Guide tube
Z3*), its position and its dimensions.

| Element | Effect |
|---|---|
| **Axial thread threaded in** or **Core threaded in** | Ticked: the thread is threaded in. Without the tick, it is removed. |
| **Color…** | Color of the thread (only when threaded in). |
| **Core diameter** | Only on the central tube: diameter of the core. In the 3D preview it determines the braid diameter; the braid lies on it. **Fill the bore** uses the diameter of the bore. |

## Configurations and your own setups { #konfigurationen-und-eigene-besetzungen }

* Herzog supplies **configurations** with the model. They contain only
  positions and carrier numbers; your colors and your yarn are added.
* If you select a configuration or a setup from Herzog and change it,
  **Save** stores your own copy *&lt;Name&gt; – own*: *Saved as your own
  setup "…" — "…" from Herzog remains unchanged.*
* Setups from Herzog cannot be deleted.

### Save setup { #besetzung-speichern }

**Save as new setup…** opens the **Save setup** dialog:

| Field | Meaning |
|---|---|
| **Name of the setup** | Suggestion *&lt;selected setup&gt; – own* or *Setup n*. If one of your own setups has the same name, the program asks whether to overwrite it. |
| **Load with “…”** | Only when one of your own programs is selected: whoever selects the program gets this setup along with it. |

The setup is saved immediately (*Setup "…" saved (32 carriers).*).
**Delete setup…** in the **⋯** menu deletes one of your own setups after a
confirmation prompt.

## In the web app { #in-der-web-app }

* The **Covering** cannot be set. The **Material diameter** applies per
  browser to all machines and is not saved with the setup.
* **Tube threads** cannot be threaded in by clicking; they only come from
  a saved setup.
* Placing and removing carriers is only possible while the run is
  stopped.
* **Color for new carriers** additionally offers the choice of
  **Palette**, **Color all carriers** and **Open color database**. In the
  card of a carrier, you set the ply count with − and +.

Details: [Braiding Simulator (web app)](../web/braiding-simulator.md).

## Related pages { #verwandte-seiten }

* [The simulator screen](editor.md)
* [Program](program.md) — switching switches and recording programs.
* [3D preview and take-up](views.md) — how colors, ply count and yarn look
  in the braid.
* [Coloring and texturing in the Designer](../designer/painting.md) —
  plying colors in the Designer.
