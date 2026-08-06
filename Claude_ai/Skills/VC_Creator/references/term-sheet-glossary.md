# 創投 Term Sheet 條款與風險檢核指南

本文件為 Term Sheet（投資意向書/條款清單）條款檢核指南，供 Claude 進行法務條款比對與風險提示時參考。

## ⚖️ 1. 核心估值與投資架構條款

- **Pre-money Valuation (投前估值) vs Post-money Valuation (投後估值)**：
  - 公式：`Post-money Valuation = Pre-money Valuation + Investment Amount`
  - *風險提示*：需確認 ESOP (員工期權池) 是計入 Pre-money（由原股東稀釋）或是 Post-money。

- **Option Pool (期權池/ESOP)**：
  - 創投通常要求設立 10% ~ 15% 的期權池。
  - *風險提示*：若要求在 Pre-money 設立過大的期權池，會大幅拉低創辦團隊的實質投前估值。

---

## 🛡️ 2. 創投權益保護條款 (Investor Rights & Protection)

| 條款名稱 | 英文名稱 | 標準市場規範 (Standard) | 需注意之高風險條款 (Red Flags) |
| :--- | :--- | :--- | :--- |
| **清算優先權** | Liquidation Preference | **1x Non-Participating** Preferred (優先清算 1 倍後轉普通股比率) | **> 2x** 或 **Participating Preferred** (雙重拿錢：先拿清算倍數，再參與剩餘分配)。 |
| **反稀釋條款** | Anti-dilution | **Broad-based Weighted Average** (加權平均反稀釋) | **Full Ratchet** (完全棘輪條款：不論發行股數多少，直接降至最低發行價，對創辦人極度不利)。 |
| **優先購買權** | Right of First Refusal (ROFR) | 股東欲轉讓股權時，現有 VC 股東有優先購買權。 | 限制過於嚴苛，導致創辦人受限制無法處分個人資產。 |
| **隨賣權 / 帶隨權** | Tag-Along (Co-Sale) / Drag-Along | Tag-Along 保護小股東隨大股東出售；Drag-Along 強制小股東跟隨多數股東出售公司。 | Drag-Along 的門檻過低（如低於 50% 或無需創辦人同意即可出售公司）。 |
| **董事會席次** | Board of Directors | 早期階段（Seed / Series A）常見 3~5 席（創辦人保持控制權）。 | VC 在早期要求過半董事席次或具備過度否決權 (Veto Rights)。 |

---

## 🔍 3. 條款風險等級評估機制

- 🟢 **綠燈 (Standard Market Terms)**：符合 1x Non-Participating, Broad-based Weighted Average，董事會席次合理。
- 🟡 **黃燈 (Negotiable Terms)**：ESOP 超過 15%、高於市場水準的否決權事項。
- 🔴 **紅燈 (High Risk / Red Flag)**：> 2x 清算優先權、Participating Preferred、Full Ratchet 反稀釋、Drag-Along 無創辦人同意條款。
