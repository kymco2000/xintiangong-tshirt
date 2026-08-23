# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
已完成「信天宮 朱府千歲紀念服」全套設計、印刷完稿及打包工作。
1. 使用者最終確定選用：**「方案一：台灣廟宇文創風」**（平安符邊框背圖 30x30cm 領下 10cm + 朱紅官印印章框 10x10cm 左胸 Logo）。
2. 已修復左胸 Logo 缺字問題，正確顯示 **「朱府千歲」**（4 字完整）與 **「信天宮」**（3 字）。
3. 已發布 GitHub Pages 線上公開展覽網頁、匯出 300 DPI 透明去背圖包 ZIP、產生兩頁式標準 PDF 完稿說明書。
4. 本次進行完整專案打包交接，方便下一個 Agent 接手。

## 🚦 目前狀態
原始方案一的背面與交付包維持可交印；左胸 Logo 已新增數款官印滿版候選，尚待使用者選定後才更新印刷包、PDF 與網站。
- 線上網頁：`https://kymco2000.github.io/xintiangong-tshirt/`
- GitHub Repo: `https://github.com/kymco2000/xintiangong-tshirt`
- ZIP 圖包：`factory_print_pack_300dpi.zip`

## 🆕 本次收工更新（2026-08-23）
1. 新增左胸 10x10cm、300 DPI、RGBA 去背的官印候選圖，保留每個版本以供比對：
   - `Style1_正面_廟宇印章Logo_朱府千歲四字等高_10x10cm_300dpi_去背.png`
   - `Style1_正面_廟宇印章Logo_朱府千歲四字飽滿版_10x10cm_300dpi_去背.png`
   - `Style1_正面_廟宇印章Logo_朱府千歲四字全滿版_10x10cm_300dpi_去背.png`
   - `Style1_正面_廟宇印章Logo_朱府千歲官印滿框版_10x10cm_300dpi_去背.png`
   - `Style1_正面_廟宇印章Logo_朱府千歲古風官印版_10x10cm_300dpi_去背.png`
   - `Style1_正面_廟宇印章Logo_朱府千歲宋體古印滿版_10x10cm_300dpi_去背.png`
2. 新增第一款背面獨立 JPG：`Style1_背面_平安符朱府千歲_獨立圖_4096px_300dpi.jpg`（4096x5624、300 DPI、白底）。它由 512x703 原圖高品質放大，不是重新繪製的原生高解析圖。
3. 可重製腳本：`render_front_logo_equal_height.py`、`export_back_jpg.py`；對應驗證：`test_render_front_logo_equal_height.py`、`test_export_back_jpg.py`。

## ➡️ 下一步（若新 Agent 接手可做的事）
1. 請使用者選定左胸 Logo 候選版；選定後再將該檔更新進 `factory_print_pack_300dpi.zip`、PDF 與 GitHub Pages，並重新驗證。
2. 若使用者要進行實體團體服打樣，可先使用原始 `factory_print_pack_300dpi.zip`；它尚未包含本次候選 Logo。
3. 若使用者後續需要新增黑底 T-shirt 版本或袖口圖騰設計，可基於 `factory_print_files/` 內的去背圖檔直接延伸編譯。

## ⚠️ 注意事項
- 左胸 Logo 印章檔在 `factory_print_files/Style1_正面_廟宇印章Logo_純圖案去背.png` 已做高解析去背處理，包含完整「朱府千歲」四字。
- 本次新增候選版均為 1181x1181、300 DPI；尚未取代原交付包中的既有印章檔。

## 🕐 最後更新
- 時間：2026-08-23 19:10
- 更新者：Codex @ GDrive
- Git push：✅ 已推至 `origin/master`（commit `4e7892e`）
