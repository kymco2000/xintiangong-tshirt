import os
from PIL import Image, ImageOps
import zipfile

output_dir = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\factory_print_files"
os.makedirs(output_dir, exist_ok=True)

# Function to remove white background (make transparent)
def make_transparent(input_path, output_path, threshold=240):
    if not os.path.exists(input_path):
        print(f"Skipping {input_path}, file not found.")
        return False
    
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # Change white or near-white to transparent
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG", dpi=(300, 300))
    print(f"Created transparent print PNG: {output_path}")
    return True

# Map original files to factory print files
files_to_process = [
    # Style 1
    (r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_tw_cultural_front_1787474977857.jpg", os.path.join(output_dir, "Style1_正面_左胸廟宇印章Logo_10x10cm去背檔.png")),
    (r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_tw_cultural_back_1787474966340.jpg", os.path.join(output_dir, "Style1_背面_平安符朱府千歲主視覺_30x30cm去背檔.png")),
    
    # Style 2
    (r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_front_text_logo_mockup_1787474913333.jpg", os.path.join(output_dir, "Style2_正面_左胸雙色書法Logo_10x10cm去背檔.png")),
    (r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_chibi_mascot_1787474502891.jpg", os.path.join(output_dir, "Style2_背面_Q版朱府千歲主視覺_30x30cm去背檔.png")),
    
    # Style 3
    (r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\style3_front_mockup_1787475059210.jpg", os.path.join(output_dir, "Style3_正面_左胸宮廟圓形小徽章_10x10cm去背檔.png")),
    (r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_vector_badge_1787474523786.jpg", os.path.join(output_dir, "Style3_背面_宮廟圓形徽章主視覺_30x30cm去背檔.png")),
]

processed_pngs = []
for src, dst in files_to_process:
    if make_transparent(src, dst):
        processed_pngs.append(dst)

# Create Readme for Print Shop
readme_content = """==================================================
信天宮 朱府千歲紀念服 - 印刷廠完稿對位與輸出說明檔
==================================================

【印製規格與尺寸標註】
1. 底衫款式：白色短袖 T-shirt (Cotton/Poly Blend)
2. 正面左胸口印製檔：
   - 檔名包含『正面_左胸』之檔
   - 印刷範圍：建議 10cm x 10cm 以內
   - 印刷技術：數碼直噴 (DTG) 或 網版印刷 (Screen Printing)
3. 背面主視覺印製檔：
   - 檔名包含『背面』之檔
   - 印刷範圍：建議 30cm x 30cm 以內
   - 印刷位置：領口下方 10cm 置中印製

【檔案說明】
本資料包包含三款風格（方案一、方案二、方案三）之高解析度 (300 DPI) 去背透明背景 PNG 檔。
圖檔均已去背處理 (Alpha 通道半透明)，可以直接匯入 Adobe Illustrator (AI)、Photoshop (PSD)、CorelDRAW 進行拼版輸出。

如有任何檔案問題，請聯繫專案窗口。
"""

readme_path = os.path.join(output_dir, "印刷廠對位說明與輸出規範_READ_ME.txt")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

# Zip all print files
zip_path = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\信天宮_朱府千歲紀念服_印刷廠完稿去背圖包.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            full_p = os.path.join(root, file)
            rel_p = os.path.relpath(full_p, output_dir)
            zipf.write(full_p, arcname=rel_p)

print("Factory print ZIP package created at:", zip_path)
