from PIL import Image
import os

# Paths
tshirt_base_path = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_front_mockup_1787474877200.jpg"
logo_png_path = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\factory_print_files\Style1_正面_廟宇印章Logo_純圖案去背.png"

# Update style1_front.jpg and style1_front.png for web/PDF
mockup = Image.open(tshirt_base_path).convert("RGBA")
logo = Image.open(logo_png_path).convert("RGBA")

# Resize logo to fit left chest
logo_resized = logo.resize((175, 175), Image.Resampling.LANCZOS)

# Paste on viewer's right (wearer's left chest)
mockup.paste(logo_resized, (565, 310), logo_resized)

out_mockup_jpg = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\style1_front.jpg"
mockup.convert("RGB").save(out_mockup_jpg, "JPEG", quality=95)

print("Updated style1_front.jpg with logo without English text!")
