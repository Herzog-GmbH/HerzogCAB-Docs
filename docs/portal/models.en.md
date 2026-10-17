# Assign machine models

!!! abstract "Reference — The “Machine models” page in the licence portal: assigning model licences for the Braiding Simulator to individual users and reassigning them"

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

For the [Braiding Simulator](../braiding-simulator/index.md), your company
licenses individual **machine models** from Herzog. Each model licence
applies to **one user**, in the program and in the browser. The
administrators of your account decide on this page who gets which model.
Herzog does not assign them.

* What is licensed is the **machine type**, not the individual machine: if
  four identical machines stand in the hall, each user who is to work on
  them in the simulator still needs only one licence for this model.
* A user can have several models.
* You can reassign the licences at any time, without a waiting period.
  Opening a model does not use up anything.
* If a machine has several models (convertible machines), each model is a
  separate licence.

The Braiding Simulator is only available with the **Herzog CAB full
version subscription**, see
[Braiding Simulator: Licence and rights](../braiding-simulator/licence.md#voraussetzungen).
You order additional model licences from Herzog sales; there is no way to
order them in the portal.

## Who sees the page { #wer-die-seite-sieht }

* The **Machine models** menu item (between **Users** and **Order**) is
  only visible to **administrators** of the account (*Manage company data*
  right), and only if the account has at least one model licence.
* All other users see the model licences on [My account](licenses.md) in
  the **Machine models** card, without being able to change them.

## The screen at a glance { #der-bildschirm-im-uberblick }

!!! warning "📷 Screenshot missing"
    **Subject:** “Machine models” page in the licence portal with two models, counter “1 of 2 assigned” and one tick per user, below it Save.
    **How to create:** Licence portal locally (localhost:8100), page `/modelle` with an account that has two model licences; not yet in the script `_tools/web_screenshots.py` (add the name `portal-modelle`).
    **Target file:** `assets/screenshots/portal/modelle.png`
    <!-- web-bild ../assets/screenshots/portal/modelle.png -->

At the top is a card with the heading **Machine models** and two
sentences on the rules:

* *Each model licence is for one user, in the program and in the browser.
  Tick the boxes and save. You can reassign at any time, without a waiting
  period. Opening a model does not use up anything.*
* *A change reaches the program after about five minutes. Without a
  connection to the licence server, Herzog CAB keeps showing a model for
  up to 7 days.*

If the account has model licences but currently no full version
subscription, the following also appears in yellow: *The Braiding
Simulator only runs with a full version subscription. Your account does
not currently have one.*

Below it follows the table with all models and, at the end, **Save**.

## Controls in detail { #bedienelemente-im-detail }

### Table of models { #tabelle-der-modelle }

| Column | Meaning |
|---|---|
| **Model** | Name of the machine model, below it *valid until &lt;date&gt;*. After the name there may be a status: **starts later** (the licence only starts later), **expired** or **no longer delivered** (Herzog has withdrawn the model). An active licence has no flag. |
| **Licences** | *n of m assigned*: how many users get the model and how many licences your account has for it. When you click the boxes, the page counts along immediately. If you tick more boxes than there are licences, the number turns red. The check is made on **Save**. Below it, *n in excess* appears in red if there are more assignments than licences, see below. |
| **Users** | One box per **active** user of the account, labeled with the name (without a name, with the e-mail address). Ticked = the user gets the model. |

Ended licences are not shown in the table.

### Save { #speichern }

**Save** applies all ticks of all models at once. Afterwards, one of the
following messages appears:

| Message | Meaning |
|---|---|
| *Saved. Herzog CAB applies the change at the next synchronisation, after about five minutes.* | The assignment applies. The web app reloads the list of machines every five minutes and whenever you return to the browser window, the program at its next synchronization with the licence server. |
| *Your account has &lt;n licences&gt; for &lt;model&gt;, but &lt;m&gt; are ticked. Please remove ticks or ask Herzog for more licences. Nothing has been saved.* | Too many ticks. **Nothing** is saved, not even for the other models. Remove ticks and save again. |
| *For &lt;model&gt;, a user is ticked who cannot receive a licence because they are deactivated or do not belong to this account. Nothing has been saved.* | The user has been deactivated in the meantime. Reload the page. |
| *There was nothing to change.* | The ticks already matched the saved state. |
| *&lt;Name&gt; is currently working offline. The model disappears there at the next synchronisation, after 7 days at the latest.* | You have taken a model away from a user who is currently working in the program with an offline lease. It is saved anyway. The program only learns of the change once it has a connection again; after at most 7 days without a connection it no longer opens the model in any case. |

Taking away is always possible. Adding is only possible up to the number
of licences.

### Assignments in excess { #uberzahlige-zuweisungen }

If Herzog reduces the number of licences for a model, your ticks remain.
The **oldest** assignments up to the number of licences are then
effective. The most recent ones are **in excess**: the name appears in
red, and the tooltip says *In excess: more assignments than licences. This
user does not get the model until a tick is removed.* Remove ticks until
no assignment is in excess any more.

### Footer and special cases { #fuzeile-und-sonderfalle }

* *Additional model licences are ordered from Herzog sales.*
* If there are deactivated users: *Deactivated users do not use a licence
  and are not listed here.*
* If the account does not yet have a model licence: *No machine model has
  been activated for this account yet. Model licences are ordered from
  Herzog sales.*
* If there is no active user yet: *There is no active user yet to whom
  you can assign a model.* With a link to [Users](users.md).

## What else changes the assignment { #was-sonst-noch-die-zuweisung-andert }

* **Deactivate** or **Delete** for a user under [Users](users.md) frees
  that user's model licences. If the user has models, the portal asks
  *Deactivate this account? Its model licences will become free.* and
  then confirms *The account has been deactivated. Its model licences are
  free and can be assigned to other users.*
* If you **Activate** a deactivated user again, the user does not get the
  models back automatically. Set the ticks here again.
* If a model licence expires or Herzog ends it, the ticks remain. If
  Herzog renews the licence, they apply again.
* A user's app role does not change the assignment. For the user to be
  able to open the model, the role also needs the *View Braiding
  Simulator* right (see [Licence and rights](../braiding-simulator/licence.md#rechte)).

## My account and Users { #mein-konto-und-benutzer }

* On [My account](licenses.md), below the modules, there is the **Machine
  models** card with the columns **Model**, **Licences** (*n of m
  assigned*, where applicable *n in excess*) and **Valid** (*until
  &lt;date&gt;*, where applicable *expired*) and the sentence *Each model
  licence is for one user. The account administrators decide who gets
  which model.* Administrators jump to this page with **Assign**.
* On [Users](users.md), the **Machine models** column shows for each
  user the models they effectively get, otherwise *none*. For
  administrators, the column heading is a link to this page.

The Braiding Simulator itself is not listed in the **Modules** card. In
the program, *Settings > Licence* names it in the **Modules:** line as
soon as your account may use it.

## Related pages { #verwandte-seiten }

* [Braiding Simulator: Licence and rights](../braiding-simulator/licence.md) —
  what the user sees in the program and in the web app.
* [Braiding Simulator](../braiding-simulator/index.md) — overview.
* [Inviting and managing users](users.md)
* [My account — modules, computers and seats](licenses.md)
