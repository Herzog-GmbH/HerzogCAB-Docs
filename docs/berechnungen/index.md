# Calculations

The heart of Herzog CAB is the **calculations**. They are organised by
topic and reachable through the navigation tree (*Calculations*) or via
*View > CAB Calculation 2.0*.

## Topic groups

<div class="grid cards" markdown>

- :material-rotate-3d-variant: __[Braid Geometry](flechtgeometrie/index.md)__

    ---
    Braid angle, lay length, picks density

- :material-tune-variant: __[Material](material/index.md)__

    ---
    Linear density, material diameter, core/cover constellations

- :material-cylinder: __[Bobbins](spulen/index.md)__

    ---
    Volume, material length on bobbin, number of winders

- :material-cog-outline: __[Machine](maschine/index.md)__

    ---
    Dimensions, pitch circle, production speed, runtime

- :material-shape-outline: __[Product](produkt/index.md)__

    ---
    Diameter, rope length, rope weight

- :material-hexagon-outline: __[Tubular Braid](rohrgeflecht/index.md)__

    ---
    Tube carriers, tube covering, yarn width

- :material-star-four-points-outline: __[Advanced](spezial/index.md)__

    ---
    Horn gear layout, carriers rules, braid mapping

</div>

## Operating a calculation

All calculations follow the same scheme:

> :material-image-area: *Screenshot: Example calculation with labelled areas*

| Area             | Contents                                                 |
|------------------|----------------------------------------------------------|
| **Inputs**       | Fields for input quantities (highlighted yellow).        |
| **Picker**       | Optionally pick material / bobbin / machine from master data. |
| **Result**       | Output values (grey background). Several at once.        |
| **Actions**      | Print, attach to job, reset values.                      |

!!! tip "Solve calculations backwards"
    Many calculations can be inverted. Example: you know the production
    speed and want to find the required RPM - enter the speed, leave
    the RPM field empty. Herzog CAB calculates the other way around
    automatically.

## Values are kept

Entered values are kept while the program runs. Switch to a different
calculation and come back later - your inputs are still there. After a
restart, values are reset.

## Attach to a job

If you do a calculation as part of a [job](../auftraege/index.md),
you can use **Attach to job** to link the result with the job. This
keeps a traceable calculation trail.
