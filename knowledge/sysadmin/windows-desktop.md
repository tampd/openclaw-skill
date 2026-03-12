# Windows 10 / 11 — Cheat Sheet Chuyên Gia

> Áp dụng: Windows 10 (21H2+), Windows 11 (22H2+)
> Cập nhật: 2026-03-12
> ⚠️ Tôm chạy trên Linux — các lệnh Windows chỉ HƯỚNG DẪN, KHÔNG chạy trực tiếp.

## PowerShell Essentials

### System Information
```powershell
# Thông tin hệ thống
Get-ComputerInfo
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
[System.Environment]::OSVersion
Get-CimInstance Win32_OperatingSystem | Select Caption, Version, BuildNumber

# Hardware
Get-CimInstance Win32_Processor | Select Name, NumberOfCores, MaxClockSpeed
Get-CimInstance Win32_PhysicalMemory | Measure -Property Capacity -Sum
Get-PhysicalDisk | Select FriendlyName, MediaType, Size, HealthStatus
Get-Disk | Select Number, FriendlyName, Size, PartitionStyle
```

### Process & Service Management
```powershell
# Process
Get-Process | Sort CPU -Descending | Select -First 10
Get-Process -Name [name]
Stop-Process -Name [name] -Force
Stop-Process -Id [PID] -Force
Start-Process [path] -Verb RunAs      # Run as Admin

# Service
Get-Service | Where Status -eq Running
Get-Service [name]
Start-Service [name]
Stop-Service [name]
Restart-Service [name]
Set-Service [name] -StartupType Disabled

# Scheduled Tasks
Get-ScheduledTask | Where State -eq Ready
Register-ScheduledTask -TaskName "MyTask" -Action (New-ScheduledTaskAction -Execute "script.ps1") -Trigger (New-ScheduledTaskTrigger -Daily -At "02:00")
Unregister-ScheduledTask -TaskName "MyTask" -Confirm:$false
```

### Disk & Storage
```powershell
# Disk info
Get-Volume
Get-Partition
Get-Disk

# Dung lượng
Get-PSDrive C | Select Used, Free, @{N='Total';E={$_.Used+$_.Free}}
Get-ChildItem C:\Users -Recurse -ErrorAction SilentlyContinue |
  Group Directory |
  Sort @{E={($_.Group | Measure Length -Sum).Sum}} -Desc |
  Select -First 10 Name, @{N='SizeMB';E={[math]::Round(($_.Group | Measure Length -Sum).Sum/1MB,2)}}

# Disk Cleanup (nâng cao)
cleanmgr /d C /sageset:1             # Cấu hình cleanup
cleanmgr /d C /sagerun:1             # Chạy cleanup
DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase

# Resize partition
Resize-Partition -DriveLetter C -Size (Get-PartitionSupportedSize -DriveLetter C).SizeMax
```

### Network
```powershell
# IP & Adapter
Get-NetIPConfiguration
Get-NetAdapter | Select Name, Status, LinkSpeed, MacAddress
Get-NetIPAddress -AddressFamily IPv4

# DNS
Get-DnsClientServerAddress
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses ("8.8.8.8","1.1.1.1")
Clear-DnsClientCache
Resolve-DnsName google.com

# Testing
Test-NetConnection google.com
Test-NetConnection -ComputerName 10.0.0.1 -Port 3389
Test-Connection 8.8.8.8 -Count 4     # Ping

# Routes
Get-NetRoute
New-NetRoute -DestinationPrefix "10.0.0.0/8" -NextHop "192.168.1.1" -InterfaceAlias "Ethernet"

# Firewall
Get-NetFirewallRule | Where Enabled -eq True | Select DisplayName, Direction, Action
New-NetFirewallRule -DisplayName "Allow HTTP" -Direction Inbound -Protocol TCP -LocalPort 80 -Action Allow
Remove-NetFirewallRule -DisplayName "Allow HTTP"
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True

# Network reset
netsh winsock reset
netsh int ip reset
ipconfig /release && ipconfig /renew
ipconfig /flushdns
```

### User & Group
```powershell
# Local users
Get-LocalUser
New-LocalUser -Name "admin2" -Password (ConvertTo-SecureString "P@ss1234" -AsPlainText -Force) -FullName "Admin User"
Remove-LocalUser -Name "admin2"
Set-LocalUser -Name "admin2" -Password (ConvertTo-SecureString "NewP@ss" -AsPlainText -Force)

# Groups
Get-LocalGroupMember -Group "Administrators"
Add-LocalGroupMember -Group "Administrators" -Member "admin2"
Remove-LocalGroupMember -Group "Administrators" -Member "admin2"

# Account policies (secpol.msc hoặc)
net accounts                         # Xem password policy
net accounts /minpwlen:12 /maxpwage:90
```

## System Repair & Recovery

### SFC & DISM (Sửa lỗi hệ thống)
```powershell
# Bước 1: DISM (sửa image trước)
DISM /Online /Cleanup-Image /CheckHealth     # Kiểm tra nhanh
DISM /Online /Cleanup-Image /ScanHealth      # Scan chi tiết
DISM /Online /Cleanup-Image /RestoreHealth   # Sửa image

# Bước 2: SFC (sửa system files)
sfc /scannow
# Log: C:\Windows\Logs\CBS\CBS.log

# Nếu SFC báo lỗi không sửa được:
DISM /Online /Cleanup-Image /RestoreHealth /Source:C:\RepairSource\Windows /LimitAccess
sfc /scannow  # Chạy lại
```

### Boot Repair
```cmd
:: Từ Recovery Environment (WinRE)
bootrec /fixmbr          :: Sửa MBR
bootrec /fixboot         :: Sửa boot sector
bootrec /rebuildbcd      :: Rebuild BCD
bcdedit /enum            :: Liệt kê boot entries

:: UEFI boot repair
bcdboot C:\Windows /s S: /f UEFI
```

### Reset & Recovery
```powershell
# Reset PC (giữ files)
systemreset --factoryreset --keepfiles

# Recovery options
reagentc /info           # Trạng thái WinRE
reagentc /enable         # Bật WinRE
shutdown /r /o /t 0      # Restart vào Advanced Startup
```

## Registry (Regedit)

```powershell
# Đọc
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion"
Get-ItemPropertyValue -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" -Name ProductName

# Ghi (⚠️ CẨN THẬN)
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control" -Name "WaitToKillServiceTimeout" -Value "2000"
New-ItemProperty -Path "HKCU:\Software\MyApp" -Name "Setting1" -Value "data" -PropertyType String

# Export/Import backup
reg export "HKLM\SOFTWARE\MyApp" C:\backup\myapp.reg
reg import C:\backup\myapp.reg

# Registry hữu ích:
# Tắt Telemetry:
# HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection → AllowTelemetry = 0
# Tắt Cortana:
# HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search → AllowCortana = 0
```

## Group Policy (Local)

```powershell
# Mở Group Policy Editor
gpedit.msc

# Áp dụng ngay
gpupdate /force

# Xem policies đang áp dụng
gpresult /R                          # Summary
gpresult /H C:\gpresult.html         # Báo cáo HTML

# Export/Import
# Backup: %SystemRoot%\System32\GroupPolicy\
```

### Các GPO hữu ích (Windows 10/11)
| Policy Path | Chức năng |
|---|---|
| Computer > Windows Settings > Security Settings > Account Policies | Password & lockout |
| Computer > Admin Templates > Windows Components > Windows Update | Cấu hình update |
| Computer > Admin Templates > System > Power Management | Power plan |
| User > Admin Templates > Start Menu and Taskbar | Customize Start menu |
| Computer > Admin Templates > Network > Lanman Workstation | SMB settings |

## Driver Management

```powershell
# Liệt kê drivers
Get-WindowsDriver -Online | Select OriginalFileName, Version, Date
driverquery /v
pnputil /enum-drivers                # Liệt kê driver packages

# Cài driver
pnputil /add-driver C:\drivers\*.inf /install /subdirs

# Gỡ driver
pnputil /delete-driver [oem*.inf] /uninstall

# Export drivers (backup)
Export-WindowsDriver -Online -Destination C:\DriversBackup

# Rollback driver
# Device Manager > Properties > Driver > Roll Back Driver
```

## WSL2 (Windows Subsystem for Linux)

```powershell
# Cài đặt
wsl --install                        # Cài WSL2 + Ubuntu mặc định
wsl --install -d [distro]            # Chọn distro
wsl --list --online                  # Distros có sẵn

# Quản lý
wsl --list --verbose                 # Liệt kê + version
wsl --set-default [distro]           # Set default
wsl --set-version [distro] 2         # Chuyển sang WSL2
wsl --shutdown                       # Tắt tất cả instances
wsl --terminate [distro]             # Tắt 1 distro

# Config WSL: %USERPROFILE%\.wslconfig
# [wsl2]
# memory=4GB
# processors=2
# swap=2GB

# Truy cập files
# Từ Windows: \\wsl$\Ubuntu\home\user
# Từ WSL: /mnt/c/Users/
```

## Windows Update

```powershell
# Kiểm tra updates
Get-WindowsUpdate                    # Cần module PSWindowsUpdate
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate
Install-WindowsUpdate -AcceptAll -AutoReboot

# USOClient (built-in)
USOClient StartScan
USOClient StartDownload
USOClient StartInstall

# Tạm dừng update
# Settings > Windows Update > Pause updates

# WSUS settings (GPO)
# Computer > Admin Templates > Windows Components > Windows Update
# > Configure Automatic Updates
```

## Performance Optimization

```powershell
# Startup apps
Get-CimInstance Win32_StartupCommand
# Task Manager > Startup tab

# Visual Effects (tối ưu performance)
SystemPropertiesPerformance.exe
# Hoặc Registry:
# HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects
# > VisualFXSetting = 2 (Custom)

# Power Plan
powercfg /list
powercfg /setactive SCHEME_MIN       # High Performance
powercfg /hibernate off              # Tắt hibernation (tiết kiệm disk)

# Disk optimization
Optimize-Volume -DriveLetter C -Defrag -Verbose  # HDD
Optimize-Volume -DriveLetter C -ReTrim -Verbose   # SSD (TRIM)

# Memory diagnostics
mdsched.exe                          # Windows Memory Diagnostic
```

## BitLocker (Mã hóa ổ đĩa)

```powershell
# Trạng thái
Get-BitLockerVolume
manage-bde -status

# Bật BitLocker
Enable-BitLocker -MountPoint "C:" -EncryptionMethod XtsAes256 -RecoveryPasswordProtector
manage-bde -on C: -RecoveryPassword

# Lấy Recovery Key
(Get-BitLockerVolume -MountPoint "C:").KeyProtector | Where KeyProtectorType -eq RecoveryPassword

# Tắt BitLocker
Disable-BitLocker -MountPoint "C:"
```

## Useful CMD Commands (Legacy)

```cmd
:: System
msconfig                :: System Configuration
msinfo32                :: System Information
devmgmt.msc             :: Device Manager
diskmgmt.msc            :: Disk Management
compmgmt.msc            :: Computer Management
eventvwr.msc            :: Event Viewer
taskschd.msc            :: Task Scheduler
services.msc            :: Services
lusrmgr.msc             :: Local Users & Groups
secpol.msc              :: Local Security Policy
perfmon                 :: Performance Monitor
resmon                  :: Resource Monitor
mstsc                   :: Remote Desktop
ncpa.cpl                :: Network Connections
appwiz.cpl              :: Programs & Features
```
