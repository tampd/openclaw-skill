# Linux CentOS / RHEL — Cheat Sheet Chuyên Gia

> Áp dụng: CentOS 7, CentOS Stream 8/9, RHEL 7/8/9, AlmaLinux, Rocky Linux
> Cập nhật: 2026-03-12

## Package Management

### CentOS 7 (yum)
```bash
yum install [pkg]              # Cài đặt
yum remove [pkg]               # Gỡ
yum update                     # Cập nhật tất cả
yum update [pkg]               # Cập nhật 1 gói
yum search [keyword]           # Tìm kiếm
yum info [pkg]                 # Thông tin gói
yum list installed             # Liệt kê đã cài
yum provides [file]            # Tìm gói chứa file
yum history                    # Lịch sử cài đặt
yum history undo [ID]          # Rollback transaction
yum makecache                  # Cập nhật cache repo
yum clean all                  # Xóa cache
```

### CentOS 8/9 / Stream (dnf)
```bash
dnf install [pkg]              # Cài đặt
dnf remove [pkg]               # Gỡ
dnf upgrade                    # Cập nhật tất cả (thay yum update)
dnf module list                # Liệt kê modules
dnf module enable [mod:stream] # Bật module stream
dnf module install [mod:stream/profile]
dnf autoremove                 # Gỡ dependencies không dùng
dnf repolist --all             # Liệt kê tất cả repo
dnf config-manager --add-repo [URL]
dnf config-manager --set-enabled [repo]
```

### EPEL & Remi
```bash
# EPEL (CentOS 7)
yum install epel-release

# EPEL (CentOS 8/9)
dnf install epel-release

# Remi (PHP versions)
dnf install https://rpms.remirepo.net/enterprise/remi-release-9.rpm
dnf module reset php
dnf module enable php:remi-8.3
dnf install php
```

## Systemd & Services

```bash
systemctl start [service]      # Khởi động
systemctl stop [service]       # Dừng
systemctl restart [service]    # Khởi động lại
systemctl reload [service]     # Reload config (không restart)
systemctl status [service]     # Trạng thái
systemctl enable [service]     # Tự khởi động cùng OS
systemctl disable [service]    # Tắt tự khởi động
systemctl is-enabled [service] # Kiểm tra auto-start
systemctl list-units --type=service --state=running
systemctl list-units --failed  # Service bị lỗi
systemctl daemon-reload        # Sau khi sửa unit file
systemctl mask [service]       # Khóa hoàn toàn (không start được)
systemctl unmask [service]

# Xem log service
journalctl -u [service] -n 100 --no-pager
journalctl -u [service] -f     # Follow realtime
journalctl -u [service] --since "2026-03-12 08:00"
journalctl -u [service] -p err # Chỉ lỗi
```

## Firewall (firewalld)

```bash
# Trạng thái
firewall-cmd --state
firewall-cmd --list-all
firewall-cmd --list-ports
firewall-cmd --list-services

# Thêm rule (permanent)
firewall-cmd --permanent --add-port=8080/tcp
firewall-cmd --permanent --add-service=http
firewall-cmd --permanent --add-service=https
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.0.0.0/8" port port="3306" protocol="tcp" accept'

# Xóa rule
firewall-cmd --permanent --remove-port=8080/tcp
firewall-cmd --permanent --remove-service=http

# Zones
firewall-cmd --get-active-zones
firewall-cmd --zone=public --list-all
firewall-cmd --permanent --zone=trusted --add-source=192.168.1.0/24

# Apply changes
firewall-cmd --reload
```

## SELinux

```bash
# Trạng thái
getenforce                           # Enforcing / Permissive / Disabled
sestatus                             # Chi tiết

# Tạm thời chuyển mode
setenforce 0                         # Permissive (tạm tắt)
setenforce 1                         # Enforcing (bật lại)

# Vĩnh viễn: sửa /etc/selinux/config
# SELINUX=enforcing|permissive|disabled

# Troubleshoot
ausearch -m avc -ts recent           # Tìm denial gần đây
sealert -a /var/log/audit/audit.log  # Phân tích chi tiết
audit2why < /var/log/audit/audit.log # Giải thích denial
audit2allow -a                       # Gợi ý policy

# Context & Labels
ls -Z [file]                         # Xem SELinux context
chcon -t httpd_sys_content_t [file]  # Đổi context tạm
restorecon -Rv [path]                # Restore default context
semanage fcontext -a -t httpd_sys_content_t "/web(/.*)?"
restorecon -Rv /web

# Booleans
getsebool -a | grep httpd            # List booleans
setsebool -P httpd_can_network_connect on  # Bật boolean
```

## User & Permission Management

```bash
# User management
useradd -m -s /bin/bash [user]       # Tạo user
useradd -m -s /bin/bash -G wheel [user]  # Tạo + sudo
passwd [user]                        # Đặt mật khẩu
usermod -aG wheel [user]             # Thêm vào sudo group
userdel -r [user]                    # Xóa user + home
id [user]                            # Thông tin user
getent passwd [user]                 # Chi tiết từ /etc/passwd

# Sudo
visudo                               # Edit sudoers an toàn
echo "[user] ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/[user]

# File permissions
chmod 644 [file]                     # rw-r--r--
chmod 755 [dir]                      # rwxr-xr-x
chmod -R 750 [dir]                   # Recursive
chown user:group [file]              # Đổi owner
chown -R user:group [dir]

# ACL (nâng cao)
getfacl [file]                       # Xem ACL
setfacl -m u:[user]:rwx [file]       # Set ACL cho user
setfacl -m g:[group]:rx [dir]        # Set ACL cho group
setfacl -d -m u:[user]:rwx [dir]     # Default ACL (kế thừa)
```

## Disk & LVM Management

```bash
# Disk info
lsblk                               # Liệt kê block devices
fdisk -l                            # Partition table
df -hT                              # Disk usage + filesystem type
blkid                               # UUID của partitions

# LVM
pvs / pvdisplay                      # Physical volumes
vgs / vgdisplay                      # Volume groups
lvs / lvdisplay                      # Logical volumes

# Mở rộng LV (online resize)
lvextend -L +10G /dev/mapper/vg-lv   # Thêm 10GB
lvextend -l +100%FREE /dev/mapper/vg-lv  # Dùng hết free space
resize2fs /dev/mapper/vg-lv          # Ext4: mở rộng filesystem
xfs_growfs /dev/mapper/vg-lv         # XFS: mở rộng filesystem

# Thêm disk mới vào LVM
pvcreate /dev/sdb                    # Tạo PV
vgextend vg_name /dev/sdb            # Mở rộng VG
lvextend -l +100%FREE /dev/vg_name/lv_name
resize2fs /dev/vg_name/lv_name

# SWAP
dd if=/dev/zero of=/swapfile bs=1G count=4
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
echo '/swapfile none swap sw 0 0' >> /etc/fstab
```

## Networking (CentOS-specific)

```bash
# CentOS 7 (NetworkManager + ifcfg)
cat /etc/sysconfig/network-scripts/ifcfg-eth0
# Sửa: BOOTPROTO=static, IPADDR=, NETMASK=, GATEWAY=, DNS1=

# CentOS 8/9 (NetworkManager + nmcli preferred)
nmcli con show                       # Liệt kê connections
nmcli con show [name]                # Chi tiết
nmcli con mod [name] ipv4.addresses "10.0.0.5/24"
nmcli con mod [name] ipv4.gateway "10.0.0.1"
nmcli con mod [name] ipv4.dns "8.8.8.8 1.1.1.1"
nmcli con mod [name] ipv4.method manual
nmcli con up [name]                  # Apply

# Hostname
hostnamectl set-hostname [name]
```

## Cron & Scheduled Tasks

```bash
crontab -e                           # Edit crontab user hiện tại
crontab -l                           # Liệt kê
crontab -u [user] -e                 # Edit cho user khác

# Format: MIN HOUR DOM MON DOW COMMAND
# Ví dụ
0 2 * * * /root/backup.sh            # 2h sáng hàng ngày
*/5 * * * * /root/check.sh           # Mỗi 5 phút
0 0 * * 0 /root/weekly.sh            # Chủ nhật 0h

# Systemd timer (thay thế cron hiện đại)
systemctl list-timers --all          # Liệt kê timers
```

## Log Analysis

```bash
# Journald
journalctl -xe                       # Lỗi gần nhất (chi tiết)
journalctl --since "1 hour ago"
journalctl -p err                    # Chỉ error trở lên
journalctl --disk-usage              # Dung lượng log
journalctl --vacuum-size=500M        # Giới hạn 500MB
journalctl --vacuum-time=30d         # Xóa log >30 ngày

# Traditional logs
tail -f /var/log/messages            # CentOS 7
tail -f /var/log/syslog              # CentOS 8+ (nếu rsyslog)
tail -f /var/log/secure              # SSH + Auth logs
cat /var/log/yum.log                 # Package install log
last                                 # Login history
lastb                                # Failed login attempts
```

## Performance Tuning

```bash
# Tuned (CentOS performance profiles)
tuned-adm list                       # Liệt kê profiles
tuned-adm active                     # Profile hiện tại
tuned-adm profile throughput-performance  # Đổi profile
tuned-adm recommend                  # Gợi ý

# Sysctl tuning
sysctl -a | grep [param]             # Xem giá trị
sysctl -w net.ipv4.ip_forward=1      # Set tạm thời
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
sysctl -p                            # Apply

# Limits
ulimit -a                            # Xem limits hiện tại
cat /etc/security/limits.conf
# [user] soft nofile 65535
# [user] hard nofile 65535
```

## Backup & Recovery

```bash
# rsync
rsync -avzP /source/ /dest/          # Archive, verbose, compress
rsync -avzP -e "ssh -p 22" /local/ user@remote:/backup/

# tar
tar czf backup_$(date +%Y%m%d).tar.gz /path/to/backup
tar xzf backup.tar.gz -C /restore/path/

# LVM snapshot (backup live system)
lvcreate -L 5G -s -n snap /dev/vg/lv_root
mount /dev/vg/snap /mnt/snap
# ... backup từ /mnt/snap ...
umount /mnt/snap
lvremove /dev/vg/snap
```
