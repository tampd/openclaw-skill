# So Sánh Chi Tiết Dịch Vụ BKNS

> Hướng dẫn cho tư vấn viên | Cập nhật: 2026-03-12

---

## 1. VPS: VM Intel vs AMD EPYC vs Giá Rẻ vs Siêu Rẻ

| Tiêu chí | VPS Siêu Rẻ | VPS Giá Rẻ (MMO) | Cloud VPS VM | Cloud VPS AMD |
|---|---|---|---|---|
| **Giá từ** | **69K** | ~70K | 140K | 165K |
| **CPU** | Intel | Intel | Intel | AMD EPYC™ |
| **Storage** | SSD | SSD | SSD NVMe | NVMe |
| **Bandwidth** | ⚠️ Giới hạn (0.5-5TB) | ✅ Unlimited | ✅ Unlimited | ✅ Unlimited |
| **Upload** | — | — | 100-200Mbps | 100-200Mbps |
| **Download** | — | — | 500Mbps | 500Mbps |
| **Network** | — | — | 10Gbps | 10Gbps |
| **IPv4** | Private | VN Private | 1 public | 1 public |
| **IPv6** | Public | /56 | — | — |
| **Chiết khấu dài hạn** | Không | 3/6/12T | Tới -45% (60T) | Tới -45% (60T) |
| **Add-ons** | Rẻ nhất (CPU 50K) | Rẻ (CPU 50K) | TB (CPU 105K) | Cao (CPU 150K) |
| **Backup** | Tuần/lần | — | — | — |
| **Target** | MMO, dev/test, traffic thấp | MMO, web nhỏ, tool | Web DN, đa năng | Workload nặng, DB, AI |

### Kết luận nhanh cho tư vấn:
- **Budget thấp nhất, traffic ít** → VPS Siêu Rẻ (VPSTK)
- **MMO, automation, tool** → VPS Giá Rẻ (MMO) hoặc Siêu Rẻ
- **Website DN, ổn định** → Cloud VPS VM ⭐ (phổ biến nhất)
- **Database nặng, AI, rendering** → Cloud VPS AMD
- **Chuyên SEO** → VPS SEO (IP khác class C)
- **Kế toán Misa** → BK Misa (SSD+HDD, cài sẵn)
- **Automation n8n** → VPS N8N (cài sẵn n8n)

---

## 2. Hosting: Platinum vs Giá Rẻ vs WordPress vs Windows

| Tiêu chí | Hosting Miễn Phí | Giá Rẻ | Platinum | WordPress | Windows |
|---|---|---|---|---|---|
| **Giá từ** | **0đ** | **19K** | **29K** | **50K** | **33K** |
| **Storage** | — | SSD Ent. | NVMe U.2 ⭐ | SSD | SSD |
| **CPU** | — | 1-6 Core | Intel Xeon Pt. | — | — |
| **RAM** | — | 1-6 GB | 1-8 GB | — | — |
| **Web Server** | — | LiteSpeed | LiteSpeed ⭐ | — | IIS |
| **CloudLinux** | — | ✅ | ✅ | — | — |
| **SSL miễn phí** | — | ✅ | ✅ | — | — |
| **Domain** | — | 1-6 | 1-10 | 2-15 | 1-15 |
| **Backup** | — | Định kỳ | 1 lần/ngày ⭐ | — | — |
| **Tính năng ĐB** | — | — | Redis, JetBackup | WP optimized | ASP.NET, MSSQL |
| **Target** | Học tập, test | Blog, DN nhỏ | DN vừa ⭐ | WordPress | .NET apps |

### Kết luận nhanh:
- **Tập tành, thử nghiệm** → Hosting Miễn Phí
- **Blog cá nhân, portfolio** → Giá Rẻ (GR1, 19K)
- **Website DN, tốc độ cao** → Platinum ⭐ (phổ biến nhất)
- **WordPress thuần** → WordPress Hosting
- **Ứng dụng .NET** → Windows Hosting
- **SEO đa site** → SEO Hosting
- **Reseller** → Reseller Hosting cPanel

---

## 3. Email: Hosting vs Server Mini vs Server Full vs Relay

| Tiêu chí | Email Hosting | Mini Email Server | Full Email Server | Email Relay |
|---|---|---|---|---|
| **Giá từ** | **45K** | **369K** | **870K** | **180K** |
| **Số user** | 5-100 | Unlimited | Unlimited | — |
| **Dung lượng** | 5GB/email | 100-255 GB | 300GB-2TB | — |
| **Quản lý** | BKNS quản lý | Toàn quyền | Toàn quyền | — |
| **Mục đích** | Gửi/nhận DN | Server riêng nhỏ | Server riêng lớn | Marketing email |
| **Email/ngày** | — | — | — | 350-30,000 |
| **Target** | DN nhỏ-vừa | DN vừa | DN lớn, ISP | Marketing |

### Kết luận nhanh:
- **DN < 20 nhân viên** → Email Hosting (gói EMAIL 1 hoặc 2)
- **DN 20-100 nhân viên** → Email Hosting (gói EMAIL 3-4)
- **DN vừa, cần toàn quyền** → Mini Email Server
- **DN lớn, ISP** → Full Email Server
- **Gửi newsletter, marketing** → Email Relay

---

## 4. SSL: DV vs OV vs EV

| Tiêu chí | DV | OV | EV |
|---|---|---|---|
| **Giá từ** | **215K** | **2,038K** | **5,782K** |
| **Xác thực** | Chỉ tên miền | DN + giấy tờ | Nghiêm ngặt nhất |
| **Thời gian cấp** | 5-15 phút | 1-3 ngày | 1-5 ngày |
| **Hiển thị** | 🔒 HTTPS | 🔒 + Tên DN | 🔒 + Tên DN nổi bật |
| **Bảo hiểm** | Tới 500K USD | Tới 1.75M USD | Tới 2M USD |
| **Target** | Blog, startup | DN, thanh toán | Ngân hàng, tài chính |

### Kết luận nhanh:
- **Web cá nhân, blog** → RapidSSL hoặc PositiveSSL (DV, ~215K)
- **Web DN vừa** → GeoTrust True BusinessID (OV, 2.17M)
- **DN lớn, thanh toán online** → Comodo EV SSL (5.78M)
- **Nhiều subdomain** → Wildcard (từ PositiveSSL WC 2.41M)
- **Nhiều domain** → Multi-Domain hoặc UCC
- **Ký phần mềm** → Code Signing (từ 12.4M)
