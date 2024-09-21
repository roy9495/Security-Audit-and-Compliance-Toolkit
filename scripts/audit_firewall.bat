@echo off

echo "Firewall Status:"
netsh advfirewall show allprofiles

echo.
echo "Open Ports (Listening):"
netstat -an | findstr LISTENING
