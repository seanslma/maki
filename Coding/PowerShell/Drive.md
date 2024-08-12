# Drive

## mapping azure file stoarge to local drive
```ps1
$connectTestResult = Test-NetConnection -ComputerName my.file.core.windows.net -Port 445
if ($connectTestResult.TcpTestSucceeded) {
    # Save the password so the drive will persist on reboot
    cmd.exe /C "cmdkey /add:`"my.file.core.windows.net`" /user:`"localhost\my`" /pass:`"pass==`""
    # Mount the drive
    New-PSDrive -Name Z -PSProvider FileSystem -Root \\my.file.core.windows.net\dropzone -Persist
} else {
    Write-Error -Message "Unable to reach the Azure storage account via port 445. Check to make sure your organization or ISP is not blocking port 445, or use Azure P2S VPN, Azure S2S VPN, or Express Route to tunnel SMB traffic over a different port."
}
```

Delete the mapped drive `net use Z: /delete`. 
Note that `Remove-PSDrive -Name "Z"` will not work as `-Persist` means the mapping is managed by the Windows OS so it cannot be removed by PowerShell.
