@echo off
echo Listing all active sessions (including remote):
where quser >nul 2>nul
if %errorlevel% equ 0 (
    quser
) else (
    query user 2>nul
)

echo.
echo Active System Console User:
powershell -NoProfile -Command "Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -ExpandProperty UserName"

echo.
echo Registered Local Accounts:
net user