#!/usr/bin/env bash
set -Eeuo pipefail

SKILL_NAME="youtube-motion-explainer-studio"
REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
FORCE=0
SKILLS_ROOT=""

usage() {
  cat <<'EOF'
Install the youtube-motion-explainer-studio skill into Antigravity, Claude Code, or Codex skills directories.

Usage:
  ./install.sh [--dest SKILLS_DIR] [--force]

Options:
  --dest PATH  Skills directory to use (e.g. ~/.gemini/config/skills or ~/.claude/skills)
  --force      Replace an existing install after moving it to a timestamped backup
  -h, --help   Show this help
EOF
}

while (($#)); do
  case "$1" in
    --dest)
      (($# >= 2)) || { echo "Missing path after --dest." >&2; usage >&2; exit 2; }
      SKILLS_ROOT="$2"
      shift 2
      ;;
    --force)
      FORCE=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

DEST_DIRS=()
if [[ -n "$SKILLS_ROOT" ]]; then
  DEST_DIRS+=("$SKILLS_ROOT")
else
  # Default destinations
  DEST_DIRS+=("$HOME/.gemini/config/skills")
  if [[ -d "$HOME/.claude" ]]; then
    DEST_DIRS+=("$HOME/.claude/skills")
  fi
  if [[ -n "${CODEX_HOME:-}" ]]; then
    DEST_DIRS+=("$CODEX_HOME/skills")
  elif [[ -d "$HOME/.codex" ]]; then
    DEST_DIRS+=("$HOME/.codex/skills")
  fi
fi

for dest_root in "${DEST_DIRS[@]}"; do
  mkdir -p "$dest_root"
  target="$dest_root/$SKILL_NAME"

  if [[ -d "$target" ]]; then
    if (( FORCE == 0 )); then
      echo "Skill already exists at: $target (Use --force to overwrite)"
      continue
    fi
    timestamp="$(date -u +%Y%m%dT%H%M%SZ)"
    backup="${target}.backup.${timestamp}"
    mv "$target" "$backup"
    echo "Backed up existing installation to: $backup"
  fi

  mkdir -p "$target"
  cp "$REPO_DIR/SKILL.md" "$target/"
  [[ -f "$REPO_DIR/README.md" ]] && cp "$REPO_DIR/README.md" "$target/"
  [[ -f "$REPO_DIR/README.zh-TW.md" ]] && cp "$REPO_DIR/README.zh-TW.md" "$target/"
  [[ -f "$REPO_DIR/LICENSE" ]] && cp "$REPO_DIR/LICENSE" "$target/"
  [[ -d "$REPO_DIR/scripts" ]] && cp -r "$REPO_DIR/scripts" "$target/"

  echo "Successfully installed $SKILL_NAME to $target"
done

echo ""
echo "=== Environment & Toolchain Status Check ==="
if command -v uv >/dev/null 2>&1; then
  echo "[✓] uv detected: $(command -v uv)"
else
  echo "[!] 'uv' not found in PATH. Install via: curl -LsSf https://astral.sh/uv/install.sh | sh"
fi

if command -v ffmpeg >/dev/null 2>&1; then
  echo "[✓] ffmpeg detected: $(command -v ffmpeg)"
else
  echo "[!] 'ffmpeg' not found in PATH. Essential for audio normalization, zoompan & sidechain ducking."
fi

if command -v python3 >/dev/null 2>&1; then
  echo "[✓] Python 3 detected: $(command -v python3)"
elif command -v python >/dev/null 2>&1; then
  echo "[✓] Python detected: $(command -v python)"
else
  echo "[!] Python not found in PATH."
fi

echo ""
echo "Installation completed! Restart your agent or start a new chat session to activate $SKILL_NAME."
