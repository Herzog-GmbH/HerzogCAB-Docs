# fenster.ps1 - Fensteraufnahme fuer Handbuch-Screenshots (PrintWindow, ohne Mauszeiger,
# Fenster muss nicht vorn liegen). Schneidet den unsichtbaren Win11-Rahmen weg.
# Aufruf:
#   powershell -File fenster.ps1 -Out <png> [-Titel <regex>] [-Breite 1600 -Hoehe 1000] [-Liste]
#   -Titel  waehlt ein Fenster des Prozesses HerzogCAB nach Titel (Dialoge!), sonst das Hauptfenster
#   -Breite/-Hoehe setzen die Fenstergroesse vor der Aufnahme (Position bleibt)
#   -Liste  zeigt nur alle sichtbaren Fenster des Prozesses mit Titel und Groesse
param(
  [string]$Out = "",
  [string]$Titel = "",
  [int]$Breite = 0,
  [int]$Hoehe = 0,
  [string]$Proc = "HerzogCAB",
  [switch]$Liste
)
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing
Add-Type @"
using System;
using System.Text;
using System.Collections.Generic;
using System.Runtime.InteropServices;
public class Fw {
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc f, IntPtr l);
  [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetWindowText(IntPtr h, StringBuilder s, int n);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
  [DllImport("user32.dll")] public static extern bool PrintWindow(IntPtr h, IntPtr hdc, uint f);
  [DllImport("user32.dll")] public static extern bool SetWindowPos(IntPtr h, IntPtr a, int x, int y, int cx, int cy, uint f);
  [DllImport("user32.dll")] public static extern IntPtr SetProcessDPIAware();
  [DllImport("dwmapi.dll")] public static extern int DwmGetWindowAttribute(IntPtr h, int a, out RECT r, int s);
  public struct RECT { public int Left, Top, Right, Bottom; }
  public static List<IntPtr> Fenster(uint pid) {
    var l = new List<IntPtr>();
    EnumWindows((h, x) => { uint p; GetWindowThreadProcessId(h, out p); if (p == pid && IsWindowVisible(h)) l.Add(h); return true; }, IntPtr.Zero);
    return l;
  }
}
"@
[Fw]::SetProcessDPIAware() | Out-Null
$p = Get-Process $Proc -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $p) { Write-Output "FEHLER: $Proc laeuft nicht"; exit 1 }
function TitelVon($h) { $sb = New-Object System.Text.StringBuilder 512; [Fw]::GetWindowText($h, $sb, 512) | Out-Null; $sb.ToString() }
$alle = [Fw]::Fenster([uint32]$p.Id)
if ($Liste) {
  foreach ($h in $alle) { $r = New-Object Fw+RECT; [Fw]::GetWindowRect($h, [ref]$r) | Out-Null
    Write-Output ("{0}  {1}x{2}  '{3}'" -f $h, ($r.Right-$r.Left), ($r.Bottom-$r.Top), (TitelVon $h)) }
  exit 0
}
$h = $p.MainWindowHandle
if ($Titel -ne "") {
  $h = $alle | Where-Object { (TitelVon $_) -match $Titel } | Select-Object -First 1
  if (-not $h) { Write-Output "FEHLER: kein Fenster mit Titel ~ '$Titel'"; exit 1 }
}
if ($Breite -gt 0 -and $Hoehe -gt 0) {
  $r = New-Object Fw+RECT; [Fw]::GetWindowRect($h, [ref]$r) | Out-Null
  [Fw]::SetWindowPos($h, [IntPtr]::Zero, $r.Left, $r.Top, $Breite, $Hoehe, 0x0014) | Out-Null  # NOZORDER|NOACTIVATE
  Start-Sleep -Milliseconds 900
}
$r = New-Object Fw+RECT; [Fw]::GetWindowRect($h, [ref]$r) | Out-Null
$e = New-Object Fw+RECT; [Fw]::DwmGetWindowAttribute($h, 9, [ref]$e, 16) | Out-Null   # EXTENDED_FRAME_BOUNDS
$w = $r.Right - $r.Left; $ht = $r.Bottom - $r.Top
$bmp = New-Object System.Drawing.Bitmap $w, $ht
$g = [System.Drawing.Graphics]::FromImage($bmp)
$hdc = $g.GetHdc(); [Fw]::PrintWindow($h, $hdc, 2) | Out-Null; $g.ReleaseHdc($hdc); $g.Dispose()
$cx = $e.Left - $r.Left; $cy = $e.Top - $r.Top; $cw = $e.Right - $e.Left; $ch = $e.Bottom - $e.Top
if ($cw -le 0 -or $ch -le 0) { $cx = 0; $cy = 0; $cw = $w; $ch = $ht }
$zu = $bmp.Clone((New-Object System.Drawing.Rectangle($cx, $cy, $cw, $ch)), $bmp.PixelFormat)
$voll = [System.IO.Path]::GetFullPath($Out)
[System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($voll)) | Out-Null
$zu.Save($voll, [System.Drawing.Imaging.ImageFormat]::Png)
$zu.Dispose(); $bmp.Dispose()
Write-Output ("GESPEICHERT {0} ({1}x{2}) '{3}'" -f $voll, $cw, $ch, (TitelVon $h))
