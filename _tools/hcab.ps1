# hcab.ps1 - Steuer- und Screenshot-Helfer fuer Herzog CAB (Handbuch-Doku)
# Aufruf:  powershell -File hcab.ps1 -Out <png> -Do "<dsl>"
# DSL-Befehle (durch ; getrennt), Koordinaten sind FENSTER-relativ (wie im PNG):
#   click:X,Y        Linksklick
#   right:X,Y        Rechtsklick
#   dbl:X,Y          Doppelklick
#   move:X,Y         Mauszeiger bewegen (Hover)
#   scroll:X,Y,N     Mausrad N Schritte (N>0 hoch, N<0 runter) an Position X,Y
#   type:<text>      Text tippen (SendKeys-escaped automatisch)
#   keys:<sendkeys>  Roh-SendKeys (z.B. {ENTER}, ^a, {TAB})
#   wait:MS          Pause in Millisekunden
# Am Ende wird das Fenster nach -Out gespeichert und "RECT left top w h" ausgegeben.
param(
  [Parameter(Mandatory=$true)][string]$Out,
  [string]$Do = "",
  [int]$Settle = 700
)
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.Windows.Forms
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class W {
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h, int n);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
  [DllImport("user32.dll")] public static extern bool IsIconic(IntPtr h);
  [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
  [DllImport("user32.dll")] public static extern void mouse_event(uint f, uint dx, uint dy, int d, IntPtr e);
  [DllImport("user32.dll")] public static extern IntPtr SetProcessDPIAware();
  public struct RECT { public int Left, Top, Right, Bottom; }
  public const uint LD=0x02, LU=0x04, RD=0x08, RU=0x10, WHEEL=0x800;
}
"@
[W]::SetProcessDPIAware() | Out-Null

$p = Get-Process HerzogCAB -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $p) { Write-Output "ERROR: HerzogCAB not running"; exit 1 }
$h = $p.MainWindowHandle
if ([W]::IsIconic($h)) { [W]::ShowWindow($h, 9) | Out-Null; Start-Sleep -Milliseconds 300 }
[W]::SetForegroundWindow($h) | Out-Null
Start-Sleep -Milliseconds 300
$r = New-Object W+RECT
[W]::GetWindowRect($h, [ref]$r) | Out-Null

function S([int]$x,[int]$y){ [W]::SetCursorPos($r.Left + $x, $r.Top + $y); Start-Sleep -Milliseconds 60 }
function Click([int]$x,[int]$y){ S $x $y; [W]::mouse_event([W]::LD,0,0,0,[IntPtr]::Zero); Start-Sleep -Milliseconds 40; [W]::mouse_event([W]::LU,0,0,0,[IntPtr]::Zero) }
function RClick([int]$x,[int]$y){ S $x $y; [W]::mouse_event([W]::RD,0,0,0,[IntPtr]::Zero); Start-Sleep -Milliseconds 40; [W]::mouse_event([W]::RU,0,0,0,[IntPtr]::Zero) }
function DblClick([int]$x,[int]$y){ S $x $y; for($i=0;$i -lt 2;$i++){ [W]::mouse_event([W]::LD,0,0,0,[IntPtr]::Zero); [W]::mouse_event([W]::LU,0,0,0,[IntPtr]::Zero); Start-Sleep -Milliseconds 40 } }
function Wheel([int]$x,[int]$y,[int]$n){ S $x $y; [W]::mouse_event([W]::WHEEL,0,0,($n*120),[IntPtr]::Zero) }
function EscapeSK([string]$t){ ($t -replace '([+^%~(){}\[\]])','{$1}') }

foreach ($cmd in ($Do -split ';')) {
  $c = $cmd.Trim()
  if ($c -eq "") { continue }
  $i = $c.IndexOf(':')
  $op = if ($i -ge 0) { $c.Substring(0,$i).Trim() } else { $c }
  $arg = if ($i -ge 0) { $c.Substring($i+1) } else { "" }
  switch ($op) {
    "click"  { $a=$arg -split ','; Click ([int]$a[0]) ([int]$a[1]) }
    "right"  { $a=$arg -split ','; RClick ([int]$a[0]) ([int]$a[1]) }
    "dbl"    { $a=$arg -split ','; DblClick ([int]$a[0]) ([int]$a[1]) }
    "move"   { $a=$arg -split ','; S ([int]$a[0]) ([int]$a[1]) }
    "scroll" { $a=$arg -split ','; Wheel ([int]$a[0]) ([int]$a[1]) ([int]$a[2]) }
    "type"   { [System.Windows.Forms.SendKeys]::SendWait((EscapeSK $arg)) }
    "keys"   { [System.Windows.Forms.SendKeys]::SendWait($arg) }
    "wait"   { Start-Sleep -Milliseconds ([int]$arg) }
    default  { Write-Output "WARN: unknown op '$op'" }
  }
  Start-Sleep -Milliseconds 120
}

Start-Sleep -Milliseconds $Settle
[W]::GetWindowRect($h, [ref]$r) | Out-Null
$w = $r.Right - $r.Left; $ht = $r.Bottom - $r.Top
$bmp = New-Object System.Drawing.Bitmap $w, $ht
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.CopyFromScreen($r.Left, $r.Top, 0, 0, (New-Object System.Drawing.Size($w, $ht)))
$dir = Split-Path $Out -Parent
if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
$bmp.Save($Out, [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose(); $bmp.Dispose()
Write-Output ("RECT {0} {1} {2} {3}" -f $r.Left, $r.Top, $w, $ht)
Write-Output ("SAVED {0}" -f $Out)
