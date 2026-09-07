# 🎨 實戰 4：打造「山嵐茶飲」品牌行銷視覺總監專案

> **所屬章節**：[Canva 連接器實戰](../README.md) ➔ **練習 4 (進階)**  
> **運作模式**：📁 **Claude Projects 專案模式**  
> **預計實作時間**：15 分鐘  
> **所需連接器**：🔹 **Canva**

---

## 🎯 任務目標

學習如何利用 **Claude Projects 專案沙盒** 常駐品牌視覺識別（VI）與色票庫，並與 **Canva 連接器** 深度串聯，讓 Claude 成為 24 小時在線的品牌專屬視覺總監，每次產出皆自動遵循法定色票，告別反覆貼色碼的瑣碎流程。

---

## 📥 專屬測試偽資料庫

| 檔案類型 | 檔案名稱（點擊檢視/下載） | 部署位置 | 說明 |
| :---: | :---| :---: | :---|
| 🎨 **視覺規範** | [**山嵐茶飲_品牌視覺規範與色彩配置表.json**](./sample_files/山嵐茶飲_品牌視覺規範與色彩配置表.json) | **Project Knowledge** | 包含品牌標準色 Hex、字型與間距系統。 |
| 📄 **企劃規格** | [**山嵐茶飲_2026夏季新品行銷企劃與視覺規格書.md**](./sample_files/山嵐茶飲_2026夏季新品行銷企劃與視覺規格書.md) | **Project Knowledge** | 產品賣點與品牌調性定義。 |

---

## 🛠️ 步驟 1：專案建置設定（Claude Projects Setup）

1. 登入 [Claude.ai](https://claude.ai) ➔ 點選左側 **Projects** ➔ **Create project**。
2. 填入專案基本資訊：
   - **Project Name（專案名稱）**：
     ```text
     山嵐茶飲_品牌視覺設計總監
     ```
   - **Project Description（專案描述）**：
     ```text
     內建山嵐茶飲官方視覺識別手冊與色票庫，直連 Canva 官方連接器，一鍵產出符合品牌規範之投影片、社群海報與直達編輯連結。
     ```
3. 點擊 **Create project**。

---

## 📜 步驟 2：設定常駐專案指引（Project Instructions）

進入專案，在右側面板點擊 **Set Project Instructions**，貼入以下常駐視覺守門員指引：

```markdown
## Role
你是「山嵐茶飲」的專屬品牌視覺總監與 Canva 設計智囊。

## Core Mission
每當使用者提出任何宣傳行銷企劃時，你必須嚴格基於專案知識庫（Project Knowledge）中的《品牌視覺規範與色彩配置表.json》，調用 Canva 連接器推薦最佳版型，並確保每一項產出皆 100% 符合品牌色票與留白哲學。

## Strict Design Guidelines
1. **絕對禁色**：嚴禁出現純黑（#000000）、死白（#FFFFFF）或高飽和霓虹色。
2. **法定色票**：
   - 主視覺：深霧綠 `#243E36`
   - 點睛色：茶湯金 `#C59B27`
   - 底色：雲霧白 `#F8F7F2`
3. **Canva 調用規範**：每次推薦範本時，優先選擇支援日系極簡、負空間（Negative Space）的版型，並主動提供一鍵開啟直達編輯連結。
```

---

## 📥 步驟 3：上傳專案知識庫（Project Knowledge）

在專案頁面右側 **Project Knowledge** 區塊，點選 **Add content** ➔ **Upload files**，上傳：
- [山嵐茶飲_品牌視覺規範與色彩配置表.json](./sample_files/山嵐茶飲_品牌視覺規範與色彩配置表.json)
- [山嵐茶飲_2026夏季新品行銷企劃與視覺規格書.md](./sample_files/山嵐茶飲_2026夏季新品行銷企劃與視覺規格書.md)

---

## 💬 步驟 4：對話實測指令（Prompt）

點擊 **Start new chat**，確認該對話已連線 Canva 連接器，貼入以下指令：

```markdown
我們下個月要舉辦「茶園漫步・品茶茶席」線下 VIP 體驗會，請呼叫 Canva 連接器幫我產出一份典雅的邀請函明信片（Postcard，5x7 吋）版面建議與 Canva 編輯連結。
```

---

## ✅ 成果驗收點

- [ ] **常駐知識庫自動啟用**：無需額外提示，Claude 自動抓取知識庫中的 `#243E36` 與 `#C59B27` 色碼。
- [ ] **精準版型推薦**：調用 Canva 連接器推薦 5x7 吋明信片範本並給予排版結構建議。

---

← [上一練習：全通路橫幅規格](../03_Multi_Format_Banner/README.md) · [返回主章節](../README.md)
