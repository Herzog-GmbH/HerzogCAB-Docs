# Bobbins

The bobbin editor is where you maintain the bobbin types used on your
machines. Based on bobbin properties (volume, stroke, flange diameter)
Herzog CAB calculates material lengths, runtimes and change intervals.

> :material-image-area: *Screenshot: Bobbin editor*

## Bobbin properties

> :material-alert-circle-outline: **TODO** *Validate fields against the editor. From code:*

| Field                 | Description                                               |
|-----------------------|-----------------------------------------------------------|
| Name                  | Bobbin name                                               |
| Outer diameter        | in mm                                                     |
| Inner diameter        | in mm                                                     |
| Flange width          | in mm                                                     |
| Winding volume        | calculated from dimensions                                |
| Note                  | Free text                                                 |

## Use

Bobbins are used in:

* [Bobbin volume](../calculations/bobbins/bobbin-volume.md)
* [Material length on bobbin](../calculations/bobbins/material-length.md)
* [Runtime and bobbin set](../calculations/machine/run-time-bobbin-set.md)
