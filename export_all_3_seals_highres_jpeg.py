import os
from PIL import Image, ImageDraw, ImageFont

output_dir = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\傳統廟印高畫畫JPEG輸出"
os.makedirs(output_dir, exist_ok=True)

CANVAS = 4096
RED = (225, 20, 20, 255) # Temple Red #E11414

font_path = r"C:\Windows\Fonts\kaiu.ttf" # 標楷體
if not os.path.exists(font_path):
    font_path = r"C:\Windows\Fonts\msjh.ttc"

# Helper function to create high-res seal image
def create_highres_seal(style_type):
    img = Image.new("RGBA", (CANVAS, CANVAS), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    margin = 300
    mid_y = int(CANVAS * 0.44)
    
    if style_type in ['A', 'B']:
        # Thick outer rounded rectangle
        draw.rounded_rectangle([margin, margin, CANVAS - margin, CANVAS - margin], radius=380, outline=RED, width=190)
        # Horizontal dividing line
        draw.line([margin + 90, mid_y, CANVAS - margin - 90, mid_y], fill=RED, width=95)
        
        font_upper = ImageFont.truetype(font_path, 600)
        font_lower = ImageFont.truetype(font_path, 530)
        
        # Top Row: 信 天 宮 (Right to Left or Left to Right)
        u_chars = ["信", "天", "宮"]
        u_x = [900, 2048, 3196]
        u_y = 660
        for char, x in zip(u_chars, u_x):
            bbox = font_upper.getbbox(char)
            cw = bbox[2] - bbox[0]
            ch = bbox[3] - bbox[1]
            draw.text((x - cw//2, u_y - ch//2), char, font=font_upper, fill=RED)
            
        # Bottom Row: 朱 府 千 歲 (4 chars)
        l_chars = ["朱", "府", "千", "歲"]
        l_x = [780, 1620, 2460, 3300]
        l_y = 2800
        for char, x in zip(l_chars, l_x):
            bbox = font_lower.getbbox(char)
            cw = bbox[2] - bbox[0]
            ch = bbox[3] - bbox[1]
            draw.text((x - cw//2, l_y - ch//2), char, font=font_lower, fill=RED)
            
    elif style_type == 'C':
        # Nine-fold Seal Script (九疊篆滿版款)
        draw.rounded_rectangle([margin, margin, CANVAS - margin, CANVAS - margin], radius=350, outline=RED, width=220)
        font = ImageFont.truetype(font_path, 580)
        
        quads = [
            ("信", 2800, 900),
            ("天", 2800, 1800),
            ("宮", 2800, 2700),
            ("朱", 1300, 750),
            ("府", 1300, 1550),
            ("千", 1300, 2350),
            ("歲", 1300, 3150),
        ]
        
        for char, x, y in quads:
            bbox = font.getbbox(char)
            cw = bbox[2] - bbox[0]
            ch = bbox[3] - bbox[1]
            draw.text((x - cw//2, y - ch//2), char, font=font, fill=RED)
            
    return img

# Generate & Save JPEG for Style A, B, C
styles = [
    ('A', "信天宮_朱府千歲_廟印樣式A_隸書分層款_4096px_300dpi"),
    ('B', "信天宮_朱府千歲_廟印樣式B_行楷分層款_4096px_300dpi"),
    ('C', "信天宮_朱府千歲_廟印樣式C_九疊篆滿版款_4096px_300dpi"),
]

base_tshirt = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_front_mockup_1787474877200.jpg"

for code, name in styles:
    seal_rgba = create_highres_seal(code)
    
    # 1. Independent High-Res White-BG JPEG
    bg_white = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    bg_white.paste(seal_rgba, (0, 0), seal_rgba)
    jpg_path = os.path.join(output_dir, f"{name}.jpg")
    bg_white.save(jpg_path, "JPEG", quality=100, dpi=(300, 300))
    # Copy to project root
    bg_white.save(os.path.join(r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt", f"{name}.jpg"), "JPEG", quality=100, dpi=(300, 300))
    print(f"Generated standalone JPEG: {jpg_path}")
    
    # 2. Transparent PNG for Print Factory
    png_path = os.path.join(output_dir, f"{name}.png")
    seal_rgba.save(png_path, "PNG", dpi=(300, 300))
    
    # 3. High-Res T-Shirt Mockup JPEG
    if os.path.exists(base_tshirt):
        tshirt = Image.open(base_tshirt).convert("RGBA")
        seal_resized = seal_rgba.resize((180, 180), Image.Resampling.LANCZOS)
        tshirt.paste(seal_resized, (565, 310), seal_resized)
        
        mockup_jpg_path = os.path.join(output_dir, f"T恤示範_{name}.jpg")
        tshirt.convert("RGB").save(mockup_jpg_path, "JPEG", quality=98)
        tshirt.convert("RGB").save(os.path.join(r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt", f"T恤示範_{name}.jpg"), "JPEG", quality=98)
        print(f"Generated T-shirt mockup JPEG: {mockup_jpg_path}")

print("All 3 Traditional Temple Seal High-Res JPEGs Generated Successfully!")
