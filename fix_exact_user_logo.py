import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

img_path = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\.user_uploaded\media_1787481598483.jpg"

# Open image
pil_img = Image.open(img_path).convert("RGBA")
w, h = pil_img.size

# The seal logo is located at approximately:
# x: 56% to 70% of width (approx 570 to 710)
# y: 30% to 45% of height (approx 310 to 450)

# Let's create an exact high-res replacement for the logo box that has 4 characters: 朱 府 千 歲
# Color of the red stamp in the image: RGB approx (154, 43, 43) / #9A2B2B

seal_w = 320
seal_h = 320
seal = Image.new("RGBA", (seal_w, seal_h), (255, 255, 255, 0))
draw = ImageDraw.Draw(seal)

color = (154, 43, 43, 255)

# Outer rounded rectangle
margin = 25
draw.rounded_rectangle([margin, margin, seal_w - margin, seal_h - margin], radius=24, outline=color, width=10)
# Inner thin border
draw.rounded_rectangle([margin+14, margin+14, seal_w - margin - 14, seal_h - margin - 14], radius=16, outline=color, width=3)

# Fonts
font_path = "C:\\Windows\\Fonts\\kaiu.ttf"
if not os.path.exists(font_path):
    font_path = "C:\\Windows\\Fonts\\msjh.ttc"

font_right = ImageFont.truetype(font_path, 52)
font_left = ImageFont.truetype(font_path, 42)

# Right column: 信天宮 (3 chars)
rx = 185
r_chars = ["信", "天", "宮"]
ry_list = [55, 130, 205]

for char, y in zip(r_chars, ry_list):
    bbox = font_right.getbbox(char)
    cw = bbox[2] - bbox[0]
    draw.text((rx - cw//2, y), char, font=font_right, fill=color)

# Left column: 朱府千歲 (4 chars: 朱, 府, 千, 歲)
lx = 110
l_chars = ["朱", "府", "千", "歲"]
ly_list = [50, 110, 170, 230]

for char, y in zip(l_chars, ly_list):
    bbox = font_left.getbbox(char)
    cw = bbox[2] - bbox[0]
    draw.text((lx - cw//2, y), char, font=font_left, fill=color)

# Add Cloud Ornaments on top-right and bottom-left
draw.arc([seal_w - 65, 20, seal_w - 20, 65], start=180, end=360, fill=color, width=4)
draw.arc([20, seal_h - 65, 65, seal_h - 20], start=0, end=180, fill=color, width=4)

# Text below logo: TAIWANESE TEMPLE CULTURAL & CREATIVE
font_en = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 14)
en_text1 = "TAIWANESE TEMPLE"
en_text2 = "CULTURAL & CREATIVE"

b1 = font_en.getbbox(en_text1)
w1 = b1[2] - b1[0]
draw.text(((seal_w - w1)//2, 272), en_text1, font=font_en, fill=color)

b2 = font_en.getbbox(en_text2)
w2 = b2[2] - b2[0]
draw.text(((seal_w - w2)//2, 290), en_text2, font=font_en, fill=color)

# Save pure transparent logo
transparent_logo_path = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\factory_print_files\Style1_正面_廟宇印章Logo_純圖案去背.png"
seal.save(transparent_logo_path, "PNG", dpi=(300, 300))

# Now composite onto the user's mockup image (media_1787481598483.jpg)
# We cover the old logo area (approx x: 570 to 710, y: 300 to 450)
mockup = Image.open(img_path).convert("RGBA")
mW, mH = mockup.size

# Clean out old logo in mockup by sampling nearby white fabric
# In media_1787481598483.jpg, logo region is around x=560..720, y=300..450
seal_on_mockup = seal.resize((155, 155), Image.Resampling.LANCZOS)

# Create a clean white patch over the old logo
patch = Image.new("RGBA", (170, 170), (255, 255, 255, 255))
mockup.paste(patch, (565, 300))

# Paste the new logo with 朱府千歲
mockup.paste(seal_on_mockup, (572, 305), seal_on_mockup)

# Save updated mockup
final_front_jpg = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\style1_front.jpg"
mockup.convert("RGB").save(final_front_jpg, "JPEG", quality=95)
mockup.convert("RGB").save(r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\style1_front_corrected.jpg", "JPEG", quality=95)

print("Successfully fixed logo in user's mockup to include '朱府千歲' (4 characters)!")
