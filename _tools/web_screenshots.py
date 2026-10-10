"""Screenshots der Web-App (app.herzog-cab.com) und des Lizenzportals aus der lokalen Testumgebung.

Voraussetzungen: Docker-Lizenzserver auf http://localhost:8100, Vite-Dev-Server der Web-App auf
http://127.0.0.1:5173, Python-Playwright mit Chromium (`pip install playwright && playwright install chromium`).
Andere Umgebung (z. B. Musterkonto „Musterflechterei GmbH“ im Worktree Lizenzserver-homepage, Portal
http://localhost:8110, Web-App http://127.0.0.1:5230): Umgebungsvariablen HCAB_WEB und HCAB_PORTAL setzen.

Zwei Schritte:
    python _tools/web_screenshots.py login   # oeffnet ein Fenster; dort in Web-App UND Portal anmelden,
                                             # Sitzung landet in _tools/state.json (nicht einchecken);
                                             # Fenster schliessen, wenn "web=True portal=True" gemeldet ist
                                             # (Datei _tools/stop_login anlegen oder Prozess beenden)
    python _tools/web_screenshots.py shots [nur:name1,name2,portal-name]
                                             # schreibt docs/assets/screenshots/web/*.png und portal/*.png
                                             # in 1440 x 900 px (Bildnamen = Referenzen in den Seiten)

Zugangsdaten werden vom Skript nie eingegeben oder gespeichert - nur die Sitzungs-Cookies in state.json.
"""
import os
import re
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, Page

HERE = Path(__file__).parent
STATE = HERE / "state.json"
STOP = HERE / "stop_login"
DOCS = HERE.parent / "docs" / "assets" / "screenshots"
WEB = os.environ.get("HCAB_WEB", "http://127.0.0.1:5173").rstrip("/")
PORTAL = os.environ.get("HCAB_PORTAL", "http://localhost:8100").rstrip("/")
WEBAPP = WEB + "/anmelden"
TIMEOUT_S = 60 * 60 * 6

only = None
for a in sys.argv[2:]:
    if a.startswith("nur:"):
        only = set(a[4:].split(","))


def status(ctx):
    web = portal = False
    for page in ctx.pages:
        try:
            url = page.url
            if url.startswith(WEB) and not any(s in url for s in ("/anmelden", "/registrieren", "/bestaetigen")):
                if page.locator("nav").count() > 0 or page.get_by_text("Konto wählen").count() > 0:
                    web = True
            if url.startswith(PORTAL) and not any(s in url for s in ("/anmelden", "/zwei-faktor", "/zugang", "/passwort-vergessen")):
                if page.get_by_text("Abmelden").count() > 0:
                    portal = True
        except Exception:
            pass
    return web, portal


def login() -> int:
    if STOP.exists():
        STOP.unlink()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--window-size=1480,1000"])
        # Vorhandene Sitzung weiterverwenden: wer nur noch in einem Tab fehlt,
        # muss sich im anderen nicht erneut anmelden.
        ctx = browser.new_context(storage_state=str(STATE) if STATE.exists() else None,
                                  viewport={"width": 1440, "height": 900}, locale="de-DE")
        web = ctx.new_page()
        web.goto(WEBAPP)
        portal = ctx.new_page()
        portal.goto(PORTAL + "/anmelden")
        web.bring_to_front()
        print("Fenster offen. Bitte in beiden Tabs anmelden (Web-App und Lizenzportal).", flush=True)
        start = time.time()
        last = (False, False)
        while time.time() - start < TIMEOUT_S and not STOP.exists():
            time.sleep(2)
            cur = status(ctx)
            if cur != last:
                last = cur
                ctx.storage_state(path=str(STATE))
                print(f"Stand: web={cur[0]} portal={cur[1]} -> {STATE.name} gespeichert", flush=True)
        ctx.storage_state(path=str(STATE))
        print(f"Ende: web={last[0]} portal={last[1]}", flush=True)
        browser.close()
    return 0



def settle(page: Page, ms=1600):
    try:
        page.wait_for_load_state("networkidle", timeout=8000)
    except Exception:
        pass
    time.sleep(ms / 1000)


def hinweise_weg(page: Page):
    """Frage nach den Nutzungsdaten ("Herzog CAB verbessern") mit "Nicht senden" beantworten.
    Die Antwort steht danach im localStorage des Kontexts und gilt fuer alle weiteren Seiten."""
    try:
        knopf = page.get_by_role("button", name="Nicht senden")
        if knopf.count() > 0 and knopf.first.is_visible():
            knopf.first.click(); time.sleep(0.6)
    except Exception as e:
        print("  Hinweis Nutzungsdaten:", e)


# Der Flechtsimulator steht nicht im Handbuch (bis er bestellbar ist). Hat das Konto ihn
# freigeschaltet, blendet HCAB_OHNE_SIMULATOR=1 fuer die Bilder aus, was ein Konto ohne ihn
# nicht sieht: Navigationseintraege (Web-App und Portal), im Portal die Karte "Maschinenmodelle"
# (#modelle) und die gleichnamige Spalte der Benutzerliste.
OHNE_SIMULATOR = """
document.addEventListener('DOMContentLoaded', () => {
  const s = document.createElement('style');
  s.textContent = "a[href^='/flechtsimulator'], a[href^='/maschinenmodelle'], a[href='/modelle'], #modelle"
                + " { display: none !important; }";
  document.head.appendChild(s);
  document.querySelectorAll('table').forEach((tab) => {
    const kopf = [...tab.querySelectorAll('thead th')];
    const i = kopf.findIndex((th) => th.textContent.trim() === 'Maschinenmodelle');
    if (i < 0) return;
    tab.querySelectorAll('tr').forEach((tr) => { const z = tr.children[i]; if (z) z.style.display = 'none'; });
  });
});
"""


def first_link(page: Page, prefix: str) -> str | None:
    """Erster Link, dessen href mit prefix beginnt und dahinter noch etwas hat."""
    hrefs = page.eval_on_selector_all("a[href]", "els => els.map(e => e.getAttribute('href'))")
    for h in hrefs:
        if h and h.startswith(prefix) and len(h) > len(prefix) and not h[len(prefix):].startswith("?"):
            return h
    return None


def shot(page: Page, folder: str, name: str, full=False):
    out = DOCS / folder / f"{name}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(out), full_page=full)
    print("  ->", out.relative_to(DOCS), flush=True)


def run_web(ctx):
    page = ctx.new_page()

    def want(n):
        return only is None or n in only

    # Seiten ohne Sitzung in einem eigenen Kontext: angemeldet leitet /anmelden
    # auf die Startseite um. Schmal (390 px) zeigt die Karte mit Kopfband statt
    # der Markenflaeche.
    for name, pfad, breite, hoehe in [("anmelden", "/anmelden", 1440, 900), ("anmelden-schmal", "/anmelden", 390, 844),
                                      ("registrieren", "/registrieren", 1440, 900)]:
        if want(name):
            leer = ctx.browser.new_context(viewport={"width": breite, "height": hoehe}, device_scale_factor=1, locale="de-DE")
            if os.environ.get("HCAB_OHNE_SIMULATOR"):
                leer.add_init_script(OHNE_SIMULATOR)
            lp = leer.new_page()
            lp.goto(WEB + pfad); settle(lp)
            hinweise_weg(lp)
            shot(lp, "web", name)
            leer.close()

    page.goto(WEB + "/"); settle(page, 1500)
    if "/anmelden" in page.url:
        print("Web-App: NICHT angemeldet - Sitzung fehlt.", flush=True)
        return
    hinweise_weg(page)
    if want("startseite"):
        shot(page, "web", "startseite")
    if want("oberflaeche"):
        btn = page.locator("button[aria-haspopup='menu']").first
        btn.click(); time.sleep(0.5)
        shot(page, "web", "oberflaeche")
        page.keyboard.press("Escape"); page.mouse.click(700, 400); time.sleep(0.3)

    if want("auftraege") or want("flechtauftrag") or want("druck") or want("spulauftrag"):
        page.goto(WEB + "/auftraege"); settle(page, 1500)
        if want("auftraege"):
            shot(page, "web", "auftraege")
        # Zeilen sind keine Links: der Stift "Oeffnen" fuehrt in den Editor.
        def ersten_oeffnen(art_chip: str) -> str | None:
            page.goto(WEB + "/auftraege"); settle(page, 1200)
            zeile = page.locator("tr:visible").filter(has=page.get_by_text(art_chip, exact=True))
            if zeile.count() == 0:
                return None
            knopf = zeile.first.locator("button[title='Öffnen']:visible")
            if knopf.count() == 0:
                return None
            knopf.first.click(); settle(page, 1500)
            return page.url
        if want("flechtauftrag") or want("druck"):
            url = ersten_oeffnen("Flechtauftrag")
            if url and want("flechtauftrag"):
                try:
                    page.locator("[role='tab']:visible, button:visible").filter(has_text=re.compile(r"^Auftrag$")).first.click(); time.sleep(0.6)
                except Exception as e:
                    print("  Reiter Auftrag:", e)
                shot(page, "web", "flechtauftrag")
            if url and want("druck"):
                page.goto(WEB + "/druck/auftrag/" + url.rstrip("/").rsplit("/", 1)[-1]); settle(page, 2500)
                shot(page, "web", "druck")
        if want("spulauftrag"):
            url = ersten_oeffnen("Spulauftrag")
            if not url:
                page.goto(WEB + "/auftraege/neu?art=winding"); settle(page, 1500)
            shot(page, "web", "spulauftrag")

    if want("berechnungen"):
        page.goto(WEB + "/berechnungen"); settle(page)
        shot(page, "web", "berechnungen")
    if want("rechner-flechtwinkel"):
        page.goto(WEB + "/berechnungen/braidAngle"); settle(page)
        try:
            inputs = page.locator("input[type='number'], input[inputmode='decimal']")
            if inputs.count() >= 2:
                inputs.nth(0).fill("10"); inputs.nth(1).fill("5")
            page.get_by_role("button", name="Berechnen").first.click(); time.sleep(0.6)
        except Exception as e:
            print("  Flechtwinkel-Eingabe:", e)
        shot(page, "web", "rechner-flechtwinkel")

    if want("designs") or want("designer"):
        page.goto(WEB + "/designs"); settle(page, 1500)
        if want("designs"):
            shot(page, "web", "designs")
        href = first_link(page, "/designs/")
        if href and want("designer"):
            page.goto(WEB + href); settle(page, 2500)
            shot(page, "web", "designer")

    if want("versionen") or want("fachungsfarben"):
        page.goto(WEB + "/designs"); settle(page, 1500)
        hrefs = page.eval_on_selector_all("a[href^='/designs/']", "els => els.map(e => e.getAttribute('href'))")
        href = next((h for h in hrefs if h and "?" not in h and h.rstrip("/") != "/designs/neu"), None)
        if href and want("versionen"):
            # Dialog "Versionen" des ersten gespeicherten Designs, erste Fassung aufgeklappt
            page.goto(WEB + href); settle(page, 2500)
            try:
                page.locator("button[aria-label='Versionen']:visible").first.click(); settle(page, 1200)
                knopf = page.locator("dialog[open] button", has_text="Unterschiede")
                if knopf.count() > 0:
                    knopf.first.click(); settle(page, 1000)
                shot(page, "web", "versionen")
                page.keyboard.press("Escape"); time.sleep(0.3)
            except Exception as e:
                print("  Versionen:", e)
        if href and want("fachungsfarben"):
            # Eigene Seite: Fachung 2 wird nur eingestellt, nie gespeichert;
            # page.close() verwirft die Aenderung ohne Rueckfrage.
            fp = ctx.new_page()
            try:
                fp.goto(WEB + href); settle(fp, 2500)
                fp.get_by_label("Fachung", exact=True).fill("2"); settle(fp, 800)
                fp.locator("tbody.select-none tr:visible").first.click(button="right"); settle(fp, 800)
                shot(fp, "web", "fachungsfarben")
            except Exception as e:
                print("  Fachungsfarben:", e)
            finally:
                fp.close()

    if want("maschinen") or want("maschine"):
        page.goto(WEB + "/maschinen"); settle(page, 1500)
        if want("maschinen"):
            shot(page, "web", "maschinen")
        href = first_link(page, "/maschinen/")
        if href and href != "/maschinen/katalog" and want("maschine"):
            page.goto(WEB + href); settle(page, 1500)
            shot(page, "web", "maschine")

    if want("katalog") or want("katalog-dialog") or want("katalog-anlegen"):
        page.goto(WEB + "/katalog"); settle(page, 2000)
        try:
            page.get_by_role("tab", name=re.compile(r"^Flechtmaschinen")).first.click(); time.sleep(0.6)
        except Exception as e:
            print("  Reiter Flechtmaschinen:", e)
        if want("katalog"):
            shot(page, "web", "katalog")
        if want("katalog-dialog") or want("katalog-anlegen"):
            # Beispiel wie im Desktop: KB 1/12-80 hat Zubehoer, Abzug und drei Besetzungen.
            try:
                page.locator("input[type='search']").first.fill("KB 1/12-80"); time.sleep(0.8)
                # Kartentitel je nach Katalogstand mit oder ohne Gattungsname davor
                page.get_by_text(re.compile(r"^(\S+flechtmaschine )?KB 1/12-80$")).first.click(); settle(page, 1200)
                dialog = page.locator("dialog[open]")
                if want("katalog-dialog"):
                    shot(page, "web", "katalog-dialog")
                if want("katalog-anlegen"):
                    for eintrag in ("Meterzähler", "Kabine"):
                        dialog.locator("label", has_text=eintrag).first.click(); time.sleep(0.2)
                    dialog.get_by_text("Als eigene Maschine anlegen", exact=True).scroll_into_view_if_needed(); time.sleep(0.4)
                    shot(page, "web", "katalog-anlegen")
                page.keyboard.press("Escape"); time.sleep(0.3)
            except Exception as e:
                print("  Katalog-Dialog:", e)

    if want("stammdaten"):
        page.goto(WEB + "/stammdaten/material"); settle(page)
        shot(page, "web", "stammdaten")

    if want("hallenplaner") or want("hallenplan-editor"):
        page.goto(WEB + "/hallenplaene"); settle(page, 1500)
        if want("hallenplaner"):
            shot(page, "web", "hallenplaner")
        href = first_link(page, "/hallenplaene/")
        if href and want("hallenplan-editor"):
            page.goto(WEB + href); settle(page, 2500)
            shot(page, "web", "hallenplan-editor")

    simple = [("einstellungen", "/einstellungen"), ("konto-benutzer", "/konto"), ("abo", "/abo"),
              ("firma", "/firma"), ("medien", "/medien"), ("rollen", "/rollen"), ("import", "/import"),
              ("druckeditor", "/druckeditor"), ("papierkorb", "/papierkorb")]
    for name, path in simple:
        if want(name):
            page.goto(WEB + path); settle(page, 1200)
            shot(page, "web", name)
    page.close()


def run_portal(ctx):
    page = ctx.new_page()

    def want(n):
        return only is None or ("portal-" + n) in only

    if want("anmelden"):
        page.goto(PORTAL + "/anmelden"); settle(page)
        shot(page, "portal", "anmelden")
    page.goto(PORTAL + "/"); settle(page)
    if "/anmelden" in page.url:
        print("Portal: NICHT angemeldet - Sitzung fehlt.", flush=True)
        return
    for name, path, full in [("mein-konto", "/", True), ("benutzer", "/benutzer", True), ("anfordern", "/anfordern", True),
                             ("herunterladen", "/download", False), ("passwort", "/passwort", False)]:
        if want(name):
            page.goto(PORTAL + path); settle(page)
            shot(page, "portal", name, full=full)
    page.close()


def shots() -> int:
    if not STATE.exists():
        print("state.json fehlt - nur Seiten ohne Anmeldung moeglich.")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(storage_state=str(STATE) if STATE.exists() else None,
                                  viewport={"width": 1440, "height": 900},
                                  device_scale_factor=1, locale="de-DE")
        if os.environ.get("HCAB_OHNE_SIMULATOR"):
            ctx.add_init_script(OHNE_SIMULATOR)
        run_web(ctx)
        run_portal(ctx)
        browser.close()
    return 0




if __name__ == "__main__":
    modus = sys.argv[1] if len(sys.argv) > 1 else ""
    if modus == "login":
        sys.exit(login())
    if modus == "shots":
        sys.exit(shots())
    print(__doc__)
    sys.exit(2)
