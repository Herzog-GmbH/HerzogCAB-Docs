# klick.ps1 - Bedient ein Fenster von Herzog CAB fuer Handbuch-Screenshots.
# Koordinaten = Pixel im Bild, das fenster.ps1 vom selben Fenster liefert (sichtbarer Rahmen, ohne Schatten).
# Aufruf:  powershell -File klick.ps1 [-Titel <regex>] -Do "<befehle>"
# Befehle (durch ; getrennt):
#   click:X,Y   right:X,Y   dbl:X,Y   move:X,Y   scroll:X,Y,N (N>0 hoch, N<0 runter)
#   drag:X1,Y1,X2,Y2      type:<text>      keys:<SendKeys, z. B. {ENTER} ^a {TAB}>      wait:MS
#   park                  Mauszeiger aus dem Fenster nehmen (rechts unten neben das Fenster)
param(
  [string]$Titel = "",
  [string]$Do = "",
  [string]$Proc = "HerzogCAB"
)
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Windows.Forms
Add-Type @"
using System;
using System.Text;
using System.Collections.Generic;
using System.Runtime.InteropServices;
public class Kw {
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc f, IntPtr l);
  [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetWindowText(IntPtr h, StringBuilder s, int n);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h, int n);
  [DllImport("user32.dll")] public static extern bool IsIconic(IntPtr h);
  [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
  [DllImport("user32.dll")] public static extern void mouse_event(uint f, uint dx, uint dy, int d, IntPtr e);
  [DllImport("user32.dll")] public static extern IntPtr SetProcessDPIAware();
  [DllImport("dwmapi.dll")] public static extern int DwmGetWindowAttribute(IntPtr h, int a, out RECT r, int s);
  public struct RECT { public int Left, Top, Right, Bottom; }
  public const uint LD=0x02, LU=0x04, RD=0x08, RU=0x10, WHEEL=0x800;
  public static List<IntPtr> Fenster(uint pid) {
    var l = new List<IntPtr>();
    EnumWindows((h, x) => { uint p; GetWindowThreadProcessId(h, out p); if (p == pid && IsWindowVisible(h)) l.Add(h); return true; }, IntPtr.Zero);
    return l;
  }
}
"@
[Kw]::SetProcessDPIAware() | Out-Null
$p = Get-Process $Proc -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $p) { Write-Output "FEHLER: $Proc laeuft nicht"; exit 1 }
function TitelVon($h) { $sb = New-Object System.Text.StringBuilder 512; [Kw]::GetWindowText($h, $sb, 512) | Out-Null; $sb.ToString() }
$h = $p.MainWindowHandle
if ($Titel -ne "") {
  $h = [Kw]::Fenster([uint32]$p.Id) | Where-Object { (TitelVon $_) -match $Titel } | Select-Object -First 1
  if (-not $h) { Write-Output "FEHLER: kein Fenster mit Titel ~ '$Titel'"; exit 1 }
}
if ([Kw]::IsIconic($h)) { [Kw]::ShowWindow($h, 9) | Out-Null; Start-Sleep -Milliseconds 300 }
[Kw]::SetForegroundWindow($h) | Out-Null
Start-Sleep -Milliseconds 250
$e = New-Object Kw+RECT; [Kw]::DwmGetWindowAttribute($h, 9, [ref]$e, 16) | Out-Null

function S([int]$x,[int]$y){ [Kw]::SetCursorPos($e.Left + $x, $e.Top + $y) | Out-Null; Start-Sleep -Milliseconds 60 }
function Ev([uint32]$f,[int]$d=0){ [Kw]::mouse_event($f,0,0,$d,[IntPtr]::Zero) }
function EscapeSK([string]$t){ ($t -replace '([+^%~(){}\[\]])','{$1}') }

foreach ($cmd in ($Do -split ';')) {
  $c = $cmd.Trim(); if ($c -eq "") { continue }
  $i = $c.IndexOf(':')
  $op = if ($i -ge 0) { $c.Substring(0,$i).Trim() } else { $c }
  $arg = if ($i -ge 0) { $c.Substring($i+1) } else { "" }
  $a = $arg -split ','
  switch ($op) {
    "click"  { S $a[0] $a[1]; Ev ([Kw]::LD); Start-Sleep -Milliseconds 40; Ev ([Kw]::LU) }
    "right"  { S $a[0] $a[1]; Ev ([Kw]::RD); Start-Sleep -Milliseconds 40; Ev ([Kw]::RU) }
    "dbl"    { S $a[0] $a[1]; Ev ([Kw]::LD); Ev ([Kw]::LU); Start-Sleep -Milliseconds 50; Ev ([Kw]::LD); Ev ([Kw]::LU) }
    "move"   { S $a[0] $a[1] }
    "scroll" { S $a[0] $a[1]; Ev ([Kw]::WHEEL) ([int]$a[2] * 120) }
    "drag"   { S $a[0] $a[1]; Ev ([Kw]::LD); Start-Sleep -Milliseconds 80
               for ($k=1; $k -le 10; $k++) { S ([int]$a[0] + ([int]$a[2]-[int]$a[0])*$k/10) ([int]$a[1] + ([int]$a[3]-[int]$a[1])*$k/10); Start-Sleep -Milliseconds 30 }
               Ev ([Kw]::LU) }
    "type"   { [System.Windows.Forms.SendKeys]::SendWait((EscapeSK $arg)) }
    "keys"   { [System.Windows.Forms.SendKeys]::SendWait($arg) }
    "wait"   { Start-Sleep -Milliseconds ([int]$arg) }
    "park"   { [Kw]::SetCursorPos($e.Right + 40, $e.Bottom - 10) | Out-Null }
    default  { Write-Output "WARN: unbekannt '$op'" }
  }
  Start-Sleep -Milliseconds 150
}
Write-Output ("OK '{0}'" -f (TitelVon $h))
