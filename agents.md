# 平面設計 (Graphic Design Studio) - 專案藍圖

> 本檔為跨 Agent 通用的專案藍圖（AGENTS.md 開放標準）。任何 Agent 的每個 session 都應先讀本檔＋`handoff.md`。

## 專案簡介
本專案已升級為全方位**「平面設計 (Graphic Design)」**專業工作站。
目標涵蓋所有平面視覺傳達作品，包括：
- **宣傳品與周邊：** 服飾（T-shirt/外套/帽款）、帆布袋、徽章、紀念品。
- **紙本與數位文宣：** 海報、傳單、摺頁、名片、電子文宣、社群圖卡。
- **大型與實體看板：** 戶外看板、展架、紅布條、燈箱、宮廟牌樓與指標系統。
- **品牌視覺與印章標誌：** Logo 設計、印章/官印設計、字體排版、品牌色彩系統。

---

## 🎨 設計風格與字體系統 (Design Styles & Typography Systems)

為滿足各種不同氛圍與期待，本專案建置多元字體與視覺風格庫：

### 1. 傳統廟宇與東方文創 (Taiwanese Temple & Traditional Oriental)
- **視覺風格：** 宮廟官印、平安符符籤、祥雲錦紋、金石篆刻、朱砂紅/金/靛青配色。
- **字體選擇：** 九疊篆體、隸書、行楷、榜書、標楷體。

### 2. 現代極簡與時尚潮牌 (Modern Minimalist & Streetwear)
- **視覺風格：** 幾何線條、負空間運用、國際主義排版 (Swiss Style)、大膽對比色。
- **字體選擇：** 無襯線體 (Helvetica/Arial/Noto Sans)、黑體、粗體標題。

### 3. 日系簡約與溫暖手感 (Japanese Muji & Handcrafted)
- **視覺風格：** 淡雅留白、大地色系、質感紙紋、手繪線條、溫馨平易近人。
- **字體選擇：** 明體/宋體 (Noto Serif)、手寫楷體、圓體。

### 4. 美式復古與美式潮牌 (Retro American & Vintage Badge)
- **視覺風格：** 徽章構圖 (Badge Emblem)、復古美式字體、美式漫畫/紋身風格。
- **字體選擇：** 復古襯線體、粗厚黑體、手寫美式花體 (Script font)。

---

## 🛠️ 產出技術與標準 (Output Standards)

- **印刷等級輸出：** 300 DPI+ 高解析度 JPEG / PNG 去背透明檔 / Vector 向量 SVG / 印刷廠對位 PDF。
- **實體標註規範：** 提供 1:1 實體尺寸標註與建議印製範圍 (如 10x10cm, 30x30cm, 大型看板比例)。
- **網頁線上預覽：** 自動編譯響應式 HTML 預覽頁面，部署於 GitHub Pages 供公開瀏覽與決策。

---

## 📂 資料夾結構

- `agents.md` (專案藍圖)
- `handoff.md` (跨 Agent 交接檔)
- `index.html` (GitHub Pages 公開展示網頁)
- `Style1_正面_廟宇印章Logo_無英文高畫質獨立圖_4096px_300dpi.jpg` (4096px 高畫質圖檔)
- `factory_print_files/` (300 DPI 透明去背檔目錄)
- `factory_print_pack_300dpi.zip` (印刷廠完稿打包 ZIP)
- `傳統廟印高畫畫JPEG輸出/` (傳統宮廟印章高畫質圖檔目錄)
- `信天宮_朱府千歲紀念服_三款初稿與完稿指示書.pdf` (高畫質 PDF 指示書)

---

## 同步層級（第 3 層級）

| 層級 | 平台 | 位置 | 讀取時機 |
|------|------|------|---------|
| L1 | 本地（GDrive） | `agents.md`＋`handoff.md` | 每個 session |
| L2 | GitHub | `https://github.com/kymco2000/xintiangong-tshirt` | 指定時 |
| L3 | Obsidian | `信天宮_朱府千歲_Tshirt/專案工作流程.md` | 有需要時 |

## 工作約定
- 任何 Agent、任何電腦：**開工先讀 `handoff.md`，收工必更新 `handoff.md`**
- 根據使用者提出的平面設計類別（宣傳品、文宣、看板、Logo 等）靈活切換風格與字體
- 所有回應與文件使用繁體中文
