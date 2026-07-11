# Druckprobleme

!!! question "Problemlösung — Drucken oder die Druckvorschau funktioniert nicht wie erwartet"

## Drucker wird nicht gefunden

Herzog CAB nutzt beim Drucken den normalen Windows-Druckdialog – es stehen
also genau die Drucker zur Auswahl, die auch unter Windows eingerichtet
sind.

* Stellen Sie sicher, dass der gewünschte Drucker unter Windows
  installiert und als **Standarddrucker** hinterlegt oder in der
  Druckerliste sichtbar ist (*Windows-Einstellungen → Drucker & Scanner*).
* Netzwerkdrucker: prüfen Sie, ob der Drucker im Netzwerk erreichbar ist
  (Testseite über Windows drucken).
* Alternativ als **PDF ausgeben**: Im Druckdialog steht „Microsoft Print to
  PDF" als Drucker zur Verfügung – so lässt sich ein Ausdruck auch ohne
  angeschlossenen Drucker prüfen oder per E-Mail weitergeben.

## Druckvorschau zeigt falsche Daten oder leere Felder

Das Aussehen und die Inhalte eines Ausdrucks bestimmt die verwendete
[Druckvorlage](../print-templates/index.md). Zwei Ursachen sind typisch:

* **Falsche Vorlage verknüpft.** Jede Vorlage legt unter **Verwendung**
  fest, wofür sie gilt (z. B. *Auftrag*). Prüfen Sie in der
  [Vorlagenverwaltung](../print-templates/manage.md), ob die richtige
  Vorlage für Ihren Auftragstyp ausgewählt ist.
* **Falsche Platzhalter in freien Textfeldern.** Anders als
  **Datentabellen**, die sich automatisch mit den Auftragsdaten füllen,
  ziehen frei platzierte **Textfelder** ihren Inhalt aus einer
  Parameter-ID, die Sie selbst eintragen (z. B. `design.name`). Ist die ID
  falsch geschrieben, bleibt das Feld beim Druck leer. Prüfen Sie die
  Parameter-IDs im [Druckvorlagen-Editor](../print-templates/editor.md) –
  eine Übersicht gültiger IDs finden Sie unter
  [Elemente und Platzhalter](../print-templates/elements.md).

!!! tip "Vorher testen"
    Drucken Sie eine neue oder geänderte Vorlage einmal probeweise (oder als
    PDF) mit einem echten Auftrag, bevor Sie sie im Tagesgeschäft einsetzen.

## Druckvorschau reagiert langsam

Bei Druckvorlagen mit sehr vielen Tabellenzeilen (z. B. großen
Klöppeltabellen) kann der Aufbau der Vorschau spürbar dauern – das ist eine
[bekannte Einschränkung](limitations.md). Reduzieren Sie testweise die
Zeilenzahl oder warten Sie den Aufbau einmal ab; danach reagiert die
Vorschau wieder normal.

## Verwandte Seiten

* [Auftrag drucken und QR-Code](../orders/print.md)
* [Vorlagen verwalten](../print-templates/manage.md)
* [Elemente und Platzhalter](../print-templates/elements.md)
* [Vorschau und Druck](../print-templates/preview-and-print.md)
