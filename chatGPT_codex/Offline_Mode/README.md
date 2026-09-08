# 無外部帳號的離線實作模式

學生不需要購買方案，也不需要連接私人帳號。外部功能章節一律先用下表的離線替代方案完成；真實連線是選修展示。

| 真實功能 | 離線輸入 | 學生仍可完成的能力 | 離線時不做 |
|---|---|---|---|
| Google Drive | [`Drive Analysis` 偽檔](../Connectors/01_Google_Workspace/01_Drive_Analysis/sample_files/) | 多檔交叉分析、來源標記 | 搜尋私人 Drive |
| Gmail | [模擬郵件](../Connectors/01_Google_Workspace/02_Gmail_Automation/sample_files/模擬客戶郵件資料集.md) | 分類、摘要、擬草稿 | 寄信或修改信箱 |
| Calendar | [模擬行程](../Connectors/01_Google_Workspace/03_Calendar_Scheduling/sample_files/模擬行事曆日程資料集.md) | 衝突分析、提出候選時段 | 建立、接受或取消會議 |
| Canva | [品牌規範](../Connectors/02_Canva/sample_files/麥禾烘焙_品牌視覺規範與色彩配置表.json)與[企劃書](../Connectors/02_Canva/01_Product_Launch_Deck/sample_files/麥禾烘焙_2026秋季新品行銷企劃與視覺規格書.md) | 文案與品牌合規審查 | 寫入或發佈 Canva 設計 |
| GitHub | [`tideflow-portal/data`](../student-lab/tideflow-portal/data/) | Issue 分流、PR review、release notes | 留言、approve、merge、關閉 Issue |
| Browser | 教材內已下載的 `.md`、`.csv`、`.json` | 擷取、核對與引用 | 登入網站、送出表單 |
| Automation | `npm run report` | 相同輸入、限制與驗收邏輯 | 定時喚醒與通知 |
| Remote | 本機 task 的操作紀錄與 diff | 練習核准判斷與成果審查 | 手機跨裝置控制 |
| Public equity web research | [固定日期來源快照](../student-lab/tideflow-portal/data/public_equity_source_snapshot.md) | 來源分級、事實／推論分離 | 當成即時投資資訊 |

## 離線作業提交格式

每份作業都要附：

1. 使用的檔名與資料日期。
2. 原本會呼叫的外部功能。
3. 離線替代方式。
4. 實際產出。
5. 驗收結果與尚未驗證的外部步驟。

不得宣稱已寄信、已建行程、已 merge 或已發佈。正確寫法是「已產生草稿，外部寫入未執行」。

← [返回教材首頁](../README.md)
