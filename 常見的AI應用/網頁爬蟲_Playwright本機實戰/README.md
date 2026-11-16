# 🕷️ 本機網頁爬蟲與動態資料蒐集（Desktop AI × Playwright）

> 💡 **為什麼一定要用「桌面版 AI ＋ 本機 Playwright」？**  
> 雲端網頁版 AI（瀏覽器上的 ChatGPT / Claude）受限於官方雲端伺服器 IP 與網路白名單，遇到 **JavaScript 動態渲染、Cloudflare 防爬、公司內網或需要帳密／2FA 登入的網頁** 時往往直接失敗。  
> 唯有使用 **桌面版 AI（Claude Desktop、ChatGPT 桌面版、Antigravity）** 搭配 **本機 Playwright**，才能直接以您自己電腦的網路環境與真實瀏覽器（Chromium）完成自動化爬取、滾動載入、人機協作登入與視覺截圖存證！

---

## 🖥️ 三大桌面版 AI × 本機 Playwright 實作方式

本單元重點不在深入探討協定細節，而是讓您手邊常用的 **3 套桌面版 AI** 都能立刻在本機驅動 **Playwright**：

| 桌面版 AI 工具 | 本機驅動 Playwright 的方式 | 最推薦的實戰用法 |
| :--- | :--- | :--- |
| **Claude Desktop** | 在設定檔加入 `@playwright/mcp@latest`（需本機有 Node.js），或請 Claude 產出 Python Playwright 腳本 | **自然語言即時互動**：說一句話就彈出真實 Chromium 視窗，適合「人機協作手動登入」與即時截圖 |
| **ChatGPT 桌面版** | 搭配 **Work with Apps（連接終端機）** 或產出本機 Python Playwright 腳本一鍵執行 | **批次寫檔與結構化輸出**：讓 ChatGPT 寫好 `playwright` 腳本在本機執行，直接把結果存成 `.csv` / `.xlsx` |
| **Antigravity（桌面版）** | 內建本機終端機與瀏覽器自動化能力，可直接下指令運行 `playwright` 腳本或操作真實網頁 | **全自動工作流整合**：爬完資料直接清洗、分析並接續產出 Word / Excel / PPTX / PDF 報告 |

---

## 🛠️ 本機快速啟動（Python Playwright 通用指令）

無論使用哪一套桌面版 AI，若要讓 AI 直接幫您寫並在本機跑一支可靠的 Playwright 爬蟲，只需先確認電腦已安裝 `uv`（或 Node.js），接著在終端機執行：

```bash
# 1. 首次使用先安裝 Chromium 瀏覽器核心（只需執行一次）
uv run --with playwright playwright install chromium

# 2. 執行 AI 產出的本機爬蟲腳本
uv run --with playwright python scrape_demo.py
```

### 📋 通用本機 Playwright 腳本範例（`scrape_demo.py`）
您可以直接把這段範本貼給 **Claude Desktop / ChatGPT 桌面版 / Antigravity**，請它改成您要抓的目標網站：

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # headless=False 代表「有頭模式」，看得到真實瀏覽器視窗（方便手動登入或除錯）
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rate.bot.com.tw/xrt?Lang=zh-TW", wait_until="networkidle")

    # 範例：截圖存證 + 擷取表格文字
    page.screenshot(path="bot_rate.png", full_page=True)
    rows = page.locator("table tbody tr").all()
    for r in rows[:5]:
        print(r.inner_text().replace("\n", " | "))

    browser.close()
```

> ⚠️ **人機協作登入小技巧（必學）**：  
> 遇到需要帳號密碼、圖形驗證碼或手機簡訊 2FA 的網站時，**務必保持 `headless=False`（有頭模式）**，並在程式中加上 `input("請在瀏覽器完成登入後按 Enter 繼續...")`，由人工安全登入後，再讓 Playwright 接續抓取後台資料！

---

## 📚 跨產業 Playwright 實戰範例庫

以下 3 份實戰範例整理自企業真實應用情境，皆可直接套用於 **Claude Desktop、ChatGPT 桌面版、Antigravity**：

| 產業／情境 | 實戰重點 | 前往查看 |
| :--- | :--- | :--- |
| **🛒 電商與零售比價** | 台灣銀行牌告匯率、momo 動態搜尋比價、競品交叉分析、**人機協作半自動登入查訂單** | [👉 電商實戰範例](./examples/ecommerce.md) |
| **💼 創投（VC）動態調研** | 科技新聞自動彙整、新創官網 JS 滾動載入與**網頁截圖存證**、雙標的橫向對比 | [👉 創投實戰範例](./examples/venture_capital.md) |
| **🌿 綠能與政府公開資訊** | 台電即時電力供需爬取、能源署／氣候變遷署動態公告追蹤、無 API 儀表板截圖存證 | [👉 綠能實戰範例](./examples/green_energy.md) |

---

## 🔗 延伸閱讀：若想了解 Claude Desktop 的設定檔寫法
若您使用的是 **Claude Desktop** 且想透過本地端設定直接以對話驅動瀏覽器，可參考：[Local MCP Servers 安裝配置手冊](../../Claude_ai/Local_MCP/README.md)。

---

[← 返回現代職場 AI 應用全指南](../README.md)
