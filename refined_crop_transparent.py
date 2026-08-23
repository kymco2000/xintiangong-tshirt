import os
import cv2
import numpy as np
from PIL import Image

output_dir = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\factory_print_files"
os.makedirs(output_dir, exist_ok=True)

# Helper 1: Isolate pure artwork by color masking & auto bounding box
def extract_pure_logo(img_path, save_path, crop_box=None, is_text_only=False):
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        return
    
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    
    # If crop_box is provided (ymin, ymax, xmin, xmax in percentages)
    h, w, _ = img.shape
    if crop_box:
        ymin, ymax, xmin, xmax = crop_box
        img = img[int(h*ymin):int(h*ymax), int(w*xmin):int(w*xmax)]
    
    # Convert to RGBA
    img_rgba = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    
    # Convert white / off-white background (t-shirt fabric / white background) to transparent
    # Gray scale thresholding
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    if is_text_only:
        # For text (red/black), anything bright white/greyish white is background
        mask = gray > 210
    else:
        # For graphics, white background
        mask = (img[:, :, 0] > 230) & (img[:, :, 1] > 230) & (img[:, :, 2] > 230)
    
    img_rgba[mask, 3] = 0  # Set alpha to 0 for background
    
    # Auto-crop to content bounding box
    alpha = img_rgba[:, :, 3]
    coords = cv2.findNonZero(alpha)
    if coords is not None:
        x, y, bw, bh = cv2.boundingRect(coords)
        # Add slight 5px padding
        x = max(0, x - 5)
        y = max(0, y - 5)
        bw = min(img_rgba.shape[1] - x, bw + 10)
        bh = min(img_rgba.shape[0] - y, bh + 10)
        img_rgba = img_rgba[y:y+bh, x:x+bw]
    
    # Save high-res PNG
    pil_img = Image.fromarray(cv2.cvtColor(img_rgba, cv2.COLOR_BGRA2RGBA))
    pil_img.save(save_path, "PNG", dpi=(300, 300))
    print(f"Successfully created clean PNG: {save_path} (Size: {pil_img.size})")

# 1. Style 1 Front: Red Seal Stamp Logo
src_s1_front = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_tw_cultural_front_1787474977857.jpg"
dst_s1_front = os.path.join(output_dir, "Style1_正面_廟宇印章Logo_純圖案去背.png")
extract_pure_logo(src_s1_front, dst_s1_front, crop_box=(0.25, 0.45, 0.55, 0.75))

# 2. Style 1 Back: Talisman Deity Artwork
src_s1_back = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_tw_cultural_back_1787474966340.jpg"
dst_s1_back = os.path.join(output_dir, "Style1_背面_平安符朱府千歲_純圖案去背.png")
extract_pure_logo(src_s1_back, dst_s1_back, crop_box=(0.15, 0.85, 0.25, 0.75))

# 3. Style 2 Front: Calligraphy Text Logo
src_s2_front = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_front_text_logo_mockup_1787474913333.jpg"
dst_s2_front = os.path.join(output_dir, "Style2_正面_雙色書法文字Logo_純圖案去背.png")
extract_pure_logo(src_s2_front, dst_s2_front, crop_box=(0.25, 0.45, 0.50, 0.75), is_text_only=True)

# 4. Style 2 Back: Chibi Mascot Deity
src_s2_back = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_chibi_mascot_1787474502891.jpg"
dst_s2_back = os.path.join(output_dir, "Style2_背面_Q版朱府千歲神像_純圖案去背.png")
extract_pure_logo(src_s2_back, dst_s2_back)

# 5. Style 3 Front: Circular Temple Badge Logo
src_s3_front = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\style3_front_mockup_1787475059210.jpg"
dst_s3_front = os.path.join(output_dir, "Style3_正面_宮廟圓形小徽章Logo_純圖案去背.png")
extract_pure_logo(src_s3_front, dst_s3_front, crop_box=(0.28, 0.48, 0.52, 0.72))

# 6. Style 3 Back: Vector Circular Badge Artwork
src_s3_back = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_vector_badge_1787474523786.jpg"
dst_s3_back = os.path.join(output_dir, "Style3_背面_宮廟圓形徽章主視覺_純圖案去背.png")
extract_pure_logo(src_s3_back, dst_s3_back)

# Re-zip
import zipfile
zip_path = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\factory_print_pack_300dpi.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            full_p = os.path.join(root, file)
            rel_p = os.path.relpath(full_p, output_dir)
            zipf.write(full_p, arcname=rel_p)

# Also copy to original user requested path
user_zip_path = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\信天宮_朱府千歲紀念服_印刷廠完稿去背圖包.zip"
import shutil
shutil.copyfile(zip_path, user_zip_path)

print("All pure logo transparent files packaged into ZIP:", zip_path)
