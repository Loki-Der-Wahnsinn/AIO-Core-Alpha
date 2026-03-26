# 🧠 FREEDOM KI // NODE OLLAMA INSTALLER
$InstallDir = "C:\FREEDOM_NODE"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "   INSTALLING OLLAMA ON NODE ALPHA (DELL)" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

# 1. Install Ollama via Winget
Write-Host "[*] Downloading and Installing Ollama..." -ForegroundColor Yellow
winget install --id Ollama.Ollama --silent --accept-package-agreements --accept-source-agreements

# 2. Start Ollama Service
Write-Host "[*] Starting Ollama Engine..." -ForegroundColor Yellow
Start-Process "ollama.exe" -ArgumentList "serve" -WindowStyle Hidden

# 3. Pull a lightweight model for the worker (e.g. llama3:8b)
Write-Host "[*] Pulling Worker Model (llama3:8b)..." -ForegroundColor Yellow
& "ollama" pull llama3:8b

Write-Host "[OK] Node ALPHA is now a cognitive worker." -ForegroundColor Green
