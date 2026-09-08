# 範例三：工程師的開發助手 —— Python 邏輯函數與單元測試 (Python)

> 🔵 **難易度**：Level 2 進階應用  
> 🎯 **產出格式**：獨立 Python 程式碼檔案 Artifact  
> 👥 **適合對象**：軟體工程師、資料分析師、自動化測試同仁  

---

## 📌 任務背景

開發團隊需要實作一個計算 Fibonacci 數列並支援記憶化快取（Memoization）的高效函數。程式碼必須符合 PEP 8 風格規範、包含完備的 Google 風格 Docstring、邊界條件處理以及單元測試範例，並能隨技術主管的反饋重構為生成器（Generator）。

---

## 📋 RTCCF Prompt（複製後直接貼給 Claude）

```markdown
## Role
你是一位嚴格遵守 PEP 8 規範、高度重視執行效能與程式碼可讀性的資深 Python 架構師。

## Task
撰寫一個 Python 函數，計算指定上限值以內的所有費波那契數列（Fibonacci sequence）。需包含完整的 Docstring、型別標註（Type Hints）、以及使用範例與預期輸出。

## Context
- 函數名稱：`get_fibonacci_sequence(limit: int) -> list[int]`
- 效能考量：需支援大量計算，避免低效遞迴
- 邊界條件：當輸入為 0、負數或非整數時，需主動拋出 ValueError 並給出清楚提示

## Constraint
- 嚴格遵守 PEP 8 規範，使用 snake_case 命名
- 撰寫標準 Google 風格 Docstring（說明 Args, Returns, Raises）
- 僅使用 Python 標準函式庫，不依賴第三方套件

## Format
- 產出為 **Python 程式碼格式的 Artifact**，便於一鍵複製或直接下載
```

---

## 🔄 實戰演練：Tech Lead 代碼審查反饋（V2 迭代）

```markdown
Tech Lead 審查後提出以下優化需求：
1. 為避免在數值極大時佔用過多記憶體，請將列表改為 Python Generator（yield）。
2. 在程式碼底部加入 `unittest` 測試案例類別，涵蓋正常測試與負數異常捕獲。
請直接在原本的 Artifact 檔案上更新。
```

> 🎯 **成果觀察**：  
> 代碼在右側面板即時就地重構為 Version 2，可點擊「Copy」直接貼進 IDE 進行測試。

---

← [返回 Artifacts 主手冊](../../README.md)
