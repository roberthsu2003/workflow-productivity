# 📚 創投 (VC) 財務評估指標與計算公式指南 (Financial Metrics Guide)

本文件提供創投分析師與盡調團隊在評估新創公司（尤其是 SaaS、訂閱制與成長型企業）財務報表時的黃金指標、計算公式與異常警訊判讀標準。

---

## 1. 核心財務與營運指標 (Core Metrics)

### 📊 Cash Runway & Burn Rate (現金續航力與燒錢率)
* **Gross Burn Rate (總燒錢率)**：每月總營業費用 (Total OpEx)。
  $$\text{Gross Burn} = \text{R\&D} + \text{S\&M} + \text{G\&A}$$
* **Net Burn Rate (淨燒錢率)**：每月現金流出減去營收現金流入。
  $$\text{Net Burn} = \text{Total OpEx} - \text{Gross Profit}$$
* **Cash Runway (現金可營運月數)**：
  $$\text{Runway (Months)} = \frac{\text{Current Cash Balance}}{\text{Monthly Net Burn}}$$
* **VC 警訊標準**：
  * 🔴 **Runway < 6 個月**：極高風險，隨時面臨現金流斷裂，需立即籌資或大幅裁員縮減 Burn。
  * 🟡 **Runway 6–12 個月**：中度警訊，應啟動下一輪募資 SOP 或縮減行銷預算。
  * 🟢 **Runway > 18 個月**：健康狀態，具備足夠的營運與研發緩衝空間。

---

### 📈 SaaS & 訂閱制核心指標 (SaaS Metrics)

1. **ARR / MRR (年度/月度可重複性營收)**
   * $\text{ARR} = \text{MRR} \times 12$
   * **MoM Growth Rate (月成長率)**：$\frac{\text{MRR}_{\text{t}} - \text{MRR}_{\text{t-1}}}{\text{MRR}_{\text{t-1}}} \times 100\%$

2. **Net Dollar Retention (NDR / 淨營收留存率)**
   $$\text{NDR} = \frac{\text{Starting MRR} + \text{Expansion} - \text{Contraction} - \text{Churn}}{\text{Starting MRR}} \times 100\%$$
   * 🟢 **NDR > 120%**：頂尖級 (Sequoia / Benchmark 標準)，代表舊客戶持續加購。
   * 🟡 **NDR 100%–110%**：及格水準。
   * 🔴 **NDR < 90%**：高客戶流失或續約衰退風險。

3. **LTV / CAC (客戶終身價值與獲客成本比)**
   $$\text{LTV} = \frac{\text{ARPU} \times \text{Gross Margin \%}}{\text{Monthly Churn Rate}}$$
   * 🟢 **LTV / CAC > 3.0x**：健康獲客模式。
   * 🔴 **LTV / CAC < 1.5x**：獲客效率過低，買流量不划算。

4. **Rule of 40 (四十法則)**
   $$\text{Rule of 40} = \text{Revenue Growth Rate (\%)} + \text{EBITDA Margin (\%)}$$
   * 🟢 **> 40%**：極佳的成長與盈利平衡。

---

## 2. 財務報表異常與 Red Flag 警訊庫 (Red Flag Audit Checklist)

| 異常類型 | 判讀特徵 | 創投風險與對策 |
| :--- | :--- | :--- |
| **毛利率急遽下滑** | Gross Margin 低於同業標準 15% 以上（例如 SaaS < 60%） | 可能隱藏高額委外人工或伺服器成本被錯歸類在 COGS |
| **S&M 爆增但 MRR 停滯** | 行銷費用 MoM 成長 > 30%，但新進客戶數 MoM < 5% | 渠道投放失效、CAC 過高或 Market Fit 發生劇變 |
| **應收帳款 (A/R) 天數過長** | DSO (Days Sales Outstanding) > 90 天 | 客戶付款意願低、做假帳/先記帳未收款疑慮 |
| **研發資本化 (Capitalized R&D)** | 將工程師薪資大幅轉列資產而非 OpEx | 虛報 EBITDA，掩蓋真實 Net Burn Rate |

---

## 3. 財務分析模式與選擇邏輯 (Analysis Modes)

當 Skill 上傳 Excel 檔案後，應依據工作表內容與數據特徵，向使用者推薦以下分析選單：

- **模式 1：財務健康度與 Runway 深度診斷** (焦點：Cash Balance, Net Burn, Runway, Breakeven Analysis)
- **模式 2：營收與成本成長趨勢分析** (焦點：MRR Growth, Gross Margin, OpEx Structure)
- **模式 3：SaaS Unit Economics 與客戶動態分析** (焦點：ARPU, Churn Rate, NDR, LTV/CAC)
- **模式 4：財務異常與風險預警 (Red Flags Audit)** (焦點：費用異常、毛利衰退、現金流拐點)
- **模式 5：綜合全方位 IC 財務盡調簡報** (涵蓋上述 1-4 面向之全覽式報告)
