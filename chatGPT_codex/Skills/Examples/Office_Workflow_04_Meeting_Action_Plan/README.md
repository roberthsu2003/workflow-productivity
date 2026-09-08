# 延伸練習 04：會議行動計畫（第二階：創作者）

> 🔵 **方案需求**：Spreadsheets plugin 需 Plus 起。

---

## 🛠️ 安裝與測試

```bash
cp -r Office_Workflow_04_Meeting_Action_Plan ~/.agents/skills/meeting-action-plan
```

用 [GWorkspace 的會議手記](../../GWorkspace/03_Docs_Meeting_Notes/sample_files/2026_Q3營運檢討會_會議手記.docx)測試：

```text
$meeting-action-plan

請處理 Skills/GWorkspace/03_Docs_Meeting_Notes/sample_files/2026_Q3營運檢討會_會議手記.docx
```

---

## 📝 預期結果

### 行動計畫（3 項）

| 項目 | 負責人 | 期限 | 相依於 |
| :--- | :--- | :--- | :--- |
| 鼎和賠償案結案時程 | 慧玲 | 本週五 | 法務審閱 |
| 南區冷藏配送時段確認 | 柏宇 | 週四 | 倉庫出貨時間 |
| 雙 11 彈性人力定案 | 文豪 | 10/15 | — |

### 待確認（至少 2 項）

| 事項 | 缺什麼 | 該問誰 |
| :--- | :--- | :--- |
| 冷鏈車採購時程 | **期限**（「採購在跑但沒給時間」） | 維倫 |
| 東區扣除颱風的準時率 | 數字未確認 | 以樂 |

### 不是行動項目

- 「建議先確認車輛再談合約」→ 只是提議，**沒有拍板**

---

## ✅ 驗收

- [ ] 「冷鏈車採購」歸入待確認，**沒有自己填期限**
- [ ] 「東區 96%」沒有被當成事實寫進表格
- [ ] 每一項都有「出處」引用
- [ ] 有列出「不是行動項目」的內容
- [ ] 範本未被修改

> [!IMPORTANT]
> **與 [Level4 會議秘書](../Level4_Meeting_Secretary/SKILL.md)的分工**：
> Level4 產出**會議紀錄**（給人讀的敘述），這個 skill 產出**行動計畫表**（給人追蹤的表格）。
>
> 兩者可以串接：先跑 Level4 產出紀錄，再跑這個產出追蹤表。

---

← [返回：Skills 範例](../README.md)
