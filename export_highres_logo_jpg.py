from PIL import Image, ImageDraw, ImageFont
import os

output_dir = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt"
output_jpg = os.path.join(output_dir, "Style1_正面_廟宇印章Logo_無英文高畫質獨立圖_4096px_300dpi.jpg")
output_png = os.path.join(output_dir, "factory_print_files", "Style1_正面_廟宇印章Logo_純圖案去背.png")

# High Resolution Canvas size (4096 x 4096 px)
CANVAS = 4096
STAMP_RED = (154, 43, 43, 255) # Cinnabar Red #9A2B2B

image = Image.new("RGBA", (CANVAS, CANVAS), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Scale helper
def scaled(val_320):
    return round(val_320 * (CANVAS / 320.0))

# Outer rounded rectangle
margin = scaled(25)
draw.rounded_rectangle(
    [margin, margin, CANVAS - margin, CANVAS - margin],
    radius=scaled(24),
    outline=STAMP_RED,
    width=scaled(10)
)

# Inner thin border
inner_m = scaled(39)
draw.rounded_rectangle(
    [inner_m, inner_m, CANVAS - inner_m, CANVAS - inner_m],
    radius=scaled(16),
    outline=STAMP_RED,
    width=scaled(3)
)

# Font selection (KaiTi 標楷體 or Noto Serif / Microsoft JhengHei)
font_path = r"C:\Windows\Fonts\kaiu.ttf"
if not os.path.exists(font_path):
    font_path = r"C:\Windows\Fonts\msjh.ttc"

font_right = ImageFont.truetype(font_path, scaled(56))
font_left = ImageFont.truetype(font_path, scaled(45))

# Right Column: 信 天 宮 (3 chars)
r_chars = ["信", "天", "宮"]
r_y_320 = [60, 132, 204]
rx = scaled(225)

for char, y320 in zip(r_chars, r_y_320):
    bbox = font_right.getbbox(char)
    char_w = bbox[2] - bbox[0]
    draw.text((rx - char_w//2, scaled(y320)), char, font=font_right, fill=STAMP_RED)

# Left Column: 朱 府 千 歲 (4 chars)
l_chars = ["朱", "府", "千", "歲"]
l_y_320 = [52, 112, 172, 232]
lx = scaled(115)

for char, y320 in zip(l_chars, l_y_320):
    bbox = font_left.getbbox(char)
    char_w = bbox[2] - bbox[0]
    draw.text((lx - char_w//2, scaled(y320)), char, font=font_left, fill=STAMP_RED)

# Top-Right and Bottom-Left Cloud Accents (Matching original border style)
draw.arc(
    [CANVAS - scaled(65), scaled(20), CANVAS - scaled(20), scaled(65)],
    start=180, end=360, fill=STAMP_RED, width=scaled(4)
)
draw.arc(
    [scaled(20), CANVAS - scaled(65), scaled(65), CANVAS - scaled(20)],
    start=0, end=180, fill=STAMP_RED, width=scaled(4)
)

# Save 300 DPI Transparent PNG (No English text)
image.save(output_png, "PNG", dpi=(300, 300))

# Create Independent High-Res JPEG on White Background
bg_white = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
bg_white.paste(image, (0, 0), image)
bg_white.save(output_jpg, "JPEG", quality=100, dpi=(300, 300))

print("Created high-res JPEG without English:", output_jpg)
print("Created high-res PNG without English:", output_png)
