from PIL import Image
import os

tshirt_base_path = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_front_mockup_1787474877200.jpg"
seal_logo_path = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\factory_print_files\Style1_正面_廟宇印章Logo_純圖案去背.png"
output_mockup_path = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\style1_front.jpg"

if os.path.exists(tshirt_base_path) and os.path.exists(seal_logo_path):
    tshirt = Image.open(tshirt_base_path).convert("RGBA")
    logo = Image.open(seal_logo_path).convert("RGBA")
    
    # Resize logo to fit left chest area (approx 180x180 px on a 1000x1000 mockup)
    logo_resized = logo.resize((180, 180), Image.Resampling.LANCZOS)
    
    # Position on left chest (approx x=580, y=320 on the right side of image / left chest of person)
    # Note: On a T-shirt flat lay, wearer's left chest is on the viewer's right!
    tshirt.paste(logo_resized, (560, 310), logo_resized)
    
    tshirt.convert("RGB").save(output_mockup_path, "JPEG", quality=95)
    print("Composited corrected logo onto T-shirt mockup successfully!")
