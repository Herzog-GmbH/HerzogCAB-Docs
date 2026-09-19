"""Ersetzt Bildverweise auf noch nicht vorhandene Web-/Portal-Screenshots durch den
Standard-Platzhalter des Styleguides (und umgekehrt, sobald das Bild da ist).

    python _tools/web_platzhalter.py           # fehlende Bilder -> Platzhalter
    python _tools/web_platzhalter.py zurueck   # Platzhalter -> Bild, wo die Datei inzwischen existiert
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'
ROUTEN = {
    'web': {
        'startseite': '/', 'oberflaeche': '/ (Benutzermenü geöffnet)', 'auftraege': '/auftraege',
        'flechtauftrag': '/auftraege/<id>, Reiter Auftrag', 'spulauftrag': '/auftraege/<id> (Spulauftrag)',
        'berechnungen': '/berechnungen', 'rechner-flechtwinkel': '/berechnungen/braidAngle (10 / 5 mm, Berechnen)',
        'designs': '/designs', 'designer': '/designs/<id>', 'maschinen': '/maschinen', 'maschine': '/maschinen/<id>',
        'stammdaten': '/stammdaten/material', 'hallenplaner': '/hallenplaene',
        'hallenplan-editor': '/hallenplaene/<grundriss>/<belegung>', 'druck': '/druck/auftrag/<id>',
        'einstellungen': '/einstellungen', 'konto-benutzer': '/konto', 'abo': '/abo', 'firma': '/firma',
        'medien': '/medien', 'rollen': '/rollen', 'import': '/import', 'anmelden': '/anmelden',
        'registrieren': '/registrieren',
    },
    'portal': {
        'anmelden': '/anmelden', 'mein-konto': '/', 'benutzer': '/benutzer', 'anfordern': '/anfordern',
        'herunterladen': '/download', 'passwort': '/passwort',
    },
}
BASIS = {'web': 'Web-App lokal (127.0.0.1:5173)', 'portal': 'Lizenzportal lokal (localhost:8100)'}

img_re = re.compile(r'^!\[(?P<cap>[^\]]*)\]\((?P<rel>(?:\.\./)+assets/screenshots/(?P<ordner>web|portal)/(?P<name>[a-z0-9-]+)\.png)\)\s*$', re.M)
ph_re = re.compile(
    r'^!!! warning "📷 Screenshot fehlt"\n'
    r'    \*\*Motiv:\*\* (?P<cap>.*?)\n'
    r'    \*\*So erzeugen:\*\* (?P<how>.*?)\n'
    r'    \*\*Ziel-Datei:\*\* `assets/screenshots/(?P<ordner>web|portal)/(?P<name>[a-z0-9-]+)\.png`\n'
    r'    <!-- web-bild (?P<rel>[^ ]+) -->\n', re.M | re.S)


def zu_platzhalter(md: Path) -> int:
    text = md.read_text(encoding='utf-8')
    n = 0

    def ersatz(m):
        nonlocal n
        ordner, name, rel, cap = m.group('ordner'), m.group('name'), m.group('rel'), m.group('cap')
        if (DOCS / 'assets' / 'screenshots' / ordner / f'{name}.png').exists():
            return m.group(0)
        n += 1
        route = ROUTEN[ordner].get(name, '?')
        how = (f'{BASIS[ordner]}, Seite `{route}`; automatisch per '
               f'`python _tools/web_screenshots.py shots nur:{"portal-" if ordner == "portal" else ""}{name}`')
        return ('!!! warning "📷 Screenshot fehlt"\n'
                f'    **Motiv:** {cap}\n'
                f'    **So erzeugen:** {how}\n'
                f'    **Ziel-Datei:** `assets/screenshots/{ordner}/{name}.png`\n'
                f'    <!-- web-bild {rel} -->\n')

    neu = img_re.sub(ersatz, text)
    if n:
        md.write_text(neu, encoding='utf-8', newline='\n')
    return n


def zurueck(md: Path) -> int:
    text = md.read_text(encoding='utf-8')
    n = 0

    def ersatz(m):
        nonlocal n
        ordner, name, rel, cap = m.group('ordner'), m.group('name'), m.group('rel'), m.group('cap')
        if not (DOCS / 'assets' / 'screenshots' / ordner / f'{name}.png').exists():
            return m.group(0)
        n += 1
        return f'![{cap}]({rel})\n'

    neu = ph_re.sub(ersatz, text)
    if n:
        md.write_text(neu, encoding='utf-8', newline='\n')
    return n


modus = sys.argv[1] if len(sys.argv) > 1 else 'hin'
gesamt = 0
for md in sorted(DOCS.rglob('*.md')):
    gesamt += zurueck(md) if modus == 'zurueck' else zu_platzhalter(md)
print(('zurueck' if modus == 'zurueck' else 'platzhalter'), gesamt)
