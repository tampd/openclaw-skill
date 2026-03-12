# Security Hardening — Cross-Platform Cheat Sheet Chuyên Gia

> Áp dụng: Linux (CentOS, Ubuntu) + Windows (10/11, Server 202x)
> Cập nhật: 2026-03-12
> Tham khảo: CIS Benchmarks, NIST, OWASP

## SSH Hardening (Linux)

### /etc/ssh/sshd_config
```bash
# Đổi port (tránh scan)
Port 2222

# Tắt root login
PermitRootLogin no

# Key-based auth only
PasswordAuthentication no
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys

# Giới hạn users
AllowUsers admin deploy
# Hoặc: AllowGroups ssh-users

# Security settings
MaxAuthTries 3
LoginGraceTime 30
ClientAliveInterval 300
ClientAliveCountMax 2
X11Forwarding no
PermitEmptyPasswords no
Protocol 2

# Crypto hardening (modern)
KexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com
```

```bash
# Apply
systemctl restart sshd

# Test trước khi đóng session cũ!
ssh -p 2222 admin@server    # Mở terminal MỚI để test

# SSH Key setup
ssh-keygen -t ed25519 -C "admin@company"
ssh-copy-id -p 2222 admin@server
```

## fail2ban (Linux)

```bash
# Cài đặt
apt install fail2ban          # Ubuntu
dnf install fail2ban          # CentOS (EPEL)

# Config: /etc/fail2ban/jail.local
cat > /etc/fail2ban/jail.local << 'EOF'
[DEFAULT]
bantime = 3600
findtime = 600
maxretry = 3
banaction = iptables-multiport
action = %(action_mwl)s

[sshd]
enabled = true
port = 2222
logpath = /var/log/auth.log
maxretry = 3
bantime = 86400

[nginx-http-auth]
enabled = true
logpath = /var/log/nginx/error.log
maxretry = 5

[nginx-limit-req]
enabled = true
logpath = /var/log/nginx/error.log
maxretry = 10
findtime = 120
bantime = 600
EOF

# Quản lý
systemctl enable --now fail2ban
fail2ban-client status
fail2ban-client status sshd
fail2ban-client set sshd unbanip 1.2.3.4
fail2ban-client set sshd banip 5.6.7.8
```

## SELinux Hardening (CentOS/RHEL)

```bash
# Đảm bảo Enforcing
getenforce
# Nếu Permissive/Disabled:
setenforce 1
sed -i 's/SELINUX=.*/SELINUX=enforcing/' /etc/selinux/config

# Troubleshoot denials
audit2why < /var/log/audit/audit.log
sealert -a /var/log/audit/audit.log

# Common booleans cho web server
setsebool -P httpd_can_network_connect 1
setsebool -P httpd_can_sendmail 1
setsebool -P httpd_can_network_connect_db 1

# File contexts
semanage fcontext -a -t httpd_sys_content_t "/var/www/html(/.*)?"
restorecon -Rv /var/www/html
```

## AppArmor Hardening (Ubuntu)

```bash
# Đảm bảo enabled
aa-status
systemctl enable --now apparmor

# Enforce all profiles
aa-enforce /etc/apparmor.d/*

# Tạo profile mới cho app
aa-genprof /path/to/app
# Hoặc tự viết profile
```

## Firewall Hardening

### Linux — Minimal rule set
```bash
# Ubuntu (ufw)
ufw default deny incoming
ufw default allow outgoing
ufw allow 2222/tcp comment "SSH"      # Custom SSH port
ufw allow 80/tcp comment "HTTP"
ufw allow 443/tcp comment "HTTPS"
ufw limit 2222/tcp                    # Rate limit SSH
ufw enable

# CentOS (firewalld)
firewall-cmd --set-default-zone=drop
firewall-cmd --permanent --add-port=2222/tcp
firewall-cmd --permanent --add-service=http
firewall-cmd --permanent --add-service=https
firewall-cmd --reload
```

### Windows — GPO Firewall
```powershell
# Block all inbound by default
Set-NetFirewallProfile -Profile Domain,Public,Private -DefaultInboundAction Block -DefaultOutboundAction Allow

# Allow only essentials
New-NetFirewallRule -DisplayName "Allow RDP" -Direction Inbound -Protocol TCP -LocalPort 3389 -Action Allow -RemoteAddress 10.0.0.0/8
New-NetFirewallRule -DisplayName "Allow WinRM" -Direction Inbound -Protocol TCP -LocalPort 5985,5986 -Action Allow -RemoteAddress 10.0.0.0/8

# Enable logging
Set-NetFirewallProfile -LogBlocked True -LogAllowed False -LogFileName "C:\Windows\system32\LogFiles\Firewall\pfirewall.log"
```

## Audit & Logging

### Linux — auditd
```bash
# Cài đặt
apt install auditd audispd-plugins    # Ubuntu
dnf install audit                     # CentOS

# Rules: /etc/audit/rules.d/custom.rules
# Monitor file changes
-w /etc/passwd -p wa -k identity
-w /etc/group -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/sudoers -p wa -k sudoers
-w /etc/ssh/sshd_config -p wa -k sshd_config

# Monitor commands
-a always,exit -F arch=b64 -S execve -F uid=0 -k root_commands
-a always,exit -F arch=b64 -S execve -F auid>=1000 -k user_commands

# Apply
augenrules --load
systemctl restart auditd

# Search
ausearch -k identity -ts recent
aureport --auth --summary
aureport --login --summary
```

### Windows — Audit Policy
```powershell
# Enable comprehensive auditing
auditpol /set /category:"Logon/Logoff" /success:enable /failure:enable
auditpol /set /category:"Account Logon" /success:enable /failure:enable
auditpol /set /category:"Account Management" /success:enable /failure:enable
auditpol /set /category:"Privilege Use" /success:enable /failure:enable
auditpol /set /category:"Policy Change" /success:enable /failure:enable
auditpol /set /category:"System" /success:enable /failure:enable

# Verify
auditpol /get /category:*

# View security events
Get-EventLog -LogName Security -EntryType FailureAudit -Newest 20
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 10  # Failed logons
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624} -MaxEvents 10  # Successful logons
```

## Password Policy

### Linux
```bash
# /etc/login.defs
PASS_MAX_DAYS   90
PASS_MIN_DAYS   7
PASS_MIN_LEN    12
PASS_WARN_AGE   14

# PAM password quality: /etc/security/pwquality.conf (hoặc pam_cracklib)
minlen = 12
dcredit = -1         # Ít nhất 1 số
ucredit = -1         # Ít nhất 1 chữ hoa
lcredit = -1         # Ít nhất 1 chữ thường
ocredit = -1         # Ít nhất 1 ký tự đặc biệt
maxrepeat = 3        # Max 3 ký tự lặp

# Account lockout: /etc/pam.d/system-auth (CentOS) hoặc /etc/pam.d/common-auth (Ubuntu)
auth required pam_faillock.so preauth deny=5 unlock_time=900 fail_interval=900
```

### Windows
```powershell
# Local policy
net accounts /minpwlen:12 /maxpwage:90 /minpwage:7 /uniquepw:5 /lockoutthreshold:5

# GPO (AD)
# Computer > Policies > Windows Settings > Security Settings > Account Policies
# Password Policy: Min length=12, Complexity=Enabled, Max age=90 days
# Account Lockout: Threshold=5, Duration=30 min, Reset counter=30 min
```

## Kernel Hardening (Linux)

```bash
# /etc/sysctl.d/99-security.conf
# Network security
net.ipv4.conf.all.rp_filter = 1              # Reverse path filtering
net.ipv4.conf.default.rp_filter = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1     # Ignore broadcast pings
net.ipv4.conf.all.accept_redirects = 0       # No ICMP redirects
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.all.accept_source_route = 0    # No source routing
net.ipv4.conf.all.log_martians = 1           # Log spoofed packets
net.ipv4.tcp_syncookies = 1                  # SYN flood protection

# Disable IPv6 (nếu không dùng)
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1

# Apply
sysctl -p /etc/sysctl.d/99-security.conf
```

## Windows Defender & Security

```powershell
# Status
Get-MpComputerStatus

# Update signatures
Update-MpSignature

# Full scan
Start-MpScan -ScanType FullScan

# Exclusions (cho apps cần)
Add-MpPreference -ExclusionPath "D:\SQLData"
Add-MpPreference -ExclusionProcess "sqlservr.exe"

# Configure
Set-MpPreference -DisableRealtimeMonitoring $false
Set-MpPreference -SubmitSamplesConsent 2          # Never send
Set-MpPreference -MAPSReporting 0                 # Disable cloud

# Attack Surface Reduction (ASR)
Set-MpPreference -AttackSurfaceReductionRules_Ids [GUID] -AttackSurfaceReductionRules_Actions Enabled
```

## CIS Benchmark Checklist (Tóm tắt)

### Linux (CentOS/Ubuntu)
| # | Kiểm tra | Lệnh check |
|---|---|---|
| 1 | Filesystem: nodev,nosuid,noexec cho /tmp | `mount \| grep /tmp` |
| 2 | Core dumps disabled | `ulimit -c` (should be 0) |
| 3 | ASLR enabled | `cat /proc/sys/kernel/randomize_va_space` (should be 2) |
| 4 | Không có file SUID/SGID lạ | `find / -perm /4000 -type f 2>/dev/null` |
| 5 | SSH hardened | `sshd -T \| grep -E "permit\|password\|port"` |
| 6 | Cron restricted | `ls -l /etc/cron.deny /etc/at.deny` |
| 7 | Firewall enabled | `ufw status` / `firewall-cmd --state` |
| 8 | Không có user UID 0 ngoài root | `awk -F: '$3==0{print}' /etc/passwd` |
| 9 | Log forwarding configured | `systemctl status rsyslog` |
| 10 | Auto security updates | `systemctl status unattended-upgrades` / `yum-cron` |

### Windows Server
| # | Kiểm tra | Cách check |
|---|---|---|
| 1 | SMBv1 disabled | `Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol` |
| 2 | NLA for RDP | Registry: `UserAuthentication = 1` |
| 3 | Windows Firewall enabled | `Get-NetFirewallProfile \| Select Enabled` |
| 4 | Audit policy configured | `auditpol /get /category:*` |
| 5 | BitLocker/EFS enabled | `Get-BitLockerVolume` |
| 6 | Guest account disabled | `Get-LocalUser Guest \| Select Enabled` |
| 7 | Password complexity | `net accounts` |
| 8 | Auto-update enabled | `Get-WindowsUpdateLog` |
| 9 | No unnecessary roles | `Get-WindowsFeature \| Where Installed` |
| 10 | Defender real-time ON | `Get-MpComputerStatus` |

## Incident Response — Quick Steps

### Linux bị hack?
```bash
# 1. Thu thập evidence (KHÔNG reboot!)
last -a                              # Login history
lastb                                # Failed attempts
cat /var/log/auth.log | grep -i "accepted\|failed"
ps auxf                              # Process tree
netstat -tulpn                       # Open connections
find / -mtime -1 -type f 2>/dev/null # Modified files <24h
find / -name ".*" -type f 2>/dev/null # Hidden files
crontab -l                           # Check crontab
cat /etc/crontab
ls /etc/cron.d/

# 2. Check rootkit
chkrootkit
rkhunter --check

# 3. Block attacker
iptables -A INPUT -s [attacker-ip] -j DROP

# 4. Change all passwords
passwd root
# Đổi tất cả user passwords
```

### Windows bị hack?
```powershell
# 1. Evidence
Get-EventLog -LogName Security -EntryType FailureAudit -Newest 50
Get-Process | Where Path -ne $null | Select Name, Path, Id
Get-NetTCPConnection | Where State -eq Established | Select RemoteAddress, RemotePort, OwningProcess
Get-ScheduledTask | Where State -eq Ready
Get-Service | Where Status -eq Running | Where DisplayName -notlike "Windows*"

# 2. Check startup
Get-CimInstance Win32_StartupCommand
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
Get-ItemProperty "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

# 3. Full scan
Start-MpScan -ScanType FullScan

# 4. Block IP
New-NetFirewallRule -DisplayName "Block Attacker" -Direction Inbound -RemoteAddress [IP] -Action Block
```
