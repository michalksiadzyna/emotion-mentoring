# Fetch Google Fonts CSS and inline all latin/latin-ext woff2 as data URIs
$cssUrl = 'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400;1,500&family=IBM+Plex+Mono:wght@400;500&family=Jost:wght@300;400&display=swap'
$ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
$css = (Invoke-WebRequest -Uri $cssUrl -Headers @{ 'User-Agent' = $ua }).Content

# split into subset-labeled blocks: /* latin */ @font-face {...}
$pattern = '/\*\s*([a-z-]+)\s*\*/\s*(@font-face\s*\{[^}]*\})'
$keep = [System.Text.StringBuilder]::new()
foreach ($m in [regex]::Matches($css, $pattern)) {
  $subset = $m.Groups[1].Value
  if ($subset -ne 'latin' -and $subset -ne 'latin-ext') { continue }
  $block = $m.Groups[2].Value
  $urlM = [regex]::Match($block, 'url\((https://[^)]+\.woff2)\)')
  if ($urlM.Success) {
    $u = $urlM.Groups[1].Value
    $bytes = (Invoke-WebRequest -Uri $u -Headers @{ 'User-Agent' = $ua }).Content
    $b64 = [Convert]::ToBase64String($bytes)
    $block = $block.Replace($u, "data:font/woff2;base64,$b64")
  }
  [void]$keep.AppendLine($block)
}
$outPath = 'C:/Users/micha/Projects/emotion-mentoring/vendor/fonts_inline.css'
Set-Content $outPath $keep.ToString() -NoNewline
$faces = ([regex]::Matches((Get-Content $outPath -Raw), '@font-face')).Count
Write-Output "faces: $faces, size: $((Get-Item $outPath).Length) bytes"
