# 💼 創投 (VC) 專屬 Skill 實戰（第二階：創作者篇）

> 🟢 **方案需求**：Free / Pro 方案皆適用  
> 💼 **適用對象**：創投分析師 (VC Analyst / Associate)、投資經理 (Investment Manager) 與法務/財務盡調人員。  
> 🎓 **核心技術**：展示 **「第二階：創作者 (Creator)」** 技巧 —— 如何結合 **`references/` 專業知識規章** 與 **`templates/` 標準 Markdown 輸出範本**，打造合乎創投機構規範的自動化 Agent Skill。

---

## 💡 為什麼第二階（references + templates）對創投極度重要？

創投日常處理的法律、財務與決議文件具有極高的專業度與規範要求：
1. **規範一致性 (Templates)**：不同分析師產出的 IC 投資備忘錄或 Term Sheet Risk Check 格式必須統一，便於投資委員會審查。
2. **知識規章對照 (References)**：分析師需對照 SaaS 財務黃金指標（LTV/CAC > 3, NDR > 110%）或法務清算條款（1x Non-participating vs Full Ratchet），將創投專業 SOP 內化至 Skill 中。

---

## 📁 創投 Level 2 Skill 實體目錄結構

```text
VC_Creator/
├── README.md                              # 本教學說明文件
├── SKILL.md                               # 主 Skill 檔 (定義 SOP 與引用規則)
├── references/                            # 📚 創投專業參考知識庫
│   ├── vc-evaluation-framework.md        # 1. SaaS 財務指標與 TAM/SAM/SOM 評估規章
│   ├── term-sheet-glossary.md            # 2. Term Sheet 條款與風險評級 (Red Flags) 檢核指南
│   └── pitch-deck-checklist.md           # 3. 國際 Top VC (Sequoia/YC) 簡報 10 大要素標準
└── templates/                             # 📄 標準 Markdown 輸出樣板
    ├── investment-memo-template.md        # 1. IC 委員會標準投資備忘錄範本
    ├── term-sheet-summary-template.md     # 2. Term Sheet 條款與風險檢核報告範本
    └── deck-review-report-template.md     # 3. Pitch Deck 簡報評估與創辦人提問單範本
```

---

## 🛠️ 3 大創投實戰範例型態

### 範例 1：IC 委員會標準投資備忘錄生成助手 (Investment Memo Generator)
- **應用場景**：分析師剛與新創創辦人開完會，手邊有雜亂的對話紀錄與財務簡報文字，需快速產出標準格式的投資備忘錄。
- **調用資源**：
  - 參考 `references/vc-evaluation-framework.md` 自動對照 LTV/CAC、NDR、Burn Multiple 等指標。
  - 套用 `templates/investment-memo-template.md` 產出帶有風險評估與創辦人提問單的簡報備忘錄。

### 範例 2：Term Sheet 條款檢核與風險評級助手 (Term Sheet Risk Checker)
- **應用場景**：收到新創或對手創投提出的 Term Sheet 草案，需快速分析是否有對創投或創辦人不利的極端條款。
- **調用資源**：
  - 參考 `references/term-sheet-glossary.md` 對照清算優先權 (Liquidation Preference)、反稀釋 (Anti-dilution) 等條款。
  - 套用 `templates/term-sheet-summary-template.md` 自動標示 🟢 綠燈、🟡 黃燈與 🔴 紅燈風險警訊。

### 範例 3：Pitch Deck 簡報審查與創辦人提問單生成器 (Pitch Deck Auditor)
- **應用場景**：初審大量的商業計畫書 (Pitch Deck)，快速評估簡報是否缺漏關鍵 Slide，並列出 IC 會議要問創辦人的 3 個關鍵問題。
- **調用資源**：
  - 參考 `references/pitch-deck-checklist.md` (Sequoia / YC 10 大簡報要素)。
  - 套用 `templates/deck-review-report-template.md` 輸出完整度打分表。

---

## 🧪 實戰測試：可直接複製的測試文字 (Test Prompts)

成功安裝此 Skill 後，您可以複製以下文字在對話中測試其效果：

### 🧪 測試 Prompt A：生成投資備忘錄 (Memo)
```text
請幫我將以下新創訪談筆記整理成標準 IC 投資備忘錄：

公司名稱：AI-Vision Tech (智視科技)
創辦人：CEO 綠川博士 (前台積電資深 AI 專家)，CTO 張大衛 (Stanford 博士)
產品：專注於半導體 AOI 缺陷檢測的 AI 模型，能降低 80% 的誤報率。
財務與營運狀況：
- 現有 ARR：$1.2M 美金
- 去年 LTV/CAC 比率為 4.2，Net Dollar Retention (NDR) 高達 125%
- 目前月燒錢 $80,000 美金，手上現金還能撐 14 個月
- 本輪計畫募資 $3.0M 美金（Series A），投前估值 $12M 美金。
- 主要競品：以色列 K 科技、美商 C 公司
```

### 🧪 測試 Prompt B：Term Sheet 條款風險檢核 (Term Sheet Check)
```text
請幫我檢核以下這份 Term Sheet 條款草案是否有高風險 (Red Flag) 項目：

專案名稱：CloudSaaS Taiwan
投資金額：$1.5M 美金，投前估值 $6.0M 美金。
條款細節：
1. 期權池：要求在投前設立 20% 的 ESOP 期權池。
2. 清算優先權：2x Participating Preferred (領取 2 倍優先清算後，繼續參與剩餘分配)。
3. 反稀釋條款：Full Ratchet (完全棘輪條款)。
4. 董事會：共 5 席，創投方佔 3 席。
```

---

## 🛠️ 安裝與部署方式

1. **手動安裝 (Claude Web)**：
   - 下載本資料夾（包含 `SKILL.md`、`references/` 與 `templates/`）。
   - 前往 Claude 網頁左下角 **Settings** ➔ **Skills** ➔ **Add Custom Skill** 上傳此資料夾。
2. **終端機部署 (Claude Code)**：
   ```bash
   cp -r VC_Creator/ ~/.claude/skills/VC_Creator
   ```

---

← [返回 Skills 主頁](../README.md) | [返回專案首頁](../../README.md)
