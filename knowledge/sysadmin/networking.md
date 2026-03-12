# Networking — Cross-Platform Cheat Sheet Chuyên Gia

> Áp dụng: Linux (CentOS, Ubuntu) + Windows (10/11, Server)
> Cập nhật: 2026-03-12

## Diagnostics — Lệnh Cơ Bản

| Mục đích | Linux | Windows (PowerShell/CMD) |
|---|---|---|
| IP address | `ip a` / `ip addr show` | `Get-NetIPAddress` / `ipconfig /all` |
| Routing table | `ip r` / `ip route` | `Get-NetRoute` / `route print` |
| DNS resolution | `dig google.com` / `nslookup` | `Resolve-DnsName` / `nslookup` |
| Ping | `ping -c 4 8.8.8.8` | `Test-Connection 8.8.8.8 -Count 4` |
| Port check | `ss -tulpn` / `netstat -tlnp` | `Get-NetTCPConnection` / `netstat -an` |
| Traceroute | `traceroute 8.8.8.8` / `mtr` | `Test-NetConnection -TraceRoute` / `tracert` |
| Port test | `nc -zv host 80` / `curl -I` | `Test-NetConnection host -Port 80` |
| ARP table | `ip neigh` / `arp -a` | `Get-NetNeighbor` / `arp -a` |
| DNS config | `cat /etc/resolv.conf` | `Get-DnsClientServerAddress` |
| Interface stats | `ip -s link` | `Get-NetAdapterStatistics` |

## IP / Subnet Cheat Sheet

| CIDR | Netmask | Hosts | Dùng cho |
|---|---|---|---|
| /32 | 255.255.255.255 | 1 | Single host |
| /30 | 255.255.255.252 | 2 | Point-to-point |
| /29 | 255.255.255.248 | 6 | Nhóm nhỏ |
| /28 | 255.255.255.240 | 14 | Small LAN |
| /27 | 255.255.255.224 | 30 | Department |
| /26 | 255.255.255.192 | 62 | Floor |
| /25 | 255.255.255.128 | 126 | Building |
| /24 | 255.255.255.0 | 254 | Standard LAN |
| /23 | 255.255.254.0 | 510 | Large LAN |
| /22 | 255.255.252.0 | 1022 | Campus |
| /16 | 255.255.0.0 | 65,534 | Enterprise |
| /8 | 255.0.0.0 | 16M+ | Class A |

### Private IP Ranges (RFC 1918)
| Range | CIDR | Dùng phổ biến |
|---|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | Enterprise, Cloud VPC |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | Docker, internal |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | Home/SMB |

## Firewall — Linux

### iptables (Legacy — CentOS 6, Ubuntu <20)
```bash
# List rules
iptables -L -n -v
iptables -L -n --line-numbers

# Allow SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP/HTTPS
iptables -A INPUT -p tcp -m multiport --dports 80,443 -j ACCEPT

# Allow từ subnet
iptables -A INPUT -s 10.0.0.0/8 -j ACCEPT

# Block IP
iptables -A INPUT -s 1.2.3.4 -j DROP

# Default deny
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow established connections (⚠️ QUAN TRỌNG — thêm TRƯỚC default deny)
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -i lo -j ACCEPT

# Save
iptables-save > /etc/iptables/rules.v4        # Ubuntu
service iptables save                          # CentOS 7

# Delete rule
iptables -D INPUT [line-number]
```

### nftables (Modern — CentOS 8+, Ubuntu 22+)
```bash
# List
nft list ruleset

# Add table
nft add table inet filter

# Add chain
nft add chain inet filter input { type filter hook input priority 0 \; policy drop \; }

# Rules
nft add rule inet filter input ct state established,related accept
nft add rule inet filter input iif lo accept
nft add rule inet filter input tcp dport 22 accept
nft add rule inet filter input tcp dport { 80, 443 } accept

# Save
nft list ruleset > /etc/nftables.conf
```

### firewalld (CentOS — xem linux-centos.md)
### ufw (Ubuntu — xem linux-ubuntu.md)

## Firewall — Windows

```powershell
# List rules
Get-NetFirewallRule | Where Enabled -eq True | Select DisplayName, Direction, Action, Profile

# Allow inbound
New-NetFirewallRule -DisplayName "Allow HTTP" -Direction Inbound -Protocol TCP -LocalPort 80 -Action Allow
New-NetFirewallRule -DisplayName "Allow App" -Direction Inbound -Program "C:\app\app.exe" -Action Allow

# Block
New-NetFirewallRule -DisplayName "Block Telnet" -Direction Inbound -Protocol TCP -LocalPort 23 -Action Block

# Remove
Remove-NetFirewallRule -DisplayName "Allow HTTP"

# Profiles
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
Get-NetFirewallProfile | Select Name, Enabled, DefaultInboundAction

# Advanced: logging
Set-NetFirewallProfile -LogFileName "C:\Windows\system32\LogFiles\Firewall\pfirewall.log" -LogMaxSizeKilobytes 4096 -LogAllowed True -LogBlocked True
```

## VPN

### Linux — WireGuard
```bash
# Cài đặt
apt install wireguard       # Ubuntu
dnf install wireguard-tools # CentOS 8+

# Generate keys
wg genkey | tee privatekey | wg pubkey > publickey

# Config: /etc/wireguard/wg0.conf
[Interface]
PrivateKey = [SERVER_PRIVATE_KEY]
Address = 10.100.0.1/24
ListenPort = 51820

[Peer]
PublicKey = [CLIENT_PUBLIC_KEY]
AllowedIPs = 10.100.0.2/32

# Start
wg-quick up wg0
systemctl enable wg-quick@wg0

# Status
wg show
```

### Linux — OpenVPN
```bash
# Cài đặt nhanh (script)
curl -O https://raw.githubusercontent.com/angristan/openvpn-install/master/openvpn-install.sh
chmod +x openvpn-install.sh
./openvpn-install.sh

# Quản lý
systemctl status openvpn-server@server
journalctl -u openvpn-server@server -f
```

### Windows — Built-in VPN
```powershell
# Tạo VPN connection
Add-VpnConnection -Name "Office VPN" -ServerAddress "vpn.company.com" -TunnelType L2tp -L2tpPsk "SharedSecret" -AuthenticationMethod Pap -RememberCredential
Get-VpnConnection
rasdial "Office VPN" username password   # Connect
rasdial "Office VPN" /disconnect          # Disconnect
```

## Port Forwarding & NAT

### Linux (iptables)
```bash
# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward
# Permanent: sysctl -w net.ipv4.ip_forward=1

# DNAT (Port forward external → internal)
iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT --to-destination 10.0.0.50:80

# SNAT / Masquerade
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# SSH Tunnel (port forward qua SSH)
ssh -L 3306:db-server:3306 user@jump-host    # Local forward
ssh -R 8080:localhost:80 user@remote          # Reverse forward
ssh -D 1080 user@proxy                        # SOCKS proxy
```

### Windows
```powershell
# Port proxy (built-in)
netsh interface portproxy add v4tov4 listenport=8080 listenaddress=0.0.0.0 connectport=80 connectaddress=10.0.0.50
netsh interface portproxy show all
netsh interface portproxy delete v4tov4 listenport=8080 listenaddress=0.0.0.0
```

## Packet Capture

### Linux
```bash
# tcpdump
tcpdump -i eth0                              # All traffic
tcpdump -i eth0 port 80                      # HTTP only
tcpdump -i eth0 host 10.0.0.5               # Specific host
tcpdump -i eth0 -w capture.pcap              # Save to file
tcpdump -i eth0 -c 100 port 443             # 100 packets on HTTPS
tcpdump -i eth0 'tcp[tcpflags] & (tcp-syn) != 0'  # SYN only

# ngrep (grep for network)
ngrep -d eth0 -W byline "GET|POST" port 80
```

### Windows
```powershell
# Built-in packet capture
netsh trace start capture=yes tracefile=C:\trace.etl maxsize=200
netsh trace stop
# Mở file .etl bằng Microsoft Message Analyzer hoặc Wireshark (convert)

# pktmon (Windows Server 2019+, Win 10 2004+)
pktmon start --etw -p 0 -c 13
pktmon stop
pktmon format PktMon.etl -o capture.txt
```

## Bandwidth & Performance

```bash
# Linux
iperf3 -s                                    # Server mode
iperf3 -c [server-ip]                        # Client test
iperf3 -c [server-ip] -R                     # Reverse (download)

# Bandwidth monitoring
nload                                        # Real-time
iftop                                        # Per-connection
vnstat                                       # Historical
nethogs                                      # Per-process

# Speed test
curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3
```

## DNS Deep Dive

```bash
# Linux
dig google.com                               # Full query
dig google.com +short                        # IP only
dig @8.8.8.8 google.com                      # Specific DNS server
dig google.com MX                            # MX records
dig google.com ANY                           # All records
dig -x 8.8.8.8                              # Reverse lookup
dig google.com +trace                        # Full resolution path

# Test DNS propagation
for ns in 8.8.8.8 1.1.1.1 9.9.9.9; do echo "==$ns=="; dig @$ns example.com +short; done
```

```powershell
# Windows
Resolve-DnsName google.com
Resolve-DnsName google.com -Type MX
Resolve-DnsName -Name 8.8.8.8 -Type PTR      # Reverse
nslookup -type=ANY google.com
Clear-DnsClientCache
Get-DnsClientCache
```

## Common Port Reference

| Port | Service | Protocol |
|---|---|---|
| 20/21 | FTP | TCP |
| 22 | SSH / SFTP | TCP |
| 25 | SMTP | TCP |
| 53 | DNS | TCP/UDP |
| 80 | HTTP | TCP |
| 110 | POP3 | TCP |
| 143 | IMAP | TCP |
| 443 | HTTPS | TCP |
| 445 | SMB | TCP |
| 587 | SMTP (submission) | TCP |
| 993 | IMAPS | TCP |
| 995 | POP3S | TCP |
| 1433 | MSSQL | TCP |
| 3306 | MySQL | TCP |
| 3389 | RDP | TCP |
| 5432 | PostgreSQL | TCP |
| 5900 | VNC | TCP |
| 6379 | Redis | TCP |
| 8080 | HTTP Alt | TCP |
| 8443 | HTTPS Alt | TCP |
| 27017 | MongoDB | TCP |
| 51820 | WireGuard | UDP |
