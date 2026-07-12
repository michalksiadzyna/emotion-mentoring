"""Facebook book graphic — matching Instagram pin style (dark bg, logo, Playfair gold)."""
from PIL import Image, ImageDraw, ImageFont
import os

SCALE = 2
W, H = 1080 * SCALE, 1080 * SCALE  # Square for Facebook
BG = (20, 20, 24)
GOLD = (201, 169, 110)
GOLD_LIGHT = (232, 204, 150)
WHITE = (245, 243, 238)
GOLD_HOVER = (245, 213, 106)
MUTED = (154, 152, 144)

font_dir = os.path.expanduser('~/AppData/Local/Microsoft/Windows/Fonts/')
font_logo_text = ImageFont.truetype(os.path.join(font_dir, 'PlayfairDisplay-Regular.ttf'), 44)
font_title = ImageFont.truetype(os.path.join(font_dir, 'PlayfairDisplay-Black.ttf'), 180)
font_subtitle = ImageFont.truetype(os.path.join(font_dir, 'PlayfairDisplay-Italic.ttf'), 88)
font_desc = ImageFont.truetype(os.path.join(font_dir, 'Barlow-Light.ttf'), 56)
font_cta = ImageFont.truetype(os.path.join(font_dir, 'PlayfairDisplay-Regular.ttf'), 56)

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


def draw_corners(margin=60, length=80):
    c = tuple(int(v * 0.5) + int(0.5 * BG[i]) for i, v in enumerate(GOLD))
    w = 2
    draw.line([(margin, margin), (margin + length, margin)], fill=c, width=w)
    draw.line([(margin, margin), (margin, margin + length)], fill=c, width=w)
    draw.line([(W - margin, margin), (W - margin - length, margin)], fill=c, width=w)
    draw.line([(W - margin, margin), (W - margin, margin + length)], fill=c, width=w)
    draw.line([(margin, H - margin), (margin + length, H - margin)], fill=c, width=w)
    draw.line([(margin, H - margin), (margin, H - margin - length)], fill=c, width=w)
    draw.line([(W - margin, H - margin), (W - margin - length, H - margin)], fill=c, width=w)
    draw.line([(W - margin, H - margin), (W - margin, H - margin - length)], fill=c, width=w)


draw_corners()

# === LOGO + BRAND ===
logo_size = 160
logo = logo_orig.resize((logo_size, logo_size), Image.LANCZOS)
lx = (W - logo_size) // 2
y_start = 200
img.paste(logo, (lx, y_start), logo)
brand_y = y_start + logo_size + 20
draw_spaced_text(draw, "EMOTION MENTORING", W // 2, brand_y, font_logo_text, GOLD)
line_y = brand_y + 65
draw.line([((W - 120) // 2, line_y), ((W + 120) // 2, line_y)], fill=GOLD, width=2)

header_bottom = line_y + 50

# === TITLE ===
y = header_bottom + 40
l1 = "The Secret Book"
h = centered_text(draw, l1, y, font_title, WHITE)
y += h + 20
l2 = "of Emotions"
h = centered_text(draw, l2, y, font_title, WHITE)
y += h + 50

# === SUBTITLE (italic, gold) ===
sub = "The force behind the nameless craving"
h = centered_text(draw, sub, y, font_subtitle, GOLD_LIGHT)
y += h + 70

# === DESCRIPTION LINES ===
desc_lines = [
    "Twenty secrets expose the hidden force behind",
    "every craving, every compulsion,",
    "every restless reach.",
]
for line in desc_lines:
    h = centered_text(draw, line, y, font_desc, WHITE)
    y += h + 14

y += 50

# === GOLD LINE + URL ===
draw.line([((W - 120) // 2, y), ((W + 120) // 2, y)], fill=GOLD, width=2)
y += 40
centered_text(draw, "emotionmentoring.com", y, font_cta, GOLD)

img.save(os.path.join(OUT, 'fb_graphic_A.png'), 'PNG', quality=95)
print('Saved fb_graphic_A.png')
