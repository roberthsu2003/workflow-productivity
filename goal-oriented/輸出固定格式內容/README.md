# 輸出固定格式內容

如果你的目標是：

> 👉 **讓 AI 不管回答什麼內容，都輸出固定格式的文件**

這在你目前教的 MCP / Agent 架構中其實非常重要，因為這會影響：

- 後續自動化流程
- 是否能被其他工具解析
- 是否能儲存成固定結構資料

---

# **🎯 方法一：在 System Prompt 強制格式（最簡單）**

這是最基本也最重要的方法。

## **範例：強制輸出 Markdown 文件格式**

```other
你是一個文件產生器。
所有回答都必須使用以下格式輸出：

# 文件標題

## 摘要
(100字內)

## 內容
(條列式)

## 結論
(一句話總結)

如果沒有按照格式，請重新產生。
```

### **優點**

- 最簡單
- 不用寫程式
- 適合教學入門

### **缺點**

- 模型有時會「不聽話」
- 無法 100% 保證

---

# **🎯 方法二：使用 JSON Schema 強制結構（進階推薦）**

如果你要做：

- MCP tool
- Pipeline
- 自動儲存
- 寫入資料庫

👉 一定要用 JSON 結構。

---

## **範例：固定 JSON 文件格式**

```other
請使用以下 JSON 格式輸出，不要加入任何額外文字：

{
  "title": "",
  "summary": "",
  "content": [],
  "conclusion": ""
}
```

### **生成結果會變成：**

```other
{
  "title": "AI 與教育",
  "summary": "說明 AI 在教育中的應用。",
  "content": [
    "自動批改作業",
    "生成教學教材",
    "個人化學習"
  ],
  "conclusion": "AI 將改變未來教育模式。"
}
```

這種做法非常適合你現在的：

- Open-WebUI
- MCP server
- Agent 自動流程

---

# **🎯 方法三：使用 OpenAI Structured Output（最穩定）**

如果你使用：

- OpenAI-compatible API
- Ollama OpenAI 模式
- Google OpenAI compatible endpoint

你可以用 response_format 或 tool schema。

例如：

```other
response_format: {
  "type": "json_schema",
  "json_schema": {
    "name": "document",
    "schema": {
      "type": "object",
      "properties": {
        "title": { "type": "string" },
        "summary": { "type": "string" },
        "content": {
          "type": "array",
          "items": { "type": "string" }
        },
        "conclusion": { "type": "string" }
      },
      "required": ["title", "summary", "content", "conclusion"]
    }
  }
}
```

這樣模型幾乎不能亂輸出。

---

# **🎯 方法四：MCP Tool 強制回傳格式（你現在最適合）**

因為你正在教 MCP，我會建議你這樣做：

### **設計一個 Tool**

```other
@tool
def generate_document(topic: str) -> dict:
    """
    產生固定格式文件
    """
```

然後由 Tool 內部去包裝格式。

這樣：

- AI 負責內容
- Tool 負責格式
- 結構永遠不會錯

這是「工程級做法」。

---

# **🧠 教學建議（給你課程用）**

你可以分成三層難度教：

### **第一層（Prompt工程）**

👉 用 System Prompt 固定 Markdown

### **第二層（JSON輸出）**

👉 強制 JSON 結構

### **第三層（Agent級設計）**

👉 MCP Tool 控制格式

這樣學生會明白：

- Prompt 只是語言控制
- JSON 是結構控制
- Tool 是工程控制

這三者的差異。

---

# **🚀 如果你要做到「完全不亂」**

最佳做法是：

```other
LLM → 只生成內容
Tool → 組裝成固定格式
資料庫 → 儲存
```

這樣 AI 永遠不會破壞格式。

---

如果你願意，我可以幫你：

- 設計一個「固定文件格式生成 MCP Server 範例」
- 或幫你寫成可直接放 GitHub 的教學章節
- 或幫你做一個給學生練習的完整實戰案例

你想要走「教學版」還是「工程實戰版」？