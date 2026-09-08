# 延伸練習 01：社群貼文文案（第一階：模仿者）

> 🟢 **方案需求**：Free。
> **對應** `Claude_ai/Skills/Examples/Office_Workflow_01_Copywriter.md`

第一階延伸練習。重點是學會用**檔案系統**建立最基礎的自訂 skill。

---

## 📖 說明

把簡單的主題想法，擴寫成符合平台特性的社群貼文。

> [!IMPORTANT]
> **與 Claude 的建立方式完全不同。**
> Claude：介面 → Customize → Skills → Create skill → 填欄位
> **Codex：直接建立資料夾與檔案。**

---

## 🛠️ 建立方式

```bash
mkdir -p ~/.agents/skills/social-post-writer
cat > ~/.agents/skills/social-post-writer/SKILL.md <<'EOF'
---
name: social-post-writer
description: 把簡單的主題想法擴寫成社群貼文（Facebook／Instagram／LinkedIn）。適用於已有明確主題與事實素材時；不要用於新聞稿、正式公告、需要法務審閱的內容，也不要在沒有事實素材時憑空生成。
---

# Social Post Writer

## 流程
1. 確認三件事：平台、受眾、這則貼文要對方做什麼（CTA）。
   **任一項缺少就先問，不要猜。**
2. 依平台特性調整長度與語氣。
3. 產出：標題 → 正文 → CTA → hashtag。

## 平台差異
| 平台 | 字數 | 語氣 | hashtag |
| Facebook | 100–200 字 | 口語、可用表情 | 0–3 個 |
| Instagram | 300 字內 | 親近、重視覺 | 3–8 個 |
| LinkedIn | 150–300 字 | 專業、有觀點 | 0–3 個 |

## 限制
- **不得新增使用者未提供的事實**（數字、日期、產品特性、獲獎紀錄）。
- 不使用無法佐證的最高級形容（最好、第一、唯一）。
- 不使用製造焦慮的用語（錯過再等一年、最後機會）。
- 涉及食品、醫療、金融時，不做功效或報酬宣稱。

## 輸出
貼文全文 + 一行說明：**你有哪些地方需要我補充事實素材？**
EOF
```

---

## ▶️ 測試

| 介面 | 輸入 |
| :--- | :--- |
| ChatGPT | `@social-post-writer` |
| Codex | `$social-post-writer` |

```text
$social-post-writer

平台：Instagram
主題：麥禾烘焙秋栗蒙布朗 10/5 上市
素材：嘉義中埔栗子、每店每日 75 個、NT$145、供應到 11/30
```

### 驗收

- [ ] 有問你缺少的資訊（受眾？CTA？過敏原？）
- [ ] **沒有新增你沒提供的事實**（例如自己補上「日本進口鮮奶油」）
- [ ] 沒有用「最好吃」「錯過再等一年」
- [ ] hashtag 數量在 3–8

> **第 2 點是關鍵測試。** 素材裡沒提到的東西，它補了就是幻覺。

---

## 🔄 與 Claude 版的差異

| | Claude | Codex |
| :--- | :--- | :--- |
| 建立 | 介面填欄位 | **建立檔案** |
| 儲存 | 雲端帳號 | `~/.agents/skills/` |
| 分享 | 介面分享 | **`git commit`** |
| 修改 | 回介面編輯 | **編輯檔案，可 `git diff`** |

---

← [返回：Skills 範例](./README.md)
