# Set up users and roles

!!! example "Guide — at the end, your employees can sign in with their own accounts and see exactly the areas that their roles allow"

**Prerequisites:**

* You are signed in with an administrator account (the
  **System administration** category is only visible with the corresponding permissions).
* In the account model: you are an **administrator of the customer account** in the
  [licence portal](../portal/index.md).
* For connecting to Microsoft Entra ID or LDAP/Active Directory
  (dongle installations only): the access data from your IT department (e.g. tenant and
  client ID or LDAP URL and bind account) is at hand.

=== "Customer account (standard case since 2.0)"

    ```mermaid
    flowchart LR
      A["Invite user in the licence portal"] --> B["Define role in the account"]
      B --> C["Desktop: assign profiles<br>Web: tick web roles"]
      C --> D["Test sign-in"]
    ```

    1. **Invite:** In the licence portal under **Users**, enter the e-mail address,
       choose a role (Administrator, Editor, Viewer) and
       click **Invite** — see
       [Invite and manage users](../portal/users.md). The person
       sets their own password via the link.
    2. **Desktop app:** Under *System administration > Users*, click **Refresh
       from customer account** (or wait for the user's next start) and assign the
       workspaces in the **Profiles and roles** area — see [Users](../admin/users.md). The
       role itself comes from the account; you can additionally assign your own roles from
       *System administration > Roles* per profile.
    3. **Web app:** Under *User menu > Account and users*, tick the
       web roles — see [Account and users](../web/account.md);
       you create your own web roles under [Roles](../web/roles.md).
    4. **Test:** The person signs in to the desktop app (e-mail and
       password) or to the web app and sees the areas of their role.

    The steps below apply to **dongle installations** with local
    user management.

=== "Dongle installation (local users)"

    ```mermaid
    flowchart LR
      A["Check/create roles"] --> B["Create or import users"]
      B --> C["Assign profiles & roles"]
      C --> D["Test sign-in"]
    ```

## Step 1: Check or create roles { #schritt-1-rollen-prufen-oder-anlegen }

1. Open *System administration > Roles* (reference:
   [Roles and permissions](../admin/roles.md)).
2. Check whether the existing default roles are sufficient for your division of
   work.
3. If not, click **New role**, enter a name and
   description and select the individual permissions — or activate
   **All permissions (Administrator)** for a full-access role.

A role is a reusable set of permissions; each user can be given one
or more roles.

## Step 2: Create or import users { #schritt-2-benutzer-anlegen-oder-importieren }

Depending on how your employees are to sign in:

=== "Local users"

    1. Open *System administration > Users* (reference:
       [Users](../admin/users.md)).
    2. Click **New user** and enter the login,
       display name, e-mail and an initial password.
    3. Create the account and then assign it the roles from step 1 in the
       **Profiles and roles** area.

=== "Microsoft Entra ID"

    1. First configure the sign-in under
       *System administration > Authentication*, **Microsoft Entra ID** tab:
       activate it, enter the tenant and client ID and, in the
       **Entra group → role** table, define which Entra group receives which
       Herzog CAB role (reference:
       [Authentication](../admin/authentication.md)).
    2. Save the configuration.
    3. Import the users under *System administration > Users* via
       **Import from Entra** — or leave this to the automatic
       account creation at first sign-in, if you have activated it in the
       configuration.

=== "LDAP / Active Directory"

    1. Configure the sign-in under
       *System administration > Authentication*, tab
       **LDAP / Active Directory**: activate it, enter the LDAP URL, bind account,
       base DN and search filter (reference:
       [Authentication](../admin/authentication.md)).
    2. Save the configuration.
    3. Import the users under *System administration > Users* via
       **Import from LDAP**.

All fields of user management — including deactivating, permanently
deleting and **Reset password** — are explained on the reference page
[Users](../admin/users.md).

## Step 3: Assign profiles and roles { #schritt-3-profile-und-rollen-zuordnen }

Open each user and check in the **Profiles and roles** area:

* **Roles** — determine what the user is allowed to do. For imported
  Entra users, roles are assigned via the group mapping from step 2.
* **Profiles** — determine which workspaces the user is allowed to work
  with (reference: [Profiles](../admin/profiles.md)).

## Step 4: Test sign-in { #schritt-4-anmeldung-testen }

1. Sign out and sign in again with the new account (reference:
   [Sign in and sign out](../admin/login.md)):
    * Local users: enter login and password, **Sign in**.
    * Entra users: click **Sign in with Microsoft** and complete the
      Microsoft sign-in.
    * LDAP users: enter the domain login and domain password in the normal
      sign-in fields, **Sign in**.
2. Check whether the navigation only shows the areas that the user's roles
   allow — entries without permission are hidden or
   locked.

## Result { #ergebnis }

* The roles reflect your division of work.
* Each employee has their own account (local or imported from Entra/LDAP)
  with assigned roles and profiles.
* Sign-in has been successfully tested with at least one new account.

## If something does not work { #wenn-etwas-nicht-klappt }

* Sign-in fails, account locked or "Sign in with Microsoft"
  aborts → [Login problems](../help/login-problems.md)
* Import finds no users → check the configuration in the respective tab,
  see [Authentication](../admin/authentication.md)
* A user sees too much or too little → check the role assignment, see
  [Roles and permissions](../admin/roles.md) and
  [Users](../admin/users.md)
* Further help → [Help overview](../help/index.md) and
  [Contact support](../help/support.md)
