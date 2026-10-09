# Printing problems

!!! question "Troubleshooting — Printing or the print preview does not work as expected"

## Printer is not found { #drucker-wird-nicht-gefunden }

Herzog CAB uses the normal Windows print dialog for printing – so
exactly the printers that are set up in Windows are available
for selection.

* Make sure that the desired printer is installed in Windows
  and set as the **default printer** or visible in the
  printer list (*Windows Settings → Printers & scanners*).
* Network printers: check whether the printer can be reached on the network
  (print a test page via Windows).
* Alternatively **output as PDF**: in the print dialog, "Microsoft Print to
  PDF" is available as a printer – this way you can check a printout without a
  connected printer or pass it on by email.

## Print preview shows wrong data or empty fields { #druckvorschau-zeigt-falsche-daten-oder-leere-felder }

The appearance and content of a printout are determined by the
[print template](../print-templates/index.md) used. Two causes are typical:

* **Wrong template linked.** Each template defines under **Usage**
  what it applies to (e.g. *Order*). Check in
  [template management](../print-templates/manage.md) whether the right
  template is selected for your order type.
* **Wrong placeholders in free text fields.** Unlike
  **data tables**, which fill automatically with the order data,
  freely placed **text fields** take their content from a
  parameter ID that you enter yourself (e.g. `design.name`). If the ID is
  misspelt, the field remains empty when printed. Check the
  parameter IDs in the [print template editor](../print-templates/editor.md) –
  you will find an overview of valid IDs under
  [Elements and placeholders](../print-templates/elements.md).

!!! tip "Test beforehand"
    Print a new or changed template once as a test (or as a
    PDF) with a real order before you use it in day-to-day business.

## Print preview responds slowly { #druckvorschau-reagiert-langsam }

With print templates with very many table rows (e.g. large
carrier tables), building the preview can take noticeably long – this is a
[known limitation](limitations.md). As a test, reduce the
number of rows or wait once for it to be built; afterwards the
preview responds normally again.

## Related pages { #verwandte-seiten }

* [Print an order and QR code](../orders/print.md)
* [Manage templates](../print-templates/manage.md)
* [Elements and placeholders](../print-templates/elements.md)
* [Preview and print](../print-templates/preview-and-print.md)
