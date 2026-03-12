# Linux Ubuntu / Debian — Cheat Sheet Chuyên Gia

> Áp dụng: Ubuntu 20.04 LTS, 22.04 LTS, 24.04 LTS, Debian 11/12
> Cập nhật: 2026-03-12

## Package Management (APT)

```bash
apt update                           # Cập nhật danh sách gói
apt upgrade                          # Nâng cấp tất cả gói
apt full-upgrade                     # Nâng cấp + xử lý dependencies
apt install [pkg]                    # Cài đặt
apt install [pkg]=1.2.3-1            # Cài phiên bản cụ thể
apt remove [pkg]                     # Gỡ (giữ config)
apt purge [pkg]                      # Gỡ + xóa config
apt autoremove                       # Gỡ dependencies không dùng
apt search [keyword]                 # Tìm kiếm
apt show [pkg]                       # Thông tin gói
apt list --installed                 # Liệt kê đã cài
apt list --upgradable                # Gói có thể upgrade
dpkg -l                              # Liệt kê tất cả packages
dpkg -L [pkg]                        # Files trong package
dpkg -S [file]                       # Tìm package chứa file

# Khóa phiên bản (hold)
apt-mark hold [pkg]                  # Không cho upgrade
apt-mark unhold [pkg]                # Bỏ khóa
apt-mark showhold                    # Xem gói đang hold

# Repository
add-apt-repository ppa:[name/ppa]    # Thêm PPA
add-apt-repository --remove ppa:[name/ppa]
# Custom repo
echo "deb [signed-by=/usr/share/keyrings/repo.gpg] https://repo.example.com stable main" \
  > /etc/apt/sources.list.d/repo.list

# Dọn dẹp
apt clean                            # Xóa cache .deb
apt autoclean                        # Xóa cache cũ
du -sh /var/cache/apt/archives/      # Kiểm tra cache size
```

## Systemd & Services

```bash
# Giống CentOS — xem linux-centos.md, section Systemd
# Ubuntu-specific:

# Thứ tự boot services
systemd-analyze                      # Thời gian boot
systemd-analyze blame                # Service chậm nhất
systemd-analyze critical-chain       # Chain dependencies

# Custom service
cat > /etc/systemd/system/myapp.service << 'EOF'
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/start.sh
Restart=on-failure
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable --now myapp.service
```

## Firewall (UFW)

```bash
# Trạng thái
ufw status                           # Trạng thái cơ bản
ufw status verbose                   # Chi tiết
ufw status numbered                  # Có số thứ tự (để xóa)

# Bật/tắt
ufw enable                           # Bật (⚠️ đảm bảo allow SSH trước!)
ufw disable                          # Tắt

# Allow rules
ufw allow ssh                        # Allow SSH (22)
ufw allow 80/tcp                     # Allow HTTP
ufw allow 443/tcp                    # Allow HTTPS
ufw allow from 10.0.0.0/8            # Allow từ subnet
ufw allow from 192.168.1.0/24 to any port 3306  # MySQL từ LAN
ufw allow in on eth0 to any port 80  # Allow trên interface cụ thể

# Deny rules
ufw deny 3306/tcp                    # Block MySQL public
ufw deny from 1.2.3.4                # Block IP cụ thể

# Xóa rule
ufw delete allow 80/tcp
ufw delete [number]                  # Xóa theo số (từ status numbered)

# Rate limiting
ufw limit ssh/tcp                    # Giới hạn SSH connections

# Default policy
ufw default deny incoming
ufw default allow outgoing

# Reset
ufw reset                            # Reset tất cả rules

# Log
ufw logging on                       # Bật logging
# Log tại: /var/log/ufw.log
```

## AppArmor

```bash
# Trạng thái
aa-status                            # Tổng quan profiles
apparmor_status                      # Alias

# Modes
aa-enforce /etc/apparmor.d/[profile] # Enforce mode
aa-complain /etc/apparmor.d/[profile]# Complain mode (log only)
aa-disable /etc/apparmor.d/[profile] # Tắt profile

# Troubleshoot
journalctl | grep apparmor           # Log denials
aa-logprof                           # Interactive profile tuning

# Reload
systemctl reload apparmor
apparmor_parser -r /etc/apparmor.d/[profile]
```

## Networking (Netplan — Ubuntu 18.04+)

```bash
# Config file: /etc/netplan/*.yaml

# Static IP
cat > /etc/netplan/01-static.yaml << 'EOF'
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      addresses:
        - 10.0.0.5/24
      routes:
        - to: default
          via: 10.0.0.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 1.1.1.1
EOF

# DHCP
cat > /etc/netplan/01-dhcp.yaml << 'EOF'
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
EOF

# VLAN
cat > /etc/netplan/02-vlan.yaml << 'EOF'
network:
  version: 2
  vlans:
    vlan100:
      id: 100
      link: eth0
      addresses:
        - 172.16.100.5/24
EOF

# Apply
netplan try                          # Test (auto-revert nếu mất kết nối)
netplan apply                        # Apply vĩnh viễn
netplan generate                     # Generate config (debug)

# Legacy (nếu không dùng netplan)
cat /etc/network/interfaces
systemctl restart networking
```

## User & Permission Management

```bash
# User management (tương tự CentOS nhưng group khác)
adduser [user]                       # Interactive (Ubuntu preferred)
useradd -m -s /bin/bash [user]       # Non-interactive
usermod -aG sudo [user]              # Thêm vào sudo group (⚠️ sudo, KHÔNG phải wheel)
deluser --remove-home [user]         # Xóa user

# Group
addgroup [group]
usermod -aG [group] [user]
groups [user]
```

## Disk Management

```bash
# Partition (giống CentOS)
lsblk
fdisk -l
df -hT
blkid

# Ubuntu-specific: ZFS (nếu cài)
zpool status                         # Trạng thái ZFS pool
zpool list                           # Liệt kê pools
zfs list                             # Liệt kê datasets
zfs snapshot pool/dataset@snap1      # Tạo snapshot
zfs rollback pool/dataset@snap1      # Rollback

# BTRFS (nếu dùng)
btrfs filesystem show
btrfs subvolume list /
btrfs subvolume snapshot / /snapshot1

# Auto-mount (fstab)
# Lấy UUID
blkid /dev/sdb1
# Thêm vào /etc/fstab:
# UUID=xxxx-xxxx /mnt/data ext4 defaults 0 2
mount -a                             # Test mount tất cả
```

## Snap & Flatpak

```bash
# Snap (Ubuntu mặc định)
snap list                            # Liệt kê đã cài
snap find [keyword]                  # Tìm kiếm
snap install [pkg]                   # Cài đặt
snap install [pkg] --classic         # Classic confinement
snap remove [pkg]                    # Gỡ
snap refresh                         # Cập nhật tất cả
snap refresh [pkg]                   # Cập nhật 1 gói
snap revert [pkg]                    # Rollback
snap connections [pkg]               # Xem permissions

# Tắt Snap auto-updates (nếu cần)
snap set system refresh.hold="$(date --date='7 days' +%Y-%m-%dT%H:%M:%S%:z)"

# Flatpak (cần cài thêm)
apt install flatpak
flatpak install flathub [app]
flatpak list
flatpak update
```

## Unattended Upgrades (Auto Security Updates)

```bash
apt install unattended-upgrades
dpkg-reconfigure -plow unattended-upgrades

# Config: /etc/apt/apt.conf.d/50unattended-upgrades
# Bật auto-reboot:
# Unattended-Upgrade::Automatic-Reboot "true";
# Unattended-Upgrade::Automatic-Reboot-Time "03:00";

# Kiểm tra
unattended-upgrades --dry-run --debug
cat /var/log/unattended-upgrades/unattended-upgrades.log
```

## Log Analysis

```bash
# Journald (giống CentOS)
journalctl -xe
journalctl --since "1 hour ago"
journalctl -p err

# Ubuntu-specific logs
tail -f /var/log/syslog              # System log chính
tail -f /var/log/auth.log            # SSH + Auth (⚠️ auth.log, KHÔNG phải secure)
tail -f /var/log/kern.log            # Kernel log
cat /var/log/dpkg.log                # Package install log
cat /var/log/apt/history.log         # APT history

# Cloud-init (nếu VPS cloud)
cat /var/log/cloud-init.log
cat /var/log/cloud-init-output.log
cloud-init status --long
```

## Performance & Monitoring

```bash
# System info
lsb_release -a                      # Ubuntu version
cat /etc/os-release                  # OS info
uname -a                            # Kernel

# Performance
top / htop                           # Process monitor
vmstat 1 5                           # VM stats (1s interval, 5 times)
iostat -x 1 5                        # Disk I/O
sar -u 1 5                           # CPU history (sysstat package)
sar -r 1 5                           # Memory history
nmon                                 # Interactive monitor

# Cgroups v2 (Ubuntu 22.04+)
systemd-cgtop                        # Cgroup resource usage
systemctl set-property myapp.service CPUQuota=50%
systemctl set-property myapp.service MemoryMax=512M
```

## Ubuntu Pro & Livepatch

```bash
# Ubuntu Pro (ESM, Livepatch, FIPS...)
pro status                           # Trạng thái
pro attach [token]                   # Attach license
pro enable livepatch                 # Kernel livepatch (no reboot)
pro enable esm-infra                 # Extended Security Updates

# Kiểm tra kernel livepatch
canonical-livepatch status
```

## Release Upgrade

```bash
# Kiểm tra version mới
do-release-upgrade -c                # Check only
do-release-upgrade                   # Upgrade (⚠️ backup trước!)
do-release-upgrade -d                # Dev version (không khuyến khích production)

# Sau upgrade
apt update && apt full-upgrade
apt autoremove
reboot
```
