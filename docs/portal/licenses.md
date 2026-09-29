# Mein Konto — Bausteine, Rechner und Plätze

!!! abstract "Referenz — Die Startseite des Lizenzportals: Bausteine mit Plätzen, angemeldete Rechner, wer gerade arbeitet, und Ihre Anfragen"

## Wofür Sie diesen Bereich nutzen

**Mein Konto** ist die Übersicht Ihres Kundenkontos. Hier sehen Sie, welche
Bausteine Ihre Firma hat und wie viele Plätze gerade belegt sind. Sie sehen
auch, welche Rechner angemeldet sind und wer gerade arbeitet, im Programm
oder im Browser. Administratoren geben hier Plätze frei, sperren Rechner
und verfolgen ihre Anfragen an Herzog.

## Der Bildschirm im Überblick

![Mein Konto im Lizenzportal (Bild vom früheren Stand): Firmenkarte, Bausteine mit Plätzen, angemeldete Rechner und Anfragen.](../assets/screenshots/portal/mein-konto.png)

<!-- VERALTET seit 24.09.2026: mein-konto.png zeigt noch "Im Browser angemeldet" statt "Wer gerade arbeitet". Neu erzeugen mit: python _tools/web_screenshots.py shots nur:portal-mein-konto -->

!!! info "Bild vom früheren Stand"
    Das Bild zeigt noch die frühere Aufteilung. Ein aktuelles Bild folgt.
    Maßgeblich ist die Beschreibung auf dieser Seite.

Die Seite besteht aus bis zu fünf Karten, von oben nach unten:

| Karte | Inhalt |
|---|---|
| **Firma** | Firmenname und Kundennummer. Darunter **Programm herunterladen** und **Herzog CAB Web öffnen** sowie der Hinweis, wie Plätze belegt und wieder frei werden. Ist das Konto gesperrt, steht hier eine rote Meldung. Dann gibt der Lizenzserver keine neuen Lizenzen mehr aus. |
| **Bausteine** | Alle Freischaltungen mit Plätzen und Laufzeit. |
| **Rechner** | Alle Rechner, die sich mit Herzog CAB am Konto angemeldet haben. |
| **Wer gerade arbeitet** | Alle Personen, die gerade einen Platz belegen, im Programm oder im Browser. |
| **Anfragen** | Ihre Anfragen an Herzog mit Status und Antwort. Die Karte erscheint, sobald es eine Anfrage gibt. |

## Bedienelemente im Detail

### Firma

| Element | Wirkung |
|---|---|
| **Programm herunterladen** | Wechselt zu [Herunterladen](download.md). Nur, wenn das Konto einen Baustein für das Programm hat. |
| **Herzog CAB Web öffnen** | Öffnet die [Web-App](../web/index.md) in einem neuen Tab. Nur, wenn das Konto die Web-App nutzen darf. |

Der Hinweis darunter fasst die Regeln für die Plätze zusammen:

* Jeder Rechner, auf dem gerade mit Herzog CAB gearbeitet wird, belegt
  einen Platz. Ebenso jede Person im Browser.
* Wer im Programm und im Browser zugleich arbeitet, belegt zwei Plätze.
* Das Programm gibt seinen Platz beim Beenden zurück. Nach einem Absturz
  ist er nach 15 Minuten frei.
* Mit *Offline arbeiten* bleibt der Platz bis zu 30 Tage belegt.
  Programmversionen bis 2.0.0 halten ihn sieben Tage.

Mehr dazu unter [Kundenkonto und Einladung](../setup/account.md#platze).

### Bausteine

| Spalte | Bedeutung |
|---|---|
| **Baustein** | Name des Bausteins, zum Beispiel *Herzog CAB Vollversion*. Darunter steht, wofür er gilt: *Programm und Web*, *nur Programm* oder *nur Web*. Dazu gegebenenfalls Ihre Bestellreferenz. Welche Bausteine es gibt, steht unter [Kundenkonto und Einladung](../setup/account.md#bausteine). |
| **Plätze** | *n von m belegt*, darunter die Zahl der freien Plätze. Programm und Web-App zählen zusammen. Hat ein Baustein mehrere Zeilen, teilen sie sich die Plätze und zeigen dieselben Zahlen. |
| **Gültig** | *Lebenszeit* oder *bis &lt;Datum&gt;*. Läuft eine Freischaltung in **30 Tagen oder weniger** ab, steht das gelb dabei. |
| **Art** | Woher die Freischaltung stammt: *Kauf*, *Abo*, *Bestellung*, *Testversion*, *Dongle-Ersatz* oder *Kulanz*. |
| Status | **aktiv**, **abgelaufen** (Laufzeit vorbei) oder **beendet** (von Herzog beendet). |

Die Schaltflächen sehen nur Administratoren.

| Schaltfläche | Wirkung |
|---|---|
| **Plätze hinzufügen** | Wechselt zu *Bestellen* im Portal. Dort bestellen Sie weitere Plätze für Ihr Jahresabo, wie unter [Abo und Bestellung](../web/subscription.md) beschrieben. |
| **Anfrage an Herzog** | Wechselt zu [Lizenz anfordern](requests.md). |
| **Zusätzliche Lizenz anfordern** | Steht statt der beiden Schaltflächen oben, wenn sich online nichts bestellen lässt. Wechselt zu [Lizenz anfordern](requests.md). |
| **Verlängern** | Erscheint, wenn eine Freischaltung bald abläuft. Öffnet die Anfrage *Laufzeit verlängern* für diese Freischaltung. |

!!! info "Erinnerung vor dem Ablauf"
    Läuft eine Freischaltung ab, erhalten die Administratoren des Kontos
    **30 Tage und 7 Tage** vorher eine E-Mail von Herzog. Verlängern Sie
    rechtzeitig. Nach dem Ablauf startet die Desktop-App mit diesem
    Baustein nicht mehr, und die Web-App verweigert die Anmeldung.

### Rechner

Jeder Rechner, auf dem Herzog CAB am Konto angemeldet ist, erscheint hier
mit seinem Rechnernamen.

| Spalte | Bedeutung |
|---|---|
| **Rechner** | Rechnername (ohne Namen: *Unbenannt*), darunter *angemeldet von &lt;E-Mail&gt;*. Das ist der Benutzer, der den Rechner zuletzt angemeldet hat. Gesperrte oder abgemeldete Rechner sind entsprechend markiert. |
| **Belegte Plätze** | Je Baustein der Stand des Platzes: *in Benutzung* (Programm läuft), *Programm geschlossen, Platz frei*, *Offline bis &lt;Zeit&gt;* oder, bei Programmversionen bis 2.0.0, *Regelmiete bis &lt;Zeit&gt;*. *keine*, wenn der Rechner keinen Platz hält. |
| **Zuletzt gesehen** | Wann sich der Rechner zuletzt beim Lizenzserver gemeldet hat. |

| Schaltfläche | Wirkung |
|---|---|
| **Plätze freigeben** | Gibt alle Plätze dieses Rechners sofort frei, nach einer Rückfrage. Beim nächsten Programmstart holt er sich neue, wenn welche frei sind. |
| **Sperren** | Der Rechner bekommt keine Lizenz mehr, bis er entsperrt wird. Etwa bei einem verlorenen Laptop. Seine Plätze werden frei. |
| **Entsperren** | Hebt die Sperre wieder auf. |

Die Schaltflächen sehen nur Administratoren. Solange noch kein Rechner
angemeldet ist, steht hier *„Noch kein Rechner angemeldet. Nach der
Anmeldung im Programm erscheint er hier."*

!!! tip "Wann Sie Plätze von Hand freigeben"
    Ab Version 2.1.0 gibt das Programm seinen Platz beim Beenden von selbst
    zurück. **Plätze freigeben** brauchen Sie vor allem, wenn ein Rechner
    mit *Offline arbeiten* unterwegs ist und nicht zurückkommt. Oder wenn
    auf einem Rechner noch eine Version bis 2.0.0 läuft: Die hält ihren
    Platz sieben Tage, auch wenn das Programm geschlossen ist.

### Wer gerade arbeitet

Die Karte listet alle Personen, die gerade einen Platz belegen. Programm und
Web teilen sich die Plätze. Im Web wird ein Platz nach **15 Minuten ohne
Aktivität** wieder frei. Interne Konten haben im Web keine Platzgrenze.

| Spalte | Bedeutung |
|---|---|
| **Benutzer** | Wer arbeitet. |
| **Wo** | *Programm auf &lt;Rechner&gt;*, *offline auf &lt;Rechner&gt;* oder *Web*, darunter der Baustein. Arbeitet jemand im Programm und im Browser, erscheint er zweimal und belegt zwei Plätze. |
| **Zuletzt aktiv** | Wann die Person zuletzt aktiv war. |

Arbeitet gerade niemand, steht hier *Gerade niemand.*

### Anfragen

Alle [Lizenzanfragen](requests.md) Ihres Kontos mit **Datum**, **Baustein**,
**Plätze** und **Status**:

| Status | Bedeutung |
|---|---|
| **in Bearbeitung** | Herzog hat die Anfrage erhalten. |
| **erledigt** | Die Freischaltung wurde angepasst. Sie erscheint sofort in der Tabelle **Bausteine**. |
| **abgelehnt** | Herzog hat die Anfrage nicht ausgeführt. Die Begründung steht unter *Antwort von Herzog*. |

Zu jeder erledigten oder abgelehnten Anfrage erhalten die Administratoren
auch eine E-Mail.

## Verwandte Seiten

* [Kundenkonto und Einladung](../setup/account.md): was Bausteine und Plätze sind
* [Abo und Bestellung](../web/subscription.md): Jahresabo bestellen, Plätze dazukaufen, verlängern
* [Lizenz anfordern](requests.md): Anfrage an Herzog
* [Benutzer](users.md): wer sich anmelden darf
* [Lizenz und Cloud (Einstellungen)](../admin/settings/license.md): Offline arbeiten und Abmelden in der Desktop-App
* [Lizenzprobleme](../help/license-problems.md): wenn kein Platz frei ist
