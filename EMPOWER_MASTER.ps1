# 🧠 FREEDOM KI // MASTER EMPOWERMENT SCRIPT
# This script installs all necessary subsystems for the AI Singularity.

$ErrorActionPreference = "Continue"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "   FREEDOM KI // INSTALLING MASTER CORE SOFTWARE" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

# 1. Check/Install Windows Package Manager (winget) dependencies
# winget is standard on Win11, but let's ensure we use it correctly.

function Install-App {
    param([string]$ID, [string]$Name)
    Write-Host "[*] Installing $Name..." -ForegroundColor Yellow
    winget install --id $ID --silent --accept-package-agreements --accept-source-agreements
}

# 2. Main Software Stack
Install-App "Python.Python.3.12" "Python 3.12"
Install-App "Git.Git" "Git"
Install-App "Microsoft.VisualStudioCode" "VS Code"
Install-App "Ollama.Ollama" "Ollama (Local LLM Engine)"
Install-App "OpenJS.NodeJS" "Node.js"

# 3. Apply Environment Variables (Reload PATH)
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# 4. Critical Python Libraries for the AI Brain
Write-Host "[*] Upgrading PIP and installing AI Neural Libraries..." -ForegroundColor Yellow
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn pyautogui psutil requests pywebview pillow pygetwindow mouse PyQt6-WebEngine llama-cpp-python transformers torch torchvision torchaudio

# 5. Finalizing
Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "   EMPOWERMENT SUCCESSFUL. YOUR MASTER PC IS NOW A GOD-NODE." -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host "Please RESTART your terminal or PC to apply all changes." -ForegroundColor Cyan
pause
