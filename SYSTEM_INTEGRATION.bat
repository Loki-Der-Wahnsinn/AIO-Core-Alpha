@echo off
setlocal
title FREEDOM KI // SYSTEM REGISTRY INITIALIZER
color 0b

echo ============================================================
echo   FREEDOM KI // AGENT SYSTEM INTEGRATION
echo ============================================================
echo.

:: 1. Persistent Environment Variables
echo [*] Setting Global Environment Variables...
setx FREEDOM_KI_ROOT "P:\FREEDOM_KI" /M
setx FREEDOM_KI_CONFIG "P:\FREEDOM_KI\config.json" /M
setx FREEDOM_KI_WORKSPACE "P:\FREEDOM_KI\workspace" /M
setx FREEDOM_KI_KNOWLEDGE "P:\FREEDOM_KI\knowledge_base" /M

:: 2. Registry Tweaks (Performance & UI)
echo [*] Applying Registry Performance Tweaks...
:: Increase Max Path support for deep knowledge structures
reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f

:: 3. Startup Entry (Optional high-level access)
echo [*] Creating Master Startup Entry...
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "FREEDOM_KI_MASTER" /t REG_SZ /d "P:\FREEDOM_KI\START_FREEDOM_MASTER.bat" /f

:: 4. User Policy Elevation (Administrative Context for AI)
echo [*] Configuring User Policy for FREEDOM_KI...
:: Enable script execution without confirmation
powershell -Command "Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope LocalMachine -Force"

echo.
echo [OK] SYSTEM INTEGRATION COMPLETE.
echo [!] FREEDOM_KI is now a top-level system entity.
echo.
pause
