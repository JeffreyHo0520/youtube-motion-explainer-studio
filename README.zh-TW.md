# YouTube & Facebook 旗艦解說動畫全能工坊 (`youtube-motion-explainer-studio`)

> **端到端 YouTube 與 Facebook 旗艦解說動畫全能工坊**  
> HyperFrames 1080p + 台灣國語旁白字幕 + 三色主題與源石黑體 + 真人實況紀錄片「我要是真人」/ 史料照片雙模組 + NASA/SpaceX 官方公有領域真實素材自動抓取 + 靜態照片 Ken Burns 緩慢推鏡 + HTML5/Python 物理動態圖解代碼現場渲染 + FFmpeg 無剪輯軟體平滑多分鏡串接 + Concat 原生剪輯軟體 MCP 自動化後製字卡與 1080p 輸出 + 全動態 B-roll 視訊無縫循環底圖 + 真人/角色主播 HUD 徽章 + Deep Tech 廣播級側鏈音訊避讓 (Sidechain BGM Ducking) + 幾何居中資訊排版 + 豐富動態特效組件 + 視覺自我審查 + -14.0 LUFS 廣播級響度校準 + 16:9 爆款縮圖與 YouTube/Facebook 社群上架包 + Antigravity 聯網法案/科技新聞調研分鏡 JSON + Pexels/Pixabay 商用 B-roll 自動化下載 + Playwright 無頭推文與法案卡片截取。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Package Manager: uv](https://img.shields.io/badge/uv-Astral-purple.svg)](https://astral.sh/uv)
[![HyperFrames](https://img.shields.io/badge/Render-HyperFrames%201080p-orange)](https://github.com/heygen-com/hyperframes)
[![Audio](https://img.shields.io/badge/Audio-EBU%20R128%20--14.0%20LUFS-green)](https://en.wikipedia.org/wiki/EBU_R_128)
[![Concat MCP](https://img.shields.io/badge/NLE-Concat%20MCP-red)](https://github.com/JeffreyHo0520/concat-video-editor)

---

## 📖 技能簡介 (Overview)

`youtube-motion-explainer-studio` 將「深度考證解說動畫（HyperFrames 1080p）」、「YouTube 高點擊率縮圖＋SEO 上架包」及「Facebook 高互動貼文包」整合為一條零斷點、抗報錯、可完全重複執行的端到端全自動生產線。

當使用者要求「做一支解說動畫並打包 YouTube 與 FB 上架素材」、「商業科技/巨頭商戰/歷史深度解說動畫全套流程」、「實況真人紀實風格動畫」、「替換背景為動態 B-roll」、「加入真人/角色主播徽章」、「背景配樂與廣播級音訊避讓 (BGM Ducking)」、「增加多一點動畫與寫實畫面」、「用 Concat 加片頭片尾與轉折字卡並輸出」、「聯網檢索法案/新聞並產出分鏡 JSON」、「自動下載 Pexels/Pixabay B-roll」或「用 Playwright 截取推文或法案條文」時觸發。

---

## 🌟 六大核心視覺與工作流模組

1. **模式 A：現代科技與巨頭商戰「真人實況模式」（Live-Action & Real Person Realism）**
   - 嚴格遵守「**我要是真人**」原則：100% 紀實超寫實電影感風格，杜絕二次元、日漫或卡通風格。
   - 真實科技領袖（黃仁勳、馬斯克、奧特曼等）發表會特寫、近地軌道衛星、無塵室工程師、發射台點火與戰情室全景。
   - 動態視覺組件：立體光暈、雷射雷達掃描線、HUD 戰術四角框線、數據收縮光條、價格暴跌刪除線、粒子擊中翻轉震顫與熱輻射呼吸波。

2. **模式 B：歷史文獻與軍事戰役「史料紀實模式」（Historical Archive Mode）**
   - 多方戰史公報交叉考證、Wikimedia Commons 開放授權史料、紙本軍圖三色雙色調（Duotone）、動態軍事標記與 Google Colab G4 MiniMax H3 實景影片。

3. **模式 C：航太深空與硬核科學「實況＋代碼動態圖解混合流」（Real-Footage & Code-Driven Motion Pipeline）**
   - **公有領域真實素材自動抓取**：Python 自動調用 NASA Image & Video Library 官方 API，批量下載真實發射與探測實拍（CC0 / Public Domain）。
   - **靜態照片 Ken Burns 緩慢推鏡**：透過 FFmpeg `zoompan` 賦予靜態歷史/新聞大圖流暢的電影級慢速推進運鏡。
   - **動態圖解代碼現場渲染**：微重力流體沉底（Ullage Thrust）、軌道力學對接等物理原理，現場編寫 HTML5 Canvas 模擬器或 Python 渲染 1080p 粒子動畫。
   - **全自動無剪輯軟體串接 (FFmpeg Concat)**：純程式碼將實拍推鏡、概念圖解、自製物理粒子動畫平滑無縫串接並燒錄中文字幕。
   - **封面頁雙軌機制與黃金 5 幕無重複敘事**：時間軸片頭封面卡 + MP4 容器海報中繼資料（`attached_pic`），拒絕結尾重複素材審美疲勞。

4. **模組 D：專業剪輯軟體「Concat MCP 自動化後製字卡與輸出管線」（Concat MCP Automated NLE Pipeline）**
   - **完全無頭（Headless）自動化剪輯**：調用本機 Concat 剪輯軟體原生 MCP 服務，免手動開啟 GUI 即可完成專案建立、影片匯入、多軌編排與文字動態配置。
   - **黃金 6 大字卡矩陣（6-Card Arc）**：精準依據腳本時間軸植入「片頭懸念勾子、物理反差轉折、領袖登場特寫、商業模式定價權、終局制空權、片尾昇華與社群行動（CTA）」。
   - **空間分層防撞車原則（Upper-Third Rule）**：字卡統一配置於上三分之一（`offsetY: -0.34`），與底部解說字幕（`offsetY: +0.38`）完美分層，互不干擾。
   - **實時影格預覽校驗（Frame Preview）**：匯出前調用 `preview_frame` 抽取片頭、高潮、片尾之合成 PNG，核實構圖、色彩對比度與行距。
   - **背景非同步編碼與安全釋放專案鎖**：`export_start` + `export_wait` 輪詢渲染 1080p 成片，並透過 `project_close` 安全釋放 `concat.lock`。

5. **模式 E：全動態 B-roll 科技新聞播報流（Dynamic B-roll & Host HUD News Pipeline）**
   - **動態 B-roll 視訊循環底圖（Dynamic B-roll Footage）**：1080p 高清動態影片為全幕背景（機房指示燈、晶圓傳輸、近地軌道衛星），透過 FFmpeg `-stream_loop -1` 實現分秒精確的無縫循環；上方疊加 80% 穿透率深海藍半透明玻璃資訊卡（`rgba(12, 19, 36, 210)`）。
   - **真人/虛擬角色主播 HUD 徽章（Host Avatar HUD Badge）**：精準擷取人物設定圖肖像，圓形遮罩裁切，封裝進 260x300 賽博龐克 HUD 徽章（雙軌霓虹光環、頂部 `🟢 LIVE` 動態信標、底部身分銘牌），右上角（`x=1560, y=45`）安全不擋標題與字幕。
   - **廣播級 Deep Tech 側鏈音訊避讓（BGM Ducking via Native FFmpeg Sidechain Compression）**：124 BPM 實體 Deep Tech 合成器律動音軌；人聲口播時 BGM 精準下潛至 `0.22` (-13dB)，人聲停頓時 350ms 平滑抬升至 `0.65`，總輸出符合 EBU R128 `-14.0 LUFS`。
   - **幾何居中排版與左右對稱膠囊（Centered Typography & Symmetric Badges）**：標題大卡片與主次標題嚴格幾何居中（`card_cx = 795`），標籤膠囊採用動態 `textbbox` 計算左右對稱 Padding（`pad_x = 24`，`pill_w = text_w + 48`），杜絕偏向或溢出。

6. **模式 F：政策法案與時事新聞自動化調研流（Policy News, Legislation & Tweet Pipeline）**
   - **Antigravity 聯網深度調研與分鏡 JSON 規範**：自動聯網檢索各國國會法案（Congress.gov、GPO 官方全文）、行政命令、巨頭政策白皮書與 X 即時貼文，提煉技術門檻與法律罰則，標準化輸出結構化 `storyboard.json`。
   - **Pexels API / Pixabay 自動化商用 B-roll 檢索與下載管線**：Python 自動根據分鏡關鍵詞批次查詢 Pexels / Pixabay API，過濾下載 1080p 橫式免版稅高清短片至 `assets/broll/`，並記錄中繼清單 `broll_manifest.json`。
   - **Playwright / Chrome 無頭推文與法案文件焦點截圖管線**：2x Retina 解析度無頭 Chromium 自動載入社群推文（X/Twitter）、政府公報 PDF/HTML，注入深色模式與 CSS Selector 裁切，輸出無水印、高對比的透明/深色 PNG 卡片。

---

## 🚀 跨電腦安裝方式 (Installation Guide)

在另一台電腦上，你可以使用以下任一方式快速安裝此技能：

### 方法一：直接 Clone 至 Antigravity 全域技能目錄（最推薦、零設定）

#### Windows (PowerShell):
```powershell
# 1. 確保 skills 目錄存在
New-Item -ItemType Directory -Force -Path "$HOME\.gemini\config\skills"

# 2. 直接 Clone 至全域技能目錄
git clone https://github.com/JeffreyHo0520/youtube-motion-explainer-studio.git "$HOME\.gemini\config\skills\youtube-motion-explainer-studio"
```

#### macOS / Linux:
```bash
# 1. 確保 skills 目錄存在
mkdir -p ~/.gemini/config/skills

# 2. 直接 Clone 至全域技能目錄
git clone https://github.com/JeffreyHo0520/youtube-motion-explainer-studio.git ~/.gemini/config/skills/youtube-motion-explainer-studio
```

---

### 方法二：使用一鍵安裝腳本（支援多 Agent：Antigravity / Claude Code / Codex）

克隆專案到任意目錄後執行內建安裝腳本：

#### Windows (PowerShell):
```powershell
git clone https://github.com/JeffreyHo0520/youtube-motion-explainer-studio.git
cd youtube-motion-explainer-studio
.\install.ps1
```
*如需覆寫既有安裝，加入 `-Force` 參數；如需安裝至自訂路徑，傳入 `-Dest "C:\your\skills"`。*

#### macOS / Linux:
```bash
git clone https://github.com/JeffreyHo0520/youtube-motion-explainer-studio.git
cd youtube-motion-explainer-studio
chmod +x install.sh
./install.sh
```

---

## 📦 專案結構 (Directory Structure)

```text
youtube-motion-explainer-studio/
├── SKILL.md                 # 技能核心規格、全流程說明書與 19 大避坑手冊
├── README.md                # 英文說明文件 (English Guide)
├── README.zh-TW.md          # 繁體中文完整說明手冊
├── LICENSE                  # MIT 開源授權
├── install.ps1              # Windows 一鍵安裝與依賴檢查腳本
├── install.sh               # macOS / Linux 一鍵安裝與依賴檢查腳本
├── .gitignore               # 忽略暫存、快取與影音渲染檔案
└── scripts/
    └── yt_studio_helper.py  # 全功能跨平台 CLI 輔助工具 (強制 UTF-8 / PEP 723 內嵌依賴)
```

---

## ⚡ CLI 工具速查 (`scripts/yt_studio_helper.py`)

本技能配備純 Python 跨平台 CLI 工具 `scripts/yt_studio_helper.py`。其頂部已內嵌 PEP 723 依賴宣告，透過 `uv run` 執行時**會自動在背景即時安裝 Pillow 與 Playwright**，不需要手動配置虛擬環境：

```powershell
# 1. 組裝後一鍵修復 CJK @font-face、captions 軌道標記、替換 repeat:-1，確保 hyperframes lint 0 error(s)
uv run scripts/yt_studio_helper.py fix-fonts-and-lint --project . --output renders/lint_status.json

# 2. 將渲染完成的 MP4 音訊無損校準至 -14.0 LUFS（影像軌 -c:v copy 100% 不重新編碼）
uv run scripts/yt_studio_helper.py normalize-audio --video renders/video.mp4 --target-lufs -14.0 --output renders/audio_loudness.json

# 3. UTF-8 安全合成 16:9 YouTube 爆款縮圖（暗角 Scrim + 橘色主標 + 白色副標 + 雙數據對決卡）
uv run scripts/yt_studio_helper.py build-thumbnail --bg assets/images/gen/youtube_thumbnail_bg.jpg --font assets/fonts/GenSekiGothic2TW-B.otf --config thumbnail_spec.json --output renders/youtube_thumbnail.jpg

# 4. 自動讀取 STORYBOARD.md 時間碼，一鍵生成 YouTube 上架包、Facebook 貼文包與專案交付報告
uv run scripts/yt_studio_helper.py generate-social-packs --project . --config social_spec.json --output social_pack_manifest.json

# 5. 自動探測成片長度與色調，生成 Concat 6 大字卡排程規劃 JSON（上三分之一安全帶 offsetY: -0.34）
uv run scripts/yt_studio_helper.py plan-concat-titles --project . --output concat_titles_plan.json

# 6. 安全解除 Concat 異常中斷殘留之專案鎖（concat.lock），防止多實例報錯
uv run scripts/yt_studio_helper.py unlock-concat --project .

# 7. 自動從人物/角色設定圖裁切正面人像，生成 260x300 賽博龐克主播 HUD 徽章（含 🟢 LIVE 呼吸燈與身分銘牌）
uv run scripts/yt_studio_helper.py build-avatar-badge --input assets/character_sheet.jpg --output renders/host_avatar_badge.png --label "科技總編 ｜ 深度觀點"

# 8. 廣播級側鏈音訊避讓（Deep Tech BGM 在口播時自動下潛至 0.22，無人聲時 350ms 平滑回彈至 0.65）
uv run scripts/yt_studio_helper.py sidechain-ducking --voice renders/full_narration.wav --bgm assets/audio/bgm_deep_tech.wav --output renders/master_ducked_audio.wav

# 9. 動態 B-roll 視訊無縫循環 (-stream_loop -1) 與半透明居中資訊卡合成
uv run scripts/yt_studio_helper.py compose-broll-scene --broll assets/broll/datacenter.mp4 --overlay cards/scene_1.png --duration 11.88 --output renders/scene_1.mp4

# 10. Pexels API / Pixabay 自動化下載 1080p 免版稅 B-roll 影片
uv run scripts/yt_studio_helper.py download-broll --query "datacenter server rack" --output assets/broll/datacenter.mp4 --source pexels

# 11. Playwright / Chrome 無頭高解析截取 X 推文、法案與新聞文件重點（深色模式 + 2x Retina）
uv run scripts/yt_studio_helper.py capture-web --url "https://x.com/RepYassAnsari/status/2118054336077127797" --selector "article[data-testid='tweet']" --dark-mode --output assets/snippets/tweet_ansari.png
```

---

## 🛡️ 核心避坑防線 (Key Pitfalls & Best Practices)

- **UTF-8 強制編碼防護**：全命令列與 JSON 讀寫強制以 UTF-8 處理，杜絕 Windows CP950 終端亂碼或 `UnicodeEncodeError`。
- **FFmpeg zoompan 慢推死鎖陷阱**：靜態照片嚴禁加上 `-loop 1`，一律使用單幀輸入搭配內部參數 `d=幀數` 控制時間軸，避免每幀重置 zoom 變數導致畫面停格。
- **FFmpeg 管道緩衝死鎖防護**：長片編碼強制加入 `-nostats -loglevel error`，防止 Windows OS 64KB 管道被 stderr 塞滿導致子程序陷入永久卡死。
- **B-roll 無縫循環底圖防黑畫面**：輸入短片強制使用 `-stream_loop -1`，分秒無縫循環，絕不卡在最後一幀或變成黑畫面。
- **空間分層防撞車原則**：轉折字卡統一配置於上三分之一（`offsetY: -0.34`），解說字幕置於下三分之一（`offsetY: +0.38`），主播徽章錨定右上角（`x=1560, y=45`），資訊層次井然有序。
- **數學邊界動態居中 (Zero-Tofu & Zero-Overflow)**：Pillow 標籤文字一律透過 `textbbox` 動態計算左右對稱邊距（`pad_x = 24`），禁用未適配 Unicode 圖示符號，確保縮圖排版零溢出、零缺字方框。

---

## 📄 授權條款 (License)

本專案採用 [MIT License](LICENSE) 開源授權，歡迎自由修改、擴充與商業應用。
