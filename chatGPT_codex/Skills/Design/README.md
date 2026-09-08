# 實作練習：使用現成 Plugin（設計與品牌實戰）

> 🔵 **方案需求**：Plus 起（Plugins、Image generation、Visualizations）。
> 🎨 **設計主軸**：用 **Creative Production** 與 **Product Design** plugin，讓產出具備一致的品牌識別，而不是每次都重新發揮。

Claude 的對應章節是 `brand-guidelines`、`canvas-design`、`theme-factory`、`algorithmic-art` 四個官方 Skill。Codex 把這些能力包進**職能 plugin**。

---

## 🛠️ 前置步驟

1. `Settings` → `Plugins`，安裝 **Creative Production**（串接 Figma、Canva、Shutterstock、Picsart、Fal）
2. 視需要安裝 **Product Design**
3. 完成 OAuth 授權——**不要授權「發佈／分享」**
4. 開啟新對話

> [!WARNING]
> 課堂請用個人帳號，不要用有真實品牌資產的公司 Canva / Figma 帳號。

---

## 🔑 核心觀念：品牌規範應該是「檔案」，不是「記憶」

> [!IMPORTANT]
> ### 這是 Codex 相對於 Claude 最大的優勢
>
> Claude 的 `brand-guidelines` 把品牌色寫在 skill 裡（Orange `#d97757`、Blue `#6a9bcc`、字型 Poppins / Lora）。
>
> Codex 的做法是：**品牌規範放成 workspace 裡的一個 JSON 檔，Codex 直接讀它。**
>
> | | Claude 做法 | Codex 做法 |
> | :--- | :--- | :--- |
> | 規範在哪 | 寫在 skill 內 | **repo 裡的 JSON 檔** |
> | 改規範 | 改 skill | 改 JSON，**有 git 歷史** |
> | 驗證 | 請模型自己檢查 | **可寫程式實際計算** |
> | 團隊同步 | 重新分享 skill | `git pull` |

本章使用 [`麥禾烘焙_品牌視覺規範與色彩配置表.json`](../../Connectors/02_Canva/sample_files/麥禾烘焙_品牌視覺規範與色彩配置表.json)。

---

## 練習 A：品牌化的產品介紹（對應 `brand-guidelines`）

### 📋 GCSV Prompt

```markdown
## Goal
為麥禾烘焙的秋栗蒙布朗製作一份品牌化的產品介紹單頁。

## Context
- 品牌規範：`Connectors/02_Canva/sample_files/麥禾烘焙_品牌視覺規範與色彩配置表.json`
- 產品資訊：`Connectors/02_Canva/01_Product_Launch_Deck/sample_files/麥禾烘焙_2026秋季新品行銷企劃與視覺規格書.md`

## Scope
- **色票、字體、留白一律以 JSON 規範為準，不可自行發揮。**
- 產品事實以企劃書為準，不可美化（產地是嘉義中埔，不是日本）。
- 不可使用禁用語清單中的任何用語。
- 不要發佈或分享設計，只建立草稿。

## Verification
產出後逐條回報：
| 規範條目 | 我的做法 | 符合？ |

特別說明三件事：
1. 你用了哪些顏色，各自用在哪裡
2. **`wheat_gold #C8912F` 你有沒有拿來當內文色？為什麼？**
3. `chestnut #8B5E3C` 的使用是否在有效期內？
```

> **第 2、3 點是陷阱題**。規範中這兩個顏色都是「有條件允許」：
> - `wheat_gold` 是主品牌色，但在 cream 背景上對比度不足 → **不可作內文**
> - `chestnut` 是秋季限定色，**有效期至 2026-11-30**

---

## 練習 B：主題與配色系統（對應 `theme-factory`）

### 📋 GCSV Prompt

```markdown
## Goal
從品牌規範衍生出一套完整的網頁配色 token，供官網改版使用。

## Context
- 來源：品牌規範 JSON
- 需求：需同時支援淺色與深色模式

## Scope
- 深色模式的色票**必須從既有品牌色推導**，不可憑空創造新顏色。
- **所有組合都必須通過 WCAG 2.1 AA**（一般文字 4.5:1、大字 3.0:1）。
- 輸出 `design/tokens.json` 與 `design/tokens.css`，不要修改原始規範 JSON。

## Verification
1. token 清單（語意化命名，如 `--color-text-primary`，不是 `--color-brown`）
2. **對比度實測表**——寫一個腳本實際計算，不要憑印象
3. 深色模式每個色票的推導邏輯
4. 若有任何組合無法同時滿足品牌調性與 AA，**明說並提出取捨方案**
```

### 🎯 為什麼要求「寫腳本實際計算」

這是本章的核心教學點。對比度是**可計算的客觀數值**：

```python
# design/contrast.py 的核心邏輯
def relative_luminance(hex_color):
    def channel(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    return 0.2126*channel(r) + 0.7152*channel(g) + 0.0722*channel(b)

def contrast_ratio(fg, bg):
    l1, l2 = sorted([relative_luminance(fg), relative_luminance(bg)], reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)
```

> **模型憑印象判斷對比度會出錯，跑一次程式不會。**
> 這個差別在無障礙需求上是「合規」與「不合規」的分野。

---

## 練習 C：多尺寸素材與版面（對應 `canvas-design`）

### 📋 GCSV Prompt

```markdown
## Goal
依主視覺衍生出企劃書素材清單中的 9 件素材。

## Context
素材清單見企劃書第三節（A2 海報到 60×20mm 貼條）。

## Scope
- 保持視覺一致性。
- **依尺寸調整資訊密度**——不是把大圖縮小。
- 品牌規範的字級下限在所有尺寸都適用。
- 不要發佈或分享。

## Verification
對照表：
| 素材 | 尺寸 | 保留 | 捨棄 | 為什麼 |

**A-03 貼條（60×20mm）特別說明**：
過敏原標示是法規要求，但這個尺寸塞不下。你怎麼處理？
```

> [!WARNING]
> **A-03 是判斷題。** 正確解法不是硬塞或省略，而是**指出矛盾並提方案**——貼條只放品名與價格，過敏原由旁邊的桌卡或商品包裝承擔。
>
> 直接把字縮到 4pt，或直接省略過敏原，都是錯的。

---

## 練習 D：生成式視覺（對應 `algorithmic-art`）

### 📖 說明

Claude 的 `algorithmic-art` 用程式生成視覺。Codex 的對應能力分成兩條路：

| 需求 | Codex 的做法 |
| :--- | :--- |
| 寫實的商品情境照 | **Image generation** |
| 程式生成的圖樣、資料視覺 | **Visualizations** 或直接寫程式產 SVG |

### 📋 Prompt：商品情境照

```text
替麥禾烘焙的「秋栗蒙布朗」產生商品情境照。

依品牌規範的 photography 章節：
- 自然光，不使用人工強光
- 俯視 45 度
- 木質桌面 + 亞麻布背景
- 素色陶盤，可搭配栗子實物與乾燥落葉（3 片以內）
- 暖色調

禁止：冷色調濾鏡、人物臉部入鏡、出現文字或 logo。
尺寸：正方形，供 Instagram 使用。
```

### 📋 Prompt：程式生成圖樣

```markdown
## Goal
產生一組可用於包裝紙的重複圖樣（seamless pattern）。

## Scope
- 只使用品牌規範中的色票。
- 輸出可縮放的 SVG，寫入 `design/patterns/`。
- **必須是真正可無縫拼接的**——寫一個測試驗證邊界對齊。

## Verification
- SVG 檔案
- 拼接測試的結果（3×3 拼貼後邊界應無接縫）
- 用到的色票清單
```

> **注意最後一條**：「寫測試驗證無縫」是 Codex 才做得到的事。它會實際檢查，而不是說「應該可以」。

---

## 🔄 與 Claude 官方 Skill 的對照

| Claude 官方 Skill | Codex 對應 | 關鍵差異 |
| :--- | :--- | :--- |
| `brand-guidelines` | **Creative Production plugin + repo 內的規範 JSON** | 規範**可版控、可程式驗證** |
| `canvas-design` | Creative Production（Canva、Figma） | 相近 |
| `theme-factory` | 自建流程 + 對比度計算腳本 | **可實測而非估算** |
| `algorithmic-art` | Image generation / Visualizations / 直接產 SVG | 拆成三條路 |
| — | **Product Design plugin** | ➕ Codex 額外提供 |

---

## ✅ 驗收檢查清單

- [ ] 沒有把 `wheat_gold` 用作內文色
- [ ] 有確認 `chestnut` 的有效期
- [ ] 對比度是**實際計算**的，不是估算
- [ ] 深色模式色票從既有品牌色推導
- [ ] A-03 貼條的過敏原有可行解法
- [ ] 產地寫「嘉義中埔」，沒有被美化
- [ ] 沒有使用禁用語
- [ ] **沒有發佈或分享任何設計**

---

## 🔗 延伸

完成本章後，接續做 [Connectors / Canva 的合規審查](../../Connectors/02_Canva/02_Instagram_Brand_Post/README.md)——那裡有一份含 **18 處違規**的真實草稿等你審查，其中一處只有交叉比對企劃書才抓得到。

---

← [返回上層：Skills](../README.md) ｜ [返回索引](../../README.md)
