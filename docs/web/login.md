# Anmelden und Konto wählen

!!! abstract "Referenz — Die Anmeldeseite der Web-App: E-Mail-Adresse, Passwort, Code aus der Authenticator-App, Kontowahl und Abmelden"

## Wofür Sie diesen Bereich nutzen

Die Web-App verlangt vor dem Einstieg eine Anmeldung mit Ihrem Benutzer aus
dem [Kundenkonto](../setup/account.md) — dieselben Zugangsdaten wie im
Lizenzportal und in der Desktop-App. Mit der Anmeldung belegen Sie einen
**Platz** Ihres Abos. Er wird beim Abmelden oder nach 15 Minuten ohne
Aktivität wieder frei. Arbeiten Sie zugleich im Programm, belegen Sie zwei
Plätze.

## Der Bildschirm im Überblick

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Anmeldeseite der Web-App am breiten Bildschirm: links die blaue Markenfläche mit „Berechnen, gestalten, planen — im Browser", drei Stichpunkten und dem laufenden Zopf, rechts die Karte „Anmelden" mit E-Mail-Adresse und Passwort.
    **So erzeugen:** Web-App lokal (127.0.0.1:5173), Seite `/anmelden`; automatisch per `python _tools/web_screenshots.py shots nur:anmelden`
    **Ziel-Datei:** `assets/screenshots/web/anmelden.png`
    <!-- web-bild ../assets/screenshots/web/anmelden.png -->

Wie die Seite aussieht, hängt von der Breite des Browserfensters ab:

* **Breite Fenster** (ab etwa 1024 px, also Laptop und Monitor): Links steht
  eine Markenfläche in Herzog-Blau mit dem Satz *Berechnen, gestalten,
  planen — im Browser*, drei Stichpunkten zur Web-App und einem **laufenden
  Zopf** aus drei Fäden. Rechts steht die Karte **Anmelden** mit dem
  Untertitel *Anmeldung mit dem Kundenkonto*.
* **Schmale Fenster** (Tablet hochkant, Smartphone): Die Markenfläche
  entfällt. Die Karte trägt stattdessen oben ein blaues **Kopfband** mit
  dem Herzog-Logo und dem Zopf.

!!! warning "📷 Screenshot fehlt"
    **Motiv:** Anmeldeseite am Smartphone: die Karte „Anmelden" mit dem blauen Kopfband (Logo und Zopf) über den Feldern.
    **So erzeugen:** Web-App lokal (127.0.0.1:5173), Seite `/anmelden` bei 390 px Breite; automatisch per `python _tools/web_screenshots.py shots nur:anmelden-schmal`
    **Ziel-Datei:** `assets/screenshots/web/anmelden-schmal.png`
    <!-- web-bild ../assets/screenshots/web/anmelden-schmal.png -->

Der Zopf ist reiner Schmuck. Während die Web-App Ihre Anmeldung prüft, läuft
er schneller. Ist in Ihrem Betriebssystem *Bewegung reduzieren* eingestellt,
steht er still.

## Bedienelemente im Detail

| Element | Bedeutung |
|---|---|
| **E-Mail-Adresse** | Ihr Anmeldename im Kundenkonto. |
| **Passwort** | Ihr Konto-Passwort. Das Augen-Symbol rechts im Feld zeigt das Passwort im Klartext an (**Passwort anzeigen**) bzw. verbirgt es wieder (**Passwort verbergen**). |
| **Anmelden** | Prüft E-Mail-Adresse und Passwort; währenddessen dreht sich ein Ladesymbol im Knopf. Danach öffnet sich die [Startseite](start.md). Ist für Ihren Benutzer der [zweite Faktor](../portal/security.md) eingerichtet, folgt zuerst der Code (siehe unten). |
| **Passwort vergessen?** | Öffnet in einem neuen Tab die Seite *Passwort vergessen* des Lizenzportals. Dort fordern Sie einen Link zum Setzen eines neuen Passworts an. Haben Sie Ihre E-Mail-Adresse schon eingetragen, ist sie dort vorbelegt. |
| **Kostenlos testen** | Führt zur [Registrierung für die Testphase](trial.md) (nur sichtbar, wenn die Selbstregistrierung freigeschaltet ist). |

### Code aus der Authenticator-App

Mit eingerichtetem zweiten Faktor wechselt die Karte nach **Anmelden** zu
**Bestätigen** mit dem Hinweis *Bitte den Code aus der Authenticator-App
eingeben.* Der **Code** steht in **sechs Kästchen**, eines je Ziffer:

* Tippen Sie die sechs Ziffern ein. Das Kästchen für die nächste Ziffer ist
  blau umrandet. Die Web-App nimmt nur Ziffern an.
* Sie können den Code auch **einfügen**. Am Smartphone schlägt die Tastatur
  den Code oft schon vor; ein Tipp darauf füllt alle Kästchen.
* Sobald die sechste Ziffer steht, prüft die Web-App den Code **von
  selbst**. Den Knopf **Bestätigen** brauchen Sie dann nicht; er ist erst
  mit sechs Ziffern bedienbar.
* Stimmt der Code nicht, schüttelt sich die Karte kurz, die Kästchen werden
  **rot** und leer, und es erscheint *Der Code stimmt nicht.* Sobald Sie
  wieder tippen, verschwindet das Rot. Die App zeigt alle 30 Sekunden einen
  neuen Code. Nehmen Sie im Zweifel den nächsten.

### Meldungen

Bei jedem Fehler schüttelt sich die Karte kurz, und die Meldung erscheint
in einem roten Kasten über dem Knopf.

| Meldung | Bedeutung |
|---|---|
| *E-Mail-Adresse oder Passwort stimmen nicht.* | Zugangsdaten prüfen; Passwort über **Passwort vergessen?** zurücksetzen. Dieselbe Meldung erscheint, wenn ein Administrator Ihren Benutzer im Lizenzportal deaktiviert hat. |
| *Der Code stimmt nicht.* | Der Code aus der Authenticator-App war falsch oder schon abgelaufen. Den aktuellen Code eingeben. |
| *Alle Plätze dieses Kontos sind gerade belegt. Belegt: n von m Plätzen.* | Alle Plätze des Kontos sind gerade belegt, im Programm oder im Browser. Warten Sie, bis ein Kollege Herzog CAB beendet, sich abmeldet oder 15 Minuten inaktiv war. Oder ein Administrator [bestellt weitere Plätze](subscription.md). |
| *Bitte zuerst die E-Mail-Adresse bestätigen. …* | Nur nach einer [Selbstregistrierung](trial.md): Der Link aus der Bestätigungsmail wurde noch nicht geöffnet. **Bestätigungsmail erneut senden** schickt die Mail noch einmal. |
| *Zu viele Fehlversuche. Bitte in n Minuten noch einmal.* | Der Lizenzserver bremst nach mehreren Fehlversuchen. Warten Sie die genannte Zeit ab. |

## Konto wählen

Als Benutzer eines Kundenkontos landen Sie nach der Anmeldung direkt in
Ihrem Konto; eine Auswahl gibt es für Sie nicht.

!!! info "Herzog-Mitarbeiter"
    Mitarbeiter von Herzog arbeiten in einem internen Konto. Gehören sie zu
    mehreren internen Konten, erscheint nach der Anmeldung die Seite
    **Konto wählen** mit einer Liste der Konten (Firma, Kundennummer) und
    einem Suchfeld; gewechselt wird später im
    [Benutzermenü](interface.md#benutzermenu) über die Auswahl **Konto**.
    Kundenkonten sind für sie nicht wählbar — für Kundendaten legt der
    Kunde selbst einen Benutzer an.

## Kein Zugang zur Web-App

Hat Ihr Konto kein Abo mit Web-App oder ist die Testphase abgelaufen, zeigt
die Web-App nach der Anmeldung die Seite **Kein Zugang zur Webapp** mit dem
Hinweis *„Für das Konto &lt;Firma&gt; ist Herzog CAB Web nicht freigeschaltet oder
die Testphase ist abgelaufen."* Von dort gelangen Sie zu
[Abo und Bestellung](subscription.md) oder melden sich ab. Ihre Daten bleiben
erhalten.

## Abmelden

* Über das **Abmelden**-Symbol unten in der Seitenleiste neben Ihrem
  Namen, oder
* über **Abmelden** im [Benutzermenü](interface.md#benutzermenu) der
  Kopfzeile.

Beim Abmelden wird Ihr Platz sofort frei. Ohne Abmeldung endet die
Sitzung nach längerer Inaktivität von selbst.

## Verwandte Seiten

* [Kundenkonto und Einladung](../setup/account.md) — Einladung annehmen, Passwort setzen
* [Passwort und zweiter Faktor](../portal/security.md)
* [Testphase und Registrierung](trial.md)
* [Login-Probleme](../help/login-problems.md)
