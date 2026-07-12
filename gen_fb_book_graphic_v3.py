"""Facebook book graphic — exact copy of Instagram pin, resized to 1080x1080."""
from PIL import Image, ImageDraw, ImageFont
import os

SCALE = 2
W, H = 1080 * SCALE, 1080 * SCALE  # Facebook square
BG = (20, 20, 24)
GOLD = (201, 169, 110)
GOLD_LIGHT = (232, 204, 150)
WHITE = (245, 243, 238)
GOLD_HOVER = (245, 213, 106)
MUTED = (154, 152, 144)

font_dir = os.path.expanduser('~/AppData/Local/Microsoft/Windows/Fonts/')
font_logo_text = ImageFont.truetype(os.path.join(font_dir, 'PlayfairDisplay-Regular.ttf'), 44)
font_title = ImageFont.truetype(os.path.join(font_dir, 'PlayfairDisplay-Black.ttf'), 210)
font_subtitle = ImageFont.truetype(os.path.join(font_dir, 'PlayfairDisplay-Italic.ttf'), 100)
font_free_big = ImageFont.truetype(os.path.join(font_dir, 'PlayfairDisplay-Black.ttf'), 210)
font_free_small = ImageFont.truetype(os.path.join(font_dir, 'PlayfairDisplay-Regular.ttf'), 110)

logo_path = 'C:/Users/micha/Projects/emotion-mentoring/logo-transparent.png'
logo_orig = Image.open(logo_path).convert('RGBA')

OUT = 'C:/Users/micha/Projects/emotion-mentoring'

img = Image.new('RGB', (W, H), BG)
draw = ImageDraw.Draw(img)


def draw_spaced_text(draw, text, x_center, y, font, fill, spacing_px=6):
    total_w = 0
    for ch in text:
        bbox = font.getbbox(ch)
        total_w += (bbox[2] - bbox[0]) + spacing_px
    total_w -= spacing_px
    cx = x_center - total_w // 2
    for ch in text:
        bbox = font.getbbox(ch)
        char_w = bbox[2] - bbox[0]
        draw.text((cx, y), ch, fill=fill, font=font)
        cx += char_w + spacing_px


def centered_text(draw, text, y, font, color):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text(((W - tw) // 2, y), text, font=font, fill=color)
    return th


# === LOGO + BRAND (identical to IG) ===
logo_size = 180
logo = logo_orig.resize((logo_size, logo_size), Image.LANCZOS)
lx = (W - logo_size) // 2
y_start = 200
img.paste(logo, (lx, y_start), logo)
brand_y = y_start + logo_size + 24
draw_spaced_text(draw, "EMOTION MENTORING", W // 2, brand_y, font_logo_text, GOLD)
line_y = brand_y + 70
draw.line([((W - 120) // 2, line_y), ((W + 120) // 2, line_y)], fill=GOLD, width=2)

header_bottom = line_y + 50

# === TITLE (same text, same fonts as IG) ===
l1 = "The Secret Book"
l1b = font_title.getbbox(l1)
l1h = l1b[3] - l1b[1]
l1w = l1b[2] - l1b[0]

l2 = "of Emotions"
l2b = font_title.getbbox(l2)
l2h = l2b[3] - l2b[1]
l2w = l2b[2] - l2b[0]

sub = "The force behind the nameless craving"
sb = font_subtitle.getbbox(sub)
sh = sb[3] - sb[1]
sw = sb[2] - sb[0]

free_big = "Download"
fbb = font_free_big.getbbox(free_big)
fbh = fbb[3] - fbb[1]
fbw = fbb[2] - fbb[0]

free_small = "free"
fsb = font_free_small.getbbox(free_small)
fsh = fsb[3] - fsb[1]
fsw = fsb[2] - fsb[0]

# === LAYOUT — same gaps as IG, compressed to fit square ===
g2 = 25   # title line 1 -> line 2
g3 = 80   # title -> subtitle (was 100 on IG, tightened for square)
g4 = 300  # subtitle -> Download (was 500 on IG, tightened for square)
g5 = 60   # Download -> free for followers (was 80)

total = l1h + g2 + l2h + g3 + sh + g4 + fbh + g5 + fsh
available = H - header_bottom - 120
y = header_bottom + (available - total) // 2 - 80

# "The Secret Book"
draw.text(((W - l1w) // 2, y), l1, fill=WHITE, font=font_title)
y += l1h + g2

# "of Emotions"
draw.text(((W - l2w) // 2, y), l2, fill=WHITE, font=font_title)
y += l2h + g3

# "The force behind the nameless craving"
draw.text(((W - sw) // 2, y), sub, fill=GOLD_LIGHT, font=font_subtitle)
y += sh + g4

# "Download" — big gold
draw.text(((W - fbw) // 2, y), free_big, fill=GOLD_HOVER, font=font_free_big)
y += fbh + g5

# "free for followers" — smaller
draw.text(((W - fsw) // 2, y), free_small, fill=GOLD_LIGHT, font=font_free_small)

img.save(os.path.join(OUT, 'fb_graphic_A.png'), 'PNG', quality=95)
print('Saved fb_graphic_A.png')
