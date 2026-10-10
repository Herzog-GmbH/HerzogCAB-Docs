# Known limitations

!!! info "Concept — Limits of Herzog CAB that are not errors but intended"

These points are not program errors, but deliberate or
technical limits of the current version. If you observe one of these
behaviors, you do not need to open a support ticket.

## Workspace on a network drive { #workspace-auf-einem-netzlaufwerk }

If the workspace folder is on a network drive and several workstations
access it: two computers can**not edit the same
order at the same time**. The most recently saved version overwrites the
previous one without Herzog CAB warning you. Agree within the team who
is currently editing which order.

## Print preview with very large templates { #druckvorschau-bei-sehr-groen-vorlagen }

Print templates with very many table rows – such as carrier tables of large
machines – can noticeably slow down the building of the print preview. This
is independent of the actual printing; once it has been built,
the preview responds normally again.

## Trial version: fixed upper limits { #testversion-feste-obergrenzen }

In the trial version, the number of machines, orders, customers, designs,
users and calculations per calculation type is limited, and the licence expires
permanently at the end of the trial period. You will find details under
[Trial version and quotas](../basics/trial-quotas.md).

## Cloud sync: the desktop takes precedence { #cloud-abgleich-der-desktop-hat-vorrang }

The cloud sync of the desktop app synchronizes in both directions, but
not on equal terms: it uploads first and then fetches the changes
from the web app. If both sides have changed the same entry, the
desktop wins. The version from the web app is then not lost: it is available in the
web app under [Versions](../web/versions.md) and can be restored
there. Further limits:

* Files deleted in the web app (images, documents) remain in the
  workspace folder.
* An account synchronizes with exactly one workspace folder; a second
  profile can only be connected by rebinding.
* Individual files over 25 MB are skipped.

If you only want to synchronize from the desktop to the web app, switch off
*Apply changes from the web app to the workspace folder* — see
[Licence and cloud](../admin/settings/license.md) and
[Move data from the desktop app to the web app](../tasks/desktop-to-web.md).

## Web app: functions not included { #web-app-nicht-enthaltene-funktionen }

The Designer of the web app only displays mixed designs; they cannot be created
there; there is no two-window comparison. The Factory Planner lacks context menus, *Connect
walls*, automatic area detection and wall textures. The
complete comparison is available under [Web app](../web/index.md).

## Web trial: limited quantities { #web-testphase-begrenzte-mengen }

In the trial of the web app, a maximum of 2 designs, 2 machines,
4 orders and 3 customers are possible, plus as many users as the
trial version has seats, and 100 calculations per calculation type. This also applies to ZIP import. Details under
[Trial and registration](../web/trial.md).

## Related pages { #verwandte-seiten }

* [Licence problems](license-problems.md)
* [Printing problems](print-problems.md)
* [Trial version and quotas](../basics/trial-quotas.md)
* [Desktop app or web app?](../basics/platforms.md)
