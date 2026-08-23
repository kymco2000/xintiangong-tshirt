from PIL import Image
import os

base_tshirt = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_front_mockup_1787474877200.jpg"
seal_dir = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\temple_seals_reference"
output_dir = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt"

seals = [
    ("廟印範例_A_隸書分層款.png", "tshirt_mockup_seal_lishu.jpg"),
    ("廟印範例_B_行楷分層款.png", "tshirt_mockup_seal_xingshu.jpg"),
    ("廟印範例_C_九疊篆滿版款.png", "tshirt_mockup_seal_zhuan.jpg"),
]

for png_name, out_jpg_name in seals:
    png_path = os.path.join(seal_dir, png_name)
    if os.path.exists(png_path) and os.path.exists(base_tshirt):
        tshirt = Image.open(base_tshirt).convert("RGBA")
        seal = Image.open(png_path).convert("RGBA")
        
        # Resize to chest size
        seal_resized = seal.resize((175, 175), Image.Resampling.LANCZOS)
        
        # Paste on left chest
        tshirt.paste(seal_resized, (565, 310), seal_resized)
        
        out_p = os.path.join(output_dir, out_jpg_name)
        tshirt.convert("RGB").save(out_p, "JPEG", quality=95)
        print(f"Created mockup: {out_p}")
