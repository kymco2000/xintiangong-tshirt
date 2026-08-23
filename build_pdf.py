import fitz  # PyMuPDF
import os

pdf_path = r"g:\我的雲端硬碟\我的第二大腦\信天宮_朱府千歲_Tshirt\信天宮_朱府千歲紀念服_三款初稿與完稿指示書.pdf"

doc = fitz.open()

# Page 1: Header + Spec + Style 1
page1 = doc.new_page(width=595, height=842) # A4 size

# Title
page1.insert_text(fitz.Point(130, 45), "信天宮 朱府千歲紀念服", fontsize=20, fontname="china-s", color=(0.7, 0.16, 0.16))
page1.insert_text(fitz.Point(100, 65), "三款初稿樣式設計提案與印製規格指示書（白色 T-shirt 款）", fontsize=11, fontname="china-s", color=(0.3, 0.3, 0.3))

# Spec summary
page1.draw_rect(fitz.Rect(40, 80, 555, 140), color=(0.7, 0.16, 0.16), fill=(0.98, 0.96, 0.96))
page1.insert_text(fitz.Point(50, 98), "印製位置與尺寸標準規範（參照團體服印製建議）：", fontsize=10, fontname="china-s", color=(0.7, 0.16, 0.16))
page1.insert_text(fitz.Point(60, 115), "1. 正面左胸口：10 * 10 cm 內（可選純文字/方印/徽章 Logo）", fontsize=9, fontname="china-s", color=(0.2, 0.2, 0.2))
page1.insert_text(fitz.Point(60, 130), "2. 背面主視覺：30 * 30 cm 內，領口下方 10 公分置中印製", fontsize=9, fontname="china-s", color=(0.2, 0.2, 0.2))

# Style 1: 台灣廟宇文創風
page1.insert_text(fitz.Point(40, 165), "方案一：台灣廟宇文創風 (Taiwanese Temple Cultural Style)", fontsize=13, fontname="china-s", color=(0.7, 0.16, 0.16))
page1.insert_text(fitz.Point(40, 182), "特色：融合平安符符籤邊框與朱紅官印印章框，展現宮廟文創質感。", fontsize=9, fontname="china-s", color=(0.4, 0.4, 0.4))

img1_front = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_tw_cultural_front_1787474977857.jpg"
img1_back = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_tw_cultural_back_1787474966340.jpg"

if os.path.exists(img1_front):
    page1.insert_image(fitz.Rect(40, 195, 280, 435), filename=img1_front)
    page1.insert_text(fitz.Point(70, 448), "正面左胸 (10x10cm 朱紅印章 Logo)", fontsize=9, fontname="china-s")

if os.path.exists(img1_back):
    page1.insert_image(fitz.Rect(315, 195, 555, 435), filename=img1_back)
    page1.insert_text(fitz.Point(340, 448), "背面領下10cm (30x30cm 平安符主圖)", fontsize=9, fontname="china-s")


# Style 2: 親民 Q 版書法風
page1.insert_text(fitz.Point(40, 480), "方案二：親民 Q 版書法風 (Chibi Calligraphy Style)", fontsize=13, fontname="china-s", color=(0.7, 0.16, 0.16))
page1.insert_text(fitz.Point(40, 497), "特色：Q版神像親切討喜，左胸搭配紅黑雙色書法字體，簡單大方。", fontsize=9, fontname="china-s", color=(0.4, 0.4, 0.4))

img2_front = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_front_text_logo_mockup_1787474913333.jpg"
img2_back = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\zhu_fu_back_mockup_1787474889163.jpg"

if os.path.exists(img2_front):
    page1.insert_image(fitz.Rect(40, 510, 280, 750), filename=img2_front)
    page1.insert_text(fitz.Point(80, 763), "正面左胸 (10x10cm 雙色書法 Logo)", fontsize=9, fontname="china-s")

if os.path.exists(img2_back):
    page1.insert_image(fitz.Rect(315, 510, 555, 750), filename=img2_back)
    page1.insert_text(fitz.Point(345, 763), "背面領下10cm (30x30cm Q版神像主圖)", fontsize=9, fontname="china-s")

page1.insert_text(fitz.Point(200, 810), "第 1 頁 / 共 2 頁", fontsize=8, fontname="china-s", color=(0.5, 0.5, 0.5))


# Page 2: Style 3 + Spec Reference Image
page2 = doc.new_page(width=595, height=842)

# Style 3: 復古圓形徽章風
page2.insert_text(fitz.Point(40, 45), "方案三：復古圓形徽章風 (Classic Temple Badge Style)", fontsize=13, fontname="china-s", color=(0.7, 0.16, 0.16))
page2.insert_text(fitz.Point(40, 62), "特色：幾何圓形宮廟徽章圖騰，金紅雙色流線設計，呈現穩重潮牌風格。", fontsize=9, fontname="china-s", color=(0.4, 0.4, 0.4))

img3_front = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\style3_front_mockup_1787475059210.jpg"
img3_back = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\style3_back_mockup_1787475047242.jpg"

if os.path.exists(img3_front):
    page2.insert_image(fitz.Rect(40, 75, 280, 315), filename=img3_front)
    page2.insert_text(fitz.Point(80, 328), "正面左胸 (10x10cm 圓形宮廟小徽章)", fontsize=9, fontname="china-s")

if os.path.exists(img3_back):
    page2.insert_image(fitz.Rect(315, 75, 555, 315), filename=img3_back)
    page2.insert_text(fitz.Point(345, 328), "背面領下10cm (30x30cm 圓形徽章主圖)", fontsize=9, fontname="china-s")


# Reference Spec Image
page2.insert_text(fitz.Point(40, 360), "附錄：團體服建議印刷位置與對照規格", fontsize=12, fontname="china-s", color=(0.3, 0.3, 0.3))

ref_img = r"C:\Users\user\.gemini\antigravity\brain\35023429-6efa-4654-a276-d87e92da8504\.user_uploaded\media_1787474764298.png"
if os.path.exists(ref_img):
    page2.insert_image(fitz.Rect(125, 380, 470, 760), filename=ref_img)

page2.insert_text(fitz.Point(200, 810), "第 2 頁 / 共 2 頁 | 信天宮 朱府千歲紀念服專案", fontsize=8, fontname="china-s", color=(0.5, 0.5, 0.5))

doc.save(pdf_path)
doc.close()
print("PDF created successfully at:", pdf_path)
