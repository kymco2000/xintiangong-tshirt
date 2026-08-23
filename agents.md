# 信天宮 朱府千歲紀念服設計（專案藍圖）

> 本檔為跨 Agent 通用的專案藍圖（AGENTS.md 開放標準）。任何 Agent 的每個 session 都應先讀本檔＋`handoff.md`。

## 專案簡介
為「信天宮 朱府千歲」設計紀念款短袖上衣。設計部位包含左胸（低調識別 Logo，10x10cm 內）與背面（遠距辨識卡通神像，30x30cm 內，領下 10cm）。需包含「信天宮」與「朱府千歲」字樣。

## 關鍵時程
- 專案初始化與初稿提案：2026-08-23（完成）
- 使用者確定選用「方案一：台灣廟宇文創風」：2026-08-23（完成）
- 修正左胸 Logo 文字為「朱府千歲」（4 字完整）：2026-08-23（完成）
- 導出 300 DPI 去背檔、兩頁式 PDF 完稿指示書與 GitHub Pages 網站：2026-08-23（完成）

## 目標與路線圖
- [x] 階段一：專案初始化與生成三款初稿概念（Q版、動漫風、徽章風、廟宇文創風）。
- [x] 階段二：根據使用者回饋收斂設計，選定「方案一：台灣廟宇文創風」，修正左胸 Logo 文字「朱府千歲」（4 字補齊）。
- [x] 階段三：輸出高解析度完稿去背圖檔 (300 DPI PNG)、PDF 指示書、網頁發布與手動打包交付。

## 資料夾結構
- `agents.md` (專案藍圖)
- `handoff.md` (跨 Agent 交接檔)
- `index.html` (GitHub Pages 公開展示網頁)
- `pdf_export.html` (PDF 渲染模板)
- `build_pdf.py` (PDF 自動編譯腳本)
- `fix_stamp_logo.py` / `fix_exact_user_logo.py` (印章 Logo 渲染與修復腳本)
- `prepare_factory_files.py` / `refined_crop_transparent.py` (300 DPI 去背圖處理腳本)
- `style1_front.jpg` / `style1_back.jpg` (選定款正反面 Mockup 參考圖)
- `factory_print_files/` (高解析 300 DPI 透明去背檔目錄)
- `factory_print_pack_300dpi.zip` / `信天宮_朱府千歲紀念服_印刷廠完稿去背圖包.zip` (印刷廠完稿打包 ZIP)
- `信天宮_朱府千歲紀念服_三款初稿與完稿指示書.pdf` (兩頁式高畫質 PDF 指示書)

## 同步層級（本專案初始化至第 3 層級）

| 層級 | 平台 | 位置 | 讀取時機 |
|------|------|------|---------|
| L1 | 本地（GDrive） | `agents.md`＋`handoff.md` | 每個 session |
| L2 | GitHub | `https://github.com/kymco2000/xintiangong-tshirt` | 指定時 |
| L3 | Obsidian | `信天宮_朱府千歲_Tshirt/專案工作流程.md` | 有需要時 |

## 工作約定
- 任何 Agent、任何電腦：**開工先讀 `handoff.md`，收工必更新 `handoff.md`**
- 修改共用檔案前先讀最新內容，避免覆蓋其他 Agent 的變更
- 所有回應與文件使用繁體中文
- 修改前先確認計畫，優先保留原有資料結構
