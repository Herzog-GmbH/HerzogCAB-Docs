# Mehrere Flechtköpfe

!!! abstract "Referenz — Wie der Flechtsimulator zweiköpfige Maschinen zeigt: Klöppelzahl, Nummern und Laufrichtung je Kopf, gemeinsamer Abzug, Maschine 3D"

## Wofür Sie diese Seite brauchen

Mehrköpfige Maschinen wie die RU 2/12-80 haben mehrere **Flechtköpfe**
an einem Antrieb: Jeder Kopf hat seine eigenen Flügelräder, seinen
Flechtpunkt und seine Abzugsscheibe; Motor und Abzugsgetriebe sind
gemeinsam. Der Flechtsimulator erkennt die Köpfe selbst und zeigt Zahlen,
Nummern und Laufrichtung je Kopf.

## Woran der Simulator einen Kopf erkennt

Ein Flechtkopf ist eine Gruppe von Rädern, die mit dem Rest der Maschine
keinen Übergang hat, gleich wie die Weichen stehen. Ein einzelnes Rad ohne
Übergang gehört zum nächsten Kopf.

Maschinen, deren Flechtkreise über Weichen verbunden sind, zum Beispiel
eine Maschine, die zwischen *Litze 32* und *2 × Rund 16* umschaltet, haben
**einen** Kopf. Dort entscheiden die Weichen, ob ein oder zwei Geflechte
entstehen; die [3D-Vorschau](views.md#infozeilen-unter-dem-bild) zeigt
das in ihrer Infozeile.

Das Wort *Flechtkopf* steht nicht in der Oberfläche; Sie erkennen eine
mehrköpfige Maschine an der Klöppelzahl.

## Was je Kopf gilt

| Thema | Verhalten |
|---|---|
| **Klöppelzahl** | Die Startseite, die Besetzungen und die Statuszeile zeigen *2 × 12 Klöppel*, wenn alle Köpfe gleich besetzt sind, sonst zum Beispiel *12 + 10 Klöppel*. |
| **Klöppelnummern** | Jeder Kopf zählt ab 1: Eine RU 2/12-80 hat zweimal die Nummern 1 bis 12. Ein neuer Klöppel bekommt die kleinste freie Nummer **in seinem Kopf**. |
| **Laufrichtung** | Gilt um die Mitte des jeweiligen Kopfes, nicht um die Maschinenmitte. Das betrifft die Ansicht [Laufrichtung](editor.md#ansicht) und **Nach Laufrichtung färben** in der [Auswahlkarte](populate.md#auswahlkarte-kloppel). |
| **Konfigurationen** | *Voll*, *Halb* und *Tandem* von Herzog gelten je Kopf; *Voll* und *Halb* besetzen beide Laufrichtungen gleich stark. |
| **Abzug** | Alle Köpfe hängen am selben Abzugsgetriebe. Der [Abzug](views.md#abzug) wird wie bei einer einköpfigen Maschine eingestellt und gilt für alle Köpfe; gemessen wird an Kopf 1. |
| **Maschine 3D** | Die [Ansicht „Maschine“](views.md#ansicht-maschine) zeigt je Kopf Flechtpunkt, Geflecht und Abzugsscheibe. Beschriftungen und feste Ansichten beziehen sich auf Kopf 1. |

Weichen, Räder, Zeitachse und Schaltplan funktionieren wie bei einer
einköpfigen Maschine; ein Programm schaltet alle Köpfe gemeinsam, weil sie
an einem Antrieb hängen.

## Desktop-App und Web-App

Mehrere Flechtköpfe zeigen beide gleich.

## Verwandte Seiten

* [Bestücken](populate.md)
* [3D-Vorschau und Abzug](views.md)
* [Flechtsimulator](index.md)
