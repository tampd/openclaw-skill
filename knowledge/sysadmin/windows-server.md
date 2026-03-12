# Windows Server 2019 / 2022 / 2025 — Cheat Sheet Chuyên Gia

> Áp dụng: Windows Server 2019, 2022, 2025 (Standard & Datacenter)
> Cập nhật: 2026-03-12
> ⚠️ Tôm chạy trên Linux — các lệnh Windows chỉ HƯỚNG DẪN, KHÔNG chạy trực tiếp.

## Roles & Features

```powershell
Get-WindowsFeature | Where InstallState -eq Installed
Install-WindowsFeature -Name [role] -IncludeManagementTools
# Roles phổ biến: AD-Domain-Services, DNS, DHCP, Web-Server, Hyper-V, FS-FileServer
Uninstall-WindowsFeature -Name [role] -Restart
```

## Active Directory (AD DS)

### Promote Domain Controller
```powershell
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools

# New Forest
Install-ADDSForest -DomainName "company.local" -DomainNetBIOSName "COMPANY" `
  -InstallDns:$true -SafeModeAdministratorPassword (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force)

# Join existing domain
Install-ADDSDomainController -DomainName "company.local" -InstallDns:$true `
  -Credential (Get-Credential) -SafeModeAdministratorPassword (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force)
```

### AD Users & Groups
```powershell
# Users
Get-ADUser -Filter * | Select Name, SamAccountName, Enabled
New-ADUser -Name "Nguyen Van A" -SamAccountName "nguyenvana" `
  -UserPrincipalName "nguyenvana@company.local" `
  -Path "OU=Users,DC=company,DC=local" `
  -AccountPassword (ConvertTo-SecureString "TempP@ss1" -AsPlainText -Force) `
  -Enabled $true -ChangePasswordAtLogon $true
Set-ADAccountPassword -Identity [user] -NewPassword (ConvertTo-SecureString "NewP@ss!" -AsPlainText -Force) -Reset
Disable-ADAccount -Identity [user]
Unlock-ADAccount -Identity [user]

# Groups
Get-ADGroupMember -Identity "Domain Admins"
New-ADGroup -Name "IT-Staff" -GroupScope Global -GroupCategory Security
Add-ADGroupMember -Identity "IT-Staff" -Members "nguyenvana"

# OUs
New-ADOrganizationalUnit -Name "HCM" -Path "DC=company,DC=local"

# Bulk import
Import-Csv users.csv | ForEach-Object {
  New-ADUser -Name $_.Name -SamAccountName $_.Username `
    -AccountPassword (ConvertTo-SecureString $_.Password -AsPlainText -Force) -Enabled $true
}
```

### Group Policy (GPO)
```powershell
Get-GPO -All | Select DisplayName, GpoStatus
New-GPO -Name "Security-Baseline" | New-GPLink -Target "OU=Computers,DC=company,DC=local"
gpupdate /force                      # Apply ngay
gpresult /R                          # Xem GPO đang áp dụng
Backup-GPO -All -Path C:\GPO-Backup
Restore-GPO -Name "Security-Baseline" -Path C:\GPO-Backup
```

## DNS Server

```powershell
Get-DnsServerZone
Add-DnsServerPrimaryZone -Name "company.local" -ZoneFile "company.local.dns"
Add-DnsServerResourceRecordA -Name "web01" -ZoneName "company.local" -IPv4Address "10.0.0.50"
Add-DnsServerResourceRecordCName -Name "www" -ZoneName "company.local" -HostNameAlias "web01.company.local"
Set-DnsServerForwarder -IPAddress "8.8.8.8","1.1.1.1"
Clear-DnsServerCache
```

## DHCP Server

```powershell
Install-WindowsFeature DHCP -IncludeManagementTools
Add-DhcpServerv4Scope -Name "LAN" -StartRange 10.0.0.100 -EndRange 10.0.0.250 -SubnetMask 255.255.255.0
Set-DhcpServerv4OptionValue -ScopeId 10.0.0.0 -Router 10.0.0.1 -DnsServer 10.0.0.1
Add-DhcpServerv4ExclusionRange -ScopeId 10.0.0.0 -StartRange 10.0.0.1 -EndRange 10.0.0.20
Add-DhcpServerv4Reservation -ScopeId 10.0.0.0 -IPAddress 10.0.0.50 -ClientId "AA-BB-CC-DD-EE-FF" -Name "printer01"
Get-DhcpServerv4Lease -ScopeId 10.0.0.0
```

## IIS (Web Server)

```powershell
Install-WindowsFeature Web-Server -IncludeManagementTools
New-IISSite -Name "MyWebsite" -BindingInformation "*:80:www.example.com" -PhysicalPath "C:\inetpub\wwwroot\mysite"
New-IISSiteBinding -Name "MyWebsite" -BindingInformation "*:443:" -Protocol https -CertificateThumbprint [thumb] -CertStoreLocation "Cert:\LocalMachine\My"
New-WebAppPool -Name "MyAppPool"
Restart-WebAppPool -Name "MyAppPool"
Start-IISSite / Stop-IISSite -Name "MyWebsite"
```

## Hyper-V

```powershell
Get-VM | Select Name, State, CPUUsage, MemoryAssigned
New-VM -Name "Ubuntu-VM" -MemoryStartupBytes 2GB -NewVHDPath "C:\VMs\Ubuntu.vhdx" -NewVHDSizeBytes 50GB -Generation 2 -SwitchName "Default Switch"
Set-VM -Name "Ubuntu-VM" -ProcessorCount 2 -DynamicMemory -MemoryMinimumBytes 1GB -MemoryMaximumBytes 4GB
Start-VM / Stop-VM / Restart-VM -Name "Ubuntu-VM"
Checkpoint-VM -Name "Ubuntu-VM" -SnapshotName "Before-Update"
Restore-VMCheckpoint -Name "Before-Update" -VMName "Ubuntu-VM"

# Virtual Switches
New-VMSwitch -Name "External" -NetAdapterName "Ethernet" -AllowManagementOS $true
New-VMSwitch -Name "Internal" -SwitchType Internal

# VHD
New-VHD -Path "C:\VMs\data.vhdx" -SizeBytes 100GB -Dynamic
Resize-VHD -Path "C:\VMs\data.vhdx" -SizeBytes 200GB

# Live Migration
Move-VM -Name "Ubuntu-VM" -DestinationHost "hyperv02" -IncludeStorage
```

## Remote Management

```powershell
# PowerShell Remoting
Enable-PSRemoting -Force
Enter-PSSession -ComputerName "server02" -Credential (Get-Credential)
Invoke-Command -ComputerName "server02","server03" -ScriptBlock { Get-Service }

# RDP
Set-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server" -Name fDenyTSConnections -Value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"

# SSH (Server 2019+)
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Set-Service sshd -StartupType Automatic
Start-Service sshd
```

## Backup & Recovery

```powershell
Install-WindowsFeature Windows-Server-Backup
wbadmin start backup -backupTarget:D: -include:C: -allCritical -quiet
wbadmin start systemstatebackup -backupTarget:D:   # AD backup

# AD Recycle Bin
Enable-ADOptionalFeature 'Recycle Bin Feature' -Scope ForestOrConfigurationSet -Target 'company.local'
Get-ADObject -Filter 'isDeleted -eq $true' -IncludeDeletedObjects | Restore-ADObject
```

## Failover Clustering

```powershell
Install-WindowsFeature Failover-Clustering -IncludeManagementTools
Test-Cluster -Node "node01","node02"
New-Cluster -Name "SQLCLUSTER" -Node "node01","node02" -StaticAddress 10.0.0.100
Set-ClusterQuorum -NodeAndFileShareMajority "\\fileserver\witness"
```

## Security Hardening

```powershell
# Disable SMBv1 (⚠️ WannaCry)
Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol

# Audit Policy
auditpol /set /category:"Logon/Logoff" /success:enable /failure:enable
auditpol /set /category:"Account Logon" /success:enable /failure:enable

# NLA for RDP
Set-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name UserAuthentication -Value 1

# Windows Defender
Update-MpSignature
Set-MpPreference -DisableRealtimeMonitoring $false
Add-MpPreference -ExclusionPath "D:\SQLData"

# Event logs
Get-EventLog -LogName System -EntryType Error -Newest 20
Get-EventLog -LogName Security -Newest 20
wevtutil cl System   # Clear log
```

## Performance Monitoring

```powershell
Get-Counter '\Processor(_Total)\% Processor Time'
Get-Counter '\Memory\Available MBytes'
Get-Counter '\PhysicalDisk(_Total)\% Disk Time'

# Storage
Get-StoragePool
Enable-DedupVolume -Volume "D:" -UsageType Default
Get-DedupStatus
```
