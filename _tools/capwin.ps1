# capwin.ps1 - bringt das Hauptfenster eines Prozesses nach vorn und macht einen Screenshot.
param(
  [Parameter(Mandatory=$true)][string]$Proc,
  [Parameter(Mandatory=$true)][string]$Out,
  [int]$Settle = 1200
)
Add-Type -AssemblyName System.Drawing
Add-Type @"
using System;using System.Runtime.InteropServices;
public class Wc{
 [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
 [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h,int n);
 [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h,out RECT r);
 [DllImport("user32.dll")] public static extern bool IsIconic(IntPtr h);
 [DllImport("user32.dll")] public static extern IntPtr SetProcessDPIAware();
 public struct RECT{public int Left,Top,Right,Bottom;}
}
"@
[Wc]::SetProcessDPIAware() | Out-Null
$p = Get-Process $Proc -ErrorAction SilentlyContinue | Where-Object { $_.MainWindowHandle -ne 0 } | Select-Object -First 1
if (-not $p) { Write-Output "ERROR: $Proc not running with window"; exit 1 }
$h = $p.MainWindowHandle
if ([Wc]::IsIconic($h)) { [Wc]::ShowWindow($h,9) | Out-Null; Start-Sleep -Milliseconds 300 }
[Wc]::SetForegroundWindow($h) | Out-Null
Start-Sleep -Milliseconds $Settle
$r = New-Object Wc+RECT
[Wc]::GetWindowRect($h,[ref]$r) | Out-Null
$w = $r.Right - $r.Left; $ht = $r.Bottom - $r.Top
$bmp = New-Object System.Drawing.Bitmap $w, $ht
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.CopyFromScreen($r.Left,$r.Top,0,0,(New-Object System.Drawing.Size($w,$ht)))
$bmp.Save($Out,[System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose();$bmp.Dispose()
Write-Output ("RECT {0} {1} {2} {3}" -f $r.Left,$r.Top,$w,$ht)
Write-Output ("SAVED {0}" -f $Out)
