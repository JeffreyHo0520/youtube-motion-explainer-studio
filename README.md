# YouTube & Facebook Flagship Motion Explainer Studio (`youtube-motion-explainer-studio`)

> **End-to-end Automated Production Pipeline for YouTube & Facebook Motion Explainer Videos**  
> HyperFrames 1080p + Traditional Chinese Neural Narration & Waveform Captions + 3-Color Theme & GenSekiGothic Bold + Live-Action Realism & Historical Archives Dual Mode + NASA/SpaceX Public Domain Asset Harvester + Ken Burns Slow Zoom + HTML5 Canvas & Python Code-Driven Physics Motion + Zero-NLE Seamless FFmpeg Concat + Concat MCP Automated Title Cards & 1080p Export + Full-Motion B-roll Video Background Loop + Cyberpunk Host Avatar HUD Badge + Broadcast-grade Deep Tech Sidechain Audio Ducking + Mathematically Centered Typography + Rich GSAP Motion Components + Visual Review Loop + EBU R128 -14.0 LUFS Loudness Calibration + 16:9 High-CTR Thumbnails & YouTube/Facebook Publishing Packs + Antigravity Web Research & Storyboard JSON Pipeline + Pexels/Pixabay B-roll Pipeline + Playwright Headless Tweet/Bill Snippet Capture.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Package Manager: uv](https://img.shields.io/badge/uv-Astral-purple.svg)](https://astral.sh/uv)
[![HyperFrames](https://img.shields.io/badge/Render-HyperFrames%201080p-orange)](https://github.com/heygen-com/hyperframes)
[![Audio](https://img.shields.io/badge/Audio-EBU%20R128%20--14.0%20LUFS-green)](https://en.wikipedia.org/wiki/EBU_R_128)
[![Concat MCP](https://img.shields.io/badge/NLE-Concat%20MCP-red)](https://github.com/JeffreyHo0520/concat-video-editor)

---

## 📖 Overview

`youtube-motion-explainer-studio` is a fully automated, fail-safe, end-to-end production studio tailored for AI coding agents (Google Antigravity, Claude Code, OpenAI Codex, Cursor). It integrates in-depth research, 1080p motion animation generation, high-CTR YouTube thumbnails, and multi-platform social media distribution kits into a single zero-breakage workflow.

Triggered whenever the user asks for:
- "Make a motion explainer video and package YouTube + Facebook upload assets"
- "Business tech, corporate war, or deep historical explainer workflow"
- "Live-action documentary realism ('我要是真人')"
- "Replace background with dynamic looping B-roll video"
- "Add a host avatar HUD badge in the corner"
- "Background music with broadcast-grade sidechain audio ducking"
- "Automated title cards via Concat MCP"
- "Web research for legislation/news outputting structured storyboard JSON"
- "Auto-download Pexels/Pixabay stock B-roll"
- "Playwright headless snippet capture for X tweets or legislative bills"

---

## 🌟 6 Core Visual & Production Modules

1. **Mode A: Live-Action & Real Person Realism ("我要是真人")**
   - 100% photorealistic documentary aesthetic, eliminating anime, cartoon, or flat-vector styles.
   - Genuine tech leader presentations (Jensen Huang, Elon Musk, Sam Altman), orbital satellites, cleanroom engineers, and command center panoramas.
   - Dynamic motion components: volumetric spotlights, lidar scanlines, HUD corner brackets, data shrink bars, strikethrough price drops, bit-flip shakes, and thermal radiation heatwaves.

2. **Mode B: Historical Archive Mode**
   - Multi-source battle archive cross-verification, Wikimedia Commons CC0 historical records, duotone military maps, animated troop badges, and Colab G4 MiniMax H3 photorealistic clips.

3. **Mode C: Real-Footage & Code-Driven Motion Pipeline**
   - **Public Domain Asset Harvester**: Automated Python querying of the official NASA Image & Video Library API for CC0/Public Domain footage.
   - **Ken Burns Cinematic Zoom**: Smooth, film-grade slow zoom via FFmpeg `zoompan` for high-resolution static photos without frame freezing.
   - **On-the-fly Code-Driven Physics Animation**: HTML5 Canvas or Python-rendered 1080p particle simulations for complex mechanics (e.g., Ullage Thrust, orbital docking).
   - **Zero-NLE FFmpeg Concatenation**: Code-only seamless splicing of live footage, diagrams, and custom physics animations with burnt-in subtitles.
   - **Dual-Track Cover System**: Timeline opening card + MP4 container attached picture (`attached_pic`) metadata.

4. **Module D: Concat MCP Automated Title Cards & Post-Production Pipeline**
   - **Headless Video NLE Automation**: Direct JSON-RPC control over local Concat video editor without opening GUI.
   - **6-Card Strategic Matrix**: Hook card, physics twist, leader entrance, economic model/pricing power, aerospace endgame, and outro CTA.
   - **Upper-Third Safe Zone (`offsetY: -0.34`)**: Positioned cleanly above subtitles (`offsetY: +0.38`), eliminating visual overlap.
   - **Real-time Frame Preview**: Automatic PNG frame extraction before export to audit typography and layout.
   - **Asynchronous 1080p Export & Safe Lock Release**: Background encoding with polling and automatic removal of `concat.lock`.

5. **Mode E: Dynamic B-roll & Host HUD News Pipeline**
   - **Dynamic B-roll Video Background**: 1080p full-screen background video with seamless loop (`-stream_loop -1`) overlaid with 80% opacity translucent glassmorphism cards (`rgba(12, 19, 36, 210)`).
   - **Cyberpunk Host Avatar HUD Badge**: 260x300 circular avatar badge with dual neon rings, top `🟢 LIVE` beacon, and bottom identity pill anchored at top-right (`x=1560, y=45`).
   - **Broadcast-Grade Deep Tech Sidechain Ducking**: 124 BPM audible Deep Tech synth groove; BGM ducks to `0.22` (-13dB) during speech and smoothly recovers to `0.65` in 350ms, meeting EBU R128 `-14.0 LUFS`.
   - **Mathematical Centering & Symmetric Badges**: Centered card typography with dynamic `textbbox` padding (`pad_x = 24`), preventing text overflow.

6. **Mode F: Policy News, Legislation & Tweet Pipeline**
   - **Antigravity Web Research & Storyboard JSON**: Automated querying of Congress.gov, GPO, policy whitepapers, and X posts to extract compute thresholds and legal penalties into a standardized `storyboard.json`.
   - **Pexels & Pixabay Commercial B-roll Harvester**: Automated batch querying and downloading of 1080p landscape royalty-free B-roll clips to `assets/broll/`.
   - **Playwright Headless Snippet Capture**: 2x Retina headless Chromium capturing dark-mode X tweets and bill text snippets with CSS selector precision.

---

## 🚀 Cross-Machine Installation

Install this skill on any computer using one of the methods below:

### Method 1: Git Clone Directly into Antigravity Skills Directory (Recommended)

#### Windows (PowerShell):
```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.gemini\config\skills"
git clone https://github.com/JeffreyHo0520/youtube-motion-explainer-studio.git "$HOME\.gemini\config\skills\youtube-motion-explainer-studio"
```

#### macOS / Linux:
```bash
mkdir -p ~/.gemini/config/skills
git clone https://github.com/JeffreyHo0520/youtube-motion-explainer-studio.git ~/.gemini/config/skills/youtube-motion-explainer-studio
```

---

### Method 2: One-Click Installer Script (Supports Antigravity, Claude Code & Codex)

Clone to any workspace and run the installer:

#### Windows (PowerShell):
```powershell
git clone https://github.com/JeffreyHo0520/youtube-motion-explainer-studio.git
cd youtube-motion-explainer-studio
.\install.ps1
```
*Use `.\install.ps1 -Force` to overwrite existing installations, or `-Dest "C:\your\skills"` for a custom location.*

#### macOS / Linux:
```bash
git clone https://github.com/JeffreyHo0520/youtube-motion-explainer-studio.git
cd youtube-motion-explainer-studio
chmod +x install.sh
./install.sh
```

---

## 📦 Directory Structure

```text
youtube-motion-explainer-studio/
├── SKILL.md                 # Full skill specifications, 8-phase workflow, and 19-pitfall defense guide
├── README.md                # English documentation
├── README.zh-TW.md          # Traditional Chinese documentation
├── LICENSE                  # MIT License
├── install.ps1              # Windows one-click installer & dependency checker
├── install.sh               # macOS / Linux one-click installer & dependency checker
├── .gitignore               # Ignored cache, temp, and rendering files
└── scripts/
    └── yt_studio_helper.py  # Full-featured CLI utility (UTF-8 safe, PEP 723 inline dependencies)
```

---

## ⚡ CLI Helper Reference (`scripts/yt_studio_helper.py`)

Equipped with PEP 723 inline dependency metadata. Executing via `uv run` **automatically resolves Pillow and Playwright on the fly** without manual virtualenv management:

```powershell
# 1. Lint fix: CJK @font-face, track kind, and repeat:-1 termination
uv run scripts/yt_studio_helper.py fix-fonts-and-lint --project . --output renders/lint_status.json

# 2. Lossless EBU R128 audio normalization to -14.0 LUFS (-c:v copy preserves video stream)
uv run scripts/yt_studio_helper.py normalize-audio --video renders/video.mp4 --target-lufs -14.0 --output renders/audio_loudness.json

# 3. High-CTR 16:9 YouTube thumbnail generator with mathematical centering
uv run scripts/yt_studio_helper.py build-thumbnail --bg assets/images/gen/youtube_thumbnail_bg.jpg --font assets/fonts/GenSekiGothic2TW-B.otf --config thumbnail_spec.json --output renders/youtube_thumbnail.jpg

# 4. Generate YouTube Upload Pack, Facebook Post Pack & delivery report from STORYBOARD.md
uv run scripts/yt_studio_helper.py generate-social-packs --project . --config social_spec.json --output social_pack_manifest.json

# 5. Plan Concat 6-card title matrix for Upper-Third safe zone (offsetY: -0.34)
uv run scripts/yt_studio_helper.py plan-concat-titles --project . --output concat_titles_plan.json

# 6. Safely unlock lingering concat.lock from previous aborted edits
uv run scripts/yt_studio_helper.py unlock-concat --project .

# 7. Generate 260x300 cyberpunk host avatar HUD badge from character portrait
uv run scripts/yt_studio_helper.py build-avatar-badge --input assets/character_sheet.jpg --output renders/host_avatar_badge.png --label "科技總編 ｜ 深度觀點"

# 8. Broadcast-grade sidechain audio ducking via native FFmpeg sidechain compression
uv run scripts/yt_studio_helper.py sidechain-ducking --voice renders/full_narration.wav --bgm assets/audio/bgm_deep_tech.wav --output renders/master_ducked_audio.wav

# 9. Compose dynamic B-roll loop (-stream_loop -1) with translucent centered cards
uv run scripts/yt_studio_helper.py compose-broll-scene --broll assets/broll/datacenter.mp4 --overlay cards/scene_1.png --duration 11.88 --output renders/scene_1.mp4

# 10. Auto-download 1080p landscape royalty-free B-roll from Pexels / Pixabay
uv run scripts/yt_studio_helper.py download-broll --query "datacenter server rack" --output assets/broll/datacenter.mp4 --source pexels

# 11. Playwright headless capture for dark-mode X tweets or official bills (2x Retina)
uv run scripts/yt_studio_helper.py capture-web --url "https://x.com/RepYassAnsari/status/2118054336077127797" --selector "article[data-testid='tweet']" --dark-mode --output assets/snippets/tweet_ansari.png
```

---

## 🛡️ Key Pitfalls & Best Practices

- **UTF-8 Enforcement**: All CLI streams and JSON files enforce UTF-8 to eliminate CP950 `UnicodeEncodeError` on Windows consoles.
- **FFmpeg zoompan Deadlock**: Never use `-loop 1` on static images; always use single-frame input with internal `d=FRAMES` to avoid zoom reset loops.
- **FFmpeg Pipe Deadlock**: Added `-nostats -loglevel error` to prevent the Windows OS 64KB stderr pipe buffer from freezing long renders.
- **B-roll Loop Black Screen Defense**: Compulsory `-stream_loop -1` before video inputs ensures zero black screen freezes on short B-roll clips.
- **Spatial Safe Zoning**: Title cards locked to `offsetY: -0.34`, subtitles at `offsetY: +0.38`, and host avatar badge at top-right (`x=1560, y=45`).
- **Mathematical Centering (Zero-Tofu)**: Dynamic bounding box measurement via `draw.textbbox` ensures exact padding (`pad_x = 24`) and eliminates unmapped glyph boxes (`□`).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
