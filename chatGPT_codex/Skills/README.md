# Codex Skills

Skill 是含 `SKILL.md` 的資料夾，用來封裝可重複的專業流程。Codex 依名稱與描述判斷何時載入，再使用 references、templates、scripts 或 assets。

```text
my-skill/
├── SKILL.md
├── references/
├── templates/
├── scripts/
└── assets/
```

```markdown
---
name: meeting-action-items
description: 將會議逐字稿整理成決議、負責人、期限與待確認事項。
---
# Meeting Action Items
不得補造未出現的負責人或期限。輸出摘要、決議、行動項目與待確認問題。
```

個人 skill 通常放在 `$CODEX_HOME/skills/<skill-name>/`。`Claude_ai/Skills/Examples` 的純文字流程可作為內容參考，但安裝路徑、工具名稱、權限與 UI 必須改成 Codex 版本。

官方說明：[Build skills](https://learn.chatgpt.com/docs/build-skills)

[← 返回索引](../README.md)
