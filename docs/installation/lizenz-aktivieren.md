# Activate Your Licence

Herzog CAB uses **Wibu CodeMeter** as its licensing system. Without a
valid licence, the application will not start.

## Licence types

| Type           | Article  | Scope                                              |
|----------------|----------|----------------------------------------------------|
| Full version   | 88805    | All features, unlimited                            |
| Demo version   | 88806    | Reduced feature set, time-limited                  |

Licences can be provided in two ways:

1. **Locally** - directly on the machine as a CmActLicense or via a USB
   dongle (CmDongle).
2. **Networked** - via a Wibu licence server in your company network.

## Variant A - activate a local licence

If you received a **ticket number** from Herzog GmbH:

1. Open the **CodeMeter Control Center** (Start menu > *CodeMeter*). If
   it is not installed, first install the *CodeMeter User Runtime* from
   [https://www.wibu.com/support/user-software.html](https://www.wibu.com/support/user-software.html).
2. Click **Update licence** > **Next**.
3. Choose **Receive licence** and click **Next**.
4. Enter the ticket number and follow the wizard.

> :material-image-area: *Screenshot: CodeMeter Control Center*

## Variant B - use a network licence

If your company runs a Wibu licence server, no further configuration is
usually needed - Herzog CAB finds the server automatically on the
network. If it doesn't:

1. Open **CodeMeter WebAdmin** (Start menu > *CodeMeter* > *CodeMeter
   Control Center* > **WebAdmin** button).
2. Go to *Settings > Server search list* and add the IP or hostname of
   your licence server.

## Licence check by Herzog CAB

On startup, Herzog CAB checks for a valid licence:

| State                       | Behaviour                                       |
|-----------------------------|-------------------------------------------------|
| Licence present, valid      | Program starts normally.                        |
| Demo licence, valid         | Program starts with a notice on remaining time. |
| Licence expired             | Notice dialog, program does not start.          |
| No licence found            | Notice dialog, program does not start.          |

If the licence check fails, see [Licence problems](../hilfe/lizenzprobleme.md).

## Next step

[First program start](erster-start.md)
