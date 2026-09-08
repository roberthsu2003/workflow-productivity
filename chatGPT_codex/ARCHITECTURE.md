# ChatGPT Codex 講義架構

本目錄以 `Claude_ai` 的教學層次為參考，但使用 Codex 的實際產品概念重新分組；它不是逐字複製，而是功能對等的教材架構。

## 目錄地圖

```text
chatGPT_codex/
├── README.md                 # 全教材入口、方案與授課順序
├── Quickstart/               # 第一次安全操作
├── Settings/                 # 權限、sandbox、network、config.toml
├── Tasks/                    # 任務描述、長時工作與驗收
├── Projects/                 # 專案知識、Instructions 與案例
├── Agent_Configuration/      # AGENTS.md 的作用域與規則
├── Skills/                   # SKILL.md、四階範例與職能專題
├── Connectors/               # Google Workspace、Canva、GitHub
├── Plugins/                  # 可安裝的能力套件
├── MCP/                      # 自建工具與外部系統協定
├── Browser/                  # Browser、瀏覽器擴充與安全操作
├── Visualizations/           # 視覺化、Sites 與發佈治理
├── Workspaces/               # Desktop、CLI、IDE、Cloud 與 worktree
├── Automations/              # 排程、事件觸發與監控案例
├── Remote/                   # 跨裝置交辦、核准與審查
├── student-lab/              # 可離線執行的完整 TideFlow 練習專案
├── Answer_Key/               # 預期發現、驗收答案與評分規準
├── Troubleshooting/          # 自學時的環境、Git 與權限除錯
├── Offline_Mode/             # 外部服務章節的無帳號替代方案
└── tools/                    # 示範資料產生與架構驗證工具
```

## 與 Claude_ai 的功能對照

| Claude_ai | chatGPT_codex | 說明 |
|---|---|---|
| Chats | Tasks | 對話改以可執行、可驗收的 task 教學 |
| Artifacts | Visualizations | 拆成 workspace 檔案、視覺化、Sites 與圖片 |
| Projects | Projects | 加入本機資料夾、Git 與 worktree 概念 |
| Custom Instructions | Agent_Configuration | 以具目錄作用域的 `AGENTS.md` 為核心 |
| Connectors | Connectors | 依實際 app／服務分組 |
| Skills | Skills | 使用 `SKILL.md`，並保留四階學習路線 |
| Plugins | Plugins | 說明 skill、MCP 與 UI 的組合關係 |
| Local_MCP | MCP | 同時涵蓋本機與遠端 MCP |
| claude_in_chrome | Browser | 以 Codex／ChatGPT 的瀏覽器操作方式重寫 |
| cowork | Workspaces | 對照 Desktop、CLI、IDE、Cloud |
| Scheduled | Automations | 排程、監控與事件型工作 |
| Dispatch | Remote | 手機交辦、核准與成果審查 |
| Settings | Settings | 權限、sandbox、network 與設定檔 |

Codex 另外需要兩個 Claude 原目錄沒有獨立呈現的入口：`Quickstart` 用於第一次安全實作，`Agent_Configuration` 用於持久化 repository 規則。

## 每類目錄的完成條件

- 主題目錄必須有 `README.md`，並可返回教材首頁。
- `Examples/` 下的每個案例必須有 `README.md` 或可直接閱讀的 `.md` 教材。
- 可安裝 skill 必須以 `SKILL.md` 為入口；需要時再搭配 `references/`、`templates/`、`scripts/`。
- 練習所引用的本機素材必須存在；Markdown 相對連結不可失效。
- 不保留空資料夾；可重建的二進位教材要有 `tools/` 腳本與固定資料種子。
- 方案、功能狀態與操作介面會變動；授課前仍須依 README 所列官方文件複核。

## 驗證

在 repository 根目錄執行：

```bash
python3 chatGPT_codex/tools/validate_structure.py
```

驗證器會檢查必備章節、主題入口、案例入口、skill 入口、空資料夾及 Markdown 相對連結。它只讀取檔案，不會修改教材。

---

← [返回教材首頁](./README.md)
