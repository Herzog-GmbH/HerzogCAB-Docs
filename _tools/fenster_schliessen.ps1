# Fenster von HerzogCAB nach Titel suchen und auf Position/Groesse setzen.
param([string]$Titel, [int]$X, [int]$Y, [int]$B, [int]$H)
Add-Type @"
using System;
using System.Text;
using System.Runtime.InteropServices;
public class Sw {
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc f, IntPtr l);
  [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetWindowText(IntPtr h, StringBuilder s, int n);
  [DllImport("user32.dll")] public static extern bool SetWindowPos(IntPtr h, IntPtr a, int x, int y, int cx, int cy, uint f);
  [DllImport("user32.dll")] public static extern IntPtr SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern bool PostMessage(IntPtr h, uint m, IntPtr w, IntPtr l);
}
"@
[Sw]::SetProcessDPIAware() | Out-Null
$p = Get-Process HerzogCAB | Select-Object -First 1
$ziel = [IntPtr]::Zero
[Sw]::EnumWindows({ param($h, $l)
  $pid2 = 0; [Sw]::GetWindowThreadProcessId($h, [ref]$pid2) | Out-Null
  if ($pid2 -eq $p.Id -and [Sw]::IsWindowVisible($h)) {
    $sb = New-Object System.Text.StringBuilder 256; [Sw]::GetWindowText($h, $sb, 256) | Out-Null
    if ($sb.ToString() -match $Titel) { $script:ziel = $h }
  }
  return $true }, [IntPtr]::Zero) | Out-Null
if ($ziel -eq [IntPtr]::Zero) { "FEHLER: kein Fenster '$Titel'"; exit 1 }
[Sw]::PostMessage($ziel, 0x0010, [IntPtr]::Zero, [IntPtr]::Zero) | Out-Null
"geschlossen"
