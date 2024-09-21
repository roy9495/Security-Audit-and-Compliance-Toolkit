Write-Output "Privilege Escalation Test..."

# Check if current user has admin privileges
if ([Security.Principal.WindowsIdentity]::GetCurrent().Groups -match "S-1-5-32-544") {
    Write-Output "Warning: User has local administrator privileges."
} else {
    Write-Output "PASS: User does not have local administrator privileges."
}

# Check for weak service permissions (can lead to privilege escalation)
$services = Get-WmiObject win32_service | Where-Object { $_.StartMode -eq 'Auto' -and $_.State -eq 'Running' }
foreach ($service in $services) {
    $permissions = Get-Acl "HKLM:\SYSTEM\CurrentControlSet\Services\$($service.Name)"
    if ($permissions.Access | Where-Object { $_.IdentityReference -eq 'Everyone' -or $_.IdentityReference -eq 'Authenticated Users' }) {
        Write-Output "Warning: Service $($service.Name) has weak permissions."
    }
}
