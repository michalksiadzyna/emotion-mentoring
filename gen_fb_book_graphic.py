"""Generate Facebook book announcement graphic — two versions (A and B)."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = "C:/Users/micha/Projects/emotion-mentoring"
COVER_PATH = "C:/Users/micha/Projects/emotion-mentoring/approved/covers/book_cover.png"
FONT_DIR = "C:/Users/micha/AppData/Local/Microsoft/Windows/Fonts"

# Colors
BG = (20, 20, 24)
GOLD = (201, 169, 110)
GOLD_LIGHT = (232, 204, 150)
WHITE = (245, 243, 238)
MUTED = (154, 152, 144)

# Canvas: 1080x1080 (Facebook photo post, square)
W, H = 2160, 2160  # 2x for retina

def load_font(name, size):
    path = os.path.join(FONT_DIR, name)
    return ImageFont.truetype(path, size)

font_title = load_font("PlayfairDisplay-Black.ttf", 130)
font_subtitle = load_font("PlayfairDisplay-Italic.ttf", 72)
font_body = load_font("Barlow-Light.ttf", 56)
font_label = load_font("Barlow-Regular.ttf", 42)
font_author = load_font("PlayfairDisplay-Regular.ttf", 52)
font_cta = load_font("Barlow-Regular.ttf", 48)

def draw_corners(draw, margin=60, length=80, color=GOLD, opacity_factor=0.5):
    c = tuple(int(v * opacity_factor) + int((1-opacity_factor)*BG[i]) for i, v in enumerate(color))
    w = 2
    # Top-left
    draw.line([(margin, margin), (margin + length, margin)], fill=c, width=w)
    draw.line([(margin, margin), (margin, margin + length)], fill=c, width=w)
    # Top-right
    draw.line([(W - margin, margin), (W - margin - length, margin)], fill=c, width=w)
    draw.line([(W - margin, margin), (W - margin, margin + length)], fill=c, width=w)
    # Bottom-left
    draw.line([(margin, H - margin), (margin + length, H - margin)], fill=c, width=w)
    draw.line([(margin, H - margin), (margin, H - margin - length)], fill=c, width=w)
    # Bottom-right
    draw.line([(W - margin, H - margin), (W - margin - length, H - margin)], fill=c, width=w)
    draw.line([(W - margin, H - margin), (W - margin, H - margin - length)], fill=c, width=w)

def centered_text(draw, text, y, font, color):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    draw.text((x, y), text, font=font, fill=color)
    return bbox[3] - bbox[1]

def draw_gold_line(draw, y, line_w=200):
    x1 = (W - line_w) // 2
    draw.line([(x1, y), (x1 + line_w, y)], fill=GOLD, width=2)


# ═══════════════════════════════════════
# VERSION A: Cover + text side by side feel (cover centered top, text below)
# ═══════════════════════════════════════
img_a = Image.new("RGB", (W, H), BG)
draw_a = ImageDraw.Draw(img_a)
draw_corners(draw_a)

# Load and place cover
cover = Image.open(COVER_PATH)
cover_h = 900
cover_w = int(cover.width * (cover_h / cover.height))
cover_resized = cover.resize((cover_w, cover_h), Image.LANCZOS)

# Add subtle border to cover
cover_with_border = Image.new("RGB", (cover_w + 4, cover_h + 4), GOLD)
cover_with_border.paste(cover_resized, (2, 2))
cx = (W - cover_with_border.width) // 2
cy = 200
img_a.paste(cover_with_border, (cx, cy))

# Text below cover
y = cy + cover_h + 100
h = centered_text(draw_a, "THE SECRET BOOK", y, font_title, WHITE)
y += h + 15
h = centered_text(draw_a, "OF EMOTIONS", y, font_title, GOLD)
y += h + 40
draw_gold_line(draw_a, y)
y += 50
h = centered_text(draw_a, "The force behind the nameless craving", y, font_subtitle, GOLD_LIGHT)
y += h + 60
h = centered_text(draw_a, "Five chapters. Twenty secrets. Free.", y, font_body, WHITE)
y += h + 30
h = centered_text(draw_a, "emotionmentoring.com", y, font_cta, GOLD)

img_a.save(os.path.join(OUT_DIR, "fb_graphic_A.png"), quality=95)
print("Version A saved.")


# ═══════════════════════════════════════
# VERSION B: Text-only, typographic (no cover image)
# ═══════════════════════════════════════
img_b = Image.new("RGB", (W, H), BG)
draw_b = ImageDraw.Draw(img_b)
draw_corners(draw_b)

# Eye symbol (simple geometric)
eye_y = 380
eye_cx, eye_cy = W // 2, eye_y
# Outer eye shape
for i in range(3):
    offset = i * 0.3
    draw_b.arc(
        [(eye_cx - 160, eye_cy - 80 + int(offset*20)), (eye_cx + 160, eye_cy + 80 - int(offset*20))],
        0, 360, fill=GOLD, width=2
    )
# Simple eye arcs
draw_b.arc([(eye_cx - 160, eye_cy - 80), (eye_cx + 160, eye_cy + 80)], 200, 340, fill=GOLD, width=2)
draw_b.arc([(eye_cx - 160, eye_cy - 80), (eye_cx + 160, eye_cy + 80)], 20, 160, fill=GOLD, width=2)
# Pupil
draw_b.ellipse([(eye_cx - 25, eye_cy - 25), (eye_cx + 25, eye_cy + 25)], outline=GOLD, width=2)

y = eye_cy + 140
h = centered_text(draw_b, "S H E N", y, font_label, MUTED)
y += h + 80

draw_gold_line(draw_b, y, 120)
y += 60

h = centered_text(draw_b, "THE SECRET BOOK", y, font_title, WHITE)
y += h + 15
h = centered_text(draw_b, "OF EMOTIONS", y, font_title, GOLD)
y += h + 50

draw_gold_line(draw_b, y)
y += 60

h = centered_text(draw_b, "The force behind the nameless craving", y, font_subtitle, GOLD_LIGHT)
y += h + 80

# Body lines
lines = [
    "Twenty secrets expose the hidden force behind",
    "every craving, every compulsion, every restless reach.",
    "Each one peels back a layer of the emotional system.",
    "The last one places the key in your hands.",
]
for line in lines:
    h = centered_text(draw_b, line, y, font_body, WHITE)
    y += h + 16

y += 50
draw_gold_line(draw_b, y, 120)
y += 55
h = centered_text(draw_b, "Free download", y, font_label, MUTED)
y += h + 12
h = centered_text(draw_b, "emotionmentoring.com", y, font_cta, GOLD)

img_b.save(os.path.join(OUT_DIR, "fb_graphic_B.png"), quality=95)
print("Version B saved.")
print("Done.")
