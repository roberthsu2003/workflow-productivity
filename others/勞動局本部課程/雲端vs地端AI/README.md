# 雲端vs地端AI

## 主要的AI工具

- ollama
- Buzz


### open source模型選擇

- 支援多國語言
- 非中國大陸模型


#### openAI:`gpt-oss:20b`
#### google:`gemaa3:12b`
#### microsoft:`phi4:14b`
#### meta:`llama3.1:8b`
#### mistral:`mistral-small3.2:latest`


---

## 一、Ollama（地端 LLM）

**官方網站**：[https://ollama.com/download](https://ollama.com/download)

### macOS 安裝

1. **方式 A（推薦）**：前往 Ollama 官網下載 `.dmg` 安裝檔，雙擊執行安裝。
2. **方式 B**：於終端機執行以下指令：

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

3. 安裝完成後，開啟 Ollama 應用程式。
4. 於終端機執行以下指令下載課程所需模型：

```bash
ollama pull gpt-oss:20b
```

5. **驗證**：執行 `ollama run gpt-oss:20b`，若可正常對話即表示安裝成功。

### Windows 安裝

1. 前往 Ollama 官網下載 Windows 安裝檔（`.exe`）。
2. 雙擊安裝檔，依指示完成安裝。
3. 安裝完成後，開啟命令提示字元（CMD）或 PowerShell，執行：

```bash
ollama pull gpt-oss:20b
```

4. **驗證**：執行 `ollama run gpt-oss:20b`，若可正常對話即表示安裝成功。

---

## 二、Buzz（語音轉文字工具）

**官方下載**：[Buzz 於 SourceForge 的檔案頁](https://sourceforge.net/projects/buzz-captions/files/)

Buzz 為免費開源之離線語音轉文字工具，採用 OpenAI Whisper 模型，支援多種語言。

### macOS 安裝

1. 前往 SourceForge Buzz 專案頁面。
2. 依電腦架構選擇對應版本（Intel 或 Apple Silicon）。
3. 下載 `.dmg` 檔案，雙擊掛載後將 Buzz 拖曳至「應用程式」資料夾。
4. 首次開啟時，於「設定」中下載 small 模型（課程建議使用）。
5. **驗證**：匯入一段音訊檔，確認可成功產生逐字稿。

### Windows 安裝

1. 前往 SourceForge Buzz 專案頁面。
2. 下載 Windows 安裝檔（`.exe`）。
3. 執行安裝檔。若出現「未簽署」警告，請點選「更多資訊」→「仍要執行」。
4. 首次開啟時，於設定中下載 small 模型。
5. **驗證**：匯入一段音訊檔，確認可成功產生逐字稿。
