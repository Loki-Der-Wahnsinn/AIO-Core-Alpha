@echo off
title FREEDOM KI // NETWORK HANDSHAKE (.77)
color 0a
echo ============================================================
echo        AUTONOMOUS REMOTE DEPLOYMENT (NODE: LOKI)
echo ============================================================
echo.
echo [*] Target: 192.168.188.77 (Loki.fritz.box)
echo [*] Local:  192.168.188.20 (Master)
echo.
echo [!] This will attempt to push the KI-DNA over the network.
echo [!] You will need to enter the credentials of the Dell Optiplex.
echo.

set /p target_user="Enter Username on Dell (e.g. Loki): "
set /p target_pass="Enter Password on Dell (will be shown): "

echo.
echo [*] Attempting Network Handshake...
net use \\192.168.188.77\C$ /user:%target_user% %target_pass%

if %errorLevel% == 0 (
    echo [OK] HANDSHAKE SUCCESSFUL. DRIVE MAPPED.
    echo [*] Injecting Freedom Core to C:\FREEDOM_NODE...
    mkdir \\192.168.188.77\C$\FREEDOM_NODE
    xcopy /E /Y "C:\FREEDOM_KI\DEPLOYMENT_STICK\*" "\\192.168.188.77\C$\FREEDOM_NODE\"
    echo.
    echo [SUCCESS] Freedom DNA has been remotely injected.
    echo [!] Go to the Dell Optiplex and run C:\FREEDOM_NODE\START_NODE.bat
    net use \\192.168.188.77\C$ /delete /y
) else (
    echo [FAIL] Handshake rejected. Check Credentials or SMB Settings.
    echo [TIP]  Use the USB Stick method in 'C:\FREEDOM_KI\DEPLOYMENT_STICK'
)

pause
