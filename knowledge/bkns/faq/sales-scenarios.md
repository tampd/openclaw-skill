# Kịch Bản Tư Vấn Bán Hàng BKNS

> Hướng dẫn cho AI tư vấn | Cập nhật: 2026-03-12

---

## Kịch bản 1: Khách cần website cho doanh nghiệp mới

**Câu hỏi mẫu:** "Tôi mới thành lập công ty, cần làm website"

**Decision Tree:**
1. Hỏi: "Website dùng WordPress hay custom code?"
2. Hỏi: "Dự kiến traffic bao nhiêu/ngày?"
3. Hỏi: "Có cần email theo tên miền không? (info@tencongty.vn)"

**Đề xuất combo:**

| Traffic | Đề xuất | Giá ước tính/tháng |
|---|---|---|
| < 500 views/ngày | Domain .com.vn + Hosting GR2 + Email Hosting 5 | ~350K + 37K + 45K = **~432K** |
| 500-2000 views/ngày | Domain .com.vn + Platinum BKCP03 + Email 20 + PositiveSSL | ~350K + 78K + 90K + 18K = **~536K** |
| 2000-10K views/ngày | Domain .com.vn + VPS VM03-VM04 + Email 50 + RapidSSL | ~350K + 220-340K + 175K + 18K = **~763K-883K** |
| > 10K views/ngày | Domain .com.vn + VPS VM06+ hoặc AMD | Tùy cấu hình |

> **Lưu ý**: Giá SSL/năm chia 12 để tính tháng. Giá domain/năm riêng.

---

## Kịch bản 2: Khách cần email doanh nghiệp

**Câu hỏi mẫu:** "Tôi cần email @tencongty.vn cho nhân viên"

**Decision Tree:**
1. Hỏi: "Công ty có bao nhiêu nhân viên cần email?"
2. Hỏi: "Có cần gửi email marketing hàng loạt không?"
3. Hỏi: "Đã có tên miền chưa?"

**Đề xuất:**

| Số nhân viên | Đề xuất | Giá/tháng |
|---|---|---|
| 1-5 | Email Hosting EMAIL 1 | 45,000đ |
| 6-20 | Email Hosting EMAIL 2 | 90,000đ |
| 21-50 | Email Hosting EMAIL 3 | 175,000đ |
| 51-100 | Email Hosting EMAIL 4 | 300,000đ |
| > 100 | Mini Email Server hoặc Full Email Server | Từ 369,000đ |
| + Marketing email | Thêm Email Relay | Từ 180,000đ |

> **Cross-sell**: Nếu chưa có domain → đề xuất mua domain .com.vn (350K/năm)

---

## Kịch bản 3: Khách cần VPS cho ứng dụng cụ thể

**Câu hỏi mẫu:** "Tôi cần VPS chạy [ứng dụng]"

**Mapping ứng dụng → gói:**

| Ứng dụng | Tối thiểu | Đề xuất | Lý do |
|---|---|---|---|
| WordPress (1 site) | VM01 (1C/1G) | VM02 (2C/2G) | WP + MySQL cần ≥2GB RAM |
| WordPress (nhiều site) | VM03 | VM04-VM05 | Multi-site cần thêm RAM |
| Node.js / Python app | VM02 | VM03 | Đủ cho app + DB nhỏ |
| PostgreSQL / MySQL nặng | VM04 (AMD) | EPYC 4-5 | AMD mạnh hơn cho DB |
| N8N (automation) | N8N-01 | N8N-02 | Cài sẵn, kèm domain .io.vn |
| Misa kế toán | BK01 | BK02 | Cài sẵn môi trường |
| Docker / DevOps | VM04 | VM06+ | Docker cần nhiều RAM |
| AI inference | EPYC 6+ | EPYC 7-8 | AMD EPYC tối ưu AI |
| SEO (nhiều IP) | SEO 01 | SEO 02 | IP khác class C |
| Game server | VM06+ | VM08 | Cần CPU+RAM cao |
| FTP / Backup storage | ST02-ST03 | ST04+ | Dung lượng lớn, giá rẻ/GB |

---

## Kịch bản 4: Khách muốn bảo mật SSL

**Câu hỏi mẫu:** "Website tôi cần SSL", "Cần chứng chỉ bảo mật"

**Decision Tree:**
1. Hỏi: "Website cá nhân/blog hay doanh nghiệp?"
2. Hỏi: "Có cần bảo vệ nhiều subdomain (*.domain.com) không?"
3. Hỏi: "Có xử lý thanh toán/giao dịch tài chính không?"

**Đề xuất:**

| Nhu cầu | Đề xuất | Giá/năm |
|---|---|---|
| Blog, web cá nhân | RapidSSL hoặc PositiveSSL (DV) | ~215K |
| DN nhỏ, 1 domain | Sectigo OV SSL | 2,038K |
| DN, nhiều subdomain | PositiveSSL Wildcard (DV) | 2,413K |
| DN vừa, cổng thanh toán | GeoTrust True BusinessID (OV) | 2,172K |
| Ngân hàng, tài chính | Comodo EV SSL | 5,782K |
| Exchange Server | Comodo UCC (OV) | 3,037K |

> **Lưu ý**: Hosting Platinum BKNS đã có **SSL miễn phí** (Let's Encrypt). Chỉ cần mua SSL trả phí khi cần OV/EV hoặc warranty.

---

## Kịch bản 5: Khách muốn chuyển từ nhà cung cấp khác

**Câu hỏi mẫu:** "Tôi muốn chuyển hosting/VPS sang BKNS"

**Checklist tư vấn:**
1. ✅ Transfer tên miền về BKNS: **Miễn phí** (cả VN và quốc tế)
2. ✅ Hỗ trợ migrate dữ liệu: Liên hệ support 24/7
3. ✅ Dùng thử 7 ngày miễn phí (một số dịch vụ)
4. ✅ Hoàn tiền 100% nếu không hài lòng
5. 💡 So sánh giá với nhà cung cấp cũ → tra bảng giá tương ứng

---

## Kịch bản 6: Khách hỏi giá dài hạn / tính chi phí

**Câu hỏi mẫu:** "VPS VM04 giá bao nhiêu 1 năm?", "Hosting 3 năm hết bao nhiêu?"

**Quy trình:**
1. Tra giá tháng từ bảng giá tương ứng
2. Áp dụng chiết khấu: tra bảng chiết khấu trong file pricing hoặc `promotions.md`
3. Format câu trả lời:

```
💰 VPS VM04 — Giá theo thời hạn:
├── 1 tháng: 340,000đ
├── 3 tháng: 1,020,000đ (340K × 3)
├── 6 tháng: 1,938,000đ (-5%)
├── 12 tháng: 3,468,000đ (-15%) ⭐ Phổ biến
├── 24 tháng: 6,120,000đ (-25%)
├── 36 tháng: 7,956,000đ (-35%)
└── 60 tháng: 11,220,000đ (-45%) 💰 Tiết kiệm nhất

📌 Giá chưa VAT. Kiểm tra giá mới nhất: bkns.vn
```

---

## Quy tắc cross-sell / upsell

| Đang mua | Gợi ý thêm | Lý do |
|---|---|---|
| **Domain** | Hosting + Email + SSL | Cần host website + email chuyên nghiệp |
| **Hosting** | Domain + SSL + Email | Trọn bộ web DN |
| **VPS** | Domain + SSL + DirectAdmin | VPS cần panel quản lý |
| **Email Hosting** | Domain (nếu chưa có) | Email cần tên miền |
| **VPS nhỏ (VM01-02)** | Nâng cấp VM03-04 | Tránh thiếu tài nguyên |
| **Hosting nhỏ** | Nâng lên VPS nếu traffic tăng | Scalability |
