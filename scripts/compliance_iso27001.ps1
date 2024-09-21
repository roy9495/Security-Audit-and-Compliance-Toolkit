Write-Output "Running ISO 27001 Compliance Checks..."

# 1. Check if Windows Firewall is enabled
Write-Output "Checking Windows Firewall status..."
$firewallStatus = Get-NetFirewallProfile | Where-Object { $_.Enabled -eq 'True' }

if ($firewallStatus) {
    Write-Output "PASS: Windows Firewall is enabled."
} else {
    Write-Output "FAIL: Windows Firewall is disabled."
}

# 2. Check if Remote Desktop (RDP) is disabled
Write-Output "Checking if Remote Desktop is disabled..."
$rdpStatus = Get-ItemProperty 'HKLM:\System\CurrentControlSet\Control\Terminal Server\' -Name "fDenyTSConnections"

if ($rdpStatus.fDenyTSConnections -eq 1) {
    Write-Output "PASS: Remote Desktop is disabled."
} else {
    Write-Output "FAIL: Remote Desktop is enabled."
}

# 3. Check password policy (complexity, minimum length)
Write-Output "Checking password complexity policy..."
$complexity = (Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters").RequireStrongKey
$minPasswordLength = (Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters").MinimumPasswordLength

if ($complexity -eq 1 -and $minPasswordLength -ge 8) {
    Write-Output "PASS: Password complexity is enforced and minimum length is 8 or more."
} else {
    Write-Output "FAIL: Weak password policies detected."
}

# 4. Ensure audit logging is enabled
Write-Output "Checking if audit logging is enabled..."
$auditPolicy = AuditPol /get /category:*

if ($auditPolicy -match "Logon/Logoff") {
    Write-Output "PASS: Audit logging is enabled."
} else {
    Write-Output "FAIL: Audit logging is not properly configured."
}

Write-Output "ISO 27001 Compliance Check Completed."

