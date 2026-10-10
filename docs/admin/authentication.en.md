# Authentication

!!! abstract "Reference — Setting up sign-in via Microsoft Entra ID or LDAP / Active Directory, including group-to-role mapping."

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

!!! info "Dongle installations only"
    Microsoft Entra ID and LDAP complement the **local** user management
    of the desktop app. If Herzog CAB obtains its licence from the
    [customer account](../setup/account.md), users and passwords come from
    the account and this area has no effect; the web app knows
    account users only.

Under *System administration > Authentication* you connect Herzog CAB to your
company's user directory. Afterwards, in addition to the local accounts,
employees can sign in

* with their **Microsoft account** (button
  [**Sign in with Microsoft**](login.md#mit-microsoft-anmelden) in the
  sign-in window), or
* with their **Windows domain account** via LDAP / Active Directory — directly in
  the company network, even without internet.

Local Herzog CAB accounts (user name + password) continue to work independently
of this, also offline.

!!! warning "Permission required"
    Only users with the **Manage users** permission can see and use
    this area.

!!! info "Prerequisite for Microsoft Entra ID"
    Before you can enter values here, your company's IT administration
    must create an **app registration** once in its own
    Microsoft Entra directory (takes about 10 minutes). You receive the
    step-by-step instructions for this from your
    Herzog contact person. Herzog does not get any access to your
    directory; a client secret or certificate is **not** required.

## The screen at a glance { #der-bildschirm-im-uberblick }

The **AUTHENTICATION** screen has two tabs — **Microsoft Entra ID**
and **LDAP / Active Directory**. Below the tabs there is a shared
error line and the **Save** button, which stores the settings of both
tabs.

!!! warning "📷 Screenshot missing"
    **Subject:** “Authentication” screen, “Microsoft Entra ID” tab with the configuration fields and the “Entra group → role” table
    **How to create:** Open *System administration > Authentication* (Microsoft Entra ID tab active); use sample data without real tenant/client IDs
    **Target file:** `assets/screenshots/admin/authentifizierung-entra.png`

!!! warning "📷 Screenshot missing"
    **Subject:** “Authentication” screen, “LDAP / Active Directory” tab with all connection fields and the “Test connection” button
    **How to create:** Open *System administration > Authentication*, select the “LDAP / Active Directory” tab; use sample data (example.local)
    **Target file:** `assets/screenshots/admin/authentifizierung-ldap.png`

## "Microsoft Entra ID" tab { #reiter-microsoft-entra-id }

As long as **Enable sign-in with Microsoft Entra ID** is not checked,
all other fields of the tab are locked.

### Connection details { #verbindungsdaten }

| Field | Meaning |
|---|---|
| **Enable sign-in with Microsoft Entra ID** | Enables Microsoft sign-in. Only then does the **Sign in with Microsoft** button appear in the sign-in window. |
| **Directory (tenant)** | Your Microsoft directory: either the keyword `organizations` (default) or the specific **Directory (tenant) ID** from the app registration. |
| **Client ID** | The **Application (client) ID** of the Herzog CAB app registered in your directory. Mandatory field — without a client ID, the enabled Entra sign-in cannot be saved. |
| **Redirect port (loopback)** | Port through which the response of the Microsoft sign-in arrives on this computer. Recommendation: **automatic** (value 0) — Herzog CAB then chooses a free port itself. |
| **Login name from** | Defines which directory entry becomes the Herzog CAB login name: **User principal name (userPrincipalName)** (normal case), **Email (mail)** or **Local logon name (onPremisesSamAccountName)**. |
| **Create account automatically on first login (JIT)** | If checked, Herzog CAB automatically creates a matching user account at the first successful Microsoft login — you do not have to import anyone in advance. If unchecked, only existing or [imported](users.md#benutzer-aus-microsoft-entra-importieren) accounts can sign in. |
| **Default profile** | Optional: profile (workspace) to which Microsoft sign-ins are assigned automatically. *— no automatic assignment —* leaves the assignment to the administrator. |
| **Import only from group** | Optional, recommended: object ID of a directory group. The [user import](users.md#benutzer-aus-microsoft-entra-importieren) then only shows its members instead of all directory users. **Search…** opens the *Select Entra group* dialog so that you can conveniently find the group by name instead of entering the ID by hand; *Selected: &lt;group name&gt;* then appears below the field. Empty = all users can be imported. |

### "Entra group → role" table { #tabelle-entra-gruppe-rolle }

Members of an Entra security group automatically receive the mapped
[role](roles.md) when they sign in. If no group matches, the
manually assigned roles remain untouched.

| Element | Description |
|---|---|
| Columns **Group / Group ID / Role** | Display name of the group, its object ID in the directory and the Herzog CAB role that members receive. You choose the role per row from a drop-down list. |
| **Select from Entra…** | Opens the *Select Entra group* dialog (search field, columns *Group* and *Description*, **Apply**) and inserts the selected group as a new row. |
| **Add manually** | Inserts an empty row in which you enter the group name and object ID yourself. |
| **Remove** | Deletes the selected row. |

!!! info "Sign-in for the group search"
    For **Search…** and **Select from Entra…**, Herzog CAB signs in to the directory once
    via a Microsoft window to load the group list.

## "LDAP / Active Directory" tab { #reiter-ldap-active-directory }

Sign-in against an in-house domain controller — works offline in the
LAN. Users sign in with name + password in the normal sign-in window
(no browser). As long as **Enable sign-in via LDAP / Active Directory**
is not checked, all other fields are locked.

| Field | Meaning |
|---|---|
| **Enable sign-in via LDAP / Active Directory** | Enables LDAP sign-in. |
| **LDAP URL** | Address of the domain controller, e.g. `ldaps://dc-1.example.local:636`. Mandatory field (together with the base DN). The encrypted variant `ldaps://` is recommended. |
| **Domain name** | Name of your Windows domain, e.g. `example.local`. |
| **Domain prefix** | Prefix before the login name, e.g. `EXAMPLE\`. |
| **Bind account** | Service account that Herzog CAB uses to search the directory (as UPN or DN). |
| **Bind password** | Password of the service account (hidden input). |
| **Base DN (person search)** | Starting point of the user search in the directory tree, e.g. `DC=example,DC=local`. Mandatory field. |
| **Person search filter** | Filter that maps the login name to a directory entry; default: `(&(objectClass=person)(sAMAccountName={user}))` — `{user}` stands for the login name entered. |
| **Login attribute** | Directory attribute that serves as the Herzog CAB login name; default `sAMAccountName` (the Windows logon name). |
| **Base DN (group search)** | Optional separate starting point for the group search — leave empty if groups are in the same branch. |
| **Connection timeout (sec.)** / **Search timeout (sec.)** | Waiting times (1–120 seconds) before a connection or search attempt is aborted. |
| **Do not verify LDAPS certificate (test / self-signed only)** | Skips the certificate check of the encrypted connection. Only for tests or self-signed certificates — leave it off in production. |
| **Test connection** | Tests the connection with the current entries (even before saving). The result appears right next to it: *Connection successful.* or an error message. |

!!! info "Roles and profile for LDAP accounts"
    The **Entra group → role** table and the **Default profile** from the
    Entra tab also apply to LDAP accounts: at every sign-in,
    Herzog CAB reads the group memberships from the directory and
    updates the roles accordingly (the directory takes precedence).
    If no group matches, manually assigned roles are
    retained. If the directory is temporarily unreachable, the
    last saved state applies — sign-in still succeeds.

## Save { #speichern }

**Save** stores both tabs together. Before saving,
Herzog CAB checks the entries:

* If Entra is enabled, a **Client ID** must be entered.
* If LDAP is enabled, **LDAP URL** and **Base DN** must be entered.

Errors appear in the red error line above the button; on success
Herzog CAB reports *"Sign-in settings saved."*

## Related pages { #verwandte-seiten }

* [Signing in and out](login.md) — what Microsoft sign-in looks like for users
* [Users](users.md) — import from Entra or LDAP, maintaining accounts
* [Roles and permissions](roles.md) — which permissions a role bundles
* [Setting up users and roles](../tasks/setup-users.md)
