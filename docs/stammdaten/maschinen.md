# Machines

The machines module is where you maintain the braiding machines in your
plant. Per machine, Herzog CAB stores technical data, optionally
documents (data sheets, manuals) and a QR code for use at the machine
itself.

> :material-image-area: *Screenshot: My Machines overview*

## Machine properties

> :material-alert-circle-outline: **TODO** *Validate fields against the editor.*

| Field               | Description                                                 |
|---------------------|-------------------------------------------------------------|
| Name                | Unique name (e.g. "Hall 2 - HM48")                          |
| Manufacturer        | e.g. Herzog GmbH                                            |
| Model               | Model designation                                           |
| Number of carriers  | Number of bobbin carriers (carriers / klueppel)             |
| Pitch circle dia.   | in mm                                                       |
| Maximum speed       | in rpm                                                      |
| Note                | Free text                                                   |

## Machine fleet

The **Machine Fleet** list shows all registered machines. Click an entry
to open details and machine-specific calculations.

## Machine documents

Per machine you can store documents (e.g. PDF manuals, maintenance
plans). Files are kept under

```
<Workspace>\Machines\<MachineID>\documents\
```

> :material-image-area: *Screenshot: Machine detail page with documents*
