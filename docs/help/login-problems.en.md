# Sign-in problems

!!! question "Troubleshooting — Signing in to Herzog CAB fails"

Herzog CAB requires you to sign in before opening the workspace — with
the **account user** (standard case since 2.0), for dongle installations locally
with login and password or via **Microsoft Entra ID**. You will find the basics of
signing in under [Sign in and sign out](../admin/login.md).

## Sign-in with the account user (desktop app, web app, licence portal) { #anmeldung-mit-dem-kontobenutzer-desktop-app-web-app-lizenzportal }

**"E-mail address or password is not correct."**
Check the address and the Caps Lock key. You reset the password yourself
via **Forgot password** on the sign-in page of the
[licence portal](../portal/index.md) — the link is valid for one hour. The
new password also applies immediately to the desktop and web app.

**The "Code from the authenticator app" field appears.**
Not an error: the [second factor](../portal/security.md) is set up for your user.
Enter the current six-digit code — in the
desktop app into the six boxes, which check it themselves after the sixth digit
([Sign-in](../admin/login.md#bedienelemente)). If the
code is not correct, check the time on your phone; if the app has been lost,
Herzog resets the second factor ([support](support.md)).

**"This user is deactivated."**
An administrator of your account has deactivated the access in the licence portal —
see [Invite and manage users](../portal/users.md).

**"Too many failed attempts. Please try again later."**
The licence server slows down after several failed attempts. Wait a few
minutes.

**"The licence server cannot be reached … Only users who have already signed in online on this computer can sign in offline."**
Without a connection, the desktop app only lets in users who have already
signed in online on this computer — with the password from that time.
Check the connection or sign in with such a user. From version 2.1.2 the
same applies when the licence server only returns an error page during
maintenance (HTTP 502, 503 or 504); older versions stopped with
*"The licence server responded with HTTP 503."*

**Invitation link expired.**
The link from the invitation email is valid for 14 days. Open the expired
link anyway: on the page *This invitation has expired*,
**Send a new invitation** sends a new invitation to your address. Or an
administrator renews the invitation in the licence portal under **Users**.
If you have since received a reminder or a new invitation,
only its link is valid.

**The web app reports "All seats of this account are currently taken".**
All seats of the account are occupied, in the program or in the browser. A seat
is released as soon as a colleague closes Herzog CAB or signs out of the web app,
on the web at the latest after 15 minutes without activity. The
[licence portal](../portal/licenses.md#wer-gerade-arbeitet) shows who is currently working.
An administrator orders more seats under
[Subscription and order](../web/subscription.md).

**After signing in, "No access to the web app" appears.**
The account lacks a subscription with the web app, or the trial has expired. See
[Subscription and order](../web/subscription.md).

## Local sign-in (login and password) — dongle installations { #lokale-anmeldung-login-und-passwort-dongle-installationen }

**"Login or password is incorrect."**
Check upper/lower case and the Caps Lock key. Only an administrator
can reset your password – see [My profile](../admin/my-profile.md).

**"Too many failed attempts. Please try again later."**
After **five** failed attempts, Herzog CAB locks the account for
a short time to make automated password guessing more difficult. Wait
a few minutes and try again.

**"This account is deactivated."**
An administrator has blocked the access. Contact them – see
[Manage users](../admin/users.md).

**"This account signs in through a different provider."**
Your account was created as a Microsoft Entra or LDAP account and therefore has
no local password. Instead, sign in via **Sign in with Microsoft**
or via your company/domain account.

## Sign-in with Microsoft Entra ID { #anmeldung-mit-microsoft-entra-id }

### The browser does not open { #der-browser-offnet-sich-nicht }

By default, Herzog CAB opens the Microsoft sign-in in its own
compact sign-in window (not in a normal browser tab). If no
Chromium-based browser (Edge, Chrome …) is set as the default or
it cannot be started, Herzog CAB falls back to the default browser
in a normal tab. If this also fails, the following appears:

> "The browser could not be opened."

* Check whether a **default browser** is set in Windows
  (*Settings → Apps → Default apps*).
* As a test, open any website manually to check the
  default browser.

### Timeout or cancellation { #zeituberschreitung-oder-abbruch }

**"Timed out during Microsoft sign-in."**
You left the Microsoft sign-in window open for too long. Click
**Sign in with Microsoft** again and sign in promptly.

**"The Microsoft sign-in was cancelled."**
The sign-in window was closed before the sign-in was completed.
Try again.

In both cases, check the internet connection – the sign-in needs
access to `login.microsoftonline.com`.

### "This Microsoft account is not enabled for Herzog CAB." { #dieses-microsoft-konto-ist-nicht-fur-herzog-cab-freigeschaltet }

This message means: your Microsoft account was successfully signed in at Microsoft,
but Herzog CAB does not know it – there is neither a
matching local account nor may a new one be created automatically.

!!! info "Only an administrator can resolve this"
    Ask your administrator to check one of the following options under *System administration →
    Authentication*:

    * Is **"Create account automatically on first login (JIT)"** activated?
      Without this option, your account must be created manually in advance.
    * Is your Entra group stored in the **"Entra group → role"** table,
      so that you automatically receive the right role when you sign in?
    * Is a **default profile** stored, to which new accounts are automatically
      assigned?

    See [Authentication (Entra ID / LDAP)](../admin/authentication.md).

### "Microsoft sign-in is not configured." { #die-microsoft-anmeldung-ist-nicht-konfiguriert }

Sign-in with Microsoft Entra ID has not yet been set up for this installation.
An administrator sets it up under *System administration →
Authentication* (directory/tenant, client ID) – see
[Authentication (Entra ID / LDAP)](../admin/authentication.md).

### "A local account with this name already exists." { #es-existiert-bereits-ein-lokales-konto-mit-diesem-namen }

Your Microsoft sign-in name matches an existing **local** account.
For security reasons, Herzog CAB does not automatically take over a local account
for the Microsoft sign-in. An administrator must rename or dissolve the local
account before you can sign in with Microsoft.

## Related pages { #verwandte-seiten }

* [Sign in and sign out](../admin/login.md)
* [Sign in and choose an account (web app)](../web/login.md)
* [Password, second factor and name (licence portal)](../portal/security.md)
* [Authentication (Entra ID / LDAP)](../admin/authentication.md)
* [My profile](../admin/my-profile.md)
* [Roles and permissions](../admin/roles.md)
