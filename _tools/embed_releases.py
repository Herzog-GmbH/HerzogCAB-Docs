#!/usr/bin/env python3
"""Bettet die Releaseliste als Offline-Fallback in die gebaute index.html ein.

Die Homepage holt die Releases im Browser live von der GitHub-API. Schlaegt das
fehl -- unauthentifiziert erlaubt GitHub nur 60 Abrufe pro Stunde und IP, was
hinter einem Firmen-NAT schnell erreicht ist -- rendert sie aus der Konstanten
EMBEDDED_RELEASES. Diese Liste wurde frueher von Hand gepflegt und hing zuletzt
vier Versionen hinterher (Stand v1.3.3 vom April, waehrend 1.4.6 aktuell war).
Deshalb entsteht sie jetzt bei jedem Build neu.

Aufruf: python _tools/embed_releases.py <pfad/zur/index.html>

Schlaegt der Abruf fehl, bricht das Skript ab. Das laesst den Build scheitern und
damit den bisherigen Stand der Seite online -- besser als eine Seite mit leerem
Fallback zu veroeffentlichen.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request

REPO = "Herzog-GmbH/HerzogCAB-Feedback"
API = f"https://api.github.com/repos/{REPO}/releases?per_page=100"
BEGIN = "/*RELEASES:BEGIN*/"
END = "/*RELEASES:END*/"
ATTEMPTS = 3


def fetch(token):
    """Holt die Releases. Ohne Token als Rueckfallebene, falls GITHUB_TOKEN das
    fremde Repo nicht lesen darf."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "herzogcab-docs-build",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(API, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_with_retry():
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    last = None
    for attempt in range(1, ATTEMPTS + 1):
        for use_token in ([True, False] if token else [False]):
            try:
                data = fetch(token if use_token else None)
                wie = "mit Token" if use_token else "ohne Token"
                print(f"Releases abgerufen ({wie}, Versuch {attempt}): {len(data)}")
                return data
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as err:
                last = err
                print(f"  Versuch {attempt} fehlgeschlagen: {err}")
        if attempt < ATTEMPTS:
            time.sleep(attempt * 3)
    raise SystemExit(f"Releases nicht abrufbar, Build abgebrochen: {last}")


def trim(release):
    """Reduziert auf die Felder, die renderReleases() in index.html liest --
    identisch zum Mapping im Live-Zweig der Seite."""
    return {
        "tag_name": release["tag_name"],
        "name": release["name"],
        "published_at": release["published_at"],
        "prerelease": release["prerelease"],
        "html_url": release["html_url"],
        "body": release.get("body") or "",
        "assets": [
            {"name": a["name"], "url": a["browser_download_url"], "size": a["size"]}
            for a in release.get("assets", [])
        ],
    }


def to_js_literal(releases):
    """JSON so kodieren, dass es gefahrlos in einem <script>-Block steht."""
    text = json.dumps(releases, ensure_ascii=False, separators=(",", ":"))
    # Ein "</script>" im Changelog wuerde den Script-Block sonst beenden.
    text = text.replace("</", "<\\/")
    # U+2028/U+2029 sind in JSON erlaubt, in JavaScript aber Zeilenumbrueche.
    text = text.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    return text


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Aufruf: embed_releases.py <pfad/zur/index.html>")
    path = sys.argv[1]

    with open(path, encoding="utf-8") as fh:
        html = fh.read()

    start = html.find(BEGIN)
    stop = html.find(END)
    if start == -1 or stop == -1 or stop < start:
        raise SystemExit(
            f"Marker {BEGIN} ... {END} nicht in {path} gefunden - "
            "wurde der Platzhalter in homepage/index.html entfernt?"
        )

    releases = [r for r in fetch_with_retry() if not r.get("draft")]
    if not releases:
        raise SystemExit("Kein einziges veroeffentlichtes Release, Build abgebrochen")

    literal = to_js_literal([trim(r) for r in releases])
    patched = html[: start + len(BEGIN)] + literal + html[stop:]

    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(patched)

    neueste = releases[0]["tag_name"]
    print(
        f"Fallback eingebettet: {len(releases)} Releases, neuestes {neueste}, "
        f"{len(literal.encode('utf-8')) / 1024:.1f} KB"
    )


if __name__ == "__main__":
    main()
