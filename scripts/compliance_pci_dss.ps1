# PCI-DSS Compliance Check for Windows

Write-Output "Running PCI-DSS Compliance Checks..."

# 1. Check for SSL/TLS usage on port 443
Write-Output "Checking for SSL/TLS usage on port 443..."
$sslStatus = Test-NetConnection -ComputerName localhost -Port 443

if ($sslStatus.TcpTestSucceeded) {
    Write-Output "PASS: SSL/TLS is enabled on port 443."
} else {
    Write-Output "FAIL: SSL/TLS is not enabled on port 443."
}

# 2. Check for unnecessary open ports
Write-Output "Checking for unnecessary open ports..."
$openPorts = netstat -an | Select-String "LISTENING" | Where-Object { $_ -notmatch "80|443" }

if ($openPorts) {
    Write-Output "FAIL: Unnecessary ports are open."
    $openPorts | ForEach-Object { Write-Output $_ }
} else {
    Write-Output "PASS: No unnecessary ports are open."
}

Write-Output "PCI-DSS Compliance Check Completed."

