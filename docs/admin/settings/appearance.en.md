# General: language, display, privacy, production planning and braiding angle

!!! abstract "Reference — “General” tab of the Settings dialog: profile quick access, language, font size, design, diagnostic log, anonymous usage statistics, production planning and reference of the braiding angle."

## What you use this area for { #wofur-sie-diesen-bereich-nutzen }

In the **General** tab (*File > Settings*) you set the language and
the appearance of the entire interface, enable the
diagnostic log if required, decide on the anonymous usage statistics and
define how Herzog CAB measures the braiding angle.

![General tab with profile, display, diagnostics and privacy.](../../assets/screenshots/settings/einstellungen-allgemein.png)

!!! warning "📷 Screenshot missing"
    **Subject:** Settings, “General” tab without header card, with the cards Profile, Display, Diagnostics, Privacy, Production planning and the new “Braiding angle” card (“Measure braiding angle” selection expanded); **Save** and **Cancel** at the bottom right.
    **How to create:** *File > Settings*, **General** tab, drag the dialog high enough that all cards are visible; expand the “Measure braiding angle” selection.
    **Target file:** `assets/screenshots/settings/einstellungen-allgemein.png` (replaces the previous image)

## Controls in detail { #bedienelemente-im-detail }

### Profile { #profil }

The **Profile** card shows the active profile and offers the
**Switch profile …** and **Manage profiles …** buttons. Details can be found on
the [Profiles (workspaces)](../profiles.md) page — profile name,
workspace folder and web server port are maintained there.

### Display { #darstellung }

| Setting | Options | Effect |
|---|---|---|
| **Language** | German, English, Italian, Spanish, Polish, Chinese | Language of the entire interface. |
| **Font size** | Normal, Large | Larger font for better readability on large or distant screens. Takes effect immediately as a preview when switched. |
| **Design** | Flat, Neumorphic | Appearance of the interface (flat surfaces or soft, three-dimensional cards). Takes effect immediately as a preview when switched. |

!!! info "A language change restarts Herzog CAB"
    So that all texts are loaded completely in the new language,
    a language change restarts the program after **Save**.
    Save open entries beforehand.

### Diagnostics { #diagnose }

| Setting | Effect |
|---|---|
| **Enable logging** | Writes a log to the `logs` folder in the workspace (file `logs\herzogcab.log`, see [Storage location](../storage-location.md)). The note next to it: *"Only needed for troubleshooting — leave off during normal operation."* |

!!! tip "Diagnostics only when needed"
    The log is only needed for troubleshooting — leave it switched off during normal
    operation. [Support](../../help/support.md) may ask you
    to switch it on temporarily.

### Privacy { #datenschutz }

| Setting | Effect |
|---|---|
| **Send anonymous usage statistics** | Sends anonymous, technical usage data so that Herzog CAB can be improved in a targeted way. |

Only technical information is sent, for example:

* which functions and calculations are used,
* how often printing or exporting takes place,
* the number of machines and users created,
* program version, operating system and language,
* how long the program is used.

**No personal data** is transmitted — it is not possible to draw conclusions about
you or your company.

!!! info "Your decision, can be changed at any time"
    At the first program start, Herzog CAB asks once for your consent
    (*"Improve Herzog CAB"* dialog). You can change your choice here at any
    time. In the **Trial version** the statistics are switched on by default
    but can also be switched off here.

### Production planning { #produktionsplanung }

| Setting | Effect |
|---|---|
| **Production hours per working day** | How many hours per working day are spent producing (1–24 h in half-hour steps, default **8 h**). Herzog CAB uses this to convert the runtime estimate of an order into calendar days when you choose **Apply production end from estimate** in the [braiding order](../../orders/braiding-order.md#tab-auftrag) or [winding order](../../orders/winding-order.md). Weekends are skipped. |

### Braiding angle { #flechtwinkel }

The braiding angle can be specified in two ways: Herzog measures it against
the **cross direction** of the braid, the technical literature mostly against the
**braid axis**. The two values add up to 90° — an angle of 30°
to the cross direction is 60° to the braid axis; at 45° both are equal.
With this card you define in which reference Herzog CAB displays the
braiding angle and expects entries.

| Setting | Options | Effect |
|---|---|---|
| **Measure braiding angle** | *To the cross direction (Herzog)* (default), *To the braid axis (technical literature)* | Reference of all braiding angle displays and entries in the program. The tooltip on each entry shows an explanatory image of the reference. Applies from **Save**; open pages show the new reference immediately. |

**What the reference changes** — everywhere only the **display and input**, not the
stored data:

* **Calculations:** every braiding angle field and every braiding angle result,
  e.g. in [Braiding angle](../../calculations/product/braid-angle.md),
  [Braiding angle via take-up](../../calculations/product/braid-angle-takeup.md),
  [Braid density](../../calculations/product/lay-length.md),
  [Product diameter](../../calculations/product/product-diameter.md),
  [Product weight](../../calculations/product/rope-weight.md),
  [Core-cover product](../../calculations/product/core-sheath.md), the
  [hollow braid](../../calculations/tubular-braid/index.md) pages and the
  printout of the calculation pages. In the hollow braid diagram, the
  reference line is horizontal for *cross direction* and vertical for *braid axis*.
* **Designer:** the **Braiding angle** field and slider in the
  [parameter panel](../../designer/parameters.md#flechtwinkel) and the
  default for new designs in the [Design](legacy-import.md) tab. The slider
  remains oriented so that moving it to the right gives a larger displayed
  value.
* **Order:** the **Braiding angle** field in the
  [braiding order](../../orders/braiding-order.md).
* **Printouts:** design printout and placeholders for the braiding angle in
  [print templates](../../print-templates/elements.md), the angle column of the
  design library and the mobile view of the
  [web server](web-server.md).

Herzog CAB always stores the braiding angle internally in the same way. If you change the
reference, nothing is converted or overwritten — orders, designs and
print templates show the same angle, just in the other reference. The
field labels do not name the reference; if you point the mouse at a
braiding angle field, the tooltip names both values, e.g. *30.0° to the
cross direction (Herzog) = 60.0° to the braid axis (technical literature)*.

!!! info "With a customer account, the choice applies to your user"
    If you sign in via the [customer account](../../setup/account.md),
    Herzog CAB additionally stores the choice with your user in the account and
    fetches it from there at program start — so it applies on every computer
    you sign in to, and in the [web app](../../web/settings.md).
    Without a connection, the last known choice applies. For
    dongle installations, the setting applies to this computer.

## Related pages { #verwandte-seiten }

* [Settings (dialog)](index.md) — overview of all tabs
* [Profiles (workspaces)](../profiles.md)
* [Storage location](../storage-location.md) — where the workspace and log are stored
* [Braiding angle (calculation)](../../calculations/product/braid-angle.md)
