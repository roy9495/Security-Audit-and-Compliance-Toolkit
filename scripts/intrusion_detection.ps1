Write-Output "Intrusion Detection Check..."

# Detect failed login attempts in Event Viewer (Event ID 4625)
$failedLogins = Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4625} | Select-Object -First 10
if ($failedLogins) {
    Write-Output "Warning: Found failed login attempts!"
    $failedLogins | Format-List | Write-Output
} else {
    Write-Output "PASS: No failed login attempts found."
}

# Check for suspicious process creations (Event ID 4688)
$suspiciousProcesses = Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4688} | Where-Object { $_.Message -like '*powershell.exe*' -or $_.Message -like '*cmd.exe*' }
if ($suspiciousProcesses) {
    Write-Output "Warning: Found suspicious processes created!"
    $suspiciousProcesses | Format-List | Write-Output
} else {
    Write-Output "PASS: No suspicious processes found."
}
