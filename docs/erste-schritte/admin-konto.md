# Create the First Admin Account

When a new workspace starts up for the first time, Herzog CAB prompts
for an administrator account. This account:

- can use all features of the program,
- can create additional users and assign roles,
- can reconfigure the workspace.

## Fields in the setup dialog

> :material-image-area: *Screenshot: First admin setup dialog*

| Field                  | Meaning                                                                |
|------------------------|------------------------------------------------------------------------|
| **Login name**         | Used in the login dialog. Case-insensitive.                            |
| **Display name**       | Full name shown in the program.                                        |
| **E-mail** (optional)  | Used for password reset (if configured).                               |
| **Password**           | Minimum 8 characters. At least one letter and one digit.               |
| **Confirm password**   | Must match "Password" exactly.                                         |
| **Profile picture** (optional) | Image from a file (JPG/PNG). Can be changed later.             |

## Practical notes

!!! tip "Who should be administrator?"
    Ideally a person who is **organisationally** responsible for
    Herzog CAB on the shop floor - e.g. a shift leader or workshop
    manager. Plain machine operators usually receive the *Production*
    or *Read-only* role.

!!! warning "Keep the password safe"
    If you forget the admin password, only an external intervention can
    help. Note it down somewhere safe.

## What's next?

After creating the admin you can:

* Create more users via [User Management](../benutzer/verwalten.md) -
  e.g. machine operators with restricted permissions.
* Jump straight into [Master Data](../stammdaten/index.md).
