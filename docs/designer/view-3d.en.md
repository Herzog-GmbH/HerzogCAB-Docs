# Views and 3D view

!!! abstract "Reference — the Designer's view switches: full and half development, the rotatable projections cylinder, square and edge, and the real 3D model of the braid."

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

The normal braid pattern shows the braid as a flat, "cut open"
section. To judge a pattern on the finished product, the Designer offers
further views: the **projections** place the development rotatably
on a cylinder or square, the real **3D model** builds the braid
thread by thread from the carrier tracks of the Occupation Overview — with
crossings, material and covering, freely rotatable. This lets you
judge spirals, rings, transitions and edges realistically before the
design goes to the machine.

## The screen at a glance { #der-bildschirm-im-uberblick }

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Vorschau-Bereich des Designers in der 3D-Ansicht: ein
    zweifarbiges Rundgeflecht als räumliches Modell, darüber die
    Ansichtsleiste (Draufsicht / Seitenansicht / Flechtpunkt + Schloss),
    darunter die Reglerzeile Material / Darstellung / Ausrichtung; in der
    Werkzeugleiste ist **3D** aktiv.
    **So erzeugen:** *Designer* öffnen, Rundgeflecht 24 Klöppel, Linkslauf
    rot und Rechtslauf blau färben, in der Werkzeugleiste **3D** wählen,
    Ansicht *Seitenansicht*.
    **Ziel-Datei:** `assets/screenshots/designer/designer-3d-ansicht.png`

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Dieselbe Vorschau in der Ansicht **Zylinder** (Projektion),
    leicht gedreht, mit den Drehpfeilen.
    **So erzeugen:** wie oben, Ansicht **Zylinder** wählen und einmal drehen.
    **Ziel-Datei:** `assets/screenshots/designer/designer-zylinder-ansicht.png`

## Controls in detail { #bedienelemente-im-detail }

### View switches in the toolbar { #ansichts-schalter-in-der-werkzeugleiste }

The switches form a group — exactly one is active. Which ones appear
depends on the braid type:

| Braid type | Switches |
|---|---|
| **Round braid** | **Full** · **Half** · **Cylinder** · **3D** |
| **Square braid** | **Full** · **Square** · **3D** |
| **Packing braid** | **Full** · **Edge** · **3D** |
| **Lace**, **spiral**, **soutache braid** | **Full** · **3D** |

| Switch | Meaning |
|---|---|
| **Full** | The complete development of the circumference as a flat braid pattern — the default view in which you color. |
| **Half** | Only the front half of the development (round braid). |
| **Cylinder** / **Square** / **Edge** | The development projected onto the cylinder (round) or the square (square, packing). The back is hidden; use the rotation arrows on the preview card to rotate the body step by step. With Square and Edge, the edges are created by light and shading, not by lines. |
| **3D** | The real spatial model of the braid from the carrier tracks of the Occupation Overview — for all six braid types. Mixed designs of round and strand sections have no 3D model; the view then shows a note. |

Colors, ply count and all ongoing changes remain identical in all views
— including [plying colors](painting.md#fachungsfarben-farbe-je-garn):
in the 3D model, each yarn of a carrier runs in its own color.
Coloring by click belongs in the flat braid pattern; in the 3D view you color
via the carrier table or the palette — the model recolors immediately,
without being rebuilt, even with many carriers and a high ply count. The
Designer remembers the selected view (including the rotation angle) per braid
type if the setting *Remember last used view* is active
([Settings > Design](../admin/settings/legacy-import.md)).

### Operating the 3D view { #die-3d-ansicht-bedienen }

At the top of the picture is the **view bar**:

| Element | Effect |
|---|---|
| **Top view** | View of the cross-section, oriented like the machine in the Occupation Overview. |
| **Side view** | The whole braid from the side — the braid pattern. |
| **Braiding point** | Close-up of the point at which the braid is currently being formed; the camera follows the track animation. |
| **Lock** | Locked: mouse and finger do not rotate the braid, the mouse wheel still zooms. Open: the left mouse button rotates, the right one pans, a double-click restores the selected view. |
| **Zoom in** / **Zoom out** (preview card) | Also work in the 3D view; so does the mouse wheel. |

Below the picture is the **slider row**:

| Control | Options | Meaning |
|---|---|---|
| **Material** | *Smooth filament*, *Twisted yarn*, *Wire*, *Light version (simple)* | Fiber structure, roughness and gloss of the threads. The carrier colors are kept in all materials; the light version is for weak graphics cards. |
| **Display** | *Default for the braid type*, *Interlacing only (schematic)*, *Automatic*, *As the machine is arranged*, *Correction: always round*, *Correction: always flat* | How the cross-section is derived: *Interlacing only* shows the thread order and crossings on the normalized cross-section (without horngear positions and horngear sizes); *Automatic* and *As the machine is arranged* derive it from the tracks. The default per braid type is interlacing for round, spiral and soutache, straightened for strand, machine shape for square and packing. |
| **Orientation** | *Top → bottom*, *Bottom → top* | Only rotates the 3D display of the braid — depending on whether you want to view the machine from above or from below. |

The **Covering** from the [measurement row](parameters.md#mazeile-in-der-vorschau)
determines the drawn thread thickness; the **Braiding angle** has a live
effect. If the [track animation](animation.md) is running, the 3D braid grows
in sync — *Back to start* shows the whole braid again. These settings
apply to the Designer as a whole, not per design.

!!! info "Limits of the 3D view"
    * Coloring by click, carrier numbers and textures are only available in
      the flat braid pattern.
    * For square and packing braid, the model shows the tracks of the
      carriers; the packed square cross-section of the finished product
      is only created on the machine.
    * Large machines (from about 100 carriers) need a moment to rebuild after
      a change of the number of carriers or the binding; color changes
      are visible immediately.
    * The view requires OpenGL-capable graphics (see
      [System requirements](../setup/system-requirements.md)).

## Related pages { #verwandte-seiten }

* [Designer overview](index.md) — zooming and panning the preview
* [Braid type and parameters](parameters.md) — choose the braid type, measurement row
* [Coloring and texturing](painting.md) — texture display in the flat braid pattern
* [Setup and track animation](animation.md) — the kinematics behind the 3D model
* [Design (settings)](../admin/settings/legacy-import.md) — remember the view
