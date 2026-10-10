"""Ersetzt Bildverweise auf noch nicht vorhandene Web-/Portal-Screenshots durch den
Standard-Platzhalter des Styleguides (und umgekehrt, sobald das Bild da ist).

    python _tools/web_platzhalter.py           # fehlende Bilder -> Platzhalter
    python _tools/web_platzhalter.py zurueck   # Platzhalter -> Bild, wo die Datei inzwischen existiert

Englische Seiten (*.en.md) bekommen den englischen Platzhalter
("📷 Screenshot missing", Subject / How to create / Target file), siehe STYLEGUIDE.md.
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
        'registrieren': '/registrieren', 'anmelden-schmal': '/anmelden bei 390 px Breite',
        'versionen': '/designs/<id>, Symbol „Versionen"', 'papierkorb': '/papierkorb',
        'fachungsfarben': '/designs/<id>, Fachung 2, Rechtsklick auf eine Zeile der Klöppeltabelle',
        'druckeditor': '/druckeditor', 'katalog': '/katalog',
    },
    'portal': {
        'anmelden': '/anmelden', 'mein-konto': '/', 'benutzer': '/benutzer', 'anfordern': '/anfordern',
        'herunterladen': '/download', 'passwort': '/passwort',
    },
}
BASIS = {'web': 'Web-App lokal (127.0.0.1:5173)', 'portal': 'Lizenzportal lokal (localhost:8100)'}
BASIS_EN = {'web': 'Web app local (127.0.0.1:5173)', 'portal': 'Licence portal local (localhost:8100)'}
# Platzhalter-Beschriftung je Sprache: Titel, Motiv, So erzeugen, Ziel-Datei
TEXTE = {
    'de': ('📷 Screenshot fehlt', 'Motiv', 'So erzeugen', 'Ziel-Datei'),
    'en': ('📷 Screenshot missing', 'Subject', 'How to create', 'Target file'),
}


def sprache(md: Path) -> str:
    return 'en' if md.name.endswith('.en.md') else 'de'


img_re = re.compile(r'^!\[(?P<cap>[^\]]*)\]\((?P<rel>(?:\.\./)+assets/screenshots/(?P<ordner>web|portal)/(?P<name>[a-z0-9-]+)\.png)\)\s*$', re.M)
ph_re = {
    lang: re.compile(
        rf'^!!! warning "{re.escape(titel)}"\n'
        rf'    \*\*{re.escape(motiv)}:\*\* (?P<cap>.*?)\n'
        rf'    \*\*{re.escape(wie)}:\*\* (?P<how>.*?)\n'
        rf'    \*\*{re.escape(ziel)}:\*\* `assets/screenshots/(?P<ordner>web|portal)/(?P<name>[a-z0-9-]+)\.png`\n'
        r'    <!-- web-bild (?P<rel>[^ ]+) -->\n', re.M | re.S)
    for lang, (titel, motiv, wie, ziel) in TEXTE.items()
}


def zu_platzhalter(md: Path) -> int:
    text = md.read_text(encoding='utf-8')
    lang = sprache(md)
    n = 0

    def ersatz(m):
        nonlocal n
        ordner, name, rel, cap = m.group('ordner'), m.group('name'), m.group('rel'), m.group('cap')
        if (DOCS / 'assets' / 'screenshots' / ordner / f'{name}.png').exists():
            return m.group(0)
        n += 1
        route = ROUTEN[ordner].get(name, '?')
        befehl = f'`python _tools/web_screenshots.py shots nur:{"portal-" if ordner == "portal" else ""}{name}`'
        if lang == 'en':
            how = f'{BASIS_EN[ordner]}, page `{route}`; automatically via {befehl}'
        else:
            how = f'{BASIS[ordner]}, Seite `{route}`; automatisch per {befehl}'
        titel, motiv, wie, ziel = TEXTE[lang]
        return (f'!!! warning "{titel}"\n'
                f'    **{motiv}:** {cap}\n'
                f'    **{wie}:** {how}\n'
                f'    **{ziel}:** `assets/screenshots/{ordner}/{name}.png`\n'
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

    neu = ph_re[sprache(md)].sub(ersatz, text)
    if n:
        md.write_text(neu, encoding='utf-8', newline='\n')
    return n


modus = sys.argv[1] if len(sys.argv) > 1 else 'hin'
gesamt = 0
for md in sorted(DOCS.rglob('*.md')):
    gesamt += zurueck(md) if modus == 'zurueck' else zu_platzhalter(md)
print(('zurueck' if modus == 'zurueck' else 'platzhalter'), gesamt)
