# Update errors

!!! question "Troubleshooting — An update cannot be installed"

## The update dialog does not appear { #der-update-dialog-erscheint-nicht }

At startup, Herzog CAB automatically checks in the background whether a newer
version is available. If no notice appears although you expect a new
version:

* Check manually via the menu *Help > Updates* – this also shows
  a message if the current version is already installed.
* Check the internet connection and whether a firewall or proxy
  is blocking access to `herzog-gmbh.github.io`.
* You can see the currently installed version under *Help > About Herzog CAB*.

## "Update check failed" { #update-prufung-fehlgeschlagen }

This message appears during the manual check (*Help > Updates*) if
the version information could not be retrieved or could not be evaluated
– usually a network or firewall problem. Check the
internet connection and try again later. If the problem
persists, contact [support](support.md).

## The maintenance tool starts but aborts { #das-maintenance-tool-startet-bricht-aber-ab }

* **Insufficient rights.** The maintenance tool must be able to run with administrator rights.
  Start `HerzogCAB_Maintenance` via right-click →
  **Run as administrator**.
* **"Repository not reachable".** Check the internet connection and
  whether the address
  `https://herzog-gmbh.github.io/HerzogCAB-Feedback/repository/` can be reached
  in the browser.
* **"Component missing".** Close Herzog CAB completely – including the
  maintenance tool itself, if it is already running in the background – and
  start the update again.

## Is my data still there after an update? { #sind-meine-daten-nach-einem-update-noch-da }

Yes. The maintenance tool only replaces the program files in the
installation directory. Your master data is stored separately – in the
workspace folder of your profile and machine-wide under `%ProgramData%` –
and is not touched by an update. You will find details under
[File locations](../appendix/file-locations.md).

!!! tip "If in doubt, back up"
    Before a major update, make a copy of your
    workspace folder to be on the safe side, especially if it is on a network drive.

## Related pages { #verwandte-seiten }

* [Install updates](../setup/update.md)
* [Uninstall](../setup/uninstall.md)
* [File locations](../appendix/file-locations.md)
