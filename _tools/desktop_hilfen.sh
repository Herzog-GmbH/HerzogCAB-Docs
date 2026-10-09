# Hilfen fuer Desktop-Aufnahmen. Aufruf: source s.sh
D=/c/Users/e.siemering/QTDIR/HerzogCAB-Docs-zweisprachig
SC="C:\Users\EBC58~1.SIE\AppData\Local\Temp\claude\C--Users-e-siemering-QTDIR-HerzogCAB\b002b1dd-dbfb-41ec-bad3-f608da8e6bfd\scratchpad"
SUF="${SUF:-}"   # "" = deutsch, ".en" = englisch
k() { powershell -ExecutionPolicy Bypass -File "$D/_tools/klick.ps1" "$@"; }        # k [-Titel t] -Do "..."
f() { local ziel="$1"; shift; local win; win=$(cygpath -w "$D/docs/assets/screenshots/$ziel")
      win="${win%.png}$SUF.png"; powershell -ExecutionPolicy Bypass -File "$D/_tools/fenster.ps1" -Out "$win" "$@"; }
v() { powershell -ExecutionPolicy Bypass -File "$D/_tools/fenster.ps1" -Out "$SC\v.png" "$@"; }   # Vorschau
nav() { k -Do "move:18,500;wait:700;click:200,$1;wait:300;move:1000,600;wait:500;park;wait:${2:-1800}"; }
liste() { powershell -ExecutionPolicy Bypass -File "$D/_tools/fenster.ps1" -Liste; }
navs() { k -Do "move:18,500;wait:700;scroll:200,700,-10;wait:500;click:200,$1;wait:300;move:1000,600;wait:500;park;wait:${2:-1800}"; }
