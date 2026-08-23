import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

output_dir = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\temple_seals_reference"
os.makedirs(output_dir, exist_ok=True)

CANVAS = 3000
RED = (225, 20, 20, 255) # Bright Temple Vermillion Red (鮮豔廟印朱紅)

# Helper to create clean seal canvas
def new_seal_canvas():
    return Image.new("RGBA", (CANVAS, CANVAS), (255, 255, 255, 0))

# -------------------------------------------------------------
# Style A: 傳統隸書分層廟印 (Lishu Style with Horizontal Divider)
# Upper: 信 天 宮 (3 chars) | Lower: 朱 府 千 歲 (4 chars)
# -------------------------------------------------------------
def make_lishu_seal():
    img = new_seal_canvas()
    draw = ImageDraw.Draw(img)
    
    # Solid thick rounded border
    margin = 220
    draw.rounded_rectangle([margin, margin, CANVAS - margin, CANVAS - margin], radius=280, outline=RED, width=140)
    
    # Horizontal dividing line
    mid_y = int(CANVAS * 0.44)
    draw.line([margin + 60, mid_y, CANVAS - margin - 60, mid_y], fill=RED, width=70)
    
    # Try Lishu or Kai font
    font_path = r"C:\Windows\Fonts\kaiu.ttf" # 標楷體
    if not os.path.exists(font_path):
        font_path = r"C:\Windows\Fonts\msjh.ttc"
        
    font_upper = ImageFont.truetype(font_path, 420)
    font_lower = ImageFont.truetype(font_path, 380)
    
    # Top Row: 信 天 宮 (Right to Left: 宮 天 信 or Left to Right: 信 天 宮)
    # Traditional Taiwanese seals often read Left to Right or Right to Left. Let's do 信 天 宮
    u_chars = ["信", "天", "宮"]
    u_x = [650, 1500, 2350]
    u_y = 480
    for char, x in zip(u_chars, u_x):
        bbox = font_upper.getbbox(char)
        cw = bbox[2] - bbox[0]
        ch = bbox[3] - bbox[1]
        draw.text((x - cw//2, u_y - ch//2), char, font=font_upper, fill=RED)
        
    # Bottom Row: 朱 府 千 歲 (4 chars)
    l_chars = ["朱", "府", "千", "歲"]
    l_x = [580, 1190, 1800, 2410]
    l_y = 2050
    for char, x in zip(l_chars, l_x):
        bbox = font_lower.getbbox(char)
        cw = bbox[2] - bbox[0]
        ch = bbox[3] - bbox[1]
        draw.text((x - cw//2, l_y - ch//2), char, font=font_lower, fill=RED)
        
    p = os.path.join(output_dir, "廟印範例_A_隸書分層款.png")
    img.save(p, "PNG", dpi=(300, 300))
    return p

# -------------------------------------------------------------
# Style B: 傳統行書/楷書分層廟印 (Xingshu Style)
# -------------------------------------------------------------
def make_xingshu_seal():
    img = new_seal_canvas()
    draw = ImageDraw.Draw(img)
    
    margin = 220
    draw.rounded_rectangle([margin, margin, CANVAS - margin, CANVAS - margin], radius=240, outline=RED, width=140)
    
    # Horizontal dividing line
    mid_y = int(CANVAS * 0.44)
    draw.line([margin + 60, mid_y, CANVAS - margin - 60, mid_y], fill=RED, width=70)
    
    font_path = r"C:\Windows\Fonts\kaiu.ttf"
    font_upper = ImageFont.truetype(font_path, 440)
    font_lower = ImageFont.truetype(font_path, 390)
    
    # Top Row: 信 天 宮
    u_chars = ["信", "天", "宮"]
    u_x = [650, 1500, 2350]
    u_y = 480
    for char, x in zip(u_chars, u_x):
        bbox = font_upper.getbbox(char)
        cw = bbox[2] - bbox[0]
        ch = bbox[3] - bbox[1]
        draw.text((x - cw//2, u_y - ch//2), char, font=font_upper, fill=RED)
        
    # Bottom Row: 朱 府 千 歲
    l_chars = ["朱", "府", "千", "歲"]
    l_x = [580, 1190, 1800, 2410]
    l_y = 2050
    for char, x in zip(l_chars, l_x):
        bbox = font_lower.getbbox(char)
        cw = bbox[2] - bbox[0]
        ch = bbox[3] - bbox[1]
        draw.text((x - cw//2, l_y - ch//2), char, font=font_lower, fill=RED)
        
    p = os.path.join(output_dir, "廟印範例_B_行楷分層款.png")
    img.save(p, "PNG", dpi=(300, 300))
    return p

# -------------------------------------------------------------
# Style C: 傳統九疊篆/篆體滿版廟印 (Zhuanshu Seal Script Style)
# -------------------------------------------------------------
def make_zhuan_seal():
    img = new_seal_canvas()
    draw = ImageDraw.Draw(img)
    
    margin = 200
    draw.rounded_rectangle([margin, margin, CANVAS - margin, CANVAS - margin], radius=260, outline=RED, width=160)
    
    # Seal script grid placement: 4 quadrants
    # Top Right: 信天 (or 宮信) | Bottom Right: 宮 | Top Left: 朱府 | Bottom Left: 千歲
    # In traditional 4-quadrant seal:
    # Q1 (top right): 信  Q2 (bottom right): 天宮
    # Q3 (top left): 朱府 Q4 (bottom left): 千歲
    font_path = r"C:\Windows\Fonts\kaiu.ttf"
    font = ImageFont.truetype(font_path, 420)
    
    # 4 Quadrants Text Layout
    quads = [
        ("信", 2050, 650),
        ("天", 2050, 1300),
        ("宮", 2050, 1950),
        ("朱", 950, 550),
        ("府", 950, 1150),
        ("千", 950, 1750),
        ("歲", 950, 2350),
    ]
    
    for char, x, y in quads:
        bbox = font.getbbox(char)
        cw = bbox[2] - bbox[0]
        ch = bbox[3] - bbox[1]
        draw.text((x - cw//2, y - ch//2), char, font=font, fill=RED)
        
    p = os.path.join(output_dir, "廟印範例_C_九疊篆滿版款.png")
    img.save(p, "PNG", dpi=(300, 300))
    return p

# Generate all 3 styles
pA = make_lishu_seal()
pB = make_xingshu_seal()
pC = make_zhuan_seal()

# Make JPEG previews with white background
for path in [pA, pB, pC]:
    im = Image.open(path).convert("RGBA")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    bg.paste(im, (0, 0), im)
    jpg_path = path.replace(".png", ".jpg")
    bg.save(jpg_path, "JPEG", quality=98)
    # Copy to project root for web preview
    basename = os.path.basename(jpg_path)
    bg.save(os.path.join(r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt", basename), "JPEG", quality=98)

print("Traditional Temple Seal Reference Styles Generated Successfully!")
