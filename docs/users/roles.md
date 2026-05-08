# Roles and Permissions

Herzog CAB uses a **role-based permission system**. Instead of setting
each permission per user, you assign roles - and each role bundles a
typical set of permissions.

## Built-in roles

| Role                 | Target group                  | Typically allowed                                          |
|----------------------|-------------------------------|------------------------------------------------------------|
| **Owner**            | Workshop manager / owner      | Everything, incl. workspace and company settings           |
| **Administrator**    | IT / functional lead          | Everything except company settings                         |
| **Master Data Editor** | Data steward                 | Edit master data and print templates, use calculations, view jobs |
| **Production**       | Machine operator              | Use calculations, edit jobs, print                         |
| **Read-only**        | Trainee / guest               | View everything, change nothing                            |

> :material-image-area: *Screenshot: Role management dialog*

## Available permissions

A role is a list made up of these individual permissions:

| Permission                | Meaning                                         |
|---------------------------|-------------------------------------------------|
| `users.manage`            | Create / change / delete users                  |
| `company.manage`          | Change company name and global settings         |
| `workspace.manage`        | Change workspace path, manage profile           |
| `masterdata.view`         | View master data                                |
| `masterdata.edit`         | Edit master data                                |
| `jobs.view`               | View jobs                                       |
| `jobs.edit`               | Edit jobs                                       |
| `designer.view`           | View designer                                   |
| `designer.edit`           | Edit in designer                                |
| `print_templates.view`    | View print templates                            |
| `print_templates.edit`    | Edit print templates                            |
| `calculations.use`        | Run calculations                                |
| `exports.print`           | Print / export                                  |

## Custom roles

In *Role management* (admin area) you can:

* view built-in roles (read-only)
* create new roles
* edit or delete custom roles

> :material-alert-circle-outline: **TODO** *Add screenshots of the dialog.*

!!! tip "Use roles sparingly"
    Start with the built-in roles. Custom roles only pay off in special
    cases - for example a "floater" role that may temporarily run
    calculations but not print.
