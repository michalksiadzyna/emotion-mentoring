# Bundle a preview into a fully self-contained mobile HTML (no network needed)
param([Parameter(Mandatory)][string]$In, [Parameter(Mandatory)][string]$Out)

$proj = 'C:/Users/micha/Projects/emotion-mentoring'
$html = Get-Content "$proj/$In" -Raw

$gsap  = Get-Content "$proj/vendor/gsap.min.js" -Raw
$st    = Get-Content "$proj/vendor/ScrollTrigger.min.js" -Raw
$lenis = Get-Content "$proj/vendor/lenis.min.js" -Raw

$html = $html.Replace('<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>', "<script>`n$gsap`n</script>")
$html = $html.Replace('<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>', "<script>`n$st`n</script>")
$html = $html.Replace('<script defer src="https://unpkg.com/lenis@1.3.25/dist/lenis.min.js"></script>', "<script>`n$lenis`n</script>")

$b64 = [Convert]::ToBase64String([IO.File]::ReadAllBytes("$proj/portrait.webp"))
$uri = "data:image/webp;base64,$b64"
$html = $html.Replace("url('portrait.webp')", "url('$uri')")
$html = $html.Replace('src="portrait.webp"', "src=""$uri""")

# fonts: replace Google Fonts link with inlined @font-face data URIs
$fonts = Get-Content "$proj/vendor/fonts_inline.css" -Raw
$html = $html.Replace('<link rel="preconnect" href="https://fonts.googleapis.com">', '')
$html = $html.Replace('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>', '')
$html = $html.Replace('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400;1,500&family=IBM+Plex+Mono:wght@400;500&family=Jost:wght@300;400&display=swap" rel="stylesheet">', "<style>`n$fonts`n</style>")
Set-Content "$proj/$Out" $html -NoNewline
Write-Output "$Out : $((Get-Item "$proj/$Out").Length) bytes"
