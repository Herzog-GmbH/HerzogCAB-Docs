# Signing in and out

!!! abstract "Reference — The sign-in window of the desktop app: account users, local sign-in, Microsoft sign-in, account lockout and profile selection."

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

Herzog CAB requires you to **sign in** before the workspace opens. This
makes it traceable who edits which data, and the
[roles and permissions](roles.md) apply per user. After
signing in, you select the [profile](profiles.md) (the workspace) you
want to work with.

Which sign-in window you see depends on the licensing method:

| Licensing method | Sign-in window | Users come from … |
|---|---|---|
| **Customer account** (normal case since 2.0) | **Herzog CAB – Sign in** with email address, password and, if applicable, code | the [customer account](../setup/account.md) — the same credentials as in the licence portal and in the web app. |
| **Dongle / CmAct licence** | **Herzog CAB – Sign in** with login and password, if applicable **Sign in with Microsoft** | the local [user management](users.md), Microsoft Entra ID or LDAP. |

!!! info "First sign-in"
    With the customer account, the user who signed the computer in is immediately
    signed in to the program — see
    [Signing in and obtaining a licence](../setup/activate-license.md). With a
    dongle installation, you first create an administrator account at the first program start
    — see
    [First start and setup](../setup/first-run.md).

---

## Signing in with the account user { #anmeldung-mit-dem-kontobenutzer }

At startup, the **Herzog CAB – Sign in** window appears (or **Herzog
CAB – Sign in to your customer account** if the computer is not yet signed in to the account,
see [Signing in and obtaining a licence](../setup/activate-license.md)).
At the top there is a blue **header band** with the lettering *Herzog CAB* and
below it the name of your account (*Account: &lt;Company&gt;*); on its right runs
a small animated **braid** made of three threads. It shows the state of the
dialog: calm while you type, fast while Herzog CAB checks the
sign-in, and almost still after a successful sign-in.

Below are the fields, each with its label above it. If the
dialog appears because a saved sign-in is no longer valid, a
light-blue note at the very top explains this (*"Your saved sign-in is no longer valid
(expired, signed out or password changed). Please sign in
again."*).

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Anmeldefenster „Herzog CAB – Anmelden“ im Kontomodell: blaues Kopfband mit „Herzog CAB“, „Konto: &lt;Firma&gt;“ und dem Zopf rechts; Felder E-Mail-Adresse und Passwort mit Beschriftung darüber, Häkchen „Angemeldet bleiben“, Link „Passwort vergessen?“, Schaltflächen Anmelden und Beenden.
    **So erzeugen:** Kunden-Build auf einem am Konto angemeldeten Rechner starten, nachdem der Benutzer sich im Programm abgemeldet hat (sonst startet es dank „Angemeldet bleiben“ ohne Dialog). Musterkonto, keine echte E-Mail-Adresse.
    **Ziel-Datei:** `assets/screenshots/admin/anmelden-konto.png`

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Derselbe Dialog im Schritt „Zweiter Faktor“: Kopfband-Unterzeile „Zweiter Faktor“, grüner Haken im Passwortfeld, darunter „Code aus der Authenticator-App“ mit sechs Kästchen in zwei Dreiergruppen (drei Ziffern eingetippt), graue Meldung zur Zwei-Faktor-Anmeldung, Schaltfläche „Bestätigen“.
    **So erzeugen:** Mit einem Testbenutzer anmelden, für den im Lizenzportal der zweite Faktor eingerichtet ist; nach **Anmelden** drei Ziffern eintippen und aufnehmen.
    **Ziel-Datei:** `assets/screenshots/admin/anmelden-konto-code.png`

### Controls { #bedienelemente }

| Element | Description |
|---|---|
| **Email address** | Your login name in the customer account. Herzog CAB pre-fills the user last signed in on this computer, or the first time the user who signed the computer in. Clicking into the field selects its content so that you can overwrite it directly. |
| **Password** | Your account password (hidden input). Press ++enter++ to sign in directly. If the password is correct and only the code is still missing, a green check mark appears in the field. |
| **Code from the authenticator app** | Only expands if the [second factor](../portal/security.md) is set up for your user — after the first click on **Sign in**. The code goes into **six boxes** (two groups of three). Only digits are accepted; a pasted code such as "123 456" is taken over without the space. **After the sixth digit, Herzog CAB checks the code by itself**; clicking **Confirm** is not necessary. The code changes every 30 seconds. |
| **Stay signed in** | On by default: Herzog CAB starts on this computer without a new sign-in until you sign out in the program, change your password or do not work with it for 30 days. Applies only to your Windows user — switch it off on computers where several people work with the same Windows user. |
| **Forgot your password?** | Opens the page of the [licence portal](../portal/index.md) in the browser that sends a link for setting a new password; the email address is already entered there. |
| **Sign in** / **Confirm** | Checks the credentials against the licence server and, if successful, opens the profile selection. During the check, the button shows a spinner and *Checking …*; in the code step it is called **Confirm**. On success, a check mark with *Signed in* appears briefly, then the dialog closes. |
| **Quit** | Quits Herzog CAB (locked during the check). |

!!! tip "Errors at a glance"
    If an entry is missing, the field gets a red border and shakes briefly;
    the border disappears as soon as you continue typing. A wrong code turns
    the boxes red, clears them and makes them shake. If the sign-in
    itself fails, the password field shakes and the message appears in red below
    the fields.

### Roles and permissions { #rollen-und-rechte }

Your role in the program corresponds to your role in the customer account:
**Administrator** = global administrator with all permissions in all
profiles, **Editor** and **Viewer** = the standard roles of the same name.
If an administrator changes your role in the licence portal, this applies
from the next online sign-in. Which profiles you see is still
determined by the local [user management](users.md).

### Signing in without internet { #anmelden-ohne-internet }

If the licence server cannot be reached, Herzog CAB still allows the sign-in
— for users who have **already signed in online on this
computer**, with the password from that time. After signing in,
the note *"The licence server cannot be reached. You are signed in with
the last known roles …"* appears. Changes to users and
roles in the account only arrive at the next online start.

### Messages of the sign-in window (account users) { #meldungen-des-anmeldefensters-kontobenutzer }

| Message | Meaning |
|---|---|
| *E-mail address or password is not correct.* | Check your credentials; you reset the password via **Forgot password** in the [licence portal](../portal/index.md). |
| *Two-factor sign-in is set up for this user. Please enter the current code …* | Not an error — enter the code from the authenticator app. |
| *The code is not correct.* | Check the time on your phone and wait for the next code. |
| *Please enter your user's e-mail address.* / *Please enter the password.* / *Please enter the code from the authenticator app.* | A field is empty or the code is incomplete. |
| *This user is deactivated.* | An administrator has deactivated the user in the licence portal. |
| *Too many failed attempts. Please try again later.* | The licence server slows down after several failed attempts — wait a few minutes. |
| *The licence server cannot be reached (…). Only users who have already signed in online on this computer can sign in offline …* | Check the connection — or use a user who has already been online here. |
| *Signing in to the customer account succeeded, but the user could not be signed in to the program …* | Rare; usually the local user file is not writable — see [Login problems](../help/login-problems.md). |

---

## Signing in with dongle installations { #anmeldung-bei-dongle-installationen }

At startup, the **Herzog CAB – Sign in** window appears with the
HERZOG logo, the input fields and — if set up — the
Microsoft button.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Anmeldefenster „Herzog CAB – Anmelden" mit Logo, Feldern Login/Passwort und der Schaltfläche „Mit Microsoft anmelden"
    **So erzeugen:** Herzog CAB mit Dongle starten (Entra-Anmeldung muss unter *Systemverwaltung > Authentifizierung* aktiviert sein, sonst fehlt die Microsoft-Schaltfläche)
    **Ziel-Datei:** `assets/screenshots/admin/anmelden.png`

### Login and password { #login-und-passwort }

| Element | Description |
|---|---|
| **Login** | Your login name. Herzog CAB automatically pre-fills the login name last used by this Windows user; the cursor is then already in the password field. |
| **Password** | Your password (hidden input). Press ++enter++ to sign in directly. |
| **Sign in** | Checks the entries and, if successful, opens the profile selection. |
| **Cancel** | Ends the sign-in process. |

Both **local accounts** and **LDAP / Active Directory accounts** sign in
via the Login/Password fields — for the latter, Herzog CAB checks the
password directly against the domain controller in the company network (no browser
required, works offline in the LAN).

### Sign in with Microsoft { #mit-microsoft-anmelden }

The **Sign in with Microsoft** button only appears if an
administrator has set up and enabled Microsoft sign-in under
[*System administration > Authentication*](authentication.md). This is how
the sign-in works:

1. Click **Sign in with Microsoft**. The sign-in window shows
   the note *"Browser opened — please sign in in the Microsoft window…"*;
   the button is locked in the meantime.
2. Herzog CAB opens its **own small browser window** (without tabs and
   address bar, centred on the screen) with the familiar
   Microsoft sign-in page. Sign in there with your Microsoft account.
3. After a successful sign-in, the window briefly shows *"Sign-in
   successful"* and **closes automatically**. Herzog CAB immediately continues
   with the profile selection.

!!! info "Your Microsoft password stays with Microsoft"
    The Microsoft password is **never** entered or stored in Herzog CAB
    — the entire sign-in takes place in the Microsoft window.

!!! tip "Window does not close automatically?"
    Herzog CAB uses its own sign-in window if your default browser is
    based on Chromium (e.g. Microsoft Edge, Google Chrome). With other
    browsers, the Microsoft sign-in opens as a normal browser tab —
    the sign-in works the same way, you just close the tab yourself
    afterwards.

If the Microsoft sign-in is cancelled or takes too long, the
sign-in window shows a message (e.g. *"Timed out during
Microsoft sign-in."*) and you can try again.

### Account lockout after failed attempts { #kontosperre-bei-fehlversuchen }

After **five** failed sign-in attempts in quick succession, the
sign-in for this account is temporarily locked (*"Too many failed attempts.
Please try again later."*). This protects against systematic
trial of passwords. Wait about one minute and try
again — the lock releases by itself. If the password has really been
forgotten, an administrator can
[reset](users.md#passwort-zurucksetzen) it.

### Messages of the sign-in window (local accounts) { #meldungen-des-anmeldefensters-lokale-konten }

| Message | Meaning |
|---|---|
| *Login or password is incorrect.* | Login name unknown or password wrong. |
| *This account is deactivated.* | The account has been deactivated in the [user management](users.md). |
| *Too many failed attempts. Please try again later.* | Account lockout, see above. |
| *This account signs in through a different provider.* | For this account, Microsoft sign-in is intended, for example — use **Sign in with Microsoft** instead of the password field. |
| *Microsoft sign-in is not configured.* | The setup under [Authentication](authentication.md) is incomplete — contact your administrator. |

---

## Profile selection after signing in { #profil-auswahl-nach-der-anmeldung }

Directly after a successful sign-in, the **Select profile** dialog asks
which workspace should be opened — provided you have been assigned more than one
profile. **Open profile** starts the selected
profile; **Manage profiles …** takes you to the [profile management](profiles.md).
If exactly one profile is assigned, Herzog CAB opens it without asking.

## Signing out and switching profiles { #abmelden-und-profil-wechseln }

* **Sign out:** At the bottom left of the navigation bar, click your
  name or profile picture and, in the
  [My profile](my-profile.md) dialog, choose the **Sign out** button. This only signs
  out the **user** — the computer remains signed in to the customer account and
  keeps its seats. You sign out the computer itself under
  [*Settings > Licence*](settings/license.md).
* **Switch profile:** happens via a program restart so that no
  unsaved entries are lost — see
  [Profiles (workspaces)](profiles.md#profil-wechseln).

## Related pages { #verwandte-seiten }

* [Signing in and obtaining a licence](../setup/activate-license.md) — signing the computer in to the customer account
* [Password, second factor and name](../portal/security.md) — changing the password, authenticator app
* [Users](users.md) — creating accounts or taking them over from the customer account
* [Authentication](authentication.md) — setting up Microsoft Entra ID and LDAP (dongle installations)
* [My profile](my-profile.md) — your own account and signing out
* [Problems signing in](../help/login-problems.md)
