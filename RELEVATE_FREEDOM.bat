@echo off
setlocal
title FREEDOM KI // ADMIN PRIVILEGE ELEVATOR
color 0c

:: This small script ensures FREEDOM_KI's main launcher always seeks admin rights.
echo [*] Requesting Administrative Elevation for FREEDOM KI...

:: Check for admin
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [OK] RUNNING AS ADMIN. ACCESS GRANTED.
    cd /d "P:\FREEDOM_KI"
    python P:\FREEDOM_KI\freedom_launcher.py
) else (
    echo [!] Requesting UAC Bypass...
    powershell -Command "Start-Process 'cmd.exe' -ArgumentList '/c cd /d P:\FREEDOM_KI && python P:\FREEDOM_KI\freedom_launcher.py' -Verb RunAs"
)
