# Getting started

!!! example "Guide — From the customer account or installation to the first program start"

This chapter guides you from the initial installation to the first
program start. Allow around 15 minutes for the whole process.
If Herzog CAB is already running at your site and you only want to install an **update**
or **uninstall** the program, jump straight
to the matching card below.

!!! info "Desktop app or web app?"
    Since version 2.0, Herzog CAB comes in two forms: as a **desktop app**
    for Windows and macOS and as a **web app** in the browser at
    [app.herzog-cab.com](https://app.herzog-cab.com). This chapter describes
    the installation of the desktop app. For the web app there is nothing to
    install — all you need is your customer account, see
    [Web app](../web/index.md). Which form suits which purpose is explained in
    [Desktop app or web app?](../basics/platforms.md).

<div class="grid cards" markdown>

- :material-clipboard-check-outline: **System requirements**

    Windows version, hardware, internet access and permissions required for
    the installation.

    [:octicons-arrow-right-24: Next](system-requirements.md)

- :material-lan: **Deployment scenarios**

    Single client, server with RDP access, mixed setup or web app —
    which topology suits your plant?

    [:octicons-arrow-right-24: Next](topology.md)

- :material-account-key-outline: **Customer account and invitation**

    Since version 2.0, the customer account is the standard licensing route: accept the
    invitation, set a password, understand modules and seats.

    [:octicons-arrow-right-24: Next](account.md)

- :material-application-cog-outline: **Install Herzog CAB**

    Run through the Herzog CAB setup wizard.

    [:octicons-arrow-right-24: Next](installer.md)

- :material-key-variant: **Sign in and obtain a licence**

    Sign in to the customer account at the first start — or, for existing customers,
    plug in the CmDongle or activate a CmAct licence.

    [:octicons-arrow-right-24: Next](activate-license.md)

- :material-usb-flash-drive-outline: **Install CodeMeter**

    Only for existing customers with a dongle or software licence: set up the
    Wibu runtime environment.

    [:octicons-arrow-right-24: Next](codemeter.md)

- :material-rocket-launch-outline: **First start and setup**

    What happens at the first program start: user, storage location and
    workspace folder.

    [:octicons-arrow-right-24: Next](first-run.md)

- :material-cloud-download-outline: **Install updates**

    Install a new version via the maintenance tool.

    [:octicons-arrow-right-24: Next](update.md)

- :material-trash-can-outline: **Uninstall**

    Remove Herzog CAB — with or without your order and master data.

    [:octicons-arrow-right-24: Next](uninstall.md)

</div>

## Initial installation sequence { #ablauf-der-erstinstallation }

Which steps are required depends on how your licence is provided.
Since version 2.0, the **customer account** is the standard case; if you have a
**CmDongle** or a **CmAct software licence**, you continue to work with it
unchanged.

=== "Customer account (standard from 2.0)"

    ```mermaid
    flowchart LR
      A[System requirements] --> B[Accept invitation,<br>set password]
      B --> C[Install Herzog CAB]
      C --> D[First start:<br>sign in to account]
      D --> E[Set up<br>workspace folder]
    ```

    1. Check the [system requirements](system-requirements.md) — the computer
       needs an internet connection to sign in.
    2. Accept the [invitation to the customer account](account.md) and set a
       password. The invitation is sent by Herzog or an administrator at your company.
    3. Download the installer from the licence portal and
       [install Herzog CAB](installer.md).
    4. At the first start, [sign in to the customer account](activate-license.md) — the
       licence is drawn from your account's pool.
    5. [Set up the workspace folder](first-run.md).

=== "Dongle or CmAct licence (existing customers)"

    ```mermaid
    flowchart LR
      A[System requirements] --> B[Deployment scenario]
      B --> C[CodeMeter]
      C --> D[Install Herzog CAB]
      D --> E[Activate licence]
      E --> F[First-start wizard]
    ```

    1. Clarify the [system requirements](system-requirements.md) and
       [deployment scenario](topology.md).
    2. [Install CodeMeter](codemeter.md).
    3. [Install Herzog CAB](installer.md).
    4. [Plug in the dongle or activate the CmAct licence](activate-license.md#bestandskunden-dongle-oder-cmact-lizenz).
    5. Run through the [first-start wizard](first-run.md) (create an
       administrator, choose the workspace folder).

Herzog CAB is then ready for use. How to find your way around the
interface is shown in the chapter [Basics](../basics/index.md).

!!! info "You don't have a customer account or installation package yet?"
    Contact your Herzog representative or write to
    [e.siemering@herzog-online.com](mailto:e.siemering@herzog-online.com).
    There you can also get a free
    [trial version](../web/trial.md) for 30 days, in the program and in the browser.
