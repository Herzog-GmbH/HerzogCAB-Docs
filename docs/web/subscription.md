# Abo und Kauf (Web-App)

!!! abstract "Referenz — Die Seite „Abo und Kauf" im Benutzermenü der Web-App: Freischaltungen des Kontos, Testphase, Kauf oder Anfrage an den Vertrieb"

## Wofür Sie diesen Bereich nutzen

Hier sehen Sie, welche Web-Bausteine Ihr Konto hat und wie lange sie
gelten, und erweitern sie: als Abo direkt im Browser (sobald der Kauf
freigeschaltet ist) oder als Anfrage an den Herzog-Vertrieb. Während der
[Testphase](trial.md) zeigt die Seite außerdem die Restlaufzeit und bietet
den Übergang zum Abo an. Die Seite ist auch dann erreichbar, wenn die
Testphase abgelaufen ist und die übrige Web-App gesperrt ist.

Sie öffnen die Seite über *Benutzermenü > Abo und Kauf*, den Chip
*Testphase: noch n Tage* in der Kopfzeile oder von der Seite *Kein Zugang
zur Webapp*.

## Der Bildschirm im Überblick

![Abo und Kauf in der Web-App: Hinweisbox zur Testphase, Freischaltungen des Kontos und die Karten Herzog CAB Web und Web Designer.](../assets/screenshots/web/abo.png)

### Hinweise oben

| Hinweis | Bedeutung |
|---|---|
| *Testphase: noch n Tage (bis <Datum>). Mit einem Abo entfällt die Mengenbegrenzung.* | Sie sind in der Testphase. |
| *Die Testphase ist am <Datum> abgelaufen. Mit einem Abo geht es sofort weiter, alle Daten bleiben erhalten.* | Testphase vorbei — die Web-App ist bis zum Abo gesperrt, die Daten bleiben. |
| *Die E-Mail-Adresse ist noch nicht bestätigt.* + **Mail noch einmal schicken** | Nach der Selbstregistrierung: den Link aus der Willkommensmail öffnen; die Schaltfläche schickt die Mail erneut. |
| *Vielen Dank! Die Zahlung ist eingegangen …* / *Der Kauf wurde abgebrochen …* | Rückmeldung nach der Kasse. |

### Freischaltungen dieses Kontos

Tabelle der Web-Bausteine mit **Baustein**, **Plätze** (= gleichzeitig
angemeldete Benutzer), **Gültig ab**, **Gültig bis**, **Quelle** (Lebenszeit,
Abo, Testversion …) und **Stand** (*gültig*, *abgelaufen*, *beendet*). Hat
das Konto noch keinen Web-Baustein, steht das hier.

### Herzog CAB Web / Herzog CAB Web Designer

Je Baustein eine Karte mit Beschreibung. Nur **Konto-Administratoren**
können kaufen oder anfragen.

| Element | Wirkung |
|---|---|
| **Plätze** | Gewünschte Zahl gleichzeitig angemeldeter Benutzer. |
| **Laufzeit** | *monatlich* oder *jährlich*. |
| **Zur Kasse (Stripe)** | Öffnet die Kasse des Zahlungsdienstleisters Stripe. Preise und Steuern zeigt die Kasse; das Abo lässt sich jederzeit zum Periodenende kündigen. Nach der Zahlung erscheint die Freischaltung von selbst in der Tabelle. |
| **Angebot anfragen** | Ist der Kauf im Browser noch nicht freigeschaltet, öffnet die Schaltfläche den Dialog **Anfrage an den Vertrieb** (**Nachricht**: Wunsch, Laufzeit, Rückfragen; **Anfrage schicken**). Die Antwort kommt per E-Mail; die Anfrage erscheint auch im [Lizenzportal](../portal/licenses.md#anfragen). |

### Weitere Schaltflächen

| Schaltfläche | Wirkung |
|---|---|
| **Rechnungen und Zahlungsmittel (Stripe-Kundenportal)** | Öffnet das Kundenportal von Stripe — Rechnungen herunterladen, Zahlungsmittel ändern, Abo kündigen. Nur nach einem Kauf im Browser. |
| **Lizenzportal** | Öffnet [license.herzog-cab.com](https://license.herzog-cab.com) — dort werden Desktop-Lizenzen, Rechnungen des Vertriebs und Benutzer verwaltet. |

!!! info "Desktop-Bausteine"
    Die Desktop-Bausteine (Vollversion, Designer) kaufen
    oder erweitern Sie nicht hier, sondern über
    [Lizenz anfordern](../portal/requests.md) im Lizenzportal.

## Verwandte Seiten

* [Testphase und Registrierung](trial.md)
* [Konto und Benutzer](account.md)
* [Lizenz anfordern (Lizenzportal)](../portal/requests.md)
* [Kundenkonto und Einladung](../setup/account.md) — die Bausteine im Überblick
