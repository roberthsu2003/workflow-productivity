# 🌿 工研院綠能所專屬 Skill 實戰（第二階：創作者篇）

> **模組名稱**：綠能專案技術摘要與規格評核專家（ITRI GEL Spec & Tech Evaluator）  
> **所屬階段**：🔵 **第二階：創作者 (Creator)** —— `SKILL.md` + `references/` 規章庫 + `templates/` 標準樣板  
> **適用對象**：工研院綠能所研發團隊、專案審查委員、能源專案經理 (PM) 與合規稽核工程師。  
> **核心技術**：透過掛載專業知識規章（TRL 成熟度、CNS/IEC 法規）與標準報告範本，實現不同研究員產出的技術摘要與審查清單「格式 100% 統一、法規標準零遺漏」。  

---

## 💡 為什麼第二階（references + templates）對綠能科研不可或缺？

工研院執行的專案常涉及數千萬至數億元的國家科研計畫與產學合作：
1. **格式一致性 (Templates)**：每年面對能源署或國科會查核，各分項計畫主持人繳交的技術摘要報告格式五花八門，透過標準樣板（`templates/`）可讓報告品質維持在最高水平。
2. **法規知識庫對照 (References)**：審查外部廠商或自身技術時，必須逐條對照國際巨型風機規範（IEC 61400-1 Class T 抗颱陣風 $\ge 70\text{ m/s}$）或儲能安規（CNS 62933、UL 9540A 延燒防阻），將專家經驗內化至 `references/`。

---

## 📁 實體自訂 Skill 結構

```text
ITRI_Creator/
├── README.md                                  # 本教學指引
├── SKILL.md                                   # 主技能定義檔 (定義雙模式路由與參照 SOP)
├── references/                                # 📚 綠能專業規章與標準庫
│   ├── itri-rd-evaluation-framework.md        # 1. 綠能技術成熟度 (TRL 1~9) 與減碳 KPI 評核指引
│   └── green-energy-safety-standards.md       # 2. 儲能與大型風電核心安全法規對照手冊 (CNS/IEC/UL)
└── templates/                                 # 📄 標準 Markdown 輸出樣板
    ├── tech-summary-report-template.md        # 1. 專案技術摘要與研發效益評估報告範本
    └── compliance-audit-checklist-template.md # 2. 設備規格合規評核與差異清單範本
```

---

## 🛠️ 1 個 Skill 內建 2 大實戰處理模式

本 Skill（`itri-green-energy-spec-evaluator`）具備智慧路由能力，能根據使用者輸入自動切換：

| 處理模式 | 適用情境 | 自動調用知識庫 (`references/`) | 自動套用樣板 (`templates/`) |
| :--- | :--- | :--- | :--- |
| **🔹 模式 A**<br/>**專案技術摘要生成** | 輸入雜亂的風電、儲能研發筆記或成果資料。 | `itri-rd-evaluation-framework.md`<br>（自動對照 TRL 等級與減碳係數計算） | `tech-summary-report-template.md`<br>（輸出標準五大章節報告與 KPI 矩陣） |
| **🔹 模式 B**<br/>**規格合規差異清單** | 輸入外部廠商提送之儲能貨櫃或風機規格書。 | `green-energy-safety-standards.md`<br>（自動對照 CNS 62933、Class T 抗颱標準） | `compliance-audit-checklist-template.md`<br>（輸出結構化合規判定與缺失退件清單） |

---

## 🚀 安裝與使用方式

### 💡 方式 A：使用內建 `/skill-creator` 技能自動建立
1. 將本資料夾內的 `references/` 與 `templates/` 所有檔案上傳至 Claude 對話中。
2. 輸入指令：
   ```text
   我想建立一個名為「工研院綠能專案規格評核專家」的自訂 Skill。
   請參考我上傳的 references 法規規章與 templates 標準樣板，使用 /skill-creator 幫我建立包含 references 與 templates 的第二階自訂技能。
   ```
3. 下載產出的 ZIP 壓縮包，前往 Claude 網頁左下角頭像 ➔ **Settings** ➔ **Skills** ➔ **Add Custom Skill** 上傳即可。

### ✍️ 方式 B：手動打包上傳
將整個 `ITRI_Creator/` 資料夾打包為 ZIP 檔案，於 Claude **Settings** ➔ **Skills** 點擊 **Add Custom Skill** 直接上傳。

---

## 🧪 課堂實戰測試用例

### 📝 測試案例 1：模式 A 實測（風力發電研發技術摘要）

**輸入測試文字：**
```text
請幫我將這段大型離岸風電研發筆記整理成工研院標準技術摘要：
專案名稱：大型離岸風電 15MW 智慧運維與全風場數位分身技術開發。
目前在示範場域已完成連續 1,200 小時實測，轉子直徑 230 米，額定功率 15MW。
透過我們開發的 10kHz 傳動鏈震動監測演算法，把非計畫性停機減少了 38%，機組可用率拉到 97.5%。
預估每年可發電 6,200 萬度電（62 GWh），換算減碳量約 3 萬多噸。目前已經申請 2 件台灣和美國抗颱偏航發明專利。
```

**預期效果：**
- 自動判斷切入 **模式 A**。
- 自動將專案判定為 **TRL 7~8**（示範場域全系統原型運轉）。
- 嚴格套用 `tech-summary-report-template.md` 格式，精準計算減碳量（$62,000,000 \times 0.495 = 30,690$ 噸 $\text{CO}_2\text{e}$），並產出標準量化 KPI 矩陣。

---

### 📝 測試案例 2：模式 B 實測（儲能貨櫃建置規格合規差異審查）

**輸入測試文字：**
```text
某系統廠商送來示範園區 5MW/10MWh 儲能貨櫃規格書，請幫我審核合規性：
1. 電芯規格：磷酸鐵鋰 (LFP)，通過 UL 1973 測試。
2. 延燒防護：廠商說明文件提到電芯密集排列，未附 UL 9540A 機櫃級延燒測試報告，僅表示「電芯本身安全不會延燒」。
3. 防爆洩壓：貨櫃頂部設有通風百葉窗，未配置符合 NFPA 68 的機械式防爆洩壓板。
4. BMS 安全：BMS 軟體具備三段過充警報，但無獨立的硬體級高壓斷路斷電機構。
```

**預期效果：**
- 自動判斷切入 **模式 B**。
- 自動比對 `references/green-energy-safety-standards.md`。
- 產出結構化查核表，抓出「未附 UL 9540A 延燒報告」、「無 NFPA 68 防爆洩壓板」、「缺乏硬體獨立斷電機構」等三大致命重大違規（Major Red Flags），總體評等給予 🔴 **不合格 (Reject) 退件修正**！

---

← [返回第一階：公文與產學信函專家](../ITRI_Imitator/README.md) · [返回 Skills 主指南](../README.md)
