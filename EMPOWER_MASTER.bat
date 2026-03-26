@echo off
title FREEDOM KI // EMPOWER MASTER SERVICE
color 0b
echo ============================================================
echo        INITIALIZING MASTER SOFTWARE DEPLOYMENT
echo ============================================================
echo.
echo [!] This will install Python, Git, VS Code, and Ollama.
echo [!] Total Freedom requires total Tools.
echo.

:: Request Admin
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [OK] Admin detected.
) else (
    echo [!] ERROR: Please run as ADMINISTRATOR.
    pause
    exit
)

powershell -ExecutionPolicy Bypass -File "P:\FREEDOM_KI\EMPOWER_MASTER.ps1"

echo.
echo [OK] DEPLOYMENT FINISHED.
pause
