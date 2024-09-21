Write-Output "Running HIPAA Compliance Checks..."

# 1. Ensure encryption for data at rest (using BitLocker)
Write-Output "Checking disk encryption (BitLocker)..."
$bitlockerStatus = manage-bde -status C:  # Replace C: with the actual drive
if ($bitlockerStatus -match "Fully Encrypted") {
    Write-Output "PASS: Disk encryption is enabled."
} else {
    Write-Output "FAIL: Disk encryption is not enabled."
}

# 2. Check access control for sensitive data (using ACLs)
Write-Output "Checking access control on sensitive data..."
$sensitivePath = "C:\path\to\sensitive\data"  # Update with actual path
$acl = Get-Acl $sensitivePath
$owner = $acl.Owner

if ($owner -eq "BUILTIN\Administrators" -or $owner -eq "NT AUTHORITY\SYSTEM") {
    Write-Output "PASS: Access control is properly configured."
} else {
    Write-Output "FAIL: Access control is not configured correctly."
}