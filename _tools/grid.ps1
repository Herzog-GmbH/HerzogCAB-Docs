# grid.ps1 - legt ein beschriftetes Koordinaten-Raster ueber einen Screenshot
# (nur zum Ablesen von Klick-Koordinaten; die finalen Doku-Bilder bleiben sauber).
# Aufruf: powershell -File grid.ps1 -In <png> -Out <png> [-Step 100]
param(
  [Parameter(Mandatory=$true)][string]$In,
  [Parameter(Mandatory=$true)][string]$Out,
  [int]$Step = 100
)
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile($In)
$bmp = New-Object System.Drawing.Bitmap $img.Width, $img.Height
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.DrawImage($img, 0, 0, $img.Width, $img.Height)
$penMinor = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(90,255,0,0)), 1
$penMajor = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(170,255,0,0)), 1
$font = New-Object System.Drawing.Font "Consolas", 11, ([System.Drawing.FontStyle]::Bold)
$brush = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::Red)
$brushBg = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(200,255,255,255))
for ($x=0; $x -lt $img.Width; $x+=$Step) {
  $pen = if ($x % ($Step*2) -eq 0) { $penMajor } else { $penMinor }
  $g.DrawLine($pen, $x, 0, $x, $img.Height)
  $g.FillRectangle($brushBg, $x+1, 1, 34, 15)
  $g.DrawString([string]$x, $font, $brush, ($x+1), 1)
  $g.FillRectangle($brushBg, $x+1, ($img.Height-16), 34, 15)
  $g.DrawString([string]$x, $font, $brush, ($x+1), ($img.Height-16))
}
for ($y=0; $y -lt $img.Height; $y+=$Step) {
  $pen = if ($y % ($Step*2) -eq 0) { $penMajor } else { $penMinor }
  $g.DrawLine($pen, 0, $y, $img.Width, $y)
  $g.FillRectangle($brushBg, 1, $y+1, 34, 15)
  $g.DrawString([string]$y, $font, $brush, 1, ($y+1))
  $g.FillRectangle($brushBg, ($img.Width-36), $y+1, 34, 15)
  $g.DrawString([string]$y, $font, $brush, ($img.Width-36), ($y+1))
}
$g.Dispose()
$bmp.Save($Out, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose(); $img.Dispose()
Write-Output "GRID $Out"
