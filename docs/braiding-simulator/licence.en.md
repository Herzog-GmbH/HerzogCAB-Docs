# Licence and rights

!!! abstract "Reference — Who gets the Braiding Simulator: full version subscription, model licences per user, rights, offline limit and what happens when a licence lapses"

## What you need this page for { #wofur-sie-diese-seite-brauchen }

The Braiding Simulator is an add-on to the Herzog CAB full version. For
every braiding machine you can buy from us, Herzog supplies a ready-made
**machine model**. Your company licenses the models it needs and assigns
them to individual users. This page explains what is required for this
and how the program and the web app behave when a licence is missing,
expires or is reassigned.

## Requirements { #voraussetzungen }

You see the **Braiding Simulator** entry in the navigation if all of the
following apply:

| Requirement | Explanation |
|---|---|
| **Herzog CAB full version subscription** | The Braiding Simulator only runs with the full version as an annual subscription (see [Modules](../setup/account.md#bausteine)). A full version without an end date, a dongle licence, the Designer and the trial version do not unlock it. |
| **At least one valid model licence** | Herzog activates the models for your account; you order them from Herzog sales. |
| **Sign-in with the customer account** | The models come from the licence server. In the program you must be signed in with your Herzog account, see [Sign in and obtain a licence](../setup/activate-license.md). |
| ***View Braiding Simulator* right** | Your role must be allowed to show the simulator, see [Rights](#rechte). |
| **Program version 2.1.1 or later** | The models from the licence server and the assignment per user are available in the program from version 2.1.1. In the web app they already apply. |

If a requirement is not met, the entry does not exist; it is not grayed
out. In the program, the **Braiding Simulator** tab in the settings and
the usage **Braiding Simulator** in the
[Print editor](../print-templates/index.md) are then missing as well.

In the program, *Settings > Licence* lists the **Braiding Simulator** in
the **Modules:** line as soon as your account may use it. In the licence
portal, the models are shown in a separate **Machine models** card, not
under the modules.

## Model licence per user { #modell-lizenz-je-benutzer }

* **One licence = one model for one user**, in the program and in the
  browser. A user can have several models.
* What is licensed is the **machine type**: for four identical machines,
  each user needs one licence for this model, not four.
* **Opening does not use up anything.** The simulator does not need a seat
  of its own; at program start only the seat of the full version counts.
* The administrators of your account decide in the licence portal who
  gets which model: [Assign machine models](../portal/models.md).
  Reassigning is possible at any time, without a waiting period.
* Deactivated users do not use a licence.
* If a convertible machine has several models, each model is a separate
  licence.

Your own setups and programs are not part of the licence. They are kept
when a licence expires or is assigned to another user, and open again as
soon as you have the model again.

## Rights { #rechte }

In role management ([desktop](../admin/roles.md),
[web app](../web/roles.md)) you find the **Braiding Simulator** group with
two rights. It only appears if your account may use the Braiding Simulator.

| Right | Allows | Default roles |
|---|---|---|
| **View Braiding Simulator** | Open the Braiding Simulator, load setups and programs, play them back, check them and output the switching plan. | Administrator, Editor, Viewer |
| **Edit Braiding Simulator** | Create, save, rename, assign and delete setups and programs. Without this right you can try everything out; when you leave, the changes are discarded without a prompt. | Administrator, Editor |

The rights only state what a role may do. Which machines a user sees is
determined solely by the assignment of the model licences.

## When a change arrives { #wann-eine-anderung-ankommt }

| Where | When |
|---|---|
| **Web app** | Reloads the list of machines every five minutes and whenever you return to the browser window. |
| **Program, online** | Notices during the regular synchronization with the licence server (every five minutes) that something has changed and reloads the list. A new assignment or a withdrawal therefore takes effect after about five minutes. |
| **Program, offline** | Shows a model without a connection to the licence server for **at most 7 days**, even if an *offline lease* allows you to work without a connection for up to 30 days. After that, the model appears in the list with *Connection to the licence server required* and only opens again once the program has had a connection. |

New versions of a model that Herzog releases also arrive with the
synchronization, see [Start page](index.md#startseite).

## When a licence lapses { #wenn-eine-lizenz-wegfallt }

### In the list { #in-der-liste }

The start page of the Braiding Simulator shows the reason why a model does
not open below its name:

| Display | Meaning |
|---|---|
| *Licence expired on &lt;date&gt;* | The licence has expired. The model appears gray in the list. Your setups and programs remain visible, but only open again when Herzog renews the licence. |
| *No valid licence* | There is no valid licence for the model. |
| *Connection to the licence server required* | The licence is valid, but the program has been without a connection to the licence server for too long. |

If no model at all is assigned to you, the empty list shows *No machine
model is assigned to you. Your administrator assigns model licences in the
licence portal.* In the web app, administrators also see the
**Assign in the licence portal** button below it.

### While you are working { #wahrend-sie-arbeiten }

If a model is withdrawn from you while it is open, or its licence expires,
playback stops immediately.

=== "Desktop app"

    A **Braiding Simulator** window states the reason, for example *The
    machine “…” is no longer assigned to you. Your administrator has given
    the licence to another user in the licence portal. Playback has been
    stopped.*

    * If you have unsaved changes of your own, it adds *You can still save
      your own setups and programs now.* Choose **Save and go back** or
      **Discard and go back**.
    * Otherwise, **Back to the list** takes you to the start page.
    * If you close the window with the cross, you stay in the machine, but
      playback remains locked.

    If the licence comes back (for example because the connection is
    restored), work continues without a prompt.

=== "Web app"

    Above the machine, *This machine is no longer assigned to you or its
    licence has expired. Playback has been stopped.* appears. **To the
    Braiding Simulator** takes you back to the list.

## Related pages { #verwandte-seiten }

* [Assign machine models](../portal/models.md) — the page in the licence
  portal for administrators.
* [Braiding Simulator](index.md) — overview and start page.
* [Customer account and invitation](../setup/account.md) — modules, seats,
  roles.
* [Roles and permissions](../admin/roles.md)
