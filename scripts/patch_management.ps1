Write-Output "Checking for missing updates..."

Get-WindowsUpdate -Install -AcceptAll -AutoReboot | Out-String | Write-Output