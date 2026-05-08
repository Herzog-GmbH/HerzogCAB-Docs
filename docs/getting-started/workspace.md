# Set Up a Workspace

A **workspace** is the central data folder for Herzog CAB. It holds your
master data, jobs, print templates and custom profiles.

## What goes into a workspace?

The workspace folder contains:

```
<Workspace>\
├── customers.json           Customers
├── machines.json            Machines
├── colors.json              Colors
├── jobs.json                Jobs
├── products.json            Products
├── Materials\               Material library
├── Printouts\
│   ├── templates\           Print templates (one file per template)
│   └── assets\              Images/logos for print templates
└── auth\
    └── assignments.json     Who-may-do-what assignments
```

!!! info "What is NOT in the workspace?"
    User accounts and passwords do **not** live in the workspace. They
    are stored machine-wide under
    `C:\ProgramData\Herzog GmbH\Herzog Cab`. This way users can sign in
    with their personal accounts to different workspaces on the same
    machine without having to be re-created.

## Where should the workspace live?

| Scenario                                       | Recommendation                       |
|------------------------------------------------|--------------------------------------|
| You work alone on one machine                  | Local, e.g. `C:\HerzogCAB\Workspace` |
| Multiple operators on the same machine         | Local - separated by login           |
| Multiple machines should share the same data   | Network drive (SMB share)            |

!!! warning "Network drive notes"
    If the workspace lives on a network drive:

    - Make sure all operators have write access.
    - Avoid editing the same job from two machines at once - changes
      could be lost.
    - A stable connection matters - data can be corrupted if the
      connection drops.

## Create the workspace on first start

After installation, the **workspace setup dialog** opens on first start.

> :material-image-area: *Screenshot: Workspace setup dialog*

1. Click **Browse** and select a folder.
2. Optional: enter a **profile name** (e.g. "Plant - Hall 2") if you
   plan to use multiple workspaces.
3. Confirm with **Next**.

The folder structure is created automatically.

## Switch the workspace later

You can change the workspace at any time:

* *Tools > Manage profile* (alternatively click the profile name at the
  top of the application).
* Choose an existing profile or create a new one.
* The program restarts; the chosen profile is then active.

More: [Switch profile](../workspace/switch-profile.md).
