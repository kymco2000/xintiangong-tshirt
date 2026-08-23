import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

img_path = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\.user_uploaded\media_1787481287325.png"
output_path = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\style1_front_fixed.jpg"
output_png_path = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\factory_print_files\Style1_正面_廟宇印章Logo_純圖案去背.png"

# Load original uploaded image
img = Image.open(img_path).convert("RGBA")
w, h = img.size

# We will create a clean high-resolution stamp from scratch or by modifying the original frame to ensure maximum quality!
# Let's inspect the seal color: RGB approx (160, 44, 44) or #A02C2C

# Let's draw high-res seal with PIL
seal_size = 1000
seal_img = Image.new("RGBA", (seal_size, seal_size), (255, 255, 255, 0))
draw = ImageDraw.Draw(seal_img)

seal_color = (160, 44, 44, 255) # Cinnabar Red

# Draw outer rounded square frame (outer border)
margin = 80
rect_outer = [margin, margin, seal_size - margin, seal_size - margin]
draw.rounded_rectangle(rect_outer, radius=60, outline=seal_color, width=28)

# Inner thin border
inner_margin = 125
rect_inner = [inner_margin, inner_margin, seal_size - inner_margin, seal_size - inner_margin]
draw.rounded_rectangle(rect_inner, radius=40, outline=seal_color, width=8)

# Load font (KaiTi 標楷體 or Microsoft JhengHei 微軟正黑體)
font_path = "C:\\Windows\\Fonts\\kaiu.ttf" # 標楷體
if not os.path.exists(font_path):
    font_path = "C:\\Windows\\Fonts\\msjh.ttc"

# Font size for 3 characters (信 天 宮) on the right
font_size_right = 160
font_right = ImageFont.truetype(font_path, font_size_right)

# Font size for 4 characters (朱 府 千 歲) on the left
font_size_left = 135
font_left = ImageFont.truetype(font_path, font_size_left)

# Text positions
# Right column: 信天宮 (x = 580)
right_x = 570
right_chars = ["信", "天", "宮"]
right_y_starts = [180, 400, 620]

for char, y in zip(right_chars, right_y_starts):
    bbox = font_right.getbbox(char)
    char_w = bbox[2] - bbox[0]
    draw.text((right_x - char_w//2, y), char, font=font_right, fill=seal_color)

# Left column: 朱府千歲 (x = 350, 4 characters)
left_x = 340
left_chars = ["朱", "府", "千", "歲"]
left_y_starts = [160, 335, 510, 685]

for char, y in zip(left_chars, left_y_starts):
    bbox = font_left.getbbox(char)
    char_w = bbox[2] - bbox[0]
    draw.text((left_x - char_w//2, y), char, font=font_left, fill=seal_color)

# Add subtle cloud motif in corners or border to match original
# Draw top-right and bottom-left cloud accents
draw.arc([seal_size - 180, 60, seal_size - 60, 180], start=180, end=360, fill=seal_color, width=12)
draw.arc([60, seal_size - 180, 180, seal_size - 60], start=0, end=180, fill=seal_color, width=12)

# Save transparent PNG
seal_img.save(output_png_path, "PNG", dpi=(300, 300))

# Now create a T-shirt mockup background image
bg_img = Image.new("RGBA", (1000, 1000), (245, 245, 245, 255))
# Place stamp on mockup
stamp_small = seal_img.resize((500, 500), Image.Resampling.LANCZOS)
bg_img.paste(stamp_small, (250, 250), stamp_small)
bg_img.convert("RGB").save(output_path, "JPEG", quality=95)

# Also copy transparent PNG & JPG to project root
import shutil
shutil.copyfile(output_path, r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\style1_front.jpg")

print("Fixed logo with '朱府千歲' (4 characters) generated successfully!")
