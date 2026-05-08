# File Locations

## Workspace (chosen by user)

```
<Workspace>\
├── customers.json           Customers
├── machines.json            Machines
├── colors.json              Colors
├── jobs.json                Jobs
├── products.json            Products
├── materials.json           (legacy) material list
├── bobbins.json             (legacy) bobbin list
├── Materials\               material library (detail)
├── Machines\<MachineID>\documents\
├── Printouts\
│   ├── templates\           print templates (one .json per template)
│   └── assets\              images / logos for templates
└── auth\
    └── assignments.json     user-role assignments
```

## Machine-wide (ProgramData)

```
%ProgramData%\Herzog GmbH\Herzog Cab\
├── users.json               all user accounts
├── profiles.json            all profiles (workspace links)
├── storage.json             storage metadata
└── auth\
    └── avatars\             profile pictures
```

## User registry

Window sizes, column widths and last UI state are kept in the Windows registry under

```
HKEY_CURRENT_USER\Software\Herzog GmbH\Herzog Cab
```

