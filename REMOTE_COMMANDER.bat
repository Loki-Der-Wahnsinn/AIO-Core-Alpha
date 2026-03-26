@echo off
title FREEDOM MASTER // COMMANDER UPLINK
color 0c
echo ============================================================
echo        FREEDOM MASTER COMMANDER // UPLINK TO NODE ALPHA
echo ============================================================
echo.
echo [*] Target: 192.168.188.77 (Dell Optiplex)
echo.
set /p command="Enter Remote Command: "
echo.
echo [*] Sending Command: %command%
powershell -Command "$client = New-Object System.Net.Sockets.TcpClient('192.168.188.77', 4444); $stream = $client.GetStream(); $writer = New-Object System.IO.StreamWriter($stream); $writer.Write('%command%'); $writer.Flush(); $client.Close();"
echo [OK] Command Injected.
pause
