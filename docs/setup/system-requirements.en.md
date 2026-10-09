# System requirements

!!! abstract "Reference — Which operating systems, hardware, browsers and permissions Herzog CAB requires"

## Desktop app

### Operating system { #betriebssystem }

| Requirement           | Recommendation                          |
|-----------------------|-----------------------------------------|
| Operating system      | Windows 10 (64-bit) or Windows 11; macOS 13 or later (from version 2.1.0) |
| Architecture          | x64 (Windows)                            |

The current version of Herzog CAB has been tested on Windows 10 and 11.
On Windows it runs only as a 64-bit program. Older Windows versions
are not supported. From version 2.1.0, Herzog CAB is also available for
macOS 13 or later, as a separate installation package (`.dmg`). The
operation is identical.

### Hardware

| Component             | Minimum                | Recommended                 |
|-----------------------|------------------------|-----------------------------|
| Processor             | Dual-core 2 GHz        | Quad-core 2.5 GHz or more   |
| Memory (RAM)          | 4 GB                   | 8 GB                        |
| Free disk space       | 500 MB                 | 2 GB (order data)           |
| Screen resolution     | 1280 x 720             | 1920 x 1080 or higher      |
| Graphics              | OpenGL-capable graphics | Dedicated graphics card for the 3D views (Designer, Factory Planner) |

### Licence { #lizenz }

You need a valid licence to operate Herzog CAB. Since
version 2.0 there are two routes:

| Licensing route | Requirement on the computer |
|---|---|
| **Customer account** (standard case) | Internet connection to the licence server `license.herzog-cab.com` (HTTPS, port 443) — at least at the first start and then at the latest every 24 hours, with version 2.0.0 every seven days. For longer periods without a connection there is the offline lease for up to 30 days. No additional software. |
| **CodeMeter** (existing customers with CmDongle or CmAct licence) | The [Wibu CodeMeter Runtime](codemeter.md) and the dongle or the activated software licence. |

More on this under [Customer account and invitation](account.md) and
[Sign in and obtain a licence](activate-license.md).

### Permissions { #berechtigungen }

You need **administrator rights** on the target computer for the installation.
Day-to-day use of the program does not require
administrator rights.

### Internet

A permanent internet connection is not strictly required. It is
needed for:

- **signing in to the customer account** and the silent renewal of the
  licence lease (with the account model; without a connection the program keeps running for up to
  24 hours, with an offline lease for up to 30 days)
- the **cloud upload** of the workspace folder to the web app, if
  switched on (see [Licence and cloud](../admin/settings/license.md))
- updates via the **Herzog CAB Maintenance** tool
- signing in with **Microsoft Entra ID** (only for dongle installations
  with Microsoft sign-in set up)
- sending feedback from the program

!!! tip "Proxy and firewall"
    Herzog CAB uses the Windows proxy settings. If the company
    firewall has to allow destinations, these are `license.herzog-cab.com` (licence) and
    `app.herzog-cab.com` (cloud upload and web app), each via HTTPS.

### Printer { #drucker }

If you want to print calculations or orders, a
printer should be installed and set up as the default printer in Windows.
A PDF printer (e.g. *Microsoft Print to PDF*) is sufficient.

## Web app

The [web app](../web/index.md) at
[app.herzog-cab.com](https://app.herzog-cab.com) requires no installation.

| Requirement | Recommendation |
|---|---|
| Browser | Current version of Microsoft Edge, Google Chrome, Firefox or Safari (in each case the last two major versions). |
| Screen | From 1280 px width for the full interface with sidebar; from 768 px (tablet) adapted layout; on a smartphone a bar with the most important destinations. |
| 3D views | Browser with WebGL 2 (standard in all browsers listed); for large braids and halls a dedicated graphics card is an advantage. |
| Internet | Permanent connection — the web app works directly on the server. |
| Printing | Via the browser's print dialog or as a PDF file. |

A seat is a **person who is currently working**. The program and the web app
share the seats of the subscription. Anyone using both at the same time occupies two
seats. You can see how many seats your account has in the
[licence portal](../portal/licenses.md) and under
[Subscription and order](../web/subscription.md).

## Next step { #nachster-schritt }

Next, clarify which [deployment scenario](topology.md) suits your
plant — this also determines where your workspace folder is located and whether
you use the web app in addition to the desktop app.
