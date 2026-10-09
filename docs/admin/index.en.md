# Administration

!!! abstract "Reference — Overview: customer account and licence portal, system administration of the desktop app, Settings dialog"

Since version 2.0, the administration of Herzog CAB is split between two places:

* The **customer account** in the [licence portal](../portal/index.md) — modules,
  seats, computers, users and passwords. It applies to the desktop app
  **and** the web app and is maintained in the browser.
* The **System administration** of the desktop app (bottom section of the left
  navigation) — role assignment per workspace, profiles, storage location
  and company master data; for dongle installations also the local
  user accounts and sign-in via Microsoft or the company network. In addition,
  there is the Settings dialog under *File > Settings* with language,
  appearance, Designer defaults, licence, cloud and web server.

The administration of the **web app** (company, media, roles, import) is located in
its user menu — see [Web app](../web/index.md).

<div class="grid cards" markdown>

- :material-account-key-outline: **Customer account and licence portal**

    Modules and seats, signed-in computers, inviting users, requesting
    licences, password, second factor and name.

    [:octicons-arrow-right-24: Licence portal](../portal/index.md)

- :material-cog-outline: **Licence and cloud (Settings)**

    Licence status in the desktop app, offline lease, signing out and the
    cloud upload of the workspace folder to the web app.

    [:octicons-arrow-right-24: Licence and cloud](settings/license.md)

</div>

## System administration of the desktop app { #systemverwaltung-der-desktop-app }

!!! info "Visibility depends on your permissions"
    The **System administration** group only appears in the navigation if your
    user account has at least one of the administration permissions. Even
    within the group, you only see the entries you are authorized
    for — a user with the *Manage company data* permission, for example, only sees
    **Company**, but not **Users** or **Roles**. The available permissions are
    explained in [Roles and permissions](roles.md).

| Entry in the navigation | Required permission |
|---|---|
| **Users** | Manage users |
| **Roles** | Manage roles |
| **Profiles** | Workspace settings |
| **Storage location** | Workspace settings |
| **Company** | Manage company data |
| **Authentication** | Manage users |

## The areas at a glance { #die-bereiche-im-uberblick }

<div class="grid cards" markdown>

- :material-login: **Signing in and out**

    The sign-in window: account users, local account, **Sign in with
    Microsoft**, account lockout and profile selection after login.

    [:octicons-arrow-right-24: Continue](login.md)

- :material-account-multiple: **Users**

    Take over users from the customer account and assign them to workspaces;
    for dongle installations, create local accounts, import from Microsoft Entra
    or LDAP and reset passwords.

    [:octicons-arrow-right-24: Continue](users.md)

- :material-shield-account: **Roles and permissions**

    The permission system: supplied standard roles, individual permissions and custom
    roles.

    [:octicons-arrow-right-24: Continue](roles.md)

- :material-key-chain: **Authentication**

    Dongle installations only: set up sign-in via Microsoft Entra ID or
    LDAP / Active Directory — with group-to-role mapping.

    [:octicons-arrow-right-24: Continue](authentication.md)

- :material-account-circle: **My profile**

    Your own account: profile picture, display name, email, changing your password and
    signing out.

    [:octicons-arrow-right-24: Continue](my-profile.md)

- :material-briefcase-outline: **Profiles (workspaces)**

    Run several clients or test/production environments, define the
    workspace folder, switch profiles.

    [:octicons-arrow-right-24: Continue](profiles.md)

- :material-database-marker: **Storage location**

    Where are the central user data and the active workspace stored?
    Locally or on the network drive — this is where you see and change it.

    [:octicons-arrow-right-24: Continue](storage-location.md)

- :material-domain: **Company**

    Maintain company master data and logo for letterhead and print templates.

    [:octicons-arrow-right-24: Continue](company.md)

- :material-cog-outline: **Settings (dialog)**

    The dialog under *File > Settings*: language, font size, design,
    privacy, storage locations, Designer defaults, legacy data import, licence
    and cloud, web server.

    [:octicons-arrow-right-24: Continue](settings/index.md)

</div>

## Typical tasks { #typische-aufgaben }

* [Setting up users and roles](../tasks/setup-users.md) — the complete
  procedure "Setting up users and permissions for a plant", for the account model and
  dongle installations.
* [Bringing data from the desktop to the web app](../tasks/desktop-to-web.md) —
  cloud upload or ZIP import.
