<#
.SYNOPSIS
    Installs the youtube-motion-explainer-studio skill into Antigravity, Claude Code, and Codex skills directories.
.USAGE
    .\install.ps1
    .\install.ps1 -Dest "C:\custom\skills"
    .\install.ps1 -Force
#>
[CmdletBinding()]
param(
    [string]$Dest,
    [switch]$Force
)

$skillName = "youtube-motion-explainer-studio"
$repoDir = Split-Path -Parent $MyInvocation.MyCommand.Path

$destDirs = @()
if ($Dest) {
    $destDirs += $Dest
} else {
    $userHome = $env:USERPROFILE
    $geminiSkills = Join-Path $userHome ".gemini\config\skills"
    $claudeSkills = Join-Path $userHome ".claude\skills"
    $codexSkills = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME "skills" } else { Join-Path $userHome ".codex\skills" }

    # Always install to Antigravity
    $destDirs += $geminiSkills

    # Install to Claude or Codex if their directories or configurations exist
    if (Test-Path (Join-Path $userHome ".claude") -or (Test-Path $claudeSkills)) {
        $destDirs += $claudeSkills
    }
    if (Test-Path (Join-Path $userHome ".codex") -or $env:CODEX_HOME) {
        $destDirs += $codexSkills
    }
}

foreach ($skillsRoot in $destDirs) {
    if (-not (Test-Path $skillsRoot)) {
        New-Item -ItemType Directory -Path $skillsRoot -Force | Out-Null
    }

    $target = Join-Path $skillsRoot $skillName
    if (Test-Path $target) {
        if (-not $Force) {
            Write-Host "Skill already exists at: $target (Use -Force to overwrite)" -ForegroundColor Yellow
            continue
        }
        $timestamp = (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssZ")
        $backup = "$target.backup.$timestamp"
        Move-Item -Path $target -Destination $backup -Force
        Write-Host "Backed up previous installation to: $backup" -ForegroundColor Cyan
    }

    New-Item -ItemType Directory -Path $target -Force | Out-Null
    Copy-Item (Join-Path $repoDir "SKILL.md") -Destination $target -Force
    if (Test-Path (Join-Path $repoDir "README.md")) {
        Copy-Item (Join-Path $repoDir "README.md") -Destination $target -Force
    }
    if (Test-Path (Join-Path $repoDir "README.zh-TW.md")) {
        Copy-Item (Join-Path $repoDir "README.zh-TW.md") -Destination $target -Force
    }
    if (Test-Path (Join-Path $repoDir "LICENSE")) {
        Copy-Item (Join-Path $repoDir "LICENSE") -Destination $target -Force
    }
    if (Test-Path (Join-Path $repoDir "scripts")) {
        Copy-Item (Join-Path $repoDir "scripts") -Destination $target -Recurse -Force
    }

    Write-Host "[✓] Successfully installed $skillName to $target" -ForegroundColor Green
}

# Environment & Dependencies Check
Write-Host ""
Write-Host "=== Environment & Toolchain Status Check ===" -ForegroundColor Cyan

# 1. uv check
$uvCmd = Get-Command "uv" -ErrorAction SilentlyContinue
if ($uvCmd) {
    Write-Host "[✓] uv detected: $($uvCmd.Source)" -ForegroundColor Green
} else {
    Write-Host "[!] 'uv' not found in PATH. Install via: irm https://astral.sh/uv/install.ps1 | iex" -ForegroundColor Yellow
}

# 2. ffmpeg check
$ffmpegCmd = Get-Command "ffmpeg" -ErrorAction SilentlyContinue
if ($ffmpegCmd) {
    Write-Host "[✓] ffmpeg detected: $($ffmpegCmd.Source)" -ForegroundColor Green
} else {
    Write-Host "[!] 'ffmpeg' not found in PATH. Essential for audio normalization, zoompan & sidechain ducking." -ForegroundColor Yellow
}

# 3. python check
$pythonCmd = Get-Command "python" -ErrorAction SilentlyContinue
if ($pythonCmd) {
    Write-Host "[✓] Python detected: $($pythonCmd.Source)" -ForegroundColor Green
} else {
    Write-Host "[!] 'python' not found in PATH." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Installation completed! Restart your agent or start a new chat session to activate $skillName." -ForegroundColor Green
