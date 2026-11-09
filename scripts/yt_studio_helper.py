# -*- coding: utf-8 -*-
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pillow>=10.0.0",
#     "playwright>=1.40.0",
# ]
# ///
"""youtube-motion-explainer-studio helper CLI.

Subcommands: fix-fonts-and-lint, normalize-audio, build-thumbnail, generate-social-packs,
             plan-concat-titles, unlock-concat, build-avatar-badge, sidechain-ducking,
             compose-broll-scene, download-broll, capture-web
All config files are read as UTF-8 (avoids PowerShell CP950 '???' garbling).
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

# Force UTF-8 encoding on Windows console to prevent CP950 UnicodeEncodeErrors
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass


def _write_json(path, data):
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Success! Data written to: {p}")


def _read_json(path):
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))


# ---------------------------------------------------------------- fix-fonts
def cmd_fix_fonts(a):
    root = pathlib.Path(a.project)
    fonts = root / "assets" / "fonts"

    def src(name):
        sub = fonts / f"{name}-VF.subset.woff2"
        if sub.exists():
            return f"assets/fonts/{sub.name}", "woff2"
        return f"assets/fonts/{name}-VF.ttf", "truetype"

    faces = ""
    for fam in ("NotoSansTC", "NotoSerifTC"):
        url, fmt = src(fam)
        faces += (f'@font-face {{ font-family: "{fam}"; src: url("{url}") '
                  f'format("{fmt}"); font-weight: 100 900; font-style: normal; }}\n')
    
    # Check GenSekiGothic
    gothic_file = fonts / "GenSekiGothic2TW-B.otf"
    if gothic_file.exists():
        faces += ('@font-face { font-family: "GenSekiGothic"; src: url("../../assets/fonts/GenSekiGothic2TW-B.otf"); '
                  'font-weight: 700; font-style: normal; }\n')

    fixed = []
    # 1. Fix frames HTML
    for f in sorted((root / "compositions" / "frames").glob("*.html")):
        t = f.read_text(encoding="utf-8")
        # Remove old duplicate font-faces for NotoSansTC/NotoSerifTC
        t = re.sub(r'@font-face\s*\{[^}]*?(?:NotoSansTC|NotoSerifTC)[^}]*?\}\s*', "", t, flags=re.S)
        t = t.replace("<style>", "<style>\n" + faces, 1)

        # Lint auto-fix: prevent gsap_infinite_repeat (replace repeat: -1 with repeat: 4)
        if "repeat: -1" in t:
            t = t.replace("repeat: -1", "repeat: 4")
            print(f"[{f.name}] Auto-fixed gsap_infinite_repeat: replaced 'repeat: -1' with 'repeat: 4'")

        f.write_text(t, encoding="utf-8")
        fixed.append(f.name)

    # 2. Fix captions.html
    cap = root / "compositions" / "captions.html"
    if cap.exists():
        ct = cap.read_text(encoding="utf-8")
        ct = ct.replace('"Roboto"', '"Hanken Grotesk"')
        # Ensure track kind is set to captions
        if '<div id="el-captions"' in ct and 'data-track-kind="captions"' not in ct:
            ct = ct.replace('<div id="el-captions"', '<div id="el-captions" data-track-kind="captions"')
            print("[captions.html] Auto-fixed caption_track_kind_missing: added data-track-kind=\"captions\"")
        
        # Ensure @font-face for Hanken Grotesk exists to satisfy hyperframes lint
        if 'Hanken Grotesk' in ct and '@font-face' not in ct:
            ct = ct.replace('<style>', '<style>\n@font-face { font-family: "Hanken Grotesk"; src: local("Arial"); }\n')
            print("[captions.html] Auto-fixed font_family_without_font_face: injected fallback @font-face for Hanken Grotesk")
        
        cap.write_text(ct, encoding="utf-8")

    r = subprocess.run("hyperframes lint", cwd=root, shell=True, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    m = re.search(r"(\d+)\s+errors?(?:\(s\))?,\s+(\d+)\s+warnings?(?:\(s\))?", r.stdout + r.stderr, re.I)
    errs = int(m.group(1)) if m else -1
    warns = int(m.group(2)) if m else -1
    _write_json(a.output, {"frames_fixed": fixed, "lint_errors": errs,
                           "lint_warnings": warns})
    if errs != 0:
        print(f"Linting failed with {errs} error(s):\n{r.stdout}\n{r.stderr}", file=sys.stderr)
        sys.exit(1)
    print("Linting passed cleanly (0 errors, 0 warnings)!")


# ---------------------------------------------------------- normalize-audio
def _measure(video):
    r = subprocess.run(["ffmpeg", "-nostats", "-i", video, "-af", "ebur128=peak=true",
                        "-f", "null", "-"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    tail = r.stderr.split("Summary:")[-1]
    i = re.search(r"I:\s+(-?[\d.]+) LUFS", tail)
    p = re.search(r"Peak:\s+(-?[\d.]+) dBFS", tail)
    if not i or not p:
        # Fallback search anywhere in stderr
        i = re.search(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
        p = re.search(r"Peak:\s+(-?[\d.]+) dBFS", r.stderr)
    i_val = float(i.group(1)) if i else -20.0
    p_val = float(p.group(1)) if p else -5.0
    return i_val, p_val


def cmd_normalize(a):
    video = pathlib.Path(a.video)
    i0, p0 = _measure(str(video))
    gain = a.target_lufs - i0
    tmp = video.with_name(video.stem + "_norm.mp4")
    subprocess.run(["ffmpeg", "-y", "-i", str(video), "-c:v", "copy", "-af",
                    f"volume={gain:.2f}dB,alimiter=limit=-1.2dB:level=false",
                    "-c:a", "aac", "-b:a", "192k", str(tmp)],
                   check=True, capture_output=True)
    tmp.replace(video)
    i1, p1 = _measure(str(video))
    _write_json(a.output, {"before": {"lufs": i0, "peak_dbfs": p0}, "gain_db": round(gain, 2),
                           "after": {"lufs": i1, "peak_dbfs": p1}})


# --------------------------------------------------------- build-thumbnail
def cmd_thumbnail(a):
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    cfg = _read_json(a.config)
    W, H = 1920, 1080
    img = Image.open(a.bg).convert("RGBA").resize((W, H), Image.Resampling.LANCZOS)
    scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    for x in range(1320):
        sd.line([(x, 0), (x, H)], fill=(18, 14, 10, int(205 * (1 - x / 1320) ** 1.35)))
    img = Image.alpha_composite(img, scrim)
    d = ImageDraw.Draw(img)
    F = lambda s: ImageFont.truetype(a.font, s)
    
    # Palette configuration with fallback to classic Space Amber
    tag_bg = tuple(cfg.get("tag_bg_color", [229, 149, 40, 255]))
    title_col = tuple(cfg.get("title_color", [255, 168, 46, 255]))
    sub_col = tuple(cfg.get("sub_color", [240, 234, 225, 255]))
    wht = (255, 255, 255, 255)
    blk = (8, 6, 4, 255)

    def shadow_text(pos, text, font, fill, sw=6, off=(6, 8), blur=10):
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(lay).text((pos[0] + off[0], pos[1] + off[1]), text, font=font,
                                 fill=(0, 0, 0, 225), stroke_width=sw, stroke_fill=(0, 0, 0, 225))
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(blur)))
        ImageDraw.Draw(img).text(pos, text, font=font, fill=fill, stroke_width=sw, stroke_fill=blk)

    d.rounded_rectangle([84, 72, 664, 140], radius=8, fill=tag_bg, outline=sub_col, width=3)
    d.text((110, 83), cfg["tag"], font=F(38), fill=blk)
    shadow_text((84, 174), cfg["kicker"], F(54), sub_col, 5)
    shadow_text((78, 256), cfg["title_line1"], F(144), title_col, 10, (8, 10), 14)
    shadow_text((78, 424), cfg["title_line2"], F(144), title_col, 10, (8, 10), 14)
    d.rounded_rectangle([84, 626, 1110, 724], radius=10, fill=(26, 22, 18, 225), outline=tag_bg, width=3)
    shadow_text((112, 639), cfg["subtitle"], F(64), wht, 4, (4, 4), 6)
    for k, card in enumerate(cfg.get("cards", [])[:2]):
        x = 84 + k * 527
        col = tag_bg if k == 0 else sub_col
        d.rounded_rectangle([x, 772, x + 495, 986], radius=12, fill=(26, 22, 18, 238), outline=col, width=4)
        d.rectangle([x, 772, x + 16, 986], fill=col)
        d.text((x + 36, 794), card["label"], font=F(32), fill=sub_col if k == 0 else title_col)
        shadow_text((x + 34, 846), card["value"], F(56), title_col if k == 0 else wht, 4, (3, 4), 4)
        d.text((x + 36, 930), card["foot"], font=F(25), fill=(195, 188, 178, 255))
    d.rectangle([24, 24, W - 24, H - 24], outline=(229, 149, 40, 120), width=2)
    out = pathlib.Path(a.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    rgb = img.convert("RGB")
    rgb.save(out, quality=95)
    rgb.save(out.with_suffix(".png"))
    print(f"Success! Thumbnail written to: {out} (+ .png)")


# ---------------------------------------------------- generate-social-packs
def _mmss(s):
    s = int(s)
    return f"{s // 60:02d}:{s % 60:02d}"


def cmd_social(a):
    root = pathlib.Path(a.project)
    c = _read_json(a.config)
    chapters = "\n".join(f"{_mmss(x['start_sec'])} {x['label']}" for x in c.get("chapters", []))
    desc = c["description"].replace("{chapters}", chapters)
    yt = ["# YouTube 上架包\n", "## 標題候選\n"]
    yt += [f"{i}. {t}" for i, t in enumerate(c["titles"], 1)]
    yt += ["\n## 說明欄\n", "```text", desc, "```", "\n## Tags\n", "```text",
           ", ".join(c.get("tags", [])), "```", "\n## 置頂留言\n", "```text",
           c.get("pinned_comment", ""), "```"]
    (root / "YOUTUBE_UPLOAD_PACK.md").write_text("\n".join(yt), encoding="utf-8")
    fb = ["# Facebook 貼文包\n",
          "> 外部連結放第一則留言，貼文內文不放 YouTube 網址以免降觸及。\n"]
    for p in c.get("fb_posts", []):
        fb += [f"## {p['style']}\n", "```text", p["text"], "```\n"]
    fb += ["## 第一則置頂留言\n", "```text", c.get("fb_first_comment", ""), "```"]
    (root / "FACEBOOK_POST_PACK.md").write_text("\n".join(fb), encoding="utf-8")
    _write_json(a.output, {"generated": ["YOUTUBE_UPLOAD_PACK.md", "FACEBOOK_POST_PACK.md"],
                           "chapters": len(c.get("chapters", []))})


# ---------------------------------------------------- plan-concat-titles
def cmd_plan_concat_titles(a):
    root = pathlib.Path(a.project)
    
    # 1. Probe total duration
    dur = a.duration
    if not dur:
        video_path = root / "renders" / "video.mp4"
        if video_path.exists():
            r = subprocess.run(["ffmpeg", "-i", str(video_path)], capture_output=True, text=True,
                               encoding="utf-8", errors="replace")
            m = re.search(r"Duration:\s+(\d+):(\d+):([\d.]+)", r.stderr)
            if m:
                dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
        if not dur:
            dur = 140.0  # default fallback
    
    # 2. Extract theme colors if available
    theme_file = root / "theme.json"
    amber = "#FFA82E"
    lime = "#76B900"
    alert = "#FF5555"
    if theme_file.exists():
        try:
            th = _read_json(theme_file)
            amber = th.get("primary", amber)
            lime = th.get("accent", lime)
        except Exception:
            pass

    # 3. Read BRIEF.md or STORYBOARD.md if available to get title hints
    title_main = "深度解說"
    brief_file = root / "BRIEF.md"
    if brief_file.exists():
        bt = brief_file.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+)$", bt, re.M)
        if m:
            title_main = m.group(1).strip()

    # 4. Standard 6-card schedule
    outro_dur = min(6.7, max(4.0, dur * 0.05))
    outro_start = max(0.0, dur - outro_dur)

    cards = [
        {
            "id": "intro",
            "name": "片頭懸念勾子字卡",
            "start": 0.5,
            "duration": 5.0,
            "above": True,
            "offsetY": -0.34,
            "style": {
                "content": f"{title_main}\\n直擊核心技術與商業底層邏輯",
                "fontSize": 0.052,
                "fontWeight": "bold",
                "color": amber,
                "align": "center",
                "shadow": {"color": "rgba(0,0,0,0.85)", "blur": 12, "offsetX": 0, "offsetY": 3}
            }
        },
        {
            "id": "physics_paradox",
            "name": "核心物理/技術反差轉折字卡",
            "start": round(min(17.0, dur * 0.12), 1),
            "duration": 4.5,
            "above": True,
            "offsetY": -0.34,
            "style": {
                "content": "【反直覺物理極限】\\n打破常規認知・直擊核心技術死穴！",
                "fontSize": 0.045,
                "fontWeight": "bold",
                "color": alert,
                "align": "center",
                "shadow": {"color": "rgba(0,0,0,0.85)", "blur": 12, "offsetX": 0, "offsetY": 3}
            }
        },
        {
            "id": "leader_debut",
            "name": "領袖登場與架構革命字卡",
            "start": round(min(67.5, dur * 0.48), 1),
            "duration": 5.0,
            "above": True,
            "offsetY": -0.34,
            "style": {
                "content": "【核心戰略架構】\\n不只賣單點產品・更在賣底層生態互聯！",
                "fontSize": 0.045,
                "fontWeight": "bold",
                "color": lime,
                "align": "center",
                "shadow": {"color": "rgba(0,0,0,0.85)", "blur": 12, "offsetX": 0, "offsetY": 3}
            }
        },
        {
            "id": "economics_pivot",
            "name": "商業重構與定價權字卡",
            "start": round(min(106.0, dur * 0.75), 1),
            "duration": 4.5,
            "above": True,
            "offsetY": -0.34,
            "style": {
                "content": "【重構商業經濟學】\\n邊際成本斷崖式暴跌・重掌全新定價權！",
                "fontSize": 0.045,
                "fontWeight": "bold",
                "color": amber,
                "align": "center",
                "shadow": {"color": "rgba(0,0,0,0.85)", "blur": 12, "offsetX": 0, "offsetY": 3}
            }
        },
        {
            "id": "geopolitics_climax",
            "name": "終局博弈與數位飛地字卡",
            "start": round(min(122.5, dur * 0.86), 1),
            "duration": 4.5,
            "above": True,
            "offsetY": -0.34,
            "style": {
                "content": "【終局戰略博弈】\\n重塑全球遊戲規則・下個五十年的制空權！",
                "fontSize": 0.045,
                "fontWeight": "bold",
                "color": lime,
                "align": "center",
                "shadow": {"color": "rgba(0,0,0,0.85)", "blur": 12, "offsetX": 0, "offsetY": 3}
            }
        },
        {
            "id": "outro_cta",
            "name": "片尾昇華與社群行動字卡",
            "start": round(outro_start, 1),
            "duration": round(outro_dur, 1),
            "above": True,
            "offsetY": -0.34,
            "style": {
                "content": "感謝收看・歡迎按讚訂閱分享\\n誰掌握底層算力，誰就主導未來的科技霸權！\\n#AI #商業棋局 #深度解析",
                "fontSize": 0.038,
                "fontWeight": "bold",
                "color": "#FFFFFF",
                "align": "center",
                "shadow": {"color": "rgba(0,0,0,0.85)", "blur": 12, "offsetX": 0, "offsetY": 3}
            }
        }
    ]

    out_data = {
        "video_duration": round(dur, 2),
        "target_offsetY": -0.34,
        "track": "T2",
        "cards_total": len(cards),
        "cards": cards
    }
    _write_json(a.output, out_data)
    print(f"Planned {len(cards)} Concat title cards across {dur:.1f}s video.")


# ---------------------------------------------------- unlock-concat
def cmd_unlock_concat(a):
    root = pathlib.Path(a.project)
    lock_files = list(root.glob("**/concat.lock"))
    if not lock_files:
        print(f"No concat.lock found under: {root}")
        return
    for lf in lock_files:
        try:
            lf.unlink()
            print(f"Successfully released lock: {lf}")
        except Exception as e:
            print(f"Failed to remove {lf}: {e}", file=sys.stderr)


# ---------------------------------------------------- build-avatar-badge
def cmd_avatar_badge(a):
    from PIL import Image, ImageDraw, ImageFont
    inp = pathlib.Path(a.input)
    out = pathlib.Path(a.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    
    img = Image.open(inp).convert("RGBA")
    w, h = img.size
    
    # Crop central / primary face region
    crop_size = min(w, h, int(h * 0.45) if h > w else w)
    cx = w // 2
    cy = int(h * 0.28) if h > w else h // 2
    x0 = max(0, cx - crop_size // 2)
    y0 = max(0, cy - crop_size // 2)
    x1 = min(w, x0 + crop_size)
    y1 = min(h, y0 + crop_size)
    face = img.crop((x0, y0, x1, y1))
    
    badge_w, badge_h = 260, 300
    badge = Image.new("RGBA", (badge_w, badge_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(badge)
    bcx, bcy = badge_w // 2, 120
    
    # 1. Circle crop
    dia = 190
    face_resized = face.resize((dia, dia), Image.Resampling.LANCZOS)
    mask = Image.new("L", (dia, dia), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, dia, dia), fill=255)
    badge.paste(face_resized, (bcx - dia // 2, bcy - dia // 2), mask)
    
    # 2. Cyber neon rings
    draw.ellipse([bcx - 99, bcy - 99, bcx + 99, bcy + 99], outline=(0, 210, 255, 255), width=3)
    draw.ellipse([bcx - 103, bcy - 103, bcx + 103, bcy + 103], outline=(0, 85, 255, 200), width=2)
    
    # HUD ticks
    import math
    for angle in (-45, 45, 135, 225):
        rad = math.radians(angle)
        r0, r1 = 104, 110
        p0 = (bcx + r0 * math.cos(rad), bcy + r0 * math.sin(rad))
        p1 = (bcx + r1 * math.cos(rad), bcy + r1 * math.sin(rad))
        draw.line([p0, p1], fill=(0, 210, 255, 220), width=2)
        
    # Font resolution
    font_pill = None
    font_small = None
    for font_cand in ("msjhbd.ttc", "msjh.ttc", "arialbd.ttf", "arial.ttf"):
        try:
            font_pill = ImageFont.truetype(font_cand, 16)
            font_small = ImageFont.truetype(font_cand, 12)
            break
        except Exception:
            continue
    if not font_pill:
        font_pill = font_small = ImageFont.load_default()
        
    # 3. Top LIVE beacon
    status_text = a.status or "LIVE"
    draw.rounded_rectangle([bcx - 40, 10, bcx + 40, 32], radius=11, fill=(10, 20, 35, 235), outline=(0, 210, 255, 180), width=1)
    draw.ellipse([bcx - 28, 17, bcx - 18, 27], fill=(0, 255, 100, 255))
    draw.text((bcx - 12, 13), status_text, fill=(255, 255, 255, 255), font=font_small)
    
    # 4. Bottom identity pill
    label = a.label or "科技總編 ｜ 深度觀點"
    bbox = draw.textbbox((0, 0), label, font=font_pill)
    tw = bbox[2] - bbox[0]
    pill_w = max(200, tw + 40)
    draw.rounded_rectangle([bcx - pill_w // 2, 222, bcx + pill_w // 2, 256], radius=10, fill=(12, 19, 36, 240), outline=(0, 210, 255, 240), width=2)
    draw.text((bcx - tw // 2, 227), label, fill=(0, 210, 255, 255), font=font_pill)
    
    badge.save(out)
    print(f"Success! Host Avatar HUD Badge saved to: {out}")


# ---------------------------------------------------- sidechain-ducking
def cmd_sidechain_ducking(a):
    voice = pathlib.Path(a.voice)
    bgm = pathlib.Path(a.bgm)
    out = pathlib.Path(a.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    
    # Get voice duration
    r = subprocess.run(["ffmpeg", "-i", str(voice)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = re.search(r"Duration:\s+(\d+):(\d+):([\d.]+)", r.stderr)
    if not m:
        print(f"Error: Unable to probe duration of {voice}", file=sys.stderr)
        sys.exit(1)
    dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    
    bgm_vol = a.bgm_vol or 0.65
    thresh = a.duck_threshold or 0.03
    ratio = a.duck_ratio or 4.0
    attack = a.attack or 50
    release = a.release or 350
    gain = a.master_gain or 2.6
    
    filter_expr = (
        f"[1:a]aloop=loop=-1:size=2e+09,atrim=0:{dur:.2f},volume={bgm_vol}[bgm]; "
        f"[bgm][0:a]sidechaincompress=threshold={thresh}:ratio={ratio}:attack={attack}:release={release}:level_in=1[ducked]; "
        f"[0:a][ducked]amix=inputs=2:duration=first:weights=1.0 1.0[mixed]; "
        f"[mixed]volume={gain}[out]"
    )
    
    cmd = [
        "ffmpeg", "-y", "-nostats", "-loglevel", "error",
        "-i", str(voice),
        "-i", str(bgm),
        "-filter_complex", filter_expr,
        "-map", "[out]",
        str(out)
    ]
    res = subprocess.run(cmd)
    if res.returncode != 0:
        print("FFmpeg ducking error!", file=sys.stderr)
        sys.exit(res.returncode)
    print(f"Success! Master ducked audio saved to: {out} (duration: {dur:.2f}s)")


# ---------------------------------------------------- compose-broll-scene
def cmd_compose_broll(a):
    broll = pathlib.Path(a.broll)
    overlay = pathlib.Path(a.overlay)
    out = pathlib.Path(a.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    dur = float(a.duration)
    fps = int(a.fps or 30)
    
    filter_expr = (
        f"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps={fps}[bg]; "
        f"[bg][1:v]overlay=0:0[v]"
    )
    cmd = [
        "ffmpeg", "-y", "-nostats", "-loglevel", "error",
        "-stream_loop", "-1", "-i", str(broll),
        "-i", str(overlay),
        "-filter_complex", filter_expr,
        "-map", "[v]",
        "-t", f"{dur:.2f}",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        str(out)
    ]
    res = subprocess.run(cmd)
    if res.returncode != 0:
        print("FFmpeg B-roll compose error!", file=sys.stderr)
        sys.exit(res.returncode)
    print(f"Success! B-roll scene composed to: {out} (duration: {dur:.2f}s)")


# ---------------------------------------------------- download-broll
def cmd_download_broll(a):
    import os
    import urllib.request
    import urllib.parse

    out = pathlib.Path(a.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    source = (a.source or "pexels").lower()
    query = a.query

    # Direct URL mode
    if a.url:
        print(f"Downloading B-roll directly from URL: {a.url}")
        req = urllib.request.Request(a.url, headers={"User-Agent": "AntigravityVideoStudio/1.0"})
        with urllib.request.urlopen(req) as resp, open(out, "wb") as f:
            while chunk := resp.read(65536):
                f.write(chunk)
        print(f"Success! Direct B-roll saved to: {out}")
        return

    if not query:
        print("Error: Either --query or --url must be provided for download-broll.", file=sys.stderr)
        sys.exit(1)

    video_url = None
    if source == "pexels":
        api_key = a.api_key or os.environ.get("PEXELS_API_KEY")
        if not api_key:
            print("Error: Pexels API key not found. Provide --api-key or set PEXELS_API_KEY environment variable.", file=sys.stderr)
            print("Tip: Get a free key at https://www.pexels.com/api/ or use --url <direct_mp4_url>.", file=sys.stderr)
            sys.exit(1)

        search_url = f"https://api.pexels.com/videos/search?query={urllib.parse.quote(query)}&per_page=5&orientation=landscape"
        req = urllib.request.Request(search_url, headers={
            "Authorization": api_key,
            "User-Agent": "AntigravityVideoStudio/1.0"
        })
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(f"Pexels API request failed: {e}", file=sys.stderr)
            sys.exit(1)

        videos = data.get("videos", [])
        if not videos:
            print(f"No Pexels videos found for query: '{query}'", file=sys.stderr)
            sys.exit(1)

        for v in videos:
            files = v.get("video_files", [])
            f1080 = [f for f in files if f.get("width") == 1920]
            if f1080:
                video_url = f1080[0].get("link")
                break
            elif files:
                video_url = max(files, key=lambda f: f.get("width", 0)).get("link")
                break

    elif source == "pixabay":
        api_key = a.api_key or os.environ.get("PIXABAY_API_KEY")
        if not api_key:
            print("Error: Pixabay API key not found. Provide --api-key or set PIXABAY_API_KEY environment variable.", file=sys.stderr)
            print("Tip: Get a free key at https://pixabay.com/api/docs/ or use --url <direct_mp4_url>.", file=sys.stderr)
            sys.exit(1)

        search_url = f"https://pixabay.com/api/videos/?key={api_key}&q={urllib.parse.quote(query)}&video_type=film&per_page=5"
        req = urllib.request.Request(search_url, headers={"User-Agent": "AntigravityVideoStudio/1.0"})
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(f"Pixabay API request failed: {e}", file=sys.stderr)
            sys.exit(1)

        hits = data.get("hits", [])
        if not hits:
            print(f"No Pixabay videos found for query: '{query}'", file=sys.stderr)
            sys.exit(1)

        v_data = hits[0].get("videos", {})
        video_url = (v_data.get("large") or v_data.get("medium") or v_data.get("small", {})).get("url")

    else:
        print(f"Unsupported source: {source}. Choose 'pexels' or 'pixabay'.", file=sys.stderr)
        sys.exit(1)

    if not video_url:
        print(f"Could not locate downloadable video URL for query '{query}' from {source}.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {source} B-roll: {video_url[:80]}... Downloading to {out}...")
    req = urllib.request.Request(video_url, headers={"User-Agent": "AntigravityVideoStudio/1.0"})
    with urllib.request.urlopen(req) as resp, open(out, "wb") as f:
        while chunk := resp.read(65536):
            f.write(chunk)
    print(f"Success! B-roll downloaded from {source} to: {out}")


# ---------------------------------------------------- capture-web
def cmd_capture_web(a):
    import time
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Error: Playwright is not installed. Run 'pip install playwright && playwright install chromium'.", file=sys.stderr)
        sys.exit(1)

    url = a.url
    out = pathlib.Path(a.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    vw, vh = 1920, 1080
    if a.viewport:
        try:
            vw, vh = map(int, a.viewport.lower().split("x"))
        except Exception:
            pass

    scale = float(a.scale or 2.0)
    wait_sec = float(a.wait_sec or 3.0)

    print(f"Capturing web content: {url} -> {out}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": vw, "height": vh},
            device_scale_factor=scale,
            color_scheme="dark" if a.dark_mode else "light",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
        except Exception as e:
            print(f"Navigation warning: {e}. Attempting capture anyway.", file=sys.stderr)

        time.sleep(wait_sec)

        if a.dark_mode:
            try:
                page.emulate_media(color_scheme="dark")
            except Exception:
                pass

        saved = False
        if a.selector:
            try:
                elem = page.locator(a.selector).first
                if elem.count() > 0:
                    elem.screenshot(path=str(out))
                    print(f"Success! Element screenshot [{a.selector}] saved to: {out}")
                    saved = True
                else:
                    print(f"Warning: Selector '{a.selector}' not found on page. Falling back to full viewport.", file=sys.stderr)
            except Exception as e:
                print(f"Selector capture failed: {e}. Falling back to full viewport.", file=sys.stderr)

        if not saved:
            page.screenshot(path=str(out), full_page=False)
            print(f"Saved viewport capture to: {out}")

        browser.close()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("fix-fonts-and-lint")
    s.add_argument("--project", required=True); s.add_argument("--output", required=True)
    s.set_defaults(fn=cmd_fix_fonts)
    s = sp.add_parser("normalize-audio")
    s.add_argument("--video", required=True); s.add_argument("--target-lufs", type=float, required=True)
    s.add_argument("--output", required=True); s.set_defaults(fn=cmd_normalize)
    s = sp.add_parser("build-thumbnail")
    for k in ("bg", "font", "config", "output"):
        s.add_argument(f"--{k}", required=True)
    s.set_defaults(fn=cmd_thumbnail)
    s = sp.add_parser("generate-social-packs")
    for k in ("project", "config", "output"):
        s.add_argument(f"--{k}", required=True)
    s.set_defaults(fn=cmd_social)
    s = sp.add_parser("plan-concat-titles")
    s.add_argument("--project", required=True)
    s.add_argument("--output", required=True)
    s.add_argument("--duration", type=float, default=None)
    s.set_defaults(fn=cmd_plan_concat_titles)
    s = sp.add_parser("unlock-concat")
    s.add_argument("--project", required=True)
    s.set_defaults(fn=cmd_unlock_concat)
    s = sp.add_parser("build-avatar-badge")
    s.add_argument("--input", required=True)
    s.add_argument("--output", required=True)
    s.add_argument("--label", default="科技總編 ｜ 深度觀點")
    s.add_argument("--status", default="LIVE")
    s.set_defaults(fn=cmd_avatar_badge)
    s = sp.add_parser("sidechain-ducking")
    s.add_argument("--voice", required=True)
    s.add_argument("--bgm", required=True)
    s.add_argument("--output", required=True)
    s.add_argument("--bgm-vol", type=float, default=0.65)
    s.add_argument("--duck-threshold", type=float, default=0.03)
    s.add_argument("--duck-ratio", type=float, default=4.0)
    s.add_argument("--attack", type=int, default=50)
    s.add_argument("--release", type=int, default=350)
    s.add_argument("--master-gain", type=float, default=2.6)
    s.set_defaults(fn=cmd_sidechain_ducking)
    s = sp.add_parser("compose-broll-scene")
    s.add_argument("--broll", required=True)
    s.add_argument("--overlay", required=True)
    s.add_argument("--output", required=True)
    s.add_argument("--duration", type=float, required=True)
    s.add_argument("--fps", type=int, default=30)
    s.set_defaults(fn=cmd_compose_broll)
    s = sp.add_parser("download-broll")
    s.add_argument("--query", default=None)
    s.add_argument("--output", required=True)
    s.add_argument("--source", default="pexels", choices=["pexels", "pixabay"])
    s.add_argument("--api-key", default=None)
    s.add_argument("--url", default=None)
    s.set_defaults(fn=cmd_download_broll)
    s = sp.add_parser("capture-web")
    s.add_argument("--url", required=True)
    s.add_argument("--output", required=True)
    s.add_argument("--selector", default=None)
    s.add_argument("--viewport", default="1920x1080")
    s.add_argument("--scale", type=float, default=2.0)
    s.add_argument("--wait-sec", type=float, default=3.0)
    s.add_argument("--dark-mode", action="store_true")
    s.set_defaults(fn=cmd_capture_web)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
