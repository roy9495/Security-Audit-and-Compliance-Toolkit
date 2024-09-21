Write-Output "System Hardening Check..."

# Check for password policy (complexity)
$PasswordPolicy = Get-ADDefaultDomainPasswordPolicy
if ($PasswordPolicy.ComplexityEnabled) {
    Write-Output "PASS: Password complexity is enabled."
} else {
    Write-Output "FAIL: Password complexity is disabled."
}

# Check if remote desktop is disabled
$RemoteDesktop = Get-ItemProperty 'HKLM:\System\CurrentControlSet\Control\Terminal Server\' -Name "fDenyTSConnections"
if ($RemoteDesktop.fDenyTSConnections -eq 1) {
    Write-Output "PASS: Remote desktop is disabled."
} else {
    Write-Output "FAIL: Remote desktop is enabled."
}
